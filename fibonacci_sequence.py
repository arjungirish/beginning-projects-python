print("Please welcome to the fibonacci sequence game")
fib_count = input("Please enter the number of fibonacci numbers you want to have displayed. (Should be greater than or equal to 2): ")

def find_fib(number):
  list_fib_numbers = [1,1]
  for number in range(2,number):
    new_fib_number = list_fib_numbers[-1] + list_fib_numbers[-2]
    list_fib_numbers.append(new_fib_number)
  return list_fib_numbers
    
if fib_count.isnumeric() == True:
  fib_count = int(fib_count)
  if fib_count >= 2:
    print(find_fib(fib_count))
  else:
    print("Your number should be greater than or equal to 2.")
else:
  print("Please type in a number.")
