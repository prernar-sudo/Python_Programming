#data type
#numeric->integer , float, complex
#ordered->string,list,tuple
#mapped->dict
#unordered->set,frozenset
#boolean
#none
#----------------------Fundamental data types-----------------------------------
#integer, float,complex
#string
#list
#tuple
#dict

#integer is immutable, crud operation can not be applied
x=10
print(x)
print(type(x))
print(id(x))
#---------this method will not apply on integer--------------------
# print(max(x))
# print(min(x))
# print(len(x))
#-----------all operators will apply on integer-------------------
#---------------string-------------
#collection of characters
#represented by '/'''/"
#indexing supported
#slicing supported
#duplicates are allowed
#immutable in nature-> find id of two element, address will occur same
s='python programming'
print(s,type(s))
#string supports all methods, max, min,len, sum
#string supports python inbuilt functions: print,type,id,len,max,min,sum,input
print(s)
print(type(s))
print(id(s))
print(len(s))
print(max(s))
print(min(s))
#print(sum(s))#unsupported operand--------this is only in -built function which is not supported by the string 
#magic_method or dinder method __ starts with double underscore and ends with double score, this we can seec eg type s. drop down menu or 
#suggestion box will appear
#methods----------of string
#swapcase(),lower(),upper(), capitalize(),title(),index(),count(),split(),join(),find(),count(),replace()
#s.
print(s.swapcase())
print(s)#reason->string nature is immutable->bcoz object is different, addressis changed
print(s.upper())
print(s.lower())
print(s.capitalize())
print(s.title())
print(s.index('y'))
#print(s.index('Y'))#SUBSTRING NOT FOUND
#index tells the position of any element
print(s.find('y'))#1
print(s.find('Y'))#-1->means substring not found , to avoid error, we used find
print(s.count('p'))#count->itcounts the frequency of any element-> how many time it get's repeated
#tomorrow->we discuss split,join,replace

#syntax of join: 'separator'.join(iterator/collection)
s1='python'
s2='java'
s3='php'
 
s4=' '.join([s1,s2,s3])#we are giving list , bcoz join takes only one argument
print(s4)

l=[s1,s2,s3]
print(l)

# a1='python'
# a2=10
# print(''.join['python',10])

#syntax of split -> string.split(),string.split('separator'),string.split('separator','How many times')
s='This is python class'
l=s.split()#by default it will split by space, how many times->till the time we have space
print(l)

l=s.split('s')
print(l)

l=s.split('s',2)
print(l)
#why it is only spliint in list , there is a reason -> bcoz tuple is immutable, set and frozenset

#replace

r='this is python'
print(r.replace('i','z'))
print(r.replace('i','z',1))
print(r.replace('this','x'))

#_isdigit
x='10'
print(x.isdigit())#it will be useful in loops

#operators in string
x1,x2='python','java'
print(x1+x2)# + -> referred as concatenation
#print(x1-x2)# - -> will give error
print(x1*5)
print(x1+x2,sep=',')#it will be s singl element so separator will not work
print('a'>'A')#true
print('Python'>'java')
print('Python'>'Pava')#true, first letter is same , so it will check second char, andif that is also same then third , then proceed

#-----------------------------------------logical and

_x='python'
_y='java'
print(_x and _y)#last true value is java, so it will come
print(_y and _x)
_z=''
print(_x and _z)
x=''
print(bool(''))#False
x='a'
print(bool(x))
s1,s2='python',''
print(s1 and s2)
s1,s2='',''
print(s1 and s2)#interview ques=> which false value is appearing, ans->first false value

#-------------------------logical or
#---last false
#----first true
s1,s2='',''
print(s1 or s2)
s1,s2='python',''
print(s1 or s2)
s1,s2,s3='','python','java'
print(s1 or s2 or s3)
s1,s2='python','java'
print(s1 or s2)

#--------------------------logical not
s1=''
print(not(bool(s1)))

#which boolean value in string return false->empty string
#which boolean value in integer return false->zero

#------------------------------membership (in, not in)
s='aeiouAEIOU'
s1='p'
print(s1 in s)
s2='a'
print()
s3='ae'
print(s3 in s)
s4='ea'
print(s4 in s)#false ->bcoz order matter, string is a ordered collection

#-------------------------------identity (is, is not)--compareon the basis of memory address, but (==) based on value it compares
s1='python'
s2='java'
print(s1 is s2)
print(s1 == s2)

#------------------------------------bitwise 
#------it is not applicable in string
#------but indirecly we can do, but that way is quiet unuseful, 



