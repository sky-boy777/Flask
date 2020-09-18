from flask import Blueprint
from exts import db
from apps.blog_app.models import *  # 导入模型
from flask import render_template, redirect, url_for, request
from sqlalchemy import or_  # 多条件查询
from flask import session


app_bp = Blueprint('app', __name__)

@app_bp.route('/', methods=['GET', 'POST'], endpoint='index')
def index():
    # 获取cookie
    # uid = request.cookies.get('uid', None)  # 获取cookie值

    # 获取session
    uid = session.get('uid')

    if uid:
        user = User.query.get(uid)
        return render_template('index.html', user=user)
    return render_template('index.html')