#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import os.path
import shlex
import subprocess
import sys
import threading
import time
from bottle import request, route, run, static_file
from daemonize import Daemonize
from env import ffmpeg_path, host, interval_sec, log_format, log_level, port, timeout_sec
from setproctitle import setproctitle

INSTANCE_DICT = dict()
DEFAULT_IMAGE_PATH = '%s/image/black_screen.jpg' % sys.path[0]

logger = logging.getLogger('sme')
_lock = threading.Lock()


class LiveStreamJob(object):
    def __init__(self, app, instance):
        self._app = app
        self._instance = instance

        self._running = False
        self._last_start_time = None
        self._last_stop_time = None
        self._last_result = None
        self._subprocess = None

    @property
    def key(self):
        return '%s/%s' % (self._app, self._instance)

    @property
    def app(self):
        return self._app

    @property
    def instance(self):
        return self._instance

    @property
    def running(self):
        return self._running

    @running.setter
    def running(self, running):
        self._running = running

    @property
    def last_start_time(self):
        return self._last_start_time

    @last_start_time.setter
    def last_start_time(self, last_start_time):
        self._last_start_time = last_start_time

    @property
    def last_stop_time(self):
        return self._last_stop_time

    @last_stop_time.setter
    def last_stop_time(self, last_stop_time):
        self._last_stop_time = last_stop_time

    @property
    def last_result(self):
        return self._last_result

    @last_result.setter
    def last_result(self, last_result):
        self._last_result = last_result

    @property
    def subprocess(self):
        return self._subprocess

    @subprocess.setter
    def subprocess(self, subprocess):
        self._subprocess = subprocess


def call_extractor(job):
    """ 执行抽帧任务 """
    logger.debug("抽帧任务 key: %s", job.key)
    images_folder_path = "%s/images/%s" % (sys.path[0], job.app)
    if not os.path.exists(images_folder_path):
        logger.debug("创建目录: %s", images_folder_path)
        os.makedirs(images_folder_path)
    command_line = generate_command_line(job)
    # args = shlex.split(command_line)
    job.last_start_time = int(time.time())

    class Extractor(threading.Thread):
        def __init__(self, name, target):
            threading.Thread.__init__(self, name='extractor-' + name)
            self._target = target
            self.setDaemon(True)

        def run(self):
            try:
                self._target.subprocess = subprocess.Popen(command_line, shell=True)
            except Exception, e:
                logger.exception('执行子进程时发生异常: %s', e)
                self._target.running = False

    job.running = True
    INSTANCE_DICT[job.key] = job
    Extractor(job.key, job).start()


def generate_rtmp_url(job):
    """ 生成RTMP播放串 """
    return "rtmp://%s.ip.%s/%s/%s" % (job.instance, job.app, job.app, job.instance)


def generate_image_path(app, instance):
    """ 获取图片路径 """
    return "%s/images/%s/%s.jpg" % (sys.path[0], app, instance)


def generate_command_line(job):
    """ 生成抽帧命令行 """
    rtmp_url = generate_rtmp_url(job)
    image_path = generate_image_path(job.app, job.instance)
    return "%s -y -i %s -vf scale=320:-1 -f image2 -r 1 -frames 1 -update 1 %s >/dev/null 2>&1" % (
        ffmpeg_path, rtmp_url, image_path)


@route('/<app:re:.*>/<instance:re:.*>.jpg')
def image(app, instance):
    logger.info('request path: %s', request.path)
    logger.debug('app: %s', app)
    logger.debug('instance: %s', instance)
    now = int(time.time())

    try:
        _lock.acquire(True)
        job = LiveStreamJob(app, instance)
        if job.key in INSTANCE_DICT:  # 之前执行过该任务
            job = INSTANCE_DICT[job.key]
            if job.running:  # 任务正在执行
                logger.debug("任务正在运行. key: %s", job.key)
            elif job.last_stop_time is not None and job.last_stop_time + interval_sec > now:  # 还没有到间隔时间
                logger.debug("任务处于冷冻期. key: %s, 距离上次运行结束: %d 秒", job.key, now - job.last_stop_time)
            else:
                call_extractor(job)
        else:  # 之前没有执行过该任务
            call_extractor(job)
    except Exception, e:
        logger.exception("请求图片 %s 发生异常: %s", request.path, e)
    finally:
        _lock.release()

    image_path = generate_image_path(app, instance)  # 抽帧图片绝对路径
    logger.debug('请求的图片在磁盘上的绝对地址为 %s', image_path)
    if not os.path.exists(image_path):  # 如果抽帧图片不存在
        image_path = DEFAULT_IMAGE_PATH
        logger.debug('图片不存在, 使用默认图片 %s', image_path)

    return static_file(image_path, root='/')


class Monitor(threading.Thread):
    """ 任务监控线程 """

    def __init__(self):
        threading.Thread.__init__(self, name='extractor-monitor')
        self.setDaemon(True)

    def run(self):
        while True:
            now = int(time.time())
            try:
                _lock.acquire(True)
                for (k, v) in INSTANCE_DICT.items():
                    if v.subprocess:  # 任务已经启动
                        rc = v.subprocess.poll()  # 判断任务是否结束
                        if rc is not None:  # 不为None说明抽帧任务已经结束
                            logger.debug('检测到抽帧任务 %s 已经结束, 返回码 %d', k, rc)
                            v.last_stop_time = now
                            v.last_result = rc
                            v.subprocess = None
                            v.running = False  # 标记抽帧任务已经结束
                        elif v.last_start_time is not None and v.last_start_time + timeout_sec > now:
                            logging.debug("检测到当前任务 %s 超时，系统自动kill" ,k)
                            v.terminate()
            except Exception, e:
                logger.exception("检测抽帧任务发生异常: %s", e)
            finally:
                _lock.release()
            logger.debug('dummy...')
            time.sleep(1)


def start():
    monitor = Monitor()
    monitor.start()  # 启动monitor线程
    try:
        run(host=host, port=port)  # 启动server
    except Exception, e:
        logger.exception("启动Server发生异常: %s", e)


def main():
    setproctitle('sme')
    pid = sys.path[0] + '/sme.pid'

    fmt = logging.Formatter(log_format)

    root_logger = logging.getLogger()
    root_logger.setLevel(log_level)

    file_handler = logging.FileHandler(sys.path[0] + '/sme.log')
    file_handler.setFormatter(fmt)
    root_logger.addHandler(file_handler)

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(fmt)
    root_logger.addHandler(stream_handler)

    keep_fds = [file_handler.stream.fileno()]
    daemon = Daemonize(app='sme', pid=pid, action=start, keep_fds=keep_fds, logger=logger)
    daemon.start()


if __name__ == '__main__':
    main()
