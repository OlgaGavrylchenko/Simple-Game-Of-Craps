'''
   CIT 287 - Gradable Assignment 3
   Write a program that allows a user to a
   very limited extend to play a Game of Craps.
   
   Created by Olga Gavrylchenko, 04/04/2018
'''
import sys
import random
import menu
import game_func

#global variables
fileName = "test.txt"
startBank = 1000
betAmount = 100

#get all users data from a file
usersData = game_func.readUserData(fileName)

#start game
menu.welcomeTitle()

#get user name and trim a space
userName = input('Please, enter your name: ').strip()
while game_func.isEmpty(userName) is not True:
   userName = input('Please, enter your name: ').strip()

#check if user exist
if game_func.isUserExist(userName, usersData) is True:
    menu.welcomeUserBack(userName, usersData[userName])
    userScore = int(usersData[userName])
    if userScore <= 0:
        userScore = startBank
    userWinFunds = 0
    usersData[userName] = str(userScore)
else:
    userScore = startBank
    userWinFunds = 0
    

while True:
    menu.mainMenu()
    ch = input('Your choice: ')

    if ch == '1':
        print('Playing...')
        isEndGame = True
        while isEndGame is True:
           
           if game_func.getResult(userScore,userWinFunds) > 0:
              
              value = game_func.isRollDice()
              if value is True:
                 num1 = game_func.getRandomNum()
                 num2 = game_func.getRandomNum()
                 print('Your dice numbers: ')
                 print(str(num1), str(num2), sep=' ', end='\n')
                 x = game_func.getResult(num1, num2)
                 
                 if x == 2 or x == 3 or x == 12:
                    menu.loseMsg()
                    # deduct 100 from total cash
                    if game_func.getResult(userScore,userWinFunds) > startBank:
                       userWinFunds -= betAmount
                    else:
                       userScore -= betAmount
                    break
                  
                 elif x == 7 or x == 11:
                    menu.congratMsg()
                    # add 100 to userWinFunds
                    if userScore < startBank:
                       userScore += betAmount
                       userWinFunds = 0
                    else:
                       userWinFunds += betAmount
                    break
                  
                 else:
                     y = 0
                     flag = True
                     
                     while flag is True:
                        
                        if game_func.getResult(userScore,userWinFunds) > 0:
                           
                           value2 = game_func.isRollDice()
                           
                           if value2 is True:
                              num3 = game_func.getRandomNum()
                              num4 = game_func.getRandomNum()
                              print('Your second dice numbers: ')
                              print(str(num3), str(num4), sep=' ', end='\n')

                              y = game_func.getResult(num3, num4)

                              if y == x:
                                 menu.congratMsg()
                                 # add 100 to userWinFunds
                                 if userScore < startBank:
                                    userScore += betAmount
                                    userWinFunds = 0
                                 else:
                                    userWinFunds += betAmount
                                 flag = False
                                 
                              elif y == 7:
                                 menu.loseMsg()
                                 # deduct 100 from total cash
                                 if game_func.getResult(userScore,userWinFunds) > startBank:
                                    userWinFunds -= betAmount
                                 else:
                                    userScore -= betAmount
                                 flag = False
                           
                        else:
                           menu.gameOver()
                           sys.exit(0)

                     else:
                        usersData[userName] = str(game_func.getResult(userScore,userWinFunds))
                        isEndGame = False
                                                
           else:
              menu.gameOver()
              #save user data to a file
              usersData[userName] = str(game_func.getResult(userScore,userWinFunds))
              game_func.saveUserData(fileName, usersData)
              #exit a game
              sys.exit(0)         
        
        
    elif ch == '2':
        menu.displayFunds(userWinFunds, userScore)

        
    elif ch == '3':
       isReset = True
       while isReset is True:
          x = menu.isResetExit()
          if x == 'Y' or x == 'y':
             print('Your cash prize is ' + str(userWinFunds) + '$')
             userWinFunds = 0
             if game_func.isUserExist(userName, usersData) is True:
                usersData[userName] = str(userScore)
             isReset = False
          elif x == 'N' or x == 'n':
             isReset = False
                
            
                
    elif ch == '4':
        #update existing user value or add new user data           
        usersData[userName] = str(game_func.getResult(userScore,userWinFunds))
        game_func.saveUserData(fileName, usersData)
        print('Your name and score was saved successfully')
      
        
    elif ch == '5':
        isExit = True
        while isExit is True:
            x = menu.isResetExit()
            if x == 'Y' or x == 'y':
                #save all user data to a file
                game_func.saveUserData(fileName, usersData)
                sys.exit(0)
            elif x == 'N' or x == 'n':
                isExit = False


