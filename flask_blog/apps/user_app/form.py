from flask_wtf import FlaskForm  # 继承的父类
from wtforms import StringField, PasswordField, DateField  # 字段
from wtforms.validators import DataRequired, Length, ValidationError, EqualTo  # 验证器
import re
from flask_wtf.file import FileField, FileRequired, FileAllowed  # 文件上传
from exts import cache  # 缓存

# 定义表单验证类
class UserRegisterForm(FlaskForm):
    '''用户登录表单验证'''
    # <input type="text">                           必填                   长度
    username = StringField(label='用户名', validators=[DataRequired(), Length(max=10, message='名字太长了')])
    password = PasswordField('password', validators=[DataRequired(), Length(min=6, message='密码太短了')])
    password2 = PasswordField('password', validators=[DataRequired(),
                              # 判断两个字段是否一致
                              EqualTo(fieldname='password', message='两次密码不一致')])
    phone = StringField(label='手机号', validators=[DataRequired(), Length(max=11, min=11, message='11位手机号')])
    # 文件上传                                                                              内部自动转换成小写
    icon = FileField(label='头像', validators=[FileRequired(message='未上传'), FileAllowed(['png', 'jpg', 'gif'], message='文件格式不对')])
    # 验证码
    yzm = StringField(validators=[DataRequired(message='请输入验证码')])

    def validate_yzm(self, data):
        '''对比验证码'''
        code = cache.get('code')
        input_code = data.data
        # 转换成小写验证
        if code != input_code:
            raise ValidationError('验证码错误')

    # 单字段验证：validate_字段名
    def validate_username(self, data):
        # self.username跟data是同一个对象
        if data.data[0].isdigit():  # 查看第一位是否是数字
            raise ValidationError('不能以数字开头')

    def validate_phone(self, data):
        '''正则验证手机号'''
        phone = data.data
        if not re.search(r'^1[3875]\d{9}$', phone):
            raise ValidationError('手机号格式不对')