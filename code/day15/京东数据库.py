from pymysql import *


# 选择帮助信息
def print_help():
    print("1查询所有商品信息")
    print("2查询所有商品在种类信息")
    print("3查询所有商品在品牌信息")
    print("4添加商品种类")
    print("5根据id查询商品信息")
    print("6根据id查询商品信息安全方式")
    print("7退出程序")


# 查询所有商品
def search_all():
    # 连接数据库
    conn = connect(host='localhost', port=3306, database='jing_dong', user='root', password='mysql', charset='utf8')
    # 获取cursor对象
    cs1 = conn.cursor()

    # 执行查询操作
    sql = """ select * from goods; """
    cs1.execute(sql)
    # 得到结果
    result = cs1.fetchall()

    for temp in result:
        print(temp)
    # 关闭连接
    cs1.close()
    conn.close()


# 查询所有商品种类
def search_cate():
    # 创建
    conn = connect(host='localhost', port=3306, database='jing_dong', user='root', password='mysql', charset='utf8')
    cs1 = conn.cursor()

    # 执行
    sql = """ select * from goods_cates; """
    cs1.execute(sql)

    # 取出结果
    result = cs1.fetchall()

    for temp in result:
        print(temp)

    # 关闭
    cs1.close()
    conn.close()


# 查询所有商品的品牌
def search_brand():
    # 连接
    conn = connect(host='localhost', port=3306, database='jing_dong', user='root', password='mysql', charset='utf8')
    cs1 = conn.cursor()

    # 执行
    sql = """ select * from goods_brands; """
    cs1.execute(sql)

    result = cs1.fetchall()
    for temp in result:
        print(temp)

    # 关闭
    cs1.close()
    conn.close()


# 添加商品种类
def add_cate(type):
    # 连接
    conn = connect(host='localhost', port=3306, database='jing_dong', user='root', password='mysql', charset='utf8')
    cs1 = conn.cursor()

    # 执行
    sql = """ insert into goods_cates (name) values('%s'); """ % type
    cs1.execute(sql)
    # 提交
    conn.commit()

    # 关闭
    cs1.close()
    conn.close()


# 查找商品
def search_goods(se_id):
    # 连接
    conn = connect(host='localhost', port=3306, database='jing_dong', user='root', password='mysql', charset='utf8')
    cs1 = conn.cursor()

    # 执行
    sql = """ select * from goods inner join goods_cates as gc on goods.cate_id = gc.id where goods.id = %s;""" % se_id
    cs1.execute(sql)

    result = cs1.fetchall()
    for temp in result:
        print(temp)

    # 关闭
    cs1.close()
    conn.close()


# 查找商品(安全)
def search_goods_safe(se_id):
    # 连接
    conn = connect(host='localhost', port=3306, database='jing_dong', user='root', password='mysql', charset='utf8')
    cs1 = conn.cursor()

    # 执行
    condition = (se_id,)
    sql = """ select * from goods inner join goods_cates as gc on goods.cate_id = gc.id where goods.id = %s;"""
    cs1.execute(sql, condition)

    result = cs1.fetchall()
    for temp in result:
        print(temp)

    # 关闭
    cs1.close()
    conn.close()


def run_JD():
    while True:
        # 打印帮助信息
        print_help()
        # 获取用户输入
        select_num = input()

        # 查询所有商品
        if select_num == '1':
            search_all()

        # 查询所有商品种类
        elif select_num == '2':
            search_cate()

        # 查询所有商品品牌
        elif select_num == '3':
            search_brand()

        # 添加商品种类
        elif select_num == '4':
            print('请输入商品种类:')
            type = input()

            add_cate(type)
        # id查询商品
        elif select_num == '5':
            print('请输入商品id:')
            se_id = input()

            search_goods(se_id)
        # id查询商品(安全)
        elif select_num == '6':
            print('请输入商品id:')
            se_id = input()

            search_goods_safe(se_id)

        # 退出程序
        elif select_num == '7':
            break

        else:
            print("输入有误！")


def main():
    run_JD()


if __name__ == '__main__':
    main()
