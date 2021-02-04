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
    club = db.Column(db.String(100), db.ForeignKey('parent.name'), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    position = db.Column(db.String(50), nullable=False)

class Add(FlaskForm):
    name = StringField('Name', [Length(min=5, max=50)])
    league = StringField('League', [Length(min=5, max = 100)])
    submit = SubmitField('Add Team')

class AddPlayer(FlaskForm):
    player_name = StringField("Player Name", [Length(min=5, max=50)])
    player_age = IntegerField("Player Age", validators=[DataRequired(), NumberRange(15,50)])
    player_position = StringField("Player Position", [Length(min=4, max=50)])
    submit = SubmitField('Add Player')

class Delete(FlaskForm):
    submit= SubmitField("Delete Player")

class Update(FlaskForm):
    submit= SubmitField("Update Player")
