# -- encoding: utf-8 --
# @time:    	2021/09/2 14:11
# @Author: 		JsonLiu
# @Email:  		492224300@qq.com
# 进程池扫描工具
import socket
import re
import threading
import time

'''
#s1=socket.socket(family,type)
TCP_sock = socket.socket(socket.AF_INET，socket. socK_STREAM)
#family参数：地址家族，可为AF_INET或AF_UNIX
AF_INET家族包括Internet地址，AF_UNIX家族用于同一台机器上的进程间通信。
#type参数:套接字类型，可为SOCK_STREAM(流套接字即TCP套接字)和SOCK_DGRAM(数据报套接字即UDP套接字)。
#默认为family=AF_INET type=SOCK_STREM
#返回一个整数描述符，用这个描述符来标识这个套接字
'''


class CustomThread(threading.Thread):
    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args
        self.name = name

    def run(self):
        self.func(*self.args)


class ScanTool():
    # 1. 检查ip

    def is_ip(self, addr):
        pattern = re.compile(r'^((\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])\.){3}(\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])$')
        # 2. 检查域名
        if pattern.match(addr):
            return True
        else:
            return False

    def is_domain_name(self, addr):
        pattern = re.compile(r'[a-zA-Z0-9][-a-zA-Z0-9]{0,62}(\.[a-zA-Z0-9][-a-zA-Z0-9]{0,62})+\.?')
        if pattern.match(addr):
            return True
        else:
            return False

    # 3. 域名转ip
    def domain_name_to_ip(self, addr):
        try:
            ip = socket.gethostbyname(addr)
            print("该域名{}对应的ip:{} \n".format(addr, ip))
            return ip
        except Exception as e:
            print("获取端口失败信息：{} \n".format(e))
            return None
        # 4. 端口扫描工具

    def scan_tool(self, ip, port, port_list):
        # 4.1建立TCP连接
        try:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.settimeout(0.5)
            conn = client.connect_ex((ip, port))
            # 4.2、查看连接返回
            # print(conn)
            # 4.3、判断连接返回值
            if conn == 0:
                print('{%s:%s}已开放！ \n' % (ip, port))
                port_list.append(port)
            else:
                pass
                # print('端口关闭{IP：%s,端口：%s}' %(ip,port))
        except:
            print('端口扫描异常！\n')
        client.close()

    def threads_scan(self, addr, ports='0,65535', port_list=None):
        # 开始时间
        if port_list is None:
            port_list = []
        star_time = time.time()
        threads_list = []
        start_port, end_port = ports.split(',')
        for port in range(int(start_port), int(end_port) + 1):
            t = CustomThread(st.scan_tool, (addr, port, port_list),name='%s' % port)
            # 把创建的子线程添加到线程列表
            threads_list.append(t)
        # 启动所有线程
        for i in threads_list:
            i.start()
        # 等待所有线程任务执行完毕
        for i in threads_list:
            i.join()
        # 结束时间
        end_time = time.time()
        print("耗时：%s秒" % (end_time - star_time))
        print("开放端口列表：%s" % port_list)
        print(f"开放端口数：%s" % len(port_list))

        f = self.export_data()
        for one in port_list:
            data = f"服务器ip：{addr},端口{one}已开放！\n"
            f.write(data)
        f.write(f"扫描过程耗时：%s秒 \n" % (end_time - star_time))
        f.close()

    def export_data(self):
        # with open("port.txt", "a",encoding='utf-8') as f:
        #     f.write(data + '\n')
        f = open("port.txt", "a", encoding='utf-8')
        return f


if __name__ == '__main__':

    st = ScanTool()
    while True:
        addr = input("请输入扫描ip或域名：")
        ports = input("请输入扫描端口范围(0,65535)：").strip()
        if st.is_ip(addr):
            st.threads_scan(addr, ports)
        elif st.is_domain_name(addr):
            ip = st.domain_name_to_ip(addr)
            if ip:
                st.threads_scan(ip, ports)
        else:
            print("输入地址有误，请重新输入!")
