# foe loop-> works for collection 
# while 
#scope -> global, local 
#syntax: 
n=int(input('Enter number: '))
total_digit=0

while n>0:
    total_digit=total_digit+1
    n=n//10
print(total_digit)

#----------armstrong---------------
#------all single digit numbers are armstrong numbers
#---1-1^1=1
#---2-2^1=2
#----153=1^3+5^3+3^3=153

n=int(input('Enter Number: '))
m=p=n
td=sum=0
while n>0:
    td=td+1
    n=n//10
while m>0:
    ld=m%10
    sum=sum+ld**td
    m=m//10
if p==sum:
    print(f'given number {p} is armstrong')
else:
    print(f'given number {p} is not armstrong')
