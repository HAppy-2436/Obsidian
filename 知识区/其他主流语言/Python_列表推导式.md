# Python 列表推导式

## 定义
列表推导式（List Comprehension）是Python创建列表的简洁语法，用一行代码完成循环和条件过滤，语法为`[expression for item in iterable if condition]`，提高代码可读性和执行效率。

## 核心内容
**1. 基本语法**
```python
# 传统方法
squares = []
for x in range(10):
    squares.append(x**2)

# 列表推导式
squares = [x**2 for x in range(10)]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

**2. 带条件过滤**
```python
# 偶数的平方
evens = [x**2 for x in range(10) if x % 2 == 0]
# [0, 4, 16, 36, 64]

# 多个条件
nums = [x for x in range(20) if x % 2 == 0 if x % 3 == 0]
# [0, 6, 12, 18]

# if-else表达式（三元运算符）
result = [x if x % 2 == 0 else -x for x in range(5)]
# [0, -1, 2, -3, 4]
```

**3. 嵌套循环**
```python
# 二维列表展开
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [num for row in matrix for num in row]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 笛卡尔积
pairs = [(x, y) for x in [1, 2, 3] for y in ['a', 'b']]
# [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b'), (3, 'a'), (3, 'b')]

# 创建二维矩阵
matrix = [[i*j for j in range(3)] for i in range(3)]
# [[0, 0, 0], [0, 1, 2], [0, 2, 4]]
```

**4. 字符串处理**
```python
# 提取字符
text = "Hello World"
vowels = [c for c in text if c.lower() in 'aeiou']
# ['e', 'o', 'o']

# 转换大小写
words = ['hello', 'world']
upper = [w.upper() for w in words]
# ['HELLO', 'WORLD']

# 分割单词
sentence = "Python is awesome"
lengths = [len(word) for word in sentence.split()]
# [6, 2, 7]
```

**5. 字典推导式**
```python
# 基本字典推导式
squares = {x: x**2 for x in range(6)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# 交换键值
original = {'a': 1, 'b': 2}
swapped = {v: k for k, v in original.items()}
# {1: 'a', 2: 'b'}

# 条件过滤
scores = {'Alice': 85, 'Bob': 70, 'Charlie': 95}
passed = {k: v for k, v in scores.items() if v >= 80}
# {'Alice': 85, 'Charlie': 95}
```

**6. 集合推导式**
```python
# 去重
nums = [1, 2, 2, 3, 3, 4]
unique = {x for x in nums}
# {1, 2, 3, 4}

# 条件集合
evens = {x for x in range(10) if x % 2 == 0}
# {0, 2, 4, 6, 8}
```

**7. 生成器表达式**
```python
# 使用()创建生成器（惰性求值）
gen = (x**2 for x in range(10))
print(next(gen))  # 0
print(next(gen))  # 1

# 节省内存
sum_squares = sum(x**2 for x in range(1000000))
# 不会创建完整列表

# 转换为列表
result = list(x**2 for x in range(5))
```

**8. 实用示例**
```python
# 文件读取
lines = [line.strip() for line in open('file.txt')]

# 数据清洗
data = ['1', '2', 'abc', '3']
nums = [int(x) for x in data if x.isdigit()]
# [1, 2, 3]

# 矩阵转置
matrix = [[1, 2, 3], [4, 5, 6]]
transposed = [[row[i] for row in matrix] for i in range(3)]
# [[1, 4], [2, 5], [3, 6]]

# 展平嵌套列表
nested = [[1, 2], [3, [4, 5]], 6]
def flatten(lst):
    return [item for sublist in lst 
            for item in (flatten(sublist) if isinstance(sublist, list) else [sublist])]

# 多维数组
cube = [[[i+j+k for k in range(3)] 
         for j in range(3)] 
        for i in range(3)]
```

**9. 性能对比**
```python
import timeit

# 列表推导式（快）
time1 = timeit.timeit('[x**2 for x in range(1000)]', number=10000)

# 传统for循环（慢）
time2 = timeit.timeit('''
result = []
for x in range(1000):
    result.append(x**2)
''', number=10000)

# map（速度居中）
time3 = timeit.timeit('list(map(lambda x: x**2, range(1000)))', number=10000)
```

## 应用场景
- 数据转换：类型转换、格式化
- 过滤筛选：提取满足条件的元素
- 数学运算：批量计算、矩阵操作
- 字符串处理：分割、清洗、提取
- 数据分析：Pandas配合列表推导式
- 算法实现：简洁实现复杂逻辑

## 注意事项
- 不要过度嵌套（降低可读性）
- 大数据集用生成器表达式（节省内存）
- 复杂逻辑用普通循环（提高可读性）
- 推导式中避免副作用（如修改外部变量）
- 推导式通常比for循环快10-20%
- 不支持break和continue

## 关联知识
与 [[Python_基础语法]]、[[Python_生成器]]、[[Python_装饰器]] 相关。
