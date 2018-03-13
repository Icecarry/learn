"""
在一个电脑中编写1个程序，有2个功能
1.获取键盘数据，并将其发送给对方
2.接收数据并显示
并且功能数据进行选择以上的2个功能调用
"""
import socket


# 发送消息函数
def send_msg():
    # 创建套接字
    s_m = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 绑定端口号
    local_soc = ('192.168.35.106', 8080)
    s_m.bind(local_soc)

    # 发送消息
    send_msg = input('请输入要发送的信息：')
    send_addr = ('192.168.35.31', 2425)
    s_m.sendto(send_msg.encode('utf-8'), send_addr)

    # 关闭套接字
    s_m.close()


# 接收消息函数
def recv_msg():
    # 创建套接字
    r_m = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 绑定端口号
    local_soc = ('', 2425)
    r_m.bind(local_soc)

    # 接收消息
    print('准备接收数据：')
    # rec_msg = r_m.recvfrom(1024)
    # print(rec_msg)
    rec_msg, rec_addr = r_m.recvfrom(1024)
    print("%s 发送了 %s " %(rec_addr[0], rec_msg.decode('utf-8')))

    # 关闭套接字
    r_m.close()


def print_help():
    print('1.发送消息')
    print('2.接收消息')
    print('3.退出')


# 主函数
def main():
    # 死循环接收发送数据
    while True:
        # 选择执行接收或者发送
        print_help()
        num = int(input("请选择操作:"))

        # 发送消息
        if num == 1:
            send_msg()

        # 接收消息
        elif num == 2:
            recv_msg()

        # 退出循环
        elif num == 3:
            break

        else:
            print('输入有错误！请重新输入！')
            print()
            continue


main()

