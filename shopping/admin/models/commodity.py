# -*- coding:utf-8 -*-
# --------------------
# Name:         commodity
# Author:       liuyonggui
# Date:         2020/2/27
# --------------------
from shopping.extension import db


class Commodity(db.Model):
    # 商品表
    __tablename__ = 'tb_commodity'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    # 商品类型
    cate_id = db.Column(db.Integer, nullable=False)
    # 商品名称
    product_name = db.Column(db.String(50), nullable=False)
    # 商品规格
    specification = db.Column(db.String(300))
    # 商品编号
    product_no = db.Column(db.String(32))
    # 商品详情
    product_detail = db.Column(db.String(500))
    # 商品型号
    product_type = db.Column(db.String(52))
    # 厂商
    product_factory = db.Column(db.String(64))
    # 产地
    product_address = db.Column(db.String(52))
    # 品牌
    brand = db.Column(db.String(52))
    # 价格
    price = db.Column(db.Float)
    # 状态（是否上架）
    status = db.Column(db.Integer)
    # 商品备注
    remark = db.Column(db.String(200))

    photos = db.relationship('Photo', backref='commodity', lazy='dynamic')
