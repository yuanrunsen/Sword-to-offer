# 面试题35：复杂链表的复制
# 题目：请实现函数ComplexListNode* Clone(ComplexListNode* pHead)，复
# 制一个复杂链表。在复杂链表中，每个结点除了有一个m_pNext指针指向下一个
# 结点外，还有一个m_pSibling 指向链表中的任意结点或者nullptr。


class Node(object):
    def __init__(self, value=None):
        self.next = None
        self.value = value
        self.sibling = None


# 使用一个map来作为辅助空间 达到O（n)的时间复杂度
def clone_nodes1(head):
    if not head:
        return None

    sibling_record = dict()  # 用一个map来保存已复制的节点 key为原结点,value为复制后的结点 .

    src_head = head  # 头结点
    res = clone_head = Node()  # 克隆链表的头结点
    clone_head.value = src_head.value
    sibling_record[src_head] = clone_head  # 保存复制前后的头结点

    if src_head.sibling is not None:  # 保存复制前后头结点的sibling
        node = Node(src_head.sibling.value)
        sibling_record[src_head.sibling] = node
        clone_head.sibling = node

    while src_head.next:
        clone_node = sibling_record.get(src_head.next, None)  # 从map里取已经保存的结点
        if not clone_node:  # 若没有则复制 并将复制完的结点保存
            clone_node = Node(src_head.next.value)
            sibling_record[src_head.next] = clone_node

        if src_head.next.sibling is not None:  # 如果该结点有sibling
            sibling_node = sibling_record.get(src_head.next.sibling, None)
            if not sibling_node:  # 判断是否已经赋值，如果已经赋值，直接使用，若无，则复制
                sibling_node = Node(src_head.next.sibling.value)
                sibling_record[src_head.next.sibling] = sibling_node
            clone_node.sibling = sibling_node

        clone_head.next = clone_node
        src_head = src_head.next
        clone_head = clone_head.next

    return res


# 通过三次循环，1.在原有的基础上复制 2.按顺序相连sibling 3.拆除
# 时间复杂度O(n)
def clone_nodes2(head):
    if not head:
        return None

    _head = head
    while _head:  # 复制结点并且将其放入原链表中 如 A->A.->B->B.->C->C.
        clone_node = Node(_head.value)
        clone_node.next = _head.next
        _head.next = clone_node
        _head = clone_node.next

    _head = head
    while _head:  # 将复制后结点的sibling相连
        if _head.sibling:
            _head.next.sibling = _head.sibling.next  # 按照顺序连就行了
        _head = _head.next.next

    _head = head
    res = clone_head = head.next
    while _head:  # 将链表拆出来
        _head.next = clone_head.next
        _head = _head.next
        if not _head:
            break
        if _head.next:
            clone_head.next = _head.next
            clone_head = clone_head.next

    return res


if __name__ == '__main__':
    A = Node('A')
    B = Node('B')
    C = Node('C')
    D = Node('D')
    E = Node('E')

    A.next = B
    B.next = C
    C.next = D
    D.next = E

    A.sibling = C
    B.sibling = E
    D.sibling = B

    clone = clone_nodes2(A)
