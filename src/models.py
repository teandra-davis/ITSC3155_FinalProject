from flask_sqlalchemy import SQLAlchemy
#import datetime
db = SQLAlchemy()

class HomeworkCategory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)

    def __repr__(self):
        return '<HomeworkCategory %r>' % self.name

class HomeworkPost(db.Model):
    post_id = db.Column(db.Integer, primary_key=True)
    author_name = db.Column(db.String, nullable=False)
    details = db.Column(db.Text, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('homework_category.id'), nullable=False)
    category = db.relationship('HomeworkCategory', backref=db.backref('posts', lazy=True))
    post_date = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __repr__(self):
        return '<HomeworkPost %r>' % self.post_id