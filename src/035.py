# 面试题38：字符串的排列
# 题目：输入一个字符串，打印出该字符串中字符的所有排列。例如输入字符串abc，
# 则打印出由字符a、b、c所能排列出来的所有字符串abc、acb、bac、bca、cab和cba。


def sort_all(array, start=0):
    length = len(array)
    if start == length-1:
        print(''.join(array))

    for i in range(start, length):
        array[i], array[start] = array[start], array[i]
        sort_all(array, start+1)
        array[i], array[start] = array[start], array[i]

# 由此题可以引申出另外两题
# 1.八皇后问题
# 2.矩形对立面顶点和的问题
# 实际上都是数列的全排列， 只不过在最后输出之前加一个判断的逻辑
