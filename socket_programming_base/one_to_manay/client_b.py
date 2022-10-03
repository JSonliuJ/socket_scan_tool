# -- encoding: utf-8 --
# @time:    	2021/09/2 10:30
# @Author: 		JsonLiu
# @Email:  		492224300@qq.com
import socket
# 1. 创建套接字
client_b = socket.socket()
# 2. 连接服务器
addr = ('127.0.0.1',9909)
client_b.connect(addr)
while True:
    # 3. 发送数据
    data_b = input("b客户端请求：")
    client_b.sendall(data_b.encode('utf-8'))
    # 4. 接收数据
    res = client_b.recv(1024).decode('utf-8')
    print("服务器响应：",res)
# 5. 关闭套接字
client_b.close()