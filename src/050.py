# 面试题59（一）：滑动窗口的最大值
# 题目：给定一个数组和滑动窗口的大小，请找出所有滑动窗口里的最大值。例如，
# 如果输入数组{2, 3, 4, 2, 6, 2, 5, 1}及滑动窗口的大小3，那么一共存在6个
# 滑动窗口，它们的最大值分别为{4, 4, 6, 6, 6, 5}


# 方法 本题可参考目录28，只不过本题相当于队列的max,28是队列的min


def max_value_in_window(window_len, array):
    # 异常处理
    if not window_len or window_len < 0 or not array or window_len > len(array):
        return None

    # 初始化， 从0开始
    window_max_sup = [array[0]]
    window_end = 0
    window_start = 0

    while True:

        # 即 窗口已经初始化完成
        if window_end - window_start == window_len - 1:
            # window_max_sup[0]就是最大值
            print(window_max_sup[0])

            # 如果滑出的值是最大值 更新滑动窗口
            if array[window_start] == window_max_sup[0]:
                window_max_sup = window_max_sup[1:]
            # 窗口前端往后滑
            window_start += 1
        # 窗口后端往后滑
        window_end += 1

        # 结束条件
        if window_end > len(array) - 1:
            break

        # not window_max_sup是为了兼顾window_len为1的情况

        # 下面当例子， 如辅助数组是（5，3，2），当前滑入数据是1，1直接添加到辅助数组尾部即可
        # 但如果当前滑入数据是4，那么数组就要更新为（5，4）
        # 当出现 比辅助数组中最小值还小时 直接加入辅助数组
        if not window_max_sup or array[window_end] <= window_max_sup[-1]:
            window_max_sup.append(array[window_end])
        else:
            # 否则 判断该数正确当截断位置
            for i in range(window_len):
                if array[window_end] > window_max_sup[i]:
                    window_max_sup = window_max_sup[:i+1]
                    window_max_sup[i] = array[window_end]
                    break

# 关于59（二）实现队列的max 此处不再写了参考28就好。
# 对于原文push时间复杂度的O（1），暂时持保留态度