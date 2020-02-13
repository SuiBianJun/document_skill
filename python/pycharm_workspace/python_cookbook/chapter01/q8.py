# -*- coding: utf-8 -*-
# @Time    : 2020/2/13 10:15:07
# @Author  : dlg
# @File    : q8.py

"""

    collections Counter计数类使用
    制表或者计数数据的场合

"""

from collections import Counter

words = [
'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
'my', 'eyes', "you're", 'under'
]

new_words = [
'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
'the', 'eyes', 'the', 'eyes'
]

c = Counter(words)

print(c.most_common())
print(c.most_common(2))

c.update(new_words) # 增加统计元素

c2 = Counter(new_words)

print(c - c2) # 运算
