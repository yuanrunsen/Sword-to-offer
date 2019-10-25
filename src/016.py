# 面试题16：数值的整数次方
# 题目：实现函数double Power(double base, int exponent)，求base的exponent
# 次方。不得使用库函数，同时不需要考虑大数问题。

# 解析：
# a(n) = a(n/2) * a(n/2) 指数n为偶数时
# a(n) = a(n-1/2) * a(n-1/2) * a 指数n为奇数时


# 循环法 不断改变底数让其等于自身的平方，当遇到指数为奇数时如9
# 用一个变量保存此时底数的1次方，然后接着求此时底数的8次方
# 最后将该变量与次数的底数相乘即可
def my_power(base, exponent):
    if exponent == 0:
        return 1
    if exponent < 0:
        exponent = -exponent
        base = 1/base
    res = 1.0
    while exponent > 0:
        if exponent % 2 == 1:
            res *= base
        base *= base
        exponent = exponent//2
    return res


# 递归法
def my_power2(base, exponent):
    if exponent == 0:
        return 1
    if exponent == 1:
        return base
    if exponent < 0:
        exponent = -exponent
        base = 1/base
    if exponent % 2 == 0:
        res = my_power2(base, exponent//2)
        res *= res
    else:
        res = my_power2(base, (exponent-1)//2)
        res *= res
        res *= base
    return res
