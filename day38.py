# cursor movement

# tell()->to check cursor current position
# seek()->to move our cursor to required position

# f=open('n11.txt','x+')
# print(f.tell())#0th index

# f=open('n11.txt','w+')
# print(f.tell())# 0

# f=open('n11.txt','r+')
# print(f.tell())#0

# f=open('n11.txt','a+')
# print(f.tell())#0

#------------------------------------ write some content in the file---------------------------
# f=open('n11.txt','w+')
# print(f.tell())# 0 (when hello is written) (it will erase data)

# f=open('n11.txt','r+')
# print(f.tell())#0 (when hello is written) (it will not erase data)
# data=f.read(10)
# print(data)
# print(f.tell())


# f=open('n11.txt','a+')
# print(f.tell())#5 (when hello is written)

#---------------------------seek()-----------------------------
'''
    syntax:
        seek('how many bits are move','from where')

        from where-> 0->starting-position
            where->1->current-position # for binary mode
            where->2->last-position    # for binary mode

            # 1 and 2 will work on binary mode, means when we write b in mode like rb+, wb+, ab+, xa+

'''
# binary data -> audio , video data
# pickle module

# f=open('n6.txt','rb+')
# print(f.tell())# 0

# data=f.read(10)
# print(data)#b'this is py'
# print(f.tell())#10
# f.seek(-5,1)
# print(f.tell())
# print(f.read(10))
# print(f.tell())

#------------------------------
f=open('n6.txt','rb+')
data=f.read(25)
print(data)
f.seek(20)
print(f.tell())
f.seek(-1,2)
print(f.tell())#1199
f.seek(-5,2)
data=f.read()
print(data)

