---
title: 图结构的通用代码实现
tags: [labuladong, 图, 实现, 数据结构与算法, 付费章节]
order: 33
prerequisites: [32-graph-terminology]
group: 图 / 实现
paywall: true
source: labuladong.online
url: https://labuladong.online/zh/algo/data-structure-basic/graph-basic/
---

# 图结构的通用代码实现

前置知识

阅读本文前，你需要先学习：

多叉树的递归/层序遍历

一句话总结

图结构就是
多叉树结构
 的延伸。图结构逻辑上由若干节点（Vertex）和边（Edge）构成，我们一般用邻接表、邻接矩阵等方式来存储图。

在树结构中，只允许父节点指向子节点，不存在子节点指向父节点的情况，子节点之间也不会互相链接；而图中没有那么多限制，节点之间可以相互指向，形成复杂的网络结构。

可视化面板
 支持创建图结构，你可以打开下面的可视化面板，即可看到图的逻辑结构，以及邻接表和邻接矩阵的存储方式：

算法可视化

图结构可以对很多复杂的问题进行抽象，产生了很多经典的图论算法，比如
二分图算法
、
拓扑排序
、
最短路径算法
、
最小生成树算法
 等，这些都会在后文介绍。

本文主要介绍图的基本概念，以及如何用代码实现图结构。

了解会员权益

更新时间：2026/06/12 00:27

> [!warning] 付费章节
> 本章内容为 labuladong.online 付费会员内容。本笔记仅保留公开部分 + C++ 代码片段的整理（由 agent 自动从 C++ tab 提取）。完整讲解请见 [原网页](https://labuladong.online/zh/algo/data-structure-basic/graph-basic/)。


## 关联章节

- [[32-graph-terminology|图的基本术语]]
