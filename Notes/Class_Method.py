from datetime import date

class Student:

  def __init__(self,name,age=0):
    self.__name = name
    self.__age = age

  def describe(self):
    print(f"My name is {self.__name}. I'm {self.__age} years old.")

  @classmethod
  def initFromBirthYear(cls, name, birthYear):
    return cls(name, date.today().year - birthYear)

student_1 = Student("Hope",24)
student_2 = Student.initFromBirthYear("Amal",1997)
student_2.describe()  #* The output is My name is Amal. I'm 25 years old.
student_1.describe()  #* The output is My name is Hope. I'm 24 years old.


class Pizza:
  def __init__(self, ingredients):
    self.__ingredients=ingredients

  @classmethod
  def veg(cls):
    return cls(['Mushrooms','Olives','Onions'])

  @classmethod
  def margherita(cls):
    return cls(['Mozarella','Sauce'])

  def __str__(self):
    return f"Pizza ingredients are {self.__ingredients}"

pizza_1 = Pizza(['Tomatoes','Olives'])
pizza_2 = Pizza.veg()
pizza_3 = Pizza.margherita()

print(pizza_2,pizza_3) #* The output is <__main__.Pizza object at 0x0000022E86478610> <__main__.Pizza object at 0x0000022E86478520> --> Before add def __str__(self) function

print(dir(Pizza)) #* The output is ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'margherita', 'veg']

print(pizza_1,pizza_2,pizza_3) #* The output is Pizza ingredients are ['Tomatoes', 'Olives'] Pizza ingredients are ['Mushrooms', 'Olives', 'Onions'] Pizza ingredients are ['Mozarella', 'Sauce'] --> After add def __str__(self) function