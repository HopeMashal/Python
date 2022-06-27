""" _______________________________ """
#!""" Writing Files """

""" 
                      | r  r+  w  w+  a  a+
______________________|_______________________
read                  | +  +      +      +
write                 |    +   +  +   +  +
create                |        +  +   +  +
truncate              |        +  +
position at start     | +  +   +  +
position at end       |               +  +
                      |
"""
workers_file=open("Workers.txt","w")
for worker in workers_file.write():
  print(worker)
workers_file.close()





""" _______________________________ """