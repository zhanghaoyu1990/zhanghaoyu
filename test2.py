#!/usr/bin/env python
# -*- coding: utf-8 -*-

# a = [1,2,3,4,5]
# b = map(lambda x: x**2, a)
# print type(b)
# print b
# for x in b:
#     print x
# c = [x for x in b]
# print c
# import socket, struct
# ip = '103.16.126.89'
#

#
# def _ip2long(_ip):
#         return struct.unpack("!L", socket.inet_aton(_ip))[0]
#
#
# def _str2long(s):
#     ii = 0
#     for _ in range(len(s)):
#         ii = (ii << 8) + ord(s[_])
#     return ii
#
# _key = _str2long('tlvp')
# print "_key:", _key
# _ip = _ip2long(ip)
# print "_ip:", _ip
# _xor_ip = _ip ^ _key
# print "_xor_ip:", _xor_ip
# _pre_xo_rip = str(_xor_ip)[0:4]
# print "_pre_xo_rip:", _pre_xo_rip
#
#
# returns = "%s%d" % (_pre_xo_rip, _ip)
# print returns
#
# sp = 'zhy-zhy'
# sp = sp + '-etag'
# print sp
# import sys
# import getopt
# opts, args = getopt.getopt(sys.argv[1:], "h:i:o:c:")
# print opts
# print args
# for op, value in opts:
#     if op == '-h':
#         print 'gangh %s' % value
#     elif op == '-i':
#         print "gangi"
#     elif op == '-c':
#         print "gangc"
#

import datetime, time
import hashlib
now = int(time.time())
timestamp = '20160121155642'
valid_time = int(time.mktime(datetime.datetime.strptime(timestamp, "%Y%m%d%H%M%S").timetuple()))
if (now < valid_time) or (now - valid_time > 10800):
    print 'ok'


str2 = 'HLS_P381503172210/3800/P381503172210_3800.m3u8?timestamp=20160121163750EzgSnNPrv8s9uB7Q'
md5str1 = hashlib.md5(str2).hexdigest()
print 'md5str1: ' + md5str1
print 'md5str2: ' + '0afbb35d7f514328efda3ac9367019bd'
print int(time.time())
print valid_time
s = ''
print s[1:]




