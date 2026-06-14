---
title: 善用区间：桶排序
tags: [排序, 数据结构, 线性]
order: 48
prerequisites:
  - "[[47-counting-sort]]"
group: 排序
paywall: false
source: https://labuladong.online/zh/algo/data-structure-basic/bucket-sort/
---

# 善用区间：桶排序

> 一句话总结：善用区间：桶排序 是 排序 模块的核心知识点。

## 学习目标

读完本文，你应该能：
- 理解 善用区间：桶排序 的核心原理
- 用 C++ 实现该数据结构/算法
- 掌握时间/空间复杂度分析
- 知道典型的应用场景

## 前置知识

阅读本文前，建议先学习：

- [[47-counting-sort]]

## 桶排序原理

桶排序（Bucket Sort）把数据分散到有限数量的**桶**里，每个桶再单独排序（通常用插入排序或递归桶排序）。

### 核心思想
1. 设置 K 个桶，每个桶对应一个值区间
2. 把每个元素根据映射函数分配到对应桶
3. 对每个桶内部排序
4. 按桶顺序合并所有元素

### 与计数排序的关系
- 计数排序是桶排序的特殊情况：每个桶只装一个值（K = max - min）
- 桶排序允许每个桶装一段区间，更节省内存

## 完整 C++ 实现

```cpp
#include <bits/stdc++.h>
using namespace std;

namespace dsa {

// 桶排序：对 [0, 1) 范围的浮点数排序
vector<double> bucketSort(vector<double>& nums) {
    int n = nums.size();
    if (n == 0) return nums;

    // 1. 创建 K 个桶
    int K = n; // 桶数量 = 元素数量（经验值）
    vector<vector<double>> buckets(K);

    // 2. 分配元素到桶
    for (double x : nums) {
        int idx = (int)(x * K);
        buckets[idx].push_back(x);
    }

    // 3. 每个桶内排序（这里用 std::sort）
    for (auto& bucket : buckets) {
        sort(bucket.begin(), bucket.end());
    }

    // 4. 合并桶
    vector<double> result;
    for (auto& bucket : buckets) {
        for (double x : bucket) result.push_back(x);
    }
    return result;
}

// 桶排序：整数版本（指定数据范围）
vector<int> bucketSortInt(vector<int>& nums, int minVal, int maxVal) {
    int n = nums.size();
    if (n == 0) return nums;

    int K = n; // 桶数
    double range = (double)(maxVal - minVal + 1) / K;

    vector<vector<int>> buckets(K);
    for (int x : nums) {
        int idx = min((int)((x - minVal) / range), K - 1);
        buckets[idx].push_back(x);
    }

    for (auto& bucket : buckets) {
        sort(bucket.begin(), bucket.end());
    }

    vector<int> result;
    for (auto& bucket : buckets) {
        for (int x : bucket) result.push_back(x);
    }
    return result;
}

} // namespace dsa

int main() {
    vector<double> a = {0.42, 0.32, 0.23, 0.52, 0.25, 0.47, 0.51};
    auto sorted = dsa::bucketSort(a);
    for (double x : sorted) cout << x << ' ';
    cout << endl;
    return 0;
}
```

## 复杂度分析

| 项目 | 复杂度 |
|------|--------|
| 平均时间复杂度 | O(N + K) |
| 最坏时间复杂度 | O(N²)（所有元素进同一桶）|
| 空间复杂度 | O(N + K) |
| 稳定性 | **稳定**（桶内排序用稳定算法）|

### 何时达到 O(N + K)？
- 数据**均匀分布**时
- 桶数量 K ≈ N（经验最优）
- 每个桶内的元素数量接近常数

## 应用场景

- 浮点数排序
- 均匀分布的大数据
- 外部排序（数据太大装不进内存，可以分桶写入磁盘）

## 局限性

1. **要求数据均匀分布**：否则退化到 O(N²)
2. **需要预先知道数据范围**
3. **桶数量的选择**：太多浪费空间，太少桶内元素多

## LeetCode 经典题

- [912. Sort an Array](https://leetcode.com/problems/sort-an-array/) - 整数排序，可用桶排序
- [220. Contains Duplicate III](https://leetcode.com/problems/contains-duplicate-iii/) - 桶排序思想的变体（桶用于 O(1) 查找邻近元素）

## 下一章
继续学习 [[49-radix-sort|基数排序]]


## 相关章节

- 同分组：排序
- 前置：[[47-counting-sort]]
- 下一章：[[49-radix-sort]]

## 下一章

继续学习 [[49-radix-sort]]
