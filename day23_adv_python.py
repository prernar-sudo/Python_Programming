#----------------------advance python----------------------

# Higher order function
# ---->map()   ----> returns collection
# ---->filter() ----> returns collection
# ---->reduce() ----> returns value

# Lambda function
# decorator
# generator
# oop's
# file handling
# error handling 

#----------------------------------------------------------------------------------------------------

# higher order func. -> it is something , when we pass a func. as an argument inside a func.

# map() --> returns collection
#---------syntax----------
''' 
    iterable1
    iterable2
    iterable3
    def func_name(parameter1, para2, para3,....):
    
    res=map(func_name,iterable1, iterable2, iterable3....)
    print(list(res))

    # as per documentation -> map(function,iterable)
    
'''
l1=[1,2,3,4]
l2=[5,6,7,8]
l3=[9,10,11,12]
def add(x,y,z):
    return x+y+z
res=map(add,l1,l2,l3)
print(res)#<map object at 0x000001B5D75CBA00>
print(type(res))#<class 'map'>
print(tuple(res))

# total no. of input element = total number of output element
# if we keep different number of input element suppose, than it will 

l1=[2,3,4,5]
def sqr(n):
    return n**2

res=map(sqr,l1)
print(tuple(res))
#print(list(res))

def square_Root(n):
    return n**0.5

res1=map(square_Root,l1)
print(list(res1))

#in case of string, use join 

#---------------------------------Filter-----------------------------------
#---- given only one iterable
#syntax
'''
        iterable
        def func_name(parameter):
        
            return
        
        res=filter(func_name,iterable)
        print(list(res))


'''
#------------------------------
l=[1,2,3,4,5,6]
def greater3(n):
    if n>=3:
        return n
res=filter(greater3,l)
print(list(res))

def even(n):
    if n%2==0:
        return n
res=filter(even,l)
print(list(res))

def odd(n):
    if n%2!=0:
        return n
res=filter(odd,l)
print(list(res))

#----------------------------------reduce---------------------------------
#syntax: 
'''
    iterable
    def func_name(parameter1,parameter2)

    res=reduce(func_name,iterable)
    # below is another syntax or method, initial value parameter is optional
    res=reduce(func_name,iterable,initial value)
    print(res)
'''
import functools
l=[1,2,3,4,5]
def sum(x,y):
    return x+y

res=functools.reduce(sum,l)
#If we give initial value - then loop will run one time extra
#if it is necessary than , we have to use initial value
#res=functools.reduce(sum,l,0)
print(res)

def max_(x,y):
    return max(x,y)
res=functools.reduce(max_,l)
print(res)

def min_(x,y):
    return min(x,y)
res=functools.reduce(min_,l)
print(res)

def maxi(x,y):
    if x>y:
        return x
    else:
        return y
res=functools.reduce(max,l)
print(res)

l1=[1,2,3,4]
def sq_sum(x,y):
    return x+y**2 # jo bhi value return hogi woh x mai store
res=functools.reduce(sq_sum,l1,0)
print(res)

def fact(x,y):
    fact=1
    for i in range(1,y+1):
        fact=fact*i
    return x+fact

res=functools.reduce(fact,l1,0)
print(res)
