x=10
y=20

#int
print(x,y)
print(type(x),type(y))

#float
a=10.5
b=0.2
print(a,b)
print(type(a),type(b))

#complex
c=5+3j
d=4+1j #don't give j alone , it will give error
print(c,d)
print(type(c),type(d))

#empty int, empty float, empty complex

e=0
print(type(e))

f=0.0
print(type(f))

g=0j
print(type(g))

# int , float, complex, inbuilt function
_e=int()
print(type(_e),_e)

_f=float()
print(type(_f),_f)

_g=complex()
print(type(_g),_g)
#--------------------literals
#string

s1='python'
s2="python"
s3='''python'''
print(type(s1),type(s2),type(s3))
print(s1,s2,s3)

#using backslash, we can print single quote inside single quote
s4='this is \'python\' class'
s5="this is \"python\" class"
s6='''Hello 'folks'
	this "is" python class'''
print(s4,s5,s6)
print(s4, type(s4))
#----------------------------
#list
l1=[2,4,6,8]
l2=[2,4,"Python",10.5,"Java"]
print(l1,l2,type(l1),type(l2))
#empty list
l=[]
print(l,type(l))
_l=list()
print(_l,type(_l))
#-----------------------------
#tuple
t=('element1','element2','element3')
t1=(2,4,6,8)
t2=(2,"Python",3.56,"Java",5+0j)
print(t1,t2,type(t1),type(t2))
#empty tuple
t=()
print(t,type(t))
_t=tuple()
print(_t,type(_t))
#----------------------------
#integer and tuple relation->, is responsible to tell difference between tuple and ineger
x=10
y=10,
z=(10)
p=(10,)
q=(10),
print(x,y,z,p,q,type(x),type(y),type(z),type(p),type(q))
#--------------------------------
#dictionary->collection of key value pairs 
d1={'name':'prerna', 'age':22, 1:'python'}
print(d1,type(d1))
#empty dictionary
d={}
print(d,type(d))
_d=dict()
print(_d,type(_d))




