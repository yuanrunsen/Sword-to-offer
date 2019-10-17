# 面试题11：青蛙跳台阶问题
# 题目：一只青蛙一次可以跳上1个台阶，也可以跳上2个台阶，求跳上N个台阶有多少种跳法


# 先写一下斐波切纳的算法


# 递归， 效率低
def get_feib(n):
    if n >= 2:
        return get_feib(n-1) + get_feib(n-2)
    elif n in (1, 0):
        return n


# 循环, 效率较递归高，但仍有重复计算
def get_feib2(n):
    if n in (1, 0):
        return n
    f0 = 0
    f1 = 1
    for i in range(n-1):
        f0, f1 = f1, f0+f1
    return f1


# 生成器
def get_feib3(n):
    i = 0
    j = 1
    while n > 0:
        yield i
        i, j = j, j + i
        n -= 1

# 方法：假设n层台阶的跳法总共有f(n)种
# 青蛙第一次跳，要么跳两个台阶，要么跳一个台阶
# 那么 f(n) = f(n-1) + f(n-2)
# 特殊的，当n<2时只有一种跳法，当n=2时有两种跳法


def get_jump(n):
    f0 = 1
    f1 = 2
    for i in range(n-2):
        f0, f1 = f1, f0+f1
    return f1


def leapfrog_jump(n):
    if n in (1, 2):
        return n
    else:
        return get_jump(n)


if __name__ == '__main__':
    print(leapfrog_jump(5))
