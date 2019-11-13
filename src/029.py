# 面试题33：二叉搜索树的后序遍历序列
# 题目：输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
# 如果是则返回true，否则返回false。假设输入的数组的任意两个数字都互不相同。


def verify_bst(array):
    if not array:
        return False

    if len(array) <= 2:  # 长度为2，不论是怎样，都一定满足条件
        return True

    root = array[-1]

    small = 0
    for small in range(len(array)-1):
        if array[small] > root:
            small -= 1
            break

    large = None
    for large in range(small+1, len(array)-1):
        if array[large] < root:
            return False

    if not large:  # 当没有右子树的时候large为None
        right = True
    else:
        right = verify_bst(array[small+1:large+1])

    if small <= 0:
        left = True
    else:
        left = verify_bst(array[:small+1])

    return left and right
