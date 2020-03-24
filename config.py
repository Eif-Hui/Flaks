# -*- coding: utf-8 -*-
# @Time    : 2020/3/6 下午12:02
# @Author  : Hui
# @File    : config.py

from flask_sqlalchemy import SQLAlchemy
from apps import app
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:Password.01@120.77.202.176/testcase"
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)


config = {
    'testing': '',
    'SECRET_KEY':"1qaz@wsx3edc"
}
