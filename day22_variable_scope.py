# # variable scope
# # 1. local
# # 2. Global
# # 3. nonlocal

# # 1. local -> (access within the block)

# def display():
#     x=10   #Local variable
#     print(x)

# display()
# # print(x) #NameError: name 'x' is not defined

# #---------------------to make local variable convert toglobal variable-----------------------------------

# def display():
#     global x  # to convert local variable into global we use 
#     x=10   #Local variable
#     print(x)

# display()
# print(x) #NameError: name 'x' is not defined

# #-------------------------------------
# # case 3

# def display_case3():
#     global y
#     y=10
#     print(y)

# # print(y) # error
# display_case3()
# print(y)

# #-----------------------------------global scope----------------------------

# z=10

# def show():
#     print(z)
# print(z)
# show()
# print(z)

#-------------------------------------------------

# x=10

# def show():
#     x=20
#     print(x)
# print(x)  #10
# show()    #20
# print(x)  #10

#--------------------------------------------------

# x=10
# def show():
#     print(x)  # UnboundLocalError: cannot access local variable 'x' where it is not associated with a value
#     x=20
#     print(x)

# show()

#--------------------------------------------------
# case4: if we want to access global variable in local scope
# x=10
# def show():
#     print(x)
#     x=20
#     print(globals()['x'])

# show()

# disadv of python -> we are able to access everything at every place
# leads to security threat

#------------------------------------------------------
# def show():
#     x=10
#     def display():
#         print(x)
#     display()
# show()

#------------------------------------------------------
# def show():
#     x=10
#     def display():
#         x=x+5 # UnboundLocalError: cannot access local variable 'x' where it is not associated with a value
#         print(x)
#     display()
# show()

#------------------------------------------------------
# def show():
#     x=10
#     def display():
#         nonlocal x  # it is internal scope , neither local nor global
#         x=x+5 # it will pick value from local , gives priority to local 
#         print(x)
#     display()
# show()
# print(x) -->NameError: name 'x' is not defined
# x=10
# def display():
#         nonlocal x  # it is internal scope , neither local nor global
                      # write inside ftwo function
#         x=x+5
#         print(x)
# display()

#----------------------------------------------------------

while (True):
    print('1. Add\n2.Sub\n3.Div\n4.Mul\n5.Exit')
    n=int(input('Please enter your choice: '))
    if n in (1,2,3,4,5):
        # pass
        if n in (1,2,3,4):
            # pass
            if n==1:
                numbers=int(input('How many numbers you want to add: '))
                l=[]
                for i in range(1,numbers+1):
                    value=int(input(f'enter {i} number '))
                    l.append(value)
                sum=0
                for i in l:
                    sum=sum+i
                print(f'addition of {l} is {sum}')
        else:
            break # loop will terminate, calculator will off
    else:
        print('Please enter valid choice')