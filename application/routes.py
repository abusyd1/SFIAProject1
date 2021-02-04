#!/usr/bin/python3

from application import app, db
from application.models import Parent, Player, Add
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

@app.route('/add', methods=['GET', 'POST'])
def add():
    form=Add()
    if request.method == 'POST':
        new_player = Player(name=form.name.data, age=form.age.data, position=form.position.data)
        if not form.validate_on_submit():
            return render_template('adderror.html', form=form, title="New Player")
        else:
            db.session.add(new_player)
            db.session.commit()
            return redirect(url_for("players"))
    return render_template('add.html', form=form, title="New Player")
