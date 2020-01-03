# 面试题55（一）：二叉树的深度
# 题目：输入一棵二叉树的根结点，求该树的深度。从根结点到叶结点依次经过的
# 结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。

# 方法1 先序遍历，记录从根结点到每一个无左右子树结点的长度的值，并只比较
# 保存最大值 遍历结束后的最大值即为树的深度
# 方法2 只递归 1+max(左边，右边)


def depth_of_tree(tree):
    if not tree:
        return 0
    return 1 + max(depth_of_tree(tree.left), depth_of_tree(tree.right))