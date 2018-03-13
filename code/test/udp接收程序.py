"""

python
# 1. 创建套接字
udp_socket = socket(AF_INET, SOCK_DGRAM)

# 2. 准备接收方的地址
send_addr = ('192.168.1.103', 8080)

# 3. 5秒钟收一次数据
while True:
    time.sleep(5)
    recv_data, dest_addr = udp_socket.recvfrom(100)
    print(recv_data.decode('utf-8'))
"""

import time
from socket import *


def main():
    # 1. 创建套接字
    udp_socket = socket(AF_INET, SOCK_DGRAM)

    # 绑定自己的端口
    local_soc = ('', 8089)
    udp_socket.bind(local_soc)

    # # 2. 准备接收方的地址
    # # send_addr = ('192.168.1.103', 8080)
    # send_addr = ('192.168.35.31', 8080)

    # 3. 5秒钟收一次数据
    while True:

        time.sleep(5)
        recv_data, dest_addr = udp_socket.recvfrom(100)
        print(recv_data.decode('utf-8'))

        if recv_data == 'exit':
            break

    # 关闭套接字
    udp_socket.close()

if __name__ == '__main__':
    main()
