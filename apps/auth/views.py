# -*- coding: utf-8 -*-
# @Time    : 2020/3/10 下午10:20
# @Author  : Hui
# @File    : views.py
from flask import jsonify,request
from flask_restful import Api
from apps.models import User
from error_message import *
from flask.blueprints import Blueprint
from utlis.common import create_token

authApi = Blueprint('auth', __name__)
user = Api(authApi)

@authApi.route('/api/login',methods=["POST"])
def login():
    res_dir = request.get_json()
    username = res_dir.get("username")
    password = res_dir.get("password")
    if username is None:
        return jsonify(code=400, msg= login_user_null_message)
    if password is None:
        return jsonify(code=400,msg=login_pwd_null_message)
    if not all([username, password]):
        return jsonify(code=400, msg=login_req_null_message)
    try:
        user = User.query.filter_by(username=username).first()
    except Exception:
        return jsonify(code=400, msg=login_user_not_message)
    if user is None or not user.verify_password(password):
        return jsonify(code=400, msg=login_user_pwd_error)
    token = create_token(user.id)
    return jsonify({"code":200,"msg":"success","token": token})