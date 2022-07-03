class Math:
  @staticmethod
  def add(x,y):
    return x+y

  @staticmethod
  def add5(num):
    return num+5

  @staticmethod
  def add10(num):
    return num+10

  @staticmethod
  def PI():
    return 3.14

x = Math.add(5,10)
y = Math.add5(x)
z = Math.add10(y)
print(x,y,z) #* The output is 15 20 30


class Pizza:
  def __init__(self, radius, ingredients):
    self.__radius = radius
    self.__ingredients=ingredients

  def __str__(self):
    return f"Pizza ingredients are {self.__ingredients}"

  def area(self):
    return Pizza.circle_area(self.__radius)

  @staticmethod
  def circle_area(r):
    return r**2 * Math.PI()

pizza_1 = Pizza(6,['Mozzarella','Tomatoes'])
print(pizza_1.area()) #* The output is 113.04
print(Pizza.circle_area(4)) #* The output is 50.24 
  
