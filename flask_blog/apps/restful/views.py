from flask import Blueprint, jsonify
from flask_restful import Resource, fields, marshal_with, reqparse, inputs
from werkzeug.datastructures import FileStorage  # 表单接收图片
from exts import api
from apps.blog_app.models import *
from flask import url_for


# 创建蓝图
restful_bp = Blueprint('restful', __name__, url_prefix='/api')

# 自定义fields的value值，必须继承fields.Raw,必须重写format方法
class isDelete(fields.Raw):
    def format(self, value):
        return '删除' if value else '未删除'

# 使用Url，产生一个链接，点击进入详情，相当于在user_fields前面加了一层
user_fields1 = {
    'username': fields.String,
    'uri': fields.Url(endpoint='single_user', absolute=True),  # endpoint为api的endpoint
}

# 用户表的字段，需跟数据库字段名一致,序列化json返回给前端（get），key默认为模型字段名
user_fields = {
    'id': fields.Integer,

    # 'username': fields.String,
    'name': fields.String(attribute='username', default='匿名'),  # attribute='数据库真实字段名'，为了不给前端显示数据库的字段名

    'register_time': fields.DateTime(dt_format='iso8601'),  # dt_format:日期格式
    'is_delete': isDelete,  # 使用自定义的fields
}

# 请求解析，就是表单验证
parser = reqparse.RequestParser(bundle_errors=True)  # bundle_errors=True，会将所有验证不通过的message返回
#                     表单的name            类型         必填         错误返回的信息    只要form表单提交的数据
parser.add_argument(name='username', type=str, required=True, help='用户名', location=['form'])
parser.add_argument(name='password', type=str, required=True, help='密码', location=['form', 'args'])
parser.add_argument(name='phone', type=inputs.regex(r'^1[8]\d{9}$'), required=True, help='手机号')
parser.add_argument('hobby', action='append')  # 列表形式：['旅游', '打球']
parser.add_argument('icon', type=FileStorage, location='files')  # 接收图片


# 类视图ss
# 对多个用户操作
class UsersResource(Resource):
    @marshal_with(user_fields1)  # 将返回的数据序列化
    def get(self):
        '''查询'''
        users = User.query.all()
        return users

    def post(self):
        '''增加'''
        # 获取post提交数据
        args = parser.parse_args()
        username = args.get('username')
        password = args.get('password')
        phone = args.get('phone')
        hobby = args.get('hobby')
        # 头像
        icon = args.get('icon')
        if icon:
            icon.save(os.path.join(settings.UPLOAD_ICON_DIR, icon.filename))  # 图片保存，里面填路径
        return jsonify(username, password, phone, hobby)

    def put(self):
        '''更改'''
        print('endpoint(别名)的使用：', url_for('uuu'))
        return {'msg': 'ok'}

    def delete(self):
        '''删除'''
        return 'delete'


# 对单个用户操作，路径传参
class UserResource(Resource):
    @marshal_with(user_fields)  # 将返回的数据序列化
    def get(self, id):
        user = User.query.get(id)
        return user

    def put(self):
        print('***************************************endpoint(别名)的使用：', url_for('uuu'))
        return 'ok'



# （类视图，路径），必须添加，不然访问不到
api.add_resource(UsersResource, '/user', endpoint='user')  # endpoint:别名,反向解析url_for()
# 路径传参，用户id，因为上面使用了fields.Url，所以要跟数据库字段一致
api.add_resource(UserResource, '/user/<int:id>', endpoint='single_user')
