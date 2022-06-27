""" _______________________________ """
#!""" Errors """

""" Send error msg when user enter string """
try:
  value = int(input("Enter a number: "))
  print(value)
except:   #* In general
  print("ERROR: Invalid Input")
print("SUCCESS")

""" Send error msg (number divide by zero) or (string)"""
try:
  value = int(input("Enter a number: "))
  print(value)
  reset = value/0
except ZeroDivisionError:  #* Case (TYPE) of error
  print("ERROR: YOU CAN'T DIVIDE BY ZERO!!!")
except ValueError as error:
  print("ERROR: ",error)
print("SUCCESS")

""" _______________________________ """