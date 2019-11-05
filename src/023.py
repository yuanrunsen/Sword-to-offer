# 面试题24：反转链表
# 题目：定义一个函数，输入一个链表的头结点，反转该链表并输出反转后链表的
# 头结点。


class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

# 方法：
# 使用三个指针 分别保存某个结点以及它的前驱和后继结点
# 由前到后分别为a,b,c.当b.next=a后，将a=b,b=c,c=c.next不断重复即可
# 要注意为空的判断


def reverse_list(Lnode):
    if Lnode is None:
        return None
    ahead = Lnode
    if ahead.next:
        mid = ahead.next
    else:
        return ahead

    while mid.next:
        behind = mid.next
        mid.next = ahead
        ahead = mid
        mid = behind
    mid.next = ahead
    Lnode.next = None
    return mid
