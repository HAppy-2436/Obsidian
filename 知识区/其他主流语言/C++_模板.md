# C++ 模板

## 定义
模板（Template）是C++泛型编程的核心机制，允许函数或类以类型作为参数，编译时根据具体类型生成代码，实现代码复用和类型安全的泛型算法。

## 核心内容
**1. 函数模板**
```cpp
// 基本语法
template <typename T>
T max(T a, T b) {
    return (a > b) ? a : b;
}

// 使用
int i = max(10, 20);        // T = int
double d = max(3.14, 2.71); // T = double
max<int>(10, 20);           // 显式指定类型
```

**2. 类模板**
```cpp
template <typename T>
class Stack {
private:
    T data[100];
    int top;
public:
    Stack() : top(-1) {}
    void push(T val) { data[++top] = val; }
    T pop() { return data[top--]; }
};

// 使用
Stack<int> s1;
Stack<string> s2;
```

**3. 多类型参数**
```cpp
template <typename T1, typename T2>
class Pair {
public:
    T1 first;
    T2 second;
    Pair(T1 f, T2 s) : first(f), second(s) {}
};

Pair<int, string> p(1, "hello");
```

**4. 非类型模板参数**
```cpp
template <typename T, int SIZE>
class Array {
private:
    T data[SIZE];
public:
    int size() { return SIZE; }
};

Array<int, 10> arr; // SIZE是编译时常量
```

**5. 模板特化**
```cpp
// 全特化
template <>
class Stack<bool> {
    // bool专门的实现（使用位存储）
};

// 偏特化
template <typename T>
class Stack<T*> {
    // 指针类型的特殊实现
};
```

**6. 模板与STL**
```cpp
// STL容器都是类模板
vector<int> vec;
map<string, int> m;
set<double> s;

// STL算法是函数模板
sort(vec.begin(), vec.end());
find(vec.begin(), vec.end(), 5);
```

## 应用场景
- 泛型容器：vector、list、map等STL容器
- 通用算法：排序、查找、遍历等与类型无关的操作
- 智能指针：unique_ptr<T>、shared_ptr<T>
- 数学库：矩阵、向量运算
- 元编程：编译时计算

## 注意事项
- 模板代码通常放在头文件中（编译时需要看到完整定义）
- 模板实例化发生在编译时，会增加编译时间和二进制大小
- 模板错误信息冗长难懂
- typename和class在模板参数中基本等价（推荐用typename）
- 模板不是多态（编译时确定，非运行时）

## 关联知识
与 [[C++_STL]]、[[C++_智能指针]]、[[C++_引用]] 相关。
