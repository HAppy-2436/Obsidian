---
title: 最小生成树算法概览
tags:
  - 图
  - 最小生成树
  - Kruskal
  - Prim
  - 数据结构
order: 36
prerequisites:
  - "[[34-graph-traverse-basic]]"
group: 图
subgroup: 算法
paywall: false
source: https://labuladong.online/zh/algo/data-structure-basic/graph-minimum-spanning-tree/
---

# 最小生成树算法概览

## 学习目标

- 理解**生成树（Spanning Tree）**和**最小生成树（MST）**的定义
- 掌握**Kruskal 算法**的贪心思想（按边权排序 + Union-Find）
- 掌握**Prim 算法**的贪心思想（按点扩展 + 优先级队列）
- 理解两种算法的**适用场景**：Kruskal 适合稀疏图，Prim 适合稠密图
- 了解 MST 在**网络设计、随机迷宫生成**等场景的应用

## 一句话总结

**最小生成树（MST）= 在加权连通无向图中找一棵**包含所有节点、边权和最小**的**生成树**。两种经典贪心算法——**Kruskal（按边排序 + 并查集）** 和 **Prim（按点扩展 + 优先队列）**——都能在 **O(E log E) ~ O(E log V)** 内解决 MST 问题。

## 前置知识

阅读本文前，你需要先学习：

- [[32-graph-terminology|图的基本术语]]（生成树、连通图、连通分量、加权图）
- [[33-graph-basic|图结构的通用代码实现]]（邻接表 / 邻接矩阵）
- [[34-graph-traverse-basic|图结构的 DFS/BFS 遍历]]（生成树的一种特例：DFS 树 / BFS 树）
- [[30-union-find-basic|Union-Find 并查集]]（Kruskal 的核心工具）

## 1. 什么是生成树？

给定一个**无向连通图** G，其**生成树（Spanning Tree）**是 G 的一个子图，满足：

1. 包含 G 中的**所有顶点**（V 个）
2. 是一棵树——**连通 + 无环**
3. 因此**边数 = V - 1**

> [!tip] 直觉
> 生成树就是"用最少的边把图中所有节点连通起来"的那个骨架——少一条边就断开，多一条边就有环。

**一个图可以有多个不同的生成树**（就像从一张网上剪掉一些边，只要保证连通就仍是生成树）。

## 2. 什么是最小生成树？

如果图 G 是**加权图**，那么**最小生成树（Minimum Spanning Tree, MST）**就是**边权重总和最小**的生成树。

例如某加权图有多个生成树：

- 生成树 A：总权重 = 5 + 3 + 7 = 15
- 生成树 B：总权重 = 2 + 3 + 5 = 10  ← **MST**

MST 在现实中有非常多的应用，**边的权重可能代表距离、成本、时间**。

### 2.1 经典应用场景

| 场景 | 节点 | 边 | 边权 |
|------|------|----|------|
| 城市公路网 | 城市 | 公路 | 修建成本 |
| 通信网络 | 城市 | 光纤 | 铺设成本 |
| 电路布线 | 元器件 | 导线 | 长度 |
| 管道铺设 | 站点 | 管道 | 距离/费用 |

> **问题抽象**：想在若干城市之间修建公路，节点代表城市，边代表可修建的公路，边权代表修建成本，希望**找到一种方案能连接所有城市且总成本最小**——这就是典型的 MST 问题。

## 3. 两种经典算法

### 3.1 Kruskal 算法（边驱动）

**核心思想**：按**边的权重**从小到大依次考虑，**如果这条边连接的两个节点不连通，就选它**；否则跳过。

> 简单地说：每次选**当前最短的、不会形成环的边**。

**算法流程**：

1. 把所有边按权重从小到大排序
2. 初始化一个 [[30-union-find-basic|Union-Find]] 数据结构（每个节点自成一个集合）
3. 遍历排序后的边：若 `(u, v)` 两端点不在同一集合 → 选这条边 → `union(u, v)`
4. 直到选满 V - 1 条边

**伪代码**：

```text
kruskal(G):
    edges = G 的所有边按权重升序
    uf = new UnionFind(G.V)
    mst = []
    for e in edges:
        if uf.find(e.u) != uf.find(e.v):
            uf.union(e.u, e.v)
            mst.append(e)
            if mst.size == V - 1: break
    return mst
```

**复杂度**：

- 排序 O(E log E)
- Union-Find O(α(V)) 几乎常数
- **总复杂度 O(E log E)** ≈ O(E log V)

**适用场景**：**稀疏图**（E 远小于 V² 时排序代价低）。

### 3.2 Prim 算法（点驱动）

**核心思想**：从一个起点出发，**每次选"连接已选集合与未选集合的最短边"对应的那个未选节点**，加入到已选集合。

> 简单地说：每一步把"距离已选集合最近"的节点拉进来。

**算法流程**：

1. 选一个起点 s 加入已选集合
2. 用一个**优先级队列**（最小堆）维护"已选集合到未选节点的最小边"
3. 每次从堆顶取最短边 (u, v)，如果 v 未被选过就选 v
4. 更新堆：v 加入后，把 v 到所有未选邻居的边加入堆
5. 直到选满 V 个节点（产生 V - 1 条边）

**伪代码**：

```text
prim(G, s):
    in_mst = [false] * G.V
    pq = MinPriorityQueue()
    pq.push((0, s))            # (边权, 节点)
    mst_weight = 0
    while pq not empty:
        (w, v) = pq.pop()
        if in_mst[v]: continue
        in_mst[v] = true
        mst_weight += w
        for (v, u, weight) in G.neighbors(v):
            if not in_mst[u]:
                pq.push((weight, u))
    return mst_weight
```

> [!tip] 关联性
> Prim 和 [[37-graph-shortest-path|Dijkstra]] 的代码框架**几乎一模一样**——区别仅在于：
> - Dijkstra 更新 `distTo[v] + weight(u,v)`
> - Prim 更新 `weight(u,v)`（**没有 `distTo[v]`**）

**复杂度**：

- 优先队列 O((V + E) log V)
- **总复杂度 O(E log V)**

**适用场景**：**稠密图**（V 大但 E 接近 V²），或者用 [[33-graph-basic|邻接矩阵]] + 朴素 Prim 达到 O(V²)。

### 3.3 对比

| 维度 | Kruskal | Prim |
|------|---------|------|
| 思想 | 按**边**排序 | 按**点**扩展 |
| 数据结构 | Union-Find | 优先级队列 |
| 适合 | **稀疏图** | **稠密图** |
| 时间复杂度 | O(E log E) | O(E log V) |
| 实现难度 | 简单 | 中等 |

> [!tip] 选哪个？
> - **E < V log V**（稀疏）→ **Kruskal** 更优
> - **E ≈ V²**（稠密）→ **Prim + 堆** 或 **Prim + 邻接矩阵 O(V²)** 更优

## 4. 最小生成树的性质

### 4.1 切分定理（Cut Property）

> **切分定理**：把图的所有节点分成两部分 A、B（A ∪ B = V），**连接 A 和 B 的最短边一定在某个 MST 中**。

Kruskal 和 Prim 都是**切分定理的贪心实现**——每一步选的边都是某次切分下的最短边。

### 4.2 MST 的数量

- 一个图可能有多棵不同的 MST（如果存在多条权重相同的边）
- 任意两棵 MST 在权重上一定相等

## 5. 随机迷宫生成（趣味应用）

最小生成树算法经过巧妙改造后，可以**生成游戏中的随机迷宫/洞穴**。

### 5.1 核心思想

利用 MST 的两个特性：

1. **连通性**——MST 包含所有节点 → 迷宫中所有房间相通
2. **无环性**——MST 恰好 V-1 条边 → 迷宫不会有"捷径"

### 5.2 两种生成风格

| 算法 | 起始状态 | 过程 | 视觉特点 |
|------|----------|------|----------|
| **Kruskal** | 网格中**多处**出现随机路径 | 各点独立向外扩展 | 多起点、最终融合 |
| **Prim** | 全是墙，从起点**单点**向外扩展 | 一条"藤蔓"逐渐蔓延 | 单点生长、藤蔓状 |

游戏面板中可以选择算法，**生成** + **求解**的过程都能直观看到（用 BFS/DFS 求解最短路径）。

> 这种"基于 MST 的迷宫生成"被广泛应用于**Roguelike、地牢探险、随机地图**等游戏中。

## 6. 最小生成树 vs 最短路径

这是两个**完全不同**的问题，初学者容易混淆：

| 维度 | 最小生成树 | 最短路径 |
|------|-----------|----------|
| 目标 | 选 V-1 条边，**覆盖所有节点**，使总权最小 | 从起点到某节点的**单条最短路** |
| 输出 | 一棵树（V-1 条边） | 一组 `dist[]` 数组 |
| 经典算法 | Kruskal / Prim | Dijkstra / Bellman-Ford / Floyd |
| 应用 | 网络设计 | 路径规划 |

## 7. 复杂度表

| 算法 | 时间复杂度 | 空间 | 适合的图 |
|------|----------|------|----------|
| **Kruskal** | O(E log E) | O(V + E) | 稀疏图 |
| **Prim（堆）** | O(E log V) | O(V + E) | 稀疏/中等 |
| **Prim（邻接矩阵）** | O(V²) | O(V²) | 稠密图 |

## 8. 应用场景

- **网络设计**：通信网络、电路布线、道路规划
- **聚类分析**：把多棵 MST 子树视为不同聚类
- **图像分割**：基于 MST 的图像分割算法
- **随机迷宫生成**：游戏开发
- **近似算法**：TSP（旅行商问题）的 2-近似解法


## C++ 完整实现

> [!info] 📌 付费章节补全内容（基于算法知识体系补充）

### Prim 算法（稠密图，O(N²)）

```cpp
#include <bits/stdc++.h>
using namespace std;

namespace dsa {

// Prim 算法：稠密图最小生成树（O(V²)，邻接矩阵）
int prim(vector<vector<int>>& graph) {
    int n = graph.size();
    vector<int> dist(n, INT_MAX);  // 到当前 MST 的最小距离
    vector<bool> visited(n, false);
    dist[0] = 0;
    int total = 0;

    for (int i = 0; i < n; i++) {
        // 找未访问的最近节点
        int u = -1;
        for (int v = 0; v < n; v++) {
            if (!visited[v] && (u == -1 || dist[v] < dist[u])) u = v;
        }
        if (u == -1 || dist[u] == INT_MAX) return -1;  // 不连通
        visited[u] = true;
        total += dist[u];

        // 更新邻居距离
        for (int v = 0; v < n; v++) {
            if (!visited[v] && graph[u][v] < dist[v]) {
                dist[v] = graph[u][v];
            }
        }
    }
    return total;
}

// Kruskal 算法（稀疏图，O(E log E)，并查集）
int kruskal(int n, vector<vector<int>>& edges) {
    // edges: [[u, v, w], ...]
    sort(edges.begin(), edges.end(),
         [](auto& a, auto& b) { return a[2] < b[2]; });

    vector<int> parent(n);
    iota(parent.begin(), parent.end(), 0);

    function<int(int)> find = [&](int x) {
        return parent[x] == x ? x : parent[x] = find(parent[x]);
    };

    int total = 0, count = 0;
    for (auto& e : edges) {
        int u = e[0], v = e[1], w = e[2];
        if (find(u) != find(v)) {
            parent[find(u)] = find(v);
            total += w;
            count++;
            if (count == n - 1) break;
        }
    }
    return count == n - 1 ? total : -1;
}

} // namespace dsa
```

### 复杂度对比

| 算法 | 时间 | 适用 |
|------|------|------|
| Prim | O(V²) | 稠密图（边数 ≈ V²）|
| Kruskal | O(E log E) | 稀疏图（边数 << V²）|

**应用场景**：
- 网络布线：最少光纤连接所有节点
- 道路规划：最短公路网络
- 电路设计：最少连线

## 下一章

→ [[37-graph-shortest-path|图结构最短路径算法概览]]

## 相关章节

- [[32-graph-terminology|图的基本术语]] — 必备基础
- [[33-graph-basic|图结构实现]] — 邻接表 + 邻接矩阵
- [[34-graph-traverse-basic|图遍历]] — DFS 树 / BFS 树 都是生成树
- [[30-union-find-basic|Union-Find]] — Kruskal 的核心工具
- [[37-graph-shortest-path|最短路径]] — 与 MST 平行的另一类图论核心问题
- [[22-binary-heap-implement|堆 / 优先级队列]] — Prim 算法的核心工具
