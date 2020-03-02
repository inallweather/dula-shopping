# -*- coding:utf-8 -*-
# --------------------
# Name:         order
# Author:       liuyonggui
# Date:         2020/2/28
# --------------------
from flask import render_template, request, redirect, url_for, flash

from ..admin_bp import admin
from ..forms.user_form import RegisterForm
from ..models import User


@admin.route('/user', methods=['GET', 'POST'])
def users_view():
    users = User.query.filter_by()
    return render_template('sys_user/index.html', users=users)


@admin.route('/user/add', methods=['GET', 'POST'])
def user_add():
    form = RegisterForm(data={'active': 1})
    if request.method == 'GET':
        return render_template('sys_user/user_add.html', form=form)
    if request.method == 'POST':
        if form.validate_on_submit():
            # if not form.username.data and not form.nickname.data and not form.password.data:
            #     flash('用户名，登录名及密码不能为空！')
            #     return render_template('sys_user/user_add.html', form=form)
            user = User(username=form.username.data, nickname=form.nickname.data, passwd=form.password.data, active=int(form.active.data), remark=form.remark.data)
            # db.session.add(user)
            # db.session.commit()
            flash('用户添加成功！')
            return redirect(url_for('admin.users_view'))
        else:
            return render_template('sys_user/user_add.html', form=form)


@admin.route('/user/update/<int:user_id>', methods=['GET', 'POST'])
def user_update(user_id):
    form = RegisterForm()
    if request.method == 'GET':
        return render_template('sys_user/user_update.html', form=form)
    if request.method == 'POST':
        return redirect(url_for('admin.users_view'))


@admin.route('/user/delete<int:user_id>', methods=['GET', 'POST'])
def user_delete(user_id):
    return redirect(url_for('admin.users_view'))
