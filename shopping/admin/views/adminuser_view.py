# -*- coding:utf-8 -*-
# --------------------
# Name:         order
# Author:       liuyonggui
# Date:         2020/2/28
# --------------------
from flask import render_template

from ..admin_bp import admin


@admin.route('/user')
def users_view():
    return render_template('sys_user/index.html')
