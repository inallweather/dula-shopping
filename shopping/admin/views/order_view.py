# -*- coding:utf-8 -*-
# --------------------
# Name:         order
# Author:       liuyonggui
# Date:         2020/2/28
# --------------------
from flask import render_template
from flask_login import login_required

from ..admin_bp import admin


@admin.route('/order')
@login_required
def orders_view():
    return render_template('order/index.html')
