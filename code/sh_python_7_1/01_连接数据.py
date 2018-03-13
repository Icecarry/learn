from pymysql import *


def main():
    # 1.连接 数据 库
    # 创建Connection连接
    conn = connect(host='localhost', port=3306, database='jing_dong', user='root', password='mysql', charset='utf8')
    # 获得Cursor对象
    cs1 = conn.cursor()
    # 2. 执行sql语句
    cs1.execute("""select * from goods;""")

    # 提交
    # conn.commit() 这个是提交的时候
    content = cs1.fetchone()

    print(content)
    content = cs1.fetchone()

    print(content)

    content = cs1.fetchmany(3)
    # 取到的数据是元组的元组,小元组代表一行
    print(content)

    content = cs1.fetchall()
    print(content)

    # 3. 关闭连接
    cs1.close()
    conn.close()

    for temp in content:
        print(temp)


if __name__ == '__main__':
    main()