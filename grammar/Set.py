"""
集合（set）是一个无序的不重复元素序列。
可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典
"""

a = {1, 2, 3}
b = {1, 2}
print(1 in a)
# 差集
print(a - b)
print(b - a)
# 并集
print(a | b)
# 公共元素
print(a & b)
# 不同时包含于a和b的元素
print(a ^ b)

a = {x for x in 'abd' if x not in 'abc'}
print(a)
# 1.集合添加元素
a.add("a")
print(a)
a.update({1, 3})
a.update([1, 4], [5, 6])
print(a)
# 2.删除元素
# 不存在会发生错误
a.remove(1)
# 不存在不会会发生错误
a.discard(0)
# 随机删除集合中的一个元素
a.pop()

print(len(a))
# a.clear()

a = {1, 2, 3}
b = {1, 2, 4}
print(a.difference(b))
print(b.difference(a))
# 移除集合中的元素，该元素在指定的集合也存在
# a.difference_update(b)
# 判断两个集合是否包含相同的元素，如果没有返回 True，否则返回 False。
print(a.isdisjoint(b))
# a是b的子集
print(a.issubset(b))
# b是a的子集
print(a.issuperset(b))
# 返回两个集合中不重复的元素集合
print(a.symmetric_difference(b))
# 移除当前集合中在另外一个指定集合相同的元素，并将另外一个指定集合中不同的元素插入到当前集合中
a.symmetric_difference_update(b)
print(a)
# 返回两个集合的并集
print(a.union(b))
