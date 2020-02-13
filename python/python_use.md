1、int理论上是每次赋值都创建一个新对象的。但是由于使用频繁，为了提升性能避免浪费，所有python有个 整数池，默认1～256的数字都属于这个整数池，这些每次赋值的时候，是取得池中的整数对象。但是其他的除外

2、python的三目运算形式

```
条件为真时的结果 if 判段的条件 else 条件为假时的结果 
```

3、使对象带上迭代器特性

```python
def __iter__(self):    
    return self
def __next__(self):   
    # 生成每次迭代的数据
    raise StopIteration # 迭代停止标志    

```

4、元组在同样长度的情况下可以进行大小比较，列表在不同长度也可以大小比较

5、（*）会把接收到的参数形成一个元组，而（**）则会把接收到的参数存入一个字典

```python
def params_test(data, data2):
    print(str(data) + '==' + str(data2))
c = [1, 2]
params_test(*c)

>>> 1==2

def params_test2(**kwargs):
    print(kwargs)
params_test2(a=1, b=2)
>>> {'a': 1, 'b': 2}
```



6、命名元组

```python
from collections import namedtuple
sub = namedtuple('sub', ['c', 'd'])
b= sub(1, 2)
print(b)
print(b.c)

>>> a(c=1, d=2)
>>> 1

# b.c = 3 # 原则上命名元组不可修改，但是可以使用_replace方法
b = b._replace(c=3)
print(b)
```