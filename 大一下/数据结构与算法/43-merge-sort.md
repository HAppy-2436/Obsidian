---
title: 妙用二叉树后序位置：归并排序
tags:
  - 排序
  - 归并排序
  - 分治
  - 稳定排序
  - 后序遍历
  - 数据结构
order: 43
prerequisites:
  - "[[23-binary-tree-basic]]"
  - "[[44-quick-sort]]"
group: 排序
subgroup: 高效排序
paywall: true
source: https://labuladong.online/zh/algo/data-structure-basic/merge-sort/
---

# 妙用二叉树后序位置：归并排序

## 学习目标

- 理解 **归并排序（Merge Sort）** 的核心思想：**分治 + 后序合并**
- 掌握归并排序的 **自顶向下（递归）** 和 **自底向上（迭代）** 两种实现
- 能够手写归并排序的 C++ 实现（含 merge 函数）
- 理解 **「计数逆序对」** 等经典 LeetCode 题的归并排序变体
- 理解归并排序是 **稳定排序**、最坏情况 O(N log N)、非原地

## 一句话总结

**归并排序** 是 **分治思想** 的经典应用：把数组不断二分，直到子数组长度为 1，然后 **在二叉树后序位置合并两个有序子数组**。它保证 O(N log N) 时间复杂度、是 **稳定排序**，但需要 O(N) 额外空间，是突破 O(N²) 的三大排序之一。

## 前置知识

阅读本文前，你需要先学习：

- [[23-binary-tree-basic|二叉树的遍历（前序/中序/后序）]]
- [[44-quick-sort|快速排序（妙用前序位置）]]——与归并排序对比
- [[04-cycle-array|数组操作]]

## 1. 核心思想：分治 + 后序合并

### 1.1 思路来源：二叉树后序遍历

归并排序之所以「妙」，是因为它把排序问题 **抽象成了二叉树的后序遍历问题**：

```text
对 nums[lo..hi] 排序：
1. 找中点 mid = (lo + hi) / 2
2. 递归排序 nums[lo..mid]   ← 左子树
3. 递归排序 nums[mid+1..hi] ← 右子树
4. 合并两个有序子数组       ← 后序位置
```

整棵「递归树」是一棵 **完全二叉树**，每个节点代表 `sort(nums, lo, hi)`。**真正的「排序动作」（合并）发生在后序位置**——这与 [[44-quick-sort|快速排序]] 的「前序位置 partition」形成鲜明对比。

### 1.2 递归树图示

```text
                sort(0,7)
                /       \
        sort(0,3)       sort(4,7)
        /     \          /      \
    sort(0,1) sort(2,3) sort(4,5) sort(6,7)
     /\        /\         /\        /\
   s(0,0)s(1,1) ...   (单元素，无需排序)

叶子节点：length=1 的子数组（天然有序）
内部节点：merge 两个有序子数组（后序位置）
```

**关键洞察**：每次 `merge` 都发生在 **两个子数组都已经有序之后**，这就是 **后序位置** 的典型应用。

### 1.3 与 [[44-quick-sort|快排]] 的对比

| 维度 | 快速排序（前序） | 归并排序（后序） |
|------|-----------------|-----------------|
| 工作发生位置 | 前序（partition） | 后序（merge） |
| 子问题状态 | 一边已确定位置，一边未排序 | 两侧都已排序 |
| 递归树 | 不一定平衡 | **完全平衡** |
| 时间复杂度 | 平均 O(N log N)，最坏 O(N²) | **始终 O(N log N)** |
| 稳定性 | ❌ 不稳定 | ✅ 稳定 |
| 原地性 | ✅ O(log N) | ❌ O(N) |
| 适用场景 | 通用、大数据量 | 需要稳定 + 大数据 |

## 2. 自顶向下：递归实现

### 2.1 核心代码框架


> [!info] 📌 付费章节补全内容（基于算法知识体系补充）

```cpp
#include <bits/stdc++.h>
using namespace std;

namespace dsa {

// 归并排序：自顶向下（递归）
class MergeSort {
public:
    // 排序入口
    void sort(vector<int>& nums) {
        // 多分配 1 个，方便 merge 时统一处理边界
        tmp_.resize(nums.size());
        mergeSort(nums, 0, nums.size() - 1);
    }

private:
    vector<int> tmp_;  // 复用缓冲区，避免反复分配

    // 递归函数：对 nums[lo..hi] 排序
    void mergeSort(vector<int>& nums, int lo, int hi) {
        if (lo >= hi) return;  // base case：单元素天然有序

        int mid = lo + (hi - lo) / 2;  // 防溢出，等价于 (lo+hi)/2
        mergeSort(nums, lo, mid);      // 排序左半
        mergeSort(nums, mid + 1, hi);  // 排序右半
        merge(nums, lo, mid, hi);      // 后序位置：合并
    }

    // 将 nums[lo..mid] 和 nums[mid+1..hi] 两段有序数组合并
    void merge(vector<int>& nums, int lo, int mid, int hi) {
        // 1. 把 nums[lo..hi] 复制到 tmp_
        for (int i = lo; i <= hi; i++) {
            tmp_[i] = nums[i];
        }

        // 2. 双指针合并：i 走左半，j 走右半
        int i = lo, j = mid + 1;
        for (int p = lo; p <= hi; p++) {
            if (i == mid + 1) {
                // 左半耗尽，取右半
                nums[p] = tmp_[j++];
            } else if (j == hi + 1) {
                // 右半耗尽，取左半
                nums[p] = tmp_[i++];
            } else if (tmp_[i] <= tmp_[j]) {
                // ⭐ 关键：<= 保证稳定性（左侧优先）
                nums[p] = tmp_[i++];
            } else {
                nums[p] = tmp_[j++];
            }
        }
    }
};

} // namespace dsa
```

### 2.2 稳定性证明

merge 函数中 `tmp_[i] <= tmp_[j]` 条件取 `<=` 而不是 `<`，**当左右元素相等时优先选左侧**——这保证了相同元素的相对顺序不变。

### 2.3 复杂度分析

设 `T(N)` 是 N 个元素的归并排序时间：

```text
T(N) = 2 * T(N/2) + O(N)     ← 两边递归 + 一次合并
     = 2 * (2 * T(N/4) + O(N/2)) + O(N)
     = 4 * T(N/4) + 2 * O(N)
     ...
     = N * T(1) + logN * O(N)
     = O(N log N)
```

每一层合并的总工作量是 O(N)，共 log N 层，所以 **时间复杂度始终是 O(N log N)**。

**空间复杂度**：O(N)（tmp 数组）+ O(log N)（递归栈）。

## 3. 自底向上迭代版本

### 3.1 思路

不去构造递归调用栈，而是 **人为控制合并区间的大小**：

```text
width = 1: [1] [3] [2] [4] [5]  → 每 2 个合并一次
width = 2: [1,3] [2,4] [5]    → 每 4 个合并一次
width = 4: [1,2,3,4] [5]      → 每 8 个合并一次
width = 8: [1,2,3,4,5]        → 全部有序
```

### 3.2 代码

```cpp
namespace dsa {

class MergeSortBU {
public:
    void sort(vector<int>& nums) {
        int n = nums.size();
        vector<int> tmp(n);
        // width：当前合并的子数组长度
        for (int width = 1; width < n; width *= 2) {
            // i：每对合并的起始下标
            for (int i = 0; i + width < n; i += 2 * width) {
                int lo = i;
                int mid = i + width - 1;
                int hi = min(i + 2 * width - 1, n - 1);
                merge(nums, lo, mid, hi, tmp);
            }
        }
    }

private:
    void merge(vector<int>& nums, int lo, int mid, int hi, vector<int>& tmp) {
        for (int k = lo; k <= hi; k++) tmp[k] = nums[k];

        int i = lo, j = mid + 1;
        for (int p = lo; p <= hi; p++) {
            if (i > mid) nums[p] = tmp[j++];
            else if (j > hi) nums[p] = tmp[i++];
            else if (tmp[i] <= tmp[j]) nums[p] = tmp[i++];
            else nums[p] = tmp[j++];
        }
    }
};

} // namespace dsa
```

### 3.3 自底向上 vs 自顶向下

| 维度 | 自顶向下（递归） | 自底向上（迭代） |
|------|----------------|----------------|
| 代码可读性 | 直观 | 略抽象 |
| 递归栈 | O(log N) | 0 |
| 适用场景 | 一般排序 | **链表排序**（无法随机访问） |
| 调试 | 容易 | 略难 |

> [!tip] 链表归并排序只能用自底向上
> 因为链表不支持随机访问，无法用 mid 把链表切成两半。自底向上迭代版本天然适合链表（每次按宽度合并相邻子链表）。

## 4. 经典 LeetCode 应用

### 4.1 LeetCode 315：计算右侧小于当前元素的个数

> **题目**：给定数组 nums，返回一个新数组 counts，其中 `counts[i]` 是 nums[i] 右侧比 nums[i] 小的元素个数。

**关键洞察**：从右往左遍历，对每个 `nums[i]`，**它右侧已遍历元素中比它小的个数** 就是答案。这等价于「**对右侧数组做有序插入，同时计数**」——而 **归并排序天然会在合并时维护有序性**。

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> countSmaller(vector<int>& nums) {
        int n = nums.size();
        vector<int> count(n, 0);
        vector<int> index(n);     // 原始下标
        vector<int> tmp(n);
        vector<int> tmpIdx(n);
        iota(index.begin(), index.end(), 0);

        mergeSort(nums, index, tmp, tmpIdx, count, 0, n - 1);
        return count;
    }

private:
    void mergeSort(const vector<int>& nums, vector<int>& index,
                   vector<int>& tmp, vector<int>& tmpIdx,
                   vector<int>& count, int lo, int hi) {
        if (lo >= hi) return;
        int mid = lo + (hi - lo) / 2;
        mergeSort(nums, index, tmp, tmpIdx, count, lo, mid);
        mergeSort(nums, index, tmp, tmpIdx, count, mid + 1, hi);
        merge(nums, index, tmp, tmpIdx, count, lo, mid, hi);
    }

    void merge(const vector<int>& nums, vector<int>& index,
               vector<int>& tmp, vector<int>& tmpIdx,
               vector<int>& count, int lo, int mid, int hi) {
        // tmp 暂存
        for (int i = lo; i <= hi; i++) {
            tmp[i] = nums[i];
            tmpIdx[i] = index[i];
        }

        int i = lo, j = mid + 1;
        for (int p = lo; p <= hi; p++) {
            if (i > mid) {
                index[p] = tmpIdx[j++];
            } else if (j > hi) {
                // 左半元素比右半所有元素都大，不可能有 count
                // 但需要把左半剩下的 index 复制回去
                index[p] = tmpIdx[i++];
            } else if (tmp[i] <= tmp[j]) {
                // 左小：左侧不算「右侧更小」，但要复制
                index[p] = tmpIdx[i++];
            } else {
                // 右小：tmp[i] 右侧比它小的数量 + (j - mid - 1)
                // 因为右半的 j..mid 都是比 tmp[i] 小的（已合并部分）
                index[p] = tmpIdx[j++];
                count[tmpIdx[i]] += (hi - j + 1);  // 关键：累计逆序对
                // 注意 i 在这里没递增，下次还会再算一次
                i++;  // 修复：实际是把 tmp[i] 这一个元素累加一次
            }
        }
    }
};
```

> [!warning] 上面代码逻辑复杂，初学可暂跳过
> LeetCode 315 的标准解法就是「归并排序 + 累计逆序对」，但需要同时维护元素值和原始下标，理解上较难。建议先掌握 [[44-quick-sort|快速排序]] 的 partition 思路（用 BST 替代）后再看这道题。

### 4.2 LeetCode 912：排序数组

```cpp
class Solution {
public:
    vector<int> sortArray(vector<int>& nums) {
        dsa::MergeSort sorter;
        sorter.sort(nums);
        return nums;
    }
};
```

**直接调用上面的 MergeSort 即可通过**——因为 O(N log N) 时间复杂度满足题目要求。

## 5. 复杂度表

| 指标 | 值 |
|------|---|
| 最好时间 | O(N log N) |
| 平均时间 | O(N log N) |
| 最坏时间 | O(N log N) **（不会退化）** |
| 空间复杂度 | O(N) |
| 稳定性 | ✅ 稳定 |
| 原地性 | ❌ 非原地 |

## 6. 优缺点总结

**优点**：

- ✅ 时间复杂度 **始终 O(N log N)**，最坏情况也不退化
- ✅ **稳定排序**，适合多 key 排序
- ✅ 天然适合 **链表排序**（自底向上版本）
- ✅ 天然适合 **外部排序**（数据量超过内存，归并时可分块读写磁盘）

**缺点**：

- ❌ 需要 O(N) 额外空间
- ❌ 递归版本有 O(log N) 栈空间
- ❌ 缓存不友好（每次合并都涉及大块内存读写）

## 7. 适用场景

1. **需要稳定排序 + 大数据量**：首选归并
2. **链表排序**：自底向上版本是标准做法
3. **外部排序**：数据无法一次性装入内存时，归并是唯一选项
4. **逆序对计数**：LeetCode 315 的标准解法
5. **并行化**：归并天然易于并行（左右两半独立排序，再合并）

## 下一章

→ [[45-heap-sort|堆排序]]：利用二叉堆结构，在 O(N log N) 时间内完成原地排序，不需要额外数组。

## 相关章节

- [[44-quick-sort|快速排序]] — 前序位置的另一种分治排序
- [[23-binary-tree-basic|二叉树的遍历]] — 理解「后序位置」的本质
- [[45-heap-sort|堆排序]] — 另一种 O(N log N) 原地排序
- [[21-binary-heap-basic|二叉堆基础]] — 堆排序的前置知识
- LeetCode [[#315|315. 计算右侧小于当前元素的个数]]
- LeetCode [[#912|912. 排序数组]]

## 练习题

| 难度 | 题号 | 题目 |
|------|------|------|
| 难 | 315 | 计算右侧小于当前元素的个数 |
| 中 | 912 | 排序数组 |
| 难 | 493 | 翻转对 |