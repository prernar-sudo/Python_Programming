#---------------------------------------

# write----> write(), writelines()

f1=open('n8.txt','a+')
data='this is python class'
f1.write(data)
f1.close()

f1=open('n6.txt','a+')
data='this is python class\n'
f1.write(data)
f1.close()

#------------------to add multiple lines of data---------------------------
f1=open('n6.txt','a+')
data=['python\n','java\n','php\n']
f1.writelines(data)

#---------------------read------------
'''
    read
        read()->read all data
        read(n)->n-bits of data
        readline()->read single-line of data
        readlines()->read all lines of data
'''
#f=open('n6.txt')# no mode given -> so by default it's read mode
f=open('n6.txt','r+')
# data=f.read()
# print(data)
#data=f.read(10)# cursor position 0th-9th
#data=f.read()
#print(data)# cursor position is 9th
# data=f.read(5)#cursor position is 10th
# print('last:',data)
# data=f.readline()
# print(data)
data=f.readlines()
print(data)
#f.close()

# cursor movement