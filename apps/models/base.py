# -*- coding:utf-8 -*-
# =============================================================================
#     FileName: base.py
#         Desc: 2020/9/26 9:24
#       Author: shaochun
#      History: 
# =============================================================================
from apps import db


class BaseModel(db.Model):
    """数据模型基类"""
    create_time = db.Column()