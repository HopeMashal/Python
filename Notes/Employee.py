""" _______________________________ """
#!""" Classes Case """

class Employee:
  def __init__(self, name, age, department, is_manager, rating, salary):
    self.name = name
    self.age = age
    self.department = department 
    self.is_manager = is_manager
    self.rating = rating  # rating from 0 to 5
    self.salary = salary

  def is_excellent(self):
    if self.rating >= 4.5:
      return True
    else:
      return False

  def bonus(self):
    if self.age == 60:
      self.salary += 500
      print("Dear",self.name,"your salary increased to",self.salary,"(500 BONUS ADDED!)")
    else:
      print("Dear",self.name," your salary is still",self.salary,"(NO BONUS ADDED!)")

""" _______________________________ """