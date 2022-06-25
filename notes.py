""" To print something in terminal you can use { print("...") } """

print("Hi Hope, please draw triangle")

print("     /|")
print("    / |")
print("   /  |")
print("  /   |")
print(" /    |")
print("/_____|")

""" _______________________________ """
""" Variables """

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
""" Print Space """

""" to print new line use \n """
""" to print " use \" """
""" to print ' use \' """
""" to print tab use \t """

""" _______________________________ """
""" Strings """

""" to print the words using lower case use { name_variable.lower() } """
print(name.lower())

""" to print the words using upper case use { name_variable.upper() } """
print(name.upper())

""" to check if the words is lower case use { name_variable.islower() } """
print(name.islower())

""" to check if the words is upper case use { name_variable.isupper() } """
print(name.isupper())

""" to print the length of the sentence use { len(name_variable) } """
print(len(name))

""" to print letter from words use { name_variable[number_letter] } """
print(name[1],name[3])

""" (to know the place of the letter in the words --> number) & (to check if this letter is in the words --> Error (we can't find the letter)) use { name_variable.index("letter")} """
print(name.index("m"))
print(name.index("al"))

""" to replace some letters use { name_variable.replace("value_to_change","new_value") } """
print(name.replace("al","ro"))

""" _______________________________ """
""" Numbers """

""" to convert the number to string use { str(number) } --> Because you can't print number with string!!"""
print("I'm " + str(24) + " years old.")

""" to take tha absolute value use { abs(number) } """
print(abs(-100.2))

""" power use { pow(a,b) } --> a^b """
print(pow(2,3))

""" to return the minimum value use { min(a,b,...)} """
print(min(2,5,3))

""" to return the maximum value use { max(a,b,...)} """
print(max(2,5,3))

""" round the number to the nearest whole number"""
print(round(3.43))
print(round(-3.76))

""" _______________________________ """
""" Use Library """

from math import * 

""" floor --> return the smallest number """
print(floor(3.7))

""" ceil --> return the largest number """
print(ceil(3.2))

""" square root  """
print(sqrt(16))

""" _______________________________ """
""" Input """

""" Take input from user use { input() } --> input type is string"""
user_name = input("Enter your name: ")
user_age = input("Enter your age: ")
print("Hi " + user_name + "!! Your age is " + user_age)

""" _______________________________ """