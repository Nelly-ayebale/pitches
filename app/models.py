from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True, index = True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pass_secure = db.Column(db.String(255))
    pitch = db.relationship('Pitch', backref='user', lazy= 'dynamic')
    comment = db.relationship('Comment', backref='user', lazy='dynamic')
    upvotes = db.relationship('Upvote', backref='user', lazy='dynamic')
    downvotes = db.relationship('Downvote', backref='user', lazy='dynamic')

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'User is {self.username}'

class Pitch(db.Model):
    __tablename__ = 'pitches'

    id = db.Column(db.Integer,primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    title = db.Column(db.String(255))
    category= db.Column(db.String(255))
    pitch = db.Column(db.String(300), index=True)
    comment = db.relationship('Comment', backref = 'pitch', lazy='dynamic')
    upvotes = db.relationship('Upvote', backref = 'pitch', lazy = 'dynamic')
    downvotes = db.relationship('Downvote', backref = 'pitch', lazy= 'dynamic')

    def save_pitches(self):
        db.session.add(self)
        db.session.commit()

       
    def __repr__(self):
        return f'Pitch is {self.title}'

class Comment(db.Model):
    __tablename__= 'comment'

    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls,id):
        comments = Comment.query.filter_by(pitch_id=id).all()
        return comments

    def __repr__(self):
        return f'Comment: {self.comment}'

class Upvote(db.Model):
    __tablename__='upvotes'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))

    def save_upvotes(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_upvotes(cls,id):
        upvotes= Upvote.query.filter_by(pitch_id=id).all()
        return upvotes

    def __repr__(self):
        return f'{self.user_id}:{self.pitch_id}'
class Downvote(db.Model):
    __tablename__='downvotes'

    id = db.Column(db.Integer, primary_key= True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))

    def save_downvotes(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_downvotes(cls,id):
        downvotes= Downvote.query.filter_by(pitch_id=id).all()
        return downvotes
    
    def __repr__(self):
        return f'{self.user_id}:{self.pitch_id}'
