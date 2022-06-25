""" Ask the user to enter the numbers and the operation """

Number_1 = input("Enter the first number: ")
Number_2 = input("Enter the second number: ")
print("Enter 1 for sum (+) \t Enter 2 for sub (-) \t Enter 3 for div (/) \t Enter 4 for mult (*) \t Enter 5 for remainder of the div (%)")
operation = input("Enter the operation: ")

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
    return "Incorrect operation, please enter (1 -> + , 2 -> - , 3 -> / , 4 -> * , 5 -> %)"

switcher = {
    1: sum_op,
    2: sub_op,
    3: div_op,
    4: mult_op,
    5: res_op,
    }

def switch(operationResult):
    return switcher.get(operationResult, default)()

op_select = ""
if int(operation) == 1 :
  op_select="+"
if int(operation) == 2 :
  op_select="-"
if int(operation) == 3 :
  op_select="/"
if int(operation) == 4 :
  op_select="*"
if int(operation) == 5 :
  op_select="%"

print("The equation is :",Number_1,op_select,Number_2)
print("The result is: ", switch(int(operation)))