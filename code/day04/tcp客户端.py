import socket


def main():
    # 创建套接字tcp
    tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 绑定端口
    server_addr = ('127.0.0.1', 8080)
    tcp_client.connect(server_addr)

    #　发送消息
    send_msg = input("请输入发送的数据：")
    tcp_client.send(send_msg.encode('utf-8'))

    #　接收消息
    print("正在接收数据：")
    tcp_recv = tcp_client.recv(1024)
    print(tcp_recv.decode('utf-8'))

    #　关闭套接字 　
    tcp_client.close()

if __name__ == '__main__':
     main()

