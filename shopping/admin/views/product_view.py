# -*- coding:utf-8 -*-
# --------------------
# Name:         product
# Author:       liuyonggui
# Date:         2020/2/27
# --------------------
from flask import render_template

from shopping.admin.admin_bp import admin


@admin.route('/product')
def prods_view():
    return render_template('product/index.html')
