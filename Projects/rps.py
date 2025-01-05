import random  #importing the module random which will be used in the program for generating the random number
import sys #importing the module sys to exit the program in case of any exceptions 
from enum import Enum #imporint gthe module enum(specifically Enum class)

game_count = 0 #declaring the gloabal variable and using it on the gamecount below

class RPS(Enum): # creating the new class and inherting from Enum
    ROCK = 1      #setting uo a CONSTANT and assigning the value
    PAPER = 2 
    SCISSORS = 3

'''playagain = True
while playagain:

    playerchoice = input(" Enter 1 for Rock \n 2 for Paper \n 3 for Scissors: ")  #getting the users choice
    player = int(playerchoice)

    if player < 1 or player >3:
        sys.exit("Enter the number from the choice 1,2 0r 3")

    computerchoice = random.choice("123")
    computer = int(computerchoice)

    print("Players Choice is: " + str(RPS(player)).replace("RPS.", "") )
    print("Computers Choice is: " + str(RPS(computer)).replace("RPS.", "") )

    if player == 1 and computer == 3:
        print("You Won")
    elif player == 2 and computer == 1:
        print("You Won")
    elif player == 3 and computer == 2:
        print("You Won")
    elif player == computer:
        print("Tie game")
    else:
        print("Computer Won") 
    
    playagain = input("\n Play again \n press y for yes \n n for No!!" )

    if playagain.lower() == "y":
        continue
    else:
        print("Thanks for playing")
        playagain = False

sys.exit("Bye!") '''       

def rec_fun():                      # having the code within a function
 
    playerchoice = input(" Enter 1 for Rock \n 2 for Paper \n 3 for Scissors: ")  #getting the users choice
    player = int(playerchoice)

    if player < 1 or player >3:
        return rec_fun()


    computerchoice = random.choice("123")
    computer = int(computerchoice)

    print("Players Choice is: " + str(RPS(player)).replace("RPS.", "") )
    print("Computers Choice is: " + str(RPS(computer)).replace("RPS.", "") )


    
    def game_logic(player,computer):
        if player == 1 and computer == 3:
            print("You Won")
        elif player == 2 and computer == 1:
            print("You Won")
        elif player == 3 and computer == 2:
            print("You Won")
        elif player == computer:
            print("Tie game")
        else:
            print("Computer Won") 

    game_logic(player,computer) 
    print(game_logic)



    global game_count
    #game_count =0
    game_count += 1
    print("Game Count : " + str(game_count) )


    print("Play again?")
    while True:
        playagain = input("\n Play again \n press y for yes \n n for No!!" )
        if playagain.lower() not in ["y", "n"]:
            continue
        else:
            break
        
    if playagain.lower() == "y":
        return rec_fun()
    else:
       print("Thanks for playing")
       sys.exit("Bye!")


rec_fun()
