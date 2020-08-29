from flask import Blueprint
from flask import render_template, url_for, request
from .models import User
from ext import db
import hashlib

# 相当于app
user_bp = Blueprint('user', __name__)

@user_bp.route('/register', methods=['GET', 'POST'], endpoint='register')  # 路由，请求方法，反向解析
def register():
    '''注册'''
    if request.method == 'POST':
        # 获取
        username = request.form.get('username')
        password = request.form.get('password')
        # 注册
        user = User()
        user.username = username
        user.password = hashlib.sha256(password.encode('utf-8'))  # 加密，先编码转换才能使用加密
        # 添加并保存
        db.session.add(user)
        db.session.commit()
        return '注册成功'

    # username = request.args.get('username')  # get
    return render_template('user/register.html')  # 渲染模板

@user_bp.route('/login', methods=['GET', 'POST'], endpoint='login')  # 未设置endpoint默认使用函数名login
def login():

    return '用户登录'

