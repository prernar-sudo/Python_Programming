# IF-ELIF-ELSE STATEMENT :-

# Example 1: Write a program to check given no is positive. (Only
# if-statement)
n=int(input('Enter the number: '))
if n>=1:
    print(f'Given number {n} is positive')

# Example 2: Write a program to
# check given no is positive or negative. (Only if-else statement)
n=int(input('Enter the number: '))
if n>0:
    print(f'Given number {n} is positive')
else:
    print(f'Given number {n} is negative')


# Example 3: Write a program to
# check given no is positive, negative or Zero.(Only if-elif-else statement)
n=int(input('Enter the number: '))
if n>0:
    print(f'Given number {n} is positive')
elif n==0:
    print(f'Given number {n} is zero')
else:
    print(f'Given number {n} is negative')


# Example 4: Write a program to
# swap two variables without using third variable.
a=40
b=20
a,b=b,a
print('afer swap first number becomes: ',a)
print('afer swap second number becomes: ',b)



# Example 5: Write a program to
# swap two variables using third variable.
a=40
b=20
print(f'Before swap, first value {a}')
print(f'Before swap, second value {b}')
temp=a
a=b
b=temp
print(f'After swap, first value {a}')
print(f'After swap, second value {b}')

# Example 6: Write a program to
# swap two variables using using Addition and Subtraction.
a=40
b=20
print(f'Before swap, first value {a}')
print(f'Before swap, second value {b}')
temp = a+b
a=temp-a
b=temp-b
print(f'After swap, first value {a}')
print(f'After swap, second value {b}')



# Example 9: Write a program to
# find squre root of given no.
n=int(input('Enter Number: '))
sqrt=n**2
print(f'sqrt of {n} is: {sqrt}')



# Example 10: Write a program to
# find largest no among the three inputs numbers.
n1=int(input('Enter first number: '))
n2=int(input('Enter Second Number: '))
n3=int(input('Enter third Number: '))
if n1>n2 and n1>n3:
    print(f'First number {n1} is greater')
elif n2>n3:
    print(f'Second number {n2} is greater')
else:
    print(f'Third number {n3} is greater')

# Example 11: Write a program to
# find area of triangle. (1/2* hight*base)
b=int(input('enter base: '))
h=int(input('enter height: '))
area=0.5*b*h
print(f'area of triangle is: {area}')

# Example 12: Write a program to
# find area of square.
side=int(input('enter side of a sq: '))
print(f'area of a square is: {side**2}')


# Example 13: Write a program to find given year is
# leap year or not.
year=int(input('Enter year: '))
if (year%4==0 and year%100!=0) or year%400==0:
    print(f'year {year} is Leap Year')
else:
    print(f'Year {year} is not a leap year')