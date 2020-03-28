# -*- coding: utf-8 -*-
# @Time    : 2020/3/8 下午10:37
# @Author  : Hui
# @File    : urls.py
from .views import user,Register,Login

user.add_resource(Login,'/api/login')
user.add_resource(Register,'/api/add/register')