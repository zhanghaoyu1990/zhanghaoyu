#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import logging
import random,string
from kafka.producer import SimpleProducer
from kafka.client import KafkaClient
LOG = logging.getLogger('kafka_producer')


class TrueCloudDataPointProducer(object):
    def __init__(self, hosts, batch_send=False, batch_send_every_n=20, topic="true_cloud_datapoint_topic"):
        self.hosts = hosts
        self.client = KafkaClient(self.hosts)
        self.batch_send = batch_send
        self.batch_send_every_n = batch_send_every_n
        self.producer = SimpleProducer(self.client, batch_send=batch_send, batch_send_every_n=batch_send_every_n)
        self.topic = topic

    def send_messages(self, msg):
        self.producer.send_messages(self.topic, msg)


def get_instance():
    hosts = ['hadoop01:9092', 'hadoop01:9093', 'hadoop01:9094', 'hadoop101:9095']
    return TrueCloudDataPointProducer(hosts)
if __name__=="__main__":
    begin=time.time()
    producer=get_instance()
    for i in range(0,10000):
        msg='Message'+str(i)+' '+''.join(random.choice(string.lowercase)
    for i in range(64))+'n'
        producer.send_messages(msg)
        end=time.time()
        print("use time:"+str((end-begin)))


