# 1- import string module
# 2- store all characters in list (upper/lower case , digits , punctuations)
# 3- take number of characters from user
# 4- make sure the number of characters is 6 or more
# 5- shuffle all lists
# 6- calculate 30% and 20% of number of characters
# 7- crete password 60% letters and 40% digits and punctuations

import string
import random

s1 = list(string.ascii_lowercase)
s2 = list(string.ascii_uppercase)
s3 = list(string.digits)
s4 = list(string.punctuation)

characters_number = input("How many characters do you want for the password? ")

while True:
  try:
    characters_number = int(characters_number)
    if characters_number < 6 :
      print("You need at least 6 characters!!!")
      characters_number= input("Please enter the number again: ")
    else:
      break
  except:
    print("Please enter numbers only!!!!")
    characters_number = input("How many characters do you want for the password? ")

random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)

