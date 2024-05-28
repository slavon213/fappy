from flask import Flask
from  flask_bootstrap import Bootstrap4
from flask_moment import Moment
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask_login import LoginManager



bootstrap = Bootstrap4()
moment = Moment()
mail = Mail()
db = SQLAlchemy()
login_manager = LoginManager()



def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)


    return app
