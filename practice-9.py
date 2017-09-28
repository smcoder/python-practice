
# -*- coding: UTF-8 -*-
import os

# 打开一个文件
fo = open("foo.txt", "r+")
str = fo.read(0)
print("读取的字符串是：", str)

# 查找当前位置
position = fo.tell()
print("当前位置：", position)


# 把指针再次移动到开头
position = fo.seek(0, 0)
str = fo.read(10)
print("重新读取的内容：", str)
# 关闭打开的文件
fo.close()


# os.rename('test1.txt', "test2.txt")


print("当前目录", os.getcwd())



try:
    fh = open("testfile.txt", "w")
    fh.write("这是一个测试文件, 用于测试异常")
except IOError:
    print("Error: 没有找到文件或读取文件失败")
else:
    print("写入文件成功")
    fh.close()


def temp_covert(var):
    try:
        return int(var)
    except ValueError:
        print("参数没有包含名字")
