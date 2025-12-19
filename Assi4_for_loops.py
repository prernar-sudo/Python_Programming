# # FOR_LOOP Examples


# Example 1: Write a program to
# display n natural numbers. (In Horizontal-1,2,3,4,5…….. )
n=int(input("Enter number: "))
for i in range(1,n+1):
    print(i,end=' ')

print()

# Example 2: Write a program to
# calculate the sum of n natural  numbers.(1+2+3+4+5+6=sum)
n=int(input('Enter Number: '))
sum=0
for i in range(1,n+1):
   sum=sum+i
   if i<n:
     print(i,end='+')
   else:
      print(i,end='=')
   
print(sum)

# Example 3: Write a program to
# print n even natural number. (2,4,6,8,….)
n=int(input("Enter the number: "))
for i in range(2,2*n+1,2):
    if i<2*n:
        print(i,end=',')
    else:
       print(i)
        



# Example 4: Write a program to
# calculate the sum of n even natural 
# numbers. (2+4+6+8+10=sum if n=5)
n=int(input("Enter Number: "))
total=0
for i in range(2,2*n+1,2):
   total+=i
   if i<2*n:
      print(i,end='+')
   else:
      print(i,end='=')
print(total)



# Example 5: Write a program to calculate the sum of even numbers up to n natural number. (2+4+6+8+10=sum if n=10)
n=int(input('Enter number: '))
total=0
for i in range(2,n+1,2):
   total+=i
   if i+2<=n:
      print(i,end='+')
   else:
      print(i,end='')
print('=',total)
    



# Example 6: Write a program to
# print n natural odd numbers. (1,3,5,7,9…..)
n=int(input("Enter number: "))
for i in range(1,2*n,2):
   if i+2<2*n:
        print(i,end=',')
   else:
      print(i)
   


# Example 7: Write a program to
# calculate the sum of n od natural 
# number. (1+3+5+7+9=sum if n 5)
n=int(input("Enter number: "))




# Example 8: Write a program to
# calculate the sum of even numbers up to n natural number. (1+3+5+7+9=sum if
# n=10)

# n=int(input('Enter number: '))
# sum=0
# for i in range (1,n+1):
#     if i%2 == 0:
#         print(i,end='+')
#         sum=sum+i
# print(sum)        

    
