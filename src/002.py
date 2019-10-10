# 面试题3（一）：找出数组中重复的数字
# 题目：在一个长度为n+1的数组里的所有数字都在1到n的范围内。
# 所以数组中至少有一个数字是重复的，请找出数组中任意一个重复的数字。例如，如果输入长度为8的数组{2, 3, 5, 4, 3, 2, 6, 7}，
# 那么对应的输出是重复的数字2或者3。

# 方法一：两层循环 时间复杂度 O(n^2)
# 方法二：先排序（如快速排序），然后一次遍历即可 时间复杂度 为排序算法的时间复杂度O(nlogn)
# 方法三：借助hash表，遍历一次即可 时间复杂度 O(n)  因为有hash表 所以空间复杂度为O(n)
# 方法四：所有的数字值都在 1～ n 的范围，且下标也是 0 ～ n
# 那么遍历一次，不断的把每个数字值对应的下标放到对应位置，直到有重复 或者遍历完成,虽然有两层循环但实际每个元素
# 最多只被交换或者主动交换了各一次 时间复杂度 O(n)
# 方法五： 数字值区间在1~n内，把1~ n分成两个区间，统计区间内出现的个数，如果大于区间元素总个数 说明有重复，再进行该区间的查找
# 有点像二分查找


# 方法五如下:
def count_number(src_data, start, end, length):
    count = 0
    for i in range(length):
        if (src_date[i] >= start) and (src_date[i] <= end):
            count += 1
    return count


def get_one_duplicate(src_data, length):
    max_value = length-1

    start = 1
    end = int((max_value + 1) / 2)

    while start < max_value:
        count = count_number(src_date, start, end, length)
        if count > end-start+1:
            max_value = end
            end = int((start+end)/2)
        else:
            start = end+1
            end = max_value
    return start



if __name__ == '__main__':
    src_date = [2, 3, 5, 4, 3, 2, 6, 7]
    length = len(src_date)
    duplicate = get_one_duplicate(src_date, length)
    print(duplicate)
