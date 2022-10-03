# -- encoding: utf-8 --
# @time:    	2021/09/2 09:10
# @Author: 		JsonLiu
# @Email:  		492224300@qq.com
import socket

# 1. 创建socket套接字
socket_server = socket.socket()
# 2. 绑定id、端口
host = ('127.0.0.1', 8899)
socket_server.bind(host)
while True:
    # 3. 开启监听(端口）
    socket_server.listen(128)
    # 4. 阻塞：等待客户端连接
    conn, addr = socket_server.accept()
    print(conn, '\n', addr)
    # 5. 接收数据
    response = conn.recv(1024).decode('utf-8')
    print("客户端请求：", response)
    # 6. 发送数据
    data = input("服务端响应数据：")
    conn.send(data.encode('utf-8'))
# 7. 关闭套接字
socket_server.close()
