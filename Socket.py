#!/usr/bin/env python
# coding:utf-8
import json
import socket

HttpResponseHeader = '''HTTP/1.1 200 OK\r\n
Content-Type: text/html\r\n\r\n
'''


def handle_request(client):
    buf = client.recv(1024)
    print(buf)
    client.send("HTTP/1.1 200 OK\r\n\r\n")
    client.send("Hello, World")


def main():
    # 创建socket对象
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # bind方法监听某个端口
    sock.bind(('127.0.0.1', 5701))
    # 开始监听,
    sock.listen(100)
    # 保持长连接，否则久了会关闭导致下次通信报错
    sock.settimeout(0)

    while True:
        # 阻塞,等...
        # 直到有请求连接
        connection, address = sock.accept()
        # connection代表客户端sockert对象
        # address客户端IP地址
        data = connection.recv(1024).decode(encoding='utf-8')
        connection.sendall(HttpResponseHeader.encode(encoding='utf-8'))
        connection.close()
        if len(data) > 0 :
            print('接收到数据：', data)
        else:
            continue
        # handle_request(connection)
        # connection.close()


if __name__ == '__main__':
    main()
