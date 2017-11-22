#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.httpserver
import tornado.httpclient
import tornado.ioloop
import tornado.options
import tornado.web
import os
_body ="""
<?xml version="1.0" encoding="UTF-8" ?>
<message module="CDN" version="3.0">
        <header action="REQUEST" command="AGENT_STATUS_REPORT" sequence="5742950446796917840" component-id="Agent-SIDE-75" component-type="AGENT" />
        <body>
                <device id="PC-172.30.61.105-vod01" device-type="PIC_UCE" pop-type="SIDE"
                        version=" ContEx 4.3.2" status="1" service-ip="172.30.61.105"
                        max-user="100000" online-user=""
                        max-bandwidth="1073741824" used-bandwidth="198000"
                        report-interval="5"/>
        </body>
</message>
 """

class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        print type(self.request.arguments)
        self.write("Index Handler")
        http_client = tornado.httpclient.HTTPRequest('http://172.30.37.88:6040', method='POST', body=_body)
        print http_client
        print http_client.body
        print http_client.

        # self.finish()


class MainHandler(tornado.web.RequestHandler):
    def get(self,    *args, **kwargs):
        self.write("Main Handler")
        self.finish()


class OtherHandler(tornado.web.RequestHandler):
    def get(self,    *args, **kwargs):
        raise tornado.web.HTTPError(status_code=403, reason="unknow request please visit localhost:8888")


class CustomApp(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", MainHandler),
            (r"/zhy", IndexHandler),
            # (r"/.*", tornado.web.RedirectHandler, {'url': '/'}),
            (r"/.*", OtherHandler)
                    ]
        setting = {
            'templates_path': os.path.join(os.path.dirname(__file__), 'templates'),
            'static_path': os.path.join(os.path.dirname(__file__), 'static'),
        }
        super(CustomApp, self).__init__(handlers, **setting)
if __name__ == "__main__":
    # app = tornado.web.Application(handlers=[(r"/", MainHandler), (r"/zhy", IndexHandler)])
    http_server = tornado.httpserver.HTTPServer(CustomApp())
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()


