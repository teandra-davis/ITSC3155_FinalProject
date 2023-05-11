from flask import Flask, redirect, render_template, request
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

@app.get('/create')
def posts_questions():
    # Trying to impleme nt the posts html
    author_name = request.form.get('author_name', '')
    title = request.form.get('title', '')
    content = request.form.get('content','')
    subject = request.form.get('subject','')
    information = post_repository.create_post(title, content, subject)
    return render_template('post.html')
    

#@app.route('/search', methods=['POST'])
#def search():
   # query = request.form['query']
   # results = perform_search(query)
  #  return render_template('search.html', results = results)
