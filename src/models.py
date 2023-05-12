from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Enum
from datetime import datetime


db = SQLAlchemy()

class Post(db.Model):
    __tablename__ = 'posts'
    
    post_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    author = db.Column(db.String, nullable=False)
    content = db.Column(db.Text, nullable=False)
    category = db.Column(Enum('1212', '1213', '2214', '3155'), nullable=False)
    comments = db.relationship('Comment', backref='post', lazy=True)
    
class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, post_id, author, content):
        self.post_id = post_id
        self.author = author
        self.content = content