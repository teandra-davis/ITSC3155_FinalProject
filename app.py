from flask import Flask, abort, redirect, render_template, request

app = Flask(__name__)

#Landing Page
@app.get('/')
def index():
    return render_template('index.html')




#Running the App
if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(debug=True)