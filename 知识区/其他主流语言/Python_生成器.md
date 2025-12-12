# Python 生成器

## 定义
生成器（Generator）是Python中使用yield关键字的特殊函数，返回迭代器对象，实现惰性求值（按需生成值），节省内存，适合处理大数据集和无限序列。

## 核心内容
**1. 基本概念**
```python
# 普通函数（一次返回所有）
def get_numbers():
    return [0, 1, 2, 3, 4]

# 生成器函数（逐个生成）
def generate_numbers():
    yield 0
    yield 1
    yield 2
    yield 3
    yield 4

gen = generate_numbers()
print(next(gen))  # 0
print(next(gen))  # 1

# 迭代
for num in generate_numbers():
    print(num)
```

**2. yield工作原理**
```python
def counter():
    print("开始")
    yield 1
    print("第一次yield后")
    yield 2
    print("第二次yield后")
    yield 3
    print("结束")

gen = counter()
print(next(gen))  # "开始" 然后返回 1
print(next(gen))  # "第一次yield后" 然后返回 2
print(next(gen))  # "第二次yield后" 然后返回 3
# next(gen)  # StopIteration异常
```

**3. 生成器表达式**
```python
# 列表推导式（一次性创建所有元素）
squares_list = [x**2 for x in range(1000000)]

# 生成器表达式（按需生成）
squares_gen = (x**2 for x in range(1000000))

# 使用
print(next(squares_gen))  # 0
print(next(squares_gen))  # 1

# 转换为列表
result = list(squares_gen)
```

**4. 无限序列**
```python
# 无限计数器
def infinite_counter(start=0):
    count = start
    while True:
        yield count
        count += 1

counter = infinite_counter()
for _ in range(5):
    print(next(counter))  # 0, 1, 2, 3, 4

# 斐波那契数列
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
for _ in range(10):
    print(next(fib))  # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
```

**5. 文件读取（节省内存）**
```python
# 传统方法（一次性读入）
def read_file_all(filename):
    with open(filename) as f:
        return f.readlines()  # 占用大量内存

# 生成器方法（按行读取）
def read_file_gen(filename):
    with open(filename) as f:
        for line in f:
            yield line.strip()

# 处理大文件
for line in read_file_gen('large_file.txt'):
    process(line)  # 逐行处理
```

**6. 管道处理**
```python
# 多个生成器组合
def read_lines(filename):
    with open(filename) as f:
        for line in f:
            yield line

def filter_comments(lines):
    for line in lines:
        if not line.startswith('#'):
            yield line

def extract_numbers(lines):
    for line in lines:
        numbers = [int(x) for x in line.split() if x.isdigit()]
        yield from numbers  # yield from展开子生成器

# 管道
pipeline = extract_numbers(filter_comments(read_lines('data.txt')))
for num in pipeline:
    print(num)
```

**7. send()和close()**
```python
def accumulator():
    total = 0
    while True:
        value = yield total  # 接收send发送的值
        if value is None:
            break
        total += value

acc = accumulator()
next(acc)  # 启动生成器
print(acc.send(10))  # 10
print(acc.send(20))  # 30
print(acc.send(5))   # 35
acc.close()  # 关闭生成器

# throw()抛出异常
def gen_with_exception():
    try:
        yield 1
        yield 2
    except ValueError:
        yield "Caught ValueError"

g = gen_with_exception()
print(next(g))  # 1
print(g.throw(ValueError))  # "Caught ValueError"
```

**8. yield from（Python 3.3+）**
```python
# 委托生成器
def sub_gen():
    yield 1
    yield 2

def main_gen():
    yield from sub_gen()  # 委托给sub_gen
    yield 3

for value in main_gen():
    print(value)  # 1, 2, 3

# 展平嵌套列表
def flatten(nested_list):
    for item in nested_list:
        if isinstance(item, list):
            yield from flatten(item)  # 递归
        else:
            yield item

nested = [1, [2, [3, 4], 5], 6]
list(flatten(nested))  # [1, 2, 3, 4, 5, 6]
```

**9. 实用示例**
```python
# 批量处理
def batch(iterable, n):
    """将可迭代对象分批"""
    it = iter(iterable)
    while True:
        chunk = []
        for _ in range(n):
            try:
                chunk.append(next(it))
            except StopIteration:
                if chunk:
                    yield chunk
                return
        yield chunk

for batch_items in batch(range(10), 3):
    print(batch_items)  # [0,1,2], [3,4,5], [6,7,8], [9]

# 滑动窗口
def sliding_window(iterable, size):
    from collections import deque
    window = deque(maxlen=size)
    for item in iterable:
        window.append(item)
        if len(window) == size:
            yield list(window)

for window in sliding_window(range(5), 3):
    print(window)  # [0,1,2], [1,2,3], [2,3,4]

# 树遍历
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []
    
    def traverse(self):
        yield self.value
        for child in self.children:
            yield from child.traverse()
```

**10. 性能对比**
```python
import sys

# 列表（占用内存大）
list_obj = [x for x in range(1000000)]
print(sys.getsizeof(list_obj))  # ~8MB

# 生成器（占用内存小）
gen_obj = (x for x in range(1000000))
print(sys.getsizeof(gen_obj))   # ~128 bytes
```

## 应用场景
- 大文件处理：逐行读取日志、CSV文件
- 数据流处理：实时数据、网络流
- 无限序列：斐波那契、素数生成器
- 管道处理：多阶段数据转换
- 内存优化：处理大数据集
- 协程：异步编程基础

## 注意事项
- 生成器只能迭代一次（不可重复使用）
- 不能用len()和索引访问
- 生成器比列表推导式节省内存但速度略慢
- yield from可以简化子生成器委托
- 生成器是懒惰的（只在需要时计算）
- 不要在生成器中使用return返回值（用StopIteration）

## 关联知识
与 [[Python_列表推导式]]、[[Python_装饰器]]、[[Python_基础语法]] 相关。
