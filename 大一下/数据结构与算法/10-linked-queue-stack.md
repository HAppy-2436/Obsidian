---
title: 链表实现队列/栈
tags:
  - 数据结构
  - 队列
  - 栈
  - 双向链表
  - 单链表
order: 10
prerequisites:
  - "[[08-queue-stack-basic]]"
  - "[[06-linkedlist-implement]]"
group: 队列/栈
subgroup: 实现
paywall: false
source: https://labuladong.online/zh/algo/data-structure-basic/linked-queue-stack/
---

# 链表实现队列/栈

## 学习目标

读完本章后，你应该能够：

- 用一个双向链表（`std::list`）实现 O(1) push/pop/peek 的栈和队列。
- 理解「为什么双向链表的尾部当队尾、头部当队头」是最高效的选择。
- 知道「单链表 + 尾指针」也能实现队列（push O(1)、pop O(1)、peek O(1)）。
- 对比 [[09-array-queue-stack|数组实现]] 和链表实现在内存、性能、扩容上的取舍。

## 一句话总结

> **双向链表的头尾操作都是 O(1)，天然适合做队列和栈**——把双向链表当成一个头尾都可以 O(1) 增删的「双向开口容器」，栈和队列只是它的一种 API 投影。

## 前置知识

阅读本章前，建议先掌握：

- [[08-queue-stack-basic|队列/栈的基本原理]]
- [[05-linkedlist-basic|链表（链式存储）的原理]]
- [[06-linkedlist-implement|链表的代码实现]]

## 一、为什么链表实现更「自然」？

回顾 [[09-array-queue-stack|数组实现]]：栈很简单（用 `vector` 末尾），但**队列要借助环形数组**才能让 pop_front 保持 O(1)。

链表没有这个烦恼：**双向链表头尾插入/删除都是 O(1)，且不需要连续内存**。这意味着：

- 栈：用双向链表就行，无所谓头还是尾当栈顶——选哪个都是 O(1)。
- 队列：用双向链表，头当队头、尾当队尾，**两端各管各的 O(1) 操作**。

代价是每个节点多一个（或两个）指针的内存开销，以及「不连续内存」对 CPU 缓存不友好。

## 二、用 `std::list` 实现栈

### 2.1 思路

把双向链表的**任意一端**当栈顶（这里选尾部）。所有操作都直接调用 `std::list` 的 `push_back/pop_back/back`：

- `push(e)` → `list_.push_back(e)`
- `pop()` → `list_.back()` 取出后 `list_.pop_back()`
- `peek()` → `list_.back()`

### 2.2 完整 C++ 实现

```cpp
#include <bits/stdc++.h>
using namespace std;

namespace dsa {

// 用双向链表作为底层数据结构实现栈
template <typename E>
class MyLinkedStack {
public:
    // 向栈顶加入元素（O(1)）
    void push(const E& e) {
        list_.push_back(e);
    }
    void push(E&& e) {
        list_.push_back(std::move(e));
    }

    // 从栈顶弹出元素（O(1)）
    E pop() {
        E e = std::move(list_.back());
        list_.pop_back();
        return e;
    }

    // 查看栈顶元素（O(1)）
    E& peek() {
        return list_.back();
    }
    const E& peek() const {
        return list_.back();
    }

    std::size_t size() const noexcept {
        return list_.size();
    }

    bool empty() const noexcept {
        return list_.empty();
    }

private:
    std::list<E> list_;
};

} // namespace dsa

int main() {
    using namespace dsa;
    MyLinkedStack<int> st;
    st.push(1);
    st.push(2);
    st.push(3);

    cout << st.peek() << "\n"; // 3
    cout << st.pop()  << "\n"; // 3
    cout << st.peek() << "\n"; // 2
    cout << st.size() << "\n"; // 2
}
```

> [!tip] 选头还是选尾当栈顶？
> 都可以——双向链表头尾都是 O(1)。如果想用头部当栈顶，把 `push_back` → `push_front`，`pop_back` → `pop_front`，`back()` → `front()` 即可。性能上没差别，纯粹看个人习惯。

## 三、用 `std::list` 实现队列

### 3.1 思路

- **队头** = 双向链表**头部**（方便 `pop_front`）
- **队尾** = 双向链表**尾部**（方便 `push_back`）

```cpp
#include <bits/stdc++.h>
using namespace std;

namespace dsa {

// 用双向链表作为底层数据结构实现队列
template <typename E>
class MyLinkedQueue {
public:
    // 向队尾插入元素（O(1)）
    void push(const E& e) {
        list_.push_back(e);
    }
    void push(E&& e) {
        list_.push_back(std::move(e));
    }

    // 从队头删除元素（O(1)）
    E pop() {
        E e = std::move(list_.front());
        list_.pop_front();
        return e;
    }

    // 查看队头元素（O(1)）
    E& peek() {
        return list_.front();
    }
    const E& peek() const {
        return list_.front();
    }

    std::size_t size() const noexcept {
        return list_.size();
    }

    bool empty() const noexcept {
        return list_.empty();
    }

private:
    std::list<E> list_;
};

} // namespace dsa

int main() {
    using namespace dsa;
    MyLinkedQueue<int> q;
    q.push(1);
    q.push(2);
    q.push(3);

    cout << q.peek() << "\n"; // 1
    cout << q.pop()  << "\n"; // 1
    cout << q.pop()  << "\n"; // 2
    cout << q.peek() << "\n"; // 3
    cout << q.size() << "\n"; // 1
}
```

### 3.2 反向也行

把**头部当队尾、尾部当队头**完全 OK，只要把 `push_back` → `push_front`、`pop_front` → `pop_back`、`front()` → `back()` 即可。两条路性能等价。

## 四、自己用裸双向链表实现（不依赖 `std::list`）

如果你想更贴近底层、不用 `std::list`，下面给一个最小可用的双向链表节点 + 队列实现。

```cpp
#include <bits/stdc++.h>
using namespace std;

namespace dsa {

template <typename E>
struct DNode {
    E       val;
    DNode*  prev = nullptr;
    DNode*  next = nullptr;
    explicit DNode(const E& v) : val(v) {}
    explicit DNode(E&& v) : val(std::move(v)) {}
};

template <typename E>
class MyLinkedQueueRaw {
public:
    MyLinkedQueueRaw() = default;
    ~MyLinkedQueueRaw() { clear(); }

    MyLinkedQueueRaw(const MyLinkedQueueRaw&)            = delete;
    MyLinkedQueueRaw& operator=(const MyLinkedQueueRaw&) = delete;

    void push(const E& e) {
        DNode<E>* n = new DNode<E>(e);
        if (!head_) {
            head_ = tail_ = n;
        } else {
            tail_->next = n;
            n->prev     = tail_;
            tail_       = n;
        }
        ++size_;
    }

    E pop() {
        DNode<E>* n = head_;
        E e = std::move(n->val);
        head_ = head_->next;
        if (head_) head_->prev = nullptr;
        else       tail_       = nullptr;
        delete n;
        --size_;
        return e;
    }

    E& peek()             { return head_->val; }
    const E& peek() const { return head_->val; }

    std::size_t size()  const noexcept { return size_; }
    bool        empty() const noexcept { return size_ == 0; }

private:
    void clear() {
        while (head_) {
            DNode<E>* n = head_->next;
            delete head_;
            head_ = n;
        }
        tail_ = nullptr;
        size_ = 0;
    }

    DNode<E>*    head_ = nullptr;
    DNode<E>*    tail_ = nullptr;
    std::size_t  size_ = 0;
};

} // namespace dsa
```

栈的版本只要把 push 接到 `tail_`、pop 从 `head_`/`tail_` 拿，看你选哪边当栈顶。

## 五、用「单链表 + 尾指针」实现队列

单链表没有 prev 指针，**头删 O(1)、尾插 O(n)**。但如果维护一个 `tail_` 指针，**尾插就是 O(1)**。于是：

- 队列头 → 单链表 head → O(1) pop
- 队列尾 → `tail_` → O(1) push
- 队列 peek → head → O(1)

这其实就是 [[06-linkedlist-implement|单链表实现]] 加一个尾指针，没什么黑魔法。

```cpp
#include <bits/stdc++.h>
using namespace std;

namespace dsa {

template <typename E>
class MySinglyLinkedQueue {
public:
    struct Node { E val; Node* next = nullptr; };

    MySinglyLinkedQueue() = default;
    ~MySinglyLinkedQueue() { clear(); }

    void push(const E& e) {
        Node* n = new Node{e, nullptr};
        if (!tail_) {
            head_ = tail_ = n;
        } else {
            tail_->next = n;
            tail_       = n;
        }
        ++size_;
    }

    E pop() {
        Node* n = head_;
        E e = std::move(n->val);
        head_ = head_->next;
        if (!head_) tail_ = nullptr;
        delete n;
        --size_;
        return e;
    }

    E& peek()             { return head_->val; }
    const E& peek() const { return head_->val; }

    std::size_t size()  const noexcept { return size_; }
    bool        empty() const noexcept { return size_ == 0; }

private:
    void clear() {
        while (head_) {
            Node* n = head_->next;
            delete head_;
            head_ = n;
        }
        tail_ = nullptr;
        size_ = 0;
    }

    Node*       head_ = nullptr;
    Node*       tail_ = nullptr;
    std::size_t size_ = 0;
};

} // namespace dsa
```

> [!warning] 单链表不能用尾插栈
> 单链表「头插 O(1)、尾删 O(n)」（没有 prev 指针）。所以栈通常用双向链表或数组实现，单链表只能做到「头当栈顶」（push_front + pop_front），不要用「尾当栈顶」。

## 六、复杂度小结

| 实现 | push | pop | peek | 空间 | 备注 |
| --- | --- | --- | --- | --- | --- |
| `list` 栈（头或尾） | O(1) | O(1) | O(1) | O(n) + 每节点 2 指针 | 最简单 |
| `list` 队列 | O(1) | O(1) | O(1) | O(n) + 每节点 2 指针 | 推荐用 `std::queue` |
| 裸双向链表队列 | O(1) | O(1) | O(1) | O(n) + 2 指针 + 内存碎片 | 面试手写常用 |
| 单链表 + 尾指针队列 | O(1) | O(1) | O(1) | O(n) + 1 指针 | 节省指针但代码更绕 |

## 七、链表版 vs 数组版：选哪个？

| 维度 | 数组版（vector / 环形数组） | 链表版（list） |
| --- | --- | --- |
| 内存 | 连续，缓存友好 | 离散，缓存不友好 |
| 单次操作 | 通常更快（cache 命中率高） | 通常稍慢（指针跳跃） |
| 扩容 | 偶尔 O(n) 拷贝 | 永不扩容，每个新元素 O(1) |
| 内存开销 | 无额外指针 | 每节点 1~2 个指针（8~16B/节点） |
| 队列 push 复杂度 | 栈尾环形数组 → 摊还 O(1) | 直接 O(1) |
| 适用场景 | 大数据量、连续访问、性能敏感 | 元素数量剧烈波动、内存敏感场景 |

> 经验法则：默认用 `std::stack` / `std::queue`（底层 `deque`），**当你确定知道数据量大且需要连续内存时**才考虑自己用 `std::vector` 或 `std::array` 改造。

## 八、易混淆点与踩坑提示

1. **`std::list::size()` 可能是 O(n)**——老标准（`< C++11`）要求线性扫描，新标准是 O(1)。如果对性能敏感，自己维护 `size_` 计数。
2. **裸链表的内存泄漏**：析构函数里一定要把节点一个一个 `delete`，不要只断指针。
3. **空队列访问 `front()`/`back()`** 是 UB（未定义行为），记得 `empty()` 检查。
4. **`std::list` 的 `splice` 和 `merge`** 是它的强项（O(1) 合并两个有序链表），但和队列/栈 API 无关。
5. **递归 / 栈溢出**：用链表实现栈时，理论上能 push 任意多元素直到 OOM，但实际写递归时调用栈是操作系统栈（一般 1~8 MB），照样会段错误。

## 九、应用场景

- **链表版栈**：表达式求值（栈深可能很大时）、DFS 非递归（特别是图很大的情况）、浏览器历史记录。
- **链表版队列**：生产者-消费者（用 `std::queue` 即可）、任务调度（任务数波动剧烈）、LRU 缓存（用 `list` + 哈希表实现 O(1) 访问 + O(1) 移动节点）。
- **裸双向链表手写**：面试常考「不让你用标准库，徒手实现队列/栈」。

## 下一章

队列/栈的核心内容到这里就结束了。**下一组章节是哈希表**——一种「用空间换时间」、平均 O(1) 增删查改的强力结构。先看 [[11-hashtable-with-array|数组实现哈希表（ArrayHashMap）]]，理解「键到数组下标」的映射原理。

## 相关章节

- 前置：[[08-queue-stack-basic|队列/栈的基本原理]]、[[05-linkedlist-basic|链表（链式存储）的原理]]、[[06-linkedlist-implement|链表的代码实现]]
- 同主题：[[09-array-queue-stack|数组实现队列/栈]]、[[07-deque-implement|双端队列（Deque）原理和实现]]
- 应用：[[24-binary-tree-traverse-basic|二叉树的层序遍历（用队列）]]、[[34-graph-traverse-basic|图的 DFS/BFS 遍历]]
- 下一组：[[11-hashtable-with-array|数组实现哈希表]]、[[13-hashmap-basic|哈希表核心原理]]
