# 面试题52：两个链表的第一个公共结点
# 题目：输入两个链表，找出它们的第一个公共结点。

# 方法1： 分别遍历两个链表，把他们放到一个栈里， 然后一起不断的pop 并判断
# 直到出现不相等，则最后一次相等的结点就是第一个公共结点
# 时间复杂度是o（m+n），空间复杂度是o(m+n)

# 方法2： 遍历其中一个链表， 把它的每个结点加到一个集合中
# 再遍历第二个链表 并且判断结点是否在集合里， 直到出现第一个
# 在集合里的结点， 就是第一个公共结点， 判断是否在集合的时间复杂度是o(1)
# 空间复杂度是o(m)或者o（n), 整体的时间复杂度是o(m+n)

# 方法3： 遍历两个链表，分别求出两个链表的长度, 然后取两个链表相同长度的位置
# 作为起始位置，一起遍历  并判断是否两结点相同 若相同则是公共结点，时间复杂度是
# o(m+n) 空间复杂度是o(1)


class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


# 方法3
def first_common_node(list1, list2):
    if not list1 or not list2:
        return None
    l1, l2 = list1, list2
    count1 = count2 = 0
    while list1:
        count1 += 1
        list1 = list1.next
    while list2:
        count2 += 1
        list2 = list2.next

    gap = abs(count1 - count2)
    for i in range(gap):
        if count1 > count2:
            l1 = l1.next
        else:
            l2 = l2.next

    while l1 and l2:
        if l1 == l2:
            return l1
        else:
            l1 = l1.next
            l2 = l2.next
    else:
        return None
