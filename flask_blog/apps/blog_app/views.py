from flask import Blueprint
from exts import db
from apps.blog_app.models import *  # 导入模型
from flask import render_template, redirect, url_for, request
from sqlalchemy import or_  # 多条件查询
from flask import session
from flask import jsonify


app_bp = Blueprint('app', __name__)

# 自定义过滤器,用于蓝图
@app_bp.app_template_filter('cut_off')
def cut_off(value):
    # 切片
    return value[:29] + '......'

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

    # articles = Article.query.order_by(-Article.create_time).all()  # 查询出全部的文章,按时间降序

    p = int(request.args.get('page', 1))  # 页码要为整形
    # 分页,当前页，每页几条,返回分页对象（pagination）
    page = Article.query.order_by(-Article.create_time).paginate(page=p, per_page=2, max_per_page=20)


    print(page.items)  # 当前页的每条记录对象,列表类型
    print(page.page)  # 当前页码
    print(page.prev_num)  # 前一页页码
    print(page.next_num)  # 后一页页码
    print(page.has_next)  # 是否有下一页（true， false）
    print(page.has_prev)  # 是否有上一页
    print(page.pages)  # 总页数
    print(page.total)  # 数据库的总的记录数

    # 获取cookie
    # uid = request.cookies.get('uid', None)  # 获取cookie值

    # 获取session
    uid = session.get('uid')
    if uid:
        user = User.query.get(uid)
        return render_template('index.html', user=user, page=page)
    return render_template('index.html', page=page)


@app_bp.route('/detail')
def detail():
    '''文章详情'''
    aid = request.args.get('id')
    article = Article.query.get(aid)
    return render_template('blog/detail.html', article=article)

@app_bp.route('/love_num')
def love_num():
    tag = request.args.get('tag')
    aid = request.args.get('aid')
    if tag == '1':
        article = Article.query.get(aid)
        article.love_num += 1
        db.session.commit()
    else:
        article = Article.query.get(aid)
    return jsonify({'code': 200, 'num': article.love_num})