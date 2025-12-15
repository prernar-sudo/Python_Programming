# generator -> used to generate collection, but in more controlled way
# yield -> holds its postion 
# return-> terminates
# it is providing more controlled in our system
# x=range(1,100)
# print(list(x))
# print(id(list(x)))

def natural_no(n):
    i=1
    while i<=n:
        yield i
        i=i+1
x=int(input('Enter no.: '))
res=natural_no(x)
print(res)
# for i 0in res:
#     print(i)
# next-> inbuilt function of generator
print(next(res))
print(next(res))
# print('hello')
# print(next(res))

# for _ in range(5):
#     print(next(res))
# print('hello')
# print('hello')
# # for _ in range(8):
# #     print(next(res))#  File "D:\AI_Cybrom\Python_for_ml\day26_generator.py", line 30, in <module>
#                     #     print(next(res))
#                     #           ~~~~^^^^^
#                     # StopIteration
# # error we got bcoz values are not prsent in collection any more
# # we will resolve this error using exception handling
# for _ in range(8):
#     try:
#         print(next(res))
#     except StopIteration:
#         print("all elements are iterated i.e collection is empty")
#         break  #used to terminate the loop, otherwise we get that line again and again

# #--------------------------------------------------------------------------------
# # iterable, iterator
# # when we have already generated collection, we don't apply generator on it, we use iter, to make it behave or use generator property
# # python collection are known as iterable
# # iterable example: list, tuple,string, dict
# l=[1,2,3,4,5]
# print(l)
# # iter()->inbuilt function
# x=iter(l)# it will gnerate iterator object
# print(x)
# for i in x:
#     print(i)
# for i in range(6):
#     try:
#         print(next(x))
#     except StopIteration:
#         print("all elements are iterated i.e collection is empty")
# for i in range(2):
#     print(l[i])
# print('Hello')
# for i in range(2):
#     print(l[i])

