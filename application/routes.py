#!/usr/bin/python3

from application import app, db
from application.models import Parent, Player, Add
from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


@app.route('/home', methods=['GET', 'POST'])
@app.route('/', methods = ['GET', 'POST'])
def home():
    if request.method =="GET":
       return render_template("index.html", query=Parent.query.all())


@app.route('/add', methods=['GET', 'POST'])
def add():
    form=Add()
    if request.method == 'POST':
        new_team = Parent(name=form.name.data, league=form.league.data)
        if not form.validate_on_submit():
            return render_template('adderror.html', form=form, title="New Team")
        else:
            db.session.add(new_team)
            db.session.commit()
            return redirect(url_for("home"))
    return render_template('add.html', form=form, title="New Team")

@app.route('/parent/<Name>', methods = ["GET", "POST"])
def parent(Name):
    if request.method == "GET":
        return render_template("update.html", query=Player.query.filter(Player.parent_id.contains('1')))
