""" _______________________________ """
#!""" Classes """

#* Classes & Objects

from Employee import Employee  #? from file_name import class_name

employee1 = Employee("Hope",24,"Meta", False, 3.5, 1000)
employee2 = Employee("Yuki",60,"Whatsapp", True, 5, 1500)

print("The first employee is",employee1.name,". She is",employee1.age,"years old.")
print("The second employee is",employee2.name,". She is",employee2.age,"years old.")


""" _______________________________ """

#* Class Functions

print("Is the employee",employee1.name,"excellent?",employee1.is_excellent())
print("Is the employee",employee2.name,"excellent?",employee2.is_excellent())
""" #* The output is 
    Is the employee Hope excellent? False
    Is the employee Yuki excellent? True
"""

employee1.bonus()
employee2.bonus()
""" #* The output is 
    Dear Hope  your salary is still 1000 (NO BONUS ADDED!)
    Dear Yuki your salary increased to 2000 (500 BONUS ADDED!)
"""

""" _______________________________ """

#* Class Inheritance (الوراثة)




""" _______________________________ """