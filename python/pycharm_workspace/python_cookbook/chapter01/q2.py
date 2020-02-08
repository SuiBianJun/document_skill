# -*- coding: utf-8 -*-
# @Time    : 2020/2/8 1:36:45
# @Author  : dlg
# @File    : q2.py

from collections import deque

def get_last_pattern_line(f, pattern):
    """
    获取匹配文本行
    :param f: 文件句柄
    :param pattern: 匹配参数
    """
    for line in f.readlines():
        if pattern in line:
            yield line

def get_last_n_pattern_line(f, pattern, n=2):
    """
    获取最后n行匹配数据
    :param f:
    :param pattern:
    :param n: 保留行数
    :return: 结果
    """
    pre_lines = deque(maxlen=n)
    for line in get_last_pattern_line(f, pattern):
        pre_lines.append(line)
    return pre_lines

if __name__ == '__main__':
    with open(r'./something.txt') as f:
        for pre_line in get_last_n_pattern_line(f, 'a', 3):
            print(pre_line)