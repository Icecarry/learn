"""服务器，进程版"""
import socket
import re
import gevent
from gevent import monkey
# import multiprocessing
import threading

monkey.patch_all()


def handle_req(client_soc):

    browser_head = client_soc.recv(1024).decode('utf-8')
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
            res_head += '\r\n'
            client_soc.send(res_head.encode('utf-8'))
            client_soc.send(res_body)

    # close
    client_soc.close()


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

    while True:
        # accept
        client_soc, client_addr = sever_sock.accept()

        # t = threading.Thread(target=handle_req, args=(client_soc,))
        # t.start()
        print("携程开始")
        gevent.spawn(handle_req, client_soc)

        # client_soc.close()
        # handle_req(client_soc)

    sever_sock.close()


if __name__ == '__main__':
    main()

