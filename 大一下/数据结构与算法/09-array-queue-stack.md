---
title: 数组实现队列/栈
tags:
  - 数据结构
  - 队列
  - 栈
  - 动态数组
  - 环形数组
order: 9
prerequisites:
  - "[[08-queue-stack-basic]]"
  - "[[03-array-implement]]"
  - "[[04-cycle-array]]"
group: 队列/栈
subgroup: 实现
paywall: false
source: https://labuladong.online/zh/algo/data-structure-basic/array-queue-stack/
---

# 数组实现队列/栈

## 学习目标

读完本章后，你应该能够：

- 用 `std::vector` 写出一个**O(1) push/pop/peek** 的栈。
- 解释「为什么普通动态数组头插头删是 O(n)，而队列偏偏要在头部删除」。
- 用 [[04-cycle-array|环形数组]] 技巧实现一个 O(1) push/pop 的数组队列。
- 清楚说出「栈用 vector、队列用 deque / 环形数组」这个 C++ 经验法则背后的原因。

## 一句话总结

> **栈 = `vector` 末尾当栈顶**（最简单）。**队列 = `vector` 头尾都用**（必须借助环形数组技巧，否则 push 或 pop 退化到 O(n)）。

## 前置知识

阅读本章前，建议先掌握：

- [[08-queue-stack-basic|队列/栈的基本原理]]
- [[03-array-implement|动态数组的代码实现]]
- [[04-cycle-array|循环数组技巧及实现]]

如果对 `size_t`、`emplace_back` 不熟，请先看 [[03-array-implement]]。

## 一、为什么用数组实现？

队列/栈的 push/pop/peek 都要求 O(1)，所以底层必须能 O(1) 完成**「在一端增、在一端删」**。两种天然候选：

- **动态数组（vector）**：末尾增删 O(1)，**头部**增删 O(n)（要搬动所有元素）。
- **环形数组（cycle array）**：头尾增删都是 O(1)，且连续内存，对 CPU 缓存友好。

下面分栈、队列两种情况来写。

## 二、数组实现栈（最简单）

### 2.1 思路

把动态数组的**末尾**当作**栈顶**：

- `push(e)` → `arr.push_back(e)`
- `pop()` → `arr.pop_back()` 并返回被弹出的值
- `peek()` → `arr.back()`

由于 `push_back` 和 `pop_back` 都是 O(1) 摊还（amortized），栈的所有 API 自然也是 O(1) 摊还。

### 2.2 完整 C++ 实现

```cpp
#include <bits/stdc++.h>
using namespace std;

namespace dsa {

// 用动态数组作为底层数据结构实现栈
template <typename E>
class MyArrayStack {
public:
    // 向栈顶加入元素（摊还 O(1)）
    void push(const E& e) {
        data_.push_back(e);
    }

    // 向栈顶加入元素（move 版本，避免拷贝）
    void push(E&& e) {
        data_.push_back(std::move(e));
    }

    // 从栈顶弹出元素（O(1) 摊还）
    E pop() {
        // 生产代码里要先检查 empty()
        E e = std::move(data_.back());
        data_.pop_back();
        return e;
    }

    // 查看栈顶元素（O(1)）
    E& peek() {
        return data_.back();
    }

    const E& peek() const {
        return data_.back();
    }

    // 返回栈中的元素个数（O(1)）
    std::size_t size() const noexcept {
        return data_.size();
    }

    bool empty() const noexcept {
        return data_.empty();
    }

private:
    std::vector<E> data_;
};

} // namespace dsa

int main() {
    using namespace dsa;
    MyArrayStack<int> st;
    st.push(1);
    st.push(2);
    st.push(3);

    cout << st.peek() << "\n"; // 3
    cout << st.pop()  << "\n"; // 3
    cout << st.peek() << "\n"; // 2
    cout << st.size() << "\n"; // 2
}
```

> [!tip] 为什么是「摊还 O(1)」？
> `vector::push_back` 单次是 O(1)，但**偶尔**要扩容到 2 倍容量、搬运所有元素，所以单次最坏是 O(n)。把 n 次 push 的总成本平摊下来，每次就是 O(1) 摊还。同理 `pop_back` 不缩容时是 O(1)，缩容时（一些实现会）也是摊还 O(1)。

### 2.3 可不可以把「数组头」当栈顶？

**普通动态数组不行**：头插 / 头删都是 O(n)，违反栈的 O(1) 约束。

**用 [[04-cycle-array|环形数组]]（CycleArray）就可以**：`addFirst` + `removeFirst` 都是 O(1)。如果你想写一个用数组头当栈顶的版本，把 `push_back/pop_back/back()` 全部换成 `addFirst/removeFirst/getFirst()` 即可，逻辑完全对称。

## 三、数组实现队列（需要环形数组）

### 3.1 为什么队列比栈难？

队列要满足：

- `push(x)`：从**队尾**插入
- `pop()`：从**队头**删除
- `peek()`：看**队头**

如果直接用 `std::vector`：

- `push_back`：O(1) ✓
- `pop_front`：O(n) ✗（所有元素都要往前搬）
- `front`：O(1) ✓

所以「pop_front 是 O(n)」这一点破坏了队列的 O(1) 承诺。

**解法**：复用 [[04-cycle-array|环形数组]]。`CycleArray::addLast` + `removeFirst` + `getFirst` 都是 O(1)，天然满足队列需求。

### 3.2 一个最小可用的环形数组

为了让你能在不依赖外部库的情况下复现 `CycleArray`，下面给出一个简化版实现（满足本章需求，扩缩容策略写得不激进但够用）：

```cpp
#include <bits/stdc++.h>
using namespace std;

namespace dsa {

// 简化版环形数组：head 是第一个元素下标，size_ 是元素个数
template <typename E>
class CycleArray {
public:
    explicit CycleArray(std::size_t cap = 8)
        : data_(cap), cap_(cap), head_(0), size_(0) {}

    std::size_t size() const noexcept { return size_; }
    bool empty() const noexcept { return size_ == 0; }
    std::size_t cap()  const noexcept { return cap_; }

    E& getFirst() {
        return data_[head_];
    }
    const E& getFirst() const {
        return data_[head_];
    }
    E& getLast() {
        // 队尾在 (head_ + size_ - 1) % cap_
        return data_[(head_ + size_ - 1) % cap_];
    }

    void addLast(const E& e) {
        ensureNotFull();
        std::size_t tail = (head_ + size_) % cap_;
        data_[tail] = e;
        ++size_;
    }
    void addLast(E&& e) {
        ensureNotFull();
        std::size_t tail = (head_ + size_) % cap_;
        data_[tail] = std::move(e);
        ++size_;
    }
    void addFirst(const E& e) {
        ensureNotFull();
        head_ = (head_ + cap_ - 1) % cap_; // 往前走一格
        data_[head_] = e;
        ++size_;
    }

    E removeFirst() {
        E e = std::move(data_[head_]);
        head_ = (head_ + 1) % cap_;
        --size_;
        return e;
    }

private:
    void ensureNotFull() {
        if (size_ == cap_) resize(cap_ * 2);
    }
    void resize(std::size_t newCap) {
        std::vector<E> nxt(newCap);
        for (std::size_t i = 0; i < size_; ++i) {
            nxt[i] = std::move(data_[(head_ + i) % cap_]);
        }
        data_ = std::move(nxt);
        head_ = 0;
        cap_ = newCap;
    }

    std::vector<E> data_;
    std::size_t    cap_;
    std::size_t    head_;
    std::size_t    size_;
};

} // namespace dsa
```

### 3.3 基于环形数组的队列

直接复用 `CycleArray`：

```cpp
#include <bits/stdc++.h>
using namespace std;

namespace dsa {

// 用环形数组作为底层数据结构实现队列
template <typename E>
class MyArrayQueue {
public:
    // 向队尾插入元素（摊还 O(1)）
    void push(const E& e) {
        arr_.addLast(e);
    }
    void push(E&& e) {
        arr_.addLast(std::move(e));
    }

    // 从队头删除元素（O(1) 摊还）
    E pop() {
        return arr_.removeFirst();
    }

    // 查看队头元素（O(1)）
    E& peek() {
        return arr_.getFirst();
    }
    const E& peek() const {
        return arr_.getFirst();
    }

    std::size_t size() const noexcept { return arr_.size(); }
    bool empty() const noexcept { return arr_.empty(); }

private:
    CycleArray<E> arr_;
};

} // namespace dsa

int main() {
    using namespace dsa;
    MyArrayQueue<int> q;
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

### 3.4 复杂度小结

| 操作 | 复杂度 | 说明 |
| --- | --- | --- |
| `push` | 摊还 O(1) | 偶尔扩容到 2 倍 |
| `pop` | 摊还 O(1) | head 指针移动 + size-- |
| `peek` | O(1) | 直接读 head 位置 |
| `size` / `empty` | O(1) | 读 size 字段 |
| **空间** | O(n) | 数组容量 ≥ 元素数 |

> 与 [[10-linked-queue-stack|链表实现队列]] 对比：数组版本**连续内存、缓存友好**，但扩容时有一次 O(n) 拷贝；链表版本**无扩容抖动**，但每个元素多一个（或两个）指针的内存开销。

## 四、用 `std::deque` 做队列

`std::vector` 头删是 O(n)，但 `std::deque`（双端队列）头尾操作都是 O(1)。它内部的实现是「分段连续」的，既支持头插头删又不会有 vector 那种扩容抖动。所以：

> **C++ 经验法则**：
>
> - 栈：`std::stack<int>`（默认底层是 `std::deque`），如果不需要随机访问，直接用就好。
> - 队列：`std::queue<int>`（默认底层也是 `std::deque`），头尾 O(1)。
> - 想自己控制底层，传模板参数：`std::stack<int, std::vector<int>>`。

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    // 队列的两种常见底层
    queue<int, deque<int>>     q1; // 默认
    queue<int, list<int>>      q2; // 链表底层
    // queue<int, vector<int>> q3; // 不行，vector 没有 pop_front
}
```

## 五、为什么 C++ 标准库没有 `std::vector_queue`？

因为 `std::vector` 的 `pop_front` 是 O(n)，不符合队列的 O(1) 要求。标准库宁愿让你用 `std::deque`（双端队列，名字里就带 `deque`）或自己实现环形数组，也不引入一个违反性能承诺的 `vector_queue`。

## 六、易混淆点与踩坑提示

1. **不要用 `vector::erase(begin())` 当 `pop_front`**，单次 O(n)。
2. **空队列访问 `front()`/`back()`** 在 `std::queue` 里是**未定义行为**，生产代码一定要 `if (!q.empty())`。
3. **`std::queue` 没有 `clear()`**，要清空：`while (!q.empty()) q.pop();`。
4. **环形数组扩容要重排**：别忘了把 `head_` 重置为 0 再按顺序搬到新数组。
5. **`size_t` 是无符号**，做差会出怪事，谨慎比较。

## 七、应用场景

- **数组版栈**：函数调用栈的「软件模拟」、表达式求值、深度优先搜索非递归写法。
- **数组版队列**：BFS 遍历、任务调度、消息缓冲、生产者-消费者、滑动窗口最值（单调队列）。
- **环形数组适用场景**：生产者-消费者环形缓冲（Ring Buffer）、日志系统、网络包的收/发缓冲。

## 下一章

数组实现看起来简单，但扩容和头删的细节容易写错。**链表实现**则把这些麻烦都消灭了——代价是每个元素多带一个 next 指针。下一篇 [[10-linked-queue-stack|链表实现队列/栈]] 给出链表版本，并对比两种实现的取舍。

## 相关章节

- 前置：[[08-queue-stack-basic|队列/栈的基本原理]]、[[03-array-implement|动态数组的代码实现]]、[[04-cycle-array|循环数组技巧及实现]]
- 同主题：[[07-deque-implement|双端队列（Deque）原理和实现]]、[[10-linked-queue-stack|链表实现队列/栈]]
- 应用：[[24-binary-tree-traverse-basic|二叉树的层序遍历]]、[[34-graph-traverse-basic|图的 BFS 遍历]]
- 对比：[[03-array-implement|动态数组]] vs [[06-linkedlist-implement|链表实现]]
