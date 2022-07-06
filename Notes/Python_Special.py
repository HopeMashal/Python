""" _______________________________ """
#!""" Python Special/Dunder Methods """

print("--------")
print(1+1) #* The output is 2
print("--------")
print("Hope"+" Mashal") #* The output is Hope Mashal
print("--------")
print(3*3) #* The output is 9
print("--------")
print("Hope"*3) #* The output is HopeHopeHope
print("--------")

""" _______________________________ """

a="Hope Mashal"
b=['Hope','Amal']

print(len(a)) #* The output is 11
print(b[1]) #* The output is Amal
print(a.__len__()) #* The output is 11
print(b.__getitem__(1)) #* The output is Amal

print(dir(a)) #* The output is --> All the dunder methods I can use it with variable a
""" The dunder/Magic methods: 
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
"""

""" _______________________________ """

class Order:
  def __init__(self, cart, customer):
    self.__cart = cart
    self.__customer = customer

  def __len__(self):
    return len(self.__cart)

  def __call__(self):
    print(f"{self.__customer}")

  def __str__(self):
    return f"{self.__customer} bought {self.__cart}"

  def __repr__(self):
    return f"Order(list of items, customer name)"

  def __bool__(self):
    return len(self.__cart)>0

  def orderMsg(self):
    if self.__cart:
      print(f"{self.__customer} order is processing!!")
    else:
      print(f"Shopping cart is empty!!!")

order = Order(["laptop","monitor"], "Hope Mashal")
print(len(order)) #* The output is 2
order() #* The output is Hope Mashal
print(order) #* The output is Hope Mashal bought ['laptop', 'monitor'] --> If we don't have __str__ method, the output will be Order(list of items, customer name)
print(repr(order)) #* The output is Order(list of items, customer name)
print(bool(order)) #* The output is True (len(order.cart)2>0)
order.orderMsg() #* The output is Hope Mashal order is processing!!

order_1=Order([],"Yuki")
order_1.orderMsg() #* The output is Shopping cart is empty!!!

""" _______________________________ """