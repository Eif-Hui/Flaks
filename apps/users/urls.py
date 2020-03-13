# -*- coding: utf-8 -*-
# @Time    : 2020/3/8 下午10:37
# @Author  : Hui
# @File    : urls.py
from .views import user,AddUsers

user.add_resource(AddUsers,'/api/add/users')