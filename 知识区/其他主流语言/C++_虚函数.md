# C++ 虚函数

## 定义
虚函数（Virtual Function）是C++实现运行时多态的机制，通过virtual关键字声明，使用基类指针或引用调用派生类重写的方法，通过虚函数表（vtable）实现动态绑定。

## 核心内容
**1. 基本语法**
```cpp
class Animal {
public:
    virtual void speak() {  // 虚函数
        cout << "Animal sound" << endl;
    }
    virtual ~Animal() {}  // 虚析构函数
};

class Dog : public Animal {
public:
    void speak() override {  // 重写（C++11推荐加override）
        cout << "Woof!" << endl;
    }
};

// 多态调用
Animal* ptr = new Dog();
ptr->speak();  // 输出 "Woof!" （动态绑定）
delete ptr;
```

**2. 纯虚函数与抽象类**
```cpp
class Shape {
public:
    virtual double area() = 0;  // 纯虚函数
    virtual void draw() = 0;
};

class Circle : public Shape {
public:
    double radius;
    double area() override {
        return 3.14 * radius * radius;
    }
    void draw() override {
        cout << "Drawing circle" << endl;
    }
};

// Shape s;  // 错误：抽象类不能实例化
Circle c;    // 正确
```

**3. 虚函数表（vtable）机制**
```
对象内存布局：
┌─────────────┐
│ vptr        │ → 指向虚函数表
├─────────────┤
│ 成员变量    │
└─────────────┘

虚函数表：
┌─────────────┐
│ &func1      │
│ &func2      │
│ &func3      │
└─────────────┘
```
- 每个包含虚函数的类有一个虚函数表
- 对象有一个vptr指向类的虚函数表
- 运行时通过vptr查找正确的函数地址

**4. 虚析构函数**
```cpp
class Base {
public:
    virtual ~Base() {  // 必须是虚析构
        cout << "~Base()" << endl;
    }
};

class Derived : public Base {
public:
    ~Derived() {
        cout << "~Derived()" << endl;
    }
};

Base* ptr = new Derived();
delete ptr;  // 调用 ~Derived()，再调用 ~Base()
// 如果析构不是虚函数，只会调用 ~Base()，内存泄漏！
```

**5. override 和 final（C++11）**
```cpp
class Base {
public:
    virtual void func1() {}
    virtual void func2() final;  // 禁止重写
};

class Derived : public Base {
public:
    void func1() override;  // 明确表示重写
    // void func2() override;  // 错误：func2是final
};

class Final final {  // 禁止继承
};
```

**6. 虚函数 vs 普通函数**
| 特性 | 虚函数 | 普通函数 |
|------|--------|----------|
| 绑定 | 动态绑定（运行时） | 静态绑定（编译时） |
| 开销 | 有额外开销（vtable查找） | 无额外开销 |
| 多态 | 支持 | 不支持 |
| 默认参数 | 使用基类的 | 使用声明类型的 |

## 应用场景
- 面向对象设计：实现接口和抽象类
- 框架开发：回调机制、策略模式
- 游戏引擎：Entity类层次结构
- GUI库：事件处理系统
- 插件系统：加载不同实现

## 注意事项
- 基类析构函数必须是虚函数（多态使用时）
- 构造函数不能是虚函数
- 静态函数不能是虚函数
- 内联函数可以是虚函数（但无法内联）
- 虚函数的默认参数使用基类的值
- 性能开销：每次调用需要查表

## 关联知识
与 [[C++_引用]]、[[C++_智能指针]]、[[C++_模板]] 相关。
