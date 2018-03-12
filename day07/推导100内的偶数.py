"""
用列表推导式生成一个100以内的偶数列表(使用 if 来处理)
"""


a = [x for x in range(101) if x % 2 == 0]

print(a)