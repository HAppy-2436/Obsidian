---
title: 突破 O(N^2)：希尔排序
tags: [labuladong, 排序, 插入改进, 数据结构与算法, 付费章节]
order: 46
prerequisites: [41-insertion-sort]
group: 排序 / 插入改进
paywall: true
source: labuladong.online
url: https://labuladong.online/zh/algo/data-structure-basic/shell-sort/
---

# 突破 O(N^2)：希尔排序

读完本文，你不仅学会了算法套路，还可以顺便解决如下题目：

LeetCode

力扣

难度

912. Sort an Array

912. 排序数组

前置知识

阅读本文前，你需要先学习：

选择排序所面临的问题

运用逆向思维：插入排序

一句话总结

希尔排序是基于
插入排序
 的简单改进，通过预处理增加数组的局部有序性，突破了插入排序的
𝑂
(
𝑁
2
)
O(N
2
) 时间复杂度。

你可以点开可视化面板，点击播放按钮，然后点击加速/减速按钮调节速度，即可直观感受希尔排序的过程：

算法可视化

必须承认，希尔排序的思路很难想到，我是在《算法 4》第一次了解到这个算法，然后惊叹于这个算法的简单优化竟然能给插入排序带来如此大的提升。

首先我们要明确一个 h 有序数组 的概念。

## h 有序数组

一个数组是 h 有序的，是指这个数组中任意间隔为 h（或者说间隔元素的个数为 h-1）的元素都是有序的。

这个概念用文字不好描述清楚，直接看个例子吧。比方说 h=3 时，一个 3 有序数组是这样的：

了解会员权益

更新时间：2026/06/12 00:27

> [!warning] 付费章节
> 本章内容为 labuladong.online 付费会员内容。本笔记仅保留公开部分 + C++ 代码片段的整理（由 agent 自动从 C++ tab 提取）。完整讲解请见 [原网页](https://labuladong.online/zh/algo/data-structure-basic/shell-sort/)。


## 关联章节

- [[41-insertion-sort|插入排序的链表思维]]
