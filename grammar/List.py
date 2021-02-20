list = ['red', 'green', 'blue', 'yellow', 'white', 'black']
print(list[0])
print(list[-1])

print(list[0:3])
# 更新列表元素
list[0] = 0
print(list[0])
# 删除元素
del list[1]
print(list)

nums = [1, 2]
# 列表元素个数
print(len(nums))
# 组合
print(list + nums)
# 重复
print(nums * 2)
# 判断
print(2 in nums)
# 迭代
for x in nums:
    print(x, end=" ")
print()
nums += nums
print(nums)

# 返回列表元素最大值
print(max(nums))
# 返回列表元素最小值
print(min(nums))
# 将元组转换为列表
# list(seq)

# 在列表末尾添加新的对象
nums.append(3)
print(nums)
# 统计某个元素在列表中出现的次数
print(nums.count(1))
# 在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
nums.extend([4, 5])
print(nums)
# 从列表中找出某个值第一个匹配项的索引位置
print(nums.index(2))
# 将对象插入列表
nums.insert(0, 99)
print(nums)
# 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
print(nums.pop())
print(nums.pop(0))
print(nums)

# 移除列表中某个值的第一个匹配项
nums.remove(2)

# 反转列表中元素
nums.reverse()
# 对原列表进行排序
nums.sort(key=None, reverse=False)
# 复制列表
a = nums.copy()
print("复制:")
print(a)
# 清空列表
nums.clear()

