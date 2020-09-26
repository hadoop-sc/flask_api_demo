# -*- coding:utf-8 -*-
# =============================================================================
#     FileName: __init__.py.py
#         Desc: 2020/9/26 9:30
#       Author: shaochun
#      History: 
# =============================================================================
"""v1接口版本"""

from flask import Blueprint

api = Blueprint('flask_demo', __name__, url_prefix='/api/v1')
