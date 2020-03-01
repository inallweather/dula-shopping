# -*- coding:utf-8 -*-
# --------------------
# Name:         extension
# Author:       liuyonggui
# Date:         2020/2/27
# --------------------
import pymysql
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
bootstrap = Bootstrap()
moment = Moment()
login_manager = LoginManager()


pymysql.install_as_MySQLdb()


def init_extension(app):
    db.init_app(app)
    bootstrap.init_app(app)
    moment.init_app(app)
    login_manager.init_app(app)
    # 确认登录状态，None,不使用，'basic'最基本的，strong，为最高级别的，当用户信息个性，会立即退出
    login_manager.session_protection = 'strong'
    # 设置登录页面端点，当用户访问需要登录才能访问的页面，此时还没有登录，会自动跳转到登录页面
    login_manager.login_view = 'admin.user_view'
    # 设置提示信息,默认为英文提示信息
    login_manager.login_message = '请先登录后在访问'

