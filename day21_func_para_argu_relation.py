# # # Relation between argument and parameter

# # # 1. Positional Argument
# # # 2. Default positional argument
# # # 3. Variable length positional argument (*args)
# # # 4. Keyword argument 
# # # 5. Default keyword argument
# # # 6. variable length keyword argument (**kwargs)

# # # ------------------------1. positional argument-----------------

# # def add(x,y,z):
# #     return x+y+z

# # p,q,r=10,20,30

# # res =add(p,q,r)
# # res = add(int(input('Enter number: ')),int(input('Enter number: ')),int(input('Enter number: ')))
# # print(res)

# # # res = add()       # add() missing 3 required positional arguments: 'x', 'y', and 'z
# # # res1 = add(p)     # TypeError: add() missing 2 required positional arguments: 'y' and 'z'
# # # res2 = add(p,q)     # TypeError: add() missing 1 required positional argument: 'z'
# # # res3 = add(p,q,r,5)  #TypeError: add() takes 3 positional arguments but 4 were given

# # # ------------------------2. Default positional argument-----------------

# # def add(x=0, y=0, z=0):
# #     return x+y+z

# # res = add()
# # print(res)

# # res1 = add(10)
# # print(res1)

# # res2 = add(10,20)
# # print(res2)

# # res3 =add(10,20,30)
# # print(res3)

# # # --- disadvantage : it total no.of arg is greater than total no. of parameter , we'll get error
# # # res4 = add(1,2,3,4)   # TypeError: add() takes from 0 to 3 positional arguments but 4 were given
# # # print(res4)

# # #-------------------------------3. Variable length positional argument---------------------------------------

# # # args is a variable , we can make itof any name like *n, but recommended to use args

# # def add(*args):
# #     print(args)  #      
# #     print(type(args))  # tuple

# # add(1,2,3,4,5,6,7,8,9)

# # #-----------------------------------
# # def add(*n):
# #     sum=0
# #     for i in n:
# #         sum=sum+i
# #     return sum
# # x=add(1,2,3,4,5)
# # print(x)

# # #-----------------------------------
# # def add(*n):
# #     print(n)
# #     print(type(n))

# # x=add(eval(input("Enter no.: ")))
# # print(x)
# # # (5,)
# # # <class 'tuple'>
# # # None

# # #-----------------------------------
# # # def add(*n):
# # #     print(n)
# # #     print(type(n))
# # #     sum=0
# # #     for i in n:  # this loop will give (5, 6, 7, 8) in i
# # #         for j in i: # now j is 5, 
# # #             sum=sum+j
# # #     # print(sum)
# # #     return sum

# # # x=add(eval(input("Enter no.: ")))
# # # print(x)

# # # ((5, 6, 7, 8),)
# # # <class 'tuple'>
# # # 26
# # # None

# # # #-----------------------------------
# # # def add(*n):
# # #     print(n)
# # #     print(type(n))

# # # x=add(*eval(input("Enter no.: ")))
# # # print(x)
# # # # (5, 6, 7)
# # # # <class 'tuple'>
# # # # None

# #---------------------------------4. Keyword argument------------------------------------
# # parameters are treated as keyword
# def fun_name(x,y,z):  #x,y,z as a keyword
#     print(x)
#     print(y)
#     print(z)

# p=10
# q=20
# r=30

# fun_name(z=p,y=r,x=q)

# #--------------------------------5. Default keyword argument----------------------------------
# def fun_name(x=0,y=0,z=0):  #x,y,z as a keyword
#     print(x)
#     print(y)
#     print(z)

# p=10
# q=20
# r=30

# fun_name()
# fun_name(z=p)
# fun_name(z=p,y=r,x=q)

# #-----------------------------------6. variable length keyword argument (**kwargs)-------------------------------------------
# def func_name(**kwargs):  # * -> all ,**-> key and value both is
#     print(kwargs)     #{'x': 10, 'y': 20, 'z': 30, 'p': 2, 'q': 5}
#     print(type(kwargs))# <class 'dict'>

# func_name(x=10,y=20,z=30,p='2',q=5)

# #-------------------------------------
# def func_name(**kwargs):  # ** -> here packing
#     print(kwargs) 
# func_name(**eval(input("Enter and dict: "))) #** -> here unpacking

# input-> {'x':10,'y':20}
#-------------------------------------

# def func_name(**kwargs):
#     for i in kwargs.keys():
#         print(i)

#     for i in kwargs.values():
#         print(i)

#     for i, j in kwargs.items():
#         print("keys= ",i,"values= ",j)

# func_name(**eval(input("Enter and dict: ")))

#---------------------------------------------

# first make positional argument then keyword argument
# otherwise we get error
# def fun_name(x,p,*z,y=0,**q):
#     print(x)
#     print(y)
#     print(z)
#     print(p)
#     print(q)

# fun_name(10,p=20,30,40,50,9,r=1,s=2,t=3)

def fun_name(x,y=0,*z,p,**q):
    print(x)
    print(y)
    print(z)
    print(p)
    print(q)

fun_name(10,20,30,40,50,p=9,r=1,s=2,t=3)

#-------------------------------------

def natural(n):
    for i in range(1,n+1):
        print(i)

n=int(input('Enter no.: '))
natural(n)

#-------------------------------------

def sum_natural(n):
    sum=0
    for i in range(1,n+1):
        sum=i+sum
    return sum

n=int(input('Enter no.: '))
print(sum_natural(n))

#--------------------------------------

def even_num(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count=count+1
        if count>2:
            return 'not prime'
    return 'prime'
            

n=int(input('Enter no.: '))
print(even_num(n))

#--------------------------------------


