from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import settings
from apps.blog_app.views import app_bp

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    app.config.from_object(settings)
    db.init_app(app)

    app.register_blueprint(app_bp)

    return app
