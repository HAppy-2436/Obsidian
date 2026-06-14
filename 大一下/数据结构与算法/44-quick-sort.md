---
title: 妙用二叉树前序位置：快速排序
tags:
  - 排序
  - 快速排序
  - 分治
  - partition
  - 前序遍历
  - 数据结构
order: 44
prerequisites:
  - "[[42-select-sort]]"
  - "[[23-binary-tree-basic]]"
group: 排序
subgroup: 高效排序
paywall: true
source: https://labuladong.online/zh/algo/data-structure-basic/quick-sort/
---

# 妙用二叉树前序位置：快速排序

## 学习目标

- 理解 **快速排序（Quick Sort）** 的核心思想：**分治 + 前序 partition**
- 掌握 **单向扫描、双向扫描、三路快排** 三种 partition 实现
- 理解 **随机化优化** 如何避免最坏 O(N²)
- 能够手写快速排序的 C++ 实现
- 理解快排是 **不稳定** 但 **原地** 的排序，平均 O(N log N)

## 一句话总结

**快速排序** 是分治思想的另一个经典应用：每次在 **前序位置** 找到一个 pivot 的正确位置（partition），然后递归排序左右两侧。它平均 O(N log N) 且 **原地**，但 **不稳定** 且最坏 O(N²)——需要 **随机化 pivot** 来降低最坏概率。

## 前置知识

阅读本文前，你需要先学习：

- [[42-select-sort|选择排序所面临的问题]]
- [[23-binary-tree-basic|二叉树的遍历（前序/中序/后序）]]

## 1. 核心思想：分治 + 前序 partition

### 1.1 思路来源：二叉树前序遍历

快速排序和 [[43-merge-sort|归并排序]] 都是分治，但「**工作发生的位置**」不同：

```text
对 nums[lo..hi] 排序：
1. 选 pivot（基准元素）
2. partition：把 nums[lo..hi] 分成三段
   - 左侧：< pivot
   - 中间：== pivot
   - 右侧：> pivot
3. 此时 pivot 已经位于最终正确位置（前序位置！）
4. 递归排序左侧、右侧
```

整棵递归树仍然是一棵二叉树（虽然不一定平衡），每个节点代表 `sort(nums, lo, hi)`。**真正的「排序动作」（partition）发生在前序位置**——这与归并排序的「后序 merge」形成对比。

### 1.2 递归树图示

```text
              sort(0,7)  pivot=4，partition 后 4 已就位
             /          \
       sort(0,3)        sort(5,7)  ← pivot 各自就位
       /     \             /    \
   sort(0,1) sort(2,3) sort(5,5) sort(6,7)
   ...
```

每个节点处理完 partition 后，**该 pivot 元素的位置就固定了**（不会在后续递归中移动）。

### 1.3 与 [[43-merge-sort|归并]] 的对比

| 维度 | 快速排序（前序） | 归并排序（后序） |
|------|-----------------|-----------------|
| 工作位置 | 前序（partition） | 后序（merge） |
| 子问题状态 | **pivot 已确定**，其余待排 | 两侧都已排序 |
| 递归树 | **可能不平衡** | 完全平衡 |
| 时间复杂度 | 平均 O(N log N)，**最坏 O(N²)** | 始终 O(N log N) |
| 稳定性 | ❌ | ✅ |
| 原地性 | ✅ | ❌ |
| 适用 | 通用、大数据 | 需要稳定 |

## 2. 单向扫描 partition（基础版）

### 2.1 思路

把 nums[lo..hi] 划分为 `[已排序 < pivot][待扫描][已排序 >= pivot]`：

```text
[lo ........ p ........ i .......... hi]
 ├─ < pivot ┤  ├─ 未扫描 ┤  ├─ >= pivot ┤
```

- 维护指针 `i` 表示已处理区间的右端点
- 维护指针 `p` 表示「< pivot 区间」的右端点（最初 = lo）
- 遍历 `i` 从 lo+1 到 hi：
  - 如果 `nums[i] < pivot`：交换 nums[p+1] 和 nums[i]，p++
  - 否则：继续
- 最后交换 nums[lo] 和 nums[p]，pivot 落位

### 2.2 代码


> [!info] 📌 付费章节补全内容（基于算法知识体系补充）

```cpp
#include <bits/stdc++.h>
using namespace std;

namespace dsa {

// 单向扫描 partition
// 返回 pivot 落位后的下标
int partition(vector<int>& nums, int lo, int hi) {
    int pivot = nums[lo];  // 选第一个元素为 pivot
    int p = lo;            // p 是「< pivot 区间」的右端点
    for (int i = lo + 1; i <= hi; i++) {
        if (nums[i] < pivot) {
            p++;
            swap(nums[p], nums[i]);
        }
    }
    // 把 pivot 放到最终位置 p
    swap(nums[lo], nums[p]);
    return p;
}

// 快速排序主函数（基础版）
void quickSort(vector<int>& nums, int lo, int hi) {
    if (lo >= hi) return;
    int p = partition(nums, lo, hi);
    quickSort(nums, lo, p - 1);
    quickSort(nums, p + 1, hi);
}

void sort(vector<int>& nums) {
    quickSort(nums, 0, nums.size() - 1);
}

} // namespace dsa
```

### 2.3 可视化示例

```text
nums = [3, 1, 4, 1, 5, 9, 2, 6], pivot = 3

i=1: nums[1]=1 < 3 → p=1, swap(1,1) → [3, 1, 4, 1, 5, 9, 2, 6]
                              < pivot = [1]
i=2: nums[2]=4 ≥ 3 → skip
i=3: nums[3]=1 < 3 → p=2, swap(2,3) → [3, 1, 1, 4, 5, 9, 2, 6]
                              < pivot = [1, 1]
i=4: nums[4]=5 ≥ 3 → skip
i=5: nums[5]=9 ≥ 3 → skip
i=6: nums[6]=2 < 3 → p=3, swap(3,6) → [3, 1, 1, 2, 5, 9, 4, 6]
                              < pivot = [1, 1, 2]
i=7: nums[7]=6 ≥ 3 → skip

最终 swap(0, 3)：pivot=3 落到下标 3
[1, 1, 2, 3, 5, 9, 4, 6]
              ↑ pivot 落位

后续递归：sort([1,1,2])、sort([5,9,4,6])
```

## 3. 双向扫描 partition（更高效）

### 3.1 思路

维护两个指针 `i`、`j` 分别从左右往中间扫描：

```text
nums[lo] 是 pivot
i 从 lo+1 向右找 ≥ pivot 的元素
j 从 hi 向左找 ≤ pivot 的元素
找到后交换 nums[i] 和 nums[j]
i >= j 时停止
最后交换 nums[lo] 和 nums[j]，j 是 pivot 的最终位置
```

### 3.2 代码

```cpp
namespace dsa {

// 双向扫描 partition（更常用、更快）
int partition2(vector<int>& nums, int lo, int hi) {
    int pivot = nums[lo];
    int i = lo + 1, j = hi;
    while (i <= j) {
        // i 向右找 >= pivot 的元素
        while (i <= j && nums[i] < pivot) i++;
        // j 向左找 <= pivot 的元素
        while (i <= j && nums[j] > pivot) j--;
        if (i >= j) break;
        swap(nums[i], nums[j]);
        i++;
        j--;
    }
    // pivot 落到 j
    swap(nums[lo], nums[j]);
    return j;
}

} // namespace dsa
```

### 3.3 与单向扫描对比

| 维度 | 单向扫描 | 双向扫描 |
|------|---------|---------|
| 交换次数 | 较多 | **更少** |
| 适用场景 | 一般 | **大量重复元素时尤其高效** |
| 代码复杂度 | 简单 | 略复杂 |

## 4. 三路快排：处理大量重复元素

### 4.1 问题

当数组中存在大量重复元素时，普通快排会把它们分到左右两侧，**递归深度变成 O(N)**，性能退化。

### 4.2 三路 partition 思路

把数组划分为三段：

```text
[< pivot][== pivot][> pivot][未处理]
```

- 维护指针 `lt`：`< pivot` 区间的右端点 + 1
- 维护指针 `gt`：`> pivot` 区间的左端点 - 1
- 维护指针 `i`：当前考察的元素下标
- 遍历 `i`，把等于 pivot 的元素聚拢到中间

### 4.3 代码

```cpp
namespace dsa {

// 三路快排 partition
// 划分后：[lo, lt) < pivot，[lt, i) == pivot，(gt, hi] > pivot
void partition3(vector<int>& nums, int lo, int hi, int& lt, int& gt) {
    int pivot = nums[lo];
    lt = lo;       // [lo, lt) < pivot
    gt = hi + 1;   // (gt, hi] > pivot
    int i = lo + 1;
    while (i < gt) {
        if (nums[i] < pivot) {
            swap(nums[i], nums[lt + 1]);
            lt++;
            i++;
        } else if (nums[i] > pivot) {
            swap(nums[i], nums[gt - 1]);
            gt--;
        } else {
            // nums[i] == pivot
            i++;
        }
    }
}

// 三路快排主函数
void quickSort3(vector<int>& nums, int lo, int hi) {
    if (lo >= hi) return;
    int lt, gt;
    partition3(nums, lo, hi, lt, gt);
    // 中间 [lt, gt) 全是等于 pivot 的，已经有序
    quickSort3(nums, lo, lt - 1);
    quickSort3(nums, gt, hi);
}

void sort3(vector<int>& nums) {
    quickSort3(nums, 0, nums.size() - 1);
}

} // namespace dsa
```

### 4.4 三路快排的优势

当数组中 **重复元素很多**（比如 `[1,1,1,...,1]`）时：

- 普通快排：每次 partition 都把数组分成 `[] + [N-1]`，递归深度 O(N)，时间 O(N²)
- 三路快排：一次 partition 把所有 1 都归到中间，递归深度 O(1)，时间 O(N)

## 5. 随机化优化：避免最坏情况

### 5.1 最坏情况分析

快排的最坏情况是每次 partition 都把数组分成 `[0] + [N-1]` 或 `[N-1] + [0]`：

```text
完全有序数组 [1,2,3,4,5]
选 nums[0]=1 为 pivot → partition 后变成 [] + [2,3,4,5]
选 nums[0]=2 为 pivot → partition 后变成 [] + [3,4,5]
...
递归深度 = N, 总时间 = O(N²)
```

### 5.2 解决方案：随机选 pivot

每次 **随机选一个元素作为 pivot**，再交换到 nums[lo]，然后正常 partition。

```cpp
#include <random>

namespace dsa {

// 随机化快排：避免最坏情况
int randomPartition(vector<int>& nums, int lo, int hi) {
    // 随机选一个下标
    int randomIdx = lo + rand() % (hi - lo + 1);
    swap(nums[lo], nums[randomIdx]);
    return partition2(nums, lo, hi);
}

void quickSortRandom(vector<int>& nums, int lo, int hi) {
    if (lo >= hi) return;
    int p = randomPartition(nums, lo, hi);
    quickSortRandom(nums, lo, p - 1);
    quickSortRandom(nums, p + 1, hi);
}

void sortRandom(vector<int>& nums) {
    srand(time(nullptr));
    quickSortRandom(nums, 0, nums.size() - 1);
}

} // namespace dsa
```

> [!tip] C++ 17 推荐用 `<random>`
> 现代 C++ 推荐 `std::mt19937` 替代 `rand()`，避免分布不均：
> ```cpp
> std::random_device rd;
> std::mt19937 gen(rd());
> std::uniform_int_distribution<> dis(lo, hi);
> int randomIdx = dis(gen);
> ```

### 5.3 期望时间复杂度

随机选 pivot 后，**最坏 O(N²) 的概率极低**，期望时间复杂度仍是 **O(N log N)**。这是快排成为「通用排序首选」的关键。

## 6. 完整版：随机化 + 三路快排

```cpp
namespace dsa {

class QuickSort {
public:
    void sort(vector<int>& nums) {
        srand(time(nullptr));
        quickSort(nums, 0, nums.size() - 1);
    }

private:
    void quickSort(vector<int>& nums, int lo, int hi) {
        if (lo >= hi) return;

        // 1. 随机化 pivot
        int randomIdx = lo + rand() % (hi - lo + 1);
        swap(nums[lo], nums[randomIdx]);

        // 2. 三路 partition
        int pivot = nums[lo];
        int lt = lo, gt = hi + 1, i = lo + 1;
        while (i < gt) {
            if (nums[i] < pivot) {
                swap(nums[i], nums[lt + 1]);
                lt++;
                i++;
            } else if (nums[i] > pivot) {
                swap(nums[i], nums[gt - 1]);
                gt--;
            } else {
                i++;
            }
        }
        swap(nums[lo], nums[lt]);
        lt--;  // pivot 落位，lt 是 < pivot 的右端点

        // 3. 递归
        quickSort(nums, lo, lt);
        quickSort(nums, gt, hi);
    }
};

} // namespace dsa
```

## 7. 复杂度表

| 指标 | 值 |
|------|---|
| 最好时间 | O(N log N) |
| 平均时间 | O(N log N) |
| 最坏时间 | O(N²)（已排序 + 不随机化） |
| 期望时间 | O(N log N)（**随机化后**） |
| 空间复杂度 | O(log N)（递归栈） |
| 稳定性 | ❌ 不稳定 |
| 原地性 | ✅ 原地 |

## 8. 为什么不稳定？

```text
[2a, 1, 2b]

第一次 partition，pivot = 2a
1 < 2a → 交换到左侧
最后把 2a 落位

结果可能是 [1, 2a, 2b] 或 [1, 2b, 2a]
            ↑                 ↑
        2a, 2b 的相对顺序被改变
```

## 9. 适用场景

1. **通用、大数据量排序**：首选快排（平均最优）
2. **内存敏感场景**：快排原地，O(log N) 栈
3. **STL std::sort 的核心**：GCC 的 `std::sort` 是 **introsort**（快排 + 堆排 + 插入排序混合），主体是快排
4. **不适用于**：
   - 需要稳定排序时（用 [[43-merge-sort|归并]]）
   - 数据几乎有序且不能随机化（用堆排）

## 10. 经典 LeetCode 题

### 10.1 LeetCode 912：排序数组

直接使用上面的 `QuickSort` 类即可通过：

```cpp
class Solution {
public:
    vector<int> sortArray(vector<int>& nums) {
        dsa::QuickSort sorter;
        sorter.sort(nums);
        return nums;
    }
};
```

> [!warning] 关键点
> LeetCode 912 的测试用例中包含 **大量重复元素**（来自真实工程场景），**三路快排** 是最优选择。如果用基础快排会接近 O(N²)，可能超时。

### 10.2 LeetCode 215：数组中的第 K 个最大元素

可以用快排的 partition 思想 **O(N) 时间** 求第 K 大元素：

```cpp
class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        // 第 K 大等价于第 N-K 小
        int target = nums.size() - k;
        return quickSelect(nums, 0, nums.size() - 1, target);
    }

private:
    int quickSelect(vector<int>& nums, int lo, int hi, int target) {
        int p = dsa::partition2(nums, lo, hi);
        if (p == target) return nums[p];
        if (p > target) return quickSelect(nums, lo, p - 1, target);
        return quickSelect(nums, p + 1, hi, target);
    }
};
```

**期望时间复杂度 O(N)**，比 [[45-heap-sort|堆排]] 的 O(N log K) 更优。

## 下一章

→ [[45-heap-sort|堆排序]]：利用二叉堆实现原地 O(N log N) 排序，避免快排的最坏 O(N²)。

## 相关章节

- [[43-merge-sort|归并排序]] — 后序位置的另一种分治排序
- [[42-select-sort|选择排序]] — 快排的优化起点
- [[45-heap-sort|堆排序]] — 解决快排最坏情况的备选
- [[21-binary-heap-basic|二叉堆基础]] — 堆排的前置
- [[22-binary-heap-implement|优先级队列]]
- LeetCode [[#912|912. 排序数组]]
- LeetCode [[#215|215. 数组中的第 K 个最大元素]]

## 练习题

| 难度 | 题号 | 题目 |
|------|------|------|
| 中 | 912 | 排序数组 |
| 中 | 215 | 数组中的第 K 个最大元素 |
| 中 | 75 | 颜色分类（三路快排思想） |