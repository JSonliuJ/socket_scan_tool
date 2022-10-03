# -- encoding: utf-8 --
# @time:    	2021/09/2 14:11
# @Author: 		JsonLiu
# @Email:  		492224300@qq.com
import socket
import re
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


class ScanTool():
    # 1. 检查ip
    def is_ip(self,addr):
        pattern= re.compile(r'^((\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])\.){3}(\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])$')
        # 2. 检查域名
        if pattern.match(addr):
            return True
        else:
            return False
    def is_domain_name(self,addr):
        pattern = re.compile(r'[a-zA-Z0-9][-a-zA-Z0-9]{0,62}(\.[a-zA-Z0-9][-a-zA-Z0-9]{0,62})+\.?')
        if pattern.match(addr):
            return True
        else:
            return False

    # 3. 域名转ip
    def domain_name_to_ip(self,addr):
        try:
            ip = socket.gethostbyname(addr)
            print("该域名{}对应的{}".format(addr,ip))
            return ip
        except Exception as e:
            print("获取端口失败信息：{}".format(e))
            return None
    # 4. 端口扫描工具
    def scan_tool(self, ip,ports):
        # 开始时间
        star_time = int(time.time())
        # 4.1建立TCP连接
        start_port,end_port = ports.split(',')
        for port in range(int(start_port),int(end_port)+1):
            try:
                client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client.settimeout(0.5)
                conn = client.connect_ex((ip,port))
                # 4.2、查看连接返回
                # print(conn)
                # 4.3、判断连接返回值
                if conn == 0:
                    print('端口开启{IP：%s,端口：%s}' %(ip,port))
                else:
                    pass
                    # print('端口关闭{IP：%s,端口：%s}' %(ip,port))
            except:
                    print('端口扫描异常！')
            client.close()
        # 结束时间
        end_time = int(time.time())
        print("耗时：%ss" % (end_time - star_time))
    def export_data(self,addr):
        with open("port.txt","a") as f:
            f.write(addr+'\n')
if __name__ == '__main__':
    from threading import Thread
    st = ScanTool()
    addr = input("请输入扫描ip或域名：")
    port = input("请输入扫描端口范围(格式xxxx,xxxx)：").strip()

    if st.is_ip(addr):
        Thread(target=st.scan_tool(addr,port),name='task1',args=port)

    elif st.is_domain_name(addr):
        ip = st.domain_name_to_ip(addr)
        if ip:
            st.scan_tool(ip,port)
    else:
        print("输入地址有误，请重新输入!")
