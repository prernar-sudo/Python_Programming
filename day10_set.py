#-----------------------set methods--------------
#-----------1. that required more than one set
#-----------2. that required only one set

# 1. union
# 2. intersection
# 3. Difference
# 4. symmetric difference
# 5. intersection update
# 6. difference update
# 7. symmetric difference update
# 8. issubset
# 9. issuperset()
# 10. isdisjoint()

s1,s2={1,2,3,4,5},{4,5,6,7,8}
print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))
print(s1.symmetric_difference(s2))
#print(s1.intersection_update(s2))
# s1.intersection_update(s2)
# print(s1)
# print(s2)
#----------
s1.difference_update(s2)
print(s1)#comment intersection code 
print(s2)

#---------------------
s1,s2={1,2,3,4,5,6,7,8,9},{5,6,7,8,9}
print(s1.issuperset(s2))
print(s2.issuperset(s1))
print(s1.issubset(s2))
print(s2.issubset(s1))

#---------------------------isdisjoint
#case:1
s1,s2={1,2,3,4,5},{6,7,8,9,10}
print(s1.isdisjoint(s1))
print(s2.isdisjoint(s1))
#case:2
s1,s2={1,2,3,4,5},{5,6,7,8,9}
print(s1.isdisjoint(s2))
print(s2.isdisjoint(s1))

#-----------------------method: that work on single set-----------------
#add(),update(),remove,discard,pop,clear,copy
s={1,2,3,'python','java'}
s1=s.copy()
print(s1)
print(id(s1),id(s))

# s.clear()
# print(s) 

#to remove it from memory 
# del s
# print(s) #-> we'll get not defined error

#add-> to add any element at random position,bcoz position is not fixed in set
s.add('php')
print(s)

#update-> to add multiple element, 
s.update({1,2,3,4,5,6})
print(s)

print(s.pop())

s.remove('python')#to delete targeted element, we use remove
print(s)

# s.remove('prerna')#this will give error, bcoz element is not present
# print(s)#to preent remove error,we use discard

s.discard('prerna')
print(s)

s.clear()
print(s) 
