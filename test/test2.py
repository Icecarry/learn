import socket
import multiprocessing
import re


def handler_client(sc):
    a = sc.recv(1024).decode('utf-8')
    c = a.splitlines()[0]
    path = re.match(r'[^/]+([^ ]+)', c).group(1)
    print(path)
    if path == '/':
        path = '/index.html'
    try:
        with open('html/html' + path, 'rb')as a:
            responbody = a.read()
    except:
        responbody = '404 您访问的页面不存在'
        responhead = 'HTTP/1.1 404 NOTFOUND\r\n'
        responhead += '\r\n'
        sc.send((responhead + responbody).encode('utf-8'))
    else:
        responhead = 'HTTP/1.1 200 OK\r\n'
        responhead += '\r\n'
        sc.send(responhead.encode('utf-8'))
        sc.send(responbody)
    sc.close()


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('127.0.0.1', 8080))
    s.listen(128)
    while True:
        sc, sa = s.accept()
        t1 = multiprocessing.Process(target=handler_client, args=(sc,))
        t1.start()
        sc.close()


if __name__ == '__main__':
    main()
