# -*- coding:utf-8 -*-
# --------------------
# Name:         web_bp
# Author:       liuyonggui
# Date:         2020/2/27
# --------------------
from flask import Blueprint

web = Blueprint('web', __name__, template_folder='templates')

from .views import *