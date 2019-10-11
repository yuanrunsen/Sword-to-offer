# 面试题5：合并两个有序数组 （假如都是从小到大）
# 输入1 3 5 7 ， 2 4 6 8
# 输出 1 2 3 4 5 6 7 8

# 方法一：从左到右遍历进行比较，因为是有序的，所以总共比较了O(n)次，每次比较完需要移动元素O(n)次，
# 时间复杂度为 O(n2)
# 方法二：先计算出总共需要的空间，从右向左遍历，然后从这个空间的最后往前进行复制，
# 时间复杂度 O(n)


# 方法一如下
def move(a1, start, end):
    for i in range(end, start-1, -1):
        a1[i] = a1[i-1]


def insert_array_1(a1, a2, len1, len2):
    ps = 0
    pe = len1-1
    for i in range(len2):
        for j in range(ps, pe+1):
            if a2[i] <= a1[j]:
                move(a1, j+1, pe+1)
                a1[j] = a2[i]
                pe += 1
                ps = j+1
                break
            else:
                ps = j+1
        if ps > pe:
            a1[ps] = a2[i]
            ps += 1


# 方法二如下
def insert_array_2(a1, a2, len1, len2):
    total_len = len1+len2
    pt = total_len-1
    p1 = len1-1
    for i in range(len2-1, -1, -1):
        for j in range(p1, -1 , -1):
            if a2[i] > a1[j]:
                a1[pt] = a2[i]
                pt -= 1
                break
            else:
                a1[pt] = a1[j]
                pt -= 1
                p1 -= 1
        if p1 == -1:
            a1[pt] = a2[i]
            pt -= 1


if __name__ == '__main__':
    import random
    import time
    import copy

    array_1 = list()
    array_2 = list()
    for i in range(2000):
        array_1.append(random.randint(0, 10000))
        array_2.append(random.randint(0, 10000))
    array_1.sort()
    array_2.sort()
    array_1.extend([None for i in range(2000)])

    array_3 = copy.deepcopy(array_1)
    array_4 = copy.deepcopy(array_2)

    func2_start = time.time()
    insert_array_2(array_1, array_2, 2000, 2000)
    func2_end = time.time()

    func1_start = time.time()
    insert_array_1(array_3, array_4, 2000, 2000)
    func1_end = time.time()

    print('方法2花费时间:', func2_end-func2_start)
    print('方法1花费时间:', func1_end-func1_start)
    # 方法2花费时间: 0.0020012855529785156
    # 方法1花费时间: 0.20215773582458496
