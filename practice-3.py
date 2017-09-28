denum = input('输入十进制数:')

print(denum, '(10)')

binnum = []
num = int(denum)
while num > 0:
    binnum.append(str(num % 2))
    num //= 2
print('= ')

while len(binnum) > 0:
    import sys
    sys.stdout.write(binnum.pop())