""" _______________________________ """
#!""" Object Oriented Programming """

#? Types of Object Oriented Programming (OOP):
#* 1- Encapsulation
#* 2- Polymorphism
#* 3- Abstraction
#* 4- Inheritance

#? What's Primitive Data Types?
#* Type that save a Single Simple Value, ex: Byte,Int,Float,Double,Char,Boolean

# Struct (structure) --> Grouping variables together makes it more easier (variables of different types) ==> It's not possible to change any value inside it

#! Object --> object is an instance of a class / class is a template for the object  ==> Grouping variables together & It's possible to change any value inside it

""" 
  Example :
    Class Feel: #Feel in chess
      Position
      Color
      Boolean --> True (dead), False (Not dead)
      Move(): return newPos (the same value for all feels in chess, so I can define it inside the class)

      feel1 = new Feel(3,"white", false)
      feel2 = new Feel(-3,"black", false)
"""

""" _______________________________ """

#! 1- Encapsulation
#? What's encapsulation?
#* من كبسولة
#* بنحط الداتا والفانكشن مع بعض داخل كلاس معين، عند ادخل مدخل بخرج مخرج من دون معرفة التفاصيل بالتحويل من مدخل الى مخرج
#* class contains --> data members + methods (behavior)
#* input --> Black Box (I can't know the details like code .. etc) --> output

#? Why we need it?
#* Setters & Getters بتعامل مع المتغيرات يلي جوا الكلاس باستخدام 
#* Setters & Getters Methods/Functions:-
#* Setters --> بتعامل مع تغير المتغيرات يلي جوا الكلاس (بقدر أغير قيمة المتغيرات)
#* Getters --> بقدر اشوف قيمة المتغيرات من دون ما اغير فيها
#* حتى ما يصير عنا مشاكل بالكود لما نغير قيمة متغير معين Setters & Getters بنستخدم
#*  (testing) بسهل علينا عملية التيستنج
#* بساعدنا في الحفاظ على النظام وتجنب الاخطاء الكثيرة وبعطينا تحكم عالي بالنظام جميعه وبسهل التيستنج وتغيير الداتا بالكلاس من دون التأثير على البرنامج جميعه (وتغيير الكود جميعه) وبالتالي بسهل علينا عملية تصليح واكتشاف الايرور وبسهل عملية كتابة الكود

""" _______________________________ """

#! 2- Polymorphism
#* متعدد الاشكال: قدرة الاوبجيكت على التصرف بعدة اشكال
#* Method overriding:-
#* الابن عنده نفس الميثود الموجود عند الاب، ولكن يلي بحصل جوا الميثود مختلف 
"""
  Example:
    Class Animal: {makeSound()-->"Sound"}
    Class Cat: {makeSound()-->"Meow"}
    Class Dog: {makeSound()-->"Hae Haw"}
"""
#* Method overloading:-
#* وجود نفس الفانكشن في نفس الكلاس وبنفس الاسم ولكن كل  فانكشين بياخد معطيات مختلفة و بأنواع مختلفة
#* فائدته بسهل العملية على نفسي، حتى ما اسمي الفانكشينز كل واحد باسم وبعدها احاول اتذكر الاسامي لان العملية  نفسها ولكن المعطيات مختلفة لهيك بنسميهم كلهم بنفس الاسم حسب العملية وبنغير بالمعطيات
"""
  Example:
    Sum (int x, int y):
      return x+y
    Sum (int x, int y, int z):
      return x+y+z
    Sum (float x, float y):
      retun x+y
"""

""" _______________________________ """

#! 3- Abstraction
#* اظهار التفاصيل المهمة والضرورية لتشغيل الشيء وباقي التفاصيل مخفية
#* يكفي معرفة كيفية استخدام الشيء والاوتبوت يلي حيطلع منه
#* Interface:- كيفية تواصل الكلاسيز مع بعض وتبادل المعلومات بين بعضها البعض
#* Using Setters & Getters in Interface to get data from classes and edit/change it
#* implementation:- تفاصيل الكود يلي احنا ما بنهتم نعرف تفاصيله او نطلع عليه
#* بسهل علي عملية تعديل كلاس معين من دون التأثير على بقية ، الكلاسيز، بنعلي عامل الامان والسيكيورتي
#* بشبه فكرة المكتبات يلي بنستدعيها! بنعرف عنها التفاصيل يلي بتهمنا بس وكيف نستخدمها وشو الاوتبوت يلي حيطلع معنا

""" _______________________________ """

#! 4- Inheritance
#* (CLASSES) الوراثة: الابن يرث بعض الصفات من الاب مثل المثال يلي كان موجود في ملف
"""
  Example:
    Class Student --> {Name, Address, numC, Hours, Grades[], getGrades()}
    Class Teacher --> {Name, Address, numC, Hours, payRate, getSalary()}
    ==> DRY : Don't Repeat Yourself

    ==> Solution:-
    Class Person --> {Name, Address, numC, Hours} --> Parent

    Class Student(Person) --> {Grades[], getGrades()} --> Child
    Class Teacher(Person) --> {payRate, getSalary()} --> Child

    --> Student/Teacher is a Person --> Child is a part of Parent
"""

""" _______________________________ """

#! Practical:
x = 1
print(type(x)) #* The output is <class 'int'>
y = "Hope"
print(type(y)) #* The output is <class 'str'>
z = True
print(type(z)) #* The output is <class 'bool'>
o = (1,2,3)
print(type(o)) #* The output is <class 'tuple'>
l = {'name':"Hope"}
print(type(l)) #* The output is <class 'dict'>

m = "Hope"
print(m.upper())  #* The output is HOPE
#* upper() is a method in class 'str'

print("hope"+1) #! Error!! 
#* You can sum (string to string) OR (int to int)

#* SEE { https://github.com/HopeMashal/Python/blob/master/Notes/Student.py } --> Without SETTER & GETTER FUNCTIONS

#* SEE { https://github.com/HopeMashal/Python/blob/master/Notes/Students.py } --> With SETTER & GETTER FUNCTIONS

#* SEE { https://github.com/HopeMashal/Python/blob/master/Notes/Class_Method.py } --> Class Method

#* SEE { https://github.com/HopeMashal/Python/blob/master/Notes/Static_Method.py } --> Static Method

#* SEE { https://github.com/HopeMashal/Python/blob/master/Notes/Inheritance_&_Polymorphism.py } --> Inheritance & Polymorphism

#* SEE { https://github.com/HopeMashal/Python/blob/master/Notes/Abstraction.py } -->  Abstraction

#* SEE { https://github.com/HopeMashal/Python/blob/master/Notes/Dunder_Methods.py } -->  Dunder Methods

""" _______________________________ """