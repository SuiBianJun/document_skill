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