# 面试题28：对称的二叉树
# 题目：请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和
# 它的镜像一样，那么它是对称的。


class Node(object):
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


def isSymmetrical2(LNode1, LNode2):
    if not LNode1 and not LNode2:
        return True
    if not LNode1 or not LNode2:
        return False
    if LNode1.value != LNode2.value:
        return False
    return isSymmetrical2(LNode1.right, LNode2.left)\
        and isSymmetrical2(LNode1.left, LNode2.right)


def isSymmetrical(LNode):
    if not LNode:
        return False
    return isSymmetrical2(LNode.right, LNode.left)


if __name__ == '__main__':
    L = Node(8)
    L.right = Node(6)
    L.left = Node(6)
    L.left.left = Node(5)
    L.left.right = Node(7)
    L.right.left = Node(7)
    L.right.right = Node(4)
    isSymmetrical(L)