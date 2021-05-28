import sys

from loguru import logger

"""
迭代器
"""


class Iterator:
    __data = None
    __index = 0
    __max_index = 0

    def __init__(self, data):
        self.data = data
        self.__max_index = len(data) - 1

    def __iter__(self):
        return self

    def __next__(self):
        index = self.__index
        self.__index += 1
        if index > self.__max_index:
            logger.error("索引{}已经超过最大值{}".format(index, self.__max_index))
            raise StopIteration
        else:
            return self.data[index]


class Generator:
    n = 0

    def __init__(self, n):
        self.n = n

    def fibonacci(self):  # 生成器函数 - 斐波那契
        a, b, counter = 0, 1, 0

        while True:
            if (counter > self.n):
                return
            yield a
            a, b = b, a + b
            counter += 1


if __name__ == "__main__":
    # f 是一个迭代器，由生成器返回生成
    f = Generator(10).fibonacci()
    while True:
        try:
            print(next(f), end=" ")
        except StopIteration:
            print()
            logger.info("生成器迭代完成")
            break

    list = [1, 2]
    itr = iter(Iterator(list))
    while True:
        try:
            print(next(itr), end="  ")
        except StopIteration:
            sys.exit()
