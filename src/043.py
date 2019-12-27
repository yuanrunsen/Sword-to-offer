# 面试题53（二）：0到n-1中缺失的数字
# 题目：一个长度为n的递增排序数组中的所有数字都是唯一的，
# 找出数组中第一个值和下标不相等的元素

# 方法： 假设数组长度已知，由于是有序数组 考虑使用二分法查找,
# 此题等价于找出数组中第一个值和下标不相等的元素

# 找起始下标时 判断二分查找的中间值若是与下标相等，则在右半部分查找
# 若是与下标不相等，则判断其左边的元素是否与下标相等，若不相等则在左半边查找,
# 若相等 则即为所求


# 循环版二分查找
def get_missing_number(array, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == mid:
            start = mid+1
        else:
            if array[mid-1] == mid-1:
                return mid
            end = mid-1

# 若全都不与下标相等
    if end < 0:
        return 0
# 若全都与下标相等
    else:
        return None

