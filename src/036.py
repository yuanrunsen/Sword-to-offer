# 面试题39：数组中出现次数超过一半的数字
# 题目：数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例
# 如输入一个长度为9的数组{1, 2, 3, 2, 2, 2, 5, 4, 2}。由于数字2在数组中
# 出现了5次，超过数组长度的一半，因此输出2。


def get_more_than_half(array):
    if not array:
        return None

# 若数字超过一半，那么他一定比其他所有数字的和都要多
# 所以，用一对变量来保存，某个数字的值和出现的次数
# 遍历数组，每遇到一个不同的value，counter减1
# 当counter为0时 保存下一个value
    res_value = 0
    res_counter = 0
    for i in range(len(array)):
        if res_counter == 0:
            res_value = array[i]
            res_counter = 1
        elif res_value == array[i]:
            res_counter += 1
        else:
            res_counter -= 1

# 要检查该value次数是否超过数组的一半
    check_counter = 0
    for i in range(len(array)):
        if array[i] == res_value:
            check_counter += 1
    if check_counter*2 <= len(array):
        return None

    return res_value
