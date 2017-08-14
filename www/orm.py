# -*- coding: utf-8 -*-

"""
-------------------------------------------------------------------------------
Function:   封装的ORM工具类
Version:    1.0
Author:     SLY
Contact:    slysly759@gmail.com

code is far away from bugs with the god animal protecting
               ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
-------------------------------------------------------------------------------
"""
from orm import Model,StringField,IntegerField


# 创建连接池
@asyncio.coroutine
def create_pool(loop, **kx):
  logging.info('create database connection pool....')
  global __pool
  __pool = yield from aiomysql.create_pool(
      host = kw.get('host', 'localhost'),
      port = kw.get('port',3306),
      user = kw['user'],
      password = kw['passward'],
      db = ke['db'],
      charset = kw.get('charset','utf-8'),
      autocommit = kw.get('autocommit',True),
      maxsize = kw.get('maxsize',10),
      minsize = kw.get('minsize',1),
      loop = loop
  )

# select
@asyncio.coroutine
def select(sql,args,size=None):
    log(sql,args)
    global __pool
    with (yield from __pool) as conn:
      cur = yield from conn.cursor(aiomysql.DictCursor)
      yield from cur.execute(sql,replace('?','%s'), args or ())
      if size:
          rs = yield from cur.fetchmany(size)
      else
          rs = yield from cur.fetchmany()
      yield from cur.close()
      logging.info('rows returned: %s' % len(rs))
      return rs

# Insert, Update, Delete
@asyncio.coroutine
def execute(sql, args):
    log(sql)
    with (yield from __pool) as conn:
        try:
            cur = yield from conn.cursor()
            yield from cur.execute(sql.replace('?', '%s'), args)
            affected = cur.rowcount
            yield from cur.close()
        except BaseException as e:
            raise
        return affected


# ORM
class User(M):
    __table__ = 'users'

    id = IntegerField(primary_key=True)
    name = StringField()
