# coding=utf-8
from pymysql import *


class DB(object):
    def __init__(self):
        # 连接数据库
        self.conn = connect(host='192.168.35.105', port=3306, database='jing_dong', user='root', password='mysql',
                            charset='utf8')
        # 创建cs1对象
        self.cs1 = self.conn.cursor()

    def __enter__(self):
        return self.cs1

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cs1.close()
        self.conn.close()


with DB() as db:
    sql = """ select * from goods; """
    db.execute(sql)
    contect = db.fetchall()
    for temp in contect:
        print(temp)
