'''
   CIT 287 - Gradable Assignment 3
   Write a program that allows a user to a
   very limited extend to play a Game of Craps.
   
   Created by Olga Gavrylchenko, 04/04/2018
'''
# module provides menu of the game

import sys

def welcomeTitle():
    print(' Game of Craps')

def mainMenu():
    print('\n\tMain menu: ')
    print('1. Play the Game\n2. Display Available Funds')
    print('3. Reset Winning to Zero\n4. Save Name and Score\n5. Quit\n')

def welcomeUserBack(name, score):
    print('Welcome back, '+ name +' here is your last score '+score)

def congratMsg():
    print('Congratulations,you win 100$')

def loseMsg():
    print('Sorry, you lose 100$')

def gameOver():
    print('GAME OVER - YOU ARE OUT OF FUNDS!')

def displayFunds(win, startBank):
    total = win + startBank
    print('Your available funds is ' + str(total) + '$')

def isResetExit():
    str = input('Are you sure (Y/N)? ')
    return str

        

