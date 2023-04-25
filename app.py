from flask import Flask, abort, redirect, render_template, request
from src.models import db
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)

db_user = os.getenv('DB_USER')
db_pass = os.getenv('DB_PASS')
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')
db_name = os.getenv('DB_NAME')

# TODO: DB connection
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}'

db.init_app(app)

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
    
   
