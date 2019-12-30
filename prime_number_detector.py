from random import randint
print("Hello, welcome to the prime number detector!")
number = input("Please enter a number: ")
if number.isnumeric() == True:
  number = int(number)
  if isinstance(number, int) and number > 1:
    for a_number in range(2,number):
      if number % a_number == 0:
        print("Your number", number, "is not a prime number")
        break
      else:
        print("Your number", number, "is a prime number")
        break
  else:
    print("Please type in a number greater than 1 and without decimals.")
else:
  print("Please type in a number greater than 1 and without decimals.")
