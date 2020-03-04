# -*- coding:utf-8 -*-
# --------------------
# Name:         order
# Author:       liuyonggui
# Date:         2020/2/28
# --------------------
from flask import render_template, redirect, url_for

from shopping.extension import db
from ..admin_bp import admin
from ..models.customer import Customer


@admin.route('/customer')
def custs_view():
    custs = Customer.query.all()
    return render_template('customer/index.html', **locals())


@admin.route('/customer/delete/<int:cust_id>')
def cust_delete(cust_id):
    cust = Customer.query.get(cust_id)
    db.session.delete(cust)
    db.session.commit()
    return redirect(url_for('admin.custs_view'))
