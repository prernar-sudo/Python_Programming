#abstraction--------------data hiding
# abstract class ---> 
# abstract method
# concrete method ---> all themethods inside the class is concrete method
# ABC->abstract base class

from abc import ABC, abstractmethod
class A(ABC):#abstract class
    def dashboard(self):
        print('welcome to dashboard')
    @abstractmethod # for data protection
    #with the help of abstract class, we want to protect the properties of parent class, so that child class do not able to accesss 
    def login(self):
        pass
class B(A):
    #pass
    # if we have not defined abstract method in child we will not able to make the object and we get the error
    # comment below method, uncomment pass, -> u will see u r not able to make the object 
    def login(self):
        print('login successfully')
obj=B()#TypeError: Can't instantiate abstract class B without an implementation for abstract method 'login'
obj.login()

#--------------------------Encapsulation------------------------------------------
#data wrapping ---> to wrap variables and methods in single unit is data encapsulation
# to achieve encapsulation -> we use access specifier/modifier
# access specifier/modified
# 1. public variable/method (x,add())
# 2. protected (_x,_add())
# 3. private   (__x,__add())
# according to oops concept access specifier does exist, but in python it is not present 