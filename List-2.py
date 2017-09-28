list = ['runoob', 786, 2.23, 'john', 70.2, [123, 321]]

tinylist= [123, 'john']

print(list)
print(list[0])
list[0] = 'Hello'
print(list[0])
print(list[1:3])
print(list[2:])
print(tinylist * 2)
print(list + tinylist)

print('------------------------')
tuple = ('runoob', 786, 2.23, 'john', 70.2, [123, 321])
tinytuple = (123, 'john')

print(tuple)
print(tuple[0])
print(tuple[1:3])
print(tuple[2:])
print(tinytuple * 2)
print(tuple + tinytuple)