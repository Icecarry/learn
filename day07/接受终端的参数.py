"""
设计一个程序，接受来自终端传入的参数
"""


# 加载包
import sys

print(sys.argv)

# 计算两个数字的和
num1 = int(sys.argv[1])
num2 = int(sys.argv[2])

sum1 = num1 + num2
print("结果为：", sum1)
