from apps import create_app  # 创建app
from flask_script import Manager  # 给app套壳
from flask_migrate import Migrate, MigrateCommand  # 数据库命令工具,执行迁移一些操作
from ext import db  # 数据库映射对象
from apps.user.models import User  # 导入模型

app = create_app()
manager = Manager(app=app)  # 套一个壳

# 数据库命令工具,迁移什么的
migrate = Migrate(app=app, db=db)
manager.add_command('db', MigrateCommand)  # 添加数据库的一些迁移操作到manager壳,跟python数据库迁移操作差不多


# 自定义命令行命令(了解)：python app.py aa
# @manager.command
# def aa():
#     print('这是自定义的')

if __name__ == '__main__':
    # app.run(port=8000)
    manager.run()  # 命令行启动：python app.py runserver -p 端口 —h 主机
