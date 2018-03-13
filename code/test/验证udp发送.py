import socket


def main():
    # 创建套接字
    udp_sed = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:

        # 传送消息
        gs = '1: 1238605487:user: machine:32:'
        msg_a = input('请输入内容：')  # 发送的内容
        msg = gs + msg_a
        # 1: 1238605487:user: machine:32: hello
        addr = ('192.168.35.31', 2425)  # 目标ip地址端口
        udp_sed.sendto(msg.encode('utf-8'), addr)

        if msg_a == 'exit':
            break

    # 关闭套接字
    udp_sed.close()

if __name__ == '__main__':
    main()
