""" _______________________________ """
#!""" Python Args & Kwargs & Unpacking Operators """

def sum_nums(x,y):
  return x+y

print(sum_nums(2,3)) #* The output is 5
#print(sum_nums(2,3,4)) #! ERROR!!! --> Just two parameters

def sum_list(my_list):
  result=0
  for x in my_list:
    result += x
  return result

list_of_nums = [1,2,3,4,5]
print(sum_list(list_of_nums)) #* The output is 15

#! Using Python Args
def Sum_Nums(*args):
  result = 0
  for x in args:
    result += x
  return result

print(Sum_Nums(1,2,3,4,5,6)) #* The output is 21

""" _______________________________ """