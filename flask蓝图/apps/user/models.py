# ORM   类-----表
# 对象----表中的一条记录
from ext import db  # 跟django差不多
from datetime import datetime

# 模型
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 主键、自动增长
    username = db.Column(db.String(30), nullable=False, unique=True)  # 不能为空、唯一
    password = db.Column(db.String(255), nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now())  # 注册时间

    def __str__(self):
        return self.username
