# Python 基础语法

## 定义
Python基础语法包括缩进定义代码块、动态类型系统、丰富的内置数据类型（list、dict、tuple、set）、简洁的控制流（if/for/while）和函数定义（def），强调代码可读性和简洁性。

## 核心内容
**1. 缩进与代码块**
```python
# 使用缩进表示代码块（通常4个空格）
if x > 0:
    print("正数")
    print("继续")
else:
    print("非正数")

# 错误示例
if x > 0:
print("错误")  # IndentationError
```

**2. 变量与数据类型**
```python
# 动态类型，无需声明
x = 10          # int
y = 3.14        # float
name = "Alice"  # str
flag = True     # bool

# 类型转换
int("123")      # 123
str(456)        # "456"
float("3.14")   # 3.14

# 多重赋值
a, b, c = 1, 2, 3
x = y = z = 0
```

**3. 字符串操作**
```python
s = "Hello"

# 拼接
s + " World"    # "Hello World"
s * 3           # "HelloHelloHello"

# 索引与切片
s[0]            # 'H'
s[-1]           # 'o'
s[1:4]          # 'ell'
s[::-1]         # 'olleH'（反转）

# 方法
s.upper()       # "HELLO"
s.lower()       # "hello"
s.replace('l', 'L')  # "HeLLo"
s.split('e')    # ['H', 'llo']

# 格式化
f"Hello {name}"  # f-string（Python 3.6+）
"Hello {}".format(name)
"Hello %s" % name
```

**4. 列表（List）**
```python
lst = [1, 2, 3, 4, 5]

# 操作
lst.append(6)       # 添加
lst.insert(0, 0)    # 插入
lst.remove(3)       # 删除值
lst.pop()           # 删除最后一个
lst[0] = 10         # 修改
len(lst)            # 长度

# 切片
lst[1:3]            # [2, 3]
lst[::2]            # [1, 3, 5]

# 方法
lst.sort()          # 排序
lst.reverse()       # 反转
lst.count(2)        # 计数
lst.index(3)        # 查找索引
```

**5. 字典（Dict）**
```python
d = {"name": "Alice", "age": 20}

# 访问
d["name"]           # "Alice"
d.get("age", 0)     # 20，不存在返回默认值

# 操作
d["city"] = "Beijing"  # 添加
del d["age"]           # 删除
d.pop("name")          # 删除并返回值

# 遍历
for key in d:
    print(key, d[key])
    
for key, value in d.items():
    print(key, value)
```

**6. 元组（Tuple）与集合（Set）**
```python
# 元组（不可变）
t = (1, 2, 3)
x, y, z = t  # 解包

# 集合（无序、不重复）
s = {1, 2, 3, 3}  # {1, 2, 3}
s.add(4)
s.remove(2)
s1 & s2  # 交集
s1 | s2  # 并集
s1 - s2  # 差集
```

**7. 控制流**
```python
# if-elif-else
if x > 0:
    print("正数")
elif x == 0:
    print("零")
else:
    print("负数")

# for循环
for i in range(5):  # 0, 1, 2, 3, 4
    print(i)

for item in [1, 2, 3]:
    print(item)

# while循环
while x > 0:
    x -= 1

# 列表推导式
squares = [x**2 for x in range(10)]
evens = [x for x in range(10) if x % 2 == 0]
```

**8. 函数**
```python
# 基本函数
def greet(name):
    return f"Hello {name}"

# 默认参数
def power(x, n=2):
    return x ** n

power(3)     # 9
power(3, 3)  # 27

# 可变参数
def sum_all(*args):
    return sum(args)

sum_all(1, 2, 3, 4)  # 10

# 关键字参数
def person(**kwargs):
    print(kwargs)

person(name="Alice", age=20)

# Lambda表达式
add = lambda x, y: x + y
add(2, 3)  # 5
```

**9. 常用内置函数**
```python
len([1, 2, 3])      # 3
max([1, 5, 3])      # 5
min([1, 5, 3])      # 1
sum([1, 2, 3])      # 6
sorted([3, 1, 2])   # [1, 2, 3]
reversed([1, 2, 3]) # 反向迭代器
enumerate(['a', 'b'])  # [(0, 'a'), (1, 'b')]
zip([1, 2], ['a', 'b'])  # [(1, 'a'), (2, 'b')]
map(lambda x: x*2, [1, 2, 3])  # [2, 4, 6]
filter(lambda x: x>0, [-1, 0, 1])  # [1]
```

## 应用场景
- 脚本编程：自动化任务
- 数据分析：NumPy、Pandas
- Web开发：Django、Flask
- 机器学习：TensorFlow、PyTorch
- 科学计算：SciPy、Matplotlib
- 爬虫：Requests、Scrapy

## 注意事项
- 严格遵守缩进（混用空格和Tab会报错）
- 变量名区分大小写
- 列表可变，元组不可变
- 字典键必须是不可变类型
- range()返回迭代器，不是列表
- Python 3中print是函数：`print()`

## 关联知识
与 [[Python_列表推导式]]、[[Python_装饰器]]、[[Python_面向对象]] 相关。
