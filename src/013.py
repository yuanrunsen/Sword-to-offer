# 面试题11：旋转数组的最小数字
# 题目：把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
# 输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。例如数组
# {3, 4, 5, 1, 2}为{1, 2, 3, 4, 5}的一个旋转，该数组的最小值为1。

import random


# 特殊情况暂不考虑
def find_min(array, start, end):
    while end-start > 1:
        mid = round((start + end) / 2)
        if array[mid] >= array[start]:
            start = mid
        else:
            end = mid
    return array[end]


if __name__ == '__main__':
    test_array1 = list()
    for i in range(10):
        test_array1.append(random.randint(10, 20))
    test_array1.sort()

    test_array2 = list()
    for i in range(20):
        test_array2.append(random.randint(0, 10))
    test_array2.sort()

    test_array1.extend(test_array2)

    print(test_array1)
    print('min:', min(test_array1))
    print('min:', find_min(test_array1, 0, 29))
