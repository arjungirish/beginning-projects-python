import random

# I do this to initiate a value for user_choice and computer_choice to make them equal so the while loop initiates when the user first starts
user_choice = "a"
computer_choice = "a"

# This makes it so if the user ties then it will restart but it will also work when the user first starts because of the above code
while user_choice == computer_choice:
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
      print("Your choice of", user_choice , "lost to the computer's choice of", computer_choice,".")
    elif computer_choice == comp_lost(user_choice):
      print("Your choice of", user_choice , "won against the computer's choice of", computer_choice,".")
    
    # Makes it so the user understands that they are restarting the game because they tied
    elif  computer_choice == comp_tied(user_choice):
      print("Your choice of", user_choice , "tied the computer's choice of", computer_choice,".")
      print("You'll play again against the computer to determine a winner.")
    

  else:
    print("Please choose either rock, paper or scissors.")

