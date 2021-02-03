#!/usr/bin/python3

from flask import Flask
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@localhost/Project"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app)

class Parent(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    league = db.Column(db.String(50), nullable=False)
    players = db.relationship('Player', backref='team')

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    position = db.Column(db.String(50), nullable=False)
    parent_id = db.Column(db.Integer, db.ForeignKey('parent.id'))

if __name__=='__main__':
    app.run(debug==True, host='0.0.0.0')
