# 面试题57（二）：和为s的连续正数序列
# 题目：输入一个正数s，打印出所有和为s的连续正数序列（至少含有两个数）。
# 例如输入15，由于1+2+3+4+5=4+5+6=7+8=15，所以结果打印出3个连续序列1〜5、
# 4〜6和7〜8。

# 方法：由于是连续数列，那么这个数列最小是1～2，把数列的最左端点叫做a, 最右端点叫做b，
# 以这个数列为起始数列 若序列的和小于s 将b增加1，即扩大数列的右端点， 若序列和大于s
# 将a增加1，即缩小数列的左端点


def find_continuous_sequence(s):
    if s < 3:
        return None, None
    start = 1
    end = 2
    res = start + end
    while start < end:
        # 这里不必每次都计算
        # res = 0
        # for i in range(start, end+1):
        #     res += i
        if res < s:
            end += 1
            res += end
        elif res > s:
            res -= start
            start += 1
        else:
            print_sequence(start, end)
            res -= start
            start += 1
            end += 1
            res += end


def print_sequence(start, end):
    for j in range(start, end + 1):
        print(j, ' ', end='')
    print()
