import random

#set initial user and computer scores
user_wins = 0
computer_wins = 0
#variable for rps
options = ["rock", "paper", "scissors"]

#input rock, paper, scissors (rps)
while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    #if user chooses to quit
    if user_input == "q":
        break
    #check if user types rock, paper, or scissors in list
    #check if user types something valid within the list
    if user_input not in options:
        continue

    #generate random number for rps
    #rock: 0, paper: 1, scissors: 2
    random_number = random.randint(0, 2)
    #index to access string from options
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")
    #if user wins, add 1 to their score
    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1

print("goodbye")
