""" In this app, I used switch and if/else statement """
""" Ask the user to enter the numbers and the operator """

Number_1 = input("Enter the first number: ")
Number_2 = input("Enter the second number: ")
print("\n ____________________________________")
print("|  Please enter the operator number  |")
print("|        Enter 1 for sum (+)         |")
print("|        Enter 2 for sub (-)         |")
print("|        Enter 3 for div (/)         |")
print("|        Enter 4 for mul (*)         |")
print("|        Enter 5 for rod (%)         |")
print("|____________________________________|\n")
operator = input("Enter the operator number: ")

""" Def. the functions """

def sum_op():
    return float(Number_1)+float(Number_2)
def sub_op():
    return float(Number_1)-float(Number_2)
def div_op():
    return float(Number_1)/float(Number_2)
def mult_op():
    return float(Number_1)*float(Number_2)
def res_op():
    return float(Number_1)%float(Number_2)
def default():
    return "Incorrect operator, please enter (1 -> + , 2 -> - , 3 -> / , 4 -> * , 5 -> %)"

""" Def. the switch value """

switcher = {
    1: sum_op,
    2: sub_op,
    3: div_op,
    4: mult_op,
    5: res_op,
    }

""" Return the result of the switch """ 

def switch(operatorResult):
    return switcher.get(operatorResult, default)()

""" Print the equation and the result """ 

op_select = ""
op_value = int(operator)
if op_value == 1 :
  op_select="+"
if op_value == 2 :
  op_select="-"
if op_value == 3 :
  op_select="/"
if op_value == 4 :
  op_select="*"
if op_value == 5 :
  op_select="%"

if op_value <= 5 and op_value >= 1 :
  print("The equation is:",Number_1,op_select,Number_2)
  print("The result is:",switch(op_value))
else:
  print(switch(op_value))