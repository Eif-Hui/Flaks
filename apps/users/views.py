# -*- coding: utf-8 -*-
# @Time    : 2020/3/8 下午10:37
# @Author  : Hui
# @File    : views.py

from flask import request,jsonify
from flask_restful import Api,Resource
from flask.blueprints import Blueprint
from apps.models import User
from error_message import *
from config import db
from flask_httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()
userApi = Blueprint('users', __name__)
user = Api(userApi)
from utlis.common import login_required

@userApi.route("/auth/test")
@login_required
def auth_test():
    return jsonify(code=0,msg="auth")

class AddUsers(Resource):
    @login_required
    def post(self):
        username = request.json.get('username')
        password = request.json.get('password')
        if username is None or password is None:
            return {'code': 400, "msg": core_add_success}
        if User.query.filter_by(username = username).first() is not None:
            return {'code': 400, "msg": users_user_in_db}
        user = User(username = username)
        user.hash_password(password)
        db.session.add(user)
        db.session.commit()
        return {'code':200,"msg":user_user_add_success}
