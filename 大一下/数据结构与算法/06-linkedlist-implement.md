---
title: 链表的代码实现
tags: [数据结构, 链表, 实现]
order: 6
prerequisites: [05-linkedlist-basic]
group: 链表
paywall: false
source: labuladong
---

# 链表的代码实现

> [!info] 章节定位
> 上一章讲了链表原理，本章落到代码：用 C++ 实现一个**支持完整增删查改的 `MyLinkedList<E>`**（双链表版 + 单链表版）。重点掌握「**虚拟头尾节点**」「**持头尾指针**」「**删除时清空指针**」三个工程技巧。

## 📚 学习目标

- 用 C++ 模板实现 `MyLinkedList<E>`，支持 8 个核心 API
- 理解「**虚拟头尾节点**」如何消除头尾操作的边界特例
- 知道为什么链表容器要**同时持有头指针 + 尾指针**
- 学会**单链表 + 虚拟头结点**的简化版实现
- 能用本实现去解 LeetCode 707「设计链表」（注意：方法名要改）

## 🎯 一句话总结

> 链表实现的关键是「**双链表 + 虚拟头尾节点 + 同时持头尾指针**」三件套；这能消除「头节点是 null」「尾节点 next 是 null」「单链表删尾要遍历」等所有边界特例，让增删查改的代码**全部对称**。

## 🔗 前置知识

- [[00-intro|本章导读]]
- [[01-complexity|时间空间复杂度入门]]
- [[02-array-basic|数组原理]]
- [[05-linkedlist-basic|链表原理]] — **必读**
- C++ 模板、智能指针（或手写 `new/delete`）

## 📖 正文

### 1. 关键点一：同时持有头尾节点的引用

工程中的链表容器（Java `LinkedList`、C++ `std::list`）几乎都是**双链表 + 持头尾指针**，原因：

| 操作 | 只有头指针 | 头尾都有 |
| --- | --- | --- |
| 头部插入 / 删除 | O(1) | O(1) |
| 尾部插入 | O(n) 要遍历 | **O(1)** |
| 尾部删除 | O(n) 单链表；O(1) 双链表 | O(1) |
| 中间按索引 | O(n) | O(n)，可双向逼近省一半时间 |

> 现实里「**在容器尾部添加元素**」是超高频操作（`addLast` 是最常调用的方法），把这条路径优化到 O(1) 非常值得。

「持尾指针」听起来简单，但有个**陷阱**：

```cpp
tail = newNode;   // 假设 tail 当前指向链表最后一个节点
```

如果**删除了尾节点**，那个 `tail` 引用就指向了一个**无效节点**。常见解决：

- **双链表**：删尾后用 `tail = tail->prev` O(1) 找回。
- **单链表**：删尾后必须**遍历**找新尾。可以顺便在 `addLast` 维护 tail 之后，**在 `removeLast` 时遍历**。

### 2. 关键点二：虚拟头尾节点

#### 2.1 痛点：边界特例

如果不引入虚拟节点，链表的「头部插入」「头部删除」「空链表」要写一堆 `if (head == nullptr)` 的特例：

```cpp
void addFirst(E e) {
    Node* n = new Node(e);
    if (head == nullptr) {  // 特例：空链表
        head = n;
        tail = n;
    } else {                // 一般情况
        n->next = head;
        head = n;
    }
}
```

类似特例在「删除头部」「删除尾部」上还要各写一次。

#### 2.2 解决方案：永远存在 dummy head + dummy tail

**无论链表是否为空**，`dummyHead` 和 `dummyTail` 两个节点都存在。空链表长这样：

```text
dummyHead <-> dummyTail
```

非空链表长这样（假设有 1, 2, 3）：

```text
dummyHead <-> 1 <-> 2 <-> 3 <-> dummyTail
```

加上 dummy 后，**所有插入 / 删除都可以统一为「在两个已知节点之间插入 / 删除」**——不再有特例。

#### 2.3 dummy 不计入 size

> [!warning] 关键约定
> 虚拟节点是**内部实现细节**，对外**不可见**：
> - `size()` 只计真实节点，不计 dummy。
> - `get(i)` 的索引 `i` 从**第一个真实节点**算起（不是从 `dummyHead`）。
> - 任何遍历循环的终止条件应该是 `p != dummyTail`（而不是 `p != nullptr`）。

### 3. 关键点三：删除时清空指针

```cpp
Node* toDel = x;
x->prev->next = x->next;
x->next->prev = x->prev;
x->prev = nullptr;   // 把被删节点的指针置空
x->next = nullptr;
delete toDel;
```

- **C++ 必须**显式 `delete`（否则内存泄漏）。
- **置空指针**是**好习惯**：避免被误用、帮助调试（gdb 看到 `nullptr` 就知道「这节点被删了」）。
- 对 Java/Go 来说，「置空 prev/next」不是必须的（GC 不可达就回收），但**仍然推荐**——避免「野指针」风格的潜在 bug。

### 4. 双链表完整实现（C++）

```cpp
#include <bits/stdc++.h>
using namespace std;

namespace dsa {

template <typename E>
class MyLinkedList {
private:
    struct Node {
        E       val;
        Node*   prev;
        Node*   next;
        Node(E v) : val(v), prev(nullptr), next(nullptr) {}
    };

    Node* head_;   // dummy head
    Node* tail_;   // dummy tail
    int   size_;

    // 工具：插入到 pPrev 与 pNext 之间
    void addBetween(Node* pPrev, Node* pNext, const E& e) {
        Node* x = new Node(e);
        x->prev  = pPrev;
        x->next  = pNext;
        pPrev->next = x;
        pNext->prev = x;
        size_++;
    }

    // 工具：把 node 从链表中摘下
    E removeNode(Node* node) {
        Node* p = node->prev;
        Node* n = node->next;
        p->next = n;
        n->prev = p;
        E val = node->val;
        node->prev = nullptr;
        node->next = nullptr;
        delete node;
        size_--;
        return val;
    }

    Node* getNode(int i) const {
        checkElementIndex(i);
        // 双向逼近：索引小从头走，索引大从尾走
        if (i < size_ / 2) {
            Node* p = head_->next;
            for (int k = 0; k < i; ++k) p = p->next;
            return p;
        } else {
            Node* p = tail_->prev;
            for (int k = size_ - 1; k > i; --k) p = p->prev;
            return p;
        }
    }

    bool isElementIndex(int i) const { return i >= 0 && i < size_; }
    bool isPositionIndex(int i) const { return i >= 0 && i <= size_; }
    void checkElementIndex(int i) const {
        if (!isElementIndex(i)) throw out_of_range("Index: " + to_string(i));
    }
    void checkPositionIndex(int i) const {
        if (!isPositionIndex(i)) throw out_of_range("Index: " + to_string(i));
    }

public:
    MyLinkedList() : size_(0) {
        head_ = new Node(E{});
        tail_ = new Node(E{});
        head_->next = tail_;
        tail_->prev = head_;
    }
    ~MyLinkedList() {
        Node* p = head_;
        while (p) {
            Node* n = p->next;
            delete p;
            p = n;
        }
    }

    MyLinkedList(const MyLinkedList&) = delete;
    MyLinkedList& operator=(const MyLinkedList&) = delete;

    // ===== 增 =====
    void addFirst(const E& e) { addBetween(head_, head_->next, e); }
    void addLast (const E& e) { addBetween(tail_->prev, tail_, e); }
    void add(int i, const E& e) {
        checkPositionIndex(i);
        if (i == size_) { addLast(e); return; }
        Node* p = getNode(i);
        addBetween(p->prev, p, e);
    }

    // ===== 删 =====
    E removeFirst() {
        if (size_ < 1) throw runtime_error("removeFirst from empty");
        return removeNode(head_->next);
    }
    E removeLast() {
        if (size_ < 1) throw runtime_error("removeLast from empty");
        return removeNode(tail_->prev);
    }
    E remove(int i) {
        checkElementIndex(i);
        return removeNode(getNode(i));
    }

    // ===== 查 / 改 =====
    E getFirst() const {
        if (size_ < 1) throw runtime_error("getFirst from empty");
        return head_->next->val;
    }
    E getLast() const {
        if (size_ < 1) throw runtime_error("getLast from empty");
        return tail_->prev->val;
    }
    E get(int i) const { return getNode(i)->val; }
    E set(int i, const E& e) {
        Node* p = getNode(i);
        E old = p->val;
        p->val = e;
        return old;
    }

    // ===== 工具 =====
    int  size() const { return size_; }
    bool isEmpty() const { return size_ == 0; }

    void display() const {
        cout << "size=" << size_ << " [";
        for (Node* p = head_->next; p != tail_; p = p->next) {
            if (p != head_->next) cout << " <-> ";
            cout << p->val;
        }
        cout << "]\n";
    }
};

} // namespace dsa

int main() {
    dsa::MyLinkedList<int> list;
    list.addLast(1);
    list.addLast(2);
    list.addLast(3);
    list.addFirst(0);
    list.add(2, 100);
    list.display();   // size=5 [0 <-> 1 <-> 100 <-> 2 <-> 3]

    cout << "get(2)=" << list.get(2) << "\n";      // 100
    list.set(2, 200);
    cout << "get(2)=" << list.get(2) << "\n";      // 200
    cout << "removeFirst=" << list.removeFirst() << "\n";
    cout << "removeLast=" << list.removeLast() << "\n";
    list.display();
    return 0;
}
```

### 5. 单链表版实现（更接近力扣风格）

```cpp
#include <bits/stdc++.h>
using namespace std;

namespace dsa {

template <typename E>
class MySinglyLinkedList {
private:
    struct Node {
        E     val;
        Node* next;
        Node(E v) : val(v), next(nullptr) {}
    };

    Node* head_;    // 虚拟头结点
    Node* tail_;    // 真实尾节点引用
    int   size_;

public:
    MySinglyLinkedList() : head_(new Node(E{})), tail_(head_), size_(0) {}
    ~MySinglyLinkedList() {
        Node* p = head_;
        while (p) { Node* n = p->next; delete p; p = n; }
    }

    MySinglyLinkedList(const MySinglyLinkedList&) = delete;
    MySinglyLinkedList& operator=(const MySinglyLinkedList&) = delete;

    // ===== 增 =====
    void addFirst(const E& e) {
        Node* n = new Node(e);
        n->next = head_->next;
        head_->next = n;
        if (size_ == 0) tail_ = n;
        size_++;
    }
    void addLast(const E& e) {
        Node* n = new Node(e);
        tail_->next = n;
        tail_ = n;
        size_++;
    }
    void add(int i, const E& e) {
        if (i < 0 || i > size_) throw out_of_range("i");
        if (i == size_) { addLast(e); return; }
        // 找前驱
        Node* prev = head_;
        for (int k = 0; k < i; ++k) prev = prev->next;
        Node* n = new Node(e);
        n->next = prev->next;
        prev->next = n;
        size_++;
    }

    // ===== 删 =====
    E removeFirst() {
        if (size_ < 1) throw runtime_error("empty");
        Node* f = head_->next;
        head_->next = f->next;
        if (size_ == 1) tail_ = head_;
        E v = f->val;
        delete f;
        size_--;
        return v;
    }
    E removeLast() {
        if (size_ < 1) throw runtime_error("empty");
        // 单链表必须找前驱
        Node* prev = head_;
        while (prev->next != tail_) prev = prev->next;
        E v = tail_->val;
        delete tail_;
        tail_ = prev;
        tail_->next = nullptr;
        size_--;
        return v;
    }
    E remove(int i) {
        if (i < 0 || i >= size_) throw out_of_range("i");
        Node* prev = head_;
        for (int k = 0; k < i; ++k) prev = prev->next;
        Node* target = prev->next;
        prev->next = target->next;
        if (i == size_ - 1) tail_ = prev;  // 删的是尾，更新 tail
        E v = target->val;
        delete target;
        size_--;
        return v;
    }

    // ===== 查 / 改 =====
    E get(int i) const {
        if (i < 0 || i >= size_) throw out_of_range("i");
        Node* p = head_->next;
        for (int k = 0; k < i; ++k) p = p->next;
        return p->val;
    }
    E set(int i, const E& e) {
        if (i < 0 || i >= size_) throw out_of_range("i");
        Node* p = head_->next;
        for (int k = 0; k < i; ++k) p = p->next;
        E old = p->val;
        p->val = e;
        return old;
    }

    int  size()   const { return size_; }
    bool isEmpty() const { return size_ == 0; }
};

} // namespace dsa
```

### 6. 关键操作的复杂度

| 操作 | 双链表（持头尾） | 单链表（持头尾） | 数组（对比） |
| --- | --- | --- | --- |
| `addFirst` | O(1) | O(1) | O(n) |
| `addLast` | **O(1)** | **O(1)** | 摊销 O(1) |
| `add(i, e)` | O(min(i, n-i)) | O(i) | O(n) |
| `removeFirst` | O(1) | O(1) | O(n) |
| `removeLast` | **O(1)** | O(n) 找前驱 | 摊销 O(1) |
| `remove(i)` | O(min(i, n-i)) | O(i) | O(n) |
| `get(i)` | O(min(i, n-i)) | O(i) | **O(1)** |
| `set(i, e)` | O(min(i, n-i)) | O(i) | **O(1)** |
| 空间开销 | 2 ptr/节点 | 1 ptr/节点 | 0 |

> [!tip] 单链表 `removeLast` 为何慢
> 单链表**没有 prev**，要删尾必须遍历到 `prev->next == tail` 的位置。**这正是双链表存在的理由**——多 8 字节换 O(1) 尾删。

### 7. 用本实现验证 LeetCode 707

> [!tip] 练手
> LeetCode 707「设计链表」要求实现 `get(index)`、`addAtHead`、`addAtTail`、`addAtIndex`、`deleteAtIndex`、`getLength`。  
> 把我们的 `MyLinkedList<int>` 套一层：
> ```cpp
> class MyLinkedList {
>     dsa::MyLinkedList<int> impl;
> public:
>     int  get(int i) { return impl.get(i); }
>     void addAtHead(int v) { impl.addFirst(v); }
>     void addAtTail(int v) { impl.addLast(v); }
>     void addAtIndex(int i, int v) { impl.add(i, v); }
>     void deleteAtIndex(int i) { impl.remove(i); }
> };
> ```
> 提交即可 AC（前提是 `get` 返回值类型对齐）。

### 8. 一些工程细节

#### 8.1 内存安全

- **C++ 异常安全**：`new` 失败会抛 `bad_alloc`，我们的代码在 `new` 之前已经检查了索引，因此不会出现「半构造」状态。
- **C++ 析构**：一定要 `delete` 所有 `new` 出来的节点。
- **C++ 拷贝构造**：默认浅拷贝会让两个 `MyLinkedList` 共享同一片节点，析构时 double free。我们**显式 `= delete`** 禁用拷贝；如果业务需要，自己写深拷贝或 `std::shared_ptr` / `std::unique_ptr` 包装。

#### 8.2 `int*` vs `Node**` 的取舍

`getNode` 返回 `Node*` 是**内部接口**，调用方不应直接操作它。一旦调用方 `delete` 那个 `Node*`，整个链表就坏了。**生产代码应该返回 `iterator` 或隐藏 `Node` 类型**。

#### 8.3 迭代器

要支持 C++ `for (auto x : list)`，需要提供 `begin()` / `end()` / `iterator` 类。这一步留作练习（生产版 `std::list` 内部就是这种结构）。

## 📊 复杂度一览

| 维度 | 双链表 | 单链表 | 数组（对比） |
| --- | --- | --- | --- |
| 头/尾增 | O(1) | O(1) 头 / O(1) 尾（有 tail） | O(n) / 摊销 O(1) |
| 头/尾删 | O(1) | O(1) 头 / O(n) 尾 | O(n) / 摊销 O(1) |
| 中间增删 | O(min(i, n-i)) | O(i) | O(n) |
| 按索引读 | O(min(i, n-i)) | O(i) | **O(1)** |
| 空间 | 2 ptr/节点 | 1 ptr/节点 | 0 |
| 适用 | 通用容器 | 力扣 / 内存敏感 | 读多写少 |

## 🛠️ 应用场景

- **通用链表容器**：本实现已经具备 `std::list` 的核心 API。
- **LRU 缓存**：见「扩展阅读」中的 LRU 章节。
- **图的邻接表**：稀疏图必备，每个节点的邻居用链表存。
- **栈 / 队列的底层**：用链表实现栈是 O(1) push/pop，见 [[10-linked-queue-stack|链表实现队列/栈]]。
- **哈希冲突链**：见 [[12-hashtable-with-linked-list|链表实现哈希表]]、[[16-hashtable-chaining|拉链法]]。

## ▶️ 下一章

[[07-deque-implement|双端队列（Deque）原理和实现]] — 把「链表 + 头尾 API」封装成标准容器；本章实现的 `MyLinkedList` 直接复用作 Deque 的底层。

## 🔗 相关章节

- [[05-linkedlist-basic|链表原理]] — 上一章
- [[07-deque-implement|双端队列]] — 下一章，复用 `MyLinkedList`
- [[10-linked-queue-stack|链表实现队列/栈]] — 链表最常见应用
- [[12-hashtable-with-linked-list|链表实现哈希表]] — 链表的另一应用
- [[20-skip-list-basic|跳表]] — 链表 + 多级索引
- [[27-tree-map-basic|搜索树]] — 链表 + 二叉
