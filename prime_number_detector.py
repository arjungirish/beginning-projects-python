from random import randint
print("Hello, welcome to the prime number detector!")
number = input("Please enter a number: ")
if number.isnumeric() == True:
  number = int(number)
  if isinstance(number, int) and number > 0:
    for  in range(number):
      possible_factors = randint(0, number)
      factors = 0
      for values in possible_factors:
        maybe_factor = number/values
        if isinstance(maybe_factor, int):
          factors += 1
          if factors <= 2:
            print("Your number is prime")
          else:
            print("Your number is not prime")
  else:
    print("Please type in a positive number without decimals.")
else:
  print("Please type in a number.")
