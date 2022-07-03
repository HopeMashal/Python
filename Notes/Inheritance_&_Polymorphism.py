class Person:
  def __init__(self,name,age):
    self.__name=name
    self.__age=age

  def display(self):
    return f"Name is {self.__name} and age is {self.__age}"

class Man(Person):
  __gender = 'Male'
  no_of_men =0

  def __init__(self, name, age,voice):
    super().__init__(name,age)
    self.__voice = voice
    Man.no_of_men +=1

  def display(self):
    string = super().display()
    return string + f" and voice is {self.__voice} and gender is {self.__gender}"

man_1 = Man('Akira',30,'High')
print(man_1.display()) #* The output is Name is Akira and age is 30 and voice is High and gender is Male
print(man_1.no_of_men) #* The output is 1

