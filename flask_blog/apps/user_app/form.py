from flask_wtf import FlaskForm  # 继承的父类
from wtforms import StringField, PasswordField, DateField  # 字段
from wtforms.validators import DataRequired, Length, ValidationError  # 验证器


# 定义表单验证类
class UserRegisterForm(FlaskForm):
    '''用户登录表单验证'''
    # <input type="text">                           必填                   长度
    username = StringField('username', validators=[DataRequired(), Length(max=10, message='名字太长了')])
    password = PasswordField('password', validators=[DataRequired(), Length(min=6, message='密码太短了')])

    # 单字段验证：validate_字段名
    def validate_username(self, data):
        # self.username跟data是同一个对象
        if data.data[0].isdigit():
            raise ValidationError('不能以数字开头')