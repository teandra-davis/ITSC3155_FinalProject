from flask import Flask, abort, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from jinja2 import FunctionLoader
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from src.models import Post, db
from dotenv import load_dotenv
from datetime import datetime #keep track of date and time
from src.routes.post_router import post_router
from src.routes.user_router import user_router

import os

#TO DOWNLOAD ALL DEPENDENCIES, PIP INSTALL -R REQUIREMENTS.TXT
load_dotenv()
app = Flask(__name__)

#LOCATED IN ENV.SAMPLE AND FILL OUT THE INFORMATION
#postgres
db_user = os.getenv('DB_USER')

db_pass = os.getenv('DB_PASS')
#postgres
db_host = os.getenv('DB_HOST')
#5432
db_port = os.getenv('DB_PORT')
#finalproject
db_name = os.getenv('DB_NAME')

# TODO: DB connectiont
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}'

db.init_app(app)

#create form class
class NamerForm(FlaskForm):
    name = StringField("What's your name", validators=[DataRequired()])
    submit = SubmitField("Submit")

#search form
class SearchForm(FlaskForm):
    searched = StringField("Searched", validators=DataRequired)
    submit = SubmitField("Submit")

app.register_blueprint(post_router)
app.register_blueprint(user_router)

#Landing Page
@app.route('/')
def index():
    return render_template('index.html')
    
@app.post('/index')
def posts_questions():
    # Trying to implememnt the posts html
    title = request.form['title']
    browse = request.form['browse']
    description = request.form['description']
    information = FunctionLoader.create_post(title, browse, description)
    return redirect('/index')


#Create profile/add user
@app.route('/user/create_profile', methods=['GET', 'POST'])
def add_user():
    pass

#login page
@app.route('/login')
def user_login():
    pass

#create post
@app.route('/post/new_post')
def create_new_post():
    pass

#view user profile
@app.route('/user/<username>')
def userprofile(username):
    pass

#view single post
@app.route('/post/<post_id>')
def view_single_post():
    pass

#show all posts
@app.route('post/all_posts')
def view_all_posts():
    pass

#Pass searched items to navbar
@app.context_processor
def base():
    form = SearchForm()
    return dict(form=form)

#search option in navbar
@app.route('/search', methods=['POST'])
def search():
    form = SearchForm()
    posts = posts.query
    if form.validate_on_submit():
        posts.searched = form.searched.data
        return render_template('search.html', form=form, searched=posts.searched)
