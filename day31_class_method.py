#---------------------------------------------method--------------------------------------------------
#     method (behaviour)
#         constructor
#         instance method: object dependent method is called instance method, aisi method jinka first parameter self hota hai
#         class method: class dependent method is called class method
#                       @classmethod
#                       def update(cls, name,....):
#        
#         static method: which is not class and object dependent method 
#                       aisi method jispe na self ho, na cls, but agar hum self ki jagah kuch bhi likhenge toh woh instance method ban jayegi
#                       @staticmethod
#                       def great():
#                             print('hello')


#-------------------------------------------------------------------------------------------------------
#class method

class student:
    grad='10th'
    def __init__(self,name,roll_no):
        self.n=name
        self.r=roll_no
    @classmethod
    def update(cls,new):
        cls.grad=new
    @classmethod
    def add_new(cls,add): # this is not usually used 
        cls.code=add
obj1=student('prerna',101)
print(student.grad)
obj1.update('11th')
print(student.grad)

obj=student('prerna',101)
obj.add_new(123)
print(student.code)
print(obj.n)

#---------------------------static method-----------------------------------------
# it is a kind of method which do not have any relationship with class variable, or instance 
# a method whose first parameter is not self,neither cls
# it is used for greetings only
class stu:
    def __init__(self,roll):
        self.n=roll
    @staticmethod
    def great(name):
        print(f'welcome{name} to my webpage')

obj=stu('prerna')
x=obj.n
obj.great(x)

#---------------------------------properties-------------------------------------
# ----------Data protection------------------
# Abstraction
# Encapsulation
#-------------Code Reusability----------------
# Inheritance
# Polymorphism
        
#--------------------Abstraction--------------
#-----abstract class
#-----abstract method
#-----concrete method
#--------------------Encapsulation------------
# access specifier/modifier
#---public variable/method
#---protected variable/method
#---private variable/method
#--------------------Inheritance--------------
# types---(5 type)
# method overrriding
# method resolustion order (mro)
# super() method
#--------------------Polymorphism-------------
# types
    # compile time (python does not support)
    # run time
# overload (python does not support)