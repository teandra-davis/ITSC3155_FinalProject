from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Enum
from datetime import datetime


db = SQLAlchemy()

class Post(db.Model):
    post_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    author = db.Column(db.String, nullable=False)
    content = db.Column(db.Text, nullable=False)
    category = db.Column(Enum('1212', '1213', '2214', '3155'), nullable=False)
    