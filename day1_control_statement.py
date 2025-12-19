#CONTROL STATEMENT
# x=int(input("Enter any value: "))
# y=int(input("Enter any value: "))
# if x>10:
#  print("Greater than")
# print("nxt statement")

# if x>=0:
#     if y>=0:
#         print(x+y)
# print("Thanks for visit")

#----------------------if and if else difference-------------------- 
# In if->the block may be executed 
# In if else ->block will be executed

n=int(input("Enter any number: "))
# if n%2==0:
#     print(f'given number {n} is even') #f-string -> this will take less memory
    
# else:
#     print(f'given number {n} is odd')

if n>0:
    print(f'given number {n} is positive')
elif n<0:
    print("negative")
else:
    print("zero")