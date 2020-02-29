# -*- coding:utf-8 -*-
# --------------------
# Name:         user
# Author:       liuyonggui
# Date:         2020/2/27
# --------------------
from shopping import db


class User(db.Model):
    __tablename__ = 'tb_user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(32), unique=True, nullable=False)
    nickname = db.Column(db.String(32), nullable=False, unique=True)
    password = db.Column(db.String(32), nullable=True)
    active = db.Column(db.Boolean, default=True)
    remark = db.Column(db.String(300))
