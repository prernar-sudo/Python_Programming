# ---------------------Theory paper-------------------------------
# 1. What is python and what are the advantage and disadvantage of python
# 2. Explain internal working of python
# 3. What is walrus operator in python. Explain with example
# 4. Write difference between continue, break , pass. Explain with example
# 5. Write difference between return and yield. Explain with example
# 6. What is python objects and their types. Explain why python object are call  by refernce
# 7. Explain difference between indexing and slicing
# 8. Explain split , replace and join method with example
# 9. Explain relation between Arguments and Returns types in python with example
# 10. What is pickling, unpickling and PEP in python

#-----------------Coding paper-------------------------------------
# 1.Wap to check if given number is palindrome or not.
n=int(input('Enter number: '))
original=n
rev_no=0
while n:
    ld=n%10
    rev_no=rev_no*10+ld
    n=n//10
if original==rev_no:
    print(f'Given number {original} is palindrome')
else:
    print("Not a Palindrome")
# 2.Wap to check if a given number is spy or not (Example Input: 1412, check 1+4+1+2==1*4*1*2 Output: Spy number)
n=int(input('Enter number: '))
ori=n
total=0
while n:
    ld=n%10
    total=total+ld
    n=n//10
mul=1
while ori:
    ld=ori%10
    mul=mul*ld
    ori=ori//10

if total==mul:
    print('Spy Number')
else:
    print('Not a spy number')

# approach 2
# n = int(input("Enter number: "))
# temp = n
# sum_d = 0
# prod_d = 1

# while temp > 0:
#     d = temp % 10
#     sum_d += d
#     prod_d *= d
#     temp //= 10

# if sum_d == prod_d:
#     print("Spy Number")
# else:
#     print("Not Spy Number")




# 3.Wap to print below mention pattern:
# 1 2 3 4 5
#  1 2 3 4
#   1 2 3
#    1 2
#     1
n = int(input("Enter number of rows: "))

for i in range(n, 0, -1):
    print(" " * (n - i), end="")
    for j in range(1, i + 1):
        print(j, end=" ")
    print()


# 4.Python program that accepts a string and calculate the number of digits and letters
s=input('Enter string: ')
digit=0
letters=0
for i in s:
    if i.isdigit():
        digit+=1
    elif i.isalpha():
        letters+=1
print('Number of digit: ',digit)
print('number of letter: ',letters)


# 5.Python program to get a fibonacci series (0,1,1,2,3,5,8......)
n=int(input('Enter Number: '))
a,b=0,1
for i in range(n):  
    print(a,end=' ')
    a,b=b,a+b
# 6.Wap to check if a given number is an Armstrong or not  example 153 (1**3+5**3+3**3=1+125+27=153)
n=int(input('Enter number: '))
temp=n
digit=len(str(n))
pow_sum=0
while temp:
   ld=temp%10
   pow_sum=pow_sum+(ld**digit)
   temp=temp//10
if n==pow_sum:
    print('Armstrong number')
else:
    print('Not Armstrong number')


# 7.Wap to check if a given number is sunny number or not (Example 19 is a sunny number because 1**2+9**2==82,now 8+2==1+9)
# 8.Write a code to print below mention patterns
# A B C D E 
#  A B C D 
#   A B C 
#    A B 
#     A
# 9.Wap to check if a given number is peterson or not (Example n=145, sum of 1!+4!+5+=145)
# 10.Wap to take input string from user and calculate how many vowels and consonants are present on their string
s=input('Enter string: ').lower()
v,c=0,0
for i in s:
    if i.isalpha():
        #if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        if i in 'aeiou':
            v+=1
        else:
            c+=1
print(f'Vowel = {v}, Consonant = {c}')
    
# 11. Write a program to check if the given string are anagram or not(python=typhon)
# An anagram is a word or phrase formed by rearranging the letters of another word or phrase, using all the same letters exactly once.
first=input('Enter first string: ').lower()
second=input("Enter second string: ").lower()

if sorted(first)==sorted(second):
    print('Anagram')
else:
    print('Not Anagram')
