from flask import Blueprint
from apps import db
from flask import render_template, redirect,url_for
from sqlalchemy import or_

app_bp = Blueprint('app', __name__)

@app_bp.route('/', methods=['GET', 'POST'], endpoint='index')
def index():
    return '主页'