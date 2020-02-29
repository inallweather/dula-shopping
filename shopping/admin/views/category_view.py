# -*- coding:utf-8 -*-
# --------------------
# Name:         category
# Author:       liuyonggui
# Date:         2020/2/27
# --------------------
from flask import render_template

from ..admin_bp import admin
from ..models import Category


@admin.route('/category')
def cates_view():
    categories = Category.query.filter_by(pid=0)
    return render_template('category/index.html', categories=categories)
