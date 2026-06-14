---
title: 线性探查法的两种代码实现
tags: [labuladong, 哈希表, 开放定址, 数据结构与算法, 付费章节]
order: 15
prerequisites: [14-linear-probing-key-point]
group: 哈希表 / 开放定址
paywall: true
source: labuladong.online
url: https://labuladong.online/zh/algo/data-structure-basic/linear-probing-code/
---

前置知识

阅读本文前，你需要先学习：

线性探查法的两个难点

前文
哈希表核心原理
 中我介绍了哈希表的核心原理和几个关键概念，
拉链法原理和实现
 中介绍了拉链法的实现，
线性探查法的两个难点
 介绍了线性探查法实现哈希表的难点所在，并给出了两种方法解决删除元素时的空洞问题，本文会同时给出这两种方法的参考代码实现。

本文会先结合可视化面板给出简化的实现，方便大家理解增删查改的过程，最后给完整实现。

简化实现中，具体简化的地方如下：

1、我们实现的哈希表只支持 key 类型为 int，value 类型为 int 的情况，如果 key 不存在，就返回 -1。

2、我们实现的 hash 函数就是简单地取模，即 hash(key) = key % table.length。这样也方便模拟出哈希冲突的情况，比如当 table.length = 10 时，hash(1) 和 hash(11) 的值都是 1。

3、底层的 table 数组的大小在创建哈希表时就固定，假设 table 数组不会被装满，不考虑负载因子和动态扩缩容的问题。

这些简化能够帮助我们聚焦增删查改的核心逻辑，并且可以借助
可视化面板
 辅助大家学习理解。

了解会员权益


> [!warning] 付费章节
> 本章内容为 labuladong.online 付费会员内容。本笔记仅保留公开部分 + C++ 代码片段的整理（由 agent 自动从 C++ tab 提取）。完整讲解请见 [原网页](https://labuladong.online/zh/algo/data-structure-basic/linear-probing-code/)。


## 关联章节

- [[14-linear-probing-key-point|线性探查法的两个难点]]
