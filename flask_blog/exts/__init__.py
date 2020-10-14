from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_caching import Cache  # 缓存

from flask_restful import Api  # restful api


db = SQLAlchemy()  # 数据库
bootstrap = Bootstrap()  # bootstrap
cache = Cache()

# restful api  需要在apps下的__init__初始化
api = Api()