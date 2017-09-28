def printme(str):
    "打印传入的字符串到标准的显示设备商"
    print(str)
    return


printme("这是测试数据")


def ChangeInt(a):
    a = 10


b = 2
ChangeInt(b)
print(b)


def changeme(mylist):
    mylist.append([1, 2, 3, 4])

    print(mylist)
    return

mylist=[9, 8, 7]
changeme(mylist)
print(mylist)

def printme(str):
    "打印任务传入的字符串"
    print(str)
    return



fo = open('foo.txt', 'wb')
print("文件名是:", fo.name)
print("是否已关闭", fo.closed)
print("访问模式", fo.mode)
