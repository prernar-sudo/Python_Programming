s='python'
print(s.index('t')) #2

#in python -ve indexing is only for representation, it does not exist in memory
#order (or sequence) of element in any collection is called index number
#orderedcollection-> (string, tuple, list)

#index ->is in- built method of python
#space ->ascii value is 32 ->it will also take memory

s1 = 'THIS IS PYTHON'
print(s1.index('Y'))
#print(s1.index('i'))  #substring not found
print(s1.index('S I'))
#print(s1.index('P',9)) #substring not found
#print(s1.index('P',100))
#print(s1.index('P',-2)) 
#print(s1.index('P',5,8)) #stop point should be +1 -> 9
#print(s1.index('P',5,4))
print(s1.index('P',5,9))

#in index function , we have passed three arguments always

list=[1,'two',3,4,5,6,7,8,9,10]
element='two'
print(list.index(element))
