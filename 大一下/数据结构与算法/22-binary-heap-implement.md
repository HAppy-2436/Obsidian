---
title: 堆排序/优先级队列的代码实现
tags:
  - 二叉堆
  - 优先级队列
  - 堆排序
  - priority_queue
  - 数据结构
order: 22
prerequisites:
  - "[[21-binary-heap-basic]]"
group: 二叉堆
subgroup: null
paywall: true
source: https://labuladong.online/zh/algo/data-structure-basic/binary-heap-implement/
---

# 堆排序/优先级队列的代码实现

## 学习目标

- 能够从零手写一个 **支持 swim/sink 的二叉堆**，并在此基础上封装出 **优先级队列**
- 理解 `std::priority_queue` 的源码本质：它就是一个 **容器适配器 + make_heap/push_heap/pop_heap 算法**
- 掌握 **Top K 问题** 的两种主流解法（小顶堆 / 快速选择），并能选型
- 理解原地堆排序的「两步走」：建堆 + 排序

## 一句话总结

二叉堆的代码实现 = 一个 **动态数组（vector）+ 两个原语操作（swim/sink）**；基于它可以封装 **优先级队列**，C++ STL 的 `std::priority_queue` 本质就是一个 **容器适配器**；最经典的应用是 [[45-heap-sort|堆排序]] 和 **Top K 问题**。

## 前置知识

阅读本文前，你需要先学习：

- [[21-binary-heap-basic|二叉堆核心原理及可视化]]（理解 swim/sink 和大顶堆/小顶堆）

## 1. 回顾：二叉堆的核心操作

在 [[21-binary-heap-basic|二叉堆原理]] 中我们已经知道，二叉堆的全部 API 都可以由两个原语 `swim`（上浮）和 `sink`（下沉）实现：

```text
push(x):     data.push_back(x); swim(N-1)
pop():       swap(data[0], data[N-1]); pop_back(); sink(0)
top():       return data[0]
```

下面我们先实现一个 **简化版**（方便理解），再实现 **完整版**（加上模板、比较器等）。

### 1.1 为什么 swim 和 sink 是关键？

我们可以把二叉堆想象成一个 **「会自动修复」** 的数组：只要某个位置的元素不满足堆序（父 < 子或父 > 子），就用 swim（向上修复）或 sink（向下修复）让它回到正确位置。其他所有 API 都可以分解为 **「破坏堆序 + 修复堆序」** 这两步：

- `push(x)`：把 x 放到末尾 → **末尾的 x 可能比它的父节点大** → swim 修复。
- `pop()`：把 root 和末尾交换 → **新的 root 可能比它的子节点小** → sink 修复。

理解了这一点，你就能从「记忆两个算法」升级为「理解一个统一的修复框架」，从而能轻松应对任何变体问题。

## 2. 简化版优先级队列实现

> 以下是优先级队列的简化版与完整版 C++ 实现，配合 `std::priority_queue` 源码分析。

简化版只支持 `int` 类型、大顶堆、最简 API，便于抓住核心：


> [!info] 📌 付费章节补全内容（基于算法知识体系补充）

```cpp
#include <bits/stdc++.h>
using namespace std;

namespace dsa {

// 简化版大顶堆优先级队列
class SimplePriorityQueue {
public:
    void push(int x) {
        data.push_back(x);
        swim(size() - 1);
    }

    int pop() {
        int top = data[0];
        data[0] = data.back();
        data.pop_back();
        sink(0);
        return top;
    }

    int top() const { return data[0]; }
    bool empty() const { return data.empty(); }
    int size() const { return (int)data.size(); }

private:
    vector<int> data;

    void swim(int k) {
        // 父节点 = (k-1)/2
        while (k > 0 && data[k] > data[(k - 1) / 2]) {
            swap(data[k], data[(k - 1) / 2]);
            k = (k - 1) / 2;
        }
    }

    void sink(int k) {
        int n = size();
        while (2 * k + 1 < n) {                  // 存在左子节点
            int j = 2 * k + 1;                    // 左子节点
            if (j + 1 < n && data[j + 1] > data[j]) j++;  // 选更大的子节点
            if (data[k] >= data[j]) break;        // 已满足堆序
            swap(data[k], data[j]);
            k = j;
        }
    }
};

} // namespace dsa

int main() {
    using namespace dsa;
    SimplePriorityQueue pq;
    for (int x : {3, 1, 4, 1, 5, 9, 2, 6}) pq.push(x);
    cout << "弹出顺序（大顶堆）: ";
    while (!pq.empty()) cout << pq.pop() << " ";
    cout << endl;
    // 预期: 9 6 5 4 3 2 1 1
    return 0;
}
```

## 3. 完整版：模板 + 自定义比较器

工业级实现需要支持 **任意类型 + 自定义比较器**，与 STL `std::priority_queue` 对齐：

```cpp
#include <bits/stdc++.h>
using namespace std;

namespace dsa {

// 完整版优先级队列：模板 + 比较器
template <typename T, typename Compare = std::less<T>>
class PriorityQueue {
public:
    explicit PriorityQueue(Compare comp = Compare{})
        : comp_(std::move(comp)) {}

    void push(const T& x) {
        data_.push_back(x);
        swim(size_() - 1);
    }

    void pop() {
        swap(data_[0], data_.back());
        data_.pop_back();
        if (!data_.empty()) sink(0);
    }

    const T& top() const { return data_[0]; }
    bool empty() const { return data_.empty(); }
    int size() const { return size_(); }

    // O(N) 建堆：比逐个 push 的 O(N log N) 更快
    PriorityQueue(const vector<T>& v, Compare comp = Compare{})
        : data_(v), comp_(std::move(comp)) {
        for (int i = parent(size_() - 1); i >= 0; --i) sink(i);
    }

private:
    vector<T> data_;
    Compare comp_;

    int size_() const { return (int)data_.size(); }
    static int parent(int i) { return (i - 1) / 2; }
    static int left(int i)   { return 2 * i + 1; }
    static int right(int i)  { return 2 * i + 2; }

    void swim(int k) {
        while (k > 0 && comp_(data_[k], data_[parent(k)])) {
            swap(data_[k], data_[parent(k)]);
            k = parent(k);
        }
    }

    void sink(int k) {
        int n = size_();
        while (left(k) < n) {
            int j = left(k);
            if (right(k) < n && comp_(data_[right(k)], data_[j])) j = right(k);
            if (!comp_(data_[j], data_[k])) break;
            swap(data_[k], data_[j]);
            k = j;
        }
    }
};

} // namespace dsa

int main() {
    using namespace dsa;

    // 1. 默认大顶堆（std::less 表示 a < b 时返回 true，"更大优先"）
    PriorityQueue<int> maxpq;
    for (int x : {3, 1, 4, 1, 5, 9, 2, 6}) maxpq.push(x);
    cout << "大顶堆弹出: ";
    while (!maxpq.empty()) cout << maxpq.top() << " ", maxpq.pop();
    cout << endl;   // 9 6 5 4 3 2 1 1

    // 2. 小顶堆（std::greater 表示 a > b 时返回 true，"更小优先"）
    PriorityQueue<int, std::greater<int>> minpq;
    for (int x : {3, 1, 4, 1, 5, 9, 2, 6}) minpq.push(x);
    cout << "小顶堆弹出: ";
    while (!minpq.empty()) cout << minpq.top() << " ", minpq.pop();
    cout << endl;   // 1 1 2 3 4 5 6 9

    // 3. 自定义比较器：按 pair 的 second 排序
    using P = pair<int, int>;  // {value, priority}
    PriorityQueue<P, std::greater<P>> taskpq;  // priority 小的先出
    taskpq.push({1, 3});
    taskpq.push({2, 1});
    taskpq.push({3, 2});
    while (!taskpq.empty()) {
        cout << "(" << taskpq.top().first << ", p=" << taskpq.top().second << ") ";
        taskpq.pop();
    }
    cout << endl;   // (2, p=1) (3, p=2) (1, p=3)
    return 0;
}
```

**关键设计点**：

1. **比较器 `comp(a, b)`**：当 `a` 应该排在 `b` **前面** 时返回 `true`。
   - `std::less<T>`（默认）：`a < b` 返回 `true` → 大顶堆。
   - `std::greater<T>`：`a > b` 返回 `true` → 小顶堆。
2. **0-indexed** 的父子关系：`parent(i) = (i-1)/2`，`left(i) = 2i+1`，`right(i) = 2i+2`。
3. **O(N) heapify**：从最后一个非叶子节点（`size/2 - 1`）开始往前 `sink`，总代价 O(N)，比逐个 `push` 的 O(N log N) 更优。

## 4. std::priority_queue 源码分析

C++ 标准库的 `std::priority_queue` 实际上是一个 **容器适配器**（container adapter），它自己不管理内存，只是把 `std::make_heap` / `std::push_heap` / `std::pop_heap` 这三个 STL 算法包成一个队列接口。

源码（简化版，源自 libstdc++）：

```cpp
template <typename T, typename Container = std::vector<T>,
          typename Compare = std::less<typename Container::value_type>>
class priority_queue {
protected:
    Container c_;       // 底层容器，默认 std::vector
    Compare comp_;      // 比较器

public:
    bool empty()  const { return c_.empty(); }
    std::size_t size() const { return c_.size(); }
    const T& top() const { return c_.front(); }

    void push(const T& x) {
        c_.push_back(x);
        std::push_heap(c_.begin(), c_.end(), comp_);
    }

    void pop() {
        std::pop_heap(c_.begin(), c_.end(), comp_);
        c_.pop_back();
    }
};
```

**关键点**：

1. **底层容器**默认是 `std::vector`，但你也可以换成 `std::deque`（不允许 `std::list`，因为 heap 算法要求随机访问迭代器）。
2. **`std::push_heap`** / **`std::pop_heap`** 这两个算法就是 swim / sink 的标准库版本。
3. **默认是大顶堆**，因为 `Compare = std::less<T>` 意味着 `a < b` 触发上浮，即大的往上走。

使用示例：

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    // 默认大顶堆
    priority_queue<int> maxpq;
    for (int x : {3, 1, 4, 1, 5, 9, 2, 6}) maxpq.push(x);
    cout << "默认大顶堆弹出: ";
    while (!maxpq.empty()) cout << maxpq.top() << " ", maxpq.pop();
    cout << endl;

    // 小顶堆：用 greater<int>
    priority_queue<int, vector<int>, greater<int>> minpq;
    for (int x : {3, 1, 4, 1, 5, 9, 2, 6}) minpq.push(x);
    cout << "小顶堆弹出: ";
    while (!minpq.empty()) cout << minpq.top() << " ", minpq.pop();
    cout << endl;

    // 自定义类型 + lambda 比较器
    using P = pair<int, string>;
    priority_queue<P, vector<P>, function<bool(const P&, const P&)>> taskpq(
        [](const P& a, const P& b) { return a.first < b.first; }  // priority 大的先出
    );
    taskpq.push({1, "low"});
    taskpq.push({5, "high"});
    taskpq.push({3, "mid"});
    while (!taskpq.empty()) {
        cout << taskpq.top().second << " ";
        taskpq.pop();
    }
    cout << endl;  // high mid low
    return 0;
}
```

## 5. Top K 问题：两种主流解法

Top K 问题是面试最高频的问题之一：「从 N 个元素中找出最大/最小的 K 个元素」。

### 5.1 方法一：小/大顶堆（O(N log K)）

**思路**：维护一个大小为 K 的堆，遍历 N 个元素：

- **第 K 大** → 用 **小顶堆**（堆顶是当前 K 个最大中的最小值，新元素如果比堆顶大就替换它）
- **第 K 小** → 用 **大顶堆**（堆顶是当前 K 个最小中的最大值）

```cpp
// LeetCode 215. 数组中的第 K 个最大元素
// 时间 O(N log K)，空间 O(K)
class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        // 小顶堆，堆顶是当前 K 个最大中的最小值
        priority_queue<int, vector<int>, greater<int>> pq;
        for (int x : nums) {
            pq.push(x);
            if ((int)pq.size() > k) pq.pop();  // 弹出当前最小
        }
        return pq.top();
    }
};
```

**为什么用小顶堆而不是大顶堆？**
小顶堆的堆顶是「当前 K 个候选者中最小的一个」，如果新元素比它大，说明新元素应该进入 Top K，旧的堆顶（最小候选）应该被淘汰。如果用大顶堆，堆顶是当前 K 个候选中最大的，新元素无法和它比较（因为堆顶可能比新元素大或小），逻辑混乱。

### 5.2 方法二：快速选择（期望 O(N)，最坏 O(N²)）

**思路**：仿照 [[44-quick-sort|快速排序]] 的 partition，每次只递归包含第 K 大元素的那一侧，期望复杂度 O(N)，最坏 O(N²)。

```cpp
// 快速选择：第 K 大
class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        // 第 K 大 = 第 N-K 小
        return quickSelect(nums, 0, nums.size() - 1, (int)nums.size() - k);
    }

private:
    int quickSelect(vector<int>& nums, int lo, int hi, int target) {
        int p = partition(nums, lo, hi);
        if (p == target) return nums[p];
        if (target < p) return quickSelect(nums, lo, p - 1, target);
        return quickSelect(nums, p + 1, hi, target);
    }

    int partition(vector<int>& nums, int lo, int hi) {
        int pivot = nums[hi], i = lo;
        for (int j = lo; j < hi; ++j) {
            if (nums[j] < pivot) swap(nums[i++], nums[j]);
        }
        swap(nums[i], nums[hi]);
        return i;
    }
};
```

### 5.3 选型对比

| 场景 | 推荐 | 理由 |
|------|------|------|
| **数据是流式的**（无法一次性加载） | 小顶堆 | 只需维护 K 大小的堆，O(N log K) |
| **数据可一次性加载**，且 N 很大 | 快速选择 | 期望 O(N)，但会修改原数组 |
| **N 较小，K 较大**（如 N=100, K=50） | 小顶堆 | O(N log K) ≈ O(N log N)，与排序相当 |
| **要求稳定 / 不允许修改原数组** | 拷贝一份再排序 | O(N log N) 简单稳妥 |

### 5.4 Top K 问题的扩展：前 K 高频元素

LeetCode 347 是 Top K 问题的经典变体：「给定一个非空整数数组，返回其中出现频率前 K 高的元素」。解法是先用哈希表统计频率，再用 **大小为 K 的最小堆** 按频率淘汰：

```cpp
// LeetCode 347. 前 K 个高频元素
// 时间 O(N log K)，空间 O(N)
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        // 1. 统计频率
        unordered_map<int, int> freq;
        for (int x : nums) freq[x]++;

        // 2. 用小顶堆按频率淘汰，堆中保留频率最高的 K 个
        //    堆元素: pair<频率, 数值>
        //    比较器：频率小的优先（这样堆顶是当前 K 个中频率最低的）
        using P = pair<int, int>;
        priority_queue<P, vector<P>, function<bool(const P&, const P&)>> pq(
            [](const P& a, const P& b) { return a.first > b.first; }
        );
        for (auto& [val, cnt] : freq) {
            pq.push({cnt, val});
            if ((int)pq.size() > k) pq.pop();
        }

        // 3. 收集结果
        vector<int> res;
        while (!pq.empty()) {
            res.push_back(pq.top().second);
            pq.pop();
        }
        return res;
    }
};
```

注意：**虽然是小顶堆，但比较器是 `a.first > b.first`（即 a 的频率更大时 a 应该排在 b 后面）**，与直觉相反。这是 STL 优先级队列的一个常见陷阱——比较器的语义是「**返回 true 表示 a 应该排在 b 后面**」，而不是「返回 true 表示 a 应该排在前面」。

### 5.5 复杂度对比总结

堆方法和排序方法在最坏情况下都是 O(N log N)（排序本身就是 O(N log N)，而 N log K ≤ N log N）；但堆方法在 K << N 时是 **O(N log K)**，远优于排序的 O(N log N)。这也是为什么 Top K 问题几乎都用堆而不是排序。

## 6. 复杂度表

| 操作 | 时间复杂度 | 空间复杂度 |
|------|-----------|-----------|
| top() / peek() | O(1) | O(1) |
| push() | O(log N) | O(1) |
| pop() | O(log N) | O(1) |
| heapify（建堆） | O(N) | O(1) |
| Top K（堆方法） | O(N log K) | O(K) |
| Top K（快速选择） | 期望 O(N)，最坏 O(N²) | O(1)（原地） |

## 7. 应用场景

- **操作系统进程调度**：每个进程有优先级，CPU 每次从优先级队列中取出优先级最高的进程运行。
- **Dijkstra 最短路径**：每次从「未确定最短路的节点集合」中取出距离最小的节点（用优先队列加速）。
- **Huffman 编码**：见 [[50-huffman-tree|赫夫曼编码]]，每次合并权重最小的两个节点（用优先队列实现贪心）。
- **A* 搜索**：用优先队列选取 f 值最小的状态进行扩展。
- **数据流中位数维护**：一个大顶堆存较小一半 + 一个小顶堆存较大一半。
- **Top K 问题**：面试高频，见 §5。

## 下一章

→ [[23-binary-tree-basic|二叉树基本概念及特殊二叉树]]

## 相关章节

- [[21-binary-heap-basic|二叉堆原理]] — 理解 swim/sink 的理论基础
- [[45-heap-sort|堆排序]] — 堆最重要的应用之一
- [[44-quick-sort|快速排序]] — Top K 问题的另一种解法
- [[50-huffman-tree|赫夫曼编码]] — 优先队列的另一个重要应用
