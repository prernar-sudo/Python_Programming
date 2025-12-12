# Polymorphism -->  many forms
# compile time polymorphism -> do not exist in python 
# run time polymorphism
# functional polymorphism -> one function has more than one forms for different data type is functional polymorphism
s='python'
print(len(s))
s=['python']
print(len(s))
# operator polymorphism -> same opertor but different output / forms
x=10
y=20
z=x+y
print(z)
x='10'
y='20'
z=x+y
print(z)

#----------------------------------------------
#method polymorphism
class human:
   def sound(self):
      print('sound from human')

class animal:
   def sound(self):
      print('sound from animal')

#list=[human, animal] # paranthesis not given means object is not created
list=[human(),animal()]

for i in list:
   #i.sound(1)
   i.sound()
  
# method overload
   