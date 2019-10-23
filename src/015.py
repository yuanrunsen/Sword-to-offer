# 面试题14：剪绳子
# 题目：给你一根长度为n绳子，请把绳子剪成m段（m、n都是整数，n>1并且m>1）。
# 每段的绳子的长度记为k[0]、k[1]、……、k[m]。k[0]*k[1]*…*k[m]可能的最大乘
# 积是多少？例如当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此
# 时得到最大的乘积18。

# 动态规划
# 动态规划有四个特点：
# 1.要求求一个问题的最优解
# 2.整体问题的最优解依赖于各个子问题的最优解
# 3.把整体问题分解成若干个子问题，这些子问题之间还有相互重叠的更小的子问题
# 4.由于子问题有重叠，那么采取从子问题到大问题的由下而上的解决方法，并把已经解决的问题存储下来以免重复求解


# 递归,用visited变保存以避免重复
def get_max(length, visited=dict(), is_main=True):
    if is_main:
        if length == 2:
            return 1
        if length == 3:
            return 2
    else:
        if length < 4:
            return length
    if not visited.get(length, None):
        max_value = 0
        for i in range(1, length//2+1):
            value = get_max(length-i, visited, False) * get_max(i, visited, False)
            if value > max_value:
                max_value = value
        visited[length] = max_value
    return visited[length]


# 动态规划,循环由小算到大
def get_max2(length):
    if length == 2:
        return 1
    if length == 3:
        return 2
    visited = dict()
    visited[1] = 1
    visited[2] = 2
    visited[3] = 3
    for i in range(4, length+1):
        max_value = 0
        for j in range(1, i//2+1):
            value = visited[i-j] * visited[j]
            if value > max_value:
                max_value = value
        visited[i] = max_value
    return visited[length]


# 贪婪算法，尽可能取长度为3的小段
def get_max3(length):
    import math
    if length == 2:
        return 1
    if length == 3:
        return 2
    if length == 4:
        return 4
    _num_3 = length//3
    _num_ = length - _num_3*3 or 1
    return int(math.pow(3, _num_3) * _num_)
