""" _______________________________ """
#!""" Reading Files """

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
# TRUNCATE -> Make the file empty
# CREATE -> Create new file if the file name doesn't exist

# SEE { https://github.com/HopeMashal/Python/blob/master/Workers.txt }
workers_file=open("Workers.txt","r")
for worker in workers_file.readlines():
  print(worker)
workers_file.close()

# file_name.readable() --> check if the file open with read mode {OUTPUT:True/False}
# file_name.read() --> Read all file
# file_name.readline() --> Read the first line and put the cursor in the second line
# file_name.readlines() --> Read all lines and put them in array
# file_name.readlines()[# of line(from 0 to ..)] --> Read one line {Ex. workers_file.readlines()[1]}




""" _______________________________ """