import random

# Intro lines
print("Hello, welcome to rock, paper, scissors.")
user_choice = input("Please enter your choice: ")
user_choice = user_choice.lower()

# Generating the random computer choice
possibilities = ["rock", "paper", "scissors"]
computer_choice = random.choice(possibilities)
computer_choice = computer_choice.lower()

# Functions for winning, losing, and tying
def comp_won(s):
  if s == "rock":
    return "paper"
  elif s == "paper":
    return "scissors"
  elif s == "scissors":
    return "rock"
    
def comp_lost(s):
  if s == "rock":
    return "scissors"
  elif s == "paper":
    return "rock"
  elif s == "scissors":
    return "paper"


# Will later make it so if you tie, the game continues
def comp_tied(s):
  if s == "rock":
    return "rock"
  elif s == "paper":
    return "paper"
  elif s == "scissors":
    return "scissors"
    
  
# Creating the match
if user_choice == "rock" or user_choice == "paper" or user_choice == "scissors":

  if computer_choice == comp_won(user_choice):
    print("Your choice of", user_choice , "lost to the computer's choice of", computer_choice, ".")
  elif computer_choice == comp_lost(user_choice):
    print("Your choice of", user_choice , "won against the computer's choice of", computer_choice, ".")
  elif computer_choice == comp_tied(user_choice):
    print("Your choice of", user_choice , "tied the computer's choice of", computer_choice, ".")

else:
  print("Please choose either rock, paper or scissors.")

