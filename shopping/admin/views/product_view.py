# -*- coding:utf-8 -*-
# --------------------
# Name:         product
# Author:       liuyonggui
# Date:         2020/2/27
# --------------------
from flask import render_template, request, redirect, url_for
from flask_login import login_required

from shopping.admin.admin_bp import admin
from shopping.admin.forms.product_form import ProductForm
from shopping.admin.models import Commodity


@admin.route('/product', methods=['GET', 'POST'])
@login_required
def prods_view():
    products = Commodity.query.filter_by()
    return render_template('product/index.html', **locals())


@admin.route('/product/add', methods=['GET', 'POST'])
@login_required
def prods_add():
    form = ProductForm()
    return render_template('product/prod_add.html', **locals())


@admin.route('/product/update/<int:prod_id>', methods=['GET', 'POST'])
@login_required
def prods_update(prod_id):
    comm = Commodity.query.get(prod_id)
    if prod_id is None:
        return redirect(url_for('admin.prods_view'))
    form = ProductForm(prefix='edit_comm', obj=comm)
    if request.method == 'POST' and form.validate_on_submit():
        return redirect(url_for('admin.prods_view'))
    return render_template('product/prod_add.html', **locals())


@admin.route('/product/delete/<int:prod_id>', methods=['GET', 'POST'])
@login_required
def prods_delete(prod_id):
    return redirect(url_for('admin.prods_view'))
