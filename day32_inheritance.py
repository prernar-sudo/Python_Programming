# inheritance-------------code reusability----------------
class Parent:
    x=10
    def home(self):
        print('from parent class')
class child(Parent):
    pass
ob=child()
print(ob.x) #10
ob.home() # From parent class
print('--------Types of Inheritance-----------------')
# 1. Single-level
'''
    parent
      |
      |
    Child
'''

# 2. Multi-Level
'''
    Grand Parent
        |
        |
        Parent
        |
        |
        Child
'''
# 3. Multiple
'''
    Parent1         Parent2
        |               |
        |               |
        ----------------
              Child
'''
# 4. Hierarichical
'''
        ----Parent---
        |           |
        |           |
        Child1     Child2
'''

# 5. HYBRID

'''
         ---Parent---
         |          |
         |          |
        Child1     Child2
         |          |
         |          |
        ---Parent/Subchild--
'''
#---------------------------------------------------------------------------------
#single level
print('--------single level--------')
# child class ki help se parent class ki properties/or to call method we use super keyword
class parent:
    x=10
    def home(self):
        print('Home from parent')
class child(Parent):
    def home(self):
        print('home from child')
        super().home()# using -> super we used to  call home method of parent class and to deal with method overriding
obj=child()
obj.home()

#-----------------multi-level inheritance
print('------multi-level inheritance---------')
class grandparent:
    def home(self):
        print('home from gp')
class parent(grandparent):
    def home(self):
        print('home from parent')
        super().home()
class child(parent):
    def home(self):
        print('home from child')
        super().home()
obj1=child()
obj1.home()

#-------------------Multiple Inheritance------------------
print('-----multiple inheri...')
class father:
    def home(self):
        print('home from father')
        mother().home()# in this class. method is the only way to access, boz we don't hanve any relation b/w father mother class
        #mother.home(self) 
class mother:
    def home(self):
        print('home from mother')
class child(father,mother): # mro(method resolution order) logic applies here- which works on depth first algorithm
    def home(self):
        print('home from child')
        super().home()
obj2=child()
obj2.home()

#--------------------Hierarchical Inheritance----------------------
print('---hierarchical Inheritance')
class A:
    def home(self):
        print('from class A')
class B(A):
    def home(self):
        print('from class B')
        C().home()
class C(A):
    def home(self):
        print('from class c')
        super().home()
class D(B,C):
    pass
obj3=D()
obj3.home()
# statisticall-> scatter plot -> correlation, spread of data
# comperative