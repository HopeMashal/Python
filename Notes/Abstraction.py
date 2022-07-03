from abc import ABC, abstractmethod

class Shape(ABC):
  @abstractmethod
  def area(self):
    pass

  @abstractmethod
  def perimeter(self):
    pass

class Square(Shape):
  def __init__(self, side):
    self.__side=side

  def area(self):
    return self.__side *self.__side

  def perimeter(self):
    return self.__side*4

class Rect(Shape):
  def __init__(self, length, width):
    self.__length=length
    self.__width=width

  def area(self):
    return self.__length *self.__width

  def perimeter(self):
    return 2*(self.__width+self.__length)

square = Square(10)
print(f"Square area is {square.area()} and perimeter is {square.perimeter()}") #* The output is Square area is 100 and perimeter is 40
rect = Rect(5,3)
print(f"Rectangle area is {rect.area()} and perimeter is {rect.perimeter()}") #* The output is Rectangle area is 15 and perimeter is 16