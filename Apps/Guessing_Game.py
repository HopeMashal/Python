secret_word = "Jofee"   #? The secret word value
guess = ""   #? The guess value
guess_count = 0  #? The counter value
guess_limit = 3  #? The limit value of guess
out_of_guesses = False  #? If guess_count = 3 => out_of_guesses = True

while guess != secret_word and not out_of_guesses:
  if guess_count < guess_limit:
    guess = input("Enter guess: ")
    guess_count += 1
  else:
    out_of_guesses = True

if out_of_guesses:
  print("YOU LOSE OUT OF GUESSES!!!")
else:
  print("YOU WIN!!!")