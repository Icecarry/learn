from  pymysql import *


# 这个就我们京东数据操作的界面入口函数
# ctrl+alt+L必须用格式化
class JD(object):
    def find_all(self):
        # 查询 所有的商品
        # 1. 去数据拿数据
        # 1. 连接数据库
        # 2. 执行sql语句
        # 3. 关闭
        # 2. 显示

        # 1.连接 数据 库

        # 创建Connection连接
        conn = connect(host='localhost', port=3306, database='jing_dong', user='root', password='mysql', charset='utf8')
        # 获得Cursor对象
        cs1 = conn.cursor()

        # 2. 执行sql语句
        cs1.execute(""" select * from goods;  """)

        content = cs1.fetchall()

        # 3. 关闭
        cs1.close()
        conn.close()

        # 4.显示
        for temp in content:
            print(temp)

    def find_cate(self):
        # 查询 所有的商品
        # 1. 去数据拿数据
        # 1. 连接数据库
        # 2. 执行sql语句
        # 3. 关闭
        # 2. 显示

        # 创建Connection连接
        conn = connect(host='localhost', port=3306, database='jing_dong', user='root', password='mysql', charset='utf8')
        # 获得Cursor对象
        cs1 = conn.cursor()
        cs1.execute(""" select * from goods_cates; """)

        content = cs1.fetchall()

        cs1.close()
        conn.close()

        for temp in content:
            print(temp)

    def find_brand(self):
        # 查询 所有的商品
        # 1. 去数据拿数据
        # 1. 连接数据库
        # 2. 执行sql语句
        # 3. 关闭
        # 2. 显示


        # 1. 连接数据
        # 创建Connection连接
        conn = connect(host='localhost', port=3306, database='jing_dong', user='root', password='mysql', charset='utf8')
        # 获得Cursor对象
        cs1 = conn.cursor()
        # 2. 执行sql语句
        cs1.execute(""" select * from goods_brands; """);

        content = cs1.fetchall()

        # 3. 关闭
        cs1.close()
        conn.close()

        for temp in content:
            print(temp)

    # 插入数据
    def insert_cate(self, cate_name):
        # 连接数据操作数据
        # 友情提示一下成功了

        # 1. 连接数据
        # 创建Connection连接
        conn = connect(host='localhost', port=3306, database='jing_dong', user='root', password='mysql', charset='utf8')
        # 获得Cursor对象
        cs1 = conn.cursor()
        # 2. 执行sql语句

        sql = """ insert into goods_cates (name) value ("%s"); """ % cate_name
        print(sql)
        cs1.execute(sql)

        conn.commit()  # 提交

        # 3. 关闭
        cs1.close()
        conn.close()

        # 4.插入成功
        print("亲,你成功了!")

    def find_all_id(self, id):

        # 1. 连接数据
        # 创建Connection连接
        conn = connect(host='localhost', port=3306, database='jing_dong', user='root', password='mysql', charset='utf8')
        # 获得Cursor对象
        cs1 = conn.cursor()
        # 2. 执行sql语句
        # cs1.execute(""" select * from goods where id = %s; """)%(id, );
        cs1.execute(""" select * from goods where id = %s; """ % id)

        # select * from goods where id = 1 or 1 ; 这个就是sql注入




        content = cs1.fetchall()

        # 3. 关闭
        cs1.close()
        conn.close()

        for temp in content:
            print(temp)

    def find_all_id_safe(id):

        # 1. 连接数据
        # 创建Connection连接
        conn = connect(host='localhost', port=3306, database='jing_dong', user='root', password='mysql', charset='utf8')
        # 获得Cursor对象
        cs1 = conn.cursor()
        # 2. 执行sql语句
        sql = """ select * from goods where id = %s; """

        cs1.execute(sql, id);
        # cs1.execute(sql,(id,) );
        # cs1.execute(sql,[id] );  ctrl+shift+i:查询api函数

        content = cs1.fetchall()

        # 3. 关闭
        cs1.close()
        conn.close()

        for temp in content:
            print(temp)

    def run_server(self):
        while True:
            print("1查询所有商品信息")
            print("2查询所有商品在种类信息")
            print("3查询所有商品在品牌信息")
            print("4添加商品种类")
            print("5根据id查询商品信息")
            print("6根据id查询商品信息安全方式")

            # 等待用户输入
            data = input()

            # 用户输入行为的判断
            # alt+j这个选中一样的代码
            if data == "1":
                self.find_all()
            elif data == "2":
                self.find_cate()
            elif data == "3":
                self.find_brand()
            elif data == "4":
                print("请输入商品类型名称")

                cate_name = input()  # 商品的类型

                self.insert_cate(cate_name)
            elif data == "5":
                print("请输入您的id")

                id = input()

                self.find_all_id(id)

            elif data == "6":
                print("请输入您的id")

                id = input()

                self.find_all_id_safe(id)


            else:
                print("亲,您输入有误!")


def main():
    jd = JD()
    jd.run_server()


if __name__ == '__main__':
    main()
