# 面试题34：二叉树中和为某一值的路径
# 题目：输入一棵二叉树和一个整数，打印出二叉树中结点值的和为输入整数的所
# 有路径。从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。


# 实际就是二叉树的遍历，不过用一个list保存经过的每一个结点，并且判断总值。
# 如果值相等，打印，并不再往该结点的下面继续，如果值大于预期值，同理。
# 只有值小于的时候才接着往下判断直到满足条件或到叶子结点结束。
# 每当一个结点访问完 就在list里删除该结点。
def serach_path(tree, nums, records=0, path=[]):
    if not tree:
        return
    value = tree.value + records

    path.append(tree.value)

    if value == nums:
        print(path)
    elif value < nums:
        if tree.right:
            serach_path(tree.right, nums, value, path)
        if tree.left:
            serach_path(tree.left, nums, value, path)

    path.pop()
