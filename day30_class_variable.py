# class variable -> which are not object dependent
# it is class dependent variable
'''
    decleration:
        1. Inside class
            a. Inside constructor
            b. Inside instance method
            c. Inside class method

        2. Outside of the class

    calling:
        1. Inside class
            a. Inside constructor
            b. Inside instance method
            c. Inside class method

        2. Outside of the class
            

'''
# any class variable , if we declare it will always called using class name
class student:
    school_name='dps'
    def __init__(self,name, rollno):
        self.n=name
        self.r=rollno
        student.school_city='Bhopal'
        print(student.school_city,student.school_name,name)
    def add_new(self):
        student.school_code=101
        print(student.school_city,student.school_name,student.school_code,student.contact)

student.contact=12345678
obj=student('prerna',25)
obj.add_new()
print(student.school_city,student.school_code,student.school_name,student.contact)
print(obj.school_city,obj.school_name,obj.school_code,obj.contact) # we can access class variable with object also, but it is not recommended, bcoz
#class variable is not dependent on object, every time while creating new object

#--------------------------------------------local variable---------------------------------
# it is a kind of variable which is declared within the scope

class stu:
    def __init__(self):
        x=10 # local variable
        print(x)
    def new(self):
        y=20 # local variable
        z=y+10
        print(z)
        #print(x)
obj=stu()
obj.new()

# function or method difference
# a function which is written inside class is method
# method is called with the help of object isn't

#---------------------------------------------method--------------------------------------------------
#     method (behaviour)
#         constructor
#         instance method: object dependent method is called instance method, aisi method jinka first parameter self hota hai
#         class method: class dependent method is called instance method
#                       @classmethod
#                       def update(cls, name,....):
#        
#         static method: which is not class and object dependent method 
#                       aisi method jispe na self ho, na cls, but agar hum self ki jagah kuch bhi likhenge toh woh instance method ban jayegi
#                       @staticmethod
#                       def great():
#                             print('hello')

    
