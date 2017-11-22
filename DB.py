#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bottle import *
import mysql.connector
import bottle_mysql_connector
# conn = mysql.connector.connect(user='root', password='123456', database='test1', use_unicode='True')
install(bottle_mysql_connector.MySQLConnectorPlugin(user='root', password='123456', database='test1',
                                                    host='172.30.37.107', ))


@route('/show')
def querys(db):
    query = "SELECT * from task_list "
    db.execute(query)
    row = db.fetchone()
    if row:
        return row
    return HTTPError(404, "Page not found")
run(host='localhost', port=8080, debug=True)
