from flask import Flask, abort, redirect, render_template, request
from src.models import db
for dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)

#Landing Page
@app.get('/')
def index():
    return render_template('index.html')




#Running the App
if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(debug=True)