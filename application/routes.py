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

@app.route('/delete/<parent_id>/<id>')
def delete(parent_id, id):
    play = Player.query.filter_by(id=id).first()
    i = play.id
    shay = Player.query.filter_by(parent_id=parent_id).first()
    j = shay.parent_id
    if play is not None:
        db.session.delete(play)
        db.session.commit()
        return redirect(url_for("parent", id=j))



@app.route('/edit/<parent_id>/<id>', methods = ["GET", "POST"])
def edit(parent_id, id):
    form=AddPlayer()
    playeredit = Player.query.filter_by(id=id).first()
    if request.method =="POST":
        playeredit.name=form.name.data
        playeredit.age=form.age.data
        playeredit.position=form.position.data
        if not form.validate_on_submit():
            return render_template('editerror.html', form=form, playeredit=playeredit)
        else:
            db.session.commit()
            return redirect(url_for("parent", id=playeredit.parent_id))
    return render_template("edit.html", form=form, playeredit=playeredit)
