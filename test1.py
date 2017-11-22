#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# from bottle import *
# @route('/zhy/<tests>', method=('GET', 'POST'))
# def test(tests):
#     print tests
# run()
import json
import time

_jsonstr = '{"data":[{"app":"zqlive","domain":"suntv.stcdn.tvmining.com","instance":"30647_JIjP2","下行流量":[{"time":"2015-12-14 15","value":"111111.916"},{"time":"2015-12-14 16","value":"263819.939"},{"time":"2015-12-14 17","value":"281584.598"},{"time":"2015-12-14 18","value":"365982.747"},{"time":"2015-12-14 19","value":"263128.099"}]},{"app":"zqlive","domain":"suntv.stcdn.tvmining.com","instance":"30222_JIjP2","流量":[{"time":"2015-12-14 15","value":"222222.916"},{"time":"2015-12-14 16","value":"263819.939"},{"time":"2015-12-14 17","value":"281584.598"},{"time":"2015-12-14 18","value":"365982.747"},{"time":"2015-12-14 19","value":"263128.099"}]},{"app":"zqlive","domain":"suntv.stcdn.tvmining.com","instance":"30222_JIjAA","流量统计":[{"time":"2015-12-14 15","value":"333333.916"},{"time":"2015-12-14 16","value":"263819.939"},{"time":"2015-12-14 17","value":"222222.598"},{"time":"2015-12-14 18","value":"365982.747"},{"time":"2015-12-14 19","value":"263128.099"}]}]}'


d = json.loads(_jsonstr, encoding='utf-8')

# print d['data'][1][u'流量统计']
# jsonstr = json.JSONDecoder().decode(_jsonstr)
# print type(jsonstr), jsonstr['data']
a = {}
instances = ['30647_JIjP2', '30222_JIjP2', '30222_JIjAA']
# for x in d['data']:
#     if x['instance'] == '30647_JIjP2':
#         a = x[u'流量统计']


def get_flow(instancelist):
        for x in d['data']:
            for i in instancelist:
                if x['instance'] == i:
                    flow_list = []
                    for f in x[u'流量统计']:
                        k = f['time']
                        v = f['value']
                        c = {k:v}
                        flow_list.append({f['time']: f['value']})
                        # flow_list.append('%s":"%s'%(f['time'], f['value']))
                    a[i] = flow_list
        print a
        b = json.dumps(a)
        print b


# get_flow(instancelist)
#
_time = '2016-02-23 00:00'
_time = time.mktime(time.strptime(_time, "%Y-%m-%d %H:%M")) - 300
_time = time.strftime('%Y-%m-%d %H:%M', time.localtime(_time))
print _time

# a = "Mar 28 22:24:24 2009"
# b = time.mktime(time.strptime(a,"%b %d %H:%M:%S %Y"))
# print b
task_list = []
_channels = 'domain1;domain2:instance1,instance2;domain3:instance1'.split(';')

# for _channel in _channels:
#     _domains = _channel.split(':')
#     _len = len(_domains)
#     if _len == 1:
#         task_list.append(_domains)
#     elif _len == 2:
#         _domains1 = _domains[0]
#         instances = _domains[1].split(',')
#         task_list.append({_domains1: instances})
#
#
# print task_list
#
# cc = {'domain2': ['instance1', 'instance2']}
# print cc.items()
# print cc.items()[0]
_data = []
for v in d['data']:
    for i in instances:
        if v['instance'] == i:
            if v['下行流量']:
                _dict = dict(channel=v['domain'], instance=i, flow=v['下行流量'])
                for f in v['下行流量']:
                    _dict['flow'].append([f['time'], f['value']])
                _data.append(_dict)
            if v['hls流量']:
                _dict1 = dict(channel=v['domain'], instance=i, flow=v['hls流量'])
                for f in v['hls流量']:
                    _dict1['flow'].append([f['time'], f['value']])
                _data.append(_dict1)

print _data











