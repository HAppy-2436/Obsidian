---
title: 二叉堆结构的运用：堆排序
tags:
  - 排序
  - 堆排序
  - 二叉堆
  - 原地排序
  - 数据结构
order: 45
prerequisites:
  - "[[21-binary-heap-basic]]"
  - "[[22-binary-heap-implement]]"
group: 排序
subgroup: 高效排序
paywall: false
source: https://labuladong.online/zh/algo/data-structure-basic/heap-sort/
---

# 二叉堆结构的运用：堆排序

## 学习目标

- 理解 **堆排序（Heap Sort）** 的两步流程：**Heapify（建堆）+ Sort（排序）**
- 掌握原地建堆的 **sink 自底向上** 算法，理解为什么是 O(N) 而非 O(N log N)
- 能够手写堆排序的 C++ 实现
- 理解堆排序是 **O(N log N) + 原地** 但 **不稳定** 的排序

## 一句话总结

**堆排序** 把 [[21-binary-heap-basic|二叉堆]] 的两个核心操作（swim + sink）应用到数组排序中，分两步：**原地建堆（heapify）+ 反复 sink 取出最大值**。它保证 O(N log N) 时间复杂度、O(1) 额外空间，但 **不稳定**。

## 前置知识

阅读本文前，你需要先学习：

- [[21-binary-heap-basic|二叉堆核心原理]]
- [[22-binary-heap-implement|二叉堆实现优先级队列]]

## 1. 为什么堆能用来排序？

### 1.1 二叉堆的回顾

> 如果你已经忘了 swim / sink 的细节，请先回到 [[21-binary-heap-basic|二叉堆核心原理]] 复习。

二叉堆（**完全二叉树 + 堆序性**）的两个核心操作：

- **swim（上浮）**：新插入元素向上冒到正确位置，O(log N)
- **sink（下沉）**：堆顶被换走后向下沉到正确位置，O(log N)

基于这两个操作，[[22-binary-heap-implement|优先级队列]] 实现了：

- **push**：放到末尾 → swim
- **pop**：堆顶与末尾交换 → 弹出末尾 → sink

### 1.2 最直接的「堆排序」

```cpp
// 思路：把所有元素 push 到小顶堆，再依次 pop 出来
void sort(vector<int>& nums) {
    SimpleMinPQ pq(nums.size());  // 小顶堆
    for (int num : nums) pq.push(num);
    for (int i = 0; i < nums.size(); i++) {
        nums[i] = pq.pop();
    }
}
```

这个思路 **逻辑正确**，时间复杂度 O(N log N)，但 **空间复杂度 O(N)**（额外建了一个堆）。

> [!question] 能否直接在原数组上做？
> 堆排序要解决的问题就是：**不申请额外空间，直接在原数组上 sink / swim**，用 O(1) 空间实现 O(N log N) 排序。

## 2. 堆排序的两个关键步骤

### 2.1 整体框架

```text
堆排序：
  1. heapify：把 nums[0..n-1] 原地变成大顶堆（O(N)）
  2. sort：反复把堆顶（最大值）与末尾交换，缩减堆大小并 sink（O(N log N)）
```

### 2.2 准备工作：复用 swim / sink

先用 **0-indexed** 数组实现 swim 和 sink（参考 [[21-binary-heap-basic|二叉堆基础]]）：

```cpp
namespace dsa {

class HeapSort {
public:
    void sort(vector<int>& nums) {
        int n = nums.size();

        // ===== 第一步：原地建堆（heapify）=====
        // 从最后一个非叶子节点开始，自底向上 sink
        // 最后一个非叶子节点的下标 = parent(n-1) = (n-2)/2
        for (int i = (n - 2) / 2; i >= 0; i--) {
            sink(nums, i, n);
        }

        // ===== 第二步：排序（Sort）=====
        // 反复把堆顶（最大值）交换到末尾，缩减堆大小
        for (int i = n - 1; i > 0; i--) {
            swap(nums[0], nums[i]);   // 把最大值放到 nums[i]
            sink(nums, 0, i);         // 对堆顶 sink，堆大小变为 i
        }
    }

private:
    // 0-indexed 下的父子关系
    int parent(int i) { return (i - 1) / 2; }
    int left(int i)   { return 2 * i + 1; }
    int right(int i)  { return 2 * i + 2; }

    // 上浮（swim）
    void swim(vector<int>& nums, int k) {
        while (k > 0 && nums[k] > nums[parent(k)]) {
            swap(nums[k], nums[parent(k)]);
            k = parent(k);
        }
    }

    // 下沉（sink）：对 nums[0..n-1] 中的下标 k 进行下沉
    void sink(vector<int>& nums, int k, int n) {
        while (true) {
            int l = left(k), r = right(k), j = k;
            if (l < n && nums[l] > nums[j]) j = l;
            if (r < n && nums[r] > nums[j]) j = r;
            if (j == k) break;
            swap(nums[k], nums[j]);
            k = j;
        }
    }
};

} // namespace dsa
```

## 3. 第一步详解：原地建堆（Heapify）

### 3.1 为什么是 O(N)？

直觉上会以为 heapify 是 O(N log N)（N 次插入，每次 log N）。但 **自底向上 sink** 比想象中更快：

```text
完全二叉树中：
- 大部分节点在底层（叶子）
- 叶子节点不需要 sink（它们没有子节点）
- 越靠近根的节点越少

叶子节点数：约 N/2
倒数第二层节点数：N/4，每个最多 sink 1 次
倒数第三层：N/8，每个最多 sink 2 次
...
根节点：1 个，最多 sink log N 次

总操作数 = N/4 * 1 + N/8 * 2 + N/16 * 3 + ... + 1 * log N
       < N * (1/4 + 2/8 + 3/16 + ...)
       = N * (1/4 + 1/4 + 1/4 + ...)   ← 公比 1/2 的等差/等比混合
       < N
```

**数学上**：∑(k * N / 2^k) for k=1..logN = **O(N)**。

> [!tip] 「自底向上 sink」比「自顶向下 swim」更快
> swim 从叶子到根，每条路径 log N，N 个元素总和 O(N log N)
> sink 从 root 到叶子，但 **只有上半部分的节点需要 sink**，下半部分是叶子 → O(N)

### 3.2 可视化建堆过程

```text
初始数组：[5, 3, 8, 1, 9, 7, 6]  （按层遍历对应的完全二叉树）

                5
              /   \
             3     8
            / \   / \
           1   9 7   6

从下标 (7-2)/2 = 2 开始（即值为 8）：

i=2 (8): 检查子节点 7, 6 → 8 > 7 且 8 > 6，不动
                5
              /   \
             3     8
            / \   / \
           1   9 7   6

i=1 (3): 检查子节点 1, 9 → 9 > 3，交换 → 子节点 9 → 检查它的子节点（无）
                5
              /   \
             9     8
            / \   / \
           1   3 7   6

i=0 (5): 检查子节点 9, 8 → 9 > 5，交换到根
        现在 5 在下标 1，检查它的子节点 1, 3 → 3 > 1，5 < 3，交换
                9
              /   \
             5     8
            / \   / \
           1   3 7   6

最终大顶堆：
                9
              /   \
             5     8
            / \   / \
           1   3 7   6
```

## 4. 第二步详解：原地排序

### 4.1 排序逻辑

大顶堆的堆顶是 **最大值**。每次：

1. 交换 `nums[0]`（堆顶）和 `nums[i]`（当前末尾）
2. 堆大小减 1（不再考虑 `nums[i]`，它已就位）
3. 对新的堆顶 `nums[0]` 调用 `sink(nums, 0, i)`

这样反复 N-1 次后，**数组就变成从小到大**。

### 4.2 可视化

```text
初始大顶堆：[9, 5, 8, 1, 3, 7, 6]

第 1 次：
  swap(9, 6) → [6, 5, 8, 1, 3, 7, 9]
  对 6 sink，堆大小=6 → [8, 5, 7, 1, 3, 6]
                              ↑ 已就位

第 2 次：
  swap(8, 6) → [6, 5, 7, 1, 3, 8, 9]
  对 6 sink → [7, 5, 6, 1, 3]
                            ↑↑ 已就位

...

最终：[1, 3, 5, 6, 7, 8, 9]
```

## 5. 完整代码（带测试）

```cpp
#include <bits/stdc++.h>
using namespace std;

namespace dsa {

class HeapSort {
public:
    void sort(vector<int>& nums) {
        int n = nums.size();
        if (n <= 1) return;

        // 1. Heapify：从最后一个非叶子节点开始，自底向上 sink
        for (int i = parent(n - 1); i >= 0; i--) {
            sink(nums, i, n);
        }

        // 2. Sort：反复把堆顶最大值交换到末尾
        for (int i = n - 1; i > 0; i--) {
            swap(nums[0], nums[i]);
            sink(nums, 0, i);
        }
    }

private:
    int parent(int i) { return (i - 1) / 2; }
    int left(int i)   { return 2 * i + 1; }
    int right(int i)  { return 2 * i + 2; }

    void sink(vector<int>& nums, int k, int heapSize) {
        while (true) {
            int l = left(k), r = right(k), j = k;
            if (l < heapSize && nums[l] > nums[j]) j = l;
            if (r < heapSize && nums[r] > nums[j]) j = r;
            if (j == k) break;
            swap(nums[k], nums[j]);
            k = j;
        }
    }
};

} // namespace dsa

int main() {
    vector<int> nums = {5, 3, 8, 1, 9, 7, 6};
    dsa::HeapSort sorter;
    sorter.sort(nums);
    for (int x : nums) cout << x << " ";  // 1 3 5 6 7 8 9
    cout << endl;
    return 0;
}
```

## 6. 复杂度分析

### 6.1 时间复杂度

| 阶段 | 时间复杂度 |
|------|-----------|
| Heapify（建堆） | O(N) |
| Sort（每趟 sink） | O(log N) |
| Sort 总计（N 趟） | O(N log N) |
| **总时间** | **O(N log N)** |

### 6.2 空间复杂度

- 原地排序：**O(1)** 额外空间
- 递归栈：无（迭代实现）

### 6.3 稳定性

**❌ 不稳定**。原因是 sink 过程中的交换会跨距离，破坏相同元素的相对顺序。

```text
[2a, 1, 2b] 建堆后假设变成大顶堆 [2a, 2b, 1]
第一次 sort：swap(2a, 1) → [1, 2b, 2a]
                sink 后：[2b, 1, 2a]
第二次 sort：swap(2b, 2a) → [2a, 1, 2b]
最终结果中 2a 在 2b 之前，相对顺序改变 → 不稳定
```

## 7. 复杂度表

| 指标 | 值 |
|------|---|
| 最好时间 | O(N log N) |
| 平均时间 | O(N log N) |
| 最坏时间 | O(N log N) **（不会退化）** |
| 空间复杂度 | O(1) |
| 稳定性 | ❌ 不稳定 |
| 原地性 | ✅ 原地 |

## 8. 与 [[44-quick-sort|快排]]、[[43-merge-sort|归并]] 的对比

| 维度 | 堆排序 | 快速排序 | 归并排序 |
|------|--------|---------|---------|
| 时间复杂度（最坏） | **O(N log N)** | O(N²) | O(N log N) |
| 时间复杂度（平均） | O(N log N) | O(N log N) | O(N log N) |
| 空间复杂度 | **O(1)** | O(log N) | O(N) |
| 稳定性 | ❌ | ❌ | ✅ |
| 缓存友好度 | 差 | **好** | 一般 |
| 常数因子 | 大（swim/sink 多次访问父子） | 小 | 中 |

### 8.1 为什么堆排序实际比快排慢？

虽然 Big O 一样，但堆排序有以下劣势：

- **缓存不友好**：sink 时访问的下标 `2k+1`、`2k+2` 跨越的内存较大，CPU cache 命中率低
- **比较次数多**：每次 sink 都要比较左右子节点 + 父节点
- **分支预测差**：判断左右子节点大小的 if-else 不利于 CPU 流水线

> [!tip] 工程经验
> 实际工程中，**快排通常是 O(N log N) 排序中最快的**。堆排序的 O(N log N) 是「**数学保证**」，但常数因子让它在实践中反而慢于快排。

## 9. 适用场景

1. **需要保证最坏 O(N log N) + 原地**：堆排序是唯一选择（如嵌入式实时系统）
2. **Top K 问题**：维护大小为 K 的小顶堆，O(N log K)
3. **优先级队列底层**：堆是 [[22-binary-heap-implement|std::priority_queue]] 的底层结构
4. **流式数据中位数**：用大顶堆 + 小顶堆维护中位数

## 下一章

→ [[47-counting-sort|计数排序]]：进入非比较类排序的世界，O(N + k) 时间内完成排序。

## 相关章节

- [[21-binary-heap-basic|二叉堆基础]] — 堆排序的前置知识
- [[22-binary-heap-implement|二叉堆实现优先级队列]]
- [[44-quick-sort|快速排序]] — 与堆排序对比
- [[43-merge-sort|归并排序]] — 另一种 O(N log N) 排序
- LeetCode [[#912|912. 排序数组]]
- LeetCode [[#215|215. 数组中的第 K 个最大元素]]

## 练习题

| 难度 | 题号 | 题目 |
|------|------|------|
| 中 | 912 | 排序数组 |
| 中 | 215 | 数组中的第 K 个最大元素 |
| 难 | 295 | 数据流的中位数 |