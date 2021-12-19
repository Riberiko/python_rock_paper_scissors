import random
from re import match
from typing import Counter, Match;

moves = ('rock', 'paper', 'scissors')

computer_move = -1  #not a valid index
player_move = -1    #not a valid index
numumber_of_rounds = 0  #minimum round value
name = ''

def intro():
    global name, numumber_of_rounds
    name = str(input('Welcome to Rocks Paper Scissors\nPlease enter your name? '))
    numumber_of_rounds = int(input('How many rounds? '))

def getRound():
    getPlayerTurn()
    getComputerTurn()

def getPlayerTurn():
    global player_move
    while(player_move != 0 and player_move != 1 and player_move != 2):
        try:
            player_move = int(input(""))
        except(ValueError):
            print("Not an integer")

def getComputerTurn():
    global computer_move
    computer_move = random.randint(0,2)

def getWinner():
    round = getRound()
    match player_move:
        case 0:
            
    
    

intro()
getWinner()