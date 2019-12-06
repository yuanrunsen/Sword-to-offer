# 面试题40：最小的k个数
# 题目：输入n个整数，找出其中最小的k个数。例如输入4、5、1、6、2、7、3、8
# 这8个数字，则最小的4个数字是1、2、3、4。

# 方法：1.如果使用快速排序 先排序然后再取值 时间复杂度是nlogn
# 方法：2.如果使用快速排序的部分思路，判断返回的index和k的关系
# 决定递归的区间，时间复杂度是n，但会改变原数组
# 方法：3.用一个数据结构来维护K个值，每次从n个整数中读取一个数，并判断是否小于这K个数中的最大值
# 如果不满足条件则舍弃，如满足则删除最大值，插入这个读取到的数，并选出新的最大值
# 这个数据结构可以是线性的如：数组，链表，也可以是二叉树类型的数据结构：堆，红黑树等等
# 使用线性结构 就不用维护一个最大值了 因为不管怎么样 都得遍历一遍 时间复杂度是n
# 使用树的结构，如平衡二叉树或堆，他们的查找效率比一般的二叉树高，时间复杂度仅为logn
# 并且本身具有一定的顺序，这里 采用最大堆，因为最大堆取最大值的时间复杂度为 1，插入为logn

# 由于python只有最小堆，这里采用最小堆取反来模拟最大堆

import heapq


def get_least_numbers(alist, k):
    max_heap = []
    length = len(alist)
    if not alist or k <= 0 or k > length:
        return
    for ele in alist:
        ele = -ele
        if len(max_heap) < k:
            heapq.heappush(max_heap, ele)

        else:
            heapq.heappushpop(max_heap, ele)

    return map(lambda x:-x, max_heap)
