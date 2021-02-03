#!/usr/bin/python3

# Fibonacci series: 斐波纳契数列
# 两个元素的总和确定了下一个数
# 代码 a, b = b, a+b 的计算方式为先计算右边表达式，然后同时赋值给左边
import sys

a, b = 0, 1
while b < 10:
    print(b, end=",")
    a, b = b, a + b
print()

var1 = 100
if var1:
    print(var1)
var2 = 0
if var2:
    print(var2)

for i in range(5):
    print(i)
for i in range(5, 9):
    print(i)
for i in range(0, 10, 2):
    print(i)
s = [1, 2, 3]
for i in range(len(s)):
    print(i, s[i])
print(list(range(5)))

list = [1, 2, 3, 4]
it = iter(list)  # 创建迭代器对象
print(next(it))  # 输出迭代器的下一个元素
for x in it:
    print(x, end=" ")

print()
it = iter(list)
while True:
    try:
        print (next(it))
    except StopIteration:
        sys.exit()
