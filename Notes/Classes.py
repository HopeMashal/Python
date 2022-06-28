""" _______________________________ """
#!""" Classes """

#* Classes & Objects

from Employee import Employee  #? from file_name import class_name
# SEE { https://github.com/HopeMashal/Python/blob/master/Notes/Employee.py }

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

from Doctor import Doctor # SEE { https://github.com/HopeMashal/Python/blob/master/Notes/Doctor.py }
from Family_Doctor import FamilyDoctor  # SEE { https://github.com/HopeMashal/Python/blob/master/Notes/Family_Doctor.py }

doctor1 = Doctor()

doctor1.studied_years()
doctor1.works_where()
doctor1.paid_by_who()
""" #* The output is
      I studied for 7 years
      I work in a hospital
      I get paid by the government
"""

doctor2 = FamilyDoctor()

doctor2.studied_years()
doctor2.works_where()
doctor2.paid_by_who()
""" #* The output is
      I studied for 7 years
      I work with families
      I get paid by the people
"""


""" _______________________________ """