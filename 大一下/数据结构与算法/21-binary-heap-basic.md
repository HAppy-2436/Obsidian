---
title: 二叉堆核心原理及可视化
tags: [labuladong, 二叉堆, 数据结构与算法, 付费章节]
order: 21
prerequisites: [02-array-basic]
group: 二叉堆
paywall: true
source: labuladong.online
url: https://labuladong.online/zh/algo/data-structure-basic/binary-heap-basic/
---

# 二叉堆核心原理及可视化

前置知识

阅读本文前，你需要先学习：

二叉树基础及常见类型

二叉树的递归/层序遍历

一句话总结

二叉堆是一种能够动态排序的数据结构，是
二叉树结构
 的延伸。

二叉堆的主要操作就两个，sink（下沉）和 swim（上浮），用以维护二叉堆的性质。

二叉堆的主要应用有两个，首先是一种很有用的数据结构优先级队列（Priority Queue），第二是一种排序方法堆排序（Heap Sort）。

这个可视化面板直观地展示了二叉堆的基本操作，你可以点击跳转执行其中的代码，或自己修改代码玩一玩：

算法可视化

下面我就结合可视化面板来展示二叉堆的原理，最后以优先级队列为例，展示二叉堆的代码实现。

了解会员权益

更新时间：2026/06/12 00:27

> [!warning] 付费章节
> 本章内容为 labuladong.online 付费会员内容。本笔记仅保留公开部分 + C++ 代码片段的整理（由 agent 自动从 C++ tab 提取）。完整讲解请见 [原网页](https://labuladong.online/zh/algo/data-structure-basic/binary-heap-basic/)。


## 关联章节

- [[02-array-basic|数组（顺序存储）的原理]]
