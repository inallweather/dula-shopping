# -*- coding:utf-8 -*-
# --------------------
# Name:         extension
# Author:       liuyonggui
# Date:         2020/2/27
# --------------------
import pymysql
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
bootstrap = Bootstrap()
moment = Moment()
pymysql.install_as_MySQLdb()


def init_extension(app):
    db.init_app(app)
    bootstrap.init_app(app)
    moment.init_app(app)
