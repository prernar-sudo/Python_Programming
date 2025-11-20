import string

spe_symbol = string.punctuation
print(spe_symbol)
print(len(spe_symbol))

ascii_lc=string.ascii_lowercase
print(ascii_lc)
print(len(ascii_lc))

#----------------------------------Naming Rules------------------------------
#1x=10
x=5
X=100
_=6
print(x,_,X)

#if=10 #will give error, keyword can not be used as name

#softkeyword can be used as variable name 
_=10
match=20
case=30
type=40
print(_,match,case, type)

#case sensitive
a=10
#print(A)
x_y=10
print(x_y)