# 面试题8：二叉树的下一个结点
# 题目：给定一棵二叉树和其中的一个结点，如何找出中序遍历顺序的下一个结点？
# 树中的结点除了有两个分别指向左右子结点的指针以外，还有一个指向父结点的指针。

# 方法：如果该节点有右节点，那么右节点的最左节点即为所求
# 如果没有右节点，那么判断该节点是不是它父节点的左子节点 如果是 父节点即为所求
# 如果以上都不满足 就要不断的向它的父节点，以及父节点的父节点寻找，知道找到一个节点
# 满足该节点是它父节点的左子节点
# 若都不满足 则没有下一个节点

# 由于python没有类似于C一样的结构体和指针，这里使用class来模拟树结点的结构体

nodes = []


class Node(object):
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
        self.parent = None


# 深度优先用栈 中序遍历
def record_nodes(root):
    global nodes
    if root:
        record_nodes(root.left)
        nodes.append(root)
        record_nodes(root.right)


# 借助上一题的构建二叉树的逻辑 就不重新写 新建二叉树的代码了
def rebuild_tree(pre_order, in_order):
    if not pre_order or not in_order:
        return None

    root_value = pre_order[0]

    left_part_end = in_order.index(root_value)-1
    left_part_start = 0
    left_len = left_part_end - left_part_start + 1

    right_part_start = left_part_end+2

    root_node = Node(root_value)
    left_node = rebuild_tree(pre_order[1:left_len+1], in_order[left_part_start:left_part_end+1])
    root_node.left = left_node

    if left_node:
        left_node.parent = root_node

    right_node = rebuild_tree(pre_order[left_len+1:], in_order[right_part_start:])
    root_node.right = right_node

    if right_node:
        right_node.parent = root_node

    return root_node


# 方法如下
def get_next(node):
    if node.right:
        node = node.right
        while node.left:
            node = node.left
        return node
    try:
        if node == node.parent.left:
            return node.parent
        else:
            while node.parent != node.parent.parent.left:
                node = node.parent
            return node.parent.parent
    except AttributeError:
        return None


if __name__ == '__main__':
    pre_order = [1, 2, 4, 7, 3, 5, 6, 8]
    in_order = [4, 7, 2, 1, 5, 3, 8, 6]

    # pre_order = [1, 2, 3, 4, 5]
    # in_order = [1, 2, 3, 4, 5]
    # pre_order = [1, 2, 3, 4, 5]
    # in_order = [5, 4, 3, 2, 1]
    # pre_order = [1, 2, 4, 5, 3, 6, 7]
    # in_order = [4, 2, 5, 1, 6, 3, 7]

    Tree = rebuild_tree(pre_order, in_order)
    record_nodes(Tree)

    for i in range(len(nodes)):
        next_node = get_next(nodes[i])
        if i != (len(nodes)-1):
            if next_node != nodes[i+1]:
                print('Error node {}'.format(nodes[i].value))
            else:
                print('{}的下一个节点是：{}'.format(nodes[i].value, nodes[i+1].value))
        else:
            if next_node != None:
                print('Error node {}'.format(nodes[i].value))
            else:
                print('{}的下一个节点是：{}'.format(nodes[i].value, None))
