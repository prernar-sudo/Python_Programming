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

# f=open('n2.txt','x')
# print(f.name) # n2.txt
# print(f.mode) # x
# print(f.readable()) # False
# print(f.writable()) # True
# print(f.encoding) # cp1252
# print(f.closed) # False


f=open('n2.txt','w')
print(f.name) # n2.txt
print(f.mode) # w
print(f.readable()) # False
print(f.writable()) # True
print(f.encoding) # cp1252
print(f.closed) # False

f=open('n2.txt','r')
print(f.name) # n2.txt
print(f.mode) # r
print(f.readable()) # True
print(f.writable()) # False
print(f.encoding) # cp1252
print(f.closed) # False

f=open('n2.txt','a')
print(f.name) # n2.txt
print(f.mode) # a
print(f.readable()) # False
print(f.writable()) # True
print(f.encoding) # cp1252
print(f.closed) # False
