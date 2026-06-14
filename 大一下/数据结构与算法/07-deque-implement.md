---
title: 双端队列（Deque）原理和实现
tags: [数据结构, 双端队列, Deque, 数组链表技巧]
order: 7
prerequisites: [06-linkedlist-implement, 03-array-implement]
group: 数组链表技巧
paywall: false
source: labuladong
---

# 双端队列（Deque）原理和实现

> [!info] 章节定位
> 学完 [[04-cycle-array|环形数组]]、[[06-linkedlist-implement|链表实现]] 后，**双端队列（Deque）**就是把这两者的能力封装成一个标准容器。本章是「数组链表技巧」组的收官，也是 [[08-queue-stack-basic|队列/栈]] 的前置。

## 📚 学习目标

- 理解 Deque 与普通 Queue 的区别（队头也能增删）
- 知道「既能用链表实现，也能用环形数组实现」
- 能用 C++ 实现一个完整的 `MyArrayDeque<E>` 与 `MyListDeque<E>`
- 知道 Deque 是栈和队列的「超集」——能模拟两者
- 了解标准库（C++ `std::deque` / Java `ArrayDeque` / Python `deque`）的差异

## 🎯 一句话总结

> 双端队列就是「**头尾都能 O(1) 增删**」的容器：底层既可以挂双链表（`MyLinkedList`），也可以挂环形数组（`CycleArray`）；它是普通队列 + 普通栈的**能力超集**。

## 🔗 前置知识

- [[00-intro|本章导读]]
- [[01-complexity|时间空间复杂度入门]]
- [[03-array-implement|动态数组实现]] — 数组版本依赖
- [[04-cycle-array|环形数组]] — 数组版本依赖
- [[05-linkedlist-basic|链表原理]]
- [[06-linkedlist-implement|链表实现]] — 链表版本依赖

## 📖 正文

### 1. Deque 的 6 个 API

普通 Queue 只能「尾进头出」；Deque **两端**都能进能出。完整的 6 个 API：

```text
void   addFirst(E e)   // 头插
void   addLast(E e)    // 尾插
E      removeFirst()   // 头删
E      removeLast()    // 尾删
E      peekFirst()     // 看头
E      peekLast()      // 看尾
```

```cpp
#include <bits/stdc++.h>
using namespace std;

namespace dsa {

template <typename E>
class MyDeque {
public:
    virtual ~MyDeque() = default;
    virtual void addFirst (const E& e) = 0;
    virtual void addLast  (const E& e) = 0;
    virtual E    removeFirst()         = 0;
    virtual E    removeLast()          = 0;
    virtual E    peekFirst()    const  = 0;
    virtual E    peekLast()     const  = 0;
    virtual int  size()        const   = 0;
    virtual bool isEmpty()     const   = 0;
};

} // namespace dsa
```

> [!tip] 类比
> 普通队列好比「排队买票」——只准**末尾进、头部出**。  
> 双端队列好比「双向过街天桥」——**两头都能进，两头都能出**。  
> 因此 Deque 的元素**不再满足「先进先出」**——它灵活但失去了 FIFO 顺序保证。

### 2. 链表版 Deque：直接复用 `MyLinkedList`

> 上一章 [[06-linkedlist-implement]] 实现的 `MyLinkedList<E>` 已经有 `addFirst / addLast / removeFirst / removeLast / getFirst / getLast` 6 个方法——**正好就是 Deque 的 6 个 API**。

所以链表版 Deque 几乎只是包一层：

```cpp
#include <bits/stdc++.h>
using namespace std;

namespace dsa {

// 假设 MyLinkedList<E> 已经定义（见 06-linkedlist-implement）
template <typename E>
class MyLinkedList;   // 依赖前置声明

template <typename E>
class MyListDeque {
private:
    MyLinkedList<E> list_;
public:
    void addFirst (const E& e) { list_.addFirst(e); }
    void addLast  (const E& e) { list_.addLast(e); }
    E    removeFirst()         { return list_.removeFirst(); }
    E    removeLast()          { return list_.removeLast(); }
    E    peekFirst()    const  { return list_.getFirst(); }
    E    peekLast()     const  { return list_.getLast(); }
    int  size()        const   { return list_.size(); }
    bool isEmpty()     const   { return list_.isEmpty(); }
};

} // namespace dsa
```

一个完整可独立编译的版本（不依赖外部 `MyLinkedList`，把链表实现内联）：

```cpp
#include <bits/stdc++.h>
using namespace std;

namespace dsa {

template <typename E>
class MyListDeque {
private:
    struct Node {
        E     val;
        Node* prev;
        Node* next;
        Node(E v) : val(v), prev(nullptr), next(nullptr) {}
    };
    Node* head_;
    Node* tail_;
    int   size_;

public:
    MyListDeque() : size_(0) {
        head_ = new Node(E{});
        tail_ = new Node(E{});
        head_->next = tail_;
        tail_->prev = head_;
    }
    ~MyListDeque() {
        Node* p = head_;
        while (p) { Node* n = p->next; delete p; p = n; }
    }

    MyListDeque(const MyListDeque&) = delete;
    MyListDeque& operator=(const MyListDeque&) = delete;

    void addFirst(const E& e) {
        Node* n = new Node(e);
        n->next = head_->next;
        n->prev = head_;
        head_->next->prev = n;
        head_->next = n;
        size_++;
    }
    void addLast(const E& e) {
        Node* n = new Node(e);
        n->prev = tail_->prev;
        n->next = tail_;
        tail_->prev->next = n;
        tail_->prev = n;
        size_++;
    }
    E removeFirst() {
        if (size_ < 1) throw runtime_error("empty");
        Node* d = head_->next;
        head_->next = d->next;
        d->next->prev = head_;
        E v = d->val;
        d->prev = d->next = nullptr;
        delete d;
        size_--;
        return v;
    }
    E removeLast() {
        if (size_ < 1) throw runtime_error("empty");
        Node* d = tail_->prev;
        tail_->prev = d->prev;
        d->prev->next = tail_;
        E v = d->val;
        d->prev = d->next = nullptr;
        delete d;
        size_--;
        return v;
    }
    E peekFirst() const {
        if (size_ < 1) throw runtime_error("empty");
        return head_->next->val;
    }
    E peekLast() const {
        if (size_ < 1) throw runtime_error("empty");
        return tail_->prev->val;
    }
    int  size() const   { return size_; }
    bool isEmpty() const { return size_ == 0; }
};

} // namespace dsa

int main() {
    dsa::MyListDeque<int> dq;
    dq.addFirst(1);
    dq.addFirst(2);
    dq.addLast(3);
    dq.addLast(4);
    cout << dq.removeFirst() << "\n";  // 2
    cout << dq.removeLast()  << "\n";  // 4
    cout << dq.peekFirst()   << "\n";  // 1
    cout << dq.peekLast()    << "\n";  // 3
    return 0;
}
```

### 3. 数组版 Deque：复用 `CycleArray`

> [[04-cycle-array]] 实现的 `CycleArray<E>` 已经把头尾 O(1) 增删搞定了，Deque 只是再包一层。

完整可独立编译版本：

```cpp
#include <bits/stdc++.h>
using namespace std;

namespace dsa {

template <typename E>
class MyArrayDeque {
private:
    // 内联的 CycleArray，避免跨文件依赖
    struct CycleArray {
        E*  data;
        int start_, end_, count_, cap_;

        explicit CycleArray(int c = 1) : start_(0), end_(0), count_(0), cap_(max(1, c)) {
            data = new E[cap_];
        }
        ~CycleArray() { delete[] data; }

        CycleArray(const CycleArray&) = delete;
        CycleArray& operator=(const CycleArray&) = delete;

        void resize(int newCap) {
            E* tmp = new E[newCap];
            for (int i = 0; i < count_; ++i) tmp[i] = data[(start_ + i) % cap_];
            delete[] data;
            data   = tmp;
            cap_   = newCap;
            start_ = 0;
            end_   = count_;
        }
        bool isFull()  const { return count_ == cap_; }
        bool isEmpty() const { return count_ == 0; }
        int  size()    const { return count_; }

        void addFirst(const E& v) {
            if (isFull()) resize(cap_ * 2);
            start_ = (start_ - 1 + cap_) % cap_;
            data[start_] = v;
            count_++;
        }
        void addLast(const E& v) {
            if (isFull()) resize(cap_ * 2);
            data[end_] = v;
            end_ = (end_ + 1) % cap_;
            count_++;
        }
        E removeFirst() {
            if (isEmpty()) throw runtime_error("empty");
            E v = data[start_];
            data[start_] = E();
            start_ = (start_ + 1) % cap_;
            count_--;
            if (count_ > 0 && count_ == cap_ / 4) resize(cap_ / 2);
            return v;
        }
        E removeLast() {
            if (isEmpty()) throw runtime_error("empty");
            end_ = (end_ - 1 + cap_) % cap_;
            E v = data[end_];
            data[end_] = E();
            count_--;
            if (count_ > 0 && count_ == cap_ / 4) resize(cap_ / 2);
            return v;
        }
        E getFirst() const { return data[start_]; }
        E getLast()  const { return data[(end_ - 1 + cap_) % cap_]; }
    };

    CycleArray arr_;
public:
    explicit MyArrayDeque(int initCap = 1) : arr_(initCap) {}

    void addFirst (const E& e) { arr_.addFirst(e); }
    void addLast  (const E& e) { arr_.addLast(e); }
    E    removeFirst()         { return arr_.removeFirst(); }
    E    removeLast()          { return arr_.removeLast(); }
    E    peekFirst()    const  { return arr_.getFirst(); }
    E    peekLast()     const  { return arr_.getLast(); }
    int  size()        const   { return arr_.size(); }
    bool isEmpty()     const   { return arr_.size() == 0; }
};

} // namespace dsa

int main() {
    dsa::MyArrayDeque<int> dq(4);
    dq.addLast(1);
    dq.addLast(2);
    dq.addFirst(0);
    dq.addLast(3);
    cout << dq.peekFirst() << "\n";  // 0
    cout << dq.peekLast()  << "\n";  // 3
    dq.removeFirst();
    dq.removeLast();
    cout << dq.peekFirst() << "\n";  // 1
    cout << dq.peekLast()  << "\n";  // 2
    return 0;
}
```

### 4. 复杂度对比

| 操作 | 链表 Deque | 数组 Deque（环形） |
| --- | --- | --- |
| `addFirst` | O(1) | 摊销 O(1) |
| `addLast` | O(1) | 摊销 O(1) |
| `removeFirst` | O(1) | 摊销 O(1) |
| `removeLast` | O(1) | 摊销 O(1) |
| `peekFirst` | O(1) | O(1) |
| `peekLast` | O(1) | O(1) |
| 额外空间 | 2 ptr/节点 | 紧凑（可能 25% 浪费） |
| Cache 友好 | ❌ | ✅ |

> [!tip] 选哪个？
> - **绝大多数场景用数组版**：连续内存、cache 友好、常数小。
> - **节点很大、指针密度低、生命周期不可预测**时用链表版：避免重新分配、内存压力更平稳。

### 5. Deque 是栈/队列的超集

普通栈的 API `push / pop / top` 可以用 Deque 模拟：

```cpp
template <typename E>
class StackOnDeque {
    dsa::MyArrayDeque<E> dq_;
public:
    void push(const E& e) { dq_.addLast(e); }   // 任意一端都行
    E    pop()            { return dq_.removeLast(); }
    E    top()      const { return dq_.peekLast(); }
    bool empty()    const { return dq_.isEmpty(); }
};
```

普通队列的 API `offer / poll / peek` 也可以用 Deque 模拟：

```cpp
template <typename E>
class QueueOnDeque {
    dsa::MyArrayDeque<E> dq_;
public:
    void offer(const E& e) { dq_.addLast(e); }
    E    poll()            { return dq_.removeFirst(); }
    E    peek()      const { return dq_.peekFirst(); }
    bool empty()    const { return dq_.isEmpty(); }
};
```

> 用「单端操作」模拟「单端容器」是 Deque 的核心价值之一。

### 6. 标准库中的 Deque

| 语言 | 标准库 Deque | 底层 |
| --- | --- | --- |
| C++ | `std::deque<T>` | **分块数组**（多段固定大小数组 + 中控索引数组），比本章的环形数组更复杂，但原理相似 |
| Java | `java.util.ArrayDeque<E>` | 循环数组 |
| Java | `java.util.LinkedList<E>` | 双链表 |
| Python | `collections.deque` | 分块双向链表 |
| Go | `container/list`（最接近） | 双链表 |

> **C++ `std::deque` 特殊**：它的 `operator[]` 是 O(1) 但**不是连续内存**，所以 `&dq[0]` 和 `&dq[1]` 不一定相邻。不能把 `std::deque` 的迭代器当指针用。

### 7. 应用场景

- **滑动窗口最大值**（LeetCode 239）：维护「单调递减 Deque」，O(n) 求每个窗口的最大值。
- **LRU 缓存**（LeetCode 146）：HashMap + 双链表/Deque 维护访问顺序。
- **BFS 队列**：用 Deque 的「头删 + 尾插」可以同时实现 BFS 的 FIFO；用「头尾都能增删」可以扩展为 0-1 BFS。
- **回文检查**：把字符串前半入队，依次头删 + 头插与后半比较。
- **工作窃取调度器（Work-Stealing Scheduler）**：线程池中空闲线程从其他线程的 **Deque 头部**偷任务——这就是 Deque「头尾都能 O(1) 增删」最典型的应用。

> [!tip] 0-1 BFS
> 边权为 0 或 1 的图最短路：权 0 的边用 `addFirst`、权 1 的边用 `addLast`，就能保证 BFS 出队顺序就是最短路顺序。这是 Deque 相对普通 Queue 的「独门优势」。

## 📊 复杂度一览

| 维度 | 链表 Deque | 数组 Deque（环形） | 普通 Queue（单链表） |
| --- | --- | --- | --- |
| 头增 / 删 | O(1) | 摊销 O(1) | ❌ 不支持 |
| 尾增 / 删 | O(1) | 摊销 O(1) | 尾增 O(1) / 头删 O(1) |
| 看头 / 看尾 | O(1) | O(1) | O(1) |
| 额外空间 | 2 ptr/节点 | 紧凑 | 2 ptr/节点 |
| Cache 友好 | ❌ | ✅ | ❌ |
| 适用 | 大对象 / 不可预测 | 默认选它 | 纯 FIFO |

## 🛠️ 应用场景汇总

- **算法题**：「单调队列」「滑动窗口」「BFS 变体」几乎都用 Deque。
- **LRU 缓存**：`HashMap` 定位 + `Deque` 维护访问顺序 = O(1) get/put。
- **工作窃取**：线程池调度器的经典实现。
- **栈 / 队列的替代**：用 Deque 模拟任意单端容器。

## ▶️ 下一章

[[08-queue-stack-basic|队列/栈的基本原理]] — Deque 是双端操作，Queue/Stack 限制为单端；下一章看队列和栈的本质、复杂度，以及如何用数组/链表实现它们。

## 🔗 相关章节

- [[03-array-implement|动态数组实现]] — Deque 数组版的前置
- [[04-cycle-array|环形数组]] — Deque 数组版的核心技巧
- [[05-linkedlist-basic|链表原理]] — Deque 链表版的前置
- [[06-linkedlist-implement|链表实现]] — Deque 链表版直接复用
- [[08-queue-stack-basic|队列/栈]] — 下一章，Deque 的「子集」
- [[10-linked-queue-stack|链表实现队列/栈]] — Deque 的单端应用
