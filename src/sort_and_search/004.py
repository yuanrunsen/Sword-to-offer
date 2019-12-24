# 归并排序
def merge_sort(array, start, end):
    if not array or start is None or end is None:
        return
    # 当递归到最后只剩1个或两个元素时 排序
    if end-start <= 1:
        if array[start] > array[end]:
            array[end], array[start] = array[start], array[end]
        return start
    else:
        # 拆分递归
        mid = (start+end)//2
        start_left = merge_sort(array, start, mid)
        start_right = merge_sort(array, mid+1, end)
        # 记录原始起始坐标
        src_start_left = start_left
        # 初始化一个数组 来临时存储每段排序后的值
        # 可以优化成只初始化一次，长度与原数组相同，
        # 然后按照原数组下标进行存值
        # 就不用每次递归都重复的初始化
        temp = [0 for i in range(end-start+1)]
        temp_index = 0
        while start_left <= mid and start_right <= end:
            if array[start_left] < array[start_right]:
                temp[temp_index] = array[start_left]
                start_left += 1
            else:
                temp[temp_index] = array[start_right]
                start_right += 1

            temp_index += 1
        while start_left <= mid:
            temp[temp_index] = array[start_left]
            temp_index += 1
            start_left += 1

        while start_right <= end:
            temp[temp_index] = array[start_right]
            temp_index += 1
            start_right += 1

        # 把临时数组复制到原数组
        for i in range(len(temp)):
            array[src_start_left+i] = temp[i]

        return src_start_left


# 面试题51：数组中的逆序对
# 题目：在数组中的两个数字如果前面一个数字大于后面的数字，则这两个数字组
# 成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。

# 方法：实际上就是归并排序的应用， 区别就是 最小段里统计一次逆序对数， 较小段的时候 需要保存的不再是
# 最左边的下标， 而是最右边的下标，用大值进行比较，再保存一次逆序对数，不断的递归， 这样段内不会重复
# 段外也不会漏。
def inverse_pairs(array, start, end):
    if not array or start is None or end is None:
        return
    # 优化临时数组只初始化一次
    temp = [0 for i in range(end-start+1)]
    count = [0]
    _inverse_pairs(array, start, end, temp, count)
    return count[0]

def _inverse_pairs(array, start, end, temp, count):
    # 当递归到最后只剩1个或两个元素时 排序， 统计逆序对数
    if end-start <= 1:
        if array[start] > array[end]:
            array[end], array[start] = array[start], array[end]
            count[0] += 1
        return end
    else:
        # 拆分递归
        mid = (start+end)//2
        end_left = _inverse_pairs(array, start, mid, temp, count)
        end_right = _inverse_pairs(array, mid+1, end, temp, count)
        # 记录原始结束坐标
        src_end_right = end_right
        temp_index = end_right

        # 从大到小比较  按下标给temp赋值
        while end_left >= start and end_right >= mid+1:
            if array[end_left] > array[end_right]:
                temp[temp_index] = array[end_left]
                end_left -= 1
                count[0] += end_right-(mid+1)+1
            else:
                temp[temp_index] = array[end_right]
                end_right -= 1

            temp_index -= 1
        while end_left >= start:
            temp[temp_index] = array[end_left]
            temp_index -= 1
            end_left -= 1

        while end_right >= mid+1:
            temp[temp_index] = array[end_right]
            temp_index -= 1
            end_right -= 1

        # 把临时数组复制到原数组
        for i in range(temp_index+1, src_end_right+1):
            array[i] = temp[i]

        return src_end_right
