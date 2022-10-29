__author__ = "JentZhang"

from socket import *
from time import ctime

HOST = '127.0.0.1'  # 服务器地址
PORT = 5701  # 服务器端口
BUFIZE = 1024  # 接受数据的大小
ADDR = (HOST, PORT)  # 创建socket时用到的地址（就是将服务器地址和端口写成一个元组的形式）

tcpSerSock = socket(AF_INET, SOCK_STREAM)  # 创建socket连接（AF_INET表示IPV4，SOCK_STREMAM表示TCP协议 ）
tcpSerSock.bind(ADDR)  # 绑定地址
tcpSerSock.listen(5)  # 开始监听端口，参数5表示可以接收的连接数量

while True:  # 循环接受多个客户端发来的请求
    try:
        print('Watting for connection...')
        tcpCliSock, addr = tcpSerSock.accept()  # 当有客户端发来请求时，通过accept()方法来接受，返回参数有两个，可以自行print出来，看看是什么
        print('...connected from :', addr)

        while True:  # 循环接受客户端发来的消息
            data = tcpCliSock.recv(BUFIZE)  # 接受客户端发来的消息，接收到的是一个byte类型的数据
            if not data:  # 当用户发送空字符串的是时候，跳出循环，重新接收数据
                break
            print('接收到数据：', data)
            tcpCliSock.send(b'[%s] % s' % (ctime().encode(), data))  # 将接收到的数据加上时间戳返回回去，同样返回的数据需要是byte类型
    except ConnectionResetError as e:  # 当客户端关闭连接时，catch这个错误做出相应的提示
        print(e)
        print('%s：%s 退出了' % (addr[0], addr[1]))  # 服务端也关闭相关的socket连接
    finally:
        tcpCliSock.close()
tcpSerSock.close()

if __name__ == '__main__':
    pass