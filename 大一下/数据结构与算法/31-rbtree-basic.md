---
title: 红黑树的自平衡原理及可视化
tags: [labuladong, 高级树, 数据结构与算法, 付费章节]
order: 31
prerequisites: [27-tree-map-basic]
group: 高级树
paywall: true
source: labuladong.online
url: https://labuladong.online/zh/algo/data-structure-basic/rbtree-basic/
---

# 红黑树的自平衡原理及可视化

前置知识

阅读本文前，你需要先学习：

二叉树基础及常见类型

多叉树的递归/层序遍历

二叉搜索树的应用及可视化

一句话总结

红黑树是自平衡的二叉搜索树，它的树高在任何时候都能保持在
𝑂
(
log
⁡
𝑁
)
O(logN)（完美平衡），这样就能保证增删查改的时间复杂度都是
𝑂
(
log
⁡
𝑁
)
O(logN)。

可视化面板支持创建红黑树：

算法可视化

二叉搜索树的应用及可视化
 讲了普通的二叉搜索树存储键值对实现 TreeMap/TreeSet 的思路。

二叉搜索树的操作效率取决于树高，树结构越平衡，树高就接近
log
⁡
𝑁
logN，增删查改的效率就比较高。而普通二叉搜索树最关键的问题是它不会自动对树进行平衡，特殊的情况下会退化成链表，增删查改的时间复杂度退化为
𝑂
(
𝑁
)
O(N)。

下面这个可视化面板就是一个例子，如果插入若干个有序的键值对，你就能发现每次新增的键都会被插入到最右侧，导致这棵二叉搜索树退化成了链表：

了解会员权益

更新时间：2026/06/12 00:27

> [!warning] 付费章节
> 本章内容为 labuladong.online 付费会员内容。本笔记仅保留公开部分 + C++ 代码片段的整理（由 agent 自动从 C++ tab 提取）。完整讲解请见 [原网页](https://labuladong.online/zh/algo/data-structure-basic/rbtree-basic/)。


## 关联章节

- [[27-tree-map-basic|二叉搜索树原理及应用技巧]]
