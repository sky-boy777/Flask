from flask import Flask
import settings
from apps.blog_app.views import app_bp  # 主模块
from apps.user_app.views import user_bp  # 用户模块
from exts import db

def create_app():
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    app.config.from_object(settings)
    db.init_app(app)

    # 注册蓝图(模块：user_app,blog_app...)
    app.register_blueprint(app_bp)
    app.register_blueprint(user_bp)

    return app
