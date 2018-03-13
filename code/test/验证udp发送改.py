import socket


def main():
    # 创建套接字
    udp_sed = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    local = ('192.168.35.106',8081)
    udp_sed.bind(local)

    while True:

        # 传送消息
        msg = input('请输入内容：')  # 发送的内容
        addr = ('192.168.35.106', 8080)  # 目标ip地址端口
        udp_sed.sendto(msg.encode('utf-8'), addr)

        if msg == 'exit':
            break

    # 关闭套接字
    udp_sed.close()

if __name__ == '__main__':
    main()
