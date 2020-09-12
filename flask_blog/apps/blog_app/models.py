# ORM   类-----表
# 对象----表中的一条记录
from apps import db  # 跟django差不多
from datetime import datetime

# 模型
class Arcitle():
    '''文章表'''
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 主键、自动增长
    title = db.Column(db.String(50), nullable=False)  # 文章标题
    # content = db.Column()

    # 外键
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # 文章属于哪个用户，外键


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 主键、自动增长
    username = db.Column(db.String(30), nullable=False)  # 用户名
    password = db.Column(db.String(255), nullable=False)  # 密码
    phone = db.Column(db.String(11), unique=True, nullable=False)  # 手机,唯一
    register_time = db.Column(db.DateTime, default=datetime.now())  # 注册时间
    is_delete = db.Column(db.Boolean, default=False)  # 是否逻辑删除，False否，True是

    # 直接打印User会输出username
    def __str__(self):
        return self.username
