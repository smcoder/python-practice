import re

print(re.match('www', 'www.runoob.com').span())  # 在起始位置匹配
print(re.match('com', 'www.runoob.com'))  # 不在起始位置匹配

line = "Cats are smarter than dogs"

matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)

if matchObj:
    print("matchObj.group():", matchObj.group())
    print("matchObj.group(1):", matchObj.group(1))
    print("matchObj.group(2):", matchObj.group(2))
else:
    print("No Match")


print(re.search('www', 'www.runoob.com').span()) # 在起始位置匹配
print(re.search('com', 'www.runoob.com')) # 不在起始位置匹配


phone = "2004-959-559 # 这是一个国外电话"

# 删除字符串中的 Python 注释
num = re.sub(r'#.*$', "", phone)
print("电话号码是:", num)

# 删除非数字(-)的字符串
num = re.sub(r'\D', "", phone)
print("电话号码是:", num)


# 将匹配的数字✖2
def double(matched):
    value = int(matched.group('value'))
    return str(value * 2)
s = 'A23G4HFD567'
print(re.sub('(?P<value>\d+)', double, s))