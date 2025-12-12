# C++ 智能指针

## 定义
智能指针是C++11引入的自动内存管理工具，封装原始指针并在对象生命周期结束时自动释放内存，通过RAII机制避免内存泄漏和悬垂指针。主要包括unique_ptr、shared_ptr、weak_ptr。

## 核心内容
**1. unique_ptr（独占所有权）**
```cpp
#include <memory>

// 创建
unique_ptr<int> p1(new int(10));
auto p2 = make_unique<int>(20);  // C++14推荐

// 访问
*p1 = 30;
cout << *p1;

// 转移所有权（移动语义）
unique_ptr<int> p3 = move(p1);  // p1变为nullptr
// unique_ptr<int> p4 = p3;     // 错误：不能拷贝

// 数组
unique_ptr<int[]> arr(new int[10]);
auto arr2 = make_unique<int[]>(10);  // C++14
arr[0] = 100;

// 自动释放
{
    unique_ptr<int> temp(new int(5));
}  // 作用域结束，自动delete
```

**2. shared_ptr（共享所有权）**
```cpp
// 创建
shared_ptr<int> sp1(new int(10));
auto sp2 = make_shared<int>(20);  // 推荐（一次内存分配）

// 共享所有权
shared_ptr<int> sp3 = sp2;  // 引用计数+1
cout << sp2.use_count();    // 输出 2

// 自动释放
{
    shared_ptr<int> sp4 = sp2;  // 引用计数=3
    cout << sp2.use_count();    // 3
}  // sp4析构，引用计数-1
cout << sp2.use_count();  // 2

// 最后一个shared_ptr析构时释放内存
```

**3. weak_ptr（弱引用，解决循环引用）**
```cpp
class B;
class A {
public:
    shared_ptr<B> bptr;
    ~A() { cout << "~A()" << endl; }
};

class B {
public:
    weak_ptr<A> aptr;  // 使用weak_ptr打破循环
    ~B() { cout << "~B()" << endl; }
};

// 使用
shared_ptr<A> a = make_shared<A>();
shared_ptr<B> b = make_shared<B>();
a->bptr = b;
b->aptr = a;  // 不增加引用计数

// 访问weak_ptr指向的对象
if (auto sp = b->aptr.lock()) {  // 尝试获取shared_ptr
    // 使用sp
}
```

**4. 循环引用问题**
```cpp
// 错误示例
class Node {
public:
    shared_ptr<Node> next;  // 双向链表循环引用
    shared_ptr<Node> prev;
};

shared_ptr<Node> n1 = make_shared<Node>();
shared_ptr<Node> n2 = make_shared<Node>();
n1->next = n2;
n2->prev = n1;  // 循环引用，内存泄漏！

// 正确做法
class Node {
public:
    shared_ptr<Node> next;
    weak_ptr<Node> prev;  // 使用weak_ptr
};
```

**5. 自定义删除器**
```cpp
// 文件指针
auto deleter = [](FILE* fp) {
    if (fp) fclose(fp);
};
unique_ptr<FILE, decltype(deleter)> fp(fopen("test.txt", "r"), deleter);

// shared_ptr
shared_ptr<int> sp(new int[10], [](int* p) { delete[] p; });
```

**6. 智能指针对比**
| 类型 | 拷贝 | 移动 | 开销 | 用途 |
|------|------|------|------|------|
| unique_ptr | ✗ | ✓ | 几乎无 | 独占资源 |
| shared_ptr | ✓ | ✓ | 引用计数 | 共享资源 |
| weak_ptr | ✓ | ✓ | 小 | 观察资源 |

**7. 注意事项代码**
```cpp
// 不要混用原始指针和智能指针
int* raw = new int(10);
shared_ptr<int> sp1(raw);
shared_ptr<int> sp2(raw);  // 错误：double free

// 使用make_shared/make_unique
auto sp = make_shared<int>(10);  // 推荐
shared_ptr<int> sp(new int(10)); // 不推荐（两次内存分配）

// 不要从this创建shared_ptr
class MyClass {
    void bad() {
        shared_ptr<MyClass> sp(this);  // 错误！
    }
};

// 使用enable_shared_from_this
class MyClass : public enable_shared_from_this<MyClass> {
    void good() {
        auto sp = shared_from_this();  // 正确
    }
};
```

## 应用场景
- 资源管理：文件、网络连接、数据库句柄
- 容器元素：vector<unique_ptr<Base>>
- 工厂模式：返回智能指针
- 观察者模式：weak_ptr避免循环引用
- 异常安全：自动清理资源

## 注意事项
- 优先使用unique_ptr（开销最小）
- 使用make_shared/make_unique创建
- 避免循环引用（使用weak_ptr）
- 不要从原始指针创建多个shared_ptr
- 性能：shared_ptr有原子操作开销
- 不要过度使用智能指针（值语义优先）

## 关联知识
与 [[指针]]、[[动态内存分配]]、[[C++_引用]]、[[C++_模板]] 相关。
