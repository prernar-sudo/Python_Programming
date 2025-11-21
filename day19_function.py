# Function ------- write onces used multiple times
# To achieve code reusability
# 1. In-built
# 2. User defined

# Syntax of function

# without name function is anonomys func

# # function defination
# def func_name(parameter):
#     fun_body # mandatory , don't wan't to execute give pass 
#     return

# # function calling
# func_name(argument)

#--------parameter, arguments, return are optional , rest all mandatory

#without parameter, without argument
def xyz():
    print('hello')

xyz()

#without parameter, without argument
def xyz():
    # print('hello')
    pass

xyz()

#--------------- parameter and argument need not to be same bcoz there purpose is different---------------

def add(x,y):
    print(x+y)

p=10
q=4
add(p,q)
add(int(input('Enter First value: ')),int(input('Enter second value: ')))
print('Hello2')

#--------------- by default function return none , if we are not returning anything

def add(x,y):
    print(x+y)
    return None
p=10
q=20
res=add(p,q)
print(res)
print(res)
print(res)

#------------
def add(x,y):
    print(x+y)
    #return None
p=10
q=20
res=add(p,q)
print(res)
print(res)
print(res)

#------------
def add(x,y):
    z=x+y
    return z
p=10
q=20
res=add(p,q)
print('nothing is printed')
#------------
def add(x,y):
    z=x+y
    return z
p=10
q=20
res=add(p,q)
print(res)
print(res)
print(res)

#-------------------disadvantage of not using return keyword------
# print(print('Hello')) # we got , hello, None

#-------------------

def add(x,y):
    print(x+y)

p=10
q=20

#add(p,q)
print(add(p,q))

#-----------------
def add(x,y):
    return x+y

p=10
q=20

print(add(p,q))


#--------------------------user-defined function--------------------------
#------recommendation ----always use with return
#------otherwise function will always return none and when we print function, it will aways give none
# 1. with argument (1.with return, 2.without return) #parameter needed
# 2. without argument (1. with return, 2.without return ) #parameter not needed

