# -*- coding:utf-8 -*-
# --------------------
# Name:         config
# Author:       liuyonggui
# Date:         2020/2/27
# --------------------

import os
from datetime import timedelta

BASE_DIR = os.path.abspath(os.path.dirname(__name__))


class Config:
    # 密钥
    SECRET_KEY = os.environ.get('SECRET_KEY') or os.urandom(20)
    # 数据库操作
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    # 数据库的追踪
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # 使用本地库中bootstrap
    BOOTSTRAP_SERVER_LOCAL = True

    WTF_CSRF_ENABLED = False
    WTF_CSRF_SECRET_KEY = os.urandom(20)
    # 配置文件最大文件上传的大小
    # MAX_CONTENT_LENGTH = 30 * 1024 * 1024
    # UPLOADED_IMAGES_DEST = os.path.join(BASE_DIR, 'app/static/uploads')

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    # 配置模板自动加载
    TEMPLATES_AUTO_RELOAD = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:root@localhost/dulashopping?charset=utf8'
    SEND_FILE_MAX_AGE_DEFAULT = timedelta(seconds=1)


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://root:root@localhost/dulashopping?charset=utf8'


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
