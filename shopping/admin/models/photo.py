# -*- coding:utf-8 -*-
# --------------------
# Name:         photo
# Author:       liuyonggui
# Date:         2020/2/27
# --------------------
from shopping import db


class Photo(db.Model):
    # 商品图片表
    __tablename__ = 'tb_photo'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 商品图片名称
    photo_name = db.Column(db.String(50))
    # 商品图片地址
    photo_url = db.Column(db.String(50))
    # 商品图片备注
    remarkd = db.Column(db.String(200))
    # 商品id
    product_id = db.Column(db.Integer, db.ForeignKey('tb_commodity.id'))

