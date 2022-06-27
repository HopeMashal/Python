""" _______________________________ """
#!""" 2D Lists & Nested Loop """

no_list= [ 
  [1,2,3],
  [4,5,6],
  [7,8,9],
  [0]
]

""" no_list[# of row][# of column] --> We start from the number zero "0" """
print(no_list[2])   #* The output is [7, 8, 9]
print(no_list[2][2])  #* The output is 9

for row in no_list:
  for column in row:
    print(pow(column,3)+1)
""" #* The output is 
      2
      9
      28
      65
      126
      217
      344
      513
      730
      1
"""

""" _______________________________ """