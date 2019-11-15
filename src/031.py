# 面试题：字符串中的最大不重复子串


def max_not_repeat_str(strings):
    start = 0
    end = 0
    max_len = 0
    records = dict()
    while start < len(strings) and end < len(strings):
        record = records.get(strings[end], None)
        if record is None: # 如果没有重复 一直增加
            _len = end - start + 1
            if _len > max_len:
                max_len = _len
        elif record >= start:  # 如果有重复 那么要判断重复的字符是否是在start 和 end之间的
            start = record + 1
        records[strings[end]] = end  # 记录每个出现的字符的最后位置
        end += 1
    print(strings[start:end+1])
    return max_len
