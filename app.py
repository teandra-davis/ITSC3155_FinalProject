from flask import Flask, abort, redirect, render_template, request

app = Flask(__name__)

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
    
    
   
