# -*- coding: utf-8 -*-
# @Time    : 2020/2/13 11:05:25
# @Author  : dlg
# @File    : q9.py

"""

    itemgetter

"""

from operator import itemgetter

s = [
    {'a': 5},
    {'a': 3},
    {'a': 2},
    {'a': 6},
    {'a': 1},
    {'a': 2},
]

print(sorted(s, key=itemgetter('a'))) # 比lambda函数更加高效，min，max等函数也支持
print(sorted(s, key=lambda x : x['a']))
print(s)