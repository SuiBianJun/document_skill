# -*- coding: utf-8 -*-
# @Time    : 2020/2/10 16:39:27
# @Author  : dlg
# @File    : function_test.py

f = lambda s : s['a']

data = [
    {'a': 5},
    {'a': 6},
    {'a': 7}
]

data2 = [1, 2, 3, 4]

#print(f(data[0]))


def func(data, key=None):
    for i in range(len(data)):
        if key== None:
            print(data[i])
        else:
            compare_data = key(data[i])
            print(compare_data)


func(data2)
func(data, key=lambda s : s['a'])