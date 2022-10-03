# -- encoding: utf-8 --
# @time:    	2022/09/2 09:23
# @Author: 		JsonLiu
# @Email:  		492224300@qq.com
import socket
while True:
    # 1. 创建套接字
    host = ('127.0.0.1', 8899)
    socket_client = socket.socket()
    # 2. 连接服务端口
    socket_client.connect(host)
    # 3. 发送数据
    client_data = input("请输入发送数据：")
    socket_client.send(client_data.encode('utf-8'))
    # 4. 接收数据
    res = socket_client.recv(1024).decode('utf-8')
    print("服务端响应数据：%s" % res)
# 5. 关闭套接字
socket_client.close()
