# 面试题42：连续子数组的最大和
# 题目：输入一个整型数组，数组里有正数也有负数。数组中一个或连续的多个整
# 数组成一个子数组。求所有子数组的和的最大值。要求时间复杂度为O(n)。
import sys
try:
    MAX_LIMIT = sys.maxint
except AttributeError:
    MAX_LIMIT = sys.maxsize


# 首先从第一个开始遍历，并且不断的累加，并且每次保存累加的最大值
# 若累加值小于零 说明 该累加值对后续元素 会造成 减量 效应
# 所以舍弃， 若大于零，则反之。遍历结束后返回最大值
def max_sub_array(array):
    if not array:
        return None
    max_sum = -MAX_LIMIT
    current_sum = 0
    for i in array:
        if current_sum <= 0:
            current_sum = i
        else:
            current_sum += i
        if current_sum > max_sum:
            max_sum = current_sum
    return max_sum
