# -*- coding: utf-8 -*-
# @Time    : 2020/3/8 下午10:37
# @Author  : Hui
# @File    : views.py

from flask import request,jsonify,json
from flask_restful import Api,Resource
from flask.blueprints import Blueprint
from apps.models import User
from utlis.common import create_token
from config import db
from flask_httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()
userApi = Blueprint('users', __name__)
user = Api(userApi)
from utlis.common import login_required

@userApi.route("/auth/test",methods=['post','get'])
def auth_test():
    return jsonify({"result":1,"message":"查询成功","data":[{"warehouseId":410,"warehouseCode":"xiaoye_JYK","warehouseName":"徐小爷金银库"},{"warehouseId":401,"warehouseCode":"daye_JYK","warehouseName":"徐大爷金银库"},{"warehouseId":370,"warehouseCode":"CK001","warehouseName":"默认仓库"}],"success":True})

# class Login(Resource):
#     def post(self):
#         res_dir = request.get_json()
#         account = res_dir.get("account")
#         password = res_dir.get("password")
#         if account is None:
#             return jsonify({"code":400, "msg":"账户不能为空"})
#         if password is None:
#             return jsonify({"code":400, "msg":"密码不能为空"})
#         if not all([account, password]):
#             return jsonify({"code":400, "msg":"账户密码不能为空"})
#         try:
#             user = User.query.filter_by(account=account).first()
#         except Exception:
#             return jsonify(code=400, msg=login_user_not_message)
#         if user is None or not user.verify_password(password):
#             return jsonify({"code":400, "msg":"账户或者密码错误"})
#         token = create_token(user.id)
#         return jsonify({"code": 200, "msg": "success", "token": token})

class Login(Resource):
    def post(self):
        if request.json:
            data = request.json
        elif request.form:
            data = request.form
        else:
            data = request.data
            data = bytes.decode(data)
            data = json.loads(data)
        account = data.get('account')
        password = data.get('password')
        user = User.query.filter_by(account=account).first()
        if user is None:
            return jsonify({'msg': '账号错误或不存在', 'code': 400})
        elif not  user.verify_password(password):
            return jsonify({'msg': '密码错误', 'code': 400})
        else:
            token = create_token(user.id)
            return jsonify({'msg': '登录成功', 'code': 200,'name': user.username,
                            'userId': user.id, 'token': token})


class Register(Resource):
    @login_required
    def post(self):
        """
        修改添加用户
        :return:
        """
        account = request.json.get('account')
        username = request.json.get('username')
        password = request.json.get('password')
        new_password = request.json.get('new_password')
        user_id = request.json.get('id')
        if user_id:
            old_data = User.query.filter_by(id=user_id).first()
            if User.query.filter_by(username=username).first() and username != old_data.username:
                return jsonify({'msg': '名字已存在', 'code': 400})
            elif User.query.filter_by(account=account).first() and account != old_data.account:
                return jsonify({'msg': '账号已存在', 'code': 400})
            if new_password:
                if not password:
                    return jsonify({"code":400,"msg":"密码不能为空"})
                else:
                    old_data.password = password
            old_data.username = username
            db.session.commit()
            return jsonify({"code":200,"msg":"修改成功"})
        else:
            if account is None or password is None or username is None:
                return jsonify({'code': 400, "msg": "账户密码不能为空"})
            if User.query.filter_by(account = account).first() is not None:
                return jsonify({'code': 400, "msg": "账户已存在"})
            user = User(account = account,username=username)
            user.hash_password(password)
            db.session.add(user)
            db.session.commit()
            return jsonify({'code':200,"msg":"账户添加成功"})


    @login_required
    def get(self):
        """
        获取用户信息
        :return:
        """
        account = request.args.get('account')
        _data = User.query.filter(User.account == account).first()
        if not _data:
            return jsonify({"code":400,"msg":"账户不存在"})
        else:
            return jsonify({"userId":_data.id,"username":_data.username,"account":_data.account})

    @login_required
    def put(self):
        """
        修改账户密码
        :return:
        """
        data = request.json
        account = data.get('account')
        old_password = data.get('oldPassword')
        new_password = data.get('newPassword')
        sure_password = data.get('surePassword')
        _data = User.query.filter(User.account == account).first()
        if not _data:
            return jsonify({"code":400,"msg":"账户不存在"})
        if not User.hash_password(old_password):
            return jsonify({'msg': '旧密码错误', 'code': 400})
        if not new_password:
            return jsonify({'msg': '新密码不能为空', 'code': 400})
        if new_password != sure_password:
            return jsonify({'msg': '新密码和确认密码不一致', 'code': 400})
        User.password_hash = User.hash_password(new_password)
        db.session.add()
        db.session.commit()
        return jsonify({'msg': '密码修改成功', 'code': 200})

    def delete(self):
        """
        删除用户
        :return:
        """
        user_id = request.json.get('id')
        old_data = User.query.filter_by(id=user_id).first()
        if not old_data:
            return jsonify({"code":400,"msg":"用户Id不存在"})
        else:
            old_data.delete()
            #User.query.filter_by(id=user_id).delete()
            return jsonify({"code":200,"msg":"删除成功"})





