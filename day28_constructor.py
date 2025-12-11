# without calling external constructor
class student:
    x=10
    y=20
obj=student #internal constructor
obj1=student() # external constructor --->paranthesis responsible for calling external constructor
print(id(obj),id(obj1))#2278419176544 2278421129808
# #----------------------------------
# self ---> reference parameter/variable, that can hold address of current object
# constructor --->  special type of method, which is called when we create object
class student:
    def __init__(self):
        print('constructor called')
        print(id(self))
    def __init__(self):
        print('hello')
obj1=student()
print(id(obj1))
obj1.__init__() #constructor is called externally

#----------------------------------
class stu:
    school='shss'
    school_city='Bhopal'
    def detail():
        print('from stu class')
# called using object
obj=stu
print(obj.school)
print(obj.school_city)
obj.detail()
# called using class
print(stu.school)
print(stu.school_city)
stu.detail()
#----------------------------------
class stu:
    school='shss'
    school_city='Bhopal'
    # any method whose first parameter is self, i.e is instance method
    def detail(self):# self 
        print('from stu class')
# called using object
obj=stu()# external constructor activated
print(obj.school)
print(obj.school_city)
obj.detail()
# called using class
# print(stu.school)
# print(stu.school_city)
# stu.detail()

#--------------------------
# constructor is needed to provide object initial value
#-----------------------
class stu1:
    def __init__(self,name,age,grad):
        self.n=name
        self.a=age
        self.g=grad
    def display(self):
        print(self.n,self.a,self.g)
obj=stu1('prerna',22,'b.tech')
obj.display()
#stu1.display()
#stu1().display()
stu1('prerna',22,'b.tech').display()

#-------------------------
# variable
# 1.Instance variable
# 2.Class variable
# 3.Local Variable
