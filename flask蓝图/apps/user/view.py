from flask import Blueprint
from flask import render_template, url_for, request, redirect
from .models import User
from ext import db
import hashlib
from sqlalchemy import or_, and_, not_  # or查询, and查询, not(非)不包含

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
        user.password = hashlib.sha256(password.encode('utf-8')).hexdigest()  # 加密，先编码转换才能使用加密
        # 添加并保存
        db.session.add(user)
        db.session.commit()
        return '注册成功'

    # username = request.args.get('username')  # get
    return render_template('user/register.html')  # 渲染模板

@user_bp.route('/login', methods=['GET', 'POST'], endpoint='login')  # 未设置endpoint默认使用函数名login
def login():
    # al = User.query.all()  # 查询全部
    # user = User.query.get(1)  # 根据主键查询
    # user1 = User.query.filter_by(username='bbb').first()  # 加first()表示取第一个
    # user2 = User.query.filter(User.username == 'aaa').first()  # 最常用,里面是布尔条件,first()表示取第一个，all()取全部
    # User.query.limit(1).all()  # 返回指定的记录数
    User.query.order_by(-User.register_time).all()  # 降序排序
    print('*' * 30)
    print(User.query.offset(2).limit(1).all())
    return render_template('user/login.html')


@user_bp.route('/user_list', methods=['GET', 'POST'], endpoint='user_list')
def user_list():
    users = User.query.all()
    return render_template('user/user_list.html', users=users)

@user_bp.route('/search', endpoint='search')
def search():
    keyword = request.args.get('keyword')
    users = User.query.filter(User.username.contains(keyword))  # 包含查询
    return render_template('user/user_list.html', users=users)

@user_bp.route('/delete', endpoint='delete')
def delete():
    user_id = request.args.get('id')
    user = User.query.get(user_id)
    # 提交到缓存
    db.session.delete(user)
    # 提交删除
    db.session.commit()

    return redirect(url_for('user.user_list'))

@user_bp.route('/update', methods=['GET', 'POST'], endpoint='update')
def update():
    if request.method == 'POST':
        username = request.form.get('username')
        user_id = request.form.get('user_id')
        # 根据id查询用户
        user = User.query.get(user_id)
        # 更新用户信息
        user.username = username
        # 提交
        db.session.commit()
        return redirect(url_for('user.user_list'))
    else:
        user_id = request.args.get('id')
        user = User.query.get(user_id)
        return render_template('user/update.html', user=user)
