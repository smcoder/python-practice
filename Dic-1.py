dict = {}
dict['one'] = "this is one"
dict[2] = "this is two"

tinydict = {'name': 'john', 'code' : 6374, 'dept': ' sales'}

print(dict)
print(dict[2])
print(tinydict)
print(tinydict.keys())
print(tinydict.values())

a = 21
b = 10
c = 0
c = a + b

if (a == b):
    print("1 - a 等于 b")
else:
    print("1 - a 不等于 b")

if (a != b):
    print("2 - a 不等于 b")
else:
    print("2 - a 等于 b")

if (a < b):
    print("3 - a 小于 b")
else:
    print("3 - a 大于 b")

if (a > b):
    print("4 - a 大于 b")
else:
    print("4 - a 小于 b")



print("1 - c 的值为：", c)

c = a - b
print("2 - c 的值为", c)

c = a * b
print("3 - c 的值为", c)

c = a / b
print("4 - c 的值为", c)

c = a % b
print("5 - c 的值为", c)

a = 2
b = 3
c = a**b

print("6 - c 的值为", c)

a = 10
b = 5
c = a//b
print("7 - c 的值为", c)

print(1/2)


a = 60
b = 13

print("-----------------")

print(a&b)
print(a|b)
print(a^b)
print(~a)


a = 10
b = 20

if (a and b):
    print("1 - 变量 a 和 b 都为true")
else:
    print("1 - 变量 a 和 b 有一个不为true")

if (a or b):
    print("2 - 变量 a 和 b 都为 true， 或其中一个不为 true")
else:
    print("2 - 变量 a 和 b 都不为true")

a = 0
if (a and b):
    print("3 - 变量 a 和 b 都为true")
else:
    print("3 - 变量 a 和 b 有一个不为true")

if (a or b):
    print("4 - 变量 a 和 b 都为true， 或其中有一个不为true")
else:
    print("4 - 变量 a 和 b 都不为true")

if not(a and b):
    print("5 - 变量 a 和 b 都为 false， 或其中一个变量为false")
else:
    print("5 - 变量 a 和 b 都为true")


a = 10
b = 20
list = [1, 2, 3, 4, 5];

if (a in list):
    print("1 - 变量 a 在给定的类表中 list 中")
else:
    print("1 - 变量 a 不在给定的类中 list 中")

if (b not in list):
    print("2 - 变量 b 不在给定列表中 list 中")
else:
    print("2 - 变量 b 在给定列表中 list 中")

a = 1
c = (1, 2, 3, 4)
if (a in c):
    print("1 - 变量 a 在给定的元组中 tuple 中")
else:
    print("1 - 变量 a 不在给定元组中 tuple 中")

a = 20
b = 20

if (a is b):
    print("1 - a 和 b 引用相同的对象")
else:
    print("1 - a 和 b 引用自不同的对象")

if (a is not b):
    print("2 - a 和 b 引用自不同的对象")
else:
    print("2 - a 和 b 引用自相同的对象")


a = 20
b = 10
c = 15
d = 5
e = 0

e = (a + b) * c / d
print(e)

e = ((a + b) * c) / d
print(e)

e = (a + b) * (c / d)
print(e)

e = a + (b * c) / d
print(e)

numbers = [12, 37, 5, 42, 8, 3]
even = []
odd = []
while len(numbers) > 0:
    number = numbers.pop()
    if (number % 2 == 0):
        even.append(number)
    else:
        odd.append(number)

print(even)
print(odd)

i = 1
while i < 10:
    i += 1
    if i % 2 > 0:
        continue
    print(i)

i = 1
while 1:
    print(i)
    i += 1
    if i > 10:
        break

count = 0
while count < 5:
    print(count, " is less than 5")
    count = count + 1
else:
    print(count, " is not less than 5")

flag = 1
while (flag): print("flag is true")