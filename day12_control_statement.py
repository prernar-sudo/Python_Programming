#control statement
#if statement (single condition)
#if else statment
# if elif statement (multiple condition )
#if - elif-else statement

# three keyword 
# if -independent key
# elif , else -dependent key

#if statement: block may be executed
# synatx: if (condition):
# if- body executed when given condition is true

n=0
if n>=1:
    print("given number is +ve") #not executed

# if -else statement (block must be executed)
#syntax: if(condition):
#             if block executed when given condition is True
# else:
#      else block exceute ehen given condition is false


n=int(input("Enter any value: "))
if n>=1:
    print(f'given number is {n} +ve') #f string
else:
    print(f'given number is {n} either -ve or zero')

#if elif statement (block may be executed)

n=int(input("Enter any value: "))
if n>=1:
    print(f'given number is {n} +ve') #f string
elif n==0:
    print(f'given number {n} is zero')

#if-elif-else statement (block must be executed)
n=int(input("Enter any value: "))
if n>=1:
    print(f'given number is {n} +ve') #f string
elif n==0:
    print(f'given number {n} is zero')
else:
    print(f'given number {n} is -ve ')

#------------------------ set boundary first------------
age=float(input("Enter age: "))
if 0<age<18:
    print("child")
elif 17<age<60:
    print('adult')
elif 59<age<100:
    print('senior citizen')
else:
    print(f"invalid age is entered {age}")

#------------------------
h = int(input('enter hindi marks: '))
if 0<=h<=100:
    e=int(input('enter english marks: '))
    if  0<=e<=100:
        m=int(input('enter maths marks: '))
        if 0<=m<=100:
            avg = ((h+e+m)/3)
            if 0<=avg<=34:
                print(f'fail: obtained marks {avg}')
            elif 35<=avg<=44:
                print(f'3rd division: obtained marks {avg}')
            elif 45<=avg<=59:
                print(f'2nd division: obtained marks {avg}')
            else:
                print(f'first division: obtained marks {avg}')
        else:
            print(f'enter marks in between 0 to 100: not->{m}')
        
    else:
        print(f'enter marks in between 0 to 100: not->{e}')
else:
    print(f'enter marks in between 0 to 100: not->{h}')

#------------drawback of if-else--------
# if same block of code is repeating in continuous manner
# To avoid same block of code repetition, we use looping or iterative statement  




