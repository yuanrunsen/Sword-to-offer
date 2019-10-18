# 二分查找

import random


def binary_search(array, start, end, value):
    while start <= end:
        mid = round((start+end)/2)
        if array[mid] == value:
            return mid
        elif array[mid] < value:
            start = mid+1
        else:
            end = mid-1
    return None


if __name__ == '__main__':
    test_array = list()
    for i in range(20):
        test_array.append(random.randint(0, 100))
    test_array.sort()
    print(test_array)
    print(binary_search(test_array, 0, 19, test_array[19]))

