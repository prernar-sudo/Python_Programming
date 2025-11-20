#If we have more than one characheter always we go for nested loop
#first loop ->responsible for row
#second loop -> for values
n=int(input('Enter number: '))
for i in range(n):
    for j in range(1,n+1):
        print(j,end='')
    print()
#-----------------------------------
n=int(input('Enter number: '))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=' ')
    print()
#-----------------------------------
n=int(input('Enter number: '))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(2*j,end=' ')#2n
    print()
#-----------------------------------
n=int(input('Enter number: '))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(2*j-1,end=' ')#2n-1
    print()
#----------------------------------Formula for increment and decrement------------------------------
x='A'
print(ord(x))#65
x='A'
print(ord(x)+1)#65
print(chr(ord(x)+1))#B
print(chr(ord('c')+1))
#increment and decrement possible in string alsothrough formul ch=chr(ord(ch)+1)
n=int(input('Enter number: '))
# ch='p'
ch=input('Enter starting char: ')
for i in range(n):
    print(ch)
    ch=chr(ord(ch)+1)
#---------------------------------
n=int(input('enter number: '))

for i in range(n):
    ch='A'
    for j in range(n):
        print(ch,end=' ')
        ch=chr(ord(ch)+1)
    print()

