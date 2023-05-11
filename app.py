from flask import Flask, redirect, render_template, request
from src.models import db
from dotenv import load_dotenv
import os
from src.repositories.post_repository import post_repository_singleton

#TO DOWNLOAD ALL DEPENDENCIES, PIP INSTALL -R REQUIREMENTS.TXT
load_dotenv()
app = Flask(__name__)

#LOCATED IN ENV.SAMPLE AND FILL OUT THE INFORMATION

# TODO: DB connection
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
db.init_app(app)
      
#Landing Page
@app.get('/')
def index():
    return render_template('index.html')

#Showing all posts
@app.get('/post/all')
def list_all_posts():
    all_posts = post_repository_singleton.get_all_posts()
    return render_template('show_all.html', posts=all_posts)

#Showing the create post html
@app.get('/post/create')
def show_post():
    return render_template('post.html')

#Showing the individual create post
@app.get('/post/<int:post_id>')
def show_single_post(post_id: int):
    single_post = post_repository_singleton.get_post_by_id(post_id)
    return render_template('single_post.html', single_post=single_post)

#Creating a new post
@app.post('/post')
def create_post():
    # Trying to implementation nt the posts html
    author_name = request.form.get('author', '')
    title = request.form.get('title', '')
    content = request.form.get('content','')
    category = request.form.get('category')
    created_post = post_repository_singleton.create_post(title, author_name, content, category)
    return redirect(f'/post/{created_post.post_id}')

#Searching all posts
@app.route('/post/search', methods=['POST'])
def search():
    postsSearch = []
    p = request.args.get('p', '')
    if p != '':
        postsSearch = post_repository_singleton.search_posts(p)
    return render_template('search.html', search_active=True, posts=postsSearch, search_query=p)
