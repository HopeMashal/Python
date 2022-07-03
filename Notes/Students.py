""" _______________________________ """
#! WITH SETTER & GETTER FUNCTIONS

class Student:
  no_of_students = 0
  def __init__(self,name,age=0,courses='none'):
    self.__name = name
    self.__age = age
    self.__courses = courses
    Student.no_of_students += 1
  
  def get_name(self):
    return self.__name

  def set_name(self, new_name):
    self.__name = new_name
  
  def get_age(self):
    return self.__age

  def set_age(self, new_age):
    self.__age = new_age

  def describe(self):
    print(f"My name is {self.__name}. I'm {self.__age} years old. My courses are {self.__courses}") 
    #* OR print("My name is {}. I'm {} years old.".format(self.name, self.age)) 

  def is_old(self, num):
    if self.__age >= num:
      print("Student is old")
    else:
      print("Student is not old")

student_1 = Student("Hope", 24)
print(student_1.get_name()) #* The output is Hope
student_1.set_name("Amal")
print(student_1.get_name()) #* The output is Amal
student_1.name="Yuki"
print(student_1.name) #* The output is Yuki --> I create a new value in class
print(student_1.get_name()) #* The output is Amal

student_1.set_name("Hope Mashal")
student_1.set_age(25)
student_1.describe() #* The output is My name is Hope Mashal. I'm 25 years old. My courses are none

print(student_1.__name) #* The output is {AttributeError: 'Student' object has no attribute '__name'} --> Because this value is private


""" _______________________________ """