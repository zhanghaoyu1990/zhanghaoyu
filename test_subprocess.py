#!/usr/bin/env python
# -*- coding: utf-8 -*-

import shlex, subprocess, time, threading
from bottle import *

class Subprocess(object):
    def __init__(self, app, instance):
        self._app = app
        self._instance = instance
        self._starttime = None
        self._endtime = None
        self._result = None
        self._subprocess = None

    @property
    def key(self):
        return '%s/%s' % (self._app, self._instance)

    @property
    def starttime(self):
        return self._starttime

    @starttime.setter
    def starttime(self,starttime):
        self._starttime = starttime

    @property
    def endtime(self):
        return self._endtime

    @endtime.setter
    def endtime(self,endtime):
        self._endtime = endtime

    @property
    def result(self):
        return self.result

    @result.setter
    def result(self,result):
        self._result = result

    @property
    def subprocess(self):
        return self._subprocess

    @subprocess.setter
    def subprocess(self,subprocess):
        self._subprocess = subprocess

jobs = dict()

def generate_rtmp_url(sub):
    """ 生成RTMP播放串 """
    return "rtmp://%s.ip.%s/%s/%s" % (sub.instance, sub.app, sub.app, sub.instance)

def generate_command_line(sub):
    """ 生成抽帧命令行 """
    rtmp_url = generate_rtmp_url(sub)
    return "%s -y -i %s -vf scale=320:-1 -f image2 -r 1 -frames 1 -update 1 %s/images/%s.jpg" % (
        "/opt/ffmpeg", rtmp_url, sys.path[0], sub.key)

def extract(sub):
    """ 模拟抽帧动作 """
    # print "新增任务 %s" % k
    command_line = generate_command_line(sub)
    args = shlex.split(command_line)
    sub.endtime= int(time.time())
    sub.subprocess = subprocess.Popen(args, stderr=subprocess.PIPE)  # 启动子进程
    jobs[sub.key] = sub

class Monitor(threading.Thread):
    """ 任务监控 """
    def __init__(self):
        threading.Thread.__init__(self)
        self.setDaemon(True)

    def run(self):
        while True:
            now = time.time()
            for (k,v) in jobs.items():
                returnCode = v.poll()  # 判断任务是否结束
                if returnCode is not None:
                    v.e = now
                    v.last_result = returnCode
                    v.subprocess = None
                    print "任务结束 %s, %d" % (k, returnCode)

            time.sleep(1)

# monitor = Monitor()
# monitor.start()

# for i in range(10):
#     extract("xdddt-%d" % i)
#     time.sleep(5)
#
# while True:
#     time.sleep(1)


@route('/<app>/<instance>/<filepath:path>')
def server_static(app,instance,filepath):
    sub = Subprocess(app,instance)
    now = int(time.time())
    if sub.key in jobs:
        sub = jobs[sub.key]
        if sub.subprocess is not None:
            return static_file(filepath, root=app+"/"+instance+"/")
        elif sub.endtime is not None and sub.endtime + 5 > now:
            return static_file(filepath, root=app+"/"+instance+"/")
        else:
            extract(sub)
    else:
        extract(sub)
    return static_file(filepath, root=app+"/"+instance+"/")

@error(404)
def error404(error):
    print error
    return '图片不存在，请稍后查看.'


def main():
    monitor = Monitor()
    monitor.start()
    run(host='localhost', port=8080)
if __name__ == '__main__':
    main()