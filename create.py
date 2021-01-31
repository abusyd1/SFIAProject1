#!/usr/bin/python3

from app import db, Team

db.drop_all()
db.create_all()

db.session.add_all([
   Team(player_name = "David De Gea", player_age = 30, player_position = "Goalkeeper"),
   Team(player_name = "Dean Henderson", player_age = '23', player_position = "Goalkeeper"),
   Team(player_name = "Lee Grant", player_age = '39', player_position = "Goalkeeper"),
   Team(player_name = "Sergio Romero", player_age = '34', player_position = "Goalkeeper"),
   Team(player_name = "Eric Bailly", player_age = '26', player_position = "Defender"),
   Team(player_name = "Alex Telles", player_age = '28', player_position = "Defender"),
   Team(player_name = "Marcos Rojo", player_age = '30', player_position = "Defender"),  
   Team(player_name = "Phil Jones", player_age = '28', player_position = "Defender"),  
   Team(player_name = "Ethan Laird", player_age = '19', player_position = "Defender"),  
   Team(player_name = "Victor Lindelof", player_age = '26', player_position = "Defender"),   
   Team(player_name = "Harry Maguire", player_age = '27', player_position = "Defender"), 
   Team(player_name = "Teden Mengi", player_age = '18', player_position = "Defender"), 
   Team(player_name = "Luke Shaw", player_age = '25', player_position = "Defender"),     
   Team(player_name = "Axel Tuanzebe", player_age = '23', player_position = "Defender"),
   Team(player_name = "Aaron Wan-Bissaka", player_age = '23', player_position = "Defender"),  
   Team(player_name = "Brandon Williams", player_age = '20', player_position = "Defender"), 
   Team(player_name = "Arnau Puigmal", player_age = '20', player_position = "Midfielder"),  
   Team(player_name = "Bruno Fernandes", player_age = '26', player_position = "Midfielder"),    
   Team(player_name = "Fred", player_age = '27', player_position = "Midfielder"),  
   Team(player_name = "Donny van de Beek", player_age = '23', player_position = "Midfielder"),  
   Team(player_name = "Jesse Lingard", player_age = '28', player_position = "Midfielder"),  
   Team(player_name = "Juan Mata", player_age = '32', player_position = "Midfielder"),  
   Team(player_name = "Nemanja Matic", player_age = '32', player_position = "Midfielder"),  
   Team(player_name = "Scott McTominay", player_age = '24', player_position = "Midfielder"),  
   Team(player_name = "Paul Pogba", player_age = '27', player_position = "Midfielder"),  
   Team(player_name = "Daniel James", player_age = '23', player_position = "Midfielder"),  
   Team(player_name = "Edinson Cavani", player_age = '33', player_position = "Forward"),  
   Team(player_name = "Mason Greenwood", player_age = '19', player_position = "Forward"), 
   Team(player_name = "Amad Diallo", player_age = '18', player_position = "Forward"),  
   Team(player_name = "Facundro Pellistri", player_age = '19', player_position = "Forward"),  
   Team(player_name = "Anthony Martial", player_age = '25', player_position = "Forward"),
   Team(player_name = "Marcus Rashford", player_age = '23', player_position = "Forward")])  


db.session.commit()
