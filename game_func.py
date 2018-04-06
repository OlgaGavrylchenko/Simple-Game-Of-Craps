'''
   CIT 287 - Gradable Assignment 3
   Write a program that allows a user to a
   very limited extend to play a Game of Craps.
   
   Created by Olga Gavrylchenko, 04/04/2018
'''
import sys
import random

def getRandomNum():
    return random.randint(1, 6)


def getResult(a, b):
    return (a+b)


def saveUserData(fileName, users):
    output = open(fileName, 'w')
    try:
        for k, v in users.items():
            output.write(k+"*"+v+"\n")
        
    finally:
        output.close()
        

def readUserData(fileName):
    D = {}
    infile = open(fileName, 'r')
    try:
        for line in infile:
            aList = line.split("*")
            if len(aList) == 2:
                D[aList[0]] = aList[1]
    finally:
        infile.close()
    return D

def isEmpty(name):
    if len(name) > 0:
        return True
    else:
        return False


def isUserExist(userKey, users):
    if userKey in users:
        return True
    else:
        return False


def isRollDice():
    str = input('Please, enter R/r to roll the dice: ')
    if str == "r" or str == "R":
        return True
    else:
        return False






    
