# -*- coding:utf-8 -*-
# --------------------
# Name:         category_form
# Author:       liuyonggui
# Date:         2020/2/29
# --------------------
from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField, StringField


class CategoryForm(FlaskForm):
    class CategoryForm(FlaskForm):
        category_name = StringField('类别名称')
        category_code = StringField('类别编号')
        remark = TextAreaField('备注')
        submit_add = SubmitField('添加')
        submit_update = SubmitField('更新')
