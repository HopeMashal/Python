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
    not False --> The value is True
    not True --> The value is False
    and --> AND GATE
    or --> OR GATE
"""

""" _______________________________ """
