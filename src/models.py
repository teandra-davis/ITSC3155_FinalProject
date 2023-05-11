from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Enum
from datetime import datetime


db = SQLAlchemy()

class Post(db.Model):
    post_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    user = db.Column(db.String, nullable=False)
    content = db.Column(db.Text, nullable=False)
    category = db.Column(Enum('1212', '1213', '2214', '3155'), nullable=False)

class User(db.Model):

    tablename = 'user'

    user_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable = False)
    last_name = db.Column(db.String(100), nullable = False)
    email = db.Column(db.String(200), nullable = False, unique = True)
    date_added = db.Column(db.DateTime, default = datetime.utcnow)
    username = db.Column(db.String(20), nullable = False, unique = True)
    password = db.Column(db.String(100), nullable = False)

    def init(self, first_name: str, last_name: str, email: str, date_added: datetime, username: str, password: str, user_id: int) -> None:
        super().init()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.date_added = date_added
        self.username = username
        self.password = password
        self.user_id = user_id


    def repr(self) -> str:
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