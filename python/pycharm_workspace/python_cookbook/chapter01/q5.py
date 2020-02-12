# -*- coding: utf-8 -*-
# @Time    : 2020/2/11 20:13:11
# @Author  : dlg
# @File    : q5.py

"""

    对字典进行运算操作

"""

dic = {
    'a': 1,
    'b': 3,
    'c': 4,
    'd': 2,
    'e': 0
}

print(min(dic.values()))
print(min(dic, key=lambda s : dic[s]))

print(min(zip(dic.values(), dic.keys())))

dic2 = {
    'a': 6,
    'f': 3,
    'c': 4,
    'h': 2,
    'e': 0
}

print(dic.keys() & dic2.keys())
print(dic.keys() - dic2.keys())
print(dic.items() & dic2.items())

for x in dic.items():
    print(x[0] + '=>' + str(x[1]))

for x in dic:
    print(x + "====" + str(dic[x]))

a = [dic[x] for x in dic.keys()]
print(a)
dic3 = {k:dic[k] for k in dic.keys()}
print(dic3)