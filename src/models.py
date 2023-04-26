from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

class User(db.Model):

    __tablename__ = 'user'

    user_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable = False)
    last_name = db.Column(db.String(100), nullable = False)
    email = db.Column(db.String(200), nullable = False, unique = True)
    date_added = db.Column(db.DateTime, default = datetime.utcnow)
    username = db.Column(db.String(20), nullable = False, unique = True)
    password = db.Column(db.String(100), nullable = False)

    def __init__(self, first_name: str, last_name: str, email: str, date_added: datetime, username: str, password: str, user_id: int) -> None:
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.date_added = date_added
        self.username = username
        self.password = password
        self.user_id = user_id


    def __repr__(self) -> str:
        return f'User({self.first_name}, {self.last_name}, {self.username}, {self.email})'

    def to_dict(self) -> dict[str, any]:
        return {
            "first_name" : self.first_name,
            "last_name" : self.last_name,
            "email" : self.email,
            "date_added" : self.date_added,
            "username" : self.username,
            "password" : self.password,
            "user_id" : self.user_id,
        }

class Post(db.Model):
    __tablename__ = "post"

    post_id = db.Column(db.Integer, primary_key=True)
    post_title = db.Column(db.String(100), nullable = False)
    post_author = db.Column(db.String(100), nullable = False)
    post_content = db.Column(db.String(100), nullable = False)
    post_comments = db.Column(db.String(200), nullable = True)
    post_likes = db.Column(db.Integer, primary_key = False)
    post_subject = db.Column(db.String(20), nullable = False)

    def __init__(self, post_title: str, post_id: int, post_author: str, post_content: str, post_comments: dict, post_likes: int, post_subject: str) -> None:
        super().__init__()
        self.post_id = post_id
        self.post_title = post_title
        self.post_author = post_author
        self.post_content = post_content
        self.post_comments = post_comments
        self.post_likes = post_likes
        self.post_subject = post_subject


    def __repr__(self) -> str
        return f'User({self.post_title}, {self.post_author}, {self.post_content}, {self.post_id})'

    def to_dict(self) -> dict[str, any]:
        return {
            "first_name" : self.first_name,
            "last_name" : self.last_name,
            "email" : self.email,
            "date_added" : self.date_added,
            "username" : self.username,
            "password" : self.password,
            "user_id" : self.user_id,
        }

class Comment(db.Model):
