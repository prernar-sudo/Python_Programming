#------------------------------
#------Transfer statement----------
#-----continue--->To skip current iteration
#-----break------>To terminate current loop
#--------pass---->to skip current block

# while loop--->runs how many time (eg n+1)condition check +1 when it is dissatisfied

#----------------infinite times it will run-------------------
# n=10
# i=1

# while i<=n:
#     if i==5:
#         print('Hello')
#         continue
#     else:
#         print(i)
#     i=i+1

#-----------------------------pass-------------
n=10
i=1

while i<=n:
    if i==5:
        pass
    else:
        print(i)
    i=i+1

#-------------------continue-----------
n=10
for i in range(1,n+1):
    if i==5:
        continue
    else:
        print(i)

#------------continue can behave like  pass in while---------
n=10
i=1
while i<=10:
    if i==5:
        i=i+1    #pass
        continue #pass
    else:
        print(i)
    i=i+1

#Practical Implementation ----> generally we don't use continue , mostly we use pass
# in case of if condition, suppose we have to write the condition but don't want to execute use pass

x=10

if x%10==0:    #without pass it could have given syntactical error
    pass

#----------------------break---------------------

n=10
i=1
while i<=n:
    if i==5:
        break
    else:
        print(i)
    i=i+1
print('Hello')


#-------To avoid loop repetition, we have functions 