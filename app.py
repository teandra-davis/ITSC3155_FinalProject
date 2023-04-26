from flask import Flask, abort, redirect, render_template, request

app = Flask(__name__)

#Landing Page
@app.get('/')
def index():
    return render_template('index.html')


@app.route('/about', methods=[''])
def about():
    return render_template("about.html")
