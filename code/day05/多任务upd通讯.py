"""
编写一个有2个线程的程序
线程1用来接收数据然后显示
线程2用来检测键盘数据然后通过udp发送数据
"""
import threading
import socket


def send_msg_to(udp_sock):
    while 1:
        # 发送数据
        send_addr = ('192.168.35.120', 8080)
        send_msg = input('请输入要发送的内容: ')
        udp_sock.sendto(send_msg.encode('utf-8'), send_addr)


def recv_msg_from(udp_sock):
    while 1:
        # 接收数据
        # print('正在接收数据～～～')
        recv_msg, recv_addr = udp_sock.recvfrom(1024)
        print('%s 发来消息: %s' % (recv_addr[0], recv_msg.decode('utf-8')))


def main():
    # 创建套接字
    udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 绑定端口
    local_addr = ('127.0.0.1', 1342)
    udp_sock.bind(local_addr)

    # 创建线程
    send_1 = threading.Thread(target=send_msg_to, args=(udp_sock,))
    recv_1 = threading.Thread(target=recv_msg_from, args=(udp_sock,))

    # 执行线程
    send_1.start()  # 发送数据
    recv_1.start()  # 接收数据

    # 发送数据
    # send_msg_to(udp_sock)

    # 接收数据
    # recv_msg_from(udp_sock)

    # 关闭套接字
    # udp_sock.close()


if __name__ == '__main__':
    main()
