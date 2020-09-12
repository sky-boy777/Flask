from flask import Blueprint
from flask import render_template

user_bp = Blueprint('user', __name__)

@user_bp.route('/register', methods=['GET', 'POST'], endpoint='register')
def user_register():
    return '注册'