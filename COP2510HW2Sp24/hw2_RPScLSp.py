#Tanzeel Rahman
#U26664695

# Simulates a game of Rock Paper Scissors Lizard Spock between the user and the computer.
# The user inputs their choice, which is compared to a randomly selected choice by the computer.
# The winner is determined based on the game's rules and the result is displayed.


import random

print("Let's play Rock, Paper, Scissors, Lizard, Spock!")
user_choice = input("Enter your choice: ").lower()

choices = ["rock", "paper", "scissors", "lizard", "spock"]
computer_choice = random.choice(choices)

print(f"Computer chose {computer_choice.capitalize()}")

if user_choice == computer_choice:
    print("It's a tie!")
elif (
    (user_choice == "rock" and computer_choice in ["scissors", "lizard"]) or
    (user_choice == "paper" and computer_choice in ["rock", "spock"]) or
    (user_choice == "scissors" and computer_choice in ["paper", "lizard"]) or
    (user_choice == "lizard" and computer_choice in ["spock", "paper"]) or
    (user_choice == "spock" and computer_choice in ["scissors", "rock"])
):
    print("You win!")
else:
    print("Computer wins!")

print("Thanks for playing!")