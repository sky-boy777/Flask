from flask import Flask
import settings
from ext import db
from apps.user.views import user_dp

def creat_app():
    # 创建app
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    app.config.from_object(settings)    # 加载配置
    db.init_app(app)  # 将db对象与app进行关联
    app.register_blueprint(user_dp)  # 注册蓝图
    return app