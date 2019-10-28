# 面试题16：正数的开平方


# 只考虑了n为正数的情况
def sqrt_bi(n):
    low = 0   # 设置下限为0
    high = max(n, 1)   # 设置上限为n和1之中的最大数，即：如果n>=1，那么上限为n；如果n<1，那么上限为1
    # 注意n为小数时，上限high将不再是n而是1
    guess = (low+high)/2   # 先从中间值开始猜
    accuracy = 0.00000000000000000001
    count = 1   # 设置猜测次数起始值为1
    while abs(guess**2-n) > accuracy and count < 100:
        # 当猜测值的平方和n本身的差值无限接近误差值时，循环才会停止；同时设置猜测次数不超过100次
        if guess**2 < n:  # 如果猜测值的平方小于n，那么将此设为下限
            low = guess
        else:           # 如果猜测值的平方大于n，那么将此设为上限
            high = guess
        guess = (low+high)/2  # 根据新的上下限，重新进行猜测
        count += 1    # 猜测次数每次增加1
    return guess
