# 面试题17：打印1到最大的n位数
# 题目：输入数字n，按顺序打印出从1最大的n位十进制数。比如输入3，则
# 打印出1、2、3一直到最大的3位数即999。


# 若不考虑数据过大导致的溢出
def print_n_1(n):
    start = 0
    end = 10 ** n
    while start < end:
        print(start)
        start += 1


# 考虑大数，即n较大，则用数组保存
# 循环法
def print_n_2(n):
    data = [0 for i in range(n)]
    start = 0
    end = 0
    while end <= n-1:
        for i in range(end, -1, -1):
            print(data[i], end='')
        print('')
        data[start] += 1
        while data[start] == 10:
            data[start] = 0
            start += 1
            if start > n-1:
                break
            data[start] += 1
        if start > end:
            end = start
        start = 0


# 递归法
def print_n_3(n, index=0, data=None):
    if index > n-1:
        return
    if not data:
        data = [0 for i in range(n)]
    for i in range(10):
        data[index] = i
        print_n_3(n, index+1, data)
        if index == n-1:
            for j in range(n):
                if data[0] != 0:
                    print(data[j], end='')
                elif data[j] != 0 or j == n-1:
                    print(data[j], end='')
            print('')
