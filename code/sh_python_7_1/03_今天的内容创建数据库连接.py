from  pymysql import  *


def main():

    # 1. 连接数据
    # 创建Connection连接
    conn = connect(host='localhost', port=3306, database='jing_dong', user='root', password='mysql', charset='utf8')
    # 获得Cursor对象
    cs1 = conn.cursor()
    # 2. 执行sql语句
    cs1.execute(""" select * from goods; """);

    content = cs1.fetchall()

    # 3. 关闭
    cs1.close()
    conn.close()

    # ctrl_alt+回车
    #处理数据
    for temp in content:
        print(temp)





if __name__ == '__main__':
    main()