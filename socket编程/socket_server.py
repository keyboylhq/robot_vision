# -*- coding: utf-8 -*-
"""
author: LHQ
by keyboy
"""
import socket
# 创建socket对象
sk = socket.socket()
address = ('127.0.0.1', 8555)
# 绑定地址
sk.bind(address)
sk.listen(3)
# 监听客户端连接
while True:
    conn, address = sk.accept()
    print(address)
    while True:
        # 接收信息
        data = conn.recv(1024)
        if not data:
            break
        print(str(data, 'utf8'))
        # 发送信息
        inp = input('>>>')
        conn.send(bytes(inp, 'utf8'))
sk.close()