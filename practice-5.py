for letter in 'Python':
    print('当前字母：', letter)


fruits = ['banana', 'apple', 'mango']
for index in range(len(fruits)):
    print('当前水果：', fruits[index])

print('Good Bye')


for num in range(10, 20):
    for i in range(2, num):
        if num % i == 0:
            j = num / i
            print('%d 等于 %d * %d' % (num, i, j))
            break
    else:
        print(num, '是一个质数')


numList = [9, 1, 5, 2, 3, 8, 6, 7, 4]
for i in range(len(numList)):
    for j in range(i + 1):
        if numList[i] < numList[j]:
            numList[i], numList[j] = numList[j], numList[i]
print(numList)


width = int(input('输出对角线长度:'))

for raw in range(width + 1):
    for col in range(width + 1):
        if ((abs(raw - width / 2) + abs(col - width / 2)) ==  width / 2):
            print("*",)
        else:
            print(" ",)
    print(" ")