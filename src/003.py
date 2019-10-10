#  面试题4：二维数组中的查找
#  题目：在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按
#  照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个
#  整数，判断数组中是否含有该整数。
# 假设数组 array 有 m 行 n 列

# 方法一：两层循环，直接遍历一遍二维数组，则时间复杂度为 O(m*n)
# 方法二：利用有序的性质，从右上角开始查找，不断的减少一行或一列，时间复杂度 O(m+n)


# 方法二如下:
def is_in_array(array, rows, columns, number):
    row = 0
    column = columns-1
    while (row <= rows-1) and (column >= 0):
        if array[row][column] == number:
            return True
        elif array[row][column] >= number:
            column -= 1
        else:
            row += 1
    return False


if __name__ == '__main__':
    array = [[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [5, 8, 11, 15]]
    is_find = is_in_array(array, 4, 4, 5)
    print(is_find)
