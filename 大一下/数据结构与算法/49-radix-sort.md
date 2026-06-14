---
title: 基数排序（Radix Sort）
tags: [排序, 数据结构, 线性]
order: 49
prerequisites:
  - "[[47-counting-sort]]"
  - "[[48-bucket-sort]]"
group: 排序
paywall: false
source: https://labuladong.online/zh/algo/data-structure-basic/radix-sort/
---

# 基数排序（Radix Sort）

> 一句话总结：基数排序（Radix Sort） 是 排序 模块的核心知识点。

## 学习目标

读完本文，你应该能：
- 理解 基数排序（Radix Sort） 的核心原理
- 用 C++ 实现该数据结构/算法
- 掌握时间/空间复杂度分析
- 知道典型的应用场景

## 前置知识

阅读本文前，建议先学习：

- [[47-counting-sort]]
- [[48-bucket-sort]]

## 基数排序原理

基数排序（Radix Sort）按数字的每一位进行排序，从低位到高位（或反过来），每轮用稳定的子排序（通常是计数排序）。

### 核心思想
1. 找出最大值，确定最大位数 D
2. 从低位（个位）到高位（十位、百位...），依次做稳定排序
3. 第 D 轮排序完成后，数组就有序了

### 为什么低位优先能保证正确？
每轮排序都是**稳定**的，所以高位排序时，相等元素的相对顺序由低位决定，整体就排好序了。

### 关键性质
- **稳定**：每轮必须用稳定排序（计数排序）
- **原地？否**：需要 O(N+K) 额外空间
- **时间复杂度 O(D(N+K))**：D 是位数

## 完整 C++ 实现

```cpp
#include <bits/stdc++.h>
using namespace std;

namespace dsa {

// 基数排序（最低位优先 LSD）
void radixSort(vector<int>& nums) {
    if (nums.empty()) return;

    // 1. 找最大值，确定位数
    int maxVal = *max_element(nums.begin(), nums.end());
    int n = nums.size();

    // 2. 从低位到高位，每轮用计数排序
    // exp = 1 表示个位，= 10 表示十位，= 100 表示百位 ...
    for (int exp = 1; maxVal / exp > 0; exp *= 10) {
        // 计数排序数组：0-9 共 10 个桶
        vector<int> count(10, 0);
        vector<int> output(n);

        // 统计当前位的出现次数
        for (int x : nums) {
            count[(x / exp) % 10]++;
        }

        // 前缀和
        for (int i = 1; i < 10; i++) {
            count[i] += count[i - 1];
        }

        // 从后往前遍历，保证稳定性
        for (int i = n - 1; i >= 0; i--) {
            int digit = (nums[i] / exp) % 10;
            output[count[digit] - 1] = nums[i];
            count[digit]--;
        }

        nums = output;
    }
}

// 处理负数的版本
void radixSortSigned(vector<int>& nums) {
    if (nums.empty()) return;

    // 分离正负数
    vector<int> negatives, positives;
    for (int x : nums) {
        if (x < 0) negatives.push_back(-x);
        else positives.push_back(x);
    }

    radixSort(negatives);
    radixSort(positives);

    // 合并（负数反转 + 正数）
    int i = 0;
    // 负数从大到小（-1 < -10，所以负数越大排越前）
    for (int j = negatives.size() - 1; j >= 0; j--) {
        nums[i++] = -negatives[j];
    }
    for (int x : positives) {
        nums[i++] = x;
    }
}

} // namespace dsa

int main() {
    vector<int> a = {170, 45, 75, 90, 802, 24, 2, 66};
    dsa::radixSort(a);
    for (int x : a) cout << x << ' ';
    cout << endl;
    return 0;
}
```

## 复杂度分析

| 项目 | 复杂度 |
|------|--------|
| 时间复杂度 | O(D × (N + K))，D=位数，K=基数（通常 10）|
| 空间复杂度 | O(N + K) |
| 稳定性 | **稳定**（子排序用计数排序）|

### 位数 D 的影响
- 32 位 int：D ≤ 10
- 字符串长度 D：D = 长度
- D 很小的时候，基数排序非常快

## 应用场景

- 整数排序（特别是位数不多的情况）
- 字符串排序（按字符）
- 日期排序（按年月日）

## 局限性

1. **只适用于整数或可拆分为"位"的数据**（字符串、定长记录）
2. **负数处理较麻烦**：需要分离正负数或加偏移
3. **浮点数不能直接用**：要转成定点数

## 与其他线性排序对比

| 排序 | 时间复杂度 | 空间 | 稳定性 | 适用范围 |
|------|-----------|------|--------|---------|
| 计数排序 | O(N+K) | O(K) | 稳定 | 整数，K 较小 |
| 桶排序 | O(N+K) | O(N+K) | 稳定 | 均匀分布数据 |
| 基数排序 | O(D(N+K)) | O(N+K) | 稳定 | 整数、定长字符串 |

## LeetCode 经典题

- [164. Maximum Gap](https://leetcode.com/problems/maximum-gap/) - 桶排序/基数排序思想求最大间距
- [912. Sort an Array](https://leetcode.com/problems/sort-an-array/) - 可用基数排序解（数据范围有限）

## 下一章
继续学习 [[50-huffman-tree|赫夫曼编码]]


## 相关章节

- 同分组：排序
- 前置：[[47-counting-sort]]
- 下一章：[[50-huffman-tree]]

## 下一章

继续学习 [[50-huffman-tree]]
