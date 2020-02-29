# -*- coding:utf-8 -*-
# --------------------
# Name:         order
# Author:       liuyonggui
# Date:         2020/2/28
# --------------------
from flask import render_template

from ..admin_bp import admin


@admin.route('/order')
def orders_view():
    return render_template('order/index.html')
