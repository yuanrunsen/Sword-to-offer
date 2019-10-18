# 面试题12：公司年龄排序
# 题目：公司年龄分布在0-100岁，写出一个时间复杂度为O(n)的算法进行排序


# 利用一个长为100的数组作为辅助空间
# 数组的下标对应年龄
# 数组下标里的值对应该年龄出现的次数
# 最后遍历辅助数组 对年龄次数大于一的依次对需要排序的数组赋值即可

import random


def sort_ages(ages_array):
    max_age = 100
    ages_count = [0 for i in range(max_age)]
    for age in ages_array:
        ages_count[age] += 1

    index = 0
    for age in range(max_age):
        for j in range(0, ages_count[age]):
            ages_array[index] = age
            index += 1


if __name__ == '__main__':
    test_array = list()
    for i in range(20):
        test_array.append(random.randint(0, 100))
    print('排序前：', test_array)

    sort_ages(test_array)
    print('排序后：', test_array)