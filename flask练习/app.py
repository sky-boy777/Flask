from flask import Flask, Response, make_response, request, redirect, render_template, escape
import settings  # 导入自定义的配置文件
import json


app = Flask(__name__)
app.config.from_object(settings)  # 加载配置文件
# print(app.config)  # 打印配置文件

# 在下面定义视图函数
# 路径前后带不带斜杠，建议路径后面不带斜杠，这样保证唯一性
@app.route('/abc/')  # 请求/abc会重定向到/abc/（状态码：308）， 请求/abc/会直接请求（状态码：200）
def abc():
    return '路径前后带斜杠'

@app.route('/def')  # 请求/def成功（状态码：200）， 请求/def/会not found（状态码：404）
def def1():
    return '路径后面不带斜杠'


# 路由
@app.route("/")
def index():
    a = {'a': '你好'}
    return a   # 返回字典类型，浏览器变成json类型：Content-Type: application/json
# return后面的字符串会做一个Response对象的封装，最终还是返回Response对象

# 响应对象
@app.route("/index0")
def index0():
    return Response('<h1>你好</h1>')  # 返回Response对象,可以设置一些请求头什么的

# 返回元组
@app.route("/index1")
def index1():
    return 'hello', 200  # 返回元组是这样表示的

# 路径变量
@app.route('/index2/<int:key>')  # 带变量的路由，key是变量，默认是str类型,所有不能加str, 类型：int,str,float,path(类视str，但可以有斜杠),uuid
def index2(key):  # 路由里有变量，这里就要传参，用来接收变量,必须
    return str(key)  # 不能返回int类型

# 定制响应头
@app.route("/index3")
def index3():
    response = Response('<h1>你好</h1>')
    response.headers['bbb'] = 'bbb'
    # response = make_response('<h1>你好</h1>')  # 获得响应头
    # response.headers['aaa'] = 'hello'  # 添加自定义的响应头
    # 打印请求头,需要导入request
    print(dir(request))
    print(request.method)
    return response

# 渲染模板
@app.route('/index4')
def index4():
    return render_template('index.html')  # 渲染模板，HTML文件要放在templates文件夹里面

# 返回json数据
@app.route('/index5')
def index5():
    json_str = json.dumps(['1', '2', '3', '4'])  # 列表转换成json字符串
    return json_str  # 返回json

# 根据状态码返回页面
@app.errorhandler(404)
def index6(error):
    return '页面找不到', 404
    # return render_template('404.html'), 404


# 自定义过滤器
# 第一种，添加
def aa(value):
    return value + '你好'  # 要返回结果
app.add_template_filter(aa, name='add')  # 函数，过滤器名字

# 第二种，装饰器方法
@app.add_template_filter # add为模板使用的装饰器名字
def aa(value):
    return value + '你好'  # 要返回结果




if __name__ == '__main__':
    print(app.url_map)  # 打印路由规则表
    # host=0.0.0.0,表示所有主机都能访问，部署的时候用
    app.run(host='127.0.0.1', port=8000)  # debug=False时，更改后保存不会自动重新加载，默认为False