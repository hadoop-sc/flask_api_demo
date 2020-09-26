# -*- coding:utf-8 -*-
# =============================================================================
#     FileName: manage.py
#         Desc: 2020/9/25 8:32
#       Author: shaochun
#      History: 
# =============================================================================

from apps import create_app, db
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

# 获取app
app = create_app()
# 初始化manager对象
manager = Manager(app)
# 将app与db关联
Migrate(app, db)
# 将MigrateCommand添加到manager中
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
