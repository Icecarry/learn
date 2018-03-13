import socket
import re
import multiprocessing
from dynamic import mini_web_06

class WEBServer(object):
    def __init__(self):
        # 1. 创建套接字
        self.tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # 2. 绑定
        self.tcp_server_socket.bind(("", 7788))

        # 3. 变为监听套接字
        self.tcp_server_socket.listen(128)

    def service_client(self, new_socket):
        """为这个客户端返回数据"""

        # 1. 接收浏览器发送过来的请求 ，即http请求
        # GET / HTTP/1.1
        # .....
        request = new_socket.recv(1024).decode("utf-8")
        # print(">>>"*50)
        # print(request)

        request_lines = request.splitlines()
        print("")
        print(">"*20)
        print(request_lines)

        # GET /index.html HTTP/1.1
        # get post put del
        file_name = ""
        ret = re.match(r"[^/]+(/[^ ]*)", request_lines[0])
        if ret:
            file_name = ret.group(1)
            # print("*"*50, file_name)
            if file_name == "/":
                file_name = "/index.html"


        #如果是.py结尾的文件 我们动态返回
        if file_name.endswith(".py"):
            # 返回数据

            url_params = dict() #生成一个字典
            url_params["url_path"] = file_name  #存入路径

            # mini_web返回数据
            body = mini_web_06.application(url_params,self.head_params)

            #这个一定要写在wsgi协议调用之后
            # header = "HTTP/1.1 200 OK\r\n"
            header = "HTTP/1.1 %s\r\n" % self.stauts
            # 这里就可以根据不同的访问的路径返回不同数据

            # 拿到mini_web的头部参数,进行拼接
            for temp in self.params:
                header += "%s:%s\r\n"%(temp[0],temp[1])   #每一个头部字段必须换行


            #返回数据固定的格式
            data = header + "\r\n" + body

            new_socket.send(data.encode("utf-8"))
        else:
            #如果不是py结尾,还是以前的处理

            # 2. 返回http格式的数据，给浏览器

            try:
                f = open("./static" + file_name, "rb")
            except:
                response = "HTTP/1.1 404 NOT FOUND\r\n"
                response += "\r\n"
                response += "------file not found-----"
                new_socket.send(response.encode("utf-8"))
            else:
                html_content = f.read()
                f.close()
                # 2.1 准备发送给浏览器的数据---header
                response = "HTTP/1.1 200 OK\r\n"
                response += "\r\n"
                # 2.2 准备发送给浏览器的数据---boy
                # response += "hahahhah"

                # 将response header发送给浏览器
                new_socket.send(response.encode("utf-8"))
                # 将response body发送给浏览器
                new_socket.send(html_content)


        # 关闭套接
        new_socket.close()


    def run_server(self):
        """用来完成整体的控制"""

        while True:
            # 4. 等待新客户端的链接
            new_socket, client_addr = self.tcp_server_socket.accept()

            # 5. 为这个客户端服务
            p = multiprocessing.Process(target=self.service_client, args=(new_socket,))
            p.start()

            new_socket.close()


        # 关闭监听套接字
        tcp_server_socket.close()

    def head_params(self, stauts, params):
        # print(stauts)
        # print(params)
        self.stauts = stauts
        self.params = params

def main():
    #开启服务器
    web_server = WEBServer()
    web_server.run_server()


if __name__ == "__main__":
    main()

