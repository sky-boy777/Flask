# ORM   类-----表
# 对象----表中的一条记录
from ext import db  # 跟django差不多
from datetime import datetime

# 模型
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 主键、自动增长
    username = db.Column(db.String(30), nullable=False, unique=True)  # 不能为空、唯一
    password = db.Column(db.String(255), nullable=False)
    register_time = db.Column(db.DateTime, default=datetime.now())  # 注册时间
    # is_delete = db.Column(db.Integer,default=1)  # 是否逻辑删除，1否，0是

    # 直接打印User会输出username
    def __str__(self):
        return self.username
