---
title: 循环数组技巧及实现
tags: [数据结构, 数组, 技巧, 环形数组]
order: 4
prerequisites: [03-array-implement]
group: 数组
subgroup: 变体
paywall: false
source: labuladong
---

# 循环数组技巧及实现

> [!info] 章节定位
> 上一章的 `MyArrayList` 头部增删还是 O(n)。本章用「求模 + 双指针」把数组「逻辑上」变成环形，让头尾 O(1) 增删成为可能。本章也是 [[07-deque-implement|双端队列]]、[[10-linked-queue-stack|循环队列]] 的核心技术。

## 📚 学习目标

- 理解「数组不可能真的成为环形，但**逻辑上**可以」的核心理念
- 掌握「**左闭右开** `[start, end)`」区间约定的便利性
- 理解 `start` / `end` 两个指针如何配合 `count` 维护「逻辑长度」
- 能写出支持 `addFirst / addLast / removeFirst / removeLast / getFirst / getLast` 的 `CycleArray<T>`
- 能分析「为什么标准库的 `vector` 不用环形数组」

## 🎯 一句话总结

> 用「**求模**」让 `start` / `end` 两个指针在数组里**转圈**，配合「**左闭右开**」约定，实现头尾 O(1) 增删；底层仍是普通数组，但逻辑上是一个**不会满**的环。

## 🔗 前置知识

- [[00-intro|本章导读]]
- [[01-complexity|时间空间复杂度入门]]
- [[02-array-basic|数组原理]]
- [[03-array-implement|动态数组实现]] — 上一章

## 📖 正文

### 1. 数组能「环形」吗？

**不能**。数组在物理上是一段线性连续的内存，地址从 `arr[0]` 增长到 `arr[n-1]`，最后不可能「绕回 `arr[0]`」。

**但我们可以让数组在「逻辑上」是环形的**，方法很简单：用「**求模**」让索引在「越界」时跳回另一端。

```text
物理数组：[ _ _ _ _ _ ]
         0 1 2 3 4

逻辑上看：
  start → 1, 2, 3, 4, 5, 1, 2, 3, ...
  end   → 3, 4, 5, 6, 7, 3, 4, 5, ...
  ↑ 用 (i + 1) % size 把 5 跳回 0
```

一段最小可运行示例：

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    int arr[5] = {1, 2, 3, 4, 5};
    int i = 0;
    // 模拟「永远遍历不完」的环形数组
    for (int step = 0; step < 12; ++step) {
        cout << arr[i] << " ";
        i = (i + 1) % 5;
    }
    cout << "\n";
    // 输出 1 2 3 4 5 1 2 3 4 5 1 2
    return 0;
}
```

### 2. 用环形数组实现「头尾 O(1) 增删」

假设我们有一个容量 6 的数组，装了 3 个元素（`_` 表示空槽）：

```text
物理:   [1, 2, 3, _, _, _]
         0  1  2  3  4  5
逻辑:   [1, 2, 3]    start=0, end=3, count=3
```

现在「删除头部元素 1」——不需要搬移，只要 `start` 指针右移一格：

```text
物理:   [_, 2, 3, _, _, _]
         0  1  2  3  4  5
逻辑:   [2, 3]       start=1, end=3, count=2
```

再「头部插入 4」——`start` 指针左移一格，写入新元素：

```text
物理:   [4, 2, 3, _, _, _]
         0  1  2  3  4  5
逻辑:   [4, 2, 3]    start=0, end=3, count=3
```

再「头部插入 5」——`start` 要左移到 -1，**求模转一圈**，跳到末尾：

```text
物理:   [4, 2, 3, _, _, 5]
         0  1  2  3  4  5
逻辑:   [5, 4, 2, 3] start=5, end=3, count=4
```

> [!tip] 关键
> 这就是「**环形数组**」的精髓：不用搬移，**头尾操作都只是改指针 + 求模**。

### 3. 区间约定：左闭右开 `[start, end)`

我们要用「`start` 指向第一个有效元素，`end` 指向最后一个有效元素的下一个位置」来定义有效区间 `[start, end)`：

| 状态 | `start` | `end` | `count` | 含义 |
| --- | --- | --- | --- | --- |
| 空数组 | 0 | 0 | 0 | 区间 `[0, 0)` 没元素 |
| 满数组 | 0 | 6 | 6 | `start == end` 既是空，也是满（用 `count == capacity` 区分） |
| 一个元素 | 0 | 1 | 1 | 区间 `[0, 1)` 一个元素 |
| 头部插入 | `(start - 1 + cap) % cap` | — | +1 | 注意先移再写 |
| 头部删除 | — | — | -1 | 先取再移 |
| 尾部插入 | — | `(end + 1) % cap` | +1 | 先写再移 |
| 尾部删除 | — | `(end - 1 + cap) % cap` | -1 | 注意先移再清 |

#### 为什么要用「左闭右开」？

| 约定 | 空数组 | 「加一个元素」后 | 优点 |
| --- | --- | --- | --- |
| 左闭右开 `[s, e)` | `[0, 0)` 空 | `[0, 1)` 1 个 | **零特判**，初始 `s==e` |
| 左闭右闭 `[s, e]` | `[0, 0]` 含 1 个（！） | `[0, 1]` 含 2 个 | 初始状态非空，边界要特判 |
| 左开右开 `(s, e)` | `(0, 0)` 空 | `(0, 1)` 仍空 | 永远空？边界处理复杂 |

> 选「左闭右开」是**最不费脑**的：初始 `s==e==0` 表示空，「追加一个」只要 `arr[e++] = v`，**完全不用特判空状态**。

### 4. 完整 C++ 实现：`CycleArray<T>`

```cpp
#include <bits/stdc++.h>
using namespace std;

namespace dsa {

template <typename T>
class CycleArray {
private:
    T*   data_;     // 底层数组
    int  start_;    // 第一个有效元素位置（闭）
    int  end_;      // 最后一个有效元素的下一个位置（开）
    int  count_;    // 有效元素个数
    int  cap_;      // 容量

    // 重新分配容量
    void resize(int newCap) {
        T* tmp = new T[newCap];
        // 把「逻辑上」从 start_ 开始的 count_ 个元素，按顺序拷到新数组 [0..count_)
        for (int i = 0; i < count_; ++i) {
            tmp[i] = data_[(start_ + i) % cap_];
        }
        delete[] data_;
        data_ = tmp;
        cap_  = newCap;
        start_ = 0;
        end_   = count_;
    }

public:
    explicit CycleArray(int cap = 1) : start_(0), end_(0), count_(0), cap_(max(1, cap)) {
        data_ = new T[cap_];
    }
    ~CycleArray() { delete[] data_; }

    CycleArray(const CycleArray&) = delete;
    CycleArray& operator=(const CycleArray&) = delete;

    // ===== 增 =====
    void addLast(const T& v) {
        if (isFull()) resize(cap_ * 2);
        // end_ 是开区间：先写，再右移
        data_[end_] = v;
        end_ = (end_ + 1) % cap_;
        count_++;
    }

    void addFirst(const T& v) {
        if (isFull()) resize(cap_ * 2);
        // start_ 是闭区间：先左移，再写
        start_ = (start_ - 1 + cap_) % cap_;
        data_[start_] = v;
        count_++;
    }

    // ===== 删 =====
    T removeFirst() {
        if (isEmpty()) throw runtime_error("removeFirst from empty");
        T v = data_[start_];
        data_[start_] = T();          // 清空引用
        start_ = (start_ + 1) % cap_;
        count_--;
        if (count_ > 0 && count_ == cap_ / 4) resize(cap_ / 2);
        return v;
    }

    T removeLast() {
        if (isEmpty()) throw runtime_error("removeLast from empty");
        // end_ 是开区间：先左移，再取
        end_ = (end_ - 1 + cap_) % cap_;
        T v = data_[end_];
        data_[end_] = T();
        count_--;
        if (count_ > 0 && count_ == cap_ / 4) resize(cap_ / 2);
        return v;
    }

    // ===== 查 =====
    T getFirst() const {
        if (isEmpty()) throw runtime_error("getFirst from empty");
        return data_[start_];
    }
    T getLast() const {
        if (isEmpty()) throw runtime_error("getLast from empty");
        return data_[(end_ - 1 + cap_) % cap_];
    }
    // 按「逻辑索引」访问
    T get(int i) const {
        if (i < 0 || i >= count_) throw out_of_range("i out of range");
        return data_[(start_ + i) % cap_];
    }

    // ===== 状态 =====
    bool isEmpty() const { return count_ == 0; }
    bool isFull()  const { return count_ == cap_; }
    int  size()    const { return count_; }
    int  capacity() const { return cap_; }

    void display() const {
        cout << "size=" << count_ << " cap=" << cap_ << " [";
        for (int i = 0; i < count_; ++i) {
            if (i) cout << ", ";
            cout << get(i);
        }
        cout << "] (start=" << start_ << ", end=" << end_ << ")\n";
    }
};

} // namespace dsa

int main() {
    dsa::CycleArray<int> ca(3);
    ca.addLast(1);
    ca.addLast(2);
    ca.addLast(3);   // 触发扩容 cap=6
    ca.addFirst(0);
    ca.addLast(4);
    ca.display();    // size=5 cap=6 [0, 1, 2, 3, 4]

    cout << "front=" << ca.getFirst() << " back=" << ca.getLast() << "\n";

    ca.removeFirst();
    ca.removeLast();
    ca.display();    // size=3 cap=6

    return 0;
}
```

### 5. 复杂度

| 操作 | 时间 | 备注 |
| --- | --- | --- |
| `addFirst` | 摊销 `O(1)` | 单次扩容 O(n) |
| `addLast` | 摊销 `O(1)` | 同上 |
| `removeFirst` | 摊销 `O(1)` | 单次缩容 O(n) |
| `removeLast` | 摊销 `O(1)` | 同上 |
| `getFirst` / `getLast` | `O(1)` | 直接读 |
| `get(i)`（逻辑索引） | `O(1)` | 算地址 + 一次访存 |

> 头尾操作全部 `O(1)`，**这是普通动态数组做不到的**。

### 6. 思考题：标准库为什么不用环形数组？

环形数组已经能做到头尾 O(1) 增删，为什么 C++ `std::vector`、Java `ArrayList` 都不用？

思考这几个角度：

1. **按索引随机访问要算一次 `(start + i) % cap`**：多了一次模运算（虽然仍是 O(1)，但常数稍大；不过现代编译器优化后差异很小）。
2. **删除/插入「中间」还是要搬移**，且搬移时元素可能跨越物理数组中段，cache 不友好。
3. **`resize` 时要按逻辑顺序重排**，比普通 `vector` 的简单 `memcpy` 复杂。
4. **「按值查索引」必须先 `get(i)` 再比较**，**无法**像 `vector` 那样用 `memcmp` / SIMD 加速。
5. **迭代器语义**：环形数组的迭代器「跨边界」要小心，标准库迭代器要求**所有有效元素在 `[begin, end)` 连续存储**，环形数组天然不满足。

所以工程上**「环形数组」更适合作为 [[07-deque-implement|双端队列]]、[[10-linked-queue-stack|循环队列]] 的内部实现**——这两个容器的接口本来就**只在头尾操作**，正好契合环形数组的优势，避开了它的劣势。

### 7. 环形数组 vs 普通数组 vs 链表

| 维度 | 普通数组 `vector` | 环形数组 `CycleArray` | 双向链表 `list` |
| --- | --- | --- | --- |
| 头部增删 | O(n) 搬移 | **O(1)** | O(1) |
| 尾部增删 | 摊销 O(1) | O(1) | O(1)（有尾指针） |
| 随机访问 | **O(1)** | O(1)（多一次模） | O(n) |
| 中间插入 | O(n) | O(n) | O(1)（已知位置） |
| 内存布局 | **连续**，cache 友好 | 连续，cache 友好 | 分散，cache 不友好 |
| 内存开销 | 紧凑 | 紧凑（+2 个指针） | 每节点 +2 指针 |
| 迭代器 | 简单 | 复杂（跨边界） | 简单（节点指针） |

> **没有银弹**：写代码前先想清楚「哪些操作是热点」，再选数据结构。

## 📊 复杂度一览

| 操作 | 时间 | 空间 | 备注 |
| --- | --- | --- | --- |
| 头/尾插入 | 摊销 O(1) | O(1) | 偶发扩容 |
| 头/尾删除 | 摊销 O(1) | O(1) | 偶发缩容 |
| get(i) 随机访问 | O(1) | O(1) | 比 vector 多一次模 |
| isEmpty/isFull | O(1) | O(1) | 直接判 count |
| 整体扩容 resize | O(n) | O(n) | 按逻辑顺序重排 |

## 🛠️ 应用场景

- **双端队列（Deque）底层**：见 [[07-deque-implement]]。
- **循环队列底层**：用 1 个数组 + 头尾指针实现 FIFO，比「head/tail + 队列搬移」简单。
- **滑动窗口**：固定大小窗口，环形数组天然适配「窗口右移 = 删一个、加一个」模式。
- **环形缓冲区（RingBuffer）**：日志、音视频帧、生产者-消费者模型的经典结构。

## ▶️ 下一章

[[05-linkedlist-basic|链表（链式存储）的原理]] — 数组的「连续性」既带来超能力也带来局限；链表用「指针串起来」走出另一条路，与数组对照学习。

## 🔗 相关章节

- [[03-array-implement|动态数组实现]] — 上一章
- [[05-linkedlist-basic|链表原理]] — 下一章
- [[07-deque-implement|双端队列]] — 本章直接复用的容器
- [[10-linked-queue-stack|链表实现队列/栈]] — 用链表实现也能头尾 O(1)
- [[11-hashtable-with-array|数组哈希表]] — 数组的另一重要应用
