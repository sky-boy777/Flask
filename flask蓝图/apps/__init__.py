from flask import Flask
import settings  # 导入配置
from apps.user.view import user_bp  # 导入用户模块
from ext import db  # 导入db对象，ext下面的__init__

def create_app():
    # 创建app，并且指定templates、static文件夹位置,一般跟创建apps的目录同级，为了好看放在外面了，或者把文件夹放进来
    app = Flask(__name__, template_folder='../templates', static_folder='../static')  # app,一个核心对象
    app.config.from_object(settings)  # 加载配置
    db.init_app(app)  # 将db对象与app进行关联

    # 蓝图
    app.register_blueprint(user_bp)  # 将蓝图对象注册到app

    return app  # 返回app对象