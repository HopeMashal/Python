""" _______________________________ """
#!""" Strings """

name = "Amal"

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
