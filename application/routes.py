#!/usr/bin/python3

from application import app, db
from application.models import Parent, Player, Add, AddPlayer, Delete, Update
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
            return render_template('adderror.html', form=form)
        else:
            db.session.add(new_team)
            db.session.commit()
            return redirect(url_for("home"))
    return render_template('add.html', form=form, title="New Team")

@app.route('/parent/<id>', methods = ["GET", "POST"])
def parent(id):
    if request.method == "GET":
        return render_template("update.html", parent= Parent.query.filter_by(id=id).first(), query=Player.query.filter_by(parent_id=id))

@app.route('/player/<id>', methods = ["GET", "POST"])
def player(id):
    form=AddPlayer()
    if request.method == "POST":
        new_player=Player(name=form.name.data, age=form.age.data, position=form.position.data, parent_id=id)
        if not form.validate_on_submit():
            return render_template('playererror.html', form=form)
        else:
            db.session.add(new_player)
            db.session.commit()
            return redirect(url_for("parent", id=new_player.parent_id))
    return render_template('player.html', form=form)

@app.route('/delete/<id>')
def delete(id):
    play = Player.query.filter_by(parent_id=id).first()
    i = play.parent_id
    if play is not None:
        db.session.delete(play)
        db.session.commit()
        return redirect(url_for("parent", id=i))



@app.route('/edit/<id>', methods = ["GET", "POST"])
def edit(id):
    form1=Delete()
    play = Player.query.filter_by(id=id).first()
    n = play.name
    a = play.age
    p = play.position
    i = play.parent_id
    if request.method == "POST":
        return redirect(url_for("delete", id=i))
    return render_template('delete.html', form1=form1, title=n)
