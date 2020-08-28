from flask import Blueprint
from flask import render_template, url_for, request
from .models import User
from ext import db

# 相当于app
user_bp = Blueprint('user', __name__)

@user_bp.route('/register', methods=['GET', 'POST'], endpoint='register')  # 路由，请求方法，反向解析
def register():
    '''注册'''
    if request.method == 'POST':
        # 注册
        # username = request.form.get('username')  # post
        user = User()
        user.username = '张三'
        user.password = '123456'

        # 创建一个新用户对象
        db.session.add(user)
        # 提交保存
        db.session.commit()
        return '注册成功'
    # username = request.args.get('username')  # get
    user = User()
    user.username = '张三'
    user.password = '123456'

    # 创建一个新用户对象
    db.session.add(user)
    # 提交保存
    db.session.commit()
    return render_template('user/register.html')  # 渲染模板

@user_bp.route('/login', methods=['GET', 'POST'], endpoint='login')  # 未设置endpoint默认使用函数名login
def login():
    print(url_for('user.login'))  # 用户模块下的登录页, /login
    return '用户登录'

