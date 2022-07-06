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
def Sum_Nums(*args): #? *args -> unpacking
  result = 0
  for x in args:
    result += x
  return result

print(Sum_Nums(1,2,3,4,5,6)) #* The output is 21


#! Using Python Kwargs -> Keyword Arguments
def my_sum(a,b,*args,option=True):
  result = 0
  if option:
    for x in args:
      result += x
    return a+b+result
  else: 
    return result

print(my_sum(1,2)) #* The output is 3
print(my_sum(1,2,3,4,5)) #* The output is 15
print(my_sum(1,2,3,4,5, option=False)) #* The output is 0

def make_sentence(**kwargs):
  result=""
  for x in kwargs.values(): #? If I type kwargs => send key like (abcde) for our example
    result += x+" "
  return result 

print(make_sentence(a='Hope',b='is',c='so',d='cute',e='!!!')) #* The output is Hope is so cute !!! 

def human_details(**kwargs):
  for key,value in kwargs.items():
    print(f"{key}:{value}")

human_details(name="Hope",job="Engineer",age="25") #* The output is 
""" 
    name:Hope
    job:Engineer
    age:25 
"""

#! Using Python Unpacking


""" _______________________________ """