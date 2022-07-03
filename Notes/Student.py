class Student:
  no_of_students = 0
  def __init__(self,name,age=0,courses='none'):
    self.name = name
    self.age = age
    self.courses = courses
    Student.no_of_students += 1

student_1 = Student("Hope", 24, ['css','math'])
student_2 = Student("Hope", 24, ['css','math'])
print(student_1,student_2) #* The output is <__main__.Student object at 0x000001E2A5DD6D60> <__main__.Student object at 0x000001E2A5DD6CA0> ==> its place in memory
print(student_1 == student_2) #* The output is False ==> theirs place are different
print(id(student_1),id(student_2)) #* The output is 2336918826336 2336918826144
print(id(student_1) == id(student_2)) #* The output is False

student_3=Student("Hope")
print(student_3.age , student_3.name , student_3.courses )  #* The output is 0 Hope none

student_4=Student("Hope",24,["math"])
print(student_4.age , student_4.name , student_4.courses )  #* The output is 24 Hope ['math']
student_4.name="Amal"
student_4.age=30
print(student_4.age , student_4.name , student_4.courses )  #* The output is 30 Amal ['math']