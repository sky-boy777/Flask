# 在这里自定义配置
DEBUG = True
ENV = 'development'  # 开发环境，生产环境:production

# 配置参考：http://www.pythondoc.com/flask-sqlalchemy/config.html
#                          数据库+驱动       用户  密码  主机      端口号 数据库名
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:mysql@127.0.0.1:3306/flask'  # 连接数据库
SQLALCHEMY_TRACK_MODIFICATIONS = False  # 不追踪对象，减少内存开销，默认为True
SQLALCHEMY_ECHO = True  # 记录所有 发到标准输出(stderr)的语句，这对调试很有帮助。