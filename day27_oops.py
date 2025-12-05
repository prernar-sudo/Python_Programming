# #oops
# # object-->object is the instance of class
# #object->physical existence of any class/design, real world entities
# # 
# # class-> is the blueprint of the object, dummy model
# # it is a design or a layout
# '''
#     class Class_Name:
#     # Class_Name: Recommended to type in camel case, bcoz class and function ,both called in same way, so to differentiate 
#         # docstring()---> which is usually in triple quote

#     variables (properties)
#         instance variable
#         class variable
#         local variable

#     method (behaviour)
#         constructor
#         instance method
#         class method
#         static method
# '''

# class Student:
#     '''This is demo class'''
#     pass
# print(dir(Student))
# print(Student.__doc__)# it will print triple quote referred as docstring, bcoz it is executable but, # comment does not execute
# #.__doc__ this is a variable

# class Student1:
#     '''This is a demo class'''
#     x=10
#     y=20
#     def show():# this is a method of our class
#         print('Hello')
# print(Student1.__dict__)#  __dict__ is a variable , it will tell how many method or variable we have and other info
# print(dir(Student1))
# # __init__() # constructor
# print(id(Student1))
# obj=Student1()# wehave  applied paranthesis maked it a method , now address changed # 
# print(id(obj))
# obj2=Student1# internal constructor called
# print(id(obj2))
# obj3=Student1
# print(id(obj3))

# #------------------------
# class Stu:
#     def __init__(self):
#         print('constructor called')
#         print(id(self))
# obj1=Stu
# print(id(obj1),id(Stu))
# obj2=Stu()#constructor called
# print(id(obj2),id(Stu))
# # self is a refernce variable that can hold current class ke current object ka address hold karta hai

# #------------------------------------------------
class student:
    x=10
    y=20
obj=student
obj1=student()
print(id(obj),id(obj1))#2278419176544 2278421129808