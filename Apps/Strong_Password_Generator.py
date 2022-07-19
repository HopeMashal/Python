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

part_30 = round(characters_number * (30/100))
part_20 = round(characters_number * (20/100))

password = []

for i in range(part_30):
  password.append(s1[i])
  password.append(s2[i])

for i in range(part_20):
  password.append(s3[i])
  password.append(s4[i])

if characters_number%2 ==1:
  y = random.randint(1,4)
  print(y)
  if y ==1: z=s1
  elif y ==2 : z=s2
  elif y ==3 : z=s3
  elif y ==4 : z=s4
  x = random.randint(0,len(z))
  password.append(z[x])

random.shuffle(password)

password = "".join(password[0:])

print("Your password is:  ",password)