# Python 面向对象

## 定义
Python面向对象编程通过class定义类，使用self表示实例，`__init__`作为构造方法，支持继承、多态、封装、魔法方法（双下划线方法），提供灵活的对象创建和操作机制。

## 核心内容
**1. 类与对象**
```python
class Person:
    # 类属性
    species = "Human"
    
    # 构造方法
    def __init__(self, name, age):
        self.name = name  # 实例属性
        self.age = age
    
    # 实例方法
    def greet(self):
        return f"Hello, I'm {self.name}"
    
    # 类方法
    @classmethod
    def from_birth_year(cls, name, birth_year):
        age = 2025 - birth_year
        return cls(name, age)
    
    # 静态方法
    @staticmethod
    def is_adult(age):
        return age >= 18

# 创建对象
p = Person("Alice", 20)
print(p.greet())

# 类方法
p2 = Person.from_birth_year("Bob", 2000)

# 静态方法
Person.is_adult(20)
```

**2. 封装**
```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # 私有属性（name mangling）
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return True
        return False
    
    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self, value):
        if value >= 0:
            self.__balance = value

account = BankAccount(1000)
account.deposit(500)
print(account.balance)  # 使用property
account.balance = 2000  # 使用setter
```

**3. 继承**
```python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        pass

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # 调用父类构造方法
        self.breed = breed
    
    def speak(self):  # 重写父类方法
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# 多继承
class FlyingDog(Dog, Animal):
    def fly(self):
        return "Flying!"
```

**4. 多态**
```python
def animal_sound(animal):
    print(animal.speak())

dog = Dog("Buddy", "Golden")
cat = Cat("Whiskers")

animal_sound(dog)  # Woof!
animal_sound(cat)  # Meow!

# 鸭子类型（Duck Typing）
class Bird:
    def speak(self):
        return "Chirp!"

bird = Bird()
animal_sound(bird)  # Chirp!（不需要继承Animal）
```

**5. 魔法方法（特殊方法）**
```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    # 字符串表示
    def __str__(self):
        return f"Point({self.x}, {self.y})"
    
    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"
    
    # 运算符重载
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    # 索引访问
    def __getitem__(self, index):
        return [self.x, self.y][index]
    
    # 长度
    def __len__(self):
        return 2
    
    # 调用对象
    def __call__(self):
        return (self.x, self.y)

p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = p1 + p2  # Point(4, 6)
print(p1)     # Point(1, 2)
print(p1[0])  # 1
print(p1())   # (1, 2)
```

**6. 常用魔法方法**
```python
# 比较运算符
__lt__  # <
__le__  # <=
__gt__  # >
__ge__  # >=
__eq__  # ==
__ne__  # !=

# 算术运算符
__add__     # +
__sub__     # -
__mul__     # *
__truediv__ # /
__mod__     # %
__pow__     # **

# 容器方法
__len__      # len()
__getitem__  # obj[key]
__setitem__  # obj[key] = value
__delitem__  # del obj[key]
__contains__ # in
__iter__     # for循环

# 上下文管理器
__enter__    # with进入
__exit__     # with退出
```

**7. 属性装饰器**
```python
class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if value > 0:
            self._radius = value
        else:
            raise ValueError("Radius must be positive")
    
    @property
    def area(self):
        return 3.14159 * self._radius ** 2
    
    @property
    def circumference(self):
        return 2 * 3.14159 * self._radius

c = Circle(5)
print(c.area)  # 78.53975
c.radius = 10
print(c.area)  # 314.159
```

**8. 抽象基类**
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

# shape = Shape()  # 错误：不能实例化抽象类
rect = Rectangle(5, 3)  # 正确
```

**9. 数据类（Python 3.7+）**
```python
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int
    city: str = "Beijing"  # 默认值
    
    def greet(self):
        return f"Hello, I'm {self.name}"

p = Person("Alice", 20)
print(p)  # Person(name='Alice', age=20, city='Beijing')
# 自动生成__init__、__repr__、__eq__等方法
```

## 应用场景
- 数据建模：用户、订单、产品等实体
- 设计模式：单例、工厂、装饰器
- 框架开发：Django Model、Flask类视图
- 游戏开发：角色、道具、场景类
- 算法封装：将算法封装为类
- API客户端：封装HTTP请求

## 注意事项
- `__init__`不是构造方法，`__new__`才是
- self是约定俗成，可以用其他名字（不推荐）
- 双下划线前缀触发name mangling（`_ClassName__attr`）
- 单下划线前缀只是约定（表示私有）
- Python支持多继承（MRO解析顺序）
- 优先使用组合而非继承

## 关联知识
与 [[Python_基础语法]]、[[Python_装饰器]]、[[Java_面向对象]] 相关。
