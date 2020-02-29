# -*- coding:utf-8 -*-
# --------------------
# Name:         views
# Author:       liuyonggui
# Date:         2020/2/27
# --------------------
from flask import render_template

from shopping.web.web_bp import web


@web.route('/')
def home():
    return render_template('home/index.html')
