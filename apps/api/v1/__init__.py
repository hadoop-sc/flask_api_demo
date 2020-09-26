# -*- coding:utf-8 -*-
# =============================================================================
#     FileName: __init__.py.py
#         Desc: 2020/9/26 9:30
#       Author: shaochun
#      History: 
# =============================================================================
"""v1接口版本"""

from flask import Blueprint
from flask_restplus import Api
from .demo import ns as demo_ns
from .demo1 import ns as demo1_ns

blueprint = Blueprint('flask_demo', __name__, url_prefix='/api/v1')

api = Api(blueprint, title='Demo API v1',
          version='1.0',
          description='Demo API v1',
          )

api.add_namespace(demo_ns)
api.add_namespace(demo1_ns)

