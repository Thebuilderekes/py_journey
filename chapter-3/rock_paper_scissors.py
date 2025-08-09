# get player1 input
# get computer input which will be a random choice from 
# rock , paper, scissors array
# if player1 isscissors and computer is scissors:
#  ask for player 1 and computer input again
# if player1 isrock and computer is rock:
#   ask for player 1 and computer input again
# if player1 isrock and computer is paper:
#   print("computer wins") end The game
# if player1 ispaper and computer is rock:
#   print("palyer1 wins") and end The game
# if player1 ispaper and computer is paper:
#  ask for player 1 and computer input again
# if player1 isscissors and computer is paper:
#   print("player1 wins") and end The game
# if player1 ispaper and computer is scissors:
#   print("computer wins") and end The game

# all thisis suppose to happen while it is checking for input
import random

choices = ["rock", "paper", "scissors"]

name = "ekeopre"

print({name})

# Keep asking until valid input is given
while True:
    player_choice = input("Rock, paper or scissors? ").lower()
    if player_choice in choices:
        break  # Exit the loop if input is valid
    else:
        print("Invalid input. Please choose rock, paper, or scissors.")

# Now play the game
computer_choice = random.choice(choices)
print(f"Player chose {player_choice} and Computer chose {computer_choice}")

if player_choice == computer_choice:
    print("It's a tie!")
elif (
    (player_choice == "scissors" and computer_choice == "paper") or
    (player_choice == "paper" and computer_choice == "rock") or
    (player_choice == "rock" and computer_choice == "scissors")
):
    print("The winner is Player!")
else:
    print("The winner is Computer!")

