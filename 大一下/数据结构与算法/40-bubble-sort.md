---
title: 拥有稳定性：冒泡排序
tags:
  - 排序
  - 冒泡排序
  - 稳定排序
  - 原地排序
  - 数据结构
order: 40
prerequisites:
  - "[[42-select-sort]]"
  - "[[04-cycle-array]]"
group: 排序
subgroup: 基础排序
paywall: false
source: https://labuladong.online/zh/algo/data-structure-basic/bubble-sort/
---

# 拥有稳定性：冒泡排序

## 学习目标

- 理解 **冒泡排序（Bubble Sort）** 的核心思想：相邻逆序对的逐步交换
- 通过对 [[42-select-sort|选择排序]] 的三波优化，掌握「**稳定排序 + 提前终止**」的改进思路
- 能够手写一个支持提前终止的冒泡排序
- 理解冒泡排序为何是稳定排序，且对 **部分有序数组** 很友好

## 一句话总结

**冒泡排序** 是对选择排序的优化版本：通过反复交换 **相邻逆序对**，把当前未排序部分的最小值「冒泡」到分界线位置。它拥有 **稳定性**，并在 **数组有序或接近有序** 时能提前终止（最好 O(N)），但平均仍为 O(N²)。

## 前置知识

阅读本文前，你需要先学习：

- [[42-select-sort|选择排序所面临的问题]]
- [[04-cycle-array|数组的增删查改操作]]

## 1. 选择排序的三大缺陷

前文 [[42-select-sort|选择排序]] 中我们分析了它有三大问题：

1. **不稳定排序**：每次交换 `nums[sortedIndex]` 和 `nums[minIndex]`，跨度大，可能打乱相同元素的相对顺序
2. **与初始有序度无关**：即便输入已经有序，依然执行 n²/2 次比较
3. **效率低下**：O(N²) 时间复杂度，常规优化无法突破

冒泡排序就是为了解决前两个问题而设计的。

## 2. 第一波优化：重获稳定性

### 2.1 选择排序为何不稳定？

关键在于「交换」步骤：

```text
[2, 2', 2'', 1, 1']
 ^           ^
sortedIndex  minIndex

交换后：[1, 2', 2'', _, 1']
                 ^
               ↑ 这里原本是 2，现在空出来
```

把 `nums[minIndex]` 放到 `nums[sortedIndex]` 这一步是稳定的，但 **把 `nums[sortedIndex]` 塞到 `nums[minIndex]`** 这步会破坏相对顺序。

### 2.2 优化思路：插入而非交换

不要图省事用 swap，而是模仿 [[04-cycle-array|数组中部插入]] 的做法：

```text
[2, 2', 2'', 1, 1']
 ^           ^
sortedIndex  minIndex

Step 1: 把 nums[sortedIndex..minIndex] 整体后移一位
        [1, 2', 2'', _, 1']
              ↑ sortedIndex+1 处空出来
Step 2: 把最小值放到 sortedIndex
        [1, 2, 2', 2'', 1']
```

这样 2, 2', 2'' 的相对顺序就保住了。

### 2.3 代码

```cpp
void sort(vector<int>& nums) {
    int n = nums.size();
    int sortedIndex = 0;
    while (sortedIndex < n) {
        int minIndex = sortedIndex;
        for (int i = sortedIndex + 1; i < n; i++) {
            if (nums[i] < nums[minIndex]) {
                minIndex = i;
            }
        }
        // 把 nums[minIndex] 插入到 nums[sortedIndex] 位置
        // nums[sortedIndex..minIndex] 整体后移一位
        int minVal = nums[minIndex];
        for (int i = minIndex; i > sortedIndex; i--) {
            nums[i] = nums[i - 1];
        }
        nums[sortedIndex] = minVal;

        sortedIndex++;
    }
}
```

> [!warning] 稳定性有了，效率却下降了
> 加上内层的数据搬移 for 循环，**实际执行次数比标准选择排序多**。Big O 仍是 O(N²)，但常数项显著增大。

## 3. 第二波优化：消除额外循环

### 3.1 合并两个 for 循环

选择排序的核心是「找到最小值 + 把它放到 sortedIndex」。能否在 **找最小值的过程中**，就顺便把它放到正确位置？

答案是：**倒序遍历未排序部分，只要发现逆序对就交换相邻元素**，最小值会像「冒泡」一样逐步浮到 sortedIndex 位置。

```text
初始 [3, 1, 2, 0, 4]，sortedIndex = 0
倒序遍历 i = n-1 → 1，发现逆序就 swap

i=3: [3, 1, 2, 0, 4]  (0<4? 否)
i=2: [3, 1, 2, 0, 4]  (2<0? 否)
i=1: [3, 1, 0, 2, 4]  (1<2? 是 → swap) → [3, 0, 1, 2, 4]
                                  (2<4? 是)
i=0: (1<3? 是 → swap) → [0, 3, 1, 2, 4]
       (3<1? 否)
       
sortedIndex=1
```

### 3.2 标准冒泡排序代码

```cpp
#include <bits/stdc++.h>
using namespace std;

namespace dsa {

// 冒泡排序（Bubble Sort）
// 时间复杂度：平均 O(N²)，最好 O(N)（加 flag 后）
// 空间复杂度：O(1)
// 稳定性：✅ 稳定（只交换相邻逆序对，不动相同元素）
void bubbleSort(vector<int>& nums) {
    int n = nums.size();
    int sortedIndex = 0;
    while (sortedIndex < n) {
        // 倒序遍历 [sortedIndex+1, n)，交换相邻逆序对
        for (int i = n - 1; i > sortedIndex; i--) {
            if (nums[i] < nums[i - 1]) {
                swap(nums[i], nums[i - 1]);
            }
        }
        sortedIndex++;
    }
}

} // namespace dsa
```

> [!success] 为什么叫「冒泡」？
> 数组尾部的最小元素，像水泡一样从底部 **逐步冒到顶部**（分界线位置）。每次内层循环结束后，当前未排序部分的最小值就稳稳地落到了 sortedIndex 处。

## 4. 第三波优化：提前终止

### 4.1 改进思路

加一个 `swapped` 标志位，**如果某一趟内层循环没有发生任何交换**，说明数组已经有序，可以直接跳出。

### 4.2 完整代码

```cpp
namespace dsa {

// 冒泡排序（带提前终止）
// 最好时间复杂度：O(N)（已排序数组直接退出）
// 平均/最坏：O(N²)
void bubbleSortEarlyStop(vector<int>& nums) {
    int n = nums.size();
    int sortedIndex = 0;
    while (sortedIndex < n) {
        bool swapped = false;
        for (int i = n - 1; i > sortedIndex; i--) {
            if (nums[i] < nums[i - 1]) {
                swap(nums[i], nums[i - 1]);
                swapped = true;
            }
        }
        // 这一趟没有任何交换 → 数组已经有序，提前终止
        if (!swapped) {
            break;
        }
        sortedIndex++;
    }
}

} // namespace dsa
```

### 4.3 效果

| 输入类型 | 比较次数 |
|---------|---------|
| 完全有序 | n - 1 次（一趟就退出） |
| 部分有序 | 取决于「逆序对」数量 |
| 完全逆序 | n²/2 次（最坏情况） |

## 5. 与选择排序的对比

| 维度 | [[42-select-sort\|选择排序]] | 冒泡排序 |
|------|---------|---------|
| 稳定性 | ❌ 不稳定 | ✅ 稳定 |
| 提前终止 | ❌ 不支持 | ✅ 加 flag 即可 |
| 实际比较次数 | ~n²/2 | ≤ n²/2 |
| 交换次数 | 最多 N 次 | 取决于逆序对数 |
| 原地 | ✅ | ✅ |

> [!tip] 选择 vs 冒泡的工程选择
> 如果 **交换代价远大于比较代价**（比如写入 EEPROM、SSD 块擦写），**选择排序更优**（交换次数少）。
> 如果 **稳定性是刚需**，必须用冒泡排序。
> 否则在大数据量场景两者都不实用，应选 [[44-quick-sort|快速排序]]。

## 6. 复杂度表

| 指标 | 值 |
|------|---|
| 最好时间 | O(N)（加 flag 提前终止） |
| 平均时间 | O(N²) |
| 最坏时间 | O(N²) |
| 空间复杂度 | O(1) |
| 稳定性 | ✅ 稳定 |
| 原地性 | ✅ 原地 |

## 7. 冒泡排序的适用场景

虽然冒泡排序在大数据量场景几乎不会被使用，但它的价值在于：

- **教学价值**：通过反复优化，认识「稳定性」「提前终止」这些指标
- **小数据 + 已排序场景**：N ≤ 50 且接近有序时，常数极小，比快排还快
- **稳定排序需求 + 小数据**：在 N 不大且需要稳定的场景

## 下一章

→ [[41-insertion-sort|运用逆向思维：插入排序]]：用「**往左插**」替代「**找最小值往左放**」，得到另一种稳定排序。

## 相关章节

- [[42-select-sort|选择排序]] — 冒泡排序的优化起点
- [[41-insertion-sort|插入排序]] — 另一种稳定排序
- [[46-shell-sort|希尔排序]] — 插入排序的「跳步」优化，突破 O(N²)
- [[39-sort-basic|排序算法的关键指标]] — 稳定性的价值
- LeetCode [[#912|912. 排序数组]]

## 练习题

| 难度 | 题号 | 题目 |
|------|------|------|
| 中 | 912 | 排序数组 |