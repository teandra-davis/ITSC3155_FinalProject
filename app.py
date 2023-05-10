from flask import Flask, abort, redirect, render_template, request
from src.models import db
from dotenv import load_dotenv
import os

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