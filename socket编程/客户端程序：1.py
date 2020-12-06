# -*- coding: utf-8 -*-
"""
author: LHQ
by keyboy
"""
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 文件名：client.py

import socket
import threading

s = socket.socket()
s.connect(('127.0.0.1', 30000))


def read_server(s):
    while True:
        # 子线程负责从服务端接受数据并打印
        content = s.recv(2048).decode('utf-8')
        print(content)


threading.Thread(target=read_server, args=(s,)).start()

while True:
    line = input('')
    if line == 'exit':
        break
    # 主线程负责将用户输入的数据发送到socket中
    s.send(line.encode('utf-8'))