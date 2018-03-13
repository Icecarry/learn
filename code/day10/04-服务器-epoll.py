"""服务器，进程版"""
import socket
import re
import select


def handle_req(client_soc,browser_head):

    # browser_head = client_soc.recv(1024).decode('utf-8')
    # print(browser_head)
    head_first = browser_head.splitlines()[0]

    if head_first:
        # re
        rule = r'[^/]+([^ ]+)'
        req_addr = re.match(rule, head_first).group(1)
        print(req_addr)

        if req_addr == '/':
            req_addr = '/index.html'
        # open request file
        try:
            with open('/home/python/Desktop/code/day09/html' + req_addr, 'rb') as file:
                res_body = file.read()
        except:
            res_head = 'HTTP/1.1 404 NO FOUND\r\n'
            res_head += '\r\n'
            res_body = '页面未找到'
            res_msg = res_head + res_body
            client_soc.send(res_msg.encode('utf-8'))
        else:
            # response
            res_head = 'HTTP/1.1 200 OK\r\n'
            res_head += 'Connection: keep-alive\r\n'
            res_head += 'Content-Length:%d\r\n' % len(res_body)
            res_head += '\r\n'
            client_soc.send(res_head.encode('utf-8'))
            client_soc.send(res_body)

    # close
    # client_soc.close()


def main():
    # creat sockt
    # creat
    sever_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # reuse port
    sever_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sever_ip = ''
    sever_port = 8080
    sever_addr = (sever_ip, sever_port)
    sever_sock.bind(sever_addr)
    # max listener 128
    sever_sock.listen(128)

    # select
    epl = select.epoll()

    # register
    # print(sever_sock.fileno())
    # print(select.EPOLLIN)
    epl.register(sever_sock.fileno(), select.EPOLLIN)

    # 字典存放文件描述符和套接字的键值对
    client_direc = {}

    while True:
        epoll_list = epl.poll()  # 0号下标文件描述符，１号下标时间类型
        print(epoll_list)

        for filedir, event in epoll_list:
            if filedir == sever_sock.fileno():
                # 获取套接字
                client_soc, client_addr = sever_sock.accept()
                print('接收到有效的套接字～～～')

                epl.register(client_soc.fileno(),select.EPOLLIN)
                # 存放套接字到列表
                client_direc[client_soc.fileno()] = client_soc
            else:
                client_soc = client_direc[filedir]
                msg = client_soc.recv(1024)
                if msg:
                    handle_req(client_soc,msg.decode('utf-8'))
                else:
                    # epl.unregister(client_soc.fileno())
                    client_soc.close()
                    epl.unregister(filedir)
                    del client_direc[filedir]
        # # accept
        # client_soc, client_addr = sever_sock.accept()
        #
        # handle_req(client_soc)
        #
        # client_soc.close()

    sever_sock.close()


if __name__ == '__main__':
    main()

