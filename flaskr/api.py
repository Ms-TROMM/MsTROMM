from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://ba6c43cb33b3be:98d7361c@us-cdbr-east-04.cleardb.com/heroku_870d88d6d1feab7?reconnect=true'

db = SQLAlchemy(app)

@app.route('/')
def root():
    return "<h1>Welcome to Ms.TROMM API</h1>"

