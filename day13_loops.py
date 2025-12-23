# To avoid same block of code repetition, we use looping or iterative statement  
#Iterative/ looping statement
# 1. while (infinite iteration)
#---while-else
# 2. for  (finite iteration)
#----for-else 

#---------------for loop----------
# syntax: for i in iterable: #iterable--->collection
s='python'
for i in s:
    print(i)

l=[1,2,3,4,5]
for i in l:
    print(i)
    print(i+5)

t=(1,2,3,4,'python')
for i in t:
    print(i)

d={'x':10,'y':20,'z':30}
for i in d:
    print(i,'=',d[i])

#-------------order is not same--------so we don't use set or frozenset with loop
s={1,2,3,4,'python'}
for i in s:
    print(i)
#---------------------
s=input('Enter your name: ')
#print(s.isalpha())
s=s.replace(' ','')#removed space
v=c=0
print(s)
# we are able to check is the entered value is alpha bet or not
if s.isalpha():
    print('alphabets')
    s=s.lower()
    for i in s:
        if i in ('a','e','i','o','u'):
            v=v+1
        else:
            c=c+1
    print('vowel',v)
    print('consonant',c)
else:
    print('not alpha/Please enter only alphabets')

# WAP to print n natural numbers
n=int(input('Enter number: '))
for i in range(1,n+1):
    # print(i,end=' ')
    # print(i,end=',')#remove comma after 10

    if i<n:
        print(i,end=',')
    else:
        print(i)

#-------------------------
n=int(input('Enter number: '))
sum=0
for i in range(1,n+1):
    # print(i,end=' ')
    # print(i,end=',')#remove comma after 10
    sum=sum+i
    if i<n:
        print(i,end='+')
    else:
        print(i,end='=')
print(sum)

#wap to print n even number
#even number formula =>2n , wher n is natural number
n=int(input('Enter number: '))
for i in range(1,n+1):
    if i<n:
        print(i*2,end=',')
    else:
        print(2*i)
#-------------2+4+6+8+10=sum
n=int(input('Enter number: '))
sum=0
for i in range(1,n+1):
    sum=sum+2*i
    if i<n:
        print(i*2,end='+')
    else:
        print(2*i,end='=')
print(sum)

#------odd number : 2n-1, wher n is natural number
n=int(input('enter number: '))
for i in range(1,n+1):
    if i<n:
        print(2*i-1,end=',')
    else:
        print(i*2-1)

#------
n=int(input('enter number: '))
sum=0
for i in range(1,n+1):
    sum=sum+(2*i-1)
    if i<n:
        print(2*i-1,end='+')
    else:
        print(i*2-1,end='=')
print(sum)
#------------------------------------

n=5
for i in range(1,6):
    print('*'*5)


