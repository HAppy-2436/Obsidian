---
title: 堆排序/优先级队列的代码实现
tags: [labuladong, 二叉堆, 数据结构与算法, 付费章节]
order: 22
prerequisites: [21-binary-heap-basic]
group: 二叉堆
paywall: true
source: labuladong.online
url: https://labuladong.online/zh/algo/data-structure-basic/binary-heap-implement/
---

前置知识

阅读本文前，你需要先学习：

二叉堆的原理

前文
二叉堆的原理
 介绍了二叉堆的基本性质、API 和常见应用。本文将结合
可视化面板
 手把手带你实现一个优先级队列。

我们先实现一个简化版的优先级队列，用来帮你理解二叉堆的核心操作 sink 和 swim。最后我再用给出一个比较完整的代码实现。

了解会员权益


> [!warning] 付费章节
> 本章内容为 labuladong.online 付费会员内容。本笔记仅保留公开部分 + C++ 代码片段的整理（由 agent 自动从 C++ tab 提取）。完整讲解请见 [原网页](https://labuladong.online/zh/algo/data-structure-basic/binary-heap-implement/)。


## 关联章节

- [[21-binary-heap-basic|二叉堆核心原理及可视化]]
