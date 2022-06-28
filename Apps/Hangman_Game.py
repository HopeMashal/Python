import random

Words=["html","css","java","javascript","react","node","python","csharp","linux"]  #? The programming languages array

word_select = Words[random.randint(0,len(Words))]  #? Select random programming language

word_guess = ""  #? The guess value is empty
for i in range(len(word_select)):
  word_guess = word_guess + "*"  #?The guess value is {***}

guess_count = 0  #? The counter value
guess_limit = 6  #? The limit value of guess
out_of_guesses = False   #? If guess_count = 3 => out_of_guesses = True

print("Welcome in Hangman Game!!")
print("Guess the Programming Language:")
print("Please!! Enter One Letter")
print("You have",guess_limit,"guesses")
print("The word length is: ",word_guess)

while word_guess != word_select and not out_of_guesses:
  if guess_count < guess_limit:
    guess_input = input("Enter Guess: ")
    guess = guess_input.lower()
    for letter in range(len(word_select)):  #? check if the input value is equal to one of the letters of the selected word
      if guess == word_select[letter]:  #? change the guess value to {*x*}
        if letter == 0:
          word_guess = guess + word_guess[1:]
        elif letter > 0 and letter < len(word_guess)-1:
          word_guess = word_guess[0:letter] + guess + word_guess[letter+1 :]
        else:
          word_guess = word_guess[0:len(word_guess)-1] + guess
        print("The word is: ",word_guess)
    if guess not in word_select:
      guess_count += 1
      print("The word is: ",word_guess)
      print("You have",(guess_limit-guess_count),"guesses")
  else:
    out_of_guesses = True

if out_of_guesses:
  print("YOU LOSE OUT OF GUESSES!!!")
  print("The correct answer is:",word_select)
else:
  print("YOU WIN!!!")
  print("The programming language is:",word_select)