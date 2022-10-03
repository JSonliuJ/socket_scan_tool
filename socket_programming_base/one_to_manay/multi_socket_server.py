# -- encoding: utf-8 --
# @time:    	2021/09/2 10:35
# @Author: 		JsonLiu
# @Email:  		492224300@qq.com
import socketserver
class SocketServer(socketserver.BaseRequestHandler):
    # 名字必须固定用hendle，否则会报错
    def handle(self):
        #处理逻辑
        while True:
            # 接收数据
            req = self.request.recv(1024).decode('utf-8')  # 解码
            print('客户端请求：', req)
            #发送数据
            res = input("服务端响应：")
            self.request.sendall(res.encode('utf-8'))  # 编号
        self.request.close()

#2- 创建服务端
server = socketserver.ThreadingTCPServer(('127.0.0.1',9910),SocketServer)
#3- 一直运行
server.serve_forever()
