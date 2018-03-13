import re
import os
import socket


def handler_client(client_soc,request_head):
    # 获取请求头
    # request_head = client_soc.recv(1024).decode('utf-8')

    if request_head:
        first_line = request_head.splitlines()[0]
        path = re.match(r'[^/]+([^ ]+)', first_line).group(1)
        print('获取到的路径为：', path)

        if path == '/':
            path = '/index.html'

        try:
            file = open('/home/python/Desktop/code/day09/html' + path, 'rb')
            response_body = file.read()
            file.close()

        except Exception:
            response_head = 'HTTP/1.1 404 NOT FOUND\r\n'
            response_head += '\r\n'
            response_body = '文件不存在！'
            client_soc.send(response_head.encode('utf-8'))
            client_soc.send(response_body)

        else:
            response_head = 'HTTP/1.1 200 OK\r\n'
            response_head += '\r\n'
            client_soc.send(response_head.encode('utf-8'))
            client_soc.send(response_body)

    client_soc.close()


def main():
    """HTTP服务器-非阻塞基本版"""
    # 创建服务器套接字
    server_soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)    # 设置套接字可以重复使用
    server_soc.bind(('', 8081))
    server_soc.listen(128)

    # 设置服务器套接字为非阻塞的
    server_soc.setblocking(False)

    # 为了每次循环都能访问已有的套接字，所以用一个列表存储他们
    client_ls = []

    while True:
        import time
        time.sleep(1)

        # 服务器获取新客户端的连接
        try:
            print('正在获取客户端连接')
            client_soc, client_addr = server_soc.accept()

        except Exception:
            print('发生异常，没有获取到客户端连接')

        else:
            print('没有发生异常，有客户端连接')
            client_soc.setblocking(False)    # 设置客户端套接字为非阻塞模式
            client_ls.append(client_soc)

        # 遍历列表获取每一个客户端套接字
        for client_soc in client_ls:
            try:
                print('开始接收数据')
                msg = client_soc.recv(1024)
            except Exception:
                print('出现异常，客户端没有传来数据')
            else:
                print('接收到了数据，', msg.decode('utf-8'))
                handler_client(client_soc,msg.decode('utf-8'))

    server_soc.close()


if __name__ == '__main__':
    main()