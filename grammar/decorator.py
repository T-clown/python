import functools
import time

from tool.decoratortools import execute_time


def my_decorator(func):
    def wrapper(*args, **kwargs):
        print(type(args))
        print(type(kwargs))
        print(kwargs)
        print('wrapper of decorator：{}'.format(args[0]))
        func(*args, **kwargs)

    return wrapper


@my_decorator
def greet(message, name):
    print(message)
    print(name)


greet("666", "2222")


def repeat(num):
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(num):
                print('wrapper of decorator')
                func(*args, **kwargs)

        return wrapper

    return my_decorator


@repeat(3)
def greet(message):
    print(message)


greet('hello world')


def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('wrapper of decorator')
        func(*args, **kwargs)

    return wrapper


@my_decorator
def greet(message):
    print(message)


print(greet.__name__)

"""
类也可以作为装饰器。类装饰器主要依赖于函数__call__()，每当你调用一个类的示例时，函数__call__()就会被执行一次
"""


class Count:
    def __init__(self, func):
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print('num of calls is: {}'.format(self.num_calls))
        return self.func(*args, **kwargs)


@Count
def example():
    print("hello world")


example()
example()


def my_decorator1(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('execute decorator1')
        func(*args, **kwargs)

    return wrapper


def my_decorator2(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('execute decorator2')
        func(*args, **kwargs)

    return wrapper


@my_decorator1
@my_decorator2
def greet(message):
    print(message)


greet('hello world')


@execute_time
def calculate_similarity(items):
    print(items)


calculate_similarity("222")

"""
类装饰器
"""


class Loging(object):
    def __init__(self, level="warn"):
        self.level = level

    def __call__(self, func):
        @functools.wraps(func)
        def _deco(*args, **kwargs):
            if self.level == "warn":
                self.notify(func)
            return func(*args, **kwargs)

        return _deco

    def notify(self, func):
        # logit只打日志，不做别的
        print("%s is running" % func.__name__)


@Loging(level="warn")  # 执行__call__方法
def bar(a, b):
    print('i am bar:%s' % (a + b))


bar(1, 3)


class email_loging(Loging):
    '''
    一个loging的实现版本，可以在函数调用时发送email给管理员
    '''

    def __init__(self, email='admin@myproject.com', *args, **kwargs):
        self.email = email
        super(email_loging, self).__init__(*args, **kwargs)

    def notify(self, func):
        # 发送一封email到self.email
        print("%s is running" % func.__name__)
        print("sending email to %s" % self.email)


@email_loging(level="warn")
def bar(a, b):
    print('i am bar:%s' % (a + b))


bar(1, 3)
