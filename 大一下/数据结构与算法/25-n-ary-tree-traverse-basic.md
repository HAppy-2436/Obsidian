---
title: N 叉树的递归/层序遍历
tags: [labuladong, 二叉树, 遍历, 数据结构与算法, 付费章节]
order: 25
prerequisites: [24-binary-tree-traverse-basic]
group: 二叉树 / 遍历
paywall: true
source: labuladong.online
url: https://labuladong.online/zh/algo/data-structure-basic/n-ary-tree-traverse-basic/
---

读完本文，你不仅学会了算法套路，还可以顺便解决如下题目：

LeetCode

力扣

难度

589. N-ary Tree Preorder Traversal

589. N 叉树的前序遍历

590. N-ary Tree Postorder Traversal

590. N 叉树的后序遍历

429. N-ary Tree Level Order Traversal

429. N 叉树的层序遍历

前置知识

阅读本文前，你需要先学习：

二叉树的递归/层序遍历

一句话总结

多叉树结构就是
二叉树结构
 的延伸，二叉树是特殊的多叉树。

多叉树的遍历就是
二叉树遍历
 的延伸。

森林是指多个多叉树的集合，单独一棵多叉树是一个特殊的森林。

二叉树的节点长这样，每个节点有两个子节点：

```cpp
class TreeNode {
public:
    int val;
    TreeNode* left;
    TreeNode* right;

    TreeNode(int v) : val(v), left(nullptr), right(nullptr) {}
};
```

多叉树的节点长这样，每个节点有任意个子节点：

```cpp
class Node {
public:
    int val;
    vector<Node*> children;
};
```

就这点区别，其他没了。

## 森林

这里介绍一下「森林」这个名词，后面讲到
Union Find 并查集算法
 时，会用到这个概念。

顾名思义，森林就是多个多叉树的集合（单独一棵多叉树也是一个特殊的森林），用代码表示就是多个多叉树的根节点列表，类似这样：

```
List<Node> forest;
```

只需对每个根节点分别进行 DFS/BFS 遍历，即可遍历森林的所有节点。

在并查集算法中，我们会同时持有多棵多叉树的根节点，那么这些根节点的集合就是一个森林。

接下来说下多叉树的遍历，和二叉树一样，也就递归遍历（DFS）和层序遍历（BFS）两种。

## 递归遍历（DFS）

对比二叉树的遍历框架看多叉树的遍历框架吧：

了解会员权益


> [!warning] 付费章节
> 本章内容为 labuladong.online 付费会员内容。本笔记仅保留公开部分 + C++ 代码片段的整理（由 agent 自动从 C++ tab 提取）。完整讲解请见 [原网页](https://labuladong.online/zh/algo/data-structure-basic/n-ary-tree-traverse-basic/)。


## 关联章节

- [[24-binary-tree-traverse-basic|二叉树的递归/层序遍历]]
