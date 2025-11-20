l=[10,20,30,40,50]
print(l[::])
print(l[::-1])
print(l[:])
print(l[1:3:5])
print(l[2:-3:4])
print(l[-1::-3])
print(l[-1::3])
#minimum 2 attribu i required, means one colon
#l[start:stop:step/direction/jump]
s='python'
print(s[::])
print(s[::-1])
t=(1,2,3,4,5)
print(t[::])

#u=input("Enter value: ")
# print(u[::-1])
# print(u[::-2])

s='this is python class'
#print(s[::-1][ ])

#-------------------------------range----------------------------------
x=range(10)
print(x)
print(list(x))
x=range(-1,-7,-1)
print(tuple(x))
x=range(-4,0)
print(tuple(x))
x=range(-4,5,2)
print(tuple(x))
x=range(4,4)
print(list(x))#empty
x=range(1,10,-1)
print(list(x))#empty
#to print n natural number, even number, odd number
x=range(2,11,2)#even
print(list(x))
x=range(1,12,2)#odd
print(list(x))
x=range(-10,0,1)
print(list(x))
x=range(-2,-5,1)
print(list(x))#empty list

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
print(list(odd_no)) 


