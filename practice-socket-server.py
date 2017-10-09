import socket # 导入socket 模块

s = socket.socket()  # 创建socket对象
host = socket.gethostname() # 获取本地主机名
port = 4567 # 设置端口
s.bind((host, port)) # 绑定端口


s.listen() # 等待客户端连接
while True:
    c, addr = s.accept() # 建立客户端连接
    print("连接地址", addr)
    c.send('www.baidu.com')
    c.close() # 关闭连接