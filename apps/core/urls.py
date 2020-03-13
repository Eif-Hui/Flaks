# -*- coding: utf-8 -*-
# @Time    : 2020/3/6 上午10:37
# @Author  : Hui
# @File    : urls.py
"""
引入视图，并根据视图定义API路径
"""
from .views import core,AddTestCase,TestCase

core.add_resource(AddTestCase, '/add/test/case')
core.add_resource(TestCase,'/add/2/test/case')

