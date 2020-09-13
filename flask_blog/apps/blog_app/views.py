from flask import Blueprint
from exts import db
from apps.blog_app.models import *  # 导入模型
from flask import render_template, redirect, url_for
from sqlalchemy import or_  # 多条件查询


app_bp = Blueprint('app', __name__)

@app_bp.route('/', methods=['GET', 'POST'], endpoint='index')
def index():

    return '主页'