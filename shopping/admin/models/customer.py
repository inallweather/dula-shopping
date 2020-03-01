# -*- coding:utf-8 -*-
# --------------------
# Name:         customer
# Author:       liuyonggui
# Date:         2020/2/27
# --------------------
from shopping.extension import db


class Customer(db.Model):
    __tablename__ = 'tb_customer'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cust_nickname = db.Column(db.String(32), nullable=False, unique=True)
    cust_name = db.Column(db.String(32))
    cust_passwd = db.Column(db.String(32))
    cust_type = db.Column(db.String(10))
    cust_address = db.Column(db.String(50))
    cust_active = db.Column(db.Boolean, default=True)
    cust_remark = db.Column(db.String(200))
