from flask import Flask, redirect, render_template, request
from src.models import db
from dotenv import load_dotenv
import os
from src.repositories.post_repository import post_repository_singleton

#TO DOWNLOAD ALL DEPENDENCIES, PIP INSTALL -R REQUIREMENTS.TXT
load_dotenv()
app = Flask(__name__)

#from src.repositories.post_repository import 

#LOCATED IN ENV.SAMPLE AND FILL OUT THE INFORMATION

# TODO: DB connection
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
db.init_app(app)
      
#Landing Page
@app.get('/')
def index():
    return render_template('index.html')

<<<<<<< HEAD
@app.post('/create')
def posts_questions():
    # Trying to impleme nt the posts html
    author_name = request.form.get('author_name', '')
=======
@app.get('/create')
def create_post():
    return render_template('post.html')

@app.post('/post')
def create_post():
    # Trying to implementation nt the posts html
    author_name = request.form.get('author', '')
>>>>>>> main
    title = request.form.get('title', '')
    content = request.form.get('content','')
    category = request.form.get('category','')
    post_repository_singleton.create_post(title, author_name, content, category)
    return redirect('show_all.html')


#@app.route('/search', methods=['POST'])
#def search():
   # query = request.form['query']
   # results = perform_search(query)
  #  return render_template('search.html', results = results)
