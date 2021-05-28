from numpy.core.defchararray import capitalize

x = "1234567890"
print(len(x))
print(x[1])
print(x[1:])
print(x[:3])
print(x[1:5])

x = "1"
print(x + x)
print(x * 2)

if "H" in x:
    print("H 在变量 a 中")
else:
    print("H 不在变量 a 中")

if "M" not in x:
    print("M 不在变量 a 中")
else:
    print("M 在变量 a 中")

print("我叫 %s 今年 %d 岁!" % ('小明', 10))

print(capitalize("abc"))
