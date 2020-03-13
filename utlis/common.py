# -*- coding: utf-8 -*-
# @Time    : 2020/3/10 下午9:23
# @Author  : Hui
# @File    : common.py

from apps.models import User
from config import config
from flask import request, jsonify
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
import functools

def login_required(view_func):
    @functools.wraps(view_func)
    def verify_token(*args, **kwargs):
        try:
            token = request.headers["Authorization"]
        except Exception:
            return jsonify(code=4103, msg='身份信息校验失败')
        s = Serializer(config["SECRET_KEY"])
        try:
            s.loads(token)
        except Exception:
            return jsonify(code=4101, msg="身份信息校验已过期")
        return view_func(*args, **kwargs)
    return verify_token

def create_token(api_user):
    '''
    :param api_user:用户id
    :return: token
    '''
    s = Serializer(config["SECRET_KEY"], expires_in=3600)
    token = s.dumps({"id": api_user}).decode("ascii")
    return token

def verify_token(token):
    '''
    校验token
    :param token:
    :return: 用户信息 or None
    '''
    s = Serializer(config["SECRET_KEY"])
    try:
        data = s.loads(token)
    except Exception:
        return None
    user = User.query.get(data["id"])
    return user