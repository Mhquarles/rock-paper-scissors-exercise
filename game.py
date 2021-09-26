#game.py
import os
from dotenv import load_dotenv

load_dotenv()

x = os.getenv("PLAYER_NAME")
print(x)

import random

print("Rock, Paper, Scissors, Shoot!")

# PROMPT USER FOR INPUT
#x = input("Choose 'rock' or 'paper' or 'scissors'"" )
user_choice = input("Choose 'rock' or 'paper' or 'scissors': ")
print("User chose:")
print(user_choice)

#COMPUTER CHOICE AT RANDOM

options = ["rock", "paper", "siccors"]

computer_choice = random.choice(options)
print("Computer chose:")
print(computer_choice)

# adapted from code shared by Diego in Slack
if computer_choice == user_choice:
    print ("NO WINNER,TIE! TRY AGAIN!")
elif computer_choice == 'rock' and user_choice == 'scissors':
    print ("COMPUTER WINS, rock beat scissors, try again dumbie!")
elif computer_choice == 'scissors' and user_choice == 'paper':
    print ("COMPUTER WINS, scissors beat paper, try again dumbie!")
elif computer_choice == 'paper' and user_choice =='rock':
    print ("COMPUTER WINS, paper beat rock, try again dumbie!")
elif computer_choice == 'scissors' and user_choice == 'rock':
    print ("YOU WIN! Guess you’re smarter than a computer;)")
elif computer_choice == 'paper' and user_choice == 'scissors':
    print ("YOU WIN! Guess you’re smarter than a computer;)")
elif computer_choice == 'rock' and user_choice == 'paper':
    print ("YOU WIN! Guess you’re smarter than a computer;)")

# adapted from code shared by Dominic in Slack    
user_choice=input("Choose 'rock' or 'paper' or 'scissors': ")
if user_choice in ["rock","paper","scissors"]:
    print("user chose:") 
    print(user_choice)
else: 
    print("You choice is not valid.  Reminder- all letters must be lowercase!")
    print("Try again")
    exit()    
