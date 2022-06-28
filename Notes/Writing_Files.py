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
# TRUNCATE -> Make the file empty
# CREATE -> Create new file if the file name doesn't exist

# SEE { https://github.com/HopeMashal/Python/blob/master/Workers.txt }
workers_file=open("Workers.txt","a")
workers_file.write("\nAkira - Automation Developer") 
workers_file.close()

# SEE { https://github.com/HopeMashal/Python/blob/master/web.html }
web_file=open("web.html","w")
web_file.write("<h1>Hi There!!</h1>") 
web_file.close()

# SEE { https://github.com/HopeMashal/Python/blob/master/Phrases.txt }
phrases_file=open("Phrases.txt","w")
list_of_phrases = ["This is a first line","\nThis is a second line","\nThis is a third line"]
phrases_file.writelines(list_of_phrases) 
phrases_file.close()

""" _______________________________ """