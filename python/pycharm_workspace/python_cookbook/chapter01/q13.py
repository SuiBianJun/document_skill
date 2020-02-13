# -*- coding: utf-8 -*-
# @Time    : 2020/2/13 16:22:30
# @Author  : dlg
# @File    : q13.py

"""

    映射名称到序列元素
    collections namedtuple

"""

from collections import namedtuple

sub = namedtuple('sub', ['c', 'd'])
b = sub(1, 2)
print(b)
print(b.c)

# b.c = 3

b = b._replace(c=3)
print(b)