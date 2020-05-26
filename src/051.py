# 面试题60：n个骰子的点数
# 题目：把n个骰子扔在地上，所有骰子朝上一面的点数之和为s。输入n，打印出s
# 的所有可能的值出现的次数


# 方法(1): 递归，假设总共有n个骰子，那么可以把这n个骰子分为1和n-1两堆，把n-1那堆看成
# 一个新的具有新的最大值，最小值，和每个值出现次数不等的特殊的骰子， 将这一个骰子和这个
# 特殊的骰子进行排列组合即可，这n-1一个即为递归的概念

# 假设普通的骰子 是大小由1到6的六面骰子

def probability(nums):
    if nums == 1:
        # 返回普通骰子
        return 1, 6, {'1': 1, '2': 1, '3': 1, '4': 1, '5': 1, '6': 1}

    # 返回n-1特殊骰子
    _min, _max, res = probability(nums - 1)

    # 进行普通骰子和特殊骰子的排列组合
    new_res = {}
    for i in range(1, 6+1):
        for j in range(_min, _max+1):
            _index = str(i+j)
            if _index not in new_res:
                new_res[_index] = res[str(j)]
            else:
                new_res[_index] += res[str(j)]

    # 返回新的特殊骰子的最小值和最大值以及其每个数字出现的次数
    return _min+1, _max+6, new_res


# 方法(2): 每增加一个普通骰子（点数1-6） 点数和的最小值就会+1，最大值会+6
# 从最大值到最小值中的任意数值假设为n， 那么每新增一个骰子，n的值就会变成
# 当前n-1 + n-2 + n-3 + n-4 + n-5 + n-6的值的和（最大值> item > 最小值）

def probability2(nums):
    for num in range(nums):
        # 1个骰子时：
        if num == 0:
            res = {'1': 1, '2': 1, '3': 1, '4': 1, '5': 1, '6': 1}
            _min = 1
            _max = 6
        # 每增加一个骰子：
        else:
            # 设置新的最大最小值
            new_res = {}
            new_min = _min + 1
            new_max = _max + 6
            # 每个新的值n都等于旧的值由n-1 + 到 n-6
            for n in range(new_min, new_max+1):
                if str(n) not in new_res:
                    # 初始化为0
                    new_res[str(n)] = 0
                _n = n
                # 由n-1 + 到 n-6
                # 从大往小加
                while _n - 1 >= n - 6:
                    _n -= 1
                    # 超过旧值的最大值时 跳过
                    if _n > _max:
                        continue
                    # 小过旧值的最小值时 直接结束
                    if _n < _min:
                        break
                    new_res[str(n)] += res[str(_n)]

            # 更新 当前最大小值和结果
            _min = new_min
            _max = new_max
            res = new_res

    return _min, _max, res