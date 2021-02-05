#!/usr/bin/python3

from application import db
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, NumberRange, Length


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

class Add(FlaskForm):
    name = StringField('Name', [Length(min=5, max=50)])
    league = StringField('League', [Length(min=5, max = 100)])
    submit = SubmitField('Add Team')

class AddPlayer(FlaskForm):
    name = StringField('Player Name', [Length(min=4, max=100)])
    age = IntegerField('Age', validators = [DataRequired(), NumberRange(15,50)])
    position = StringField('Position', [Length(min=3, max=100)])
    submit = SubmitField('Add Player')
