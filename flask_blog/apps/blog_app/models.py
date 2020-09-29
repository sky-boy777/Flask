# ORM   类-----表
# 对象----表中的一条记录
from exts import db  # 跟django差不多
from datetime import datetime
import os
import settings

# 数据库模型都在这里创建
class Article_type(db.Model):
    '''文章类型'''
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type_name = db.Column(db.String(30), nullable=False)  # 类型名称

    # 类型下的文章列表
    articles = db.relationship('Article', backref='article_type')


class Article(db.Model):
    '''文章表'''
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 主键、自动增长
    title = db.Column(db.String(50), nullable=False)  # 文章标题
    content = db.Column(db.Text, nullable=False)  # 文章内容
    create_time = db.Column(db.DateTime, default=datetime.now())  # 发布时间
    click_num = db.Column(db.Integer, default=0)  # 浏览量
    save_num = db.Column(db.Integer, default=0)  # 收藏数
    love_num = db.Column(db.Integer, default=0)  # 喜欢（点赞）数

    # 评论数
    comments = db.relationship('Comment', backref='article')  # 一篇文章多个评论
    # 文章类型外键
    type_id = db.Column(db.Integer, db.ForeignKey('article_type.id'), nullable=False)
    # 文章作者外键，文章属于哪个用户
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # 文章属于哪个用户，外键


    # 建立多对多关系：评论、用户、文章
    # users = db.relationship('User', backref='article', secondary='comment')

    def __str__(self):
        return self.title


class User(db.Model):
    '''用户表'''
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 主键、自动增长
    username = db.Column(db.String(30), nullable=False)  # 用户名
    password = db.Column(db.String(255), nullable=False)  # 密码
    phone = db.Column(db.String(11), unique=True, nullable=False)  # 手机,唯一
    # 用户头像，保存文件路径
    icon = db.Column(db.String(255), default='upload/icon/default_icon.jpg')
    register_time = db.Column(db.DateTime, default=datetime.now())  # 注册时间
    is_delete = db.Column(db.Boolean, default=False)  # 是否逻辑删除，False否，True是

    # 一对多关系：一个用户多篇文章：关联查询
    # 建立文章跟用户的关系       1、对应哪个类  2、反向引用：Arcitle.user.username
    articles = db.relationship('Article', backref='user')  # 不用迁移，不在数据库层面

    # 直接打印User会输出username
    def __str__(self):
        return self.username


class Comment(db.Model):
    '''评论表'''
    # 自定义表名
    # __tablename = '表名'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.String(255))  # 评论内容
    create_time = db.Column(db.DateTime, default=datetime.now())  # 评论时间

    # 外键：评论的用户，评论的文章
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    article_id = db.Column(db.Integer, db.ForeignKey('article.id'), nullable=False)






# 多对多关系练习（用户跟商品）
# class Goods(db.Model):
#     '''商品表'''
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     title = db.Column(db.String(20), nullable=False)
#     price = db.Column(db.Float, nullable=False)
#
#     # 关联表                  模型名            反向                   表名:数据库里面
#     users = db.relationship('User', backref='goods', secondary='user__goods')
#
# class User_Goods(db.Model):
#     '''多对多辅助表'''
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#     goods_id = db.Column(db.Integer, db.ForeignKey('goods.id'), nullable=False)
#     num = db.Column(db.Integer, default=1)  # 商品数量
