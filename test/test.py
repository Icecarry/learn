import socket


def main():
    sever_soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sever_soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sever_soc.bind(('', 1314))
    sever_soc.listen(128)

    print('-------1-----')
    sclient, saddr = sever_soc.accept()

    print('------2------')
    sclient.recv(1024)
    # m = sclient.recv(1024).decode('utf-8')
    # print(m)
    print(sclient.recv(1024).decode('utf-8'))

    respond_head = 'HTTP/1.1 200 OK\r\n'
    respond_head += '\r\n'
    respond_body = 'hello world 2'
    respond_msg = respond_head + respond_body
    sclient.send(respond_msg.encode('utf-8'))

    sclient.close()
    sever_soc.close()


if __name__ == '__main__':
    main()

# import socket
# import re
#
#
# def main():
#     # 服务器套接字初始化
#     # 创建服务器套接字
#     sever_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     # 绑定地址
#
#     # 设置当服务器先close 即服务器端4次挥手之后资源能够立即释放，这样就保证了，下次运行程序时 可以立即绑定1314端口
#     sever_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#
#     sever_ip = ''
#     sever_port = 1314
#     sever_addr = (sever_ip,sever_port)
#     sever_sock.bind(sever_addr)
#     # 设置套接字转为监听模式，最大连接数为１２８
#     sever_sock.listen(128)
#
#     # 获取客户端套接字
#     client_sock,client_addr = sever_sock.accept()
#
#     # 接收客户端请求数据
#     headler_info = client_sock.recv(1024).decode("utf-8")
#     # 解析请求头
#     recv_header = headler_info.splitlines()[0]
#     print(recv_header)
#
#     # 正则解析
#     # rule = r'[^/]+([^ ]+)'
#     rule = r'.+?\s(.*?)\s.+'
#     res = re.match(rule, recv_header).group(1)
#     print('address is :', res)
#
#     # 返回响应头和响应体
#     response_head = 'HTTP/1.1 200 OK\r\n'
#     response_head += '\r\n'
#     response_body = 'haha'
#     response_msg = response_head + response_body
#
#     client_sock.send(response_head.encode('utf-8'))
#     client_sock.send(response_body.encode('utf-8'))
#
#     # 关闭客户端套接字
#     client_sock.close()
#     # 关闭服务器套接字
#     sever_sock.close()
#
#
# if __name__ == '__main__':
#     main()
