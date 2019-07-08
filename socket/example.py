# -*- coding:utf-8 -*-
import socket

# socket 连接方式
# socket.AF_UNIX        本地进程通信用
# socket.AF_INET        IPV4网络通信
# socket.AF_INET6       IPV6网络通信

# socket 数据流
# socket.SOCK_STREAM    TCP流式 scoket通信
# socket.SOCK_DGRAM     UDP数据报式 socket通信
# socket.SOCK_RAW       原始套接字，可以处理ICMP,IGMP网络报文
# socket.SOCK_SEQPACKET 可靠的连续数据包服务

# 创建socket实例
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 创建客户端连接
host = 'www.baidu.com'
remote_ip = socket.gethostbyname(host)
port = 80
s.connect((remote_ip,port))
# 发送套接字
message = "GET / HTTP/1.1\r\n\r\n".encode('utf-8')
s.sendall(message)
# 接收信息
r = s.recv(4096)
print(r)
# 关闭socket
s.close()
