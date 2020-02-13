# -*- coding: utf-8 -*-
# @Time    : 2020/2/13 16:00:28
# @Author  : dlg
# @File    : q12.py

"""

    字典推导

"""

prices = {
'ACME': 45.23,
'AAPL': 612.78,
'IBM': 205.55,
'HPQ': 37.20,
'FB': 10.75
}

p_d = {key : value for key, value in prices.items() if value > 300} # 性能相对较好
print(p_d)

d = dict(a=1)
print(d)

print(dict((k, v) for k, v in prices.items()))
