# -*- coding: utf-8 -*-
from bottle import *
import json
@post('/keys/sync')
def key_sync():
    """ 密钥同步接口 """

    key_list = request.json

run(app, host='localhost', port=8080)