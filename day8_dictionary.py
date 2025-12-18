# dictionary
# collection of key value pairs where 'key' and 'value' is separated by:
# represented by {} with comma (,) separated pairs
# {pair1, pair2, pair3}
# key must be unique but value may be duplicate
# mapped datatype
# indexing not supported
# slicing not supported
# mutable in nature

d={'name':'prerna','age':23,'quali':'B.Tech'}
print(d,type(d))#code optimization----less memory, faster processing

#---------------------------dict in-built function---------
print(len(d))
print(type(d))
print(id(d))

print(max(d))
print(min(d))
#print(sum(d))

#ascii ''->32#space
#0-9->47-58
#A-Z->65-90
#a-z->97-122

dict = {1:'prerna',2:'21',3:'B.Tech'}
print(sum(dict))

#-----------------dict methods---------------
print('-----dict methods---------------')
#copy,clear,get,values, keys,items,frame keys, update, pop, popitems, setdefault
print(dict.get(1))#prerna

d1=d.copy()
print(d,d1)# {'name': 'prerna', 'age': 23, 'quali': 'B.Tech'} {'name': 'prerna', 'age': 23, 'quali': 'B.Tech'}
print(id(d),id(d1))#immutable in nature

# d2=d.clear()
# print(d2)#none 

# d.clear()
# print(d)

del d#delete d permanently from memory
#print(d) #we will get error , becoz , del is used to erase data from memory

#--------------------------------------------------------------------
d={'x':10,'y':20,'z':30}
print(d.get('x'))
print(d.keys())
print(d.values())
print(d.items())#list of tuples 
print(d.pop('y'))
print(d)
print(d.popitem())#target last value
print(d)

s='python'
d=dict.fromkeys(s)#convert it into dictionary
print(d)#{'p': None, 'y': None, 't': None, 'h': None, 'o': None, 'n': None}

s1=[10,20,30,'python']
d1=dict.fromkeys(s1,100)
print(d1)

#-------------------------------------updated value
s2=['name','email','contact','add']
d=dict.fromkeys(s2)
d={'name':None,'email':None,'contact':None,'add':None}
n='prerna'
e='prerna@gmail.com'
c=123456
a='Bhopal'

# d['key']=updated_value
d['name']=n
d['email']=e
d['contact']=c
d['add']=a
print(d)

d5={'x':10,'y':20}
d6={'z':30}
d5.update(d6)
print(d5)#updated dict
print(d6)#old dict

#-------------------setdefault
d7={'x':10,'y':20}
print(d7.setdefault('x',30))
print(d7.setdefault('z',30))
print(d7)








