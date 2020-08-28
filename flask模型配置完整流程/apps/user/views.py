from flask import Blueprint
from flask import render_template

# 创建蓝图
user_dp = Blueprint('user', __name__)

# 路由、请求方法、反向解析
@user_dp.route('/register', methods=['GET', 'POST'], endpoint='register')
def register():
    '''用户注册'''
    return render_template('user/register.html')  # 模板渲染