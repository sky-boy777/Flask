from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_caching import Cache  # 缓存

db = SQLAlchemy()  # 数据库
bootstrap = Bootstrap()  # bootstrap
cache = Cache()