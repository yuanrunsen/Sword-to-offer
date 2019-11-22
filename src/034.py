# 面试题37：序列化二叉树
# 题目：请实现两个函数，分别用来序列化和反序列化二叉树。


class Node(object):
    def __init__(self, value=None):
        self.left = None
        self.value = value
        self.right = None


# 前序遍历 结果连同None一起保存到列表
def serialize(head, results=[]):
    if not head and not results:
        return results
    elif not head:
        results.append(None)
    else:
        results.append(head.value)
        serialize(head.left)
        serialize(head.right)
    return results


# 读取序列化列表，由于是前序遍历，那么从左到右一直遍历列表，并且不断删除列表读过的元素，
# 读到None时，说明该结点某一方向读取到了尽头。
def deserialize(results):
    if not results:
        return None
    if results[0] is None:
        results.remove(None)
        return None
    node = Node(results[0])
    results.remove(results[0])
    node.left = deserialize(results)
    node.right = deserialize(results)
    return node


if __name__ == '__main__':
    head = Node(1)
    head.left = Node(2)
    head.right = Node(3)
    head.left.left = Node(4)
    head.right.left = Node(5)
    head.right.right = Node(6)
    res=serialize(head)
    print(res)
    head = deserialize(res)