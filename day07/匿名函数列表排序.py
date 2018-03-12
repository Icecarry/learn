"""
* a = [{'name':'zhangsan','age':18},{'name':'lisi','age':19},{'name':'wanger','age':16}]
    * 按照姓名排序并打印
    * 按照年龄排序并打印
"""


# 按照姓名排序
a = [
    {'name': 'zhangsan', 'age': 18},
    {'name': 'lisi', 'age': 19},
    {'name': 'wanger', 'age': 16}
]
a.sort(key=lambda x: x['name'])
print(a)


# 按照年龄排序
a.sort(key=lambda x: x['age'])
print(a)

