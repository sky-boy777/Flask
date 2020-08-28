from apps import creat_app
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from ext import db
from apps.user.models import User  # 必须导入已创建好的模型


app = creat_app()  # 创建app
manager = Manager(app=app)  # 添加壳

migrate = Migrate(app=app, db=db)  # 数据库命令工具
manager.add_command('db', MigrateCommand)  # 添加数据库的一些迁移操作，迁移等


if __name__ == '__main__':
    manager.run()  # 启动:python app.py runserver -p 端口号 -h 主机号