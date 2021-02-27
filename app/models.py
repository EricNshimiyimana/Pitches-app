from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from . import login_manager
from flask_login import UserMixin
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model,UserMixin)
    __tablename_ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(255),unique=True,index=True)
    email = db.Column(db.String(255),unique=True, index=True)
    pass_secure  = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pitches = db.relationship('Pitch',backref='author', lazy='dynamic')

    @property
    def password(self):
        return AttributeError('You cannot read the password attribute')

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def save_user(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'User{self.username}'