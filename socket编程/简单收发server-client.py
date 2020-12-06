# -*- coding: utf-8 -*-
"""
author: LHQ
by keyboy
"""
'''
支持并发聊天的server
'''
import socketserver


class MySocketServer(socketserver.BaseRequestHandler):
    def handle(self):
        print('服务端启动')
        while True:
            conn = self.request
            print(self.client_address)
            while True:
                # 接收数据
                client_data = conn.recv(1024)
                print(str(client_data, 'utf8'))
                print('waiting...')
                # 发送数据
                inp = input('>>>')
                conn.sendall(bytes(inp, 'utf8'))
            conn.close()


if __name__ == '__main__':
    # 创建socketserver对象
    server = socketserver.ThreadingTCPServer(('127.0.0.1', 8000), MySocketServer)
    # 启动服务
    server.serve_forever()