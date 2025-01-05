import random  #importing the module random which will be used in the program for generating the random number
import sys #importing the module sys to exit the program in case of any exceptions 
from enum import Enum #imporint gthe module enum(specifically Enum class)

#game_count = 0 #declaring the gloabal variable and using it on the gamecount below

class RPS(Enum): # creating the new class and inherting from Enum
    ROCK = 1      #setting uo a CONSTANT and assigning the value
    PAPER = 2 
    SCISSORS = 3
  
def rps():      #implementing the closure concept by creating function within function
    game_count = 0
    computer_wins = 0
    player_wins = 0
    tie_games = 0

    def user_input():   # getting inputs from the user having the code within a function
    
        playerchoice = input(" Enter 1 for Rock \n Enter 2 for Paper \n Enter 3 for Scissors \n #: ")  #getting the users choice
        player = int(playerchoice)

        if player < 1 or player >3:
            return user_input()

        computerchoice = random.choice("123")
        computer = int(computerchoice)

        print("")
        print("Players Choice is: " + str(RPS(player)).replace("RPS.", "") )
        print("")
        print("Computers Choice is: " + str(RPS(computer)).replace("RPS.", "") )
        print("")

        
        def game_logic(player,computer):
            nonlocal computer_wins, player_wins, tie_games  #pulling the variables from parent function, for using the closure concept
            if player == 1 and computer == 3:
                player_wins += 1
                print("You Won")
            elif player == 2 and computer == 1:
                print("You Won")
                player_wins += 1
            elif player == 3 and computer == 2:
                print("You Won")
                player_wins += 1
            elif player == computer:
                print("Tie game")
                tie_games += 1
            else:
                print("Computer Won")
                computer_wins += 1 

        game_logic(player,computer) 
        #print(game_logic)

        nonlocal game_count        #since we are using the closure, using the nonlocal to modify the var value in the function
        #game_count =0
        game_count += 1
        
        print("Game Count : " + str(game_count) )
        print("")
        print("Player Wins : " + str(player_wins) )
        print("")
        print("Computer Wins : " + str(computer_wins) )
        print("")
        print("Tie Games : " + str(tie_games) )
        print("")

        print("Play again?")
        while True:
            playagain = input("\n press y for yes \n press n for No \n ?: " )
            if playagain.lower() not in ["y", "n"]:
                continue
            else:
                break
            
        if playagain.lower() == "y":
            return user_input()
        else:
            print("Thanks for playing")
            sys.exit("Bye!")

    return user_input   


play = rps()
if __name__ == "__mani__":
    play()

