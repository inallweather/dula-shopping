# -*- coding:utf-8 -*-
# --------------------
# Name:         order
# Author:       liuyonggui
# Date:         2020/2/28
# --------------------
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required

from shopping.extension import db
from ..admin_bp import admin
from ..forms.user_form import RegisterForm
from ..models import User


@admin.route('/user', methods=['GET', 'POST'])
@login_required
def users_view():
    users = User.query.filter_by()
    return render_template('sys_user/index.html', users=users)


@admin.route('/user/add', methods=['GET', 'POST'])
@login_required
def user_add():
    form = RegisterForm()
    return render_template('sys_user/user_add.html', **locals())


@admin.route('/user/update/<int:user_id>', methods=['GET', 'POST'])
@login_required
def user_update(user_id):
    user = User.query.get(user_id)
    form = RegisterForm(prefix='edit_user', obj=user)

    if request.method == 'GET':
        return render_template('sys_user/user_update.html', form=form)
    if request.method == 'POST' and form.validate_on_submit():
        user.username = form.username.data
        user.nickname = form.nickname.data
        user.active = int(form.active.data)
        user.remark = form.remark.data
        db.session.commit()
        flash('更新成功')
        return redirect(url_for('admin.users_view'))


@admin.route('/user/delete<int:user_id>', methods=['GET', 'POST'])
@login_required
def user_delete(user_id):
    user = User.query.get(user_id)
    db.session.delete(user)
    db.session.commit()
    flash('删除成功')
    return redirect(url_for('admin.users_view'))
