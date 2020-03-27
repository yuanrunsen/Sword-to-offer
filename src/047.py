# 面试题57（一）：和为s的两个数字
# 题目：输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们
# 的和正好是s。如果有多对数字的和等于s，输出任意一对即可。


# 方法： 因为这个是有序的数列 所以要利用这个特性，不必采用时间复杂度为O(n2)的
# 算法， 使用首尾两个指针，两个指针的数字之和与s进行判断，如果大于s，尾指针往前滑
# 如果小于s，首指针往右滑。
def find_numbers_with_sum(array, s):
    if not array or len(array) < 2:
        return None, None
    start = 0
    end = len(array)-1
    while start < end:
        if array[start] + array[end] > s:
            end -= 1
        elif array[start] + array[end] < s:
            start += 1
        else:
            return array[start], array[end]

    else:
        return None, None
