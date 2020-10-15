import sys
from collections import Counter

from math import ceil

"""
检查给定列表是不是存在重复元素
"""


def all_unique(lst):
    return len(lst) == len(set(lst))


"""
检查两个字符串的组成元素是不是一样的。
"""


def anagram(first, second):
    return Counter(first) == Counter(second)


"""
检查变量所占用的内存
"""
variable = 308
print(sys.getsizeof(variable))

"""
检查字符串占用的字节数
"""


def byte_size(string):
    return len(string.encode('utf-8'))


"""
打印 N 次字符串
"""
n = 2;
s = "Programming"
print(s * n)

"""
大写字符串中每一个单词的首字母
"""
s = "programming is awesome"

print(s.title())

"""
给定具体的大小，定义一个函数以按照这个大小切割列表
"""


def chunk(lst, size):
    return list(
        map(lambda x: lst[x * size:x * size + size],
            list(range(0, ceil(len(lst) / size)))))


print(chunk([1, 2, 3, 4, 5], 2))

"""

"""


def compact(lst):
    return list(filter(bool, lst))


print(compact([0, 1, False, 2, '', 3, 'a', 's', 34]))
