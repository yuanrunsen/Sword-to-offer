# 面试题7：重建二叉树
# 题目：输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输
# 入的前序遍历和中序遍历的结果中都不含重复的数字。例如输入前序遍历序列{1,
# 2, 4, 7, 3, 5, 6, 8}和中序遍历序列{4, 7, 2, 1, 5, 3, 8, 6}，则重建出
# 图2.6所示的二叉树并输出它的头结点。

# 由于python没有类似于C一样的结构体和指针，这里使用class来模拟树结点的结构体


class Node(object):
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


# 深度优先用栈
def print_tree_by_deep(root):
    if root:
        print(root.value)
        print_tree_by_deep(root.left)
        print_tree_by_deep(root.right)


# 广度优先用队列
def print_tree_by_queue(root):
    import queue
    queue = queue.Queue()
    queue.put(root)
    while not queue.empty():
        node = queue.get()
        print(node.value)
        if node.left:
            queue.put(node.left)
        if node.right:
            queue.put(node.right)


# 方法如下,主要利用的是递归的思想
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
    right_node = rebuild_tree(pre_order[left_len+1:], in_order[right_part_start:])
    root_node.right = right_node
    return root_node


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
    print_tree_by_deep(Tree)
    print_tree_by_queue(Tree)