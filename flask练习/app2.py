#                         渲染模板引擎         重定向     请求对象  反向解析重定向
from flask import Flask, render_template, redirect, request, url_for, escape, abort
import settings  # 导入配置

app = Flask(__name__)
app.config.from_object(settings)  # 加载配置

# 视图函数
# 主页
@app.route('/', endpoint='index')  # endpoint:反向解析
def index():
    name = '张三'
    age = 18
    names = ['aa', 'bb', 'cc', 'dddd', 'eeeee']
    print(locals(), type(locals()))  # 键值对形式的字典类型

    #                                       字典形式
    return render_template('index.html', content=locals())  # 渲染模板,键值对形式：content.name
    # return render_template('index.html', name=name, age=age)  # 渲染模板


# 注册，接收前端参数，get，post方法
@app.route('/register', methods=['GET', 'POST'], endpoint='register')  # 指定请求方法, 还有反向解析
def register():
    if request.method == 'POST':  # 判断请求方法
        username = request.form.get('username')  # post方法提取参数，表单
        print(username)
        # return redirect('/')  # 重定向到主页,参数：路径，状态码（302），浏览器看到状态码为302，会改变请求路径
        return redirect(url_for('index'))  # 使用反向解析重定向到主页

    # 默认get方法
    print(request.args.get('key'))  # 问号传参接收参数，get方法
    return render_template('register.html')


if __name__ == '__main__':
    print(app.url_map)  # 打印路由规则(路径)
    app.run(port=7000)  # 指定端口