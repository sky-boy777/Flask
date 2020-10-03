from flask import Blueprint
from exts import db
from apps.blog_app.models import *  # 导入模型
from flask import render_template, redirect, url_for, request
from sqlalchemy import or_  # 多条件查询
from flask import session


app_bp = Blueprint('app', __name__)

# 自定义过滤器,用于蓝图
@app_bp.app_template_filter('cut_off')
def cut_off(value):
    # 切片
    return value[:50] + '......'

# 用于应用程序的过滤器
# @app_bp.add_app_template_filter('aa')
# def cut_off(value):
#     return value[:50] + '......'


@app_bp.route('/', methods=['GET', 'POST'], endpoint='index')
def index():
    '''主页'''
    # c = Comment()
    # c.article_id = 2
    # c.content = '这是一条评论'
    # c.user_id = 1
    # db.session.add(c)
    # db.session.commit()

    articles = Article.query.order_by(-Article.create_time).all()  # 查询出全部的文章,按时间降序

    # 获取cookie
    # uid = request.cookies.get('uid', None)  # 获取cookie值

    # 获取session
    uid = session.get('uid')
    if uid:
        user = User.query.get(uid)
        return render_template('index.html', user=user, articles=articles)


    return render_template('index.html', articles=articles)