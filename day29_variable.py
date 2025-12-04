#-------------------------
# variable
# 1.Instance variable
# 2.Class variable
# 3.Local Variable

#--------------Instance variable-------------------
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
    def __init__(self,name,contact):#Inside constructor
        self.n=name #instance variable
        self.c=contact
        print(self.n,self.c)
    def add_new(self,roll_no):#Inside instance method
        self.r=roll_no
    def display(self):
        print(self.n,self.c,self.r,self.email)

obj=student('Prerna',12345)
obj.add_new(101)
obj.email='prerna@gmail.com'# self/obj both have same address # instance variable 
obj.display()
print(obj.n,obj.c,obj.r,obj.email)

