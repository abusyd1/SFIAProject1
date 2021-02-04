#!/usr/bin/python3

from application import app, db
from application.models import Parent, Player
from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


@app.route('/home', methods=['GET', 'POST'])
@app.route('/', methods = ['GET', 'POST'])
def home():
    return render_template("layout.html")


@app.route('/players', methods=['GET', 'POST'])
def players():
    if request.method == "GET":
       return render_template("players.html", query=Player.query.all())
