# 面试题18（一）：在O(1)时间删除链表结点
# 题目：给定单向链表的头指针和一个结点指针，定义一个函数在O(1)时间删除该
# 结点。

# 因为要求了时间复杂度是O（1），所以就不能进行遍历，找到要删除结点的前一个结点P
# if p->next == i
# p->next = i->next
# delete i


# 假设要删除的节点为i，可以这样
# i->value = i->next->value
# p = i->next
# i-> next = p->next
# delete p
# 这样就不用进行遍历了（前提是i确定在链表中，不然还需要遍历一遍判断i在不在链表里）

# 注意python的del只是将引用计数减一 所以delete逻辑部分会有问题，不够算法思路明确就行了。

class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


def delete_node(node):
    if node.next is None:
        del node
    else:
        next_node = node.next
        node.value = next_node.value
        node.next = next_node.next
        del next_node


# 面试题18（二）：删除链表中重复的结点
# 题目：在一个排序的链表中，如何删除重复的结点？
# 例如1,2,3,3,4,4,5 删除后为1,2,5

def delete_node2(Lnode):
    P = Lnode
    while P.next:
        if P.next.value == P.value:
            Q = P.next
            while Q.next:
                if Q.next.value == Q.value:
                    Q = Q.next
                else:
                    break
            P.value = Q.next.value
            P.next = Q.next.next
        else:
            P = P.next
