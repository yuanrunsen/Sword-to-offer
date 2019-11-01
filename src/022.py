# 面试题23：链表中环的入口结点
# 题目：一个链表中包含环，如何找出环的入口结点？


class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

# 方法：
#   首先要判断一个链表是否有环：只需要两个快慢指针，快指针一直走，
# 若链表没有环，那么走到链表尾部就停止，停止即为无环的判断条件
# 若链表有环 那么快指针将永远不会停，并且一定会在某个时刻与慢指针相遇，
# 相遇即为有环的判断条件
#   然后两指针相遇后，让其中一个指针停止，另一个指针接着运动，并且不断计数
# 直到二指针再次相遇， 计数可得链表环的长度，然后，将两个指针从链表头部开始
# 让其中一个指针先走该长度，然后再让两个指针一起运动，当二指针相遇时 就是环
# 的头部


def is_has_ring(Lnode):
    if not Lnode or not Lnode.next:
        return None
    Pahead = Lnode.next
    Pbehind = Lnode
    step = 3
    while Pahead != Pbehind:
        for i in range(step):
            if Pahead.next:
                Pahead = Pahead.next
                if Pahead == Pbehind:
                    return Pbehind
            else:
                return None
        Pbehind = Pbehind.next
    return Pahead

def get_exit(Lnode):
    meetig = is_has_ring(Lnode)
    if not meetig:
        print('no ring')
        return None
    P = meetig.next
    count = 1
    while P != meetig:
        P = P.next
        count += 1
    Pahead = Lnode
    Pbehind = Lnode
    for i in range(count):
        Pahead = Pahead.next
    while Pahead != Pbehind:
        Pahead  = Pahead.next
        Pbehind = Pbehind.next
    return Pahead.value
