# -*- coding: utf-8 -*-
# @Time    : 2020/2/8 2:22:44
# @Author  : dlg
# @File    : my_deque.py

"""

    双端队列基本功能实现

"""

class my_deque(object):
    def __init__(self, size=5):
        self.size = size
        self.index_left = 0
        self.index_right = 0
        self.arr = [0] * size  # 初始化数组
        self.count = 0  # 记录当前队列中元素个数

    def append(self, data):
        """
        在最右端插入数据
        :param data:
        """
        if self.count < self.size:
            self.arr[self.index_right] = data
            self.index_right = (self.index_right + 1) % self.size
            self.count += 1
        else:
            print('queue has full.')

    def appendLeft(self, data):
        """
        最左端插入数据
        :param data:
        """
        if self.count < self.size:
            self.index_left = (self.index_left - 1) % self.size
            self.arr[self.index_left] = data
            self.count += 1
        else:
            print('queue has full.')

    def pop(self):
        """
        弹出最左端的数据
        """
        if self.count > 0:
            temp_data = self.arr[self.index_left]
            self.index_left = (self.index_left + 1) % self.size
            self.count -= 1
            return temp_data
        else:
            print('queue is empty.')

    def popRight(self):
        """
        弹出最右端的数据
        """
        if self.count > 0:
            self.index_right = (self.index_right - 1) % self.size
            self.count -= 1
            return self.arr[self.index_right]
        else:
            print('queue is empty.')

    def count(self):
        """
        当前队列数据长度
        """
        return self.count

if __name__ == '__main__':
    dq = my_deque(3)
    #print(dq.size)

    dq.append(1)
    dq.append(2)
    dq.append(3)
    dq.append(4)

    print(dq.pop())
    print(dq.pop())

    dq.appendLeft(5)
    dq.appendLeft(6)

    print(dq.popRight())
    print(dq.popRight())
    print(dq.popRight())
    print(dq.popRight())

    dq.append(7)
    dq.append(8)

    print(dq.pop())
    print(dq.pop())

    dq.appendLeft(9)

    print('done')