# -*- coding:utf-8 -*-
# --------------------
# Name:         login
# Author:       liuyonggui
# Date:         2020/2/27
# --------------------
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from shopping.extension import login_manager, db


class User(UserMixin, db.Model):
    __tablename__ = 'tb_user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(32), unique=True, nullable=False)
    nickname = db.Column(db.String(32), nullable=False, unique=True)
    password = db.Column(db.String(150), nullable=True)
    active = db.Column(db.Boolean, default=True)
    remark = db.Column(db.String(300))

    @property
    def passwd(self):
        return self.password

    @passwd.setter
    def passwd(self, raw_passwd):
        self.password = generate_password_hash(raw_passwd)

    def validator_passwd(self, raw_passwd):
        return check_password_hash(self.password, raw_passwd)


@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(int(user_id))
