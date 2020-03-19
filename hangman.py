print("Hello, welcome to Hangman!")

creator_name = input("Word creator, please enter your name here: ")
guesser_name = input("Word answerer, please enter your name here: ")

word_og = input("Now, {}, please hide the computer from {} and enter your word: ".format(creator_name, guesser_name))
try:
  word_og.lower()
except:
  print("Please type in only letters.")
else:
  print("-")
  print("-")
  print("-")
  print("-")
  print("-")
  print("-")
  print("-")
  print("-")
  print("-")
  print("-")
  print("-")
  print("-")
  print("-")
  print("-")
  print("-")
  print("-")
  print("-")
  print("-")
  print("-")
  print("-")
  print("-")
  print("-")
  
  word = word_og.lower()
  word_len = len(word)
  
  print("Ok, {}, now it's your time to guess!".format(guesser_name))
  
  print("{}, please make sure that {} isn't cheating by scrolling up.".format(creator_name, guesser_name))
  
  print("Each wrong letter counts as a guess, so be sure before you guess the whole word! You have 5 guesses.")
  
  wrong_letters_so_far = []
  # List version of user guess
  user_guess_so_far = []
  for some_character in word:
    user_guess_so_far.append("-")
  
  # This is to avoid having issues when there are 2 of the same letters
  def list_duplicate_index(seq,item):
    start_at = -1
    dup_indexes = []
    while True:
      try:
        dup_index = seq.index(item,start_at+1)
      except ValueError:
        break
      else:
        dup_indexes.append(dup_index)
        start_at = dup_index
    return dup_indexes
  
  # Actual game starts
  tries = 5
  while tries > 0:
    print("Your guess so far is {}".format(user_guess_so_far))
    
    print("The letters you got wrong so far are {}".format(wrong_letters_so_far))
    
    user_guess_og = input("Please enter the letter/word you are guessing here: ")
  
    user_guess_a = user_guess_og.lower()
    user_guess = user_guess_a
    # Winning scenario
    if user_guess == word:
      print("{} won!".format(guesser_name))
      print("{}'s word was {}!".format(creator_name, word))
      break
    
    else:
      for a_character in user_guess:
        if a_character in word:
          the_duplicate_indexes = list_duplicate_index(word, a_character)
          number_of_duplicates = len(the_duplicate_indexes)
          print("{} is in {}'s word {} time(s)".format(a_character, creator_name, number_of_duplicates))
          for number in range(0, number_of_duplicates):
            user_guess_so_far[the_duplicate_indexes[number-1]] = a_character
        
        else:
          print("Your letter {} is not in {}'s word.".format(a_character, creator_name))
          wrong_letters_so_far.append(a_character)
          tries -= 1
      continue
      
  else:
    print("{} ran out of tries so {} won!".format(guesser_name, creator_name))
    print("The word was {}".format(word))
    
  
  
