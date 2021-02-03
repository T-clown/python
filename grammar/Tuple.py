"""
元组与列表类似，不同之处在于元组的元素不能修改。
元组使用小括号 ( )，列表使用方括号 [ ]
"""
tup1 = (1)
print(type(tup1))
tup2 = (1, 2)
print(type(tup2))

tup = (1, 2, 3, 4, 5, 6, 7)
print("tup1[0]: ", tup[0])
print("tup2[1:5]: ", tup[1:5])
print(len(tup))
print(max(tup))
print(min(tup))
list = [1, 2, 3]
tuple = tuple(list)
print(tuple)
print(id(tup))
print(id(tuple))

tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')

# 以下修改元组元素操作是非法的。
# tup1[0] = 100

# 创建一个新的元组
tup3 = tup1 + tup2
print(tup3)

del tup3
#print(tup3)
