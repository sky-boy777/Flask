from ext import db
from datetime import datetime

# 创建模型
class User(db.Model):
    '''用户表'''
    #                  整形      主键                自动增长
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(30), nullable=False, unique=True)  # 不能为空，唯一
    password = db.Column(db.String(255), nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now())  # 时间

    def __str__(self):
        return self.username