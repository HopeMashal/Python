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

order = Order(["laptop","monitor"], "Hope Mashal")
print(len(order)) #* The output is 2

""" _______________________________ """