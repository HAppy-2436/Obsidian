---
title: 图结构的 DFS/BFS 遍历
tags:
  - 图
  - DFS
  - BFS
  - 遍历
  - 数据结构
order: 34
prerequisites:
  - "[[33-graph-basic]]"
  - "[[24-binary-tree-traverse-basic]]"
group: 图
subgroup: 遍历
paywall: false
source: https://labuladong.online/zh/algo/data-structure-basic/graph-traverse-basic/
---

# 图结构的 DFS/BFS 遍历

## 学习目标

- 理解图遍历是**多叉树遍历的延伸**，核心区别是**需要 visited 数组**
- 掌握 **DFS（深度优先）** 和 **BFS（广度优先）** 两种基本遍历方式
- 区分**遍历节点、遍历边、遍历路径**三种场景
- 理解**visited（一维）** 与 **onPath + visited** 的区别
- 能够基于 [[33-graph-basic|Graph 接口]] 写出 DFS / BFS 模板
- 理解 O(V + E) 的时间复杂度来源

## 一句话总结

图的遍历 = **多叉树遍历 + visited 数组**——因为图可能**有环**，所以必须用 `visited` 在**前序位置**标记已访问节点来避免死循环；DFS 走"一条路走到黑"、BFS 走"一圈一圈扩散"，时间复杂度都是 **O(V + E)**。

## 前置知识

阅读本文前，你需要先学习：

- [[33-graph-basic|图结构的通用代码实现]]
- [[24-binary-tree-traverse-basic|二叉树的递归/层序遍历]]（图的 DFS / BFS 概念原型）

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
