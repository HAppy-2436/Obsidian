# Python 装饰器

## 定义
装饰器（Decorator）是Python中修改或增强函数行为的语法糖，本质是接受函数作为参数并返回新函数的高阶函数，使用@decorator语法应用，常用于日志、缓存、权限检查、性能测试等。

## 核心内容
**1. 基本概念**
```python
# 不使用装饰器
def my_function():
    print("Hello")

my_function = decorator(my_function)

# 使用装饰器语法糖
@decorator
def my_function():
    print("Hello")

# 等价于上面的写法
```

**2. 简单装饰器**
```python
def simple_decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

@simple_decorator
def say_hello():
    print("Hello!")

say_hello()
# 输出：
# Before function
# Hello!
# After function
```

**3. 带参数的函数装饰器**
```python
def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Finished {func.__name__}")
        return result
    return wrapper

@log_decorator
def add(a, b):
    return a + b

result = add(3, 5)  # 8
# 输出：
# Calling add
# Finished add
```

**4. 保留函数元信息**
```python
from functools import wraps

def my_decorator(func):
    @wraps(func)  # 保留原函数的__name__、__doc__等
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def greet(name):
    """Greet someone"""
    return f"Hello {name}"

print(greet.__name__)  # "greet"（不是"wrapper"）
print(greet.__doc__)   # "Greet someone"
```

**5. 带参数的装饰器**
```python
def repeat(times):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(times=3)
def say_hello():
    print("Hello!")

say_hello()
# 输出：Hello! Hello! Hello!
```

**6. 类装饰器**
```python
class CountCalls:
    def __init__(self, func):
        self.func = func
        self.count = 0
    
    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"Call {self.count} of {self.func.__name__}")
        return self.func(*args, **kwargs)

@CountCalls
def say_hello():
    print("Hello!")

say_hello()  # Call 1 of say_hello
say_hello()  # Call 2 of say_hello
```

**7. 多个装饰器**
```python
def bold(func):
    def wrapper():
        return "<b>" + func() + "</b>"
    return wrapper

def italic(func):
    def wrapper():
        return "<i>" + func() + "</i>"
    return wrapper

@bold
@italic
def greet():
    return "Hello"

print(greet())  # <b><i>Hello</i></b>
# 执行顺序：从下到上（先italic，后bold）
```

**8. 实用装饰器示例**
```python
# 计时装饰器
import time
def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f}s")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)

# 缓存装饰器
def cache(func):
    cached = {}
    @wraps(func)
    def wrapper(*args):
        if args not in cached:
            cached[args] = func(*args)
        return cached[args]
    return wrapper

@cache
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# 权限检查
def require_auth(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not current_user.is_authenticated:
            raise PermissionError("Not authenticated")
        return func(*args, **kwargs)
    return wrapper

@require_auth
def delete_account():
    # ...
    pass

# 重试装饰器
def retry(max_attempts=3):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1:
                        raise
                    print(f"Retry {attempt + 1}/{max_attempts}")
            return wrapper
        return decorator

@retry(max_attempts=3)
def unstable_function():
    # 可能失败的函数
    pass
```

**9. 装饰类**
```python
def singleton(cls):
    instances = {}
    @wraps(cls)
    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return wrapper

@singleton
class Database:
    def __init__(self):
        print("Creating database connection")

db1 = Database()  # Creating database connection
db2 = Database()  # 不会打印（使用缓存的实例）
print(db1 is db2)  # True
```

**10. 内置装饰器**
```python
class MyClass:
    # 静态方法
    @staticmethod
    def static_method():
        print("Static method")
    
    # 类方法
    @classmethod
    def class_method(cls):
        print(f"Class method of {cls.__name__}")
    
    # 属性
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, val):
        self._value = val

# 使用
MyClass.static_method()
MyClass.class_method()

obj = MyClass()
obj.value = 10
print(obj.value)
```

**11. functools中的装饰器**
```python
from functools import lru_cache, wraps

# LRU缓存（最近最少使用）
@lru_cache(maxsize=128)
def expensive_function(n):
    # 计算密集型函数
    return n ** n

# 单分派泛型函数
from functools import singledispatch

@singledispatch
def process(data):
    raise NotImplementedError("Unsupported type")

@process.register(int)
def _(data):
    return data * 2

@process.register(str)
def _(data):
    return data.upper()

process(5)      # 10
process("hi")   # "HI"
```

## 应用场景
- 日志记录：记录函数调用和参数
- 性能测试：计时、性能分析
- 缓存：记忆化、LRU缓存
- 权限控制：登录验证、角色检查
- 事务处理：数据库事务包装
- Web框架：Flask路由、Django权限

## 注意事项
- 使用@wraps保留原函数元信息
- 装饰器执行顺序：从下到上
- 带参数的装饰器需要三层嵌套
- 装饰器会隐藏原函数（调试困难）
- 类装饰器需要实现`__call__`方法
- 避免过度使用（降低可读性）

## 关联知识
与 [[Python_基础语法]]、[[Python_闭包]]、[[Python_面向对象]] 相关。
