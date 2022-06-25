""" Python Notes!! """

""" You can use { #... } for inline comments
And { """  """ } for multiline comments """
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
print("I'm " + str(24) + " years old.")

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

""" _______________________________ """
