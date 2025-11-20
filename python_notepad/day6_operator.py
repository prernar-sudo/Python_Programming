#Arithmetic (+,-,*,/,%,//,**)->it will return value
x=45
y=10

print(x+y)
print(x-y)
print(x*y)
print(x/y)
#it will divide the value till fractional value
print(x//y)
print(x%y)
#---------------

x=246532
y=10
#to remove last digit we always bring the floor of it 
print(x//10)
print(x%y)

x=2
y=5
print(x**y)
#------------------Assignment (=, +=,-=,*-,/=,//=,%=,**=)-------- (walrus return by value)
#note: without walrus, it will not return anything, 
#in statement the value is only assigned, but in expressions, it will assign and return
x=10
print(x)
#print(y=20) is a statement , it will not return value, so it will not print
#walrus operator (:=) ->is a expression; it can convert any statement into expressions
print(y:=20)
#python does not have increment or decrement operator, so we have expression
x=10
print(x)
x=x+1
print(x)
x=x-1
print(x)
x+=1
print(x)
x-=1
print(x)
x*=2
print(x)
x/=3
print(x)
x//=3
print(x)
x%=3
print(x)
x**=2
print(x)
print('----comparison----------')
#----------comparison----(==,!=,>,>=,<,<=)->return boolean value
x=10
y=20
print(x==y)
print(x!=y)
print(x>y)
print(x>=y)
print(x<y)
print(x<=y)
print("---------logical----------")

#4. -----Logical operator(and, or, not)---->return boolean value
x=10
y=15
z=20
print((x>y)and(x<z))
print((x>y)or(x<z))
print(not(x>y))
print(not((x>y)or(x<z)))
print('----------day7--membership----------------')

#5.---------membersip operator(in,not in)-----------return boolean value
s='python'
print('P' in s)
print('P' not in s)

l=[10,20,30,'python','java']
print(2 in l)
print(2 not in l)

t=(10,20,30,'python','java')
print('tuple: ',2 in t)
print(2 not in t)

d={'name':'prerna', 'age':22}
print('name' in d)
print('qualification'  not in d)

s1={10,20,30,'python','java'}
print(20 in s1)
print(2 not in s1)
print('-------------identity---------')
#6.------------identity operator (is, is not)--------------- return boolean value 
#identity operator compare on basis of memory
#iq(interview/ques)->difference b/w is and == operator
#is->compare memory address
#== -> compare values
x=10
y=20
print(x is y)

#7.-------------Bitwise operator (&, |, ^, ~,>>,<<)-------- return value
x=30
y=20
z=7

print(x&y)
print(f'{x}^{y}={x^y}')
print(f'{x}~{y}={~x}')
print(x|y)
print(z<<1)
print(z<<2)
#------------day8---------pyhon-object-> is call by reference
x=10 #memory will point to 10, no memory will assigned to x
y=10
print(id(x),id(y))
#i.e why?->python is dynamically typed language
#memory assigned at runtime
#-------------------------------
#only python object gets memory address
#on the basis of nature mutable(changeable),immutable(not changeable)
#--------------------------------
x=10
y=10
print(id(x),id(y))#immutable
x=10.1
y=10.1
print(id(x),id(y))#immutable
x=10.1+0j
y=10.1+0j
print(id(x),id(y))#immutable
x='python'
y='python'
print(id(x),id(y))#immutable
x=True
y=True
print(id(x),id(y))#immutable
x=(10,20,30,'python','java')
y=(10,20,30,'python','java')
print(id(x),id(y))#immutable

x=[10,20,30,'python','java']
y=[10,20,30,'python','java']
print(id(x),id(y))#mutable

x={'name':'prerna', 'age':22}
y={'name':'prerna', 'age':22}
print(id(x),id(y))#mutable

x={10,20,30,'python','java'}
y={10,20,30,'python','java'}
print(id(x),id(y))#mutable

x=None
y=None
print(id(x),id(y))#immutable

x=frozenset({10,20,30,'python','java'})
y=frozenset({10,20,30,'python','java'})
print(id(x),id(y))#immutable->exception 

#numeric and string can never be mutable 
#required bit for empty objects

import sys
x=int()
print(sys.getsizeof(x))

x=float()
print(sys.getsizeof(x))

x=complex()
print(sys.getsizeof(x))

x=str()
print(sys.getsizeof(x))

x=list()
print(sys.getsizeof(x))

x=tuple()
print(sys.getsizeof(x))

x=dict()
print(sys.getsizeof(x))

x=set()
print(sys.getsizeof(x))

x=frozenset()
print(sys.getsizeof(x))

x=bool()
print(sys.getsizeof(x))

#difference between all literals type 
#difference of list and tuple
#->required nature
#->representation
#->speed
#tuple is faster then list


#python  disavntage-> memory management is not in users hand

#python comment
#single line comment (#)->ctrl+/
#multiline comment (''' ''')->

#multiline string vs multiline comment
#difference-> in multiline string is always  put on right side of equals to 
#-----------------------------------------------
#CONTROL STATEMENT
x=int(input("Enter any value: "))
if x>10:
 print("Greater than")
print("nxt statement")









