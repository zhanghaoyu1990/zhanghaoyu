# -*-coding: utf-8-*-
from flask import Flask, request
import json
import simplejson
import hashlib
import requests
app = Flask(__name__)


def byteify(input):
    if isinstance(input, int):
        return str(input)
    elif isinstance(input, unicode):
        return input.encode('utf-8')
    else:
        return input

security_key = 'insurance.jiankangka'
request_url = 'http://127.0.0.1:5555/'
headers = {'content-type': 'application/json'}
###########

@app.route('/', methods=['get', 'post'])
def repeater():
    rep = request.data
    rep_dict = simplejson.loads(rep)['requestData']
    # rep_dict = [(k, rep_dict[k]) for k in sorted(rep_dict.keys())]
    rep_string = ''
    for k in sorted(rep_dict.keys()):
        if k != 'sign':
            k = byteify(k)
            v = byteify(rep_dict[k])
            rep_string += k + '=' + v + '&'
    rep_string += security_key
    m2 = hashlib.md5()
    m2.update(rep_string)
    sign = m2.hexdigest()
    rep_dict['sign'] = sign
    rep = simplejson.dumps({'requestData': rep_dict})
    res = requests.post(request_url, rep, headers)
    return res.text
    # return sign

app.run(debug=True)
