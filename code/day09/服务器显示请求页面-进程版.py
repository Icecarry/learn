"""
写一个静态服务器，显示固定页面，页面内容为hello world
"""
import socket
import re
import multiprocessing


def handler_client(client_sock):
    # 接收客户端请求数据
    headler_info = client_sock.recv(1024).decode("utf-8")
    # print(recv_header)
    if headler_info:
        # 解析请求头
        recv_header = headler_info.splitlines()[0]

        # 正则解析
        # rule = r'[^/]+([^ ]+)'
        rule = r'.+?\s(.*?)\s.+'
        path = re.match(rule, recv_header).group(1)
        print('address is :', path)

        if path == '/':
            path = '/index.html'

        # 返回响应头和响应体
        response_head = 'HTTP/1.1 200 OK\r\n'
        response_head += '\r\n'

        try:
            with open('html'+path, 'rb') as file:
                response_body = file.read()
        except:
            response_head = 'HTTP/1.1 404 NOT FOUND\r\n'
            response_head += '\r\n'
            response_body = '找不到文件'
            response_msg = response_head + response_body
            client_sock.send(response_msg.encode('utf-8'))
        else:
            # response_body = 'hello world'
            # response_msg = response_head + response_body

            client_sock.send(response_head.encode('utf-8'))
            client_sock.send(response_body)

    # 关闭客户端套接字
    client_sock.close()


def main():
    # 服务器套接字初始化
    # 创建服务器套接字
    sever_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 绑定地址

    # 设置当服务器先close 即服务器端4次挥手之后资源能够立即释放，这样就保证了，下次运行程序时 可以立即绑定1314端口
    sever_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    sever_ip = ''
    sever_port = 1315
    sever_addr = (sever_ip, sever_port)
    sever_sock.bind(sever_addr)
    # 设置套接字转为监听模式，最大连接数为１２８
    sever_sock.listen(128)

    while True:
        # 获取客户端套接字
        client_sock, client_addr = sever_sock.accept()

        # 客户端套接字
        # handler_client(client_sock)

        pro = multiprocessing.Process(target=handler_client, args=(client_sock,))
        pro.start()

        client_sock.close()

    # 关闭服务器套接字
    sever_sock.close()


if __name__ == '__main__':
    main()
