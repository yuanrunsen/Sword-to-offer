# 回溯法查找

# 面试题12：矩阵中的路径
# 题目：请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有
# 字符的路径。路径可以从矩阵中任意一格开始，每一步可以在矩阵中向左、右、
# 上、下移动一格。如果一条路径经过了矩阵的某一格，那么该路径不能再次进入
# 该格子。例如在下面的3×4的矩阵中包含一条字符串“bfce”的路径（路径中的字
# 母用下划线标出）。但矩阵中不包含字符串“abfb”的路径，因为字符串的第一个
# 字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入这个格子。


# 方法：回溯法，并且设置一个变量 来保存已经到达的地方 以免重复回溯

from collections import OrderedDict


def search_str(matrix, row, col, strs, visited, rows, cols, str_index):
    if str_index == len(strs):
        return True
    if row > rows or col > cols or row < 0 or col < 0:
        return False
    _in = False
    if matrix[row][col] == strs[str_index] and not visited.get((row, col), False):
        visited[(row, col)] = True
        _in_1 = search_str(matrix, row, col+1, strs, visited, rows, cols, str_index=str_index+1)
        _in_2 = search_str(matrix, row, col-1, strs, visited, rows, cols, str_index=str_index+1)
        _in_3 = search_str(matrix, row-1, col, strs, visited, rows, cols, str_index=str_index+1)
        _in_4 = search_str(matrix, row+1, col, strs, visited, rows, cols, str_index=str_index+1)
        _in = _in_1 or _in_2 or _in_3 or _in_4
        if not _in:
            del visited[(row, col)]
    return _in


def search_path_matrix(matrix, strs, rows, cols):
    visited = OrderedDict()
    for row in range(rows):
        for col in range(cols):
            _in = search_str(matrix, row, col, strs, visited, rows, cols, str_index=0)
            if _in:
                return list(visited.keys())
    return None


if __name__ == '__main__':
    matrix = [['a', 'b', 't', 'g'],
              ['c', 'f', 'c', 's'],
              ['q', 'd', 'e', 'h']]
    print('字符串在矩阵中的路径：', search_path_matrix(matrix, 'bfce', 3, 4))
