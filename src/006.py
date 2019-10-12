# 面试题6：从尾到头打印链表
# 题目：输入一个链表的头结点，从尾到头反过来打印出每个结点的值

# 方法一：将结点指针反转，反转链表，再从头到尾打印即可（详情见后续章节）
# 方法二：正向遍历，使用栈的数据结构来保存每个结点的指针或值，然后再pop出去即可
# 方法三：递归，函数的递归本质就是栈的结构，既然可以用方法二，那么就可以用递归
# 注意就是当结点的个数较多时，递归会变得很慢

# 由于python没有类似于C一样的结构体和指针，这里使用class来模拟
# 用list来模拟栈的数据结构


class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


# 方法二如下
def print_list_reverse_1(LNode):
    P = LNode
    Stack = list()
    while P:
        Stack.append(P)
        P = P.next
    while Stack:
        node = Stack.pop()
        print(node.value)


# 方法三如下
def print_list_reverse_2(LNode):
    P = LNode
    if P.next:
        print_list_reverse_2(P.next)
    print(P.value)


if __name__ == '__main__':
    LNode = Node(-1)
    P = LNode
    for i in range(10):
        node = Node(i)
        P.next = node
        P = P.next

    print_list_reverse_1(LNode)
    print_list_reverse_2(LNode)