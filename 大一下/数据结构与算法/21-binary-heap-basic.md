---
title: 二叉堆核心原理及可视化
tags:
  - 二叉堆
  - 堆排序
  - 优先级队列
  - 数据结构
order: 21
prerequisites:
  - "[[02-array-basic]]"
  - "[[23-binary-tree-basic]]"
group: 二叉堆
subgroup: null
paywall: true
source: https://labuladong.online/zh/algo/data-structure-basic/binary-heap-basic/
---

# 二叉堆核心原理及可视化

## 学习目标

- 理解二叉堆的本质：一种 **特殊的完全二叉树**
- 掌握 **大顶堆 / 小顶堆** 的定义与区别
- 理解 **swim（上浮）** 与 **sink（下沉）** 两个核心操作
- 理解为何二叉堆能用 **数组** 紧凑存储
- 能够手写一个最小堆的 C++ 实现
- 了解二叉堆的两个核心应用：[[45-heap-sort|堆排序]] 与 [[22-binary-heap-implement|优先级队列]]

## 一句话总结

二叉堆是一种能够 **动态维护最值** 的数据结构，是 [[23-binary-tree-basic|二叉树结构]] 在「完全二叉树 + 堆序性质」约束下的延伸；它的两个核心操作是 **sink（下沉）** 与 **swim（上浮）**，主要应用是 **优先级队列（Priority Queue）** 与 **堆排序（Heap Sort）**。

## 前置知识

阅读本文前，你需要先学习：

- [[02-array-basic|数组（顺序存储）的原理]]
- [[23-binary-tree-basic|二叉树基本概念及特殊二叉树]]

## 1. 二叉堆的本质：完全二叉树 + 堆序性质

### 1.1 二叉堆的定义

二叉堆（Binary Heap）必须满足以下两个性质：

1. **结构性**：是一棵 **完全二叉树**（即除最后一层外每层都是满的，且最后一层的节点紧凑靠左排列）。
2. **堆序性**：每个节点的值都必须 **大于等于（或小于等于）其子节点的值**。
   - 若父节点 ≥ 子节点，则称为 **大顶堆（Max Heap）**。
   - 若父节点 ≤ 子节点，则称为 **小顶堆（Min Heap）**。

> [!tip] 为什么是「完全二叉树」？
> 完全二叉树能用数组紧凑存储（不需要指针），且父子节点的索引存在数学关系（见 §1.3），所以堆是「用数组实现的树」的最佳代表。

### 1.2 直观理解

下面是一棵 **大顶堆**（每个父节点都 ≥ 子节点）：

```
              10
            /    \
           7      9
          / \    / \
         5   6  8   ?
```

把它存储到数组 `arr` 中（按层遍历、从 1 开始编号）：

```
索引:  1   2   3   4   5   6   7
值:   10   7   9   5   6   8   ?
```

你会发现，`arr[1] = 10` 是最大值，`arr[2] = 7`、`arr[3] = 9` 都小于等于 `10`，等等。这就是大顶堆。

### 1.3 数组存储的核心公式

二叉堆用数组存储时（**1-indexed**，从下标 1 开始），对于下标为 `i` 的节点：

| 关系 | 公式 |
|------|------|
| 父节点 | `parent(i) = i / 2` |
| 左子节点 | `left(i) = 2 * i` |
| 右子节点 | `right(i) = 2 * i + 1` |

如果采用 **0-indexed**（从下标 0 开始）：

| 关系 | 公式 |
|------|------|
| 父节点 | `parent(i) = (i - 1) / 2` |
| 左子节点 | `left(i) = 2 * i + 1` |
| 右子节点 | `right(i) = 2 * i + 2` |

**为什么不用 0-indexed？** 因为 `parent(0) = -1/2 = 0`（整数除法），会指向自己；而 1-indexed 中 `parent(1) = 0` 是有效的「哨兵」。实际工程上两种都常用，关键是保持一致。

## 2. 大顶堆 vs 小顶堆

| 性质 | 大顶堆（Max Heap） | 小顶堆（Min Heap） |
|------|-------------------|-------------------|
| 父节点 vs 子节点 | 父 ≥ 子 | 父 ≤ 子 |
| 堆顶（root） | 最大值 | 最小值 |
| 应用 | 堆排序升序（每次 pop 最大） | 优先级队列（任务调度）、堆排序降序、Top K |

C++ STL 的 [[22-binary-heap-implement|std::priority_queue]] 默认是 **大顶堆**；如果需要小顶堆，可以传入 `std::greater<T>()` 作为比较函数。

## 3. 核心操作：swim（上浮）与 sink（下沉）

二叉堆的全部 API（push、pop、top）都建立在两个原语之上：

### 3.1 swim（上浮 / 上升）

> 当某个节点 **比父节点更大**（大顶堆），就把它和父节点交换，直到它不再比父节点大，或者上浮到了 root。

```text
swim(k):
    while k > 1 and arr[k] > arr[k/2]:
        swap(arr[k], arr[k/2])
        k = k / 2
```

**作用**：用于 `push` 操作。把新元素放到数组末尾，然后调用 `swim(N)` 让它上浮到正确位置。

### 3.2 sink（下沉 / 下沉）

> 当某个节点 **比某个子节点更小**（大顶堆），就把它和 **更大的那个子节点** 交换，直到它不再比子节点小，或者下沉到了叶子节点。

```text
sink(k):
    while 2*k <= N:
        j = 2*k                       # 左子节点
        if j+1 <= N and arr[j+1] > arr[j]:
            j = j + 1                 # 选左右子节点中更大的
        if arr[k] >= arr[j]:
            break
        swap(arr[k], arr[j])
        k = j
```

**作用**：用于 `pop` 操作。把堆顶和最后一个元素交换，弹出堆顶，然后对新的 root 调用 `sink(1)`。

### 3.3 复杂度分析

- 单次 swim 或 sink 的复杂度为 **O(log N)**（因为完全二叉树的高度是 log N）。
- 整个堆的 push、pop、top 都是 O(log N)、O(log N)、O(1)。

### 3.4 为什么 swim 和 sink 一定要用 while 循环？

很多初学者第一次实现堆时会写成 `if` 单次比较，这是错误的。原因是：当我们把一个节点和它的父节点（或子节点）交换后，**新位置可能仍然不满足堆序**。比如大顶堆中插入 100，可能需要连续上浮 3-4 次才能到达 root；只有 `while` 才能保证它一路上浮到正确位置。`sink` 同理，下沉后还可能继续违反堆序。

### 3.5 堆与平衡二叉搜索树的区别

虽然堆和 [[27-tree-map-basic|二叉搜索树（BST）]] 都能动态维护有序数据，但它们的设计目标不同：

| 数据结构 | 目标 | 找最值 | 找任意值 | 插入/删除 |
|---------|------|--------|---------|----------|
| 二叉堆 | 维护 **最值** | **O(1)**（堆顶） | O(N) | O(log N) |
| 二叉搜索树 | 维护 **全局有序** | O(log N)（最值在叶子） | **O(log N)** | O(log N) |
| 平衡 BST（红黑树） | 维护 **全局有序 + 自平衡** | O(log N) | **O(log N)** | O(log N) |

如果你的需求是「反复拿当前最大/最小」，用堆；如果需求是「查找任意值 / 范围查询」，用 BST。

## 4. 堆的可视化文字描述

下面通过一个 **插入 5 个元素** 的例子演示大顶堆的可视化过程（push 操作）：

**插入 5 → 直接放到末尾**：

```
树:    5
数组: [_, 5]
```

**插入 3 → 末尾，5 > 3，不需要 swim**：

```
树:    5
      /
     3
数组: [_, 5, 3]
```

**插入 8 → 末尾，3 < 8，swim 上浮一次**：

```
树:    8
      / \
     3   5
数组: [_, 8, 3, 5]
```

**插入 1 → 末尾，5 > 1，不需要 swim**：

```
树:    8
      / \
     3   5
    /
   1
数组: [_, 8, 3, 5, 1]
```

**插入 9 → 末尾，1 < 9，swim → 3 < 9，swim → 到达 root**：

```
树:    9
      / \
     8   5
    / \
   1   3
数组: [_, 9, 8, 5, 1, 3]
```

**结论**：堆顶始终是最大值（9），每次 `pop` 都能拿到当前剩余元素中的最大者——这就是堆排序和优先级队列的基础。

### 4.1 pop 操作的可视化

与 push 相反，`pop` 操作把堆顶元素取出，然后用最后一个元素填补 root，再调用 `sink` 让它下沉：

```
初始:    9                pop → 取出 9
       / \
      8   5
     / \
    1   3

步骤 1: 交换 root 和最后一个元素，弹出末尾
树:    3
      / \
     8   5
    /
   1
数组: [_, 3, 8, 5, 1]

步骤 2: 对 root=3 调用 sink(1)
3 < 8（更大的子节点），交换
树:    8
      / \
     3   5
    /
   1
数组: [_, 8, 3, 5, 1]

步骤 3: sink(2) = 3 的左子节点是 1，3 > 1，停止
最终堆顶为 8，依次 pop 可得到 8 5 3 1
```

可以看到，**每次 pop 都能拿到当前最大的元素**——这就是 [[45-heap-sort|堆排序]] 的核心思想：把所有元素 push 到堆中，然后依次 pop 出来，就是降序序列；反之可得到升序序列。

### 4.2 为什么 push/pop 是 O(log N)？

完全二叉树的高度是 `⌊log₂ N⌋ + 1`。`swim` 和 `sink` 沿着父子路径走，最多走树的深度，因此单次操作的时间复杂度是 **O(log N)**。这个性质让二叉堆在维护「动态最值」时远比有序数组（插入 O(N)）和链表（找最值 O(N)）高效。

## 5. 二叉堆的 C++ 实现

下面给出一个完整、可编译的大顶堆 C++ 实现（基于 `std::vector`，0-indexed）：

> 以下是二叉堆的完整 C++ 实现，包括 push、pop、top、heapify 等核心 API。


> [!info] 📌 付费章节补全内容（基于算法知识体系补充）

```cpp
#include <bits/stdc++.h>
using namespace std;

namespace dsa {

// 大顶堆（Max Heap）：父节点 ≥ 子节点，堆顶为最大值
class MaxHeap {
public:
    // 1. 插入新元素：放到末尾，然后 swim 上浮
    void push(int x) {
        data.push_back(x);
        swim(size() - 1);
    }

    // 2. 弹出堆顶（最大值）：把末尾元素提到 root，然后 sink 下沉
    int pop() {
        int top = data[0];
        data[0] = data.back();
        data.pop_back();
        if (!data.empty()) sink(0);
        return top;
    }

    // 3. 查看堆顶（不删除）
    int top() const { return data[0]; }

    // 4. 判空和大小
    bool empty() const { return data.empty(); }
    int size() const { return (int)data.size(); }

    // 5. heapify：把一个无序数组变成堆（从最后一个非叶子节点开始 sink）
    //    时间复杂度 O(N)，比逐个 push 的 O(N log N) 更快
    MaxHeap(const vector<int>& arr) : data(arr) {
        for (int i = parent(size() - 1); i >= 0; --i) {
            sink(i);
        }
    }

private:
    vector<int> data;

    // 0-indexed 下的父子关系
    static int parent(int i) { return (i - 1) / 2; }
    static int left(int i)   { return 2 * i + 1; }
    static int right(int i)  { return 2 * i + 2; }

    // swim：把下标 k 处的元素上浮到正确位置（大顶堆版本）
    void swim(int k) {
        while (k > 0 && data[k] > data[parent(k)]) {
            swap(data[k], data[parent(k)]);
            k = parent(k);
        }
    }

    // sink：把下标 k 处的元素下沉到正确位置（大顶堆版本）
    void sink(int k) {
        int n = size();
        while (true) {
            int l = left(k), r = right(k), j = k;
            if (l < n && data[l] > data[j]) j = l;
            if (r < n && data[r] > data[j]) j = r;
            if (j == k) break;
            swap(data[k], data[j]);
            k = j;
        }
    }
};

} // namespace dsa

int main() {
    using namespace dsa;

    // 演示 1：逐个 push + pop
    MaxHeap h;
    for (int x : {5, 3, 8, 1, 9}) h.push(x);
    cout << "堆顶: " << h.top() << endl;   // 输出 9
    cout << "pop 顺序: ";
    while (!h.empty()) cout << h.pop() << " ";  // 输出 9 8 5 3 1
    cout << endl;

    // 演示 2：heapify（O(N) 建堆）
    MaxHeap h2({5, 3, 8, 1, 9, 7, 6});
    cout << "heapify 后堆顶: " << h2.top() << endl;  // 输出 9

    return 0;
}
```

**输出**：

```text
堆顶: 9
pop 顺序: 9 8 5 3 1
heapify 后堆顶: 9
```

## 6. 复杂度表

| 操作 | 时间复杂度 | 空间复杂度 |
|------|-----------|-----------|
| top() / peek() | O(1) | O(1) |
| push() | O(log N) | O(1) |
| pop() | O(log N) | O(1) |
| heapify（建堆） | O(N) | O(1) |
| 整体存储 | — | O(N) |

## 7. 应用场景

- **堆排序（Heap Sort）**：见 [[45-heap-sort|堆排序]]，基于 `push` + `pop` 或原地 heapify 实现，复杂度 O(N log N)、原地排序。
- **优先级队列（Priority Queue）**：见 [[22-binary-heap-implement|优先级队列实现]]，任务调度、Dijkstra 算法、Huffman 编码都需要它。
- **Top K 问题**：维护一个大小为 K 的小顶堆，可在 O(N log K) 内找到第 K 大/小的元素。
- **流式数据的中位数**：用一个大顶堆 + 一个小顶堆，可以在 O(log N) 内维护中位数。

## 下一章

→ [[22-binary-heap-implement|堆排序/优先级队列的代码实现]]

## 相关章节

- [[02-array-basic|数组原理]] — 二叉堆的底层存储结构
- [[23-binary-tree-basic|二叉树基础]] — 二叉堆的逻辑结构
- [[45-heap-sort|堆排序]] — 二叉堆最重要的应用之一
- [[27-tree-map-basic|二叉搜索树原理]] — 另一种「动态排序」数据结构，对比学习
