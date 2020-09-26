# -*- coding:utf-8 -*-
# =============================================================================
#     FileName: demo.py
#         Desc: 2020/9/26 9:40
#       Author: shaochun
#      History: 
# =============================================================================
"""接口示例"""

from flask_restplus import Namespace, Resource

ns = Namespace('demo', description='namespace api demo', path='/demo')


@ns.route('/index')
class Demo(Resource):

    def get(self):
        return 'hello world'

