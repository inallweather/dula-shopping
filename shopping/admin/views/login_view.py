# -*- coding:utf-8 -*-
# --------------------
# Name:         login_view
# Author:       liuyonggui
# Date:         2020/3/1
# --------------------
from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user

from ..admin_bp import login
from ..forms.user_form import LoginForm
from ..models import User


@login.route('/', methods=['GET', 'POST'])
def login_view():
    form = LoginForm()
    if request.method == 'GET':
        return render_template('login/login.html', form=form)
    if request.method == 'POST' and form.validate():
        u = User.query.filter_by(nickname=form.nickname.data).first()
        if u is None:
            flash('请确认你的用户名及密码，然后再试')
        elif u.password == form.password.data:
            login_user(u)
            flash('登录成功！')
            return redirect(url_for('admin.cates_view'))
        else:
            flash('请确认你是否注册')
    else:
        flash('登录失败')
        return render_template('login/login.html', form=form)
