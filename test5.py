#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# def log(text):
#     def decorator(func):
#         def wrapper(*args, **kw):
#             print 'call %s():' % text
#             return func(*args, **kw)
#         return wrapper
#     return decorator
#
# @log('testsss')
# def now():
#     return 'xianzai'
#
# print now()

# from bottle import jinja2_template as template
# contextstr = template('pcm_fds_request.xml', username='test', password='123455', item_id='2043854',
#                       source_path='http://asdasdasd.com', publish_path='http://asdasxzczcx.cn', md5='j43jsjfk5mdkfj4jsjdkeoi876')
# print contextstr
# from urlparse import urlparse
# url = 'http://www.baidu.com/test.mp4'
# print urlparse(url)[2][1:]
# # scheme = urlparse.urlparse(url).scheme
# # netloc = urlparse.urlparse(url).netloc
# # path = urlparse.urlparse(url).path
# # if path[:path.rindex('/')]:
# #     print 'asd'
# # path = path + path[path.rindex('/'):]
# # print path
# # print scheme + '://' + netloc + path
# url1 = 'http://www.cztv.com/video/mp4/cztv_test01.mp4/cztv_test01.mp4_playlist.m3u8'
# scheme = urlparse(url1).scheme
# netloc = urlparse(url1).netloc
# path = urlparse(url1).path
# path = path + path[path.rindex('/'):]
# url = scheme + '://' + netloc + path
# print url[:url.rindex('/')][:url[:url.rindex('/')].rindex('_')]

from bottle import Jinja2Template
data = {'status': 1, 'statusdesc': u'success', 'data': [{'bandwidth': [['2016-01-15 18:05', '0.00'], ['2016-01-15 18:10', '0.00'], ['2016-01-15 18:15', '0.00'], ['2016-01-15 18:20', '0.00'], ['2016-01-15 18:25', '0.00'], ['2016-01-15 18:30', '0.00'], ['2016-01-15 18:35', '0.00'], ['2016-01-15 18:40', '0.00'], ['2016-01-15 18:45', '0.00'], ['2016-01-15 18:50', '0.00'], ['2016-01-15 18:55', '0.00'], ['2016-01-15 19:00', '0.00'], ['2016-01-15 19:05', '0.00'], ['2016-01-15 19:10', '0.00'], ['2016-01-15 19:15', '0.00'], ['2016-01-15 19:20', '0.00'], ['2016-01-15 19:25', '0.00'], ['2016-01-15 19:30', '0.00'], ['2016-01-15 19:35', '1.81'], ['2016-01-15 19:40', '1.53'], ['2016-01-15 19:45', '2.33'], ['2016-01-15 19:50', '2.24'], ['2016-01-15 19:55', '2.02'], ['2016-01-15 20:00', '1.90'], ['2016-01-15 20:05', '3.54'], ['2016-01-15 20:10', '3.10'], ['2016-01-15 20:15', '0.15'], ['2016-01-15 20:20', '0.00']], 'tpye': 'hls', 'types': 'down', 'channel': 'sthlsplay.cdn.suicam.com'}], 'curtime': '2016-03-08 17:15:38'}
msg = Jinja2Template(name='mbw/views/band_width1.tpl').render(**_kwargs)
