#---------frozenset------------------
#works on set property
#it is designed to freeze the element
#after freezing we can't change the element
#memory will be different bcoz of set , but nature is immutable

#collection of unique element
#represented by frozenset({}) with comma separated elements
#unordered collection
#indexing not supported
#slicing not supported
#immutable in nature

s='python'
l=[10,20,30,'python']
t=(1,2,3,4,'python')
l1=[10,20,30,5]

fs1=frozenset(s)
print(fs1,type(fs1))
fs2=frozenset(l)
print(fs2,type(fs2))
fs3=frozenset(t)
print(fs3,type(fs3))
fs4=frozenset(l1)

#---------------python in-built function-----------
print(len(fs1))
print(id(fs1))
print(type(fs1))
print(fs1)

#------max ,min , sum -> will work on homogeneous-----
print(sum(fs4))

#it is immutable-> so update , pop, u,remove, insert,.....these set methods will not work 

#-------method---------------
fs1=frozenset({1,2,3,4,5})
fs2=frozenset({4,5,6,7,8})

print(fs1.union(fs2))
print(fs1.intersection(fs2))
print(fs1.difference(fs2))
print(fs1.symmetric_difference(fs2))
print(fs1.isdisjoint(fs2))
print(fs1.issuperset(fs2))
print(fs1.issubset(fs2))


