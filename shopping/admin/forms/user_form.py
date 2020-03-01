# -*- coding:utf-8 -*-
# --------------------
# Name:         user_form
# Author:       liuyonggui
# Date:         2020/3/1
# --------------------
from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, SubmitField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, Length


class RegisterForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired(message='请输入用户名'), Length(5, 15, message='用户名在5到15个字符之间')])
    nickname = StringField('登录名', validators=[DataRequired(message='请输入登录名称，最好是英文组合'), Length(5, 15, message='登录名在5到15个字符之间')])
    password = PasswordField('密码', validators=[DataRequired(message='请输入密码'), Length(5, 15, message='密码在5到15个字符之间')])
    active = RadioField('是否可用', choices=[(1, '激活'), (0, '禁用')])
    remark = TextAreaField('备注')
    submit_add = SubmitField('添加用户')
    submit_update = SubmitField('更新用户')


class LoginForm(FlaskForm):
    nickname = StringField('登录名', validators=[DataRequired(), Length(5, 15, message='登录名在5到15个字符之间')])
    password = PasswordField('密码', validators=[DataRequired(), Length(5, 15, message='密码在5到15个字符之间')])
    submit = SubmitField('立即登录')
