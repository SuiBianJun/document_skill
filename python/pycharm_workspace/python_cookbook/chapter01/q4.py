# -*- coding: utf-8 -*-
# @Time    : 2020/2/10 20:42:20
# @Author  : dlg
# @File    : q4.py

from collections import defaultdict

df = defaultdict(list)

d = {}
d.setdefault('a', []).append(1)
d.setdefault('a', []).append(2)

print(d)

d2 = {}
d2.setdefault('b', set()).add(1)
d2.setdefault('b', set()).add(2)

print(d2)
