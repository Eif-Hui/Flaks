# -*- coding: utf-8 -*-
# @Time    : 2020/1/18 下午5:06
# @Author  : Hui
# @File    : views.py
import datetime
from flask import request,jsonify
from apps.models import Test
from config import db
from error_message import *
from flask_restful import Api, Resource
from flask.blueprints import Blueprint

coreApi = Blueprint('core', __name__)
core = Api(coreApi)


class TestCase(Resource):
    def post(self):
        case_id = '{0:%Y%m%d%H%M%S}'.format(datetime.datetime.now())[4:]
        req = request.get_json()
        story = req.get('story')
        title = req.get('title')
        method = req.get('method')
        path = req.get('path')
        req_data = req.get('req_data')
        sql = req.get('sql')
        expect1 = req.get('expect1')
        expect2 = req.get('expect2')
        expect3 = req.get('expect3')
        if (len(story)> 0 )&(len(title)> 0 )&(len(method)> 0 )&(len(path)> 0 )\
                &(len(req_data)> 0 )&(len(sql)> 0 )&(len(expect1) > 0)&(len(expect2) > 0)&(len(expect3) > 0):
            req_dict = Test(caseId = case_id,story=story,title=title,method=method,path=path,
                            req_data=req_data,sql=sql,expect1=expect1,expect2=expect2,expect3=expect3)
            db.session.add(req_dict)
            db.session.commit()
            return {"code":200,"msg":core_add_success}
        else:
            return {"code": 400, "msg": "Incomplete data , please check."}

    def get(self):
        title = request.args.get('title')
        results = Test.query.filter_by(title=title).first()
        return {"code":0,"msg":"success","data":results.story}

    def put(self):
        title = request.json.get('title')
        results = Test.query.filter_by(title=title).first()
        results.title = title
        db.session.commit()




