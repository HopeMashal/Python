import random

Words=["html","css","java","javascript","react","node","python","csharp","linux"]

word_select = Words[random.randint(0,len(Words))]

word_guess = ""
for i in range(len(word_select)):
  word_guess = word_guess + "*"

guess_count = 0
guess_limit = 6
out_of_guesses = False

print("Welcome in Hangman Game!!")
print("Guess the Programming Language:")
print("Please!! Enter One Letter")
print("You have",guess_limit,"guesses")
print("The word length is: ",word_guess)

while word_guess != word_select and not out_of_guesses:
  if guess_count < guess_limit:
    guess_input = input("Enter Guess: ")
    guess = guess_input.lower()
    for letter in range(len(word_select)):
      if guess == word_select[letter]:
        if letter == 0:
          word_guess = guess + word_guess[1:]
        elif letter > 0 and letter < len(word_guess)-1:
          word_guess = word_guess[0:letter] + guess + word_guess[letter+1 :]
        else:
          word_guess = word_guess[0:len(word_guess)-1] + guess
        print("The word is: ",word_guess)
    if guess not in word_select:
      guess_count += 1
      print("You have",(guess_limit-guess_count),"guesses")
  else:
    out_of_guesses = True

if out_of_guesses:
  print("YOU LOSE OUT OF GUESSES!!!")
  print("The correct answer is:",word_select)
else:
  print("YOU WIN!!!")
  print("The programming language is:",word_select)