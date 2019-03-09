import functools

l = [11, 10, 54, 45, 12]
f = lambda a, b: a if a > b else b
r = functools.reduce(f, l)
print(r)

'''
lambda 参数(一个,多个):返回值或者是返回值的运算表达式
下边是一个将列表内的字典排序的例子

'''
students = [
    {'name': 'TOM', 'age': 20},
    {'name': 'ROSE', 'age': 19},
    {'name': 'Jack', 'age': 22}
]

students.sort(key=lambda i: i['age'], reverse=True)
print(students)

list1m = [2, 3, 8, 9, 6]
print(list(map(lambda a: a ** a, list1m)))
# 将列表内的各个值传入列表 函数操作后进行改变 返回一个全新的列表
print(functools.reduce(lambda a, b: a * b, list1m))
# 将列表的组合值挨个传入函数参数(可为两个,三个,)若列表为list1m
# 函数需要两个值 则函数传入的依次为(2,3)(3,8)(8,9)
# 它返回的可不是个新列表 是函数内的运算结果
print(list(filter(lambda x: x % 3 == 0, list1m)))
# 删选列表用的 函数内筛选功能,
