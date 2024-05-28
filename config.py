import os
import secrets



basedir = os.path.abspath(os.path.dirname(__file__))

class Config():
    SECRET_KEY = os.environ.get('SECRET_KEY') or secrets.token_urlsafe(16)
    MAIL_SERVER = os.environ.get('MAIL_SERVER') or 'localhost'
    MAIL_PORT = os.environ.get('MAIL_PORT') or '2525'
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', False)
    MAIL_USER_NAME = os.environ.get('MAIL_USER_NAME')
    MAIL_USER_PASSWORD = os.environ.get('MAIL_USER_PASSWORD')
    FAPPY_MAIL_SUBJECT_PREFIX = '[Fappy]'
    FAPPY_MAIL_SENDER = 'Fappy Admin <admin.fappy@gmail.com>'
    FAPPY_ADMIN = os.environ.get('FAPPY_ADMIN') or 'admin.fappy@gmail.com>'

    SQLALCHEMY_TRACK_MODIFICATIONS = False


    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or 'sqlite:///' \
        + os.path.join(basedir, 'fappy-dev.sqlite')



class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URI') or \
    'sqlite:///:memory:'
    WTF_CSRF_ENABLED = False



config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig, 
    'default': DevelopmentConfig
}
