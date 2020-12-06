# -*- coding: utf-8 -*-
"""
author: LHQ
by keyboy
"""
import socket
sk = socket.socket()
address = ('127.0.0.1', 8555)
sk.connect(address)
while True:
    inp = input('>>>')
    if inp == 'exit':
        break
    if not inp:
        continue
        # 发送数据
    sk.send(bytes(inp, 'utf8'))
    data = sk.recv(1024)  # 接收数据
    print(str(data, 'utf8'))
sk.close()