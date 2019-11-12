# 面试题30：包含min函数的栈
# 题目：定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的min
# 函数。在该栈中，调用min、push及pop的时间复杂度都是O(1)。


class Stack(object):
    def __init__(self):
        self.storage = list()
        self.storage_sup = list()
        self._min = None

    def push(self, value):
        self.storage.append(value)
        if not self._min:
            self._min = value
            self.storage_sup.append(value)
        elif value <= self._min:
            self._min = value
            self.storage_sup.append(value)

    def pop(self):
        value = self.storage.pop()
        if value == self._min:
            self.storage_sup.pop()
            if self.storage_sup:
                self._min = self.storage_sup[-1]
            else:
                self._min = None
        return value

    def min(self):
        return self._min
