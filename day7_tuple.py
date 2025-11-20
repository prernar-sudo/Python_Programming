#tuple->
#collection of elements
#represented by () with comma(,) separated elements
#ordered collection
#indexing supported
#slicing supported
#duplicates are allowed
#immutable in nature
t=(1,2,3,4)
t1=(8,9)
print(t+t1)
print(t)
print(type(t))

#------------------------------------tuple---------------(python in built)functions
#len(),type(),id(),print()
#max(),min(),sum()
print(len(t))
print(type(t))
print(id(t))
print(t)

#max , min, sum only works if we have same datatype and collection
print(max(t))
print(min(t))
print(sum(t))

#---------------tuple------------method
print(t.index(1))
print(t.count(2))

