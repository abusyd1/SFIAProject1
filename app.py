#!/usr/bin/python3

from flask import Flask
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@localhost/Project"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app)

class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    player_name = db.Column(db.String(50), nullable=False)
    player_age = db.Column(db.Integer, nullable=False)
    player_position = db.Column(db.String(10), nullable = False)

if __name__=='__main__':
    app.run(debug==True, host='0.0.0.0')
