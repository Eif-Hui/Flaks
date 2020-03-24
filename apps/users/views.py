# -*- coding: utf-8 -*-
# @Time    : 2020/3/8 下午10:37
# @Author  : Hui
# @File    : views.py

from flask import request,jsonify
from flask_restful import Api,Resource
from flask.blueprints import Blueprint
from apps.models import User
from utlis.common import create_token
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

class Login(Resource):
    def post(self):
        res_dir = request.get_json()
        account = res_dir.get("account")
        password = res_dir.get("password")
        if account is None:
            return jsonify({"code":400, "msg":"账户不能为空"})
        if password is None:
            return jsonify({"code":400, "msg":"密码不能为空"})
        if not all([account, password]):
            return jsonify({"code":400, "msg":"账户密码不能为空"})
        try:
            user = User.query.filter_by(account=account).first()
        except Exception:
            return jsonify(code=400, msg=login_user_not_message)
        if user is None or not user.verify_password(password):
            return jsonify({"code":400, "msg":"账户或者密码错误"})
        token = create_token(user.id)
        return jsonify({"code": 200, "msg": "success", "token": token})

class Register(Resource):
    @login_required
    def post(self):
        account = request.json.get('account')
        username = request.json.get('username')
        password = request.json.get('password')
        if account is None or password is None or username is None:
            return jsonify({'code': 400, "msg": "账户密码不能为空"})
        if User.query.filter_by(account = account).first() is not None:
            return jsonify({'code': 400, "msg": "账户已存在"})
        user = User(account = account,username=username)
        user.hash_password(password)
        db.session.add(user)
        db.session.commit()
        return {'code':200,"msg":"账户添加成功"}

    def get(self):
        account = request.json.get('account')
        if account:
            _data = User.query.filter(User.account.like('%{}%'.format(account)))
            if not _data:
                return jsonify({"code": 400, "msg": "没找到该账户"})
        else:
            _data = User.query



