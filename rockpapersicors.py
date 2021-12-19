import random
from re import match
from typing import Counter, Match;

moves = ('rock', 'paper', 'scissors')

computer_move = -1  #not a valid index
player_move = -1    #not a valid index
numumber_of_rounds = 0  #minimum round value
computer_wins = 0
player_wins = 0
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
    global computer_wins
    global player_wins
    global moves

    round = getRound()

    for i in range (round):
        match (player_move):
            case 0:
                match(computer_move):
                    case 0:
                        print('Both '+name+' Computer played '+moves[0])
                        print('No Winner')
                    case 1:
                        print(name+' played '+moves[0]+' Computer Played '+moves[1])
                        print('Winner Computer')
                        computer_wins +=1
                    case 2:
                        print(name+' played '+moves[0]+' Computer Played '+moves[2])
                        print('Winner '+name)
                        player_wins+=1
            case 1:
                match(computer_move):
                    case 0:
                        print(name+' played '+moves[1]+' Computer Played '+moves[0])
                        print('Winner Player')
                        player_wins+=1
                    case 1:
                        print('Both '+name+' Computer played '+moves[1])
                        print('No Winner')
                    case 2:
                        print(name+' played '+moves[1]+' Computer Played '+moves[2])
                        print('Winner Computer')
                        computer_wins+=1
            case 2:
                match(computer_move):
                    case 0:
                        print(name+' played '+moves[2]+' Computer Played '+moves[0])
                        print('Winner Player')
                        computer_wins+=1
                    case 1:
                        print(name+' played '+moves[2]+' Computer Played '+moves[1])
                        print('Winner Player')
                        player_wins+=1
                    case 2:
                        print('Both '+name+' Computer played '+moves[2])
                        print('No Winner')

    if(player_move > computer_wins):
        print('Player Wins')
    elif(player_wins == computer_wins):
        print('Tie')
    else:
        print('Computer Wins')

            
    
    

intro()
getWinner()