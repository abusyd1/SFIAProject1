#!/usr/bin/python3

from application import app, db
from application.models import Parent, Player
from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

@app.route('/home', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "GET":
       return render_template("index.html", query=Player.query.all())
