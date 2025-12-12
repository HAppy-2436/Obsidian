# C++ 引用

## 定义
引用（Reference）是C++中的别名机制，为已存在的变量提供另一个名字。必须在声明时初始化，初始化后不能重新绑定到其他变量，主要用于函数参数传递和返回值。

## 核心内容
**1. 基本语法**
```cpp
int a = 10;
int& ref = a;  // ref是a的引用（别名）

ref = 20;      // 等价于 a = 20
cout << a;     // 输出 20
```

**2. 引用 vs 指针**
```cpp
int x = 5;

// 指针
int* p = &x;
*p = 10;       // 通过指针修改
p = nullptr;   // 可以重新指向

// 引用
int& r = x;
r = 10;        // 直接使用
// r = y;      // 这是赋值，不是重新绑定
```

**对比表**
| 特性 | 引用 | 指针 |
|------|------|------|
| 初始化 | 必须 | 可选 |
| 重新绑定 | 不可 | 可以 |
| 空值 | 无 | nullptr |
| 语法 | 直接使用 | 需要* |
| 底层实现 | 通常是指针 | 地址 |

**3. 函数参数（避免拷贝）**
```cpp
// 值传递（拷贝）
void func1(vector<int> v) {  // 拷贝整个vector
    v.push_back(10);
}

// 引用传递（无拷贝）
void func2(vector<int>& v) {  // 直接操作原对象
    v.push_back(10);
}

// const引用（只读，无拷贝）
void func3(const vector<int>& v) {
    cout << v.size();  // 只读访问
}
```

**4. 返回引用**
```cpp
// 返回局部变量引用（错误！）
int& bad_func() {
    int local = 10;
    return local;  // 悬垂引用
}

// 返回成员引用（正确）
class MyClass {
    int data;
public:
    int& getData() {
        return data;  // 对象存在时引用有效
    }
};

// 链式调用
class String {
public:
    String& append(const char* s) {
        // ...
        return *this;  // 返回自身引用
    }
};
String str;
str.append("hello").append(" world");
```

**5. 右值引用（C++11）**
```cpp
// 左值引用
int a = 10;
int& lr = a;  // 绑定到左值

// 右值引用
int&& rr = 10;  // 绑定到临时对象
int&& rr2 = a + b;  // 绑定到表达式结果

// 移动语义
class MyString {
    char* data;
public:
    // 移动构造函数
    MyString(MyString&& other) {
        data = other.data;
        other.data = nullptr;  // 转移所有权
    }
};
```

**6. 常见应用模式**
```cpp
// range-based for循环（避免拷贝）
for (const auto& item : vec) {
    cout << item;
}

// swap实现
void swap(int& a, int& b) {
    int temp = a;
    a = b;
    b = temp;
}

// 运算符重载
class Complex {
public:
    Complex& operator+=(const Complex& other) {
        // ...
        return *this;
    }
};
```

## 应用场景
- 大对象传递：避免拷贝开销（vector、string等）
- 修改参数：函数需要修改实参
- 运算符重载：返回*this实现链式调用
- 迭代器：容器元素的引用
- 移动语义：高效转移资源所有权

## 注意事项
- 不要返回局部变量的引用（悬垂引用）
- 引用不能为nullptr（但可能绑定到被删除的对象）
- 引用必须初始化，不能有引用数组
- const引用可以绑定到临时对象
- 引用占用存储空间（通常实现为指针）
- 优先使用const引用传递大对象

## 关联知识
与 [[指针]]、[[函数传参]]、[[C++_智能指针]]、[[C++_模板]] 相关。
