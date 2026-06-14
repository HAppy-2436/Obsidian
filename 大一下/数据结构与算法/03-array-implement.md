---
title: 动态数组的代码实现
tags: [数据结构, 数组, 实现]
order: 3
prerequisites: [02-array-basic]
group: 数组
paywall: false
source: labuladong
---

# 动态数组的代码实现

> [!info] 章节定位
> 上一章讲了静态数组的内存模型和复杂度分析；本章动手实现一个动态数组 `MyArrayList`，把「末尾追加 / 中间插入 / 末尾删除 / 中间删除 / 自动扩缩容 / 索引越界」全部落到代码。理解这一章后，标准库里的 `std::vector` / `ArrayList` / `list` 就不再神秘。

## 📚 学习目标

- 用 C++ 实现一个**模板类** `MyArrayList<T>`，支持 8 个核心 API
- 理解「**自动扩缩容**」的触发条件与实现细节
- 区分 `checkElementIndex`（不允许 `index == size`）和 `checkPositionIndex`（允许 `index == size`）的本质
- 知道删除元素时「清空引用」的目的——避免内存泄漏
- 能用本实现去解 LeetCode 707「设计链表」验证正确性

## 🎯 一句话总结

> 动态数组 = **静态数组 + 增删查改 API + 自动扩缩容**；本章实现一个 `MyArrayList<T>`，重点是「扩容 / 缩容触发条件」「两类越界检查」「删除时清空引用」三个关键点。

## 🔗 前置知识

- [[00-intro|本章导读]]
- [[01-complexity|时间空间复杂度入门]]
- [[02-array-basic|数组原理]] — 上一章必读
- C++ 模板类基础语法

## 📖 正文

### 1. 关键点一：自动扩缩容

#### 1.1 扩容（grow）

「扩容」是数组最贵的操作（`O(n)`），所以我们要尽可能**少触发**。

最常见的策略是**倍增**（geometric expansion）：

- 当 `size == capacity` 时，扩容为 `2 * capacity`。
- 每次扩容后，下一次填满的成本被「摊销」到之前的 N/2 次插入上，整体摊销复杂度是 `O(1)`。

> [!tip] 为什么是「2 倍」而不是「1.5 倍」或「3 倍」？
> - 1.5 倍：扩容次数多、均摊成本偏高，但内存利用率高。
> - 2 倍：是工程折中（Java `ArrayList` 用 1.5，C++ `std::vector` 用 2，Python `list` 也接近 2）。
> - 3 倍：扩容次数少，但浪费的尾部空间多。

#### 1.2 缩容（shrink）

只扩容不缩容，会让数组长期占用远超实际需要的内存（比如装 10 个元素但底层分配了 1000 个槽）。

常见的「懒缩容」策略是：

- 当 `size <= capacity / 4` 时，缩容为 `capacity / 2`。
- 「除以 4」而不是「除以 2」是避免「删一个加一个」时反复扩缩容（**颠簸**）。

```text
size=100, cap=200  满
删到 size=50, cap/4=50  → 触发缩容，cap=100
再删一个 size=49, cap/4=25 → 不触发
...
继续删到 size=25, cap/4=25  → 触发缩容，cap=50
```

> 这种「缩到 1/2，缩容门槛设 1/4」的滞后策略，能让扩缩容次数摊销 O(1)。

### 2. 关键点二：两类索引越界检查

动态数组的索引语义有两种：

| 语义 | 允许的范围 | 用途 |
| --- | --- | --- |
| **元素位置** | `0 <= i < size` | `get(i)`、`set(i, v)`、`remove(i)` |
| **插入空隙** | `0 <= i <= size` | `add(i, v)`——可以在末尾「空隙」追加 |

下面这段示意图能说明区别：

```text
nums = [5, 6, 7, 8]
index   0  1  2  3
        ^元素位置: 0..3

如果要在数组中插入新元素，插入位置不是「元素位置」，
而是元素之间的「空隙」：
[ | 5 | 6 | 7 | 8 | ]
   0   1   2   3   4
   ^空隙位置: 0..4
```

因此：

```cpp
bool isElementIndex(int i) { return i >= 0 && i < size; }
bool isPositionIndex(int i) { return i >= 0 && i <= size; }
```

只有「插入」相关方法用 `checkPositionIndex`；其他都使用 `checkElementIndex`。

### 3. 关键点三：删除元素要清空引用

看下面这段 `removeLast`：

```cpp
E removeLast() {
    E deletedVal = data[size - 1];
    data[size - 1] = null;   // <-- 这一行不能少
    size--;
    return deletedVal;
}
```

如果省略 `data[size - 1] = null`，对于 Java/C# 等**带 GC 的语言**，会发生**内存泄漏**：data 数组这个槽还引用着对象，GC 判定它「可达」，于是这个对象永远不会被回收。

对 C++，`std::vector` 用 RAII 自动析构，不会有这个泄漏问题，但**显式清空是个好习惯**（比如存的是 `std::shared_ptr` 时）。

### 4. 关键点四：底层是「裸数组 + size + capacity」三件套

```cpp
template<typename T>
class MyArrayList {
    T*   data;       // 真正的存储（裸数组）
    int  size_;      // 已有元素个数
    int  capacity_;  // 底层数组总长度
    static constexpr int INIT_CAP = 1;
    ...
};
```

`data` 是连续内存，`size_` 是逻辑长度（外部可见的「size()」），`capacity_` 是物理长度（`data` 的真实长度）。`size_ <= capacity_` 永远成立。

### 5. 完整 C++ 实现

```cpp
#include <bits/stdc++.h>
using namespace std;

namespace dsa {

template <typename T>
class MyArrayList {
private:
    T*   data_;       // 底层存储
    int  size_;       // 已有元素个数
    int  capacity_;   // 底层数组容量

    static constexpr int INIT_CAP = 1;

    // 工具：把容量扩/缩到 newCap
    void resize(int newCap) {
        T* tmp = new T[newCap];
        for (int i = 0; i < size_; ++i) {
            tmp[i] = data_[i];   // 对内置类型是拷贝；对复杂类型会调拷贝构造
        }
        delete[] data_;
        data_ = tmp;
        capacity_ = newCap;
    }

    bool isElementIndex(int i) const { return i >= 0 && i < size_; }
    bool isPositionIndex(int i) const { return i >= 0 && i <= size_; }

    void checkElementIndex(int i) const {
        if (!isElementIndex(i)) {
            throw out_of_range("Index: " + to_string(i) +
                               ", Size: " + to_string(size_));
        }
    }
    void checkPositionIndex(int i) const {
        if (!isPositionIndex(i)) {
            throw out_of_range("Index: " + to_string(i) +
                               ", Position max: " + to_string(size_));
        }
    }

public:
    // ===== 构造 / 析构 =====
    MyArrayList() : MyArrayList(INIT_CAP) {}
    explicit MyArrayList(int initCap) : size_(0), capacity_(initCap) {
        if (initCap < 1) initCap = 1;
        data_ = new T[initCap];
    }
    ~MyArrayList() { delete[] data_; }

    // 禁用拷贝（C++ 教程简化处理；生产代码应写深拷贝或 =delete）
    MyArrayList(const MyArrayList&) = delete;
    MyArrayList& operator=(const MyArrayList&) = delete;

    // ===== 增 =====
    void addLast(const T& e) {
        if (size_ == capacity_) {
            resize(2 * capacity_);
        }
        data_[size_++] = e;
    }

    void addFirst(const T& e) {
        add(0, e);
    }

    void add(int index, const T& e) {
        checkPositionIndex(index);
        if (size_ == capacity_) {
            resize(2 * capacity_);
        }
        // 从后往前搬移
        for (int i = size_ - 1; i >= index; --i) {
            data_[i + 1] = data_[i];
        }
        data_[index] = e;
        size_++;
    }

    // ===== 删 =====
    T removeLast() {
        if (size_ == 0) throw runtime_error("removeLast from empty list");
        if (size_ == capacity_ / 4) {
            resize(capacity_ / 2);
        }
        T val = data_[size_ - 1];
        data_[size_ - 1] = T();   // 清空
        size_--;
        return val;
    }

    T removeFirst() {
        return remove(0);
    }

    T remove(int index) {
        checkElementIndex(index);
        if (size_ == capacity_ / 4) {
            resize(capacity_ / 2);
        }
        T val = data_[index];
        // 从前往后搬移
        for (int i = index + 1; i < size_; ++i) {
            data_[i - 1] = data_[i];
        }
        data_[size_ - 1] = T();   // 清空
        size_--;
        return val;
    }

    // ===== 查 / 改 =====
    T get(int index) const {
        checkElementIndex(index);
        return data_[index];
    }

    T set(int index, const T& e) {
        checkElementIndex(index);
        T old = data_[index];
        data_[index] = e;
        return old;
    }

    // ===== 工具 =====
    int  size()     const { return size_; }
    bool isEmpty()  const { return size_ == 0; }
    int  capacity() const { return capacity_; }

    void display() const {
        cout << "size=" << size_ << " cap=" << capacity_ << " [";
        for (int i = 0; i < size_; ++i) {
            if (i) cout << ", ";
            cout << data_[i];
        }
        cout << "]\n";
    }
};

} // namespace dsa

// ===== 简单测试 =====
int main() {
    dsa::MyArrayList<int> arr(3);
    for (int i = 1; i <= 5; ++i) arr.addLast(i);
    arr.display();                 // size=5 cap=6
    arr.remove(3);
    arr.add(1, 9);
    arr.addFirst(100);
    int v = arr.removeLast();
    (void)v;
    arr.display();
    return 0;
}
```

### 6. 关键操作的复杂度总结

| 操作 | 时间复杂度 | 备注 |
| --- | --- | --- |
| `addLast(e)` | 摊销 `O(1)` | 单次可能 `O(n)` 扩容 |
| `addFirst(e)` | `O(n)` | 全部搬移 |
| `add(i, e)` | `O(n)` | index 之后搬移 |
| `removeLast()` | 摊销 `O(1)` | 单次可能 `O(n)` 缩容 |
| `removeFirst()` | `O(n)` | 全部搬移 |
| `remove(i)` | `O(n)` | index 之后搬移 |
| `get(i)` | `O(1)` | 随机访问 |
| `set(i, e)` | `O(1)` | 随机访问 |

### 7. 几个工程细节

#### 7.1 为什么扩容时用 `new T[newCap]` 而不是 `realloc`？

C++ 中 `T` 可能是带构造/析构函数的对象，`realloc` 不会调用构造函数（甚至会浅拷贝对象，破坏其内部指针）。我们用 `new T[]` + 循环赋值，让编译器正确处理非平凡类型。

#### 7.2 为什么 `add` 时扩容和搬移分开？

把 `resize` 单独抽成函数，是为了让「扩缩容」成为一个原子操作，外部看不到「半新半旧」的中间状态。

#### 7.3 异常安全

- `add` 流程：先检查索引 → 扩容 → 搬移 → 写入。  
  扩容失败（`bad_alloc`）时，原数组不变，安全。
- `remove` 流程：先检查索引 → 缩容 → 搬移 → 清空。  
  同样安全。

#### 7.4 怎样验证你的实现

> [!tip] 练手建议
> 1. 跑一遍 `main()` 的测试，覆盖 add/remove/set/get。
> 2. 改用「初始容量 1」，连续 `addLast 1000` 次，用 `cout << arr.capacity();` 观察容量从 1 → 2 → 4 → 8 → ... → 1024 的扩缩规律。
> 3. 拿到 LeetCode 707「设计链表」——它的 API 名字不同，但内部用「数组」实现可以过；你就用 `MyArrayList` 套一层，验证正确性。

### 8. 与 `std::vector` 的差异

| 特性 | 本章 `MyArrayList` | `std::vector` |
| --- | --- | --- |
| 模板 | ✅ | ✅ |
| 自动扩容 | ✅ 倍增 | ✅ 倍增（GCC 下大致 2 倍） |
| 自动缩容 | ✅ 1/4 触发 | ❌ 只在 `shrink_to_fit` 时缩 |
| 迭代器 | ❌ | ✅ 随机访问迭代器 |
| 移动语义 | ❌ | ✅ |
| 异常安全 | 基础 | 强保证（commit/rollback） |
| 内存分配器 | 默认 `new/delete` | 可自定义 Allocator |

`std::vector` 远比我们的玩具版复杂，但**核心思想一致**。

## 📊 复杂度一览

| 操作 | 时间 | 空间 | 备注 |
| --- | --- | --- | --- |
| 增（尾） | 摊销 O(1) | O(1) 摊销 | 单次最坏 O(n) |
| 增（头/中） | O(n) | O(1) | 搬移 |
| 删（尾） | 摊销 O(1) | O(1) 摊销 | 单次最坏 O(n) |
| 删（头/中） | O(n) | O(1) | 搬移 |
| 查 / 改（按索引） | O(1) | O(1) | 随机访问 |
| 整体拷贝构造 | O(n) | O(n) | 拷贝所有元素 |

## 🛠️ 应用场景

- **写题 / 面试**：手写 `MyArrayList` 是入门数据结构最常考的「白板题」之一。
- **理解标准库**：知道 `std::vector` / `ArrayList` 内部就是这玩意儿，再去看源码就不会迷路。
- **构造更复杂结构**：[[08-queue-stack-basic|栈]] 和 [[09-array-queue-stack|用数组实现队列]] 都用 `MyArrayList` 当底层。
- **性能分析**：当遇到「vector 突然卡顿」时，怀疑扩容；用 `vector::capacity()` 打印验证。

## ▶️ 下一章

[[04-cycle-array|循环数组技巧及实现]] — 用「求模」让数组在「逻辑上」变成环形，从而让头尾增删也变 O(1)。

## 🔗 相关章节

- [[02-array-basic|数组原理]] — 上一章
- [[04-cycle-array|环形数组]] — 下一章
- [[07-deque-implement|双端队列]] — 头尾都要 O(1) 的标准容器
- [[08-queue-stack-basic|队列/栈]] — 数组实现的两种最简单结构
- [[11-hashtable-with-array|数组哈希表]] — 数组的另一重要应用
