import functools
import time


# 统计方法执行消耗时间
def execute_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        res = func(*args, **kwargs)
        end = time.perf_counter()
        print('方法{} 执行消耗时间 {} ms'.format(func.__name__, (end - start) * 1000))
        return res

    return wrapper
