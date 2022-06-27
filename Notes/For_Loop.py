""" _______________________________ """
#!""" FOR LOOP """

""" print all letters (String) """
print("The string length is: ",len('Hope'))
for letter in "Hope":
  print(letter)
"""  #* The output is 
      The buddies length is:  4
      H
      o
      p
      e
"""

""" print all element (Array) """
buddies = ["pikachu","grandizer","subzero"]
print("The buddies length is: ",len(buddies))
for buddy in buddies:
  print(buddy)
"""  #* The output is 
      The buddies length is:  3
      pikachu
      grandizer
      subzero
"""

""" print all number between 0 to (5-1 = 4) """
for x in range(5):
  print(x)
"""  #* The output is 
      0
      1
      2
      3
      4
"""

""" print all number between 7 to (11-1 = 10) """
for y in range(7,11):
  print(y)
"""  #* The output is 
      7
      8
      9
      10
"""

""" print the index number then print the value """
new_list = ["Hope","Amal","Akira","Yuki"]
for index in range(len(new_list)):
  print(index)
"""  #* The output is 
      0
      1
      2
      3
"""
for i in range(len(new_list)):
  print(new_list[i])
"""  #* The output is 
      Hope
      Amal
      Akira
      Yuki
"""

""" Check if the number even or odd for all numbers between 0 to (10-1=9) """
for n in range(10):
  if n % 2 ==0:
    print(n," is an even number")
  else:
    print(n," is an odd number")
"""  #* The output is 
      0  is an even number
      1  is an odd number
      2  is an even number
      3  is an odd number
      4  is an even number
      5  is an odd number
      6  is an even number
      7  is an odd number
      8  is an even number
      9  is an odd number
"""

""" Check if this value equal "Winner" when it match finish the loop """
my_arr = ["False","True","Winner","Lost"]
for value in range(len(my_arr)):
  if my_arr[value] == "Winner":
    print(value," is the Winner")
    break
  else:
    print(value," is not the Winner")
"""  #* The output is 
      0  is not the Winner
      1  is not the Winner
      2  is the Winner
"""

""" Check if "Akira" is your friend --> (found in array) """
for val in new_list:
  if val == "Akira":
    print(val," is your friend! :)")
    break
else: print("NOT FOUND")
"""  #* The output is 
      Akira  is your friend! :)
"""

""" All number between 3 to 9 are chosen number except 5 (Because we have continue when x=5) """
for x in range(3,10):
  if x == 5:
    continue
  print(x, " is the chosen number")
"""  #* The output is 
      3  is the chosen number
      4  is the chosen number
      6  is the chosen number
      7  is the chosen number
      8  is the chosen number
      9  is the chosen number
"""

""" _______________________________ """