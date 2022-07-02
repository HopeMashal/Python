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


""" _______________________________ """