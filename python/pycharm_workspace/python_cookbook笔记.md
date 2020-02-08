1.1 解压序列变量并赋值

- 变量的数量必须跟序列元素的数量一样
- 这种解压赋值可以用在任何可迭代对象上面，而不仅仅是列表或者元组。
  包括字符串，文件对象，迭代器和生成器
- 可能只想解压一部分，丢弃其他的值。对于这种情况 Python 并没有提
  供特殊的语法。但是你可以使用任意变量名去占位

```python
>>> a,b=(1,2)
>>> a
1
>>> b
2
>>> a = (1,2)
>>> a
(1, 2)
>>> a,b=(1)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    a,b=(1)
TypeError: cannot unpack non-iterable int object
>>> 
>>> a,b='cd'
>>> a
'c'
>>> b
'd'
>>> 
```

1.2 得到N个元素，可使用* ，通常，这些可迭代对象的元素结构有相同的确定的规则



```python
def get_avg_score(data):
    """
    使用*获取N个序列解压值
    :param data: all score
    :return: remove first and last, then cacl avg score
    """
    first, *scores, last = data
    return sum(scores) / len(scores)

avg_score = get_avg_score([1, 2, 3, 4])
print("avg score = " + str(avg_score)) # 2.5
```

1.3 保留最后N个元素