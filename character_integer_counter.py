print("Hello, welcome to the character counter program.")
the_string = input("Please enter the sentence which you want the characters counted for: ")
spaces = 0
numbers = 0
for character in the_string:
  if character.isspace() == True:
    spaces += 1
  elif character.isnumeric() == True:
    numbers += 1
string_length = len(the_string)
string_length = str(string_length)
spaces = str(spaces)
numbers = str(numbers)
print("You have " + string_length + " characters in your input")
print("You have " + spaces + " spaces in your input")
print("You have " + numbers + " numbers in your input")
