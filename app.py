from flask import Flask, redirect, render_template, request
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
