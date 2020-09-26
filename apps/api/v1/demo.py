# -*- coding:utf-8 -*-
# =============================================================================
#     FileName: demo.py
#         Desc: 2020/9/26 9:40
#       Author: shaochun
#      History: 
# =============================================================================
"""接口示例"""

from apps.api.v1 import api


@api.route('/index')
def index():
    return 'hello world'

