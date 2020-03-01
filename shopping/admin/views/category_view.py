# -*- coding:utf-8 -*-
# --------------------
# Name:         category
# Author:       liuyonggui
# Date:         2020/2/27
# --------------------
from flask import render_template, request, redirect, url_for
from flask_login import login_required

from shopping.extension import db
from ..admin_bp import admin
from ..forms.category_form import CategoryForm
from ..models import Category


@admin.route('/category', methods=['GET', 'POST'])
def cates_view():
    form = CategoryForm()
    cate_name = form.category_name.data
    if not cate_name:
        categories = Category.query.filter_by(pid=0)
    else:
        categories = Category.query.filter_by(category_name=cate_name)
    return render_template('category/index.html', categories=categories)


@admin.route('/category/add', methods=['GET', 'POST'])
def cate_add():
    form = CategoryForm()
    if request.method == 'POST':
        category = Category.query.filter_by(category_name=form.category_name.data).first()
        if category is None:
            cate = Category(pid=0, category_name=form.category_name.data, category_code=form.category_code.data, remark=form.remark.data)
            db.session.add(cate)
            db.session.commit()
            return redirect(url_for('admin.cates_view'))
    return render_template('category/cate_add.html', form=form)


@admin.route('/category/update/<int:cate_id>', methods=['GET', 'POST'])
def cate_update(cate_id):
    if cate_id is None:
        return redirect(url_for('admin.cates_view'))
    cate = Category.query.get(cate_id)
    form = CategoryForm(category_name=cate.category_name, category_code=cate.category_code, remark=cate.remark)
    if request.method == 'POST':
        cate.category_name = form.category_name.data
        cate.category_code = form.category_code.data
        cate.remark = form.remark.data
        db.session.commit()
        return redirect(url_for('admin.cates_view'))
    return render_template('category/cate_update.html', form=form)


@admin.route('/category/delete/<int:cate_id>', methods=['GET', 'POST'])
def cate_delete(cate_id):
    if cate_id is None:
        return redirect(url_for('admin.cates_view'))
    cate = Category.query.get(cate_id)
    db.session.delete(cate)
    db.session.commit()
    return redirect(url_for('admin.cates_view'))
