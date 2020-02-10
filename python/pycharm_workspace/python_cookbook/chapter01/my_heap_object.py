# -*- coding: utf-8 -*-
# @Time    : 2020/2/9 14:38:29
# @Author  : dlg
# @File    : my_heap.py

"""

    大、小根堆的基本实现
    类对象支持

"""

class my_heap(object):
    def __init__(self):
        print('init')
    def heap_init(self, data, length, type='small', key=None):
        """
            将输入数据初始化为一个堆，默认为小根堆
        :param data: 输入数据
        :param length: 长度
        :param type: 堆的类型
        """
        self.arr = [None] * length
        self.type = type
        self.key = key
        for i in range(len(data)):
            self.arr[i] = data[i]
            self.heap_fine(i, key)

    def heap_push(self, data):
        """
            新元素入堆
        :param data:
        """
        self.arr.append(data)
        self.heap_fine(len(self.arr) - 1, self.key)

    def heap_pop(self):
        """
            弹出堆顶元素
        :return:
        """
        return self.heap_remove()

    def heap_remove(self, index=0):
        """
            弹出指定下标的元素
        :param index:
        :return:
        """
        data = self.arr.pop(index)
        self.heap_init(self.arr, len(self.arr), type=self.type)
        return data

    def heap_fine(self, index, key):
        """
            堆调整函数
        :param index:
        """
        temp_index = index
        while int((temp_index - 1) / 2) >= 0 and temp_index != 0:
            if key != None:
                current_index_data = key(self.arr[temp_index])
                pre_index_data = key(self.arr[int((temp_index - 1) / 2)])
            else:
                current_index_data = self.arr[temp_index]
                pre_index_data = self.arr[int((temp_index - 1) / 2)]
            if type == 'big':
                if pre_index_data < current_index_data:
                    pass
                else:
                    break
            elif pre_index_data > current_index_data:
                pass
            else:
                break
            temp_data = self.arr[int((temp_index - 1) / 2)]
            self.arr[int((temp_index - 1) / 2)] = self.arr[temp_index]
            self.arr[temp_index] = temp_data
            temp_index = int((temp_index - 1) / 2)

        # if key != None:
        #     while int((temp_index - 1) / 2) >= 0 and temp_index != 0:
        #         if type == 'big':
        #             if key(self.arr[int((temp_index - 1) / 2)]) < key(self.arr[temp_index]):
        #                 pass
        #             else:
        #                 break
        #         elif key(self.arr[int((temp_index - 1) / 2)]) > key(self.arr[temp_index]):
        #             pass
        #         else:
        #             break
        #         temp_data = self.arr[int((temp_index - 1) / 2)]
        #         self.arr[int((temp_index - 1) / 2)] = self.arr[temp_index]
        #         self.arr[temp_index] = temp_data
        #         temp_index = int((temp_index - 1) / 2)
        # else:
        #     while int((temp_index - 1) / 2) >= 0 and temp_index != 0:
        #         if type == 'big':
        #             if self.arr[int((temp_index - 1) / 2)] < self.arr[temp_index]:
        #                 pass
        #             else:
        #                 break
        #         elif self.arr[int((temp_index - 1) / 2)] > self.arr[temp_index]:
        #             pass
        #         else:
        #             break
        #         temp_data = self.arr[int((temp_index - 1) / 2)]
        #         self.arr[int((temp_index - 1) / 2)] = self.arr[temp_index]
        #         self.arr[temp_index] = temp_data
        #         temp_index = int((temp_index - 1) / 2)

    def heap_size(self):
        """
            返回当前堆大小
        :return:
        """
        return len(self.arr)

    def heap_type_change(self, type):
        """
            修改堆的类型
        :param type:
        """
        if type != self.type:
            self.heap_init(self.arr, len(self.arr), type)

    def print(self):
        pass

if __name__ == '__main__':
    data = [5, 3, 1, 4, 3, 0, 9, 2, 5, 1]
    h = my_heap()
    h.heap_init(data, len(data))
    h.heap_push(1)
    print(h.heap_size())
    print(h.heap_pop())
    print(h.heap_remove(3))
    h.heap_type_change('big')
    print('done')


    data2 = [
        {'name': 'a', 'age': 1},
        {'name': 'b', 'age': 3},
        {'name': 'c', 'age': 5},
        {'name': 'd', 'age': 4},
        {'name': 'e', 'age': 2},
        {'name': 'f', 'age': 0},
    ]

    h2 = my_heap()
    h2.heap_init(data2, len(data2), key=lambda s : s['age'])

    h2.heap_push({'name': 'g', 'age': 1})
    h2.heap_push({'name': 'g', 'age': -1})

    print('done')