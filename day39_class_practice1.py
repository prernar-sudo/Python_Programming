# 1 Create a class Person with attributes name and age. Add a method show_details() that prints both.
class Person:
    def __init__(self,name,age):
        self.n=name
        self.a=age
    def show_details(self):
        print(f'Name is: {self.n} \nAge is: {self.a} ')

obj=Person('Prerna',23)
obj.show_details()

# 2 Create a class Circle with attribute radius and methods:
# area() → calculate circle area
# circumference() → calculate circle circumference

class Circle:
    def __init__(self,radius):
        self.r=radius
    def area(self):
        return 3.14*self.r*self.r
    def circumfrence(self):
        return 2*3.14*self.r
    
c1=Circle(int(input('Enter Radius: ')))
print("Area of a circle: ",c1.area())
print("Circumference of a circle: ",c1.circumfrence())

# 3. Create a class Student with a class variable school_name and instance variables name and roll.
#    Initialize them in constructor and create a method show() that displays details.

class Student:
    school_name='MontFort' #class variable
    def __init__(self,name,roll):
        self.n=name
        self.r=roll
    def show(self):
        print(f'School Name: {Student.school_name} , Name: {self.n}, Roll_No.:{self.r}')
s1=Student('Prerna',20)
s2=Student('Priya',19)
s1.show()
s2.show()

#  Create a class BankAccount with methods:
# **deposit(amount) **→ add money
# **withdraw(amount) **→ subtract money if balance is sufficient
# **check_balance() **→ print balance

class BankAccount:
    def __init__(self,owner,balance=0):
        self.owner=owner
        self.balance=balance
        
    def deposit(self,amount):
        self.balance+=amount
        print(f'Deposited amount:{amount}, Total Balance: {self.balance}')

    def withdraw(self,amount):
        if self.balance<amount:
            print('Insufficient Balance')
        else:
            self.balance-=amount
            print(f'Withdrawl amount: {amount}, Remaining Balance: {self.balance}')

    def check_balance(self):
        print(f'Current balance is {self.balance}')
customer1=BankAccount('Prerna',5000)
customer1.deposit(3000)
customer1.withdraw(1000)
customer1.check_balance()

# 5 Create a class Employee with attributes name and salary. Add a method get_tax() that calculates 10% of the salary as tax.

class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def get_tax(self):
        return 0.10*self.salary
e1=Employee('Prerna',50000)
print(f'Employee Name: {e1.name}, Tax Amount:{e1.get_tax()}')

# 6 Inheritance Practice:
# Class Animal → method speak()
# Class Dog (inherits Animal) → override speak() to print "Woof!"
# Class Cat (inherits Animal) → override speak() to print "Meow!"

class Animal:
    def speak(self):
        print("I'm an animal")
class Dog(Animal):
    def speak(self):
        print("Woof! from dog child")
        #super().speak()
class Cat(Animal):
    def speak(self):
        print("Meow! from cat child ")
        #super().speak()
# class combi(Dog,Cat):
#     pass

a=Animal()
b=Dog()
c=Cat()
a.speak()
b.speak()
c.speak()

# 7 Create a class ShoppingCart with methods:
# add_item(item, price) → add items to cart
# remove_item(item) → remove item from cart
# get_total() → return total price of items
# Use a dictionary to store items and prices.

class ShoppingCart:
    def __init__(self):
        self.items={}
    
    def add_item(self, item ,price):
        self.items[item]=price
        print(f'Added item: {item}-{price}')

    def remove_item(self, item):
        if item in self.items:
            del self.items[item]
            print(f"Removed item: {item}")
        else:
            print(f"{item} not found in cart")

    def get_total(self):
        return sum(self.items.values())
    
cart=ShoppingCart()
cart.add_item('shirt',1200)
cart.add_item('trouser',1500)
cart.remove_item('shirt')
print("Total: ",cart.get_total())

# 8 Create a class Library that maintains a list of books. Methods:
# add_book(title)
# remove_book(title)
# display_books() → show all books
class Library:
    def __init__(self):
        self.books=[]

    def add_book(self,title):
        self.books.append(title)
        print(f'Book - {title} Added')

    def remove_book(self, title):
        if title in self.books:
            self.books.remove(title)
            print(f'Book -{title} Removed')
        else:
            print(f'Book {title} not found')

    def display_books(self):
        print(f'Books in Library: {self.books}')
book=Library()
book.add_book('You Can Win')
book.add_book('Alchemist')
book.add_book('Ikigai')
book.display_books()
book.remove_book('Alchemist')
book.display_books()

# 9 Create a class Math with:
# Static method factorial(n)
# Class method square(cls, x)
# Test both methods.

class Math:
    @staticmethod
    def factorial(n):
        result=1
        for i in range(1,n+1):
            if i<=n:
                result*=i
        return result

    @classmethod
    def square(cls,x):
        return x*x

print('Factorial is: ',Math.factorial(5))
print('Square is: ',Math.square(8))

#10 Multiple Inheritance Practice:
# Class Teacher → method teach()
# Class Student → method study()
# Class TeachingAssistant inherits from both Teacher and Student, and should be able to call both teach() and study().

class Teacher:
    def teach(self):
        print('Teach from Teacher class')
class Student:
    def study(self):
        print('study from student class')
class TeachingAssistant(Teacher,Student):
    # def assist(self):
    #     print('Assisting teacher and helping students')
    pass
        
ta=TeachingAssistant()
ta.teach()
ta.study()

