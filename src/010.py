# 面试题9：用两个队列实现栈
# 题目：用两个栈实现一个队列。请实现它的两个函数stack_push
# stack_pop，分别完成在栈的入栈和出栈。

# 方法：两个队列分别为A,B ，根据队列先进先出的特性,例如 出栈时，把A一个一个pop出队列
# 然后入到B队列，当A只剩最后一个时 就是要出栈的那个元素

# 由于python没有类似于C一样的结构体和指针，这里使用class来模拟树结点的结构体

import queue


class MyStack(object):
    def __init__(self):
        self.queue1 = queue.Queue()
        self.queue2 = queue.Queue()

    def stack_push(self, value):
        if self.queue1.qsize():
            self.queue1.put(value)
        else:
            self.queue2.put(value)

    def stack_pop(self):
        if self.queue1.qsize():
            pop_queue = self.queue1
            storage_queue = self.queue2
        else:
            pop_queue = self.queue2
            storage_queue = self.queue1
        while pop_queue.qsize() > 1:
            v = pop_queue.get()
            storage_queue.put(v)
        try:
            return pop_queue.get(False)
        except queue.Empty:
            return None
