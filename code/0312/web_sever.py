# 自己写个服务器
import socket
import multiprocessing
import re


# 服务器类
class Web_server(object):
    # 初始化服务器
    def __init__(self):
        # 创建服务器套接字
        self.server_soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # 绑定
        self.server_ip = ""
        self.server_port = 7788
        self.server_soc.bind((self.server_ip, self.server_port))

        # 监听,最大监听128
        self.server_soc.listen(128)

        # 根据请求返回值

    def to_client(self, client_soc):
        # 获取请求头
        request = client_soc.recv(1024).decode('utf-8')
        request_lines = request.splitlines()

        # 正则匹配请求文件
        file_name = ''
        rule = r'[^/]+(/[^ ]*)'
        ret = re.match(rule, request_lines[0])
        if ret:
            file_name = ret.group(1)
            if ret == '/':
                file_name = '/index.html'
        else:
            # 如果不是.py结尾
            try:
                f = open('./代码/sh_python_07_mini02/static', 'rb')
            except:


    # 运行服务器
    def run_server(self):
        # 用来完成整体的控制
        while 1:
            # 获取客户端套接字
            client_soc, client_addr = self.server_soc.accept()

            # 多进程创建套接字
            client_p = multiprocessing.Process(target=self.to_client, args=(client_soc,))
            client_p.start()

            # 关闭客户端套接字
            client_soc.close()

        # 关闭服务器套接字
        self.server_soc.close()


def main():
    # 创建服务器
    web_server = Web_server()
    web_server.run_server()


if __name__ == '__main__':
    main()
