# -*- coding: utf-8 -*-
# @Time    : 2020/2/12 10:24:26
# @Author  : dlg
# @File    : q6.py

"""

    保留原始顺序，删除重复的元素

"""

def delete_dupe(data):
    """
        hashable数据支持
    :param data:
    """
    seen = set()
    for x in data:
        if x not in seen:
            yield x
            seen.add(x)

def delete_dupe_object(data):
    """
        复杂数据结构支持
    :param data:
    :param key:
    """
    seen = set()
    for x in data:
        # print('x: ' + str(x))
        # print('item: ' + x.popitem())
        item = x.popitem()
        if item not in seen:
            yield item
            seen.add(item)

l = [1, 6, 2, 10, 3, 2, 4, 7, 1, 9]

s = set(l) # 不保证原始顺序
print(s)

s2 = set()
s2.add(5)
s2.add(2)
s2.add(3)
s2.add(4)

print(s2)
print([x for x in delete_dupe(l)]) # 保证顺序一致

dic = [
    {'a': 3},
    {'a': 1},
    {'c': 1},
    {'b': 1},
    {'a': 3},
]

# for x in dic:
#     print(x.popitem()) # 直接作用在dic上

print([x for x in delete_dupe_object(dic)])


