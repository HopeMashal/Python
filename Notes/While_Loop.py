""" _______________________________ """
#!""" WHILE LOOP """

i=1
while i <= 10:
  print(i)
  i += 1
else:
  print("The condition is not true")  #? When i=11
print("The loop has ended")
"""  #* The output is
      1
      2
      3
      4
      5
      6
      7
      8
      9
      10
      The condition is not true
      The loop has ended
"""

j=1
while j<=10:
  j += 1
  if j == 6:
    continue  #?skip this step
  print(j)
print("The loop has ended")
"""  #* The output is 
      2
      3
      4
      5
      7
      8
      9
      10
      11
      The loop has ended
"""

k =1
while k<=10:
  k += 1
  if k ==6:
    break   #?finish the loop
  print(k)
print("The loop has ended")
"""  #* The output is 
      2
      3
      4
      5
      The loop has ended
"""

""" _______________________________ """
