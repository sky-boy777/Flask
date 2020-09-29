from flask import Blueprint
from flask import render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash  # 密码加密,验证密码
from apps.blog_app.models import User, Article_type, Article
from exts import db
from flask import jsonify
from flask import session, sessions  # 设置session
from apps.user_app.sms_send import SmsSendAPIDemo  # 发送短信验证码
from flask import g  # g对象，本次请求的对象,全局的
from werkzeug.utils import secure_filename  # 将文件名转换为安全的，符合python的类型
import settings  # 导入配置
import os

# url_prefix为路由前导，以下路由全部要加路由前导,例如：/user/register
user_bp = Blueprint('user', __name__, url_prefix='/user')

# 需要登录才能访问的路径列表
required_login_path = ['/user/user_center', '/user/publish']
# 登录后不能访问的页面
login_not_path = ['/user/login', '/user/register']

# 每个请求前执行的钩子函数，只用于蓝图，用户权限验证
@user_bp.before_app_request
def my_before_request():
    '''用户权限验证'''
    # 获取已登录的用户id
    uid = session.get('uid')
    # 如果请求的路径需要登录才能访问
    if request.path in required_login_path:
        if uid:
            user = User.query.get(uid)
            g.user = user  # 使用g对象存储用户，这样哪个页面都能用了
        else:
            # 未登录，渲染登录页面
            return render_template('user/login.html')
    elif request.path in login_not_path:
        # 已登录，不能访问登录跟注册页面
        if uid:
            return redirect(url_for('app.index'))


# /user/register
@user_bp.route('/register', methods=['GET', 'POST'], endpoint='register')
def user_register():
    '''用户注册'''
    if request.method == 'POST':
        # 获取前端数据
        username = request.form.get('username')
        password = request.form.get('password')
        phone = request.form.get('phone')
        print(User.query.filter(User.phone == phone).all())
        if len(User.query.filter(User.phone == phone).all()) > 0:
            return render_template('user/register.html', msg='号码已被注册了')
        # 添加用户
        user = User()
        user.username = username
        user.password = generate_password_hash(password)  # 密码格式：方法$盐值$哈希
        user.phone = phone
        # 提交数据库
        db.session.add(user)
        db.session.commit()
        return '注册成功'

    return render_template('user/register.html')


# 表单失去焦点，Ajax请求:$.get()，验证手机号唯一
@user_bp.route('/check_phone')
def check_phone():
    '''验证手机号唯一'''
    phone = request.args.get('phone')
    user = User.query.filter(User.phone == phone).all()  # 查看手机号是否存在
    if len(user) > 0:
        return jsonify(code=400, msg='手机号已被注册')
    else:
        return jsonify(code=200, msg='手机号可注册')

@user_bp.route('/login', methods=['GET', 'POST'], endpoint='login')
def user_login():
    '''登录'''
    if request.method == 'POST':
        key = request.args.get('key')  # key:1为密码登录，2为短信验证码登录,str类型
        if key == '1':  # 密码登录
            username = request.form.get('username')
            password = request.form.get('password')
            users = User.query.filter(User.username == username).all()
            for user in users:
                if check_password_hash(user.password, password):
                    # 设置cooke,需要实例一个响应对象
                    # res = redirect(url_for('app.index'))
                    # res.set_cookie('uid', str(user.id), max_age=1800)  # 用户主键作为cookie
                    # return res

                    # 设置session, 字典形式
                    session['uid'] = user.id
                    return redirect(url_for('app.index'))
                else:
                    return render_template('user/login.html', msg='用户名或密码错误')
        elif key == '2':  # 短信验证码登录
            phone = request.args.get('phone')  # 获取手机号
            yzm = request.args.get('yzm')  # 获取前端的验证码
            code = session.get(phone)  # 获取真实验证码
            # 判断验证码是否正确
            if code == yzm:
                user = User.query.filter(phone == phone).first()  # 查询用户
                if user:  # 如果用户存在
                    session['uid'] = user.id
                    return redirect(url_for('app.index'))
                else:
                    return render_template('user.phone_login', msg='号码未注册')
            else:
                return render_template('user.phone_login', msg='验证码错误')
    return render_template('user/login.html')


@user_bp.route('/phone_login', methods=['GET', 'POST'], endpoint='phone_login')
def phone_login():
    '''短信验证登录页面'''
    return render_template('user/phone_login.html')

# 手机登录，发送验证码
@user_bp.route('/send_msg', methods=['GET', 'POST'], endpoint='send_msg')
def send_msg():
    '''发送短信验证码'''
    phone = request.args.get('phone')
    print(phone)
    SECRET_ID = "ebf79d9288825ef70ac1e0335f71fe25 "  # 产品密钥ID，产品标识
    SECRET_KEY = "040c04fa10e06b5a9e83c5e175473e6b"  # 产品私有密钥，服务端生成签名信息使用，请严格保管，避免泄露
    BUSINESS_ID = "931f3201039240128b129b77370a1286"  # 业务ID，易盾根据产品业务特点分配
    api = SmsSendAPIDemo(SECRET_ID, SECRET_KEY, BUSINESS_ID)
    params = {
        "mobile": phone,  # 手机号码
        "templateId": "10084",  # 短信模板id
        "paramType": "json",
        "params": "json格式字符串"
        # 国际短信对应的国际编码(非国际短信接入请注释掉该行代码)
        # "internationalCode": "对应的国家编码"
    }
    ret = api.send(params)
    print(ret)
    session[phone] = '3333'  # 因为没有申请短信服务，所以用个假的练习
    return jsonify(code=200, msg='短信发送成功')
    # if ret is not None:
    #     if ret["code"] == 200:
    #         taskId = ret["data"]["taskId"]
    #         print("taskId = %s" % taskId)
    #          # 将手机号码作为键，验证码作为值
    #         return jsonify(code=200, msg='短信发送成功')
    #     else:
    #         print("ERROR: ret.code=%s,msg=%s" % (ret['code'], ret['msg']))
    #         return jsonify(code=400, msg='发送失败')

@user_bp.route('/logout', endpoint='logout')
def user_logout():
    '''退出登录'''
    # 删除cookie
    # res = redirect(url_for('app.index'))
    # res.delete_cookie('uid')
    # return res

    # 删除session
    # del session['uid']  # 删除某一个，只删除session键值对，不会删除session的内存空间和cookie
    session.clear()  # 删除session的内存空间和cookie
    return redirect(url_for('app.index'))


@user_bp.route('/user_center', methods=['GET', 'POST'], endpoint='user_center')
def user_center():
    '''用户中心'''
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        phone = request.form.get('phone')

        # 接收头像图片
        icon = request.files.get('icon')  # FileStorage对象
        icon_name = icon.filename  # 获取上传的文件名字，包括后缀名
        icon_extend = icon_name.rsplit('.')[-1]  # 从右边以点分割，提取文件后缀名
        if icon_extend in ['jpg', 'png']:
            # 验证手机号
            if User.query.filter(User.phone == phone).first() and phone != g.user.phone:
                return render_template('user/user_center.html', user=g.user, msg='错误，号码已注册')

            # 返回一个安全的文件名，会把斜杠转换为下划线
            icon_name = secure_filename(icon_name)

            # 生存文件路径,绝对路径，改文件名字使得唯一，然后保存到本地
            file_path = os.path.join(settings.UPLOAD_ICON_DIR, str(g.user.id) + icon_name)
            icon.save(file_path)

            user = g.user  # 使用g对象
            user.username = username
            user.phone = phone
            user.password = generate_password_hash(password)
            # 使用相对路径方式将图片的路径保存在数据库，相对于静态文件路径，模板渲染的路径一样
            path = 'upload/icon'
            name = str(user.id) + icon_name
            path = os.path.join(path, name)  # 名字要跟文件夹里的名字一样，不然找不到
            user.icon = path.replace('\\', '/')  # 将window系统生成的路径\替换为/, 反斜杠要转义

            # 提交更改
            db.session.commit()
            return redirect(url_for('app.index'))
        else:
            return render_template('user/user_center.html', user=g.user, msg='文件格式不正确')
    return render_template('user/user_center.html', user=g.user)


@user_bp.route('publish', methods=['POST', 'GET'])
def publish():
    '''发表文章'''
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        type_name = request.form.get('type_name')
        print(title, content, type_name)
    # 查询文章类型渲染到前端select标签
    article_type = Article_type.query.all()
    return render_template('user/publish.html', article_type=article_type)
