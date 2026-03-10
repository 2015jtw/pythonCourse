import random

# find a way to randomly select between rock, paper, scissors for the computer
choices = ["rock", "paper", "scissors"]
computer_choice = random.choice(choices)

# compare that against your choice and determine if you win, lose, or draw
user_choice = input("What do you choose? Type rock, paper, or scissors.\n").lower()

print(f"Computer chose: {computer_choice}")
if user_choice == computer_choice:
    print("It's a draw.")
elif user_choice == "rock":
    if computer_choice == "scissors":
        print("You win!")
    else:
        print("You lose.")
elif user_choice == "paper":
    if computer_choice == "rock":
        print("You win!")
    else:
        print("You lose.")
elif user_choice == "scissors":
    if computer_choice == "paper":
        print("You win!")
    else:
        print("You lose.")
else:
    print("Invalid choice. Please choose rock, paper, or scissors.")

