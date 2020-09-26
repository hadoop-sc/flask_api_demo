# -*- coding:utf-8 -*-
# =============================================================================
#     FileName: demo.py
#         Desc: 2020/9/26 9:40
#       Author: shaochun
#      History: 
# =============================================================================
"""接口示例"""

from flask_restplus import Namespace, Resource

ns = Namespace('demo1', description='namespace api demo1', path='/demo1')


@ns.route('/index1')
class Demo(Resource):

    def get(self):
        return 'hello world'

