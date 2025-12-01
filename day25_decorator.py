# Decorator
# reprsented by @
# It is a special type of higher order function
# It will take function an argument and return function


def decore(fun_name):
    def inner():
        print('Hello')

    return inner

x=decore(10)
print(x)
#------------------------------
def decore(fun):
    def inner():
        fun()#->add()# indirectly calling add
    return inner
def add():
    print('hello')
res=decore(add)
print(res)
res()
#---------------------------------internal working---------------------------------
def decore(fun):
    def inner(p,q):
        p=p+5 #bluff game
        q=q*2 #bluff game
        fun(p,q)
    return inner
def add(x,y):
    print(x+y)
res=decore(add) # calling inner
res(10,20)#55
#---------------------------------decorator-----------------------------------
def decore(fun):#---->in this add is passing as a parameter
    def inner(p,q):
        p=p+5 #bluff game
        q=q*2 #bluff game
        fun(p,q)
    return inner
@decore#position will always be above that function whose, internal behaviour we want to modifiy
def add(x,y):
    print(x+y)
add(10,20)#55--->modified value is called
#----------------------
def first(fun):
    def inner():
        print('welcome')
    return inner
@first
def great():
    print('hello')
great()
#----------------------
def decore(fun):
    def inner(x):
        #fun(x)
        for i in range(1,x+1):
            print(2*i-1)
    return inner
@decore
def even(n):
    for i in range(1,n+1):
        print(2*i)
n=int(input('Enter number: '))
even(n)
# H.W ques
# add ki jagah sub
# mul ki jagah divide
#-------------------------
def decore(fun):
    def inner(x,y):

        return(x-y)
    return inner

@decore
def add(p,q):
    return(p+q)
a,b=int(input('Enter first number: ')),int(input('Enter Second number: '))
print(add(a,b))
#-------------------------
def decore(fun):
    def inner(x,y):

        return(x//y)
    return inner

@decore
def mul(p,q):
    return(p*q)
a,b=int(input('Enter first number: ')),int(input('Enter Second number: '))
print(mul(a,b))

