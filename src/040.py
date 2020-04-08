# 面试题50（一）：字符串中第一个只出现一次的字符
# 题目：在字符串中找出第一个只出现一次的字符。如输入"abaccdeff"，则输出
# 'b'。
# 面试题50（二）：字符流中第一个只出现一次的字符
# 题目：请实现一个函数用来找出字符流中第一个只出现一次的字符。例如，当从
# 字符流中只读出前两个字符"go"时，第一个只出现一次的字符是'g'。当从该字
# 符流中读出前六个字符"google"时，第一个只出现一次的字符是'l'。

# 方法1（题一）. 使用dict， 遍历字符串 统计每个字符出现的次数
# (注意 不可在统计到次数超过1时就从dict中删除
# 因为若是奇数个数，最后会导致该元素在dict里的次数为1)，
#  结束后，再次遍历字符串 结合dict 找出第一个出现一次的字符
# （不使用题二的原因是因为 由于是字符流所以只能遍历一次 无法再次遍历字符串）
from collections import OrderedDict


def search_no_repeat(strings):
    hash_map = dict()
    for s in strings:
        exists = hash_map.get(s, 0)
        if not exists:
            hash_map[s] = 1
        else:
            hash_map[s] += 1
    for s in strings:
        if hash_map[s] == 1:
            return s

# 方法2（题一、二都试用）
# 同方法1类似，不过改用python的有序字典OrderedDict
# 这样就不用再次遍历原字符串了，只用取有序字典的第一个key就可以了


def search_no_repeat2(strings):
    hash_map = OrderedDict()
    for s in strings:
        exists = hash_map.get(s, 0)
        if not exists:
            hash_map[s] = 1
        else:
            hash_map[s] += 1
    for k, v in hash_map.items():
        if v == 1:
            return k
# 顺便再说一下OrderedDict, 主要有三部分：
# 1,普通dict存储数据用
# 2.双向链表 保存每次新增数据的key， 遍历时根据链表结点对应的key从普通dict取值
# (使用双项链表是为了方便删除元素)
# 3.普通字典 key为数据字典的key,value保存链表结点，当删除元素时就可以直接找到key对应的链表
