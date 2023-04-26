from flask import Flask, abort, redirect, render_template, request
from src.models import db
from dotenv import load_dotenv
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