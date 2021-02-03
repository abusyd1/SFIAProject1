#!usr/bin/python3

from application import app, db
from application.models import Parent, Player

db.drop_all()
db.create_all()

united = Parent(name = "Manchester United", league = "Premier League")

db.session.add(united)
db.session.add_all([
    Player(name = "David De Gea", age = 30, position = "Goalkeeper", team=united),
   Player(name = "Dean Henderson", age = '23', position = "Goalkeeper", team=united),
   Player(name = "Lee Grant", age = '39', position = "Goalkeeper", team=united),
   Player(name = "Sergio Romero", age = '34', position = "Goalkeeper", team=united),
   Player(name = "Eric Bailly", age = '26', position = "Defender", team=united),
   Player(name = "Alex Telles", age = '28', position = "Defender", team=united),
   Player(name = "Marcos Rojo", age = '30', position = "Defender", team=united),
   Player(name = "Phil Jones", age = '28', position = "Defender", team=united),
   Player(name = "Ethan Laird", age = '19', position = "Defender", team=united),
   Player(name = "Victor Lindelof", age = '26', position = "Defender", team=united),
   Player(name = "Harry Maguire", age = '27', position = "Defender", team=united),
   Player(name = "Teden Mengi", age = '18', position = "Defender", team=united),
   Player(name = "Luke Shaw", age = '25', position = "Defender", team=united),
   Player(name = "Axel Tuanzebe", age = '23', position = "Defender", team=united),
   Player(name = "Aaron Wan-Bissaka", age = '23', position = "Defender", team=united),
   Player(name = "Brandon Williams", age = '20', position = "Defender", team=united),
   Player(name = "Arnau Puigmal", age = '20', position = "Midfielder", team=united),
   Player(name = "Bruno Fernandes", age = '26', position = "Midfielder", team=united),
   Player(name = "Fred", age = '27', position = "Midfielder", team=united),
   Player(name = "Donny van de Beek", age = '23', position = "Midfielder", team=united),
   Player(name = "Jesse Lingard", age = '28', position = "Midfielder", team=united),
   Player(name = "Juan Mata", age = '32', position = "Midfielder", team=united),
   Player(name = "Nemanja Matic", age = '32', position = "Midfielder", team=united),
   Player(name = "Scott McTominay", age = '24', position = "Midfielder", team=united),
   Player(name = "Paul Pogba", age = '27', position = "Midfielder", team=united),
   Player(name = "Daniel James", age = '23', position = "Midfielder", team=united),
   Player(name = "Edinson Cavani", age = '33', position = "Forward", team=united),
   Player(name = "Mason Greenwood", age = '19', position = "Forward", team=united),
   Player(name = "Amad Diallo", age = '18', position = "Forward", team=united),
   Player(name = "Facundro Pellistri", age = '19', position = "Forward", team=united),
   Player(name = "Anthony Martial", age = '25', position = "Forward", team=united),
   Player(name = "Marcus Rashford", age = '23', position = "Forward", team=united)])
db.session.commit()





