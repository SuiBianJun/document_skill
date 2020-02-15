# -*- coding: utf-8 -*-
# @Time    : 2020/2/15 19:45:49
# @Author  : dlg
# @File    : q1.py

"""

    字符串分割
    re

"""


import re

# 可使用unix shell规则的匹配模式
from fnmatch import fnmatch, fnmatchcase

line = 'asdf fjdk; afed, fjek,asdf, foo'
print(re.split(r';', line))
print(re.split(r'[;\s,]\s*', line))

s = 'a.txt'

print(fnmatch(s, '*.txt'))
print(fnmatch(s, '*txt'))

print(fnmatchcase(s, '*.txt'))

