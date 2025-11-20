#list
#collection of elements
#represented by [] with comma (,) separated value
#ordered collection
#indexing supported
#slicing supported
#duplicates are allowed
#mutable in nature (CRUD operation can be performed)
#empty list is false->check by boolean value 
#hw->checkevery operator on list, and make a list whicg is working or not
#list is a collection of homogeneous and hetrogeneous 

#---------------------Python in -built function for list---------
# max(), min(), sum() ->{we can only use, when the collection is homogeneous-}
# len(), type(), id() ->these func. does not depend on datatype element

l=[10,20,'python','java',10,20]#heterogeneous
l1=['python','java','php']#homogeneous
print(l)
print(type(l))
#print(max(l))
print(max(l1))#python
print(min(l1))#java
#print(sum(l1))#error-> for sum it is imp to have numeric value, then only it will work
print(len(l1))
print(type(l1))
print(id(l1))
print(len(l))
print(type(l))
print(id(l))

#-----------------------------list methods--------------------------------------------------
l=[1,2,3,4,5]
l=[2,4,6,8,'python',3,5]
n=eval(input("Enter any value: "))
print(l.append(n))#to add element in the list #add single element in last position#o/p->none
print(l)
# l.copy()#create new object with same element
# l.clear()#clear all element from list
# print(l)
# l.index(1)#findout order/location of any element
# l.count()#findout frequncy of any element
print(l.pop())#remove index targeted element, by default it remove -1 index element
print(l)

# l.remove()#remove targeted element
n=eval(input("Enter any value: "))
print(l.extend(n))#add multiple element at last position #it should be a collection at int we get error
print(l)
# l.sort()#to arrange all element in ascending order #sort need same data type of collection
# #to arrange in descending order, first sort, then reverse
# l.reverse()#to reverse all given element 
n=eval(input("Enter any value: "))
l.insert(5,"fifth")#add element in targeted position ->insert(position,element)
print(l)

l.remove('python')
print(l)

m=[1,2,3,'java']
print(l.index('java'))
print(l.count('python'))




#differnce between function and method



