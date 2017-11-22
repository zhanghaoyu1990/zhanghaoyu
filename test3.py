#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from time import *
from kazoo.client import KazooClient
from samsa.cluster import Cluster
# class Fibs(object):
#     def __init__(self):
#         self.a = 0
#         self.b = 1
#
#     def next(self):
#         self.a, self.b = self.b, self.a + self.b
#         return self.a
#
#     def __iter__(self):
#         return self
#
# fibs = Fibs()
# for f in fibs:
#     if f > 1000:
#         print f
#         break
#
# it = iter([1, 2, 3, 4])
# print it.next()
# print it.next()

# class Fab(object):
#
#     def __init__(self, max):
#         self.max = max
#         self.n, self.a, self.b = 0, 0, 1
#
#     def __iter__(self):
#         return self
#
#     def next(self):
#         if self.n < self.max:
#             r = self.b
#             self.a, self.b = self.b, self.a + self.b
#             self.n += 1
#             return r
#         raise StopIteration()
#
# for n in Fab(100):
#     print n


#
#  def fab(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         yield b
#         a, b = b, a+b
#         n += 1
#
# print [x for x in fab(30)]


##  print [x for x in dir(fileinput) if not x.startswith('_')]
#
# # for line in fileinput.input('ag/requirements.txt'):
# #     print fileinput.filename(),'|','Line Number:',fileinput.lineno(),'|: ',line
# print fileinput.input('ag/requirements.txt').next()
# print fileinput.filename()

# def process(line):
#     return line.rstrip() + ' line'
#
# for line in fileinput.input(['1.txt', '2.txt'], inplace=1):
#     print process(line)

#!/usr/bin/python
#coding:utf-8

#author:	gavingeng
#date:		2011-12-03 10:50:01

# class Person:
#
#     def __init__(self):
#         print "init"
#
#     @staticmethod
#     def sayHello(hello):
#         if not hello:
#             hello='hello'
#             print "i will sya %s" %hello
#
#     @classmethod
#     def introduce(clazz,hello):
#         clazz.sayHello(hello)
#         print "from introduce method"
#
#     def hello(self,hello):
#         self.sayHello(hello)
#         print "from hello method"
#
#
# def main():
#     Person.sayHello("haha")
#     Person.introduce("hello world!")
#     #Person.hello("self.hello")	#TypeError: unbound method hello() must be called with Person instance as first argument (got str instance instead)
#
#     print "*" * 20
#     p = Person()
#     p.sayHello("haha")
#     p.introduce("hello world!")
#     p.hello("self.hello")
#
# if __name__=='__main__':
#     main()

# sleep(1)
# print u"第一次调用时间 %d" % clock()
# sleep(1)
# print u"第二次调用时间 %d" % clock()
# sleep(1)
# print u"第三次调用时间 %d" % clock()

print strftime("%a %d %b %H:%M:%S %Y", localtime())
print strftime("%Y年 %H:%M:%S",gmtime())

mount_path = '/opt/sp'
files_path = 'data/h265'
dsts_path = 'encode'
task ='/opt/sp/sp1/data/h265/asdd.mp4'
# transcode_param = '-c:a mp2 -b:a 128k -c:v libx265 -s 3840x2160 -aspect 16:9 -b:v 15000k -minrate 8000k -maxrate 30000k' \
#                   ' -g 50 -r 25 -refs 4 -bf 1 -x265-params no-mixed-refs:analyse=0x1,0:ratetol=0.2:nal-hrd=vbr:b-adapt' \
#                   '=0:no-weightb:keyint=50:min-keyint=50:no-scenecut -f mpegts'
transcode_path = '/data/transcode_temp'
# print task.find(files_path)
# print task[len(mount_path)+1:task.find(files_path)-1]
# def transcode(task):
#     dst_path = '%s_15M_VBR_H265.ts' % task[task.rfind('/')+1:][:task[task.rfind('/')+1:].rfind('.')]
#     dst_path = '%s/%s/ecode/%s' % (transcode_path, task[len(mount_path)+1:task.find(files_path)-1], dst_path)
#     transcode_commond = "/opt/onewave/ffmpeg/ffmpeg-2.6-64bit-static/ffmpeg -i %s %s -c %s" % (task, transcode_param, dst_path)
#     return transcode_commond
#
# dst_path = '%s_15M_VBR_H265.ts' % task[task.rfind('/')+1:][:task[task.rfind('/')+1:].rfind('.')]
# print dst_path
# print transcode(task)
# dst_path = '%s/%s/ecode/%s' % (transcode_path, task[len(mount_path)+1:task.find(files_path)-1], dst_path)
#
# print dst_path
# save_path = '%s/%s/encode/' % (mount_path, task[len(mount_path)+1:task.find(files_path)-1])
# save_file = 'mv %s %s' % (dst_path, save_path)
# print save_file
# dst_path = '%s_15M_VBR_H265.ts' % task[task.rfind('/')+1:][:task[task.rfind('/')+1:].rfind('.')]
# abs_path = '%s/%s/encode/%s' % (transcode_path, task[len(mount_path)+1:task.find(files_path)-1], dst_path)
# print abs_path
# file_size = os.path.getsize(abs_path) + 'bytes'
# save_path = '/encode/%s' % dst_path
# times = '%s' % (strftime("%a %d %b %H:%M:%S %Y", localtime()))
# task = '/encode/%s' % dst_path
# msg = '%s [pid 30092] [stcloud] OK UPLOAD: Client "172.30.21.34","%s",%s,5939.84Kbyte/sec' % (times, save_path, file_size)
# print msg
dst_path = '%s_15M_VBR_H265.ts' % task[task.rfind('/')+1:][:task[task.rfind('/')+1:].rfind('.')]
abs_path = '%s/%s/%s/%s' % (transcode_path, task[len(mount_path)+1:task.find(files_path)-1], dsts_path, dst_path)
# file_size = str(os.path.getsize(abs_path)) + 'bytes'
user = task[len(mount_path)+1:task.find(files_path)-1]
save_path = '/%s/%s' % (dsts_path, dst_path)
times = '%s' % (strftime("%a %d %b %H:%M:%S %Y", localtime()))
msg = '%s [pid 30092] [%s] OK UPLOAD: Client "172.30.21.34","%s",5939.84Kbyte/sec' % (times, user, save_path)
print msg
