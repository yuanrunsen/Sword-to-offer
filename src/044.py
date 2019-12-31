# 面试题54：二叉搜索树的第k个结点
# 题目：给定一棵二叉搜索树，请找出其中的第k大的结点。
# k从1开始计数

# 二叉搜索树 也是二叉排序树，本身有序，中序遍历即可。


def _k_in_tree(tree, k):
    if tree.left:
        node = _k_in_tree(tree.left, k)
        if node:
            return node

    k[0] -= 1
    if k[0] == 0:
        return tree

    if tree.right:
        node = _k_in_tree(tree.right, k)
        return node

# 有时间可以想一想 如果是倒数第K个结点的解法
