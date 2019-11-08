# 面试题27：二叉树的镜像
# 题目：请完成一个函数，输入一个二叉树，该函数输出它的镜像。

# 方法：实际上就是二叉树的遍历（递归循环都可以,深度广度都可以），在遍历的时候进行交换


class Node(object):
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


def mirror_tree(LNode):
    if not LNode:
        return None
    if not LNode.right and not LNode.left:
        return None
    LNode.right, LNode.left = LNode.left, LNode.right
    mirror_tree(LNode.right)
    mirror_tree(LNode.left)


def mirror_tree2(LNode):
    if not LNode:
        return None
    stack = list()
    stack.append(LNode)
    while stack:
        node = stack.pop()
        if not node.right and not node.left:
            continue
        node.right, node.left = node.left, node.right
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
