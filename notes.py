""" Python Notes!! """

""" You can use { #... } for inline comments
And { """    """ } for multiline comments """
# inline comments
""" 
multiline comments
"""

#!""" To print something in terminal you can use { print("...") } """

print("Hi Hope, please draw triangle")

print("     /|")
print("    / |")
print("   /  |")
print("  /   |")
print(" /    |")
print("/_____|")

""" _______________________________ """
#!""" Variables """

name = "Hope"  
""" You can change variable value, name="..." the variable value type is string """  

age = "25"
year = 1997
""" year=# the variable value type is integer (number) """

average = 81.8
""" average=# the variable value type is float (number) """

print("Hi there!")
print("My name is " + name +". I'm " + age + " years old.")
name = "Amal" 
print("I changed my name to " + name)

is_Female = True
""" Boolean input --> True or False """

""" _______________________________ """
#!""" Print Space """

""" to print new line use \n """
""" to print " use \" """
""" to print ' use \' """
""" to print tab use \t """

""" _______________________________ """
#!""" Strings """

""" to print the words using lower case use { name_variable.lower() } """
print(name.lower())   #* The output is amal

""" to print the words using upper case use { name_variable.upper() } """
print(name.upper())   #* The output is AMAL

""" to check if the words is lower case use { name_variable.islower() } """
print(name.islower())  #* The output is False

""" to check if the words is upper case use { name_variable.isupper() } """
print(name.isupper())  #* The output is False

print(name.upper().isupper())  #* The output is True

""" to print the length of the sentence use { len(name_variable) } """
print(len(name))  #* The output is 4

""" to print letter from words use { name_variable[number_letter] } """
print(name[1],name[3])  #* The output is m l

""" (to know the place of the letter in the words --> number) & (to check if this letter is in the words --> Error (we can't find the letter)) use { name_variable.index("letter")} """
print(name.index("m"))  #* The output is 1
print(name.index("al"))  #* The output is 2

""" to replace some letters use { name_variable.replace("value_to_change","new_value") } """
print(name.replace("al","ro"))  #* The output is Amro

""" _______________________________ """
#!""" Numbers """

""" to convert the number to string use { str(number) } --> Because you can't print number with string!!"""
print("I'm " + str(24) + " years old.")   #* The output is I'm 24 years old.

""" to take tha absolute value use { abs(number) } """
print(abs(-100.2))   #* The output is 100.2

""" power use { pow(a,b) } --> a^b """
print(pow(2,3))   #* The output is 8

""" to return the minimum value use { min(a,b,...)} """
print(min(2,5,3))   #* The output is 2

""" to return the maximum value use { max(a,b,...)} """
print(max(2,5,3))  #* The output is 5

""" round the number to the nearest whole number"""
print(round(3.43))    #* The output is 3
print(round(-3.76))   #* The output is -4

""" to convert the string to integer number use { int(string) } """
print(int("30"))   #* The output is 30

""" to convert the string to float number use { float(string) } """
print(float("30"))   #* The output is 30.0

""" _______________________________ """
#!""" Use Library """

from lib2to3.pgen2.token import EQUAL
from math import * 

""" floor --> round the number to the smallest number """
print(floor(3.7))  #* The output is 3

""" ceil --> round the number to the largest number """
print(ceil(3.2))  #* The output is 4

""" square root  """
print(sqrt(16))  #* The output is 4

""" _______________________________ """
#!""" Input """

""" Take input from user use { input() } --> input type is string"""
user_name = input("Enter your name: ")
user_age = input("Enter your age: ")
print("Hi " + user_name + "!! Your age is " + user_age)

""" _______________________________ """
#!""" Lists (Array) """

""" You can put string, number, and array inside the array """
my_list = ["Hope" , 24 , ["Drawing","Swimming"]]
print("Hi There! \nMy name is " + my_list[0] + ". I'm " + str(my_list[1]) + " years old. My hobbies are " + my_list[2][0] + " and " + my_list[2][1] + ".")

my_data = ["HTML" , "CSS" , "JAVASCRIPT" , "REACT" , "NODE"]

print(my_data[1:3])
""" The output is --> ['CSS', 'JAVASCRIPT'] => take the values from my_data[1] to my_data[3-1] = my_data[2]  """

print(my_data[1:])
""" The output is --> ['CSS', 'JAVASCRIPT', 'REACT', 'NODE'] => take the values from my_data[1] to last item  """

print(my_data[-1])   #* The output is --> NODE

""" You can change the value of any items in the array """
my_data[0] = "HTML3" 

""" Add the second array to first array use { array1.extend(array2) OR array1 += array2 OR array1 = array1 + array2} """
array1 = ["Hope" , "Amal"]
array2 = ["Yuki" , "Akira"]
array1.extend(array2)
print(array1)   #* The output is --> ['Hope', 'Amal', 'Yuki', 'Akira']

""" Add new item to the array (last item) use { array.append(item_value) } """
array2.append("Yuyu")
print(array2)   #* The output is --> ['Yuki', 'Akira', 'Yuyu']

""" Add new item to the array (any place) use { array.insert(place , item_value) } """
array2.insert(1,"Moshy")
print(array2)   #* The output is --> ['Yuki', 'Moshy', 'Akira', 'Yuyu']

""" Remove any item from array use { array.remove(item_value) } """
array2.remove("Yuyu")
print(array2)  #* The output is --> ['Yuki', 'Moshy', 'Akira']

""" Remove last item from array use { array.pop() } """
last_item = array2.pop()
print(last_item)   #* The output is --> Akira
print(array2)  #* The output is --> ['Yuki', 'Moshy']

""" Clear the array use {array.clear()} """
array2.clear()  
print(array2)   #* The output is --> []

""" (to know the place of the item in the array --> number) & (to check if this item is in the array --> Error (we can't find the item)) use { array.index("item_value")} """
print(array1.index("Amal"))  #* The output is 1

""" Count the item in the array use { array.count(item_value) } """
arr = ["hope","amal","hope","yuki"]
print(arr.count("hope"))   #* The output is 2

""" Sorting (a -> z) OR ( -infinite -> infinite ) use { array.sort() } """
arr1 = ["hope","amal","yuki","mashal"]
arr1.sort()
print(arr1)   #* The output is ['amal', 'hope', 'mashal', 'yuki']

arr2 = [55,3,4,65]
arr2.sort()
print(arr2)   #* The output is [3, 4, 55, 65]

""" Shallow copy the array use { array.copy() } """
old_arr = ["Hi","Hello"]
new_arr = old_arr.copy()
old_arr.append("There!")
print(new_arr)   #* The output is ['Hi', 'Hello']
print(old_arr)   #* The output is ['Hi', 'Hello', 'There!']

""" Copy the array use { new_array = old_array } """
old_arr1 = ["Hi!!","Hello!!"]
new_arr1 = old_arr1
old_arr1.append("There!!!")
print(new_arr1)   #* The output is ['Hi!!', 'Hello!!', 'There!!!']
print(old_arr1)   #* The output is ['Hi!!', 'Hello!!', 'There!!!']

""" _______________________________ """
#!""" Tuples """

""" You can't change the tuples item value """
""" To def. the tuples use { tuples_name = (..,..,...etc) } """
coordinates = (34,45)
""" You can't do this operation --> coordinates[0]=20 (ERROR!!)"""
print(coordinates)  #* The output is (34, 45)
print(coordinates[1])  #* The output is 45
array_of_tuples = [(12,23),(22,32)]
""" You can't do this operation --> array_of_tuples[0][0]=10 (ERROR!!)"""

""" _______________________________ """
#!""" Functions """

""" To create function use { def function_name(): } """
def say_hi():
  print("Hi There!!")
  print("Enjoy")

say_hi()   #* The output is Hi There!!  \n  Enjoy

""" Function with parameter  """
def print_name(name):
  print("Hello " + name)

print_name("Hope!!!")   #* The output is Hello Hope!!!

""" Cube Function """
def cube(num):
  return pow(num,3)

print(cube(3))  #* The output is 27.0

""" _______________________________ """
#!""" Conditionals """

""" If statement """
a=10
if a>0:
  print("a is Positive Number")

b=5
c=3
if a>b and b>c:
  print("a is the largest number")
elif a<b or b<c:
  print("b or c is the largest number")
elif a == b:
  print("a and b are equal")
else:
  print("Else Value")

is_male = False
if not is_male:
  print("FEMALE!!")

""" _______________________________ """
#!""" Comparisons """

""" Return the maximum number """
def max_num(num1,num2,num3):
  if num1 >= num2 and num1 >= num3:
    return num1
  elif num2 >= num1 and num2 >= num3:
    return num2
  else:
    return num3

print(max_num(6,22,42))   #* The output is 42

""" Return if the two strings are the same (Match strings) """
def match_string(string1,string2):
  if string1 == string2:
    return "The strings do match"
  else:
    return "The strings don't do match"

print(match_string("Hope","Hope"))    #* The output is The strings do match
print(match_string("Amal","Hope"))    #* The output is The strings don't match

""" 
  Comparisons:
    == equal 
    != not equal
    >= bigger than or equal 
    <= smaller than or equal 
"""

""" _______________________________ """
#!""" Dictionaries (OBJECTS) """

""" OBJECT use { 
  object_name={
    "KEY":"VAlUE"
  }
  KEY type number or string
  Value type number or string or boolean or array or object
} """
convert_month = {
  "Jan":"January",
  "Feb":"February",
  "Mar":"March",
  "Apr":"April",
  "May":"May",
  "Jun":"June",
}

print(convert_month["Mar"])   #* The output is March
print(convert_month.get("Jun"))   #* The output is June
print(convert_month.get("Hope"))   #* The output is None
""" print(object_name.get(KEY_value,ERROR_MSG)) """
print(convert_month.get("Hope","The value doesn't exist"))   #* The output is The value doesn't exist 
print(convert_month.get("Jan","The value doesn't exist"))   #* The output is January

""" _______________________________ """
#!""" WHILE LOOP """

i=1
while i <= 10:
  print(i)
  i += 1
else:
  print("The condition is not true")  #? When i=11
print("The loop has ended")
"""  #* The output is
      1
      2
      3
      4
      5
      6
      7
      8
      9
      10
      The condition is not true
      The loop has ended
"""

j=1
while j<=10:
  j += 1
  if j == 6:
    continue  #?skip this step
  print(j)
print("The loop has ended")
"""  #* The output is 
      2
      3
      4
      5
      7
      8
      9
      10
      11
      The loop has ended
"""

k =1
while k<=10:
  k += 1
  if k ==6:
    break   #?finish the loop
  print(k)
print("The loop has ended")
"""  #* The output is 
      2
      3
      4
      5
      The loop has ended
"""

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

for val in new_list:
  if val == "Akira":
    print(val," is your friend! :)")
    break
else: print("NOT FOUND")
"""  #* The output is 
      Akira  is your friend! :)
"""

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
