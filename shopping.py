# -*- coding:utf-8 -*-
# --------------------
# Name:         shopping
# Author:       liuyonggui
# Date:         2020/2/27
# --------------------
import os

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Server

from shopping import create_app, db
from shopping.admin.models import *


app = create_app(os.environ.get('FLASK_ENV') or 'default')

manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

manager.add_command('runserver', Server(host='localhost', port=3000, use_debugger=True))

if __name__ == '__main__':
    manager.run()
