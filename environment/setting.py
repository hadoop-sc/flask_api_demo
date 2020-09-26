# -*- coding:utf-8 -*-
# =============================================================================
#     FileName: setting.py
#         Desc: 2020/9/26 8:50
#       Author: shaochun
#      History: 
# =============================================================================

import os

"""从系统中获取对应的环境变量配置"""

# 密钥设置
flask_demo_secret_key = os.environ.get('FlASK_DEOM_SECRET_KEY', 'flask-demo-secret-key')

# 数据库设置(以mysql为例)
flask_demo_mysql_host = os.environ.get('FLASK_DEMO_MYSQL_HOST', 'localhost')
flask_demo_mysql_port = os.environ.get('FLASK_DEMO_MYSQL_PORT', '3306')
flask_demo_mysql_user = os.environ.get('FLASK_DEMO_MYSQL_USER', 'root')
flask_demo_mysql_password = os.environ.get('FLASK_DEMO_MYSQL_PASSWORD', '123456')
flask_demo_mysql_dbname = os.environ.get('FLASK_DEMO_MYSQL_DBNAME', 'flask_demo')

# redis设置
flask_demo_redis_host = os.environ.get('FLASK_DEMO_REDIS_HOST', 'localhost')
flask_demo_redis_port = os.environ.get('FLASK_DEMO_REDIS_PORT', '6379')
flask_demo_redis_dbname = os.environ.get('FLASK_DEMO_REDIS_DBNAME', '0')
flask_demo_redis_password = os.environ.get('FLASK_DEMO_REDIS_PASSWORD', None)

# session设置
# session 过期时间默认一天
permanent_session_lifetime = int(os.environ.get('FLASK_DEMO_PERMANENT_SESSION_LIFETIME', '86400'))

# 日志等级
log_level = os.environ.get('FLASK_DEMO_LOG_LEVEL', 'INFO')