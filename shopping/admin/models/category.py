# -*- coding:utf-8 -*-
# --------------------
# Name:         category
# Author:       liuyonggui
# Date:         2020/2/27
# --------------------
from shopping import db


class Category(db.Model):
    __tablename__ = 'tb_category'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pid = db.Column(db.Integer, default=0)
    category_name = db.Column(db.String(32), nullable=False, unique=True)
    category_code = db.Column(db.String(32))
    order = db.Column(db.Integer, default=1)
    remark = db.Column(db.String(200))
