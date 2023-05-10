from flask import Flask, abort, redirect, render_template, request
from src.models import db
from src.models import User 
from security import bcrypt
from dotenv import load_dotenv
from datetime import datetime
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

# TODO: DB connection
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}'

db.init_app(app)
bcrypt.init_app(app)

#Landing Page
@app.get('/')
def index():
    return render_template('index.html')
    
@app.post('/index')
def posts_questions():
    # Trying to implememnt the posts html
    title = request.form['title']
    browse = request.form['browse']
    description = request.form['description']
    information = functional.create_post(title, browse, description)
    return redirect('/index')
    
   

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
        user = User(username=username, password=hashed_password, email=email, first_name=first_name, last_name=last_name, date_added=datetime.date)


        # Add the new user to the database
        db.session.add(user)
        db.session.commit()

        # Redirect to the login page
        return redirect('/login')
    else:
        # Render the registration page
        return render_template('register.html')
