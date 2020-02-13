# -*- coding: utf-8 -*-
# @Time    : 2020/2/13 9:43:47
# @Author  : dlg
# @File    : q7.py

"""

    命名切片

"""

a = [1, 2, 3, 4, 5, 6, 7, 8]

print(a[1:2])
print(a[1:3])

s1 = slice(1, 9)
s2 = slice(1, 3)

print(a[slice(1, 2)])

print(a[s1])
print(a[s2])

b = 'asdfghjkl'
print(b[s1])
print(b[s2])

print(s1.stop)

print(s1.indices(len(b)))
print(s2.indices(len(b)))

for i in range(*s1.indices(len(b))): # *将参数组成元组形式
    print(i)


def params_test(data, data2):
    print(str(data) + '==' + str(data2))
c = [1, 2]
params_test(*c)

def params_test2(**kwargs):
    print(kwargs)
params_test2(a=1, b=2)