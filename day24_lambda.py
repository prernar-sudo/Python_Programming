# lambda
# a function with no name is called lambda function
# anonomuys function -> meaning lambda
# syntax
'''
    x = lambda parameters:expression
    x(argument)

    As per documentation:
        lambda variable:expression

'''
# it resolve single expression
x=lambda x,y,z:2*x+y+z
print(x(1,2,3))

x=lambda x,y: x if x>y else y
print(x(5,10))

# lambda x,y: if result if condition else else_result

x=lambda age: 'child'  if age>=0 and age<=17 else ('adult' if 17<age<60 else ('senior' if 59<age else 'invalid_age'))
print(x(int(input('Enter age: '))))

# even or not
#x=lambda n: 'even' if n%2==0 else pass
# pass will not work here bcoz, we are not writing else in block or it is not creatng a block
x=lambda n: 'even' if n%2==0 else None
n=int(input('Enter number: '))
print(x(n))

# to find square
x=lambda n:n**2
n=int(input('Enter number: '))
print(x(n))

# to get collection of natural number
x=lambda n:[i for i in range(1,n+1)]
n=int(input('Enter number: '))
print(x(n))

# to get collection of even natural number
x=lambda n:[i for i in range(1,n+1) if i%2==0]  # i to for...(1,n+1) this is -> if result
n=int(input('Enter number: '))
print(x(n))

#--------------------map with lambda--------------------
l=[1,2,3,4,5]
print('---')
print(list(map(lambda n:n**2, l)))

#----------------
l1=[1,2,3,4]
l2=[5,6,7,8]
l3=[9,10,11,12]

print('---')
print(list(map(lambda p,q,r:p+q+r, l1,l2,l3)))
print(list(map(lambda p,q,r:p**0.5+q**0.5+r**0.5, l1,l2,l3)))

#----------------filter with lambda------------------------
l=[1,2,3,4,5,6]
print(list(filter(lambda n: n if n%2==0 else None , l)))
#----------------reduce with lambda------------------------
import functools
l=[1,2,3,4,5,6]
print((functools.reduce(lambda n,m:n+m,l)))
