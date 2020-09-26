# -*- coding:utf-8 -*-
# =============================================================================
#     FileName: __init__.py.py
#         Desc: 2020/9/25 9:30
#       Author: shaochun
#      History: 
# =============================================================================
"""flask app 初始化"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from redis import StrictRedis
from flask_wtf import CSRFProtect
from config import config_map
from environment.setting import flask_demo_redis_host, flask_demo_redis_port, flask_demo_redis_dbname, \
    flask_demo_redis_password

db = SQLAlchemy()
redis_store = None


def create_app(config_name='dev'):
    """
    初始化app设置
    :param config_name: str 根据部署环境选择对应的app设置（dev,test,prod）, 默认dev
    :return: app对象
    """
    # 初始化app对象
    app = Flask(__name__)
    app.config.from_object(config_map[config_name])
    print(app.config)

    # 初始化db对象
    db.init_app(app)

    # 初始化session对象

    Session(app)

    # 增加CRSF防护
    CSRFProtect(app)

    # 初始化redis
    global redis_store
    if flask_demo_redis_password:
        redis_store = StrictRedis(flask_demo_redis_host, flask_demo_redis_port, flask_demo_redis_dbname,
                                  flask_demo_redis_password)
    else:
        redis_store = StrictRedis(flask_demo_redis_host, flask_demo_redis_port, flask_demo_redis_dbname)

    # 注册蓝图(在create_app方法内引用，防止循环导入)
    from apps.api.v1 import blueprint as api_v1
    app.register_blueprint(api_v1)

    return app
