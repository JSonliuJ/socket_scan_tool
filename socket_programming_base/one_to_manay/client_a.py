# -- encoding: utf-8 --
# @time:    	2021/09/2 10:26
# @Author: 		JsonLiu
# @Email:  		492224300@qq.com
import socket
# 1. 创建套接字
client_a = socket.socket()
# 2. 连接服务器
addr = ('127.0.0.1',9909)
client_a.connect(addr)
while True:
    # 3. 发送数据
    data_a = input("a客户端请求：")
    client_a.sendall(data_a.encode('utf-8'))
    # 4. 接收数据
    res = client_a.recv(1024).decode('utf-8')
    print("服务器响应：",res)
# 5. 关闭套接字
client_a.close()
