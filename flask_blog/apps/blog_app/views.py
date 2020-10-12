from flask import Blueprint
from exts import db, cache  # cache缓存
from apps.blog_app.models import *  # 导入模型
from flask import render_template, redirect, url_for, request
from sqlalchemy import or_  # 多条件查询
from flask import session
from flask import jsonify
from flask import g


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
# @cache.cached(timeout=10)  # 视图缓存
def index():
    '''主页'''
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


@app_bp.route('/detail', methods=['GET', 'POST'])
def detail():
    '''文章详情'''
    aid = request.args.get('id')
    # 查询对应的文章
    article = Article.query.get(aid)
    # 查询文章对应评论
    comments = Comment.query.filter(Comment.article_id == aid).all()

    # post请求，添加评论
    if request.method == 'POST':
        if session.get('uid'):
            content = request.form.get('content')
            if len(content) <= 0:
                return render_template('blog/detail.html', article=article, comments=comments, msg='评论不能为空')
            comment = Comment()
            comment.content = content
            comment.article_id = int(aid)
            comment.user_id = int(session.get('uid'))
            db.session.add(comment)
            db.session.commit()

            aid = request.args.get('id')
            # 查询对应的文章
            article = Article.query.get(aid)
            # 查询文章对应评论
            comments = Comment.query.filter(Comment.article_id == aid).all()

            return render_template('blog/detail.html', article=article, comments=comments)
        else:
            return redirect(url_for('user.login'))
    return render_template('blog/detail.html', article=article, comments=comments)


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