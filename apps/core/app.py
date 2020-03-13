# # -*- coding: utf-8 -*-
# # @Time    : 2020/1/18 下午5:06
# # @Author  : Hui
# # @File    : views.py
#
# from flask import Flask,jsonify,request
# from connect_db import insert_database
#
# app = Flask(__name__)
#
# @app.route('/api/v1.0/tasks', methods=['post','get'])
# def get_tasks():
#     """获取请求参数"""
#     #dd = request.json.get('DDD')  # json
#     #aa = request.form.get('dd')  #  from
#     aw = request.get_json()
#     ww = aw.get("dd")
#     return jsonify({'tasks': ww})
#
# @app.route('/db/testCase/dataCollect', methods=['post'])
# def dataCollect():
# #判断接口的请求方式是GET还是POST,POST传值，GET获取统计
#     if request.method == 'POST':
#         # 获取请求参数是json格式，返回结果是字典
#         caseId = request.json.get('caseId')
#         story = request.json.get('story')
#         title = request.json.get('title')
#         method = request.json.get('method')
#         path = request.json.get('path')
#         req_data = request.json.get('req_data')
#         sql = request.json.get('sql')
#         expect1 = request.json.get('expect1')
#         expect2 = request.json.get('expect2')
#         expect3 = request.json.get('expect3')
#         if (len(caseId)> 0 )&(len(story)> 0 )&(len(title)> 0 )&(len(method)> 0 )&(len(path)> 0 )\
#                 &(len(req_data)> 0 )&(len(sql)>0)&(len(expect1)>0)&(len(expect2)>0)&(len(expect3)>0):  #判断不为空，则写入数据库
#             sql_insert = "insert into TestCaseList value(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
#             insert_database(sql_insert,caseId,story,title,method,path,req_data,sql,expect1,expect2,expect3)
#             return jsonify({"code": 200, "msg": "Data insert successful."})
#         else:
#             return jsonify({"code": 400, "msg": "Incomplete data , please check."})
#
#
# if __name__ == '__main__':
#     app.run(debug=True)