# -*- coding:utf-8 -*-
# --------------------
# Name:         admin_bp
# Author:       liuyonggui
# Date:         2020/2/27
# --------------------
from flask import Blueprint

admin = Blueprint('admin', __name__, url_prefix='/admin', template_folder='templates')

from .views import *
