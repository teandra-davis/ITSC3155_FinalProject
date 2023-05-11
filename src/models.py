from flask_sqlalchemy import SQLAlchemy
from flask import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash 
import datetime

from sqlalchemy import DateTime

db = SQLAlchemy()

# Create Model
class Users(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20), nullable=False, unique=True)
	name = db.Column(db.String(200), nullable=False)
	email = db.Column(db.String(120), nullable=False, unique=True)
	about_author = db.Column(db.Text(), nullable=True)
	date_added = db.Column(db.DateTime, default=datetime.utcnow)
	profile_pic = db.Column(db.String(), nullable=True)

	# Password hash
	password_hash = db.Column(db.String(128))
	# User Can Have Many Posts 
	posts = db.relationship('Posts', backref='poster')


	@property
	def password(self):
		raise AttributeError('password is not a readable attribute!')

	@password.setter
	def password(self, password):
		self.password_hash = generate_password_hash(password)

	def verify_password(self, password):
		return check_password_hash(self.password_hash, password)

	# Create A String
	def __repr__(self):
		return '<Name %r>' % self.name

class Post(db.Model):
    __tablename__ = "post"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    content = db.Column(db.Text)
	#author = db.Column(db.String(255))
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    slug = db.Column(db.String(255))
    likes = db.Column(db.Integer)
	# Foreign Key To Link Users (refer to primary key of the user)
    poster_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    posts = db.relationship('Comment', backref='comments')

class Comment(db.Model):
    class Comment(db.Model):
        __tablename__ = "comments"

        comment_author = db.Column(db.Integer, db.ForeignKey('users.id'))
        content = db.Column(db.Text, nullable = False)
        likes = db.Column(db.Integer, primary_key = False)
        comment_postid = db.Column(db.Integer, db.ForeignKey('post.id'))
        comment_date = db.Column(db.DateTime, default = datetime.datetime)
