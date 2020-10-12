import os

# 在这里自定义配置
DEBUG = True
ENV = 'development'  # 开发环境，生产环境:production

# 配置参考：http://www.pythondoc.com/flask-sqlalchemy/config.html
#                          数据库+驱动       用户  密码  主机      端口号 数据库名
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:mysql@127.0.0.1:3306/flask_blog'  # 连接数据库
SQLALCHEMY_TRACK_MODIFICATIONS = False  # 不追踪对象，减少内存开销，默认为True
SQLALCHEMY_ECHO = True  # 记录所有 发到标准输出(stderr)的语句，这对调试很有帮助。

SECRET_KEY = 'kdfuiefjk4343424@&&$^@&$@&$&@^$&fkjksjfkdsf'


# 项目路径
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# 静态文件
STATIC_DIR = os.path.join(BASE_DIR, 'static')
# 模板
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
# 上传文件路径
UPLOAD_DIR = os.path.join(BASE_DIR, 'static/upload')
# 头像图片文件路径
UPLOAD_ICON_DIR = os.path.join(BASE_DIR, 'static/upload/icon')