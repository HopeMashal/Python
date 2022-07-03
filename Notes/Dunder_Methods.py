class Man():
  def __init__(self,name,age):
    self.__name=name
    self.__age=age

  def __add__(self,other): #? Add Function
    names = self.__name + " and " + other.__name
    ages = self.__age + other.__age
    return f"Names combined are {names} and sum of ages is {ages}"

  def __lt__(self,other): #? Less Than Function
    return self.__age < other.__age

  def display(self):
    return f"Name is {self.__name} and age is {self.__age}"

man = Man("Akira",20)
man_2 = Man("Amro",30)
print(man+man_2) #* The output is Names combined are Akira and Amro and sum of ages is 50
print(man<man_2) #* The output is True --> age of man(20) < age of man_2(30)
print(man>man_2) #* The output is False --> age of man(20) > age of man_2(30)