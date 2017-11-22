#coding:utf-8
from bottle import *
def transcode():
    """
    转码任务方法
    """
    pass
# @route('/hello/<name>')
# def index(name):
#     return template('<b>Hello {{name}}</b>!', name=name)
@route('/<app>/<instance>/<filepath:path>')
def server_static(app,instance,filepath):
    a = app+instance
    print a
    return static_file(filepath, root=app+"/"+instance+"/")


@error(404)
def error404(error):
    print error
    return '图片不存在，请稍后查看.'
run(host='localhost', port=8080)