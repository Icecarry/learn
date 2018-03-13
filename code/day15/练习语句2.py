from pymysql import *


def run_jing_dong():
    # 连接数据库
    # 执行操作
    # 关闭连接

    # 1.创建连接
    conn = connect(host='localhost', port='3306', database='jing_dong', user='root', password='mysql', charset='utf8')
    cs1 = conn.cursor()

    # 执行数据库操作
    sql = """ select * from goods; """
    cs1.execute(sql)

    db = cs1.fetchall()

    # 关闭连接
    cs1.close()
    conn.close()


def main():
    run_jing_dong()


if __name__ == '__main__':
    main()
