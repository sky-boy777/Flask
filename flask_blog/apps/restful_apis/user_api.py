# flask-restful: api蓝图练习
from flask import Blueprint
from flask_restful import Api, Resource, fields, marshal_with, reqparse, marshal, abort
from apps.blog_app.models import *

api_user_bp = Blueprint('user_api', __name__, url_prefix='/user_api')
api = Api(api_user_bp)

# 输入验证（表单）
parser = reqparse.RequestParser()
# post:form, get:args
# parser.add_argument(name='username', required=True, help='用户名', location=['form', 'args'])

# 输出格式
user_fields = {
    'id': fields.Integer,
    'name': fields.String(attribute='username', default='匿名'),
    'register_time': fields.DateTime(dt_format='iso8601'),  # dt_format:日期格式
}

class UserList(Resource):
    @marshal_with(user_fields)
    def get(self):
        users = User.query.all()
        if not users:
            abort(400, msg='这是异常')  # abort抛出异常，状态码是内置的，msg可自定义
        return users


# 用户登录或注册
class UserRegister(Resource):
    def post(self):
        # 接收参数
        args = parser.parse_args()
        username = args.get('username')

        # 演示输出数据，注册成功返回用户
        user = User.query.get(1)

        data = marshal(user, user_fields)
        # 使用marshal格式化数据
        return {'success': True,  # 是否成功（布尔值）
                'status': 200,  # 状态码（数字）
                'msg': '注册成功',  # 消息（字符串）
                'data': data,  # 数据，键值对形式
                }


api.add_resource(UserList, '/users')
api.add_resource(UserRegister, '/api_register')