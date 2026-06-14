---
title: 利用前序位置：快速排序
tags: [labuladong, 排序, 分治, 数据结构与算法, 付费章节]
order: 44
prerequisites: [24-binary-tree-traverse-basic, 43-merge-sort]
group: 排序 / 分治
paywall: true
source: labuladong.online
url: https://labuladong.online/zh/algo/data-structure-basic/quick-sort/
---

前置知识

阅读本文前，你需要先学习：

选择排序所面临的问题

二叉树的遍历

一句话总结

快速排序的核心思路需要结合
二叉树的前序遍历
 来理解：在二叉树遍历的前序位置将一个元素排好位置，然后递归地将剩下的元素排好位置。

你可以点开这个可视化面板，点击全屏按钮 ，然后多次点击 let p = partition(nums, lo, hi) 这部分代码，即可直观地看到快排的递归过程和排序效果：

算法可视化

上来这一句总结是不是就把初学者听懵了？数组排序算法怎么扯到二叉树上了？

所以说，计算机思维和人类思维是不一样的。

正常人要排序数组，一般就是维护一个 sortedIndex，保持 [0, sortedIndex) 有序，逐步右移 sortedIndex，直到整个数组有序。这中间历经种种坎坷，逢山开路遇水搭桥，正如我们前面讲的
选择排序
、
冒泡排序
、
插入排序
、
希尔排序
。

但是越是效率高的算法，离计算机思维越近，未经训练的人就越难理解。学过前面几种基础排序算法，现在你应该可以感觉到这一点了，容易理解和推导的排序算法复杂度全都是
O(N2)，而突破
O(N2) 的排序算法，都感觉不是人类能想出来的。

哪个人要是张嘴就说：排序数组简单啊，只要把一个元素排好序，然后把剩下元素排好序，就能把整个数组排好序了。那只能说这个人可能是三体人潜伏在地球的特务：）

了解会员权益


> [!warning] 付费章节
> 本章内容为 labuladong.online 付费会员内容。本笔记仅保留公开部分 + C++ 代码片段的整理（由 agent 自动从 C++ tab 提取）。完整讲解请见 [原网页](https://labuladong.online/zh/algo/data-structure-basic/quick-sort/)。


## 关联章节

- [[24-binary-tree-traverse-basic|二叉树的递归/层序遍历]]
- [[43-merge-sort|利用后序位置：归并排序]]
