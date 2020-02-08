# -*- coding: utf-8 -*-
# @Time    : 2020/2/8 11:11:03
# @Author  : dlg
# @File    : my_queue.py
"""

队列基本功能实现

"""

import queue

class my_queue(object):

    def __init__(self, size):
        """
        :param size: 队列大小
        """
        self.size = size
        self.index_left = 0
        self.index_right = 0
        self.arr = [0] * size # 初始化数组
        self.count = 0 # 记录当前队列中元素个数

    def push(self, data):
        """
            右端入队列
        :param data:
        """
        if self.count < self.size:
            self.arr[self.index_right] = data
            self.index_right = (self.index_right + 1) % self.size
            self.count += 1
        else:
            print('queue has full.')
    def pop(self):
        """
            左端出队列
        :return:
        """
        if self.count > 0:
            temp_data = self.arr[self.index_left]
            self.index_left = (self.index_left + 1) % self.size
            self.count -= 1
            return temp_data
        else:
            print('queue is empty.')

    def print(self):
        temp_index_left = self.index_left
        while self.count > 0:
            print(self.arr[temp_index_left])
            temp_index_left = (temp_index_left + 1) % self.size
        print('---------------------------------------')

if __name__ == '__main__':
    q = my_queue(3)
    q.push(1)
    q.push(2)
    q.push(3)
    q.push(4)

    print(q.pop())
    print(q.pop())
    q.push(5)
    print(q.pop())
    q.push(6)
    print(q.pop())
    q.push(7)
    print(q.pop())
    q.push(8)
    print(q.pop())

    q.push(1)
    q.push(2)
    q.push(3)
    q.push(4)

    print(q.pop())
    print(q.pop())
    q.push(5)
    print(q.pop())
    q.push(6)
    print(q.pop())
    q.push(7)
    print(q.pop())
    q.push(8)
    print(q.pop())
    print(q.pop())
    print(q.pop())
    print(q.pop())


