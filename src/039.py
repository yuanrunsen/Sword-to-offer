# 面试题47：礼物的最大价值
# 题目：在一个m行n列的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值
# （价值大于0）。你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或
# 者向下移动一格直到到达棋盘的右下角。给定一个棋盘及其上面的礼物，请计
# 算你最多能拿到多少价值的礼物？


# 方法1. 递归， f(i,j) = max(f(i,j-1),f(i-1,j)) + gift(i,j)
# 但是在求f(i,j-1)和f(i-1,j)的时候 中间会有重复递归 如f(i-1,j-1)
# 当gift较多时 效率会很低, 需要去重处理

# 方法2. 循环，用一个数组保存经过每个gift时 能拿到的最大价值
# 如果用 一维数组，那么只关心数组最右的元素即可
# 如果是二维数组，只关心最右下角的元素

def max_value1(gift, m, n):
    if not gift:
        return 0
    record_max = [0 for i in range(n)]
    for i in range(m):
        for j in range(n):
            forward_up = 0
            forward_left = 0
            if i > 0:
                forward_up = record_max[j]
            if j > 0:
                forward_left = record_max[j-1]

            record_max[j] = max(forward_up, forward_left) + gift[i][j]
    return record_max.pop()


# 那么 延伸出， 从矩阵的左上角到右下角 总共有多少条路径
# f(i,j) = f(i-1,j)+f(i,j+1)
# 用辅助数组保存 从起点到达每个点的路径数
def max_path(m, n):
    record_max = [1 for i in range(n)]
    for i in range(1,m):
        for j in range(0, n):
            forward_up = 0
            forward_left = 0
            if i > 0:
                forward_up = record_max[j]
            if j > 0:
                forward_left = record_max[j-1]

            record_max[j] = sum((forward_up, forward_left))
    return record_max.pop()
