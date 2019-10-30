# 面试题21：调整数组顺序使奇数位于偶数前面
# 题目：输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有
# 奇数位于数组的前半部分，所有偶数位于数组的后半部分。

# 方法一：遍历数组，遇到偶数就把该数后面的所有数往前移一格，把该偶数放到最后一格，
# 时间复杂度为O（n2）


# 方法二：两头往中间遍历，遇到左偶右奇就交换，直到两指针相遇,O(n)
def reorder(arrary, length):
    start = 0
    end = length-1
    while True:
        while arrary[start] % 2 != 0:
            start += 1
        while arrary[end] % 2 == 0:
            end -= 1
        if start < end:
            arrary[start], arrary[end] = arrary[end], arrary[start]
        else:
            break
