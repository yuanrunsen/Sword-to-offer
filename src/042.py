# 面试题53（一）：数字在排序数组中出现的次数
# 题目：统计一个数字在排序数组中出现的次数。例如输入排序数组{1, 2, 3, 3,
# 3, 3, 4, 5}和数字3，由于3在这个数组中出现了4次，因此输出4。

# 方法： 假设数组长度已知，由于是有序数组 考虑使用二分法查找,
# 找到该数字的起始下标 和该数字的终止下标即知道总共出现了多少次

# 找起始下标时 判断二分查找的中间值若是小于该数字，则再右半部分查找
# 如是大于该数组 则再左半部分查找，若是等于 则判断该数字的前一个数字
# 前一个数字若是与该数字相等 那么 在前半部分查找， 若是不相等
# 则该数字的下标就是起始下标

# 找终止下标类似 判断二分查找的中间值若是小于该数字，则再右半部分查找
# 如是大于该数组 则再左半部分查找，若是等于 则判断该数字的后一个数字
# 后一个数字若是与该数字相等 那么 在后半部分查找， 若是不相等
# 则该数字的下标就是终止下标


# 递归版二分查找
def get_k_left(array, start, end, k):
    mid = (start + end) // 2
    # 边界判断
    if start > end:
        return None
    if start == end:
        if array[mid] == k:
            return mid
        else:
            return None

    if array[mid] < k:
        return get_k_left(array, mid+1, end, k)
    elif array[mid] > k:
        return get_k_left(array, start, mid-1, k)
    else:
        if array[mid-1] != k:
            return mid
        else:
            return get_k_left(array, start, mid-1, k)


def get_k_right(array, start, end, k):
    mid = (start + end) // 2
    # 边界判断
    if start > end:
        return None
    if start == end:
        if array[mid] == k:
            return mid
        else:
            return None

    if array[mid] < k:
        return get_k_right(array, mid+1, end, k)
    elif array[mid] > k:
        return get_k_right(array, start, mid-1, k)
    else:
        if array[mid+1] != k:
            return mid
        else:
            return get_k_right(array, mid+1, end, k)


def get_k(array, start, end, k):
    left = get_k_left(array, start, end, k)
    right = get_k_right(array, start, end, k)
    length = right - left + 1
    return length
