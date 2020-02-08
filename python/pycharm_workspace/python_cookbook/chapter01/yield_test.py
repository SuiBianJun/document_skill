# -*- coding: utf-8 -*-
# @Time    : 2020/2/8 1:28:18
# @Author  : dlg
# @File    : yield_test.py

def get_data(length):
    for i in range(length):
        yield i
        print('done')


for x in get_data(5):
    print(x)