# -*- coding:utf-8 -*-
# --------------------
# Name:         product_form
# Author:       liuyonggui
# Date:         2020/3/9
# --------------------
from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, SubmitField, RadioField, TextAreaField
from wtforms.validators import DataRequired


class ProductForm(FlaskForm):
    product_name = StringField('商品名称', validators=[DataRequired()])
    specification = TextAreaField('商品规格')
    product_no = StringField('商品编号')
    product_detail = TextAreaField('商品详情')
    product_type = StringField('商品型号')
    product_factory = StringField('厂商')
    product_address = StringField('产地')
    brand = StringField('品牌')
    price = DecimalField('价格')
    status = RadioField('商品状态', choices=[('1', '上架'), ('0', '下架')], default='1')
    remark = TextAreaField('备注')
    submit_add = SubmitField('添加商品')
    submit_update = SubmitField('更新商品')
