from flask import Flask
import settings
from apps.blog_app.views import app_bp  # 主模块
from apps.user_app.views import user_bp  # 用户模块
from exts import db, bootstrap, cache
from flask_bootstrap import Bootstrap
from flask_wtf.csrf import CsrfProtect  # 全局的csrf保护

csrf = CsrfProtect()

def create_app():
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    app.config.from_object(settings)
    db.init_app(app)  # 初始化db
    # 初始化csrf，需要配置SECRET_KEY
    csrf.init_app(app=app)

    # 初始化缓存文件
    cache.init_app(app=app, config={
        'CACHE_TYPE': 'redis',  # 缓存类型
        # 'CACHE_REDIS_HOST': 'localhost',  # 地址，默认使用0号数据库
        # 'CACHE_REDIS_PORT': 6379  # 端口号
        'CACHE_REDIS_URL': 'redis://@localhost:6379/2'  # 无密码， 有密码：redis://user:password@localhost:6379/2
    })

    # 初始化bootstrap两种方法
    bootstrap.init_app(app)
    # Bootstrap(app)

    # 注册蓝图(模块：user_app,blog_app...)
    app.register_blueprint(app_bp)
    app.register_blueprint(user_bp)

    return app
