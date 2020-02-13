# -*- coding: utf-8 -*-
# @Time    : 2020/2/13 11:58:44
# @Author  : dlg
# @File    : q11.py

"""

    过滤序列元素
    itertools compress过滤

"""
from itertools import compress

mylist = [1, 4, -5, 10, -7, 2, 3, -1]

print([x for x in mylist if x > 0]) # 列表推导

g = (x for x in mylist if x > 0) # 迭代器，比列表推导省内存
for x in g:
    print(x)

print([x if x > 0 else 0 for x in mylist]) # 列表推导,不符合条件的替换

def is_positive(n):
    try:
        x = int(n)
        return True if x > 0 else False
    except:
        return False
print(list(filter(is_positive, mylist))) # filter内置过滤模块

a = ['a', 'b', 'c', 'd', 'e', 'f']
b = [1, 2, 3, 4, 5, 6]

print(list(compress(a, [True if x > 3 else False for x in b]))) # compress结合Boolean列表实现两组相关列表的数据过滤