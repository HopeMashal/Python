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

""" to print new line use \n """
""" to print " use \" """
""" to print ' use \' """
""" to print tab use \t """

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