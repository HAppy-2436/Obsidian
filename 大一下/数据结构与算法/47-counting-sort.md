---
title: 全新的排序原理：计数排序
tags: [排序, 数据结构, 线性]
order: 47
prerequisites:
  - "[[39-sort-basic]]"
group: 排序
paywall: false
source: https://labuladong.online/zh/algo/data-structure-basic/counting-sort/
---

# 全新的排序原理：计数排序

> 一句话总结：全新的排序原理：计数排序 是 排序 模块的核心知识点。

## 学习目标

读完本文，你应该能：
- 理解 全新的排序原理：计数排序 的核心原理
- 用 C++ 实现该数据结构/算法
- 掌握时间/空间复杂度分析
- 知道典型的应用场景

## 前置知识

阅读本文前，建议先学习：

- [[39-sort-basic]]

## 计数排序原理

计数排序（Counting Sort）是一种**非比较**的排序算法，时间复杂度 O(N+K)，其中 N 是数组长度，K 是数值范围。

### 核心思想
1. 统计每个值出现的次数（count 数组）
2. 根据 count 数组的前缀和，确定每个元素的最终位置
3. 将元素放到正确位置（从后往前遍历以保证稳定性）

### 适用场景
- 数据范围不大（K 不太大）
- 需要稳定排序
- 比如：年龄排序、考试成绩排序、字符计数等

## 完整 C++ 实现

```cpp
#include <bits/stdc++.h>
using namespace std;

namespace dsa {

// 朴素版计数排序（不要求稳定，O(N+K)）
vector<int> countingSort(vector<int>& nums, int maxVal) {
    vector<int> count(maxVal + 1, 0);
    for (int x : nums) count[x]++;

    vector<int> result;
    for (int v = 0; v <= maxVal; v++) {
        for (int i = 0; i < count[v]; i++) {
            result.push_back(v);
        }
    }
    return result;
}

// 稳定版计数排序（O(N+K)）
vector<int> countingSortStable(vector<int>& nums, int maxVal) {
    int n = nums.size();
    vector<int> count(maxVal + 1, 0);
    for (int x : nums) count[x]++;

    // 前缀和：count[v] 表示 ≤ v 的元素个数
    for (int v = 1; v <= maxVal; v++) {
        count[v] += count[v - 1];
    }

    // 从后往前遍历，保证稳定性
    vector<int> result(n);
    for (int i = n - 1; i >= 0; i--) {
        result[count[nums[i]] - 1] = nums[i];
        count[nums[i]]--;
    }
    return result;
}

} // namespace dsa

int main() {
    vector<int> a = {2, 5, 3, 0, 2, 3, 0, 3};
    auto sorted = dsa::countingSortStable(a, 5);
    for (int x : sorted) cout << x << ' ';
    cout << endl;
    return 0;
}
```

## 复杂度分析

| 项目 | 复杂度 |
|------|--------|
| 时间复杂度 | O(N + K) |
| 空间复杂度 | O(N + K) |
| 稳定性 | **稳定**（前缀和 + 倒序遍历）|

### 与比较排序的对比
- 计数排序跳过了"比较"操作，理论下界不再是 O(N log N)
- 代价是需要 O(K) 的额外空间
- 当 K << N log N 时，计数排序明显更快

## 应用场景

- 排序 0-100 的考试成绩
- 对字符做计数（仅 26 个英文字母）
- 基数排序的子过程（按某一位排序时使用计数排序）

## 局限性

1. **只能排整数**：依赖 count 数组下标
2. **数据范围不能太大**：K = max - min，太大内存爆炸
3. **不适用于浮点数、字符串**：需要先转换

## LeetCode 经典题

- [912. Sort an Array](https://leetcode.com/problems/sort-an-array/) - 数据范围 -50000 ~ 50000，可以用计数排序
- [75. Sort Colors](https://leetcode.com/problems/sort-colors/) - 颜色排序（0/1/2 三色），本质是计数排序

## 下一章
继续学习 [[48-bucket-sort|桶排序]]


## 相关章节

- 同分组：排序
- 前置：[[39-sort-basic]]
- 下一章：[[48-bucket-sort]]

## 下一章

继续学习 [[48-bucket-sort]]
