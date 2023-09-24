import random

#set initial user and computer scores
user_wins = 0
computer_wins = 0

#input rock, paper, scissors
while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    #if user chooses to quit
    if user_input == "q":
        break
    #check if user types rock, paper, or scissors in list
    #check if user types something valid within the list
    if user_input not in ["rock", "paper", "scissors"]:
        continue

print("goodbye")
