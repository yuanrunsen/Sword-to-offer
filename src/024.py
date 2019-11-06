# 面试题25：合并两个排序的链表
# 题目：输入两个递增排序的链表，合并这两个链表并使新链表中的结点仍然是按
# 照递增排序的。例如输入图3.11中的链表1和链表2，则合并之后的升序链表如链
# 表3所示。


class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


# 方法1：
# 递归，每次只比较两个链表的头结点，取出一个较小的，然后将剩下的作为一个整体递归
def merge_list(L1, L2):
    if L1 is None:
        return L2
    if L2 is None:
        return L1

    if L1.value < L2.value:
        Head = L1
        Head.next = merge_list(L1.next, L2)

    else:
        Head = L2
        Head.next = merge_list(L1, L2.next)

    return Head


# 方法2：
# 循环,用Phead指针保存新的头结点，Head指针作为新链表的游动指针
def merge_list2(L1, L2):
    if L1 is None:
        return L2
    if L2 is None:
        return L1

    P1 = L1
    P2 = L2
    Head = None
    Phead = None

    while P2 and P1:
        if P2.value < P1.value:
            if not Head:
                Head = P2
                Phead = Head
            else:
                Head.next = P2
                Head = Head.next
            P2 = P2.next
        else:
            if not Head:
                Head = P1
                Phead = Head
            else:
                Head.next = P1
                Head = Head.next
            P1 = P1.next

    if P2 is None:
        Head.next = P1
    if P1 is None:
        Head.next = P2
    return Phead
