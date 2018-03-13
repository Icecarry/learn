# import pymysql
from pymysql import *


def main():
    # 创建Connection对象
    conn = connect(host='localhost', port=3306, database='jing_dong', user='root', password='mysql', charset='utf8')
    # 获取出对象
    cs1 = conn.cursor()
    # 执行操作
    count = cs1.execute("""select * from goods order by price desc;""")
    # for i in range(count):
    #     result = cs1.fetchone()
    #     print(result)

    for temp in cs1.fetchall():
        print(temp)

    print(count)
    # conn.commit()

    # 关闭对象
    cs1.close()
    conn.close()


if __name__ == '__main__':
    main()
