# -*- coding:utf-8 -*-
# --------------------
# Name:         __init__.py
# Author:       liuyonggui
# Date:         2020/2/27
# --------------------
from flask import Flask

from .config import config
from .extension import db, init_extension
from shopping.admin.admin_bp import admin
from shopping.web.web_bp import web


def create_app(config_name):
    app = Flask(__name__)
    # 初始化数据及flask配置参数
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    init_extension(app)
    # 初始化orm
    db.init_app(app)
    # 注册前台端路由
    register_router(app)
    return app




def register_router(app):
    app.register_blueprint(admin)
    app.register_blueprint(web)
