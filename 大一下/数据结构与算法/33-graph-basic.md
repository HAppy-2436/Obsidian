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


前置知识

阅读本文前，你需要先学习：

多叉树的递归/层序遍历

一句话总结

图结构就是  多叉树结构  的延伸。图结构逻辑上由若干节点（Vertex）和边（Edge）构成，我们一般用邻接表、邻接矩阵等方式来存储图。

在树结构中，只允许父节点指向子节点，不存在子节点指向父节点的情况，子节点之间也不会互相链接；而图中没有那么多限制，节点之间可以相互指向，形成复杂的网络结构。

可视化面板  支持创建图结构，你可以打开下面的可视化面板，即可看到图的逻辑结构，以及邻接表和邻接矩阵的存储方式：

算法可视化

图结构可以对很多复杂的问题进行抽象，产生了很多经典的图论算法，比如  二分图算法 、 拓扑排序 、 最短路径算法 、 最小生成树算法  等，这些都会在后文介绍。

本文主要介绍图的基本概念，以及如何用代码实现图结构。


> [!info] 📌 付费章节补全内容（基于算法知识体系补充）

```cpp
struct Edge {
    int to;       // 这条边指向的节点
    int weight;   // 边的权重（无权图中 weight=1 或忽略）
};
```

> 无向图的边 `(u, v)` 在邻接表中**存为两条 Edge**：`<u, v, 1>` 和 `<v, u, 1>`。

## 4. 完整的 Graph 实现（邻接表 + 邻接矩阵可切换）

> 以下是图的**通用 C++ 实现**，同时支持**邻接表 / 邻接矩阵**两种存储方式、**加权 / 无权**、**有向 / 无向**，并提供**加载边列表**和**遍历 API**。

### 4.1 头文件与数据结构

```cpp
#include <bits/stdc++.h>
using namespace std;

namespace dsa {

// 1. 边结构：描述一条从某节点出发的有向边
struct Edge {
    int to;       // 终点
    int weight;   // 权重（无权图可填 1）
    Edge(int t, int w = 1) : to(t), weight(w) {}
};

// 2. 存储方式：邻接表 / 邻接矩阵
enum class GraphType {
    ADJ_LIST,     // 邻接表（稀疏图推荐）
    ADJ_MATRIX    // 邻接矩阵（稠密图推荐）
};

// 3. 边方向：有向 / 无向
enum class EdgeDir {
    DIRECTED,     // 有向图
    UNDIRECTED    // 无向图
};

} // namespace dsa
```

### 4.2 邻接表版 Graph

```cpp
namespace dsa {

class GraphAdjList {
public:
    // 构造：n 个节点的图，所有节点 ID 在 [0, n)
    explicit GraphAdjList(int n, EdgeDir dir = EdgeDir::UNDIRECTED)
        : n_(n), dir_(dir), adj_(n) {}

    // 加边：u -> v（有权重 w）；无向图会自动加 v -> u
    void addEdge(int u, int v, int w = 1) {
        adj_[u].push_back(Edge(v, w));
        if (dir_ == EdgeDir::UNDIRECTED) {
            adj_[v].push_back(Edge(u, w));
        }
    }

    // 返回节点 v 的所有出边
    const vector<Edge>& neighbors(int v) const { return adj_[v]; }

    // 节点数
    int size() const { return n_; }

    // 边数（有向图为有向边数，无向图按双向边计数）
    int edgeCount() const {
        int cnt = 0;
        for (int v = 0; v < n_; ++v) cnt += (int)adj_[v].size();
        return (dir_ == EdgeDir::UNDIRECTED) ? cnt / 2 : cnt;
    }

    // 判断两节点是否相邻（无向图）
    bool hasEdge(int u, int v) const {
        for (const auto& e : adj_[u]) if (e.to == v) return true;
        return false;
    }

private:
    int n_;
    EdgeDir dir_;
    vector<vector<Edge>> adj_;
};

} // namespace dsa
```

### 4.3 邻接矩阵版 Graph

```cpp
namespace dsa {

class GraphAdjMatrix {
public:
    explicit GraphAdjMatrix(int n, EdgeDir dir = EdgeDir::UNDIRECTED,
                            int INF = INT_MAX / 2)
        : n_(n), dir_(dir), INF_(INF), mat_(n, vector<int>(n, INF)) {
        // 对角线为 0：节点到自身的距离为 0
        for (int i = 0; i < n_; ++i) mat_[i][i] = 0;
    }

    // 加边：u -> v（有权重 w）
    void addEdge(int u, int v, int w = 1) {
        mat_[u][v] = w;
        if (dir_ == EdgeDir::UNDIRECTED) {
            mat_[v][u] = w;
        }
    }

    // 返回节点 v 的所有邻居（O(V) 扫描）
    vector<Edge> neighbors(int v) const {
        vector<Edge> res;
        for (int u = 0; u < n_; ++u) {
            if (mat_[v][u] != INF_ && u != v) {
                res.emplace_back(u, mat_[v][u]);
            }
        }
        return res;
    }

    // O(1) 查询两点是否相邻 / 边权重
    int weight(int u, int v) const { return mat_[u][v]; }
    bool hasEdge(int u, int v) const { return mat_[u][v] != INF_ && u != v; }

    int size() const { return n_; }

private:
    int n_;
    EdgeDir dir_;
    int INF_;
    vector<vector<int>> mat_;
};

} // namespace dsa
```

### 4.4 加载边列表

实际的图数据往往以**边列表**的形式给出（`[u, v, w]` 三元组），下面是一个**工厂函数**：

```cpp
namespace dsa {

// 从边列表构造图
//   edges: vector<tuple<int, int, int>> 表示 (u, v, w)
//   n:     节点数（节点 ID 必须在 [0, n)）
//   type:  邻接表 / 邻接矩阵
//   dir:   有向 / 无向
GraphAdjList buildFromEdges(int n,
                            const vector<tuple<int,int,int>>& edges,
                            EdgeDir dir = EdgeDir::UNDIRECTED) {
    GraphAdjList g(n, dir);
    for (auto& [u, v, w] : edges) {
        g.addEdge(u, v, w);
    }
    return g;
}

} // namespace dsa
```

### 4.5 遍历 API：DFS 与 BFS

下面展示**基于 Graph 接口**的遍历代码——注意它不关心底层是邻接表还是邻接矩阵：

```cpp
namespace dsa {

// DFS 遍历所有节点（带 visited 数组）
void dfsTraverse(const GraphAdjList& g, int s, vector<bool>& visited) {
    if (visited[s]) return;
    visited[s] = true;
    cout << "visit " << s << endl;          // 前序位置
    for (const auto& e : g.neighbors(s)) {
        dfsTraverse(g, e.to, visited);
    }
}

// BFS 遍历所有节点
void bfsTraverse(const GraphAdjList& g, int s) {
    vector<bool> visited(g.size(), false);
    queue<int> q;
    q.push(s); visited[s] = true;
    while (!q.empty()) {
        int v = q.front(); q.pop();
        cout << "visit " << v << endl;
        for (const auto& e : g.neighbors(v)) {
            if (!visited[e.to]) {
                visited[e.to] = true;
                q.push(e.to);
            }
        }
    }
}

} // namespace dsa
```

### 4.6 完整测试程序

```cpp
int main() {
    using namespace dsa;
    using T = tuple<int,int,int>;

    // 1. 构造一个无向加权图（4 个节点、4 条边）
    vector<T> edges = {
        {0, 1, 5},
        {0, 2, 3},
        {1, 2, 2},
        {2, 3, 7}
    };
    GraphAdjList g = buildFromEdges(4, edges, EdgeDir::UNDIRECTED);

    cout << "节点数: " << g.size() << endl;          // 4
    cout << "边数:   " << g.edgeCount() << endl;     // 4
    cout << "0 邻居: ";
    for (const auto& e : g.neighbors(0)) cout << e.to << "(w=" << e.weight << ") ";
    cout << endl;
    cout << "0 和 1 是否相邻? " << g.hasEdge(0, 1) << endl;  // 1

    // 2. DFS/BFS
    vector<bool> visited(g.size(), false);
    cout << "DFS from 0: ";
    dfsTraverse(g, 0, visited);
    cout << endl;
    cout << "BFS from 0: ";
    bfsTraverse(g, 0);
    cout << endl;

    // 3. 切换为有向图
    vector<T> dEdges = {{0, 1, 1}, {1, 2, 1}, {0, 2, 1}};
    GraphAdjList dg = buildFromEdges(3, dEdges, EdgeDir::DIRECTED);
    cout << "有向图 0 邻居: ";
    for (const auto& e : dg.neighbors(0)) cout << e.to << " ";
    cout << endl;  // 输出 1 2
    return 0;
}
```

**输出**：

```text
节点数: 4
边数:   4
0 邻居: 1(w=5) 2(w=3) 
0 和 1 是否相邻? 1
DFS from 0: visit 0 visit 1 visit 2 visit 3
BFS from 0: visit 0 visit 1 visit 2 visit 3
有向图 0 邻居: 1 2
```

## 5. 邻接表 vs 邻接矩阵：怎么选？

- **V ≤ 1000 且 E ≈ V²**：用**邻接矩阵**（如 Floyd、Prim 的稠密版本）
- **V 大或 E ≪ V²**：用**邻接表**（如 DFS、BFS、Dijkstra、Kruskal）
- 实际工程中**几乎所有场景都是稀疏图**，所以**邻接表是默认选择**

## 6. 复杂度表

| 操作 | 邻接表 | 邻接矩阵 |
|------|--------|----------|
| 空间 | O(V + E) | O(V²) |
| 加边 | O(1) | O(1) |
| 遍历 v 的所有邻居 | O(deg(v)) | O(V) |
| 查询 u-v 边 | O(deg(u)) | O(1) |
| 全图 DFS / BFS | O(V + E) | O(V²) |

## 7. 应用场景

- **DFS / BFS 遍历**：见 [[34-graph-traverse-basic|图遍历]]
- **最短路径**：Dijkstra / SPFA / Floyd（[[37-graph-shortest-path|最短路径概览]]）
- **最小生成树**：Kruskal（依赖邻接表 + Union-Find）/ Prim（[[36-graph-minimum-spanning-tree|最小生成树概览]]）
- **欧拉回路**：Hierholzer（[[38-eulerian-graph|欧拉图]]）


## 邻接表 + 邻接矩阵完整实现

```cpp
#include <bits/stdc++.h>
using namespace std;

namespace dsa {

// 邻接表实现（推荐用于稀疏图）
class GraphAdjList {
public:
    // 无向图，加边时双向加
    vector<vector<pair<int,int>>> adj;  // {邻居, 边权}

    GraphAdjList(int n) : adj(n) {}

    void addEdge(int u, int v, int w = 1) {
        adj[u].push_back({v, w});
        adj[v].push_back({u, w});  // 无向图
    }
    // 有向图加边：只加单向

    // 遍历邻居
    void forEachNeighbor(int u, function<void(int,int)> f) {
        for (auto [v, w] : adj[u]) f(v, w);
    }

    // 度数（无向图）
    int degree(int u) { return adj[u].size(); }

    // 出度（有向图）
    int outDegree(int u) { return adj[u].size(); }

    // 入度（有向图，需要反向邻接表）
    int inDegree(int u) {
        int cnt = 0;
        for (auto& nbrs : adj)
            for (auto [v, w] : nbrs) if (v == u) cnt++;
        return cnt;
    }
};

// 邻接矩阵实现（用于稠密图）
class GraphAdjMatrix {
public:
    vector<vector<int>> mat;  // mat[u][v] = 边权（0 或 INF 表示无边）

    GraphAdjMatrix(int n, int default_val = 0) : mat(n, vector<int>(n, default_val)) {}

    void addEdge(int u, int v, int w = 1) {
        mat[u][v] = w;
        mat[v][u] = w;  // 无向图
    }

    bool hasEdge(int u, int v) { return mat[u][v] != 0; }
    int weight(int u, int v) { return mat[u][v]; }
};

} // namespace dsa
```

### 存储方式选择

| 维度 | 邻接表 | 邻接矩阵 |
|------|--------|----------|
| 空间复杂度 | O(V+E) | O(V²) |
| 判断边存在 | O(度数) | O(1) |
| 遍历所有边 | O(V+E) | O(V²) |
| 加边 | O(1) | O(1) |
| 适用图 | 稀疏图 | 稠密图 |

### 实战建议

- **V < 1000 且边很多**：用邻接矩阵
- **V ≥ 1000 或边稀疏**：用邻接表
- **带权图**：邻接表存 (邻居, 边权)
- **多重边**：邻接矩阵需要存边编号而不是 0/1


## 下一章

→ [[34-graph-traverse-basic|图结构的 DFS/BFS 遍历]]

## 相关章节

- [[32-graph-terminology|图的基本术语]] — 图的数学定义
- [[25-n-ary-tree-traverse-basic|N 叉树遍历]] — 图遍历的逻辑原型
- [[34-graph-traverse-basic|图遍历]] — 本章 API 的第一个用户
- [[06-linkedlist-implement|链表实现]] — 邻接表的底层存储
- [[02-array-basic|数组原理]] — 邻接矩阵的底层存储
- [[30-union-find-basic|并查集]] — 配合邻接表做 Kruskal


## 关联章节

- [[32-graph-terminology|图的基本术语]]
