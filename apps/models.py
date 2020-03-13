# -*- coding: utf-8 -*-
# @Time    : 2020/3/6 上午11:18
# @Author  : Hui
# @File    : models.py
from config import db
from config import config
from passlib.apps import custom_app_context as pwd_context
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer,SignatureExpired,BadSignature
# 创建模型对象

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(32), index = True)
    password_hash = db.Column(db.String(128))

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)




# def __repr__(self):
#     return '<User %r>' % self.username

class Test(db.Model):
    __tablename__ = "TestCase"
    id = db.Column(db.Integer, primary_key=True)
    caseId = db.Column(db.String(120),unique=True,nullable=False,comment='用例ID')
    story = db.Column(db.String(250),nullable=False,comment='用例模块')
    title = db.Column(db.String(250),nullable=False,comment='用例标题')
    method = db.Column(db.String(250), nullable=False,comment='请求方法')
    path = db.Column(db.String(250),nullable=False,comment='请求路径')
    req_data = db.Column(db.String(250),nullable=False,comment='请求参数')
    sql = db.Column(db.String(250),nullable=False,comment='数据库查询语句')
    expect1 = db.Column(db.String(120),nullable=False,comment='预期结果1')
    expect2 = db.Column(db.String(120),nullable=False,comment='预期结果2')
    expect3 = db.Column(db.String(120),nullable=False,comment='预期结果3')


#
# def __repr__(self):
#     return '<TestCase %r>' % self.case_id

if __name__ == '__main__':

    db.drop_all()
    db.create_all()