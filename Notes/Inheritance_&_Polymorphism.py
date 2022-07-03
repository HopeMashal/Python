from datetime import date

class Person:
  def __init__(self,name,age):
    self.__name=name
    self.__age=age

  def display(self):
    return f"Name is {self.__name} and age is {self.__age}"

  @classmethod
  def initFromBirthYear(cls,name,birthday,extra):
    return cls(name, date.today().year - birthday, extra)

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
man = Man.initFromBirthYear('Amro',1998,"Hard")
print(man.display()) #* The output is Name is Amro and age is 24 and voice is Hard and gender is Male
print(man_1.no_of_men) #* The output is 2

class Woman(Person):
  __gender = 'Female'
  no_of_women =0

  def __init__(self, name, age,hair):
    super().__init__(name,age)
    self.__hair = hair
    Woman.no_of_women +=1

  def display(self):
    string = super().display()
    return string + f" and hair is {self.__hair} and gender is {self.__gender}"

woman_1 = Woman('Yuki',20,'Curly')
print(woman_1.display()) #* The output is Name is Yuki and age is 20 and hair is Curly and gender is Female
print(woman_1.no_of_women) #* The output is 1
woman = Woman.initFromBirthYear('Yuyu',1996,"Curly")
print(woman.display()) #* The output is Name is Yuyu and age is 26 and hair is Curly and gender is Female
print(woman_1.no_of_women) #* The output is 2