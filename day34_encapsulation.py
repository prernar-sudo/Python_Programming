#--------------------------Encapsulation------------------------------------------
#data wrapping ---> to wrap variables and methods in single unit is data encapsulation
# to achieve encapsulation -> we use access specifier/modifier
# access specifier/modified
# 1. public variable/method (x,add())
# 2. protected (_x,_add())
# 3. private   (__x,__add())
# according to oops concept access specifier does exist, but in python it is not present 

#-------------------------public variable/ method--------------------------------
# a method that can called inside child class/ parent class/ outside the class ,means can be called at everwhere is known as public variable/method 
class A:
    x=10
    def show(self):
        print('from class A')
        print(A.x)
class B(A):
    pass
obj=B()
print(obj.x)
obj.show()
print(A.x)
print(A.show(1))

# ------protected variable/ method------------(python not supported)-----------------------
# can only accessed inside child class not outside
print('---------------protected-----------------')
class A:
    _x=10
    def _show(self):
        print('from class A')
        print(A._x)
class B(A):
    pass
obj=B()
print(obj._x)
obj._show()
print(A._x) # we are able to access it outside , hence we can say python do not support protected
print(A._show(1)) # we are able to access it outside but acc to defination, we should not , hence we can say python do not support protected

# ------private variable/ method------------(python not supported)-----------------------
# can only accessed inside it's own class
print('---------------private-----------------')
class A:
    __x=10
    def __show(self):
        print('from class A')
        print(A.__x)
class B(A):
    pass
obj=B()
#print(obj.__x) # AttributeError: 'B' object has no attribute '__x' # through child class
#obj.__show() # AttributeError: 'B' object has no attribute 'show'    # through child class
#print(A.__x) # AttributeError: type object 'A' has no attribute '__x' # outside class
#print(A.__show(1)) # # outside class

# through name mangling we can access private variable
print(dir(A))  # '_A__show', '_A__x
print(obj._A__x) # i am able to access private variable, outside the class 

# name mangling syntax: _classname__variable/method


# read about-> hard reset / deep reset