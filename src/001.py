# 面试题3（一）：找出数组中重复的数字
# 题目：在一个长度为n的数组里的所有数字都在0到n-1的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，
# 也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。例如，如果输入长度为7的数组{2, 3, 1, 0, 2, 5, 3}，
# 那么对应的输出是重复的数字2或者3。

# 方法一：两层循环 时间复杂度 O(n^2)
# 方法二：先排序（如快速排序），然后一次遍历即可 时间复杂度 为排序算法的时间复杂度O(nlogn)
# 方法三：借助hash表，遍历一次即可 时间复杂度 O(n)  因为有hash表 所以空间复杂度为O(n)
# 方法四：所有的数字值都在 0 ～ n-1 的范围，且下标也是 0 ～ n-1，若无重复且有序，则数字值和下标相等
# 那么遍历一次，不断的把每个数字值对应的下标放到对应位置，直到有重复 或者遍历完成,虽然有两层循环但实际每个元素
# 最多只被交换或者主动交换了各一次 时间复杂度 O(n)


# 方法三如下:
def get_one_duplicate_by_hash(src_data, length):
    hash_map = dict()
    for index in range(length):
        is_duplicate = hash_map.get(src_data[index], False)
        if not is_duplicate:
            hash_map[src_data[index]] = True
        else:
            return src_data[index]


# 方法四如下:
def get_one_duplicate(src_data, length):
    for index in range(length):
        while src_date[index] != index:
            new_location = src_date[index]
            if src_date[index] == src_date[new_location]:
                return src_date[index]
            src_date[index], src_date[new_location] = src_date[new_location], src_date[index]


if __name__ == '__main__':
    src_date = [2, 3, 1, 0, 2, 5, 3]
    length = len(src_date)
    duplicate1 = get_one_duplicate_by_hash(src_date, length)
    print(duplicate1)
    duplicate2 = get_one_duplicate(src_date, length)
    print(duplicate2)
