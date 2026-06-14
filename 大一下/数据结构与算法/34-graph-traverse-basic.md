---
title: 图结构的 DFS/BFS 遍历
tags: [labuladong, 图, 遍历, 数据结构与算法, 付费章节]
order: 34
prerequisites: [33-graph-basic, 24-binary-tree-traverse-basic]
group: 图 / 遍历
paywall: true
source: labuladong.online
url: https://labuladong.online/zh/algo/data-structure-basic/graph-traverse-basic/
---

# 图结构的 DFS/BFS 遍历

前置知识

阅读本文前，你需要先学习：

图结构基础及通用代码实现

多叉树的递归/层序遍历

一句话总结

图的遍历就是
多叉树遍历
 的延伸，主要遍历方式还是深度优先搜索（DFS）和广度优先搜索（BFS）。

唯一的区别是，树结构中不存在环，而图结构中可能存在环，所以我们需要标记遍历过的节点，避免遍历函数在环中死循环。

由于图结构的复杂性，可以细分为遍历图的「节点」、「边」和「路径」三种场景，每种场景的代码实现略有不同。

遍历图的「节点」和「边」时，需要 visited 数组在前序位置做标记，避免重复遍历；遍历图的「路径」时，需要 onPath 数组在前序位置标记节点，在后序位置撤销标记。

可视化面板
 支持创建图结构，同时支持可视化 DFS/BFS 遍历的路径。你可以直观地看到，图结构看起来虽然比树结构复杂，但图的遍历本质上还是树的遍历。

先看 DFS 算法，你可以打开下面的可视化面板，多次点击 console.log 这行代码，即可看到 DFS 遍历图的过程，traverse 函数本质上在遍历一棵多叉递归树：

算法可视化

再看 BFS 算法，你可以打开下面的可视化面板，多次点击 console.log 这行代码，即可看到 BFS 遍历图的过程，本质上是在层序遍历一棵多叉树：

算法可视化

下面具体讲解。

## 深度优先搜索（DFS）

前文
图结构基础和通用实现
 中说了，我们一般不用 Vertex 这样的类来存储图，但是这里我还是先用一下这个类，以便大家把图的遍历和多叉树的遍历做对比。后面我会给出基于邻接表/邻接矩阵的遍历代码。

### 遍历所有节点（visited 数组）

对比多叉树的遍历框架看图的遍历框架吧：

```cpp
// 多叉树节点
class Node {
public:
    int val;
    vector<Node*> children;
};

// 多叉树的遍历框架
void traverse(Node* root) {
    // base case
    if (root == nullptr) {
        return;
    }
    // 前序位置
    cout << "visit " << root->val << endl;
    for (auto child : root->children) {
        traverse(child);
    }
    // 后序位置
}

// 图节点
class Vertex {
public:
    int id;
    vector<Vertex*> neighbors;
};

// 图的遍历框架
// 需要一个 visited 数组记录被遍历过的节点
// 避免走回头路陷入死循环
void traverse(Vertex* s, vector<bool>& visited) {
    // base case
    if (s == nullptr) {
        return;
    }
    if (visited[s->id]) {
        // 防止死循环
        return;
    }
    // 前序位置
    visited[s->id] = true;
    cout << "visit " << s->id << endl;
    for (auto neighbor : s->neighbors) {
        traverse(neighbor, visited);
    }
    // 后序位置
}
```

可以看到，图的遍历比多叉树的遍历多了一个 visited 数组，用来记录被遍历过的节点，避免遇到环时陷入死循环。

为什么成环会导致死循环

举个最简单的成环场景，有一条 1 -> 2 的边，同时有一条 2 -> 1 的边，节点 1, 2 就形成了一个环：

```cpp
// 遍历图的所有节点
void traverse(const Graph& graph, int s, vector<bool>& visited) {
    // base case
    if (s < 0 || s >= graph.size()) {
        return;
    }
    if (visited[s]) {
        // 防止死循环
        return;
    }
    // 前序位置
    visited[s] = true;
    cout << "visit " << s << endl;
    for (const Graph::Edge& e : graph.neighbors(s)) {
        traverse(graph, e.to, visited);
    }
    // 后序位置
}
```

如果我们不标记遍历过的节点，那么从 1 开始遍历，会走到 2，再走到 1，再走到 2，再走到 1，如此 1->2->1->2->... 无限递归循环下去。

如果有了 visited 数组，第一次遍历到 1 时，会标记 1 为已访问，出现 1->2->1 这种情况时，发现 1 已经被访问过，就会直接返回，从而终止递归，避免了死循环。

有了上面的铺垫，就可以写出基于邻接表/邻接矩阵的图遍历代码了。虽然邻接表/邻接矩阵的底层存储方式不同，但提供了统一的 API，所以直接使用
图结构基础和通用实现
 中那个 Graph 接口的方法即可：

```cpp
// 多叉树节点
class Node {
public:
    int val;
    vector<Node*> children;

    Node(int v = 0) : val(v) {}
};

// 遍历多叉树的树枝
void traverseBranch(Node* root) {
    // base case
    if (root == nullptr) {
        return;
    }
    for (Node* child : root->children) {
        cout << "visit branch: " << root->val << " -> " << child->val << endl;
        traverseBranch(child);
    }
}

// 图节点
class Vertex {
public:
    int id;
    vector<Vertex*> neighbors;

    Vertex(int i = 0) : id(i) {}
};

// 遍历图的边
// 需要一个二维 visited 数组记录被遍历过的边，visited[u][v] 表示边 u->v 已经被遍历过
void traverseEdges(Vertex* s, vector<vector<bool>>& visited) {
    // base case
    if (s == nullptr) {
        return;
    }
    for (Vertex* neighbor : s->neighbors) {
        // 如果边已经被遍历过，则跳过
        if (visited[s->id][neighbor->id]) {
            continue;
        }
        // 标记并访问边
        visited[s->id][neighbor->id] = true;
        cout << "visit edge: " << s->id << " -> " << neighbor->id << endl;
        traverseEdges(neighbor, visited);
    }
}
```

你可以打开下面的可视化面板，多次点击 console.log 这行代码，即可看到 DFS 遍历图的过程：

算法可视化

由于 visited 数组的剪枝作用，这个遍历函数会遍历一次图中的所有节点，并尝试遍历一次所有边，所以算法的时间复杂度是
𝑂
(
𝐸
+
𝑉
)
O(E+V)，其中 E 是边的总数，V 是节点的总数。

时间复杂度为什么是 $O(E + V)$？

我们之前讲解
二叉树的遍历
 时说，二叉树的遍历函数时间复杂度是
𝑂
(
𝑁
)
O(N)，其中
𝑁
N 是节点的总数。

这里图结构既然是树结构的延伸，为什么图的遍历函数时间复杂度是
𝑂
(
𝐸
+
𝑉
)
O(E+V)，要把边的数量
𝐸
E 也算进去呢？为什么不是
𝑂
(
𝑉
)
O(V) 呢？

这是个非常好的问题。你可以花上两分钟想想，我把答案写在下面。

点击查看答案

### 遍历所有边（二维 visited 数组）

对于图结构，遍历所有边的场景并不多见，主要是
计算欧拉路径
 时会用到，所以这里简单提一下。

上面遍历所有节点的代码用一个一维的 visited 数组记录已经访问过的节点，确保每个节点只被遍历一次；那么最简单直接的实现思路就是用一个二维的 visited 数组来记录遍历过的边（visited[u][v] 表示边 u->v 已经被遍历过），从而确保每条边只被遍历一次。

先参考多叉树的遍历进行对比：

```cpp
// 从起点 s 开始遍历图的所有边
void traverseEdges(const Graph& graph, int s, vector<vector<bool>>& visited) {
    // base case
    if (s < 0 || s >= graph.size()) {
        return;
    }
    for (const Graph::Edge& e : graph.neighbors(s)) {
      // 如果边已经被遍历过，则跳过
      if (visited[s][e.to]) {
        continue;
      }
      // 标记并访问边
      visited[s][e.to] = true;
      cout << "visit edge: " << s << " -> " << e.to << endl;
      traverseEdges(graph, e.to, visited);
    }
}
```

提示

由于一条边由两个节点构成，所以我们需要把前序位置的相关代码放到 for 循环内部。

接下来，我们可以用
图结构基础和通用实现
 中的 Graph 接口来实现：

```
// 从起点 s 开始遍历图的所有边
void traverseEdges(const Graph& graph, int s, vector<vector<bool>>& visited) {
    // base case
    if (s < 0 || s >= graph.size()) {
        return;
    }
    for (const Graph::Edge& e : graph.neighbors(s)) {
      // 如果边已经被遍历过，则跳过
      if (visited[s][e.to]) {
        continue;
      }
      // 标记并访问边
      visited[s][e.to] = true;
      cout << "visit edge: " << s << " -> " << e.to << endl;
      traverseEdges(graph, e.to, visited);
    }
}
```

显然，使用二维 visited 数组并不是一个很高效的实现方式，因为需要创建二维 visited 数组，这个算法的时间复杂度是
𝑂
(
𝐸
+
𝑉
2
)
O(E+V
2
)，空间复杂度是
𝑂
(
𝑉
2
)
O(V
2
)，其中
𝐸
E 是边的数量，
𝑉
V 是节点的数量。

在讲解
Hierholzer 算法计算欧拉路径
 时，我们会介绍一种简单的优化避免使用二维 visited 数组，这里暂不展开。

### 遍历所有路径（onPath 数组）

为啥要把图的这几种遍历都讲清楚？因为本站开篇就讲，一切算法的本质是穷举。只要你学会了穷举一切路径，就肯定会计算最短路径，这是图论中一类经典问题。

对于树结构，遍历所有「路径」和遍历所有「节点」是没什么区别的。而对于图结构，遍历所有「路径」和遍历所有「节点」稍有不同。

因为对于树结构来说，只能由父节点指向子节点，所以从根节点 root 出发，到任意一个节点 targetNode 的路径都是唯一的。换句话说，我遍历一遍树结构的所有节点之后，必然可以找到 root 到 targetNode 的唯一路径：

了解会员权益

更新时间：2026/06/12 00:27

> [!warning] 付费章节
> 本章内容为 labuladong.online 付费会员内容。本笔记仅保留公开部分 + C++ 代码片段的整理（由 agent 自动从 C++ tab 提取）。完整讲解请见 [原网页](https://labuladong.online/zh/algo/data-structure-basic/graph-traverse-basic/)。


## 关联章节

- [[33-graph-basic|图结构的通用代码实现]]
- [[24-binary-tree-traverse-basic|二叉树的递归/层序遍历]]
