# s=input('Enter any value')#121
# if s==s[::-1]:
#     print(f'{s} is palindrome')
# else:
#     print(f'{s} is not palindrome')
# #-----------------------------------------------
# s_='python'
# s1=''
# for i in s_:
#     s1=i+s1
# print(s1)

# #------------------------------------------------

# n=int(input('Enter Number: '))
# i,l=2,[]
# while i<n:
#     if n%i==0:
#         l.append(i)
#     i=i+1
# print(f'Factors of {n} is {l}')

#-------------------------------------------------

n=5
i=1
# ch='A'
# j=1
while i<=n:
    ch='A'
    j=1
    while j<=n:
        print(ch,end='')
        ch=chr(ord(ch)+1)
        j=j+1
    i=i+1
    print()

#------------------------------
n=int(input('Enter number: '))
for _ in range(1,n+1):
    for i in range(1,n+1):
        print(i,end=' ')
    print()

# 1 2 3 4 5 
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5

#------------------------------
n=int(input('Enter number: '))
for x in range(1,n+1):
    for i in range(1,x+1):
        print(i,end=' ')
    print()
# 1 
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

#------------------------------
n=int(input('Enter number: '))
for x in range(1,n+1):
    for i in range(1,x+1):
        print(2*i,end=' ')
    print()

# 2 
# 2 4
# 2 4 6
# 2 4 6 8
# 2 4 6 8 10

#------------------------------
n=int(input('Enter number: '))
for x in range(1,n+1):
    for i in range(1,x+1):
        print(2*i-1,end=' ')
    print()

# 1 
# 1 3
# 1 3 5
# 1 3 5 7
# 1 3 5 7 9

#------------------------------
n=int(input('Enter number: '))
y=1
for x in range(1,n+1):
    for i in range(1,x+1):
        print(y,end=' ')
        y=y+1
    print()

# 1  
# 2  3
# 4  5  6
# 7  8  9  10
# 11  12  13  14  15

#------------------------------
n=int(input('Enter number: '))

for x in range(1,n+1):
    y=1
    for i in range(1,x+1):
        print(y,end=' ')
        y=y+1
    print()

# 1 
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5   

#------------------------------
#H.W

# ----1----
# ---1 2----
# --1 2 3---
# -1 2 3 4---
# 1 2 3 4 5