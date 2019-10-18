# 快速排序

import random


def quick_sort_one(array, start, end):
    threshold = random.randint(start, end)
    index = start-1

    array[threshold], array[end] = array[end], array[threshold]

    for i in range(start, end):
        if array[i] < array[end]:
            index += 1
            if index != i:
                array[index], array[i] = array[i], array[index]
    index += 1
    array[index], array[end] = array[end], array[index]
    return index


def quick_sort(array, start, end):
    index = quick_sort_one(array, start, end)
    if index > start:
        quick_sort(array, start, index-1)
    if index < end:
        quick_sort(array, index+1, end)


if __name__ == '__main__':
    test_array = list()
    for i in range(20):
        test_array.append(random.randint(0, 100))
    print('排序前：', test_array)

    quick_sort(test_array, 0, 19)
    print('排序后：', test_array)
