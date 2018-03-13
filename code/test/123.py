# import socket
#
# def main():
#     # 1.创建套接字
#     udp_soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#
#     # 2.发送文件
#     addr = ('192.168.35.31', 8080)
#     udp_soc.sendto(b'hi girl', addr)
#
#     # 3.关闭套接字
#     udp_soc.close()
#
# if __name__ == '__main__':
#     main()

#
# import re
#
#
# ls_net = ['http://www.interoem.com/messageinfo.asp?id=35',
#           'http://3995503.com/class/class09/news_show.asp?id=14',
#           'http://lib.wzmc.edu.cn/news/onews.asp?id=769',
#           'http://www.zy-ls.com/alfx.asp?newsid=377&id=6',
#           'http://www.fincm.com/newslist.asp?id=415']
#
#
# for net in ls_net:
#     res = re.match(r'.+\.(com|cn)', net).group()
#     print(res)

import re


ls_net = '''
            http://www.interoem.com/messageinfo.asp?id=35
            http://3995503.com/class/class09/news_show.asp?id=14
            http://lib.wzmc.edu.cn/news/onews.asp?id=769
            http://www.zy-ls.com/alfx.asp?newsid=377&id=6
            http://www.fincm.com/newslist.asp?id=415
            '''

res = re.findall(r'(http://.+\.(com|cn))', ls_net)
print(res)
