#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/17 17:17
# @Author  : yangyanxue
# @File    : PyMysql.py
# @Software: PyCharm
import pymysql
class MysqlHander:
    def __init__(self,host,username,password,databasename,port=3306):
        self.host = host
        self.username = username
        self.password =password
        self.databasename =databasename
        self.port = int(port)
        self.conn = None
    def _conn(self):
        if self.conn is  None:
            self.conn = pymysql.connect(
                host = self.host,
                port = self.port,
                user = self.username,
                password = self.password,
                db = self.databasename,
                charset = 'utf8mb4',
                cursorclass = pymysql.cursors.DictCursor
                )

    def _dis_conn(self):
        if self.conn is not None:
            try:
                self.conn = None
                self.conn.close()
            except Exception as _:
                pass
    def get_query_results(self,*args,**kwargs):
        try:
            self._conn()
            with self.conn.cursor() as cursor:
                cursor.execute(*args,**kwargs)
                result = cursor.fetchall()
                return result
        finally:
            self._dis_conn()