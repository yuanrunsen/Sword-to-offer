# 面试题36：二叉搜索树与双向链表
# 题目：输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求
# 不能创建任何新的结点，只能调整树中结点指针的指向。


class Node(object):
    def __init__(self, value=None):
        self.left = None
        self.value = value
        self.right = None


# 二叉搜索树 本身就是有序的，中序遍历即可保持顺序的遍历
# 中序遍历， 使用一个link指针把遍历到的结点串起来即可。
# 注意的是 这个link一定要使用 引用类型的（二级指针）
def convert(node, link=[]):
    if not node:
        return

    convert(node.left, link)
    if not link:
        link.append(node)
    else:
        link[0].right = node
        node.left = link[0]
        link[0] = link[0].right
    convert(node.right, link)

    return link[0]


if __name__ == '__main__':
    head = Node(10)
    head.left = Node(6)
    head.right = Node(14)
    head.left.left = Node(4)
    head.left.right = Node(8)
    head.right.left = Node(12)
    head.right.right = Node(16)
    head = convert(head)
    while head != None:
        print(head.value)
        head = head.left