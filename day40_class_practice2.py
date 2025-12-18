# 1 Create a class MaxFinder that identifies the largest number in a list.
# Input:[45,2,49,3]
# Output:49

class MaxFinder:
    def __init__(self,input_list):
        self.input_list=input_list
    def largest(self):
        if not self.input_list:
            return None # handle empty list
        return max(self.input_list)
nums=[45,2,49,3]
Finder=MaxFinder(nums)
print('Input:',nums)
print('Largest Number: ',Finder.largest())

# 2 Last Digit in Words: Write a class with a method that takes an integer and prints the last digit of that
# number in words.
# Input:[123]
# Output:Three
class LastDigitInWords:
    digit_words=['Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine']
    def __init__(self,number):
        self.number=number
    def print_last_digit_in_words(self):
        last_digit=abs(self.number)%10 #get last digit
        print(self.digit_words[last_digit])
num=124
obj=LastDigitInWords(num)
print('Input: ',num)
print('Output: ',end='')
obj.print_last_digit_in_words()

# 3 Student Grade Calculator: Implement a Student class with attributes for name and a list of
# marks(for 5 subjects). Include a method to calculate the average and determine the grade.
# Input:[85,78,90,88,91]
# Output:Joy grade=A
class StudentGradeCalculator:
    def __init__(self,name,markslist):
        self.name=name
        self.markslist=markslist # list of marks for 5 subjects
    def average(self):
        avg= sum(self.markslist)/len(self.markslist)
        if avg>=80 and avg<=100:
            return ('grade=A')
        elif 80>avg>=60:
            return ('grade=B')
        elif 60>avg>=40:
            return ('grade=C')
        else:
            return ('grade=D')
        
    
markslist=[85,78,90,88,91]
stu1=StudentGradeCalculator("Joy",markslist)
print(stu1.name,stu1.average())

#------another approach---------------
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks  # list of marks for 5 subjects
    def calculate_average(self):
        return sum(self.marks) / len(self.marks)
    def determine_grade(self):
        avg = self.calculate_average()
        if avg >= 90:
            return 'A+'
        elif avg >= 80:
            return 'A'
        elif avg >= 70:
            return 'B'
        elif avg >= 60:
            return 'C'
        elif avg >= 50:
            return 'D'
        else:
            return 'F'
    def display_result(self):
        grade = self.determine_grade()
        print(f"{self.name} grade={grade}")
marks = [85, 78, 90, 88, 91]
student = Student("Joy", marks)
student.display_result()

# 4 Define an abstract base class Polygon with an abstract method area. Implement this in derived classes Rectangle and Triangle.
# Output:Rectangle Area: 200
# Triangle Area: 50.0

from abc import ABC, abstractmethod
class Polygon(ABC):#abstract method
    @abstractmethod
    def area(self):
        pass

class Rectangle(Polygon):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth

    def area(self):
        return self.length*self.breadth
        

class Triangle(Polygon):
    def __init__(self,base,height):
        self.base=base
        self.height=height
    def area(self):
        return 0.5*self.base*self.height
    
rect=Rectangle(10,20)
tri=Triangle(50,60)
print("Area of Rectangle: ",rect.area())
print("Area of Triangle: ",tri.area())

# 5. Design a class that tracks how many objects have been created from it and has a method to display this count.
class ObjectCounter:
    count = 0   # class variable to track number of objects
    def __init__(self):
        ObjectCounter.count += 1
    @classmethod
    def display_count(cls):
        print("Number of objects -", cls.count)
obj1 = ObjectCounter()
obj2 = ObjectCounter()
obj3 = ObjectCounter()
ObjectCounter.display_count()

# 6. Implement a class Account with a private attribute balance and provide methods to deposit and
# withdraw safely, checking for sufficient funds.
# Ouput:  Deposited: 50, New Balance: 150
#              Withdrew: 100, Remaining Balance: 50
#              Insufficient funds

class Account:
    def __init__(self,initial_balance=0):
        self.__balance=initial_balance

    def deposit(self,amount):
        pass

        
        

        
        
   


        