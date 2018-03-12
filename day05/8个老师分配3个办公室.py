# 使用列表嵌套，完成8名老师随机分配3个办公室

import random

# 8个老师放在列表里
teachers = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

# 有三个教室
classRooms = [[], [], []]

# 循环遍历老师，把他们放入教室
for teacher in teachers:
    classRooms[random.randint(0, 2)].append(teacher)
print(classRooms)

