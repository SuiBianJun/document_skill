# -*- coding: utf-8 -*-
# @Time    : 2020/2/15 21:25:31
# @Author  : dlg
# @File    : q3.py

"""

    字符串匹配好搜索

"""

import re

text1 = '11/27/2012   11/27/2012'

print(re.match(r'\d+/\d+/\d+', text1))
print(re.match(r'\d+/\d+/\d+$', text1)) # 更精确的匹配,只匹配一次

pattern = re.compile(r'\d+/\d+/\d+')
print(pattern.match(text1))

pattern2 = re.compile(r'(\d+)/(\d+)/(\d+)') # 捕获分组
print(pattern2.match(text1).groups())

print(pattern.findall(text1)) # 循环匹配