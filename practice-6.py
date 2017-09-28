i = 2
while i < 100:
    j = 2
    while j <= (i /j ):
        if not(i % j):
            break
        j = j + 1
    if j > i / j: print(i, " 是素数")
    i = i + 1



print("My name is %s and weight is %d kg!" % ('Zara', 21))

str = "lkasjdf"
print(str.capitalize())

print(str.center(2))


dict = {'Name': 'Zara', 'Age': 21, 'Class': 'First'}

dict['Age'] = 28
dict['School'] = 'high School'

print(dict['Age'])
print(dict['School'])

del dict['Age']
dict.clear()
del dict

dictc = {['Name']:'Zara', 'Age': 76}

print(dictc['Age'])