# 面试题9：用两个栈实现队列
# 题目：用两个栈实现一个队列。请实现它的两个函数queue_in
# 和queue_out，分别完成在队列尾部插入结点和在队列头部删除结点的功能。

# 方法：两个栈分别为A,B,利用栈后入先出的特性，入栈的时候入A栈，出栈的时候B栈为空时
# 将A POP到 B  再POP B即可，B栈不为空时直接POP B

# 由于python没有类似于C一样的结构体和指针，这里使用class来模拟树结点的结构体


class MyQueue(object):
    def __init__(self):
        self.stack1 = list()
        self.stack2 = list()

    def queue_in(self, value):
        self.stack1.append(value)

    def queue_out(self):
        if self.stack2:
            return self.stack2.pop()
        else:
            while self.stack1:
                v = self.stack1.pop()
                self.stack2.append(v)
            return self.stack2.pop()
