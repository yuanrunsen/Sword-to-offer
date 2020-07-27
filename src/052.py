# 面试题60：扑克牌中的顺子
# 题目：从扑克牌中随机抽5张牌，判断是不是一个顺子，即这5张牌是不是连续的。
# 2〜10为数字本身，A为1，J为11，Q为12，K为13，而大、小王可以看成任意数字。


# 方法: 其实本题基本等价于 5个随机数经排序后每相邻两个数的间隔是否为1
# 不过在此基础上加入了任意数的概念，也就是说，两个数的间隔如果不为一的时候
# 相差的数可以由任意数来代替，除此之外还要考虑两数相当的情况。

# 把大小王定义为0


KING = 0


def is_continuous(nums):
    if not nums:
        return False
    nums = list(nums)
    nums.sort()
    any_num = 0
    gap = 0
    start = 0
    end = len(nums) - 1
    while start < end:
        # 由于大小王是0 那么排序后是在最左端
        if nums[start] == KING:
            any_num += 1
        elif nums[start+1] == nums[start]:
            return False
        else:
            gap += nums[start+1] - nums[start] - 1

        start += 1

    if any_num >= gap:
        return True
    else:
        return False
