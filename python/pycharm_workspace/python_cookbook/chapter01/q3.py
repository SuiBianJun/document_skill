# -*- coding: utf-8 -*-
# @Time    : 2020/2/9 14:22:14
# @Author  : dlg
# @File    : q3.py

"""

    python堆数据结构拓展库

"""

import heapq

num = [1, 3, 5, 2, 7, 9, 5, 2]

print(heapq.nlargest(2, num))
print(heapq.nsmallest(3, num))

data = [
    {'name': 'a', 'age': 1},
    {'name': 'b', 'age': 3},
    {'name': 'c', 'age': 2},
    {'name': 'd', 'age': 6},
    {'name': 'e', 'age': 4},
]

def kdef(s):
    return s['age']

print(heapq.nlargest(2, data, key=kdef))
print(heapq.nlargest(2, data, key=lambda s:s['age']))

#heapq.heappush(num)
print(heapq.heappop(num))
print(heapq.heappop(num))
print(heapq.heappop(num))

print(num)