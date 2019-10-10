# 面试题5：替换空格
# 题目：请实现一个函数，把字符串中的每个空格替换成"%20"。例如输入“We are happy.”，
# 则输出“We%20are%20happy.”。

# 方法一：从左到右遍历，遇到空格就把后面部分往右移动，并替换空格，那么每有一个空格 最后一个空格右边的字符就得移动一次，
# 如果有n个空格，第n个空格的右边字符就得移动n次，第n-1个空格右边的空格就得移动n-1一次，那么总计是 1+2+.....+n
# 等差数列求和，则时间复杂度为 O(n2)
# 方法二：先遍历一次统计总共有多少个空格，然后计算出总共需要的空间，然后从这个空间的最后往前进行复制，
# 当遇到空格时进行替换，则时间复杂度 O(n)


# 方法二如下（python里内置函数比较多，而且字符串为常量，这里用列表进行替代）
# 其实相当于数组内的字符移动
def replace_str(str_array, length, new_block='%20'):
    blank_counters = 0
    for s in str_array:
        if s == ' ':
            blank_counters += 1
        if s is None:
            break
    new_length = length+blank_counters*2
    p1 = length-1
    p2 = new_length-1
    while p1 != p2:
        if str_array[p1] != ' ':
            str_array[p2] = str_array[p1]
            p2 -= 1
            p1 -= 1
        else:
            for i in range(len(new_block)-1, -1, -1):
                str_array[p2] = new_block[i]
                p2 -= 1
            p1 -= 1


if __name__ == '__main__':
    str_array = [None for i in range(50)]
    value = 'we are happy'
    length = len(value)
    for i in range(length):
        str_array[i] = value[i]
    replace_str(str_array, length)
    print(str_array)
