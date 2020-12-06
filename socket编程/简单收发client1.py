# -*- coding: utf-8 -*-
"""
author: LHQ
by keyboy
"""
'''
支持并发聊天的client
'''
import socket

# 创建socket对象
sk = socket.socket()
# 指定ip 端口
ip_port = ('127.0.0.1', 8000)

# 连接服务
sk.connect(ip_port)
print('客户端启动')
while True:
    inp = input('>>>')
    sk.sendall(bytes(inp, 'utf8'))
    # 接收数据
    data = sk.recv(1024)
    print(str(data, 'utf8'))
    if inp == 'exit':
        break
sk.close()