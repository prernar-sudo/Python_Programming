l=[10,20,30,40,50]
print(l[::])#[10,20,30,40,50]
print(l[::-1])#[50,40,30,20,10]
print(l[:])#[10,20,30,40,50]
print(l[1:3:5])#[20]
print(l[2:-3:4])#[]
print(l[-1::-3])#[50,20]
print(l[-1::3])#[50]
#minimum 2 attribute is required, means one colon
#l[start:stop:step/direction/jump]
s='python'
print(s[::])#python
print(s[::-1])#nohtyp
t=(1,2,3,4,5)
print(t[::])#(1, 2, 3, 4, 5) 

# u=input("Enter value: ")#'python'
# print(u[::-1])#'nohtyp'
# print(u[::-2])#'otp'

s='this is python class'
print(s[::-1][:])#ssalc nohtyp si siht
print(s[2:8:-1])# empyty nothing will be displayed
print(s[2:8:1])# is is
print(s[2:8:1][2:2])# empyty nothing will be displayed

#-------------------------------range----------------------------------
x=range(10)
print(x)#range(0, 10)
print(list(x))#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
x=range(-1,-7,-1)#(-1, -2, -3, -4, -5, -6)
print(tuple(x))
x=range(-4,0)#(-4, -3, -2, -1)
print(tuple(x))
x=range(-4,5,2)#(-4, -2, 0, 2, 4)
print(tuple(x))
x=range(4,4)
print(list(x))#empty #[]
x=range(1,10,-1)
print(list(x))#empty # []
#to print n natural number, even number, odd number
x=range(2,11,2)#even
print(list(x))#[2, 4, 6, 8, 10]
x=range(1,12,2)#odd
print(list(x))#[1, 3, 5, 7, 9, 11]
x=range(-10,0,1)
print(list(x))#[-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]
x=range(-2,-5,1)
print(list(x))#empty list #[]

#---------------------range practice question------------
#Write a program to print all even numbers between 2 and 10 using range()
even_no = range(2,11,2)
print(list(even_no))

even_no=list(range(2,11,2))
print(list(even_no))

lst = [10, 20, 30, 40, 50]
print(lst[2])

data = [5, 10, 15, 20, 25, 30]
print(data[0:3])
print(data[1:7:2])
print(data[1:5])

text = "abcdefgh"
print(text[::-2])
print(text[1])

arr = [10, 20, 30, 40, 50, 60, 70]
print(arr[2:5:2])

odd_no=range(1,5)
print(list(range(1,5,2)))

#-----------------------
data = {'a': [1, 2, 3], 'b': [4, 5], 'c': [6]} 
result = [] 
for key in data: 
    for value in data[key]: 
        if value % 2 == 0: 
            result.append((key, value)) 
result.sort(key=lambda x: x[1], reverse=True) 
print(result)#[('c', 6), ('b', 4), ('a', 2)]
#---------------------
for i in range(5): 
    print(i) 
else: 
    print("Done") 
# 0
# 1
# 2
# 3
# 4
# Done

