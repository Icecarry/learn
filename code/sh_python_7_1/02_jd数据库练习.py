from pymysql import *

# 一定死循环等用户的输入
#查询所有商品信息
def search_info():
    # 1. 连接数据库
    # 创建Connection连接
    conn = connect(host='localhost', port=3306, database='jing_dong', user='root', password='mysql', charset='utf8')
    # 获得Cursor对象
    cs1 = conn.cursor()
    # 2. 执行sql语句
    sql = """ select * from goods; """
    cs1.execute(sql)

    # 得到结果
    content = cs1.fetchall()
    for temp in content:
        print(temp)

    # 3. 关闭连接
    cs1.close()
    conn.close()

#查询种类信息
def search_cate():
    # 1.连接数据库
    # 创建Connection连接
    conn = connect(host='localhost', port=3306, database='jing_dong', user='root', password='mysql', charset='utf8')
    # 获得Cursor对象
    cs1 = conn.cursor()

    # 2. 执行数据
    sql = """ select * from goods_cates; """
    cs1.execute(sql)

    content = cs1.fetchall()
    for temp in content:
        print(temp)

    # 3. 关闭数据
    cs1.close()
    conn.close()


#查询品牌信息
def search_brand():
    # 1.连接数据
    # 创建Connection连接
    conn = connect(host='localhost', port=3306, database='jing_dong', user='root', password='mysql', charset='utf8')
    # 获得Cursor对象
    cs1 = conn.cursor()
    # 2.执行sql语句
    sql = """ select * from goods_brand; """
    cs1.execute(sql)

    content = cs1.fetchall()

    for temp in content:
        print(temp)

    # 3.关闭连接
    cs1.close()
    conn.close()

# 添加一个商品信息
def add_info(type):
    # 1.连接数据
    # 创建Connection连接
    conn = connect(host='localhost', port=3306, database='jing_dong', user='root', password='mysql', charset='utf8')
    # 获得Cursor对象
    cs1 = conn.cursor()
    # 2 执行sql语句
    sql = """ insert into goods_cates(name) values("%s"); """%type

    # 执行sql
    cs1.execute(sql)
    conn.commit()  #提交数据


    # 3. 关闭
    cs1.close()
    conn.close()


def find_info(id):
    # 1.连接数据
    # 创建Connection连接
    conn = connect(host='localhost', port=3306, database='jing_dong', user='root', password='mysql', charset='utf8')
    # 获得Cursor对象
    cs1 = conn.cursor()

 # 2 执行sql语句
    sql = """ select * from goods where id = %s"""%id

    # 执行sql
    cs1.execute(sql)

    content = cs1.fetchall()
    for temp in content:
        print(temp)

    # 3. 关闭
    cs1.close()
    conn.close()


def find_info_safe(id):
    # 1.连接数据
    # 创建Connection连接
    conn = connect(host='localhost', port=3306, database='jing_dong', user='root', password='mysql', charset='utf8')
    # 获得Cursor对象
    cs1 = conn.cursor()

    # 2 执行sql语句
    sql = """ select * from goods where id = %s"""

    # 执行sql
    cs1.execute(sql,id)

    content = cs1.fetchall()
    for temp in content:
        print(temp)

    # 3. 关闭
    cs1.close()
    conn.close()


def run_server():
    while True:
        print("1查询所有商品信息")
        print("2查询所有商品在种类信息")
        print("3查询所有商品在品牌信息")
        print("4添加商品种类")
        print("5根据id查询商品信息")
        print("6根据id查询商品信息安全方式")
        data = input()

        #得到数据进行不同的处理
        if data == "1":
            #查询所有的商品信息
            print("商品信息")
            search_info()
        elif data == "2":
            #查询所有商品的种类信息
            print("商品种类")
            search_cate()
        elif data == "3":
            # 查询所有的商品品牌信息
            print("商品品牌")
            search_brand()
        elif data == "4":
            #需要用户输入商品种类
            print("请输入商品品牌")
            type = input()

            add_info(type)
        elif data == "5":
            print("请输入商品id")
            id = input()

            find_info(id)
        elif data == "6":
            print("请输入商品id")
            id = input()

            find_info_safe(id)
        else:
            # 输入的信息有误
            print("您好!您的输入有误!")


def main():
    # 1.用户在命令行输入相应的数字
    run_server()

if __name__ == '__main__':
    main()