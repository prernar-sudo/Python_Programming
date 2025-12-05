#-------------------------
# variable
# 1.Instance variable
# 2.Class variable
# 3.Local Variable

#--------------Instance variable-------------------
# self dependent variables referred as instance variable
# object dependent variable also referres as instance variable i guess
'''declaration

    1. In-side class
        -> Inside constructor
        -> Inside instance method
    2. Outside class

Calling: 
     1. In-side class
        -> Inside constructor
        -> Inside instance method
    2. Outside class
'''
class student:
    def __init__(self,name,contact):
        self.n=name #instance variable # declaration Inside constructor
        self.c=contact # declaration inside constructor
        print(self.n,self.c) # calling inside constructor
    def add_new(self,roll_no):
        self.r=roll_no# declaration Inside instance method
    def display(self): #
        print(self.n,self.c,self.r,self.email) # calling inside instance method

obj=student('Prerna',12345)
obj.add_new(101) #AttributeError: 'student' object has no attribute 'r' 
#obj.display() #AttributeError: 'student' object has no attribute 'email' 
obj.email='prerna@gmail.com'# declaration outside class # self/obj both have same address # instance variable 
obj.display() 
print(obj.n,obj.c,obj.r,obj.email)# calling outside of the class
#------------------------------------------------------------------------
class student:
    def __init__(self,name,contact):
        self.n=name #instance variable # declaration Inside constructor
        self.c=contact # declaration inside constructor
        print(self.n,self.c) # calling inside constructor
    def add_new(self,roll_no):
        self.r=roll_no# declaration Inside instance method
    def display(self): #
        print(self.n,self.c,self.r,self.email) # calling inside instance method



