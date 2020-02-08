# -*- coding: utf-8 -*-
# @Time    : 2020/2/8 16:24:56
# @Author  : dlg
# @File    : my_list.py

"""

    链表数据结构基本使用

"""

class node(object):
    def __init__(self):
        self.pre = None
        self.next = None
        self.data = None


class my_list(object):
    def __init__(self):
        self.head = node()
        self.tail = self.head
        self.size = 0
        self.itr_point = self.head

    def add(self, data):
        """
            添加列表数据
        :param data:
        """
        new_node = node()
        new_node.data = data
        new_node.next = None
        new_node.pre = None

        self.tail.next = new_node
        self.tail = new_node

        self.size += 1

        # if self.head.next == None:
        #     self.tail = new_node
        #     self.head.next = self.tail
        # else:
        #     self.tail.next = new_node
        #     self.tail = new_node

    def get(self, index=0):
        """
            获取列表数据
        :param index:
        """
        temp_node = self.head
        while index > -1 and temp_node.next != None:
            temp_node = temp_node.next
            index -= 1
        return temp_node.data

    def remove(self, index=0):
        """
            删除列表数据
        :param index:
        """
        temp_node = self.head
        pre_node = temp_node
        while index > -1 and temp_node.next != None:
            pre_node = temp_node
            temp_node = temp_node.next
            index -= 1
        pre_node.next = temp_node.next

        if temp_node.next == None:
            self.tail = pre_node

        self.size -= 1

    def length(self):
        """
            获取列表当前元素数量
        """
        return self.size

    def print(self):
        """
            打印列表数据
        """
        temp_node = self.head
        data = []
        while temp_node.next != None:
            data.append(temp_node.next.data)
            temp_node = temp_node.next
        print(str(data))

    # 加上迭代属性
    def __iter__(self):
        return self
    def __next__(self):
        data = None
        if self.itr_point.next == None:
            raise StopIteration # 迭代停止标志
        else:
            data = self.itr_point.next.data
            self.itr_point = self.itr_point.next
            return data


if __name__ == '__main__':
    l = my_list()

    l.add(1)
    l.add(2)
    l.add(3)

    print(l.get(0))
    print(l.get(1))
    print(l.get(2))

    l.remove(2)

    l.add(4)
    l.add(5)
    l.add(6)

    l.remove(0)
    l.remove(1)

    l.print()

    print('size: ' + str(l.length()))

    ll = my_list()
    for i in range(1, 1000):
        ll.add(i)
    # ll.print()
    sum_data = 0;
    for x in ll:
        sum_data += x
    print('sum = ' + str(sum_data))