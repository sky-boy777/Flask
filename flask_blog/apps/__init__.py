from flask import Flask
import settings
from apps.blog_app.views import app_bp  # 主模块
from apps.user_app.views import user_bp  # 用户模块
from exts import db, bootstrap, cache
from flask_bootstrap import Bootstrap

# redis缓存配置
config = {
    'CACHE_TYPE': 'redis',
    'CACHE_REDIS_HOST': '127.0.0.1',
    'CACHE_REDIS_PORT': 6379
}

def create_app():
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    app.config.from_object(settings)
    db.init_app(app)  # 初始化db

    # 初始化缓存文件
    cache.init_app(app=app)

    # 初始化bootstrap两种方法
    bootstrap.init_app(app)
    # Bootstrap(app)

    # 注册蓝图(模块：user_app,blog_app...)
    app.register_blueprint(app_bp)
    app.register_blueprint(user_bp)

    return app
