#!/usr/bin/python3

from app import db, Team

db.create_all()

players = Team(player_name="Bruno Fernandes", player_age = 26, player_position = "Midfielder")

db.session.add(players)
db.session.commit()


