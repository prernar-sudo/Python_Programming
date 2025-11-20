#For typecasting -> python has in-built function (int(),float(),complex(),str(),list(),tuple(),dict(),set(),frozenset())
#it is used to change one data type into another
#for empty declaraion, we have also used this
#chr ord  in built function-something extra

x=10.5
y=int(x)
print(y)
z=float(y)
print(z)

w=complex(z)
print(w)

p=input()
q=str(p)
print(q)

l=[10,20,30]
t=tuple(l)
print(t)

l1=list(t)
print(l1)

s1=set(l1)
print(s1)

fs=frozenset(s1)
print(fs)

#---------about print function------------ end , sep is argument-------------------
#print does not start at new line, it et terminates to new line
#print->by default terminate to new line
print(sep=' ',end='\n') #sep is separator
print("Hello",end='') #we can end at , normal , or by giving space, or + sign, then see the magic
print("Welcome")
print("Hello", end='+')
print("Welcome")

#Separator
print(10,20)
print(10,20,sep=',')

#------------------input()----is used totake value from user at runtime------------
x=input('Enter any value: ')
print(x) 
print(type(x))#give any value it will always give str, at any data type whether it is int , float, tuple, list

#-------------eval()-------in-built function---------
x=eval(input("Enter any value: "))
print(x)
print(type(x))
#by doing typecasting
#but remember at runtime give the value in correct format eg-> 'hello', {1,2,3}
#, is responsible for tuple
x=10
print(type(x))#int
y=(10)
print(type(x))#int