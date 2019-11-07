# 面试题26：判断一棵树是否为另一棵树的子树
# 题目：输入两棵二叉树A和B，判断B是不是A的子结构。

# 方法：遍历A（递归，循环都可以），每访问一个结点就判断是否和B的根结点一致，若不一致
# 接着判断A的下一个结点（直至遍历结束），若一致，则判断同时遍历该节点和B子树的所有后续节点，
# 若完全一致 则返回True 否则 重复之前的步骤(直至遍历A结束)


class Node(object):
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


def check_trees(T1, T2):
    if not T2:
        return True
    if not T1:
        return False
    if T1.value == T2.value:
        result_right = check_trees(T1.right, T2.right)
        result_left = check_trees(T1.left, T2.left)
        return result_left and result_right
    else:
        return False


def check_tree(T1, T2):
    if not T1 or not T2:
        return False
    if T1.value == T2.value:
        result = check_trees(T1, T2)
        if result:
            return result
    result = check_tree(T1.right, T2)
    if not result:
        result = check_tree(T1.left, T2)
    return result


# 这两种写法都可以， 第二个看着优雅一点，第一个好理解一点
def check_tree(T1, T2):
    if not T1 or not T2:
        return False
    result = check_trees(T1, T2)
    if not result:
        result = check_tree(T1.right, T2)
        if not result:
            result = check_tree(T1.left, T2)
    return result
