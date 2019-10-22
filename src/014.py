# 面试题13：机器人的运动范围
# 题目：地上有一个m行n列的方格。一个机器人从坐标(0, 0)的格子开始移动，它
# 每一次可以向左、右、上、下移动一格，但不能进入行坐标和列坐标的数位之和
# 大于k的格子。例如，当k为18时，机器人能够进入方格(35, 37)，因为3+5+3+7=18。
# 但它不能进入方格(35, 38)，因为3+5+3+8=19。请问该机器人能够到达多少个格子？


def get_k(col, row):
    k = 0
    col = str(col)
    row = str(row)
    for c in col:
        k += int(c)
    for r in row:
        k += int(r)
    return k


def robot_move(matrix, row, col, visited, rows, cols, k):
    if row > rows or col > cols or row < 0 or col < 0:
        return
    _k = get_k(row, col)
    if _k <= k and (row, col) not in visited:
        visited.add((row, col))
        robot_move(matrix, row, col+1, visited, rows, cols, k)
        robot_move(matrix, row, col-1, visited, rows, cols, k)
        robot_move(matrix, row-1, col, visited, rows, cols, k)
        robot_move(matrix, row+1, col, visited, rows, cols, k)


def start_move(matrix, rows, cols, k):
    visited = set()
    robot_move(matrix, 0, 0, visited, rows, cols, k)
    return visited


if __name__ == '__main__':
    matrix = [[j for j in range(10)] for i in range(10)]
    row_col_record = start_move(matrix, 10, 10, 5)
    print('机器人能到达的坐标：', row_col_record)  # 无序
    print('机器人能到达的坐标总和：', len(row_col_record))
