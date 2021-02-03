"""
字典是另一种可变容器模型，且可存储任意类型对象。
字典的每个键值 key=>value 对用冒号 : 分割，每个对之间用逗号(,)分割，整个字典包括在花括号 {} 中
键必须是唯一的，但值则不必。
值可以取任何数据类型，但键必须是不可变的，如字符串，数字
"""
dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}

print("dict['Name']: ", dict['Name'])
print("dict['Age']: ", dict['Age'])
dict['Age'] = 8
print("dict['Age']: ", dict['Age'])
del dict['Name']  # 删除键 'Name'
dict.clear()  # 清空字典
del dict  # 删除字典

# 1）不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住
dict = {'Name': 'Runoob', 'Age': 7, 'Name': '小菜鸟'}

print("dict['Name']: ", dict['Name'])
# 2）键必须不可变，所以可以用数字，字符串或元组充当，而用列表就不行


print("字典key-value对数：", len(dict))
print(str(dict))
print(type(dict))
copy = dict.copy()
print("copy:", copy)
# dict.clear()
# print("dict:", dict)
# print("copy:", copy)
# 创建一个新字典，以序列seq中元素做字典的键，val为字典所有键对应的初始值
copy2 = copy.fromkeys(dict)
print(copy2)

print(copy2.get("aa", "默认值"))
print("aa" in copy)
i = copy.items()
print(i)

print(copy.keys())
print(copy.values())
# 如果键不存在于字典中，将会添加键并将值设为default
dict.setdefault("a", "a")
print(dict)
# 把字典dict的键/值对更新到copy里
copy.update(dict)
print(copy)

print(dict.pop("b", "b"))
print(dict.popitem())
