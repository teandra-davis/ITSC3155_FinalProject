from flask import Flask, redirect, render_template, request
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

#Landing Page
@app.get('/')
def index():
    return render_template('index.html')

@app.get('/create')
def posts_questions():
    # Trying to impleme nt the posts html
    title = request.form['title']
    content = request.form['content']
    subject = request.form['subject']
    #information = models.c
    # reate_post(title, content, subject)
    return render_template('post.html')
    
   