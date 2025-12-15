# file handling -> to store useful information permanently
# to perform crud operation we need to handle the file

# file handling
# 1. create()/open()
# 2. write()/read()
# 3. close()

# -----------------------------1.open
'''
    syntax: 
        open('filename with extension' , mode )

        mode -> create-> x, write-> w, read-> r, append-> a

'''
#f=open('n1.txt','x')
# on existing file x mode will not work 
# FileExistsError: [Errno 17] File exists: 'n1.txt'

f=open('n3.txt','w')
#print(f.read())
print(f.name) # n2.txt
print(f.mode) # x
print(f.readable()) # False
print(f.writable()) # True
print(f.encoding) # cp1252
print(f.closed) # False


# f=open('n2.txt','w')
# print(f.name) # n2.txt
# print(f.mode) # w
# print(f.readable()) # False
# print(f.writable()) # True
# print(f.encoding) # cp1252
# print(f.closed) # False

# f=open('n2.txt','r')
# print(f.name) # n2.txt
# print(f.mode) # r
# print(f.readable()) # True
# print(f.writable()) # False
# print(f.encoding) # cp1252
# print(f.closed) # False

# f=open('n2.txt','a')
# print(f.name) # n2.txt
# print(f.mode) # a
# print(f.readable()) # False
# print(f.writable()) # True
# print(f.encoding) # cp1252
# # print(f.closed) # False

# #-----------------------------------------
# # f=open('n5.txt','w')
# # print(f.name) # n2.txt
# # print(f.mode) # w
# # print(f.readable()) # False
# # print(f.writable()) # True
# # print(f.encoding) # cp1252
# # print(f.closed) # False

# #f=open('n5.txt','w') # in w mode, if we open it will erase existing content , cursor position will become zero

# f=open('n5.txt','a') # in a mode, cursor position previous last

# # in x+, w+, r+, a+ --> in this case we can do readable and writeable both, are true

# f=open('n5.txt','w+')
# print(f.readable())
# print(f.writable())
# f=open('n5.txt','a+')
# print(f.readable())
# print(f.writable())
# f=open('n5.txt','r+')
# print(f.readable())
# print(f.writable())
# #f=open('n5.txt','x+')
# print(f.readable())
# print(f.writable())

# #---------------------------------------

# write----> write(), writelines()

# f1=open('n6.txt','a+')
# data='this is python class'
# f1.write(data)
# f1.close()