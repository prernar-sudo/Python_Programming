#set->collection of unique elements, unordered collection
#order is changing through hashing technique
my_set={10,10,30,'python','java'}
print(my_set,type(my_set))

#empty set->can onlybe declared using set inbuilt method
my_set=set()
print(my_set,type(my_set))

#frozenset
print('-----frozenset---------')
my_set={10,10,30,'python','java'}
fs=frozenset(my_set)
print(fs,type(fs))

l=[10,20,10,'python']
print(frozenset(l), type(frozenset(l)))

s='python'
print(frozenset(s))

# _i=10  #it is not a collection
# print(frozenset(_i))

#empty frozenset
fs=frozenset()
print(fs,type(fs))

#boolean
print('-----boolean---------')
x=True
y=False

print(x,y,type(x),type(y))
#empty boolean is not possible

#none
print('-----None---------')
x=None  #N->uppercase 
y='None'
print(x,y,type(x),type(y))

x=True
Y='True'
z=True,
w=(True)
print(x,y,z,w,type(z),type(w))
#----------------------------------

#object-nature

x=10
y=10
print(id(x),id(y)) #immutable, unchangeable

x=10.0
y=10.0
print(id(x),id(y))

x=10+0j
y=10+0j
print(id(x),id(y))

#list
print('--------list: mutable->changeable--------')
x=[10,20,30,"Python"]
y=[10,20,30,"Python"]
print(id(x),id(y))

#tuple
x=(10,20,30,"Python")
y=(10,20,30,"Python")
print(id(x),id(y))

#string
x='python'
y='python'
print(id(x),id(y))

#dict
print('--------dict: mutable->changeable--------')
x={'name':'prerna', 'age':22}
y={'name':'prerna', 'age':22}
print(id(x),id(y))

#set
print('--------set: mutable->changeable--------')
x={10,10,20}
y={10,10,20}
print(id(x),id(y))

#frozenset
print('--------frozenset: immutable->exception--------')
x=frozenset(x)
y=frozenset(y)
print(id(x),id(y))

fs1=(1,2,3)
fs2=(1,2,3)
fs1_=frozenset(fs1)
fs2_=frozenset(fs2)
print(id(fs1_),id(fs2_))

x=None
y=None
print(id(x),id(y))




