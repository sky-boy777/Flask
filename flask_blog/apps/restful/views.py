from flask import Blueprint
from flask_restful import Resource, fields, marshal_with
from exts import api
from apps.blog_app.models import *

# 创建蓝图
restful_bp = Blueprint('restful', __name__, url_prefix='/api')

# 用户表的字段，需跟数据库字段名一致
user_fields = {
    'username': fields.String,
}

# 类视图
class RestfulResource(Resource):
    @marshal_with(user_fields)
    def get(self):
        '''查询'''
        users = User.query.all()
        return users

    def post(self):
        '''增加'''
        return 'post'

    def put(self):
        '''更改'''
        return 'put'

    def delete(self):
        '''删除'''
        return 'deletd'


# api资源（类视图，路径），必须添加，不然访问不到
api.add_resource(RestfulResource, '/rest')
