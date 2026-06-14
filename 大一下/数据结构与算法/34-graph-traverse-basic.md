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


## 1. 图遍历 vs 多叉树遍历

[[25-n-ary-tree-traverse-basic|多叉树遍历]] 的核心框架：

```cpp
// 多叉树遍历框架
void traverse(Node* root) {
    if (root == nullptr) return;
    // 前序位置
    for (Node* child : root->children) {
        traverse(child);
    }
    // 后序位置
}
```

**图遍历** 的差异只有**一行**——加一个 `visited` 数组：

```cpp
// 图遍历框架
void traverse(Graph& g, int s, vector<bool>& visited) {
    if (visited[s]) return;        // 防止环中死循环
    visited[s] = true;              // 前序位置标记
    // 访问节点 s
    for (const Edge& e : g.neighbors(s)) {
        traverse(g, e.to, visited);
    }
}
```

### 1.1 为什么必须有 visited？

**图可能有环**——比如 `1 <=> 2`：

- 没有 visited：从 1 出发 → 走到 2 → 走到 1 → 走到 2 → ... **无限递归**！
- 有 visited：第一次到 1 时标记，第二次到 1 时**直接返回**，避免死循环。

## 2. 三种遍历场景

| 场景 | 标记数组 | 标记位置 | 撤销位置 | 典型应用 |
|------|----------|----------|----------|----------|
| **遍历所有节点** | `visited[]` | 前序 | 不需要 | 连通块、岛屿数 |
| **遍历所有边** | `visited[][]`（二维） | 前序（for 循环内） | 不需要 | 欧拉路径 |
| **遍历所有路径** | `onPath[]` + `visited[]` | 前序进入 | 后序撤销 | 排列/子集/拓扑序 |

> [!tip] 为什么"遍历路径"要撤销？
> 遍历**节点**只关心"是否访问过"，但遍历**路径**要枚举"从起点出发的所有可能路径"。一条路径结束时，需要把节点标记**撤销**，让其他路径能再次经过它。

## 3. 深度优先搜索（DFS）

### 3.1 基于 Vertex 类的对比版本

为了和[[25-n-ary-tree-traverse-basic|多叉树遍历]]直观对比，先用一个"伪 Vertex" 类：

```cpp
class Vertex {
public:
    int id;
    vector<Vertex*> neighbors;
};

// 多叉树遍历（无环）
void traverseTree(Node* root) {
    if (!root) return;
    cout << "visit " << root->val << endl;          // 前序
    for (Node* child : root->children) {
        traverseTree(child);
    }
}

// 图遍历（有环，加 visited）
void traverseGraph(Vertex* s, vector<bool>& visited) {
    if (!s) return;
    if (visited[s->id]) return;                     // 防死循环
    visited[s->id] = true;                          // 前序标记
    cout << "visit " << s->id << endl;
    for (Vertex* n : s->neighbors) {
        traverseGraph(n, visited);
    }
}
```

### 3.2 基于 Graph 接口的版本

实际工程里我们用 [[33-graph-basic|Graph 接口]] 写，更通用：

```cpp
#include <bits/stdc++.h>
using namespace std;

namespace dsa {

// 深度优先遍历：从 s 出发，访问所有可达节点
void dfs(const GraphAdjList& g, int s, vector<bool>& visited) {
    if (s < 0 || s >= g.size()) return;
    if (visited[s]) return;                          // 防环
    visited[s] = true;
    cout << "visit " << s << endl;                   // 前序
    for (const Edge& e : g.neighbors(s)) {
        dfs(g, e.to, visited);
    }
}

// 遍历整张图（可能不连通）
void dfsAll(const GraphAdjList& g) {
    vector<bool> visited(g.size(), false);
    for (int s = 0; s < g.size(); ++s) {
        if (!visited[s]) {
            dfs(g, s, visited);                      // 从每个连通分量起点开始
        }
    }
}

} // namespace dsa
```

### 3.3 时间复杂度分析

`dfsAll` 会**访问每个节点恰好一次**（被 `visited` 剪掉），并**遍历每条边恰好一次**（两次，方向各一次），所以：

- **时间复杂度**：**O(V + E)**
- **空间复杂度**：O(V)（递归栈 + visited 数组）

> [!question] 为什么不是 O(V)，要把 E 算进去？
> 树遍历是 O(N)，因为树的边数 = N-1，O(V + E) = O(V)。但图的 E 可以是 O(V²)，所以必须单独算。

## 4. 广度优先搜索（BFS）

BFS 用**队列**实现，逻辑是"一圈一圈向外扩散"——这一点和多叉树的**层序遍历**完全相同。

```cpp
#include <bits/stdc++.h>
using namespace std;

namespace dsa {

void bfs(const GraphAdjList& g, int s) {
    vector<bool> visited(g.size(), false);
    queue<int> q;
    q.push(s);
    visited[s] = true;

    while (!q.empty()) {
        int v = q.front(); q.pop();
        cout << "visit " << v << endl;               // 第一次出队即访问

        for (const Edge& e : g.neighbors(v)) {
            if (!visited[e.to]) {
                visited[e.to] = true;                // 入队时立即标记
                q.push(e.to);
            }
        }
    }
}

// 整图 BFS
void bfsAll(const GraphAdjList& g) {
    vector<bool> visited(g.size(), false);
    for (int s = 0; s < g.size(); ++s) {
        if (!visited[s]) bfs(g, s);
    }
}

} // namespace dsa
```

### 4.1 BFS 的两个细节

1. **入队时立即标记**（而不是出队时）——避免同一节点被多次入队。
2. **遍历顺序**：BFS 在无权图中得到的访问顺序就是**从起点出发的层序**——这是 BFS 找**最短路**的基础（见 [[35-use-case-of-dfs-bfs|DFS/BFS 应用]]）。

### 4.2 复杂度

- **时间复杂度**：O(V + E)（每个节点入队一次、出队一次，每条边检查一次）
- **空间复杂度**：O(V)

## 5. 遍历所有边（二维 visited）

遍历**边**的场景较少，主要在**欧拉路径**问题中出现。简单思路是用 `visited[u][v]` 标记 `u -> v` 这条边是否被走过。

```cpp
namespace dsa {

// 遍历所有有向边（用二维 visited）
void traverseEdges(const GraphAdjList& g, int s,
                   vector<vector<bool>>& visited) {
    if (s < 0 || s >= g.size()) return;
    for (const Edge& e : g.neighbors(s)) {
        if (visited[s][e.to]) continue;             // 边走过了就跳过
        visited[s][e.to] = true;
        cout << "visit edge: " << s << " -> " << e.to << endl;
        traverseEdges(g, e.to, visited);
    }
}

} // namespace dsa
```

> [!warning] 性能警告
> 二维 visited 数组占用 **O(V²) 空间**，对大图很浪费。[[38-eulerian-graph|Hierholzer 算法]] 会给出更聪明的优化（不依赖二维数组）。

## 6. 遍历所有路径（onPath + visited）

这是最有趣的场景——枚举**从起点到任意节点的所有可能路径**，典型应用是**排列、子集、拓扑序**。

```cpp
namespace dsa {

// 遍历从 s 出发的所有路径
// onPath[v] = true 表示 v 在当前路径上
// visited[v] = true 表示 v 曾经过（防止环）
vector<vector<int>> allPaths;

void traversePaths(const GraphAdjList& g, int s,
                   vector<bool>& visited,
                   vector<bool>& onPath,
                   vector<int>& path) {
    if (s < 0 || s >= g.size()) return;
    if (onPath[s]) return;                          // 路径上重复 → 有环
    if (visited[s]) return;                         // 已访问

    // 前序：加入路径
    visited[s] = true;
    onPath[s] = true;
    path.push_back(s);

    // 递归所有邻居
    for (const Edge& e : g.neighbors(s)) {
        traversePaths(g, e.to, visited, onPath, path);
    }

    // 假设到达终点就记录一条路径（这里以"叶节点"为例）
    bool isLeaf = true;
    for (const Edge& e : g.neighbors(s)) {
        if (!onPath[e.to]) { isLeaf = false; break; }
    }
    if (isLeaf) {
        allPaths.push_back(path);
    }

    // 后序：撤销
    path.pop_back();
    onPath[s] = false;
}

} // namespace dsa
```

### 6.1 visited 与 onPath 的区别

| 数组 | 标记时机 | 撤销时机 | 作用 |
|------|----------|----------|------|
| `visited` | 前序 | 不撤销 | 防止**重复访问**（剪枝） |
| `onPath` | 前序 | **后序**撤销 | 标记**当前路径上**的节点 |

> [!tip] 记忆口诀
> `visited` 是"永久记忆"，`onPath` 是"临时记忆"。
> **只想遍历节点** → 只用 `visited`。
> **要枚举所有路径** → `visited` + `onPath`。

## 7. 完整测试程序

```cpp
int main() {
    using namespace dsa;
    // 一张图：
    //   0 - 1 - 3
    //   |   |
    //   2 - 4
    vector<tuple<int,int,int>> edges = {
        {0, 1, 1}, {1, 3, 1},
        {0, 2, 1}, {1, 4, 1},
        {2, 4, 1}
    };
    GraphAdjList g = buildFromEdges(5, edges, EdgeDir::UNDIRECTED);

    cout << "DFS from 0: ";
    vector<bool> visited(g.size(), false);
    dfs(g, 0, visited);
    cout << endl;

    cout << "BFS from 0: ";
    bfs(g, 0);
    cout << endl;

    cout << "整图 DFS（处理不连通）: ";
    dfsAll(g);
    cout << endl;
    return 0;
}
```

**输出**：

```text
DFS from 0: visit 0 visit 1 visit 3 visit 4 visit 2
BFS from 0: visit 0 visit 1 visit 2 visit 3 visit 4
整图 DFS（处理不连通）: visit 0 visit 1 visit 3 visit 4 visit 2
```

> 注意到 DFS 和 BFS 的访问顺序不同——DFS 一条路走到黑（0→1→3→4→2），BFS 一圈圈扩散（0→1,2→3,4）。

## 8. 复杂度表

| 算法 | 时间 | 空间 | 适用场景 |
|------|------|------|----------|
| DFS 遍历节点 | O(V + E) | O(V) | 连通块、岛屿、排列 |
| BFS 遍历节点 | O(V + E) | O(V) | 最短路、扩散 |
| 遍历所有边（二维 visited） | O(E + V²) | O(V²) | 欧拉路径（不推荐） |
| 遍历所有路径 | O(路径数) | O(V) | 排列、子集、拓扑序 |

## 9. 应用场景

- **DFS**：连通块、岛屿、排列、子集、拓扑排序、欧拉路径
- **BFS**：无权图最短路、扩散、层序访问
- 详细应用见 [[35-use-case-of-dfs-bfs|DFS 和 BFS 的常用场景]]

## 下一章

→ [[35-use-case-of-dfs-bfs|DFS 和 BFS 的常用场景]]

## 相关章节

- [[33-graph-basic|图结构通用实现]] — 遍历的目标对象
- [[24-binary-tree-traverse-basic|二叉树遍历]] — 图遍历的逻辑原型
- [[25-n-ary-tree-traverse-basic|N 叉树遍历]] — 另一种"无环"的多叉遍历
- [[35-use-case-of-dfs-bfs|DFS/BFS 应用]] — 遍历的具体用例
- [[37-graph-shortest-path|最短路径]] — BFS 的扩展
- [[38-eulerian-graph|欧拉图]] — 遍历所有边的应用

## 关联章节

- [[33-graph-basic|图结构的通用代码实现]]
- [[24-binary-tree-traverse-basic|二叉树的递归/层序遍历]]
