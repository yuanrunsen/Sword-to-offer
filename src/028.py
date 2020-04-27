# 面试题30：包含min函数的栈
# 题目：定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的min
# 函数。在该栈中，调用min、push及pop的时间复杂度都是O(1)。


class Stack(object):
    def __init__(self):
        self.storage = list()
        self.storage_sup = list()

    def push(self, value):
        self.storage.append(value)
        if not self.storage_sup:
            self.storage_sup.append(value)
        elif value <= self.storage_sup[-1]:
            self.storage_sup.append(value)

    def pop(self):
        value = self.storage.pop()
        if value == self.storage_sup[-1]:
            self.storage_sup.pop()
        return value

    def min(self):
        # 栈顶元素永远是最小值
        if not self.storage_sup:
            return None
        return self.storage_sup[-1]


# 面试题30(自定义)：包含min函数的队列
# 题目：定义队列的数据结构，请在该类型中实现一个能够得到队列的最小元素的min
# 函数。在该栈中，调用min，的时间复杂度都是O(1)。
import queue


class Queue(object):
    def __init__(self):
        self.storage = queue.Queue()
        self.storage_sup = list()

    def put(self, value):
        self.storage.put(value)
        if not self.storage_sup:
            self.storage_sup.append(value)
        else:
            if value >= self.storage_sup[-1]:
                self.storage_sup.append(value)
            else:
                # 按顺序插入 并且删除其后的元素
                # 例如 3 4 5 6 7 5的队列， 其最小值不可能比5还大
                # 那么 这里的辅助数组只用保存3 4 5即可
                # 下面的for循环就是做了这个事情
                for i in range(len(self.storage_sup)):
                    if self.storage_sup[i] > value:
                        self.storage_sup = self.storage_sup[:i+1]
                        self.storage_sup[-1] = value
                        break

    def get(self):
        value = self.storage.get()
        if value == self.storage_sup[0]:
            self.storage_sup = self.storage_sup[1:]
        return value

    def min(self):
        # 队首元素永远是最小值
        if not self.storage_sup:
            return None
        return self.storage_sup[0]

