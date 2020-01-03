# 面试题55（二）：平衡二叉树
# 题目：输入一棵二叉排序树的根结点，判断该树是不是平衡二叉树。如果某二叉树中
# 任意结点的左右子树的深度相差不超过1，那么它就是一棵平衡二叉树。

# 方法1，求每个结点的左右子树的深度，进行判断


def depth_of_tree(tree):
    if not tree:
        return 0
    return 1 + max(depth_of_tree(tree.left), depth_of_tree(tree.right))


def is_avl_tree(tree):
    # 先求根结点的左右子树的高度差
    left_depth = depth_of_tree(tree.left)
    right_depth = depth_of_tree(tree.right)
    gap = left_depth - right_depth
    if gap > 1:
        return False
    # 再求每个结点的左右子树的高度差
    return depth_of_tree(tree.left) and depth_of_tree(tree.right)
# 这种做法的缺点就是 重复遍历了很多结点


# 方法2 在遍历的途中 就对每个结点的左右子树进行判断
# 如果是平衡二叉树则返回树的高度， 如果不是 则返回-1
def is_avl_tree2(tree):
    if not tree:
        return 0
    # if not tree.left and not tree.right:
    #     return 1
    left_depth = is_avl_tree2(tree.left)
    if left_depth == -1:
        return -1
    right_depth = is_avl_tree2(tree.right)
    if right_depth == -1:
        return -1
    # if -1 in (left_depth, right_depth):
    #     return -1
    gap = left_depth - right_depth
    if gap not in (0, 1, -1):
        return -1
    else:
        return 1 + max(left_depth, right_depth)
