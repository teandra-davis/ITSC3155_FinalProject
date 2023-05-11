from flask import Flask, redirect, render_template, request, abort
from src.models import db
from src.models import User 
from security import bcrypt
from dotenv import load_dotenv
from datetime import datetime
import os
from src.repositories.post_repository import post_repository_singleton
from src.repositories.user_repository import user_repository_singleton

#TO DOWNLOAD ALL DEPENDENCIES, PIP INSTALL -R REQUIREMENTS.TXT
load_dotenv()
app = Flask(__name__)

#LOCATED IN ENV.SAMPLE AND FILL OUT THE INFORMATION

# TODO: DB connection
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
db.init_app(app)
bcrypt.init_app(app)

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

@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    # results = perform_search(query)
    return render_template('search.html', results = results)

# Login Page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Check if the login credentials are valid
        username = request.form['username']
        password = request.form['password']

        existing_user = User.query.filter_by(username=username).first()

        if bcrypt.check_password_hash(existing_user.password, password):
            # Redirect to the landing page
            return redirect('/')
        else:
            # Return an error message
            return render_template('login.html', error='Invalid login credentials')
    else:
        # Render the login page
        return render_template('login.html')



# Register Page
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Get the user's information from the form
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        first_name = request.form['fname']
        last_name = request.form['lname']


        if not username or not password:
            abort(400)

        # Check if the user already exists in the database
        if User.query.filter_by(username=username).first():
            return render_template('register.html', error='Username already exists')

        hashed_password = bcrypt.generate_password_hash(password).decode()

        # Create a new User object

        now = datetime.now()
        date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
        new_user = user_repository_singleton.create_user(username, hashed_password, email, first_name, last_name, date_time)

        # Redirect to the login page
        return redirect('/login')
    else:
        # Render the registration page
        return render_template('register.html')
