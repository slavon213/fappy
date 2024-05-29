import jwt
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, AnonymousUserMixin
from . import db
from . import login_manager



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Institution(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    users = db.relationship('User', backref='institution', lazy='dynamic')
    # products = db.relationship('Product', backref='institution', lazy='dynamic')
    # suppliers = db.relationship('Supplier', backref='institution', lazy='dynamic')
    # stock_entries = db.relationship('StockEntry', backref='institution', lazy='dynamic')
    # menus = db.relationship('Menu', backref='institution', lazy='dynamic')
    # dishes = db.relationship('Dish', backref='institution', lazy='dynamic')



class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True, nullable=False)
    username = db.Column(db.String(64), unique=True, index=True, nullable=False)
    role_id = db.Column(db.Integer)
    password_hash = db.Column(db.String(256))
    confirmed = db.Column(db.Boolean, default=False)
    name = db.Column(db.String(64))
    institution_id = db.Column(db.Integer, db.ForeignKey('institution.id'), nullable=False)


