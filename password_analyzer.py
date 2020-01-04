"""password = input("Please enter a password to check the strength of: ")

# Counts characters in string
character_counter = 0
for a_character in password:
  character_counter += 1
  
# All wrong because this tests one character at a time and one character can't be a lowercase uppercase and number at the same time

if character_counter > 3 and character_counter <= 10:
  for character in password:

    # Strongest
    if password.isdigit() == True and password.islower() == True and password.isupper() == True:
      print("Your password is very strong.")
 
    # Could be stronger
    elif password.isdigit() == True and password.islower() == True and password.isupper() == False:
      print("Your password is strong but could be stronger if you add an uppercase.")
      
    elif password.isdigit() == False and password.islower() == True and password.isupper() == True:
      print("Your password is strong but could be stronger if you add a number.")
      
    elif password.isdigit() == True and password.islower() == False and password.isupper()== True:
      print("Your password is strong but could be stronger if you add a lowercase.")
      
    # Weak
    elif password.isdigit() == True and password.islower() == False and password.isupper == False:
      print("Your password is weak but can be made stronger if you add an uppercase and a lowercase.")
      
    elif password.isdigit() == False and password.islower() == True and password.isupper == False:
      print("Your password is weak but can be made stronger if you add an uppercase and a number.")
      
    elif password.isdigit() == False and password.islower() == False and password.isupper() == True:
      print("Your password is weak but can be made stronger if you add a number and a lowercase.")
      

else:
  print("Your password should be greater than 3 characters but less than or equal to 10 characters.")

"""

# new attempt
password = input("Please enter a password to check the strength of: ")
# checks if there are spaces in password
check_space = " " in password

# Counts characters in string
character_counter = 0
for a_character in password:
  character_counter += 1
  

# If character counter is between 3 and 10 and there are no spaces
if character_counter > 3 and character_counter <= 10 and check_space == False:
  # If there are only numbers in password
  if password.isnumeric():
    print("Add both uppercase and lowercase letters to make your password stronger.")
  # If there are only uppercase letters and maybe numbers
  elif password.isupper():
    print("Add some lowercase letters to make your password stronger.")
  # If there are only lowercase letters and maybe numbers
  elif password.islower():
    print("Add some uppercase letters to make your password stronger.")
  # If it reaches here it means that there is a mix of upper and lower case but
  # I don't know if it has numbers or not
  else:
    # I didn't really know how else to write this but basically what it does is
    # if there is a number, 1 is added to strength checker and so if strength
    # checker is > or = 1 then it can be determined that there is a number
    strength_checker = 0
    for character in password:
      if character.isnumeric():
        strength_checker += 1
      else:
        strength_checker += 0
    if strength_checker >= 1:
      print("Your password is strong")
    else:
      print("Add some numbers to your password to make it stronger.")
      
# In case the password doesn't meet the basic requirements
else:
  print("Please make sure that your password is greater than 3 characters, less than or equal to 10 characters and has no spaces.")
    
"""variable = "13431a3A"
print(variable.isdigit())
print(variable.isnumeric())
print(variable.islower())"""
    
    

