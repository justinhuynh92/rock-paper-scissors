import random

#set initial user and computer scores
user_wins = 0
computer_wins = 0
#variable for rps
options = ["rock", "paper", "scissors"]

#input rock, paper, scissors (rps) and make lowercase
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

    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1
    #add to computer's score if it wins
    else:
        print("You lost!")
        computer_wins += 1

#print when broken out of the while loop
print("You won", user_wins, "times.")
print("Computer won", computer_wins, "times.")
print("Goodbye!")
