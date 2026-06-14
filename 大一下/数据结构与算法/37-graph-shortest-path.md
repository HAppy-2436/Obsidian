---
title: 图结构最短路径算法概览
tags:
  - 图
  - 最短路径
  - Dijkstra
  - Bellman-Ford
  - Floyd
  - 数据结构
order: 37
prerequisites:
  - "[[34-graph-traverse-basic]]"
group: 图
subgroup: 算法
paywall: false
source: https://labuladong.online/zh/algo/data-structure-basic/graph-shortest-path/
---

# 图结构最短路径算法概览

## 学习目标

- 理解**单源最短路径 / 点对点最短路径 / 多源最短路径**三类问题的差别
- 掌握四种经典最短路算法的**核心思想、适用场景**：
  - **Dijkstra**（单源，不能负权）
  - **Bellman-Ford / SPFA**（单源，可负权）
  - **A\***（点对点，启发式）
  - **Floyd**（多源，可负权）
- 理解**负权重边和负权重环**对算法的影响
- 能够根据题目场景**正确选择**算法

## 一句话总结

**最短路径**是图论的另一类核心问题，目标是求**从起点到目标节点的最小权重路径**；根据起点数量分为**单源 / 点对点 / 多源**，根据边权是否为负选择**Dijkstra / Bellman-Ford / Floyd**——这些算法本质都是 [[34-graph-traverse-basic|BFS / DFS]] 的加权扩展。

## 前置知识

阅读本文前，你需要先学习：

- [[33-graph-basic|图结构的通用代码实现]]
- [[34-graph-traverse-basic|图结构的 DFS/BFS 遍历]]（最短路算法的逻辑起点）

## 1. 最短路径问题概览

**最短路径**在生活中应用非常广泛：地图导航、网络路由、社交推荐…… 算法中我们一般把这类问题抽象成**计算加权图中的最小路径权重**。

> "**最短路径**"和"**最小路径权重和**"在本文中是**等价**的。

根据起点数量，最短路径问题分为三大类：

| 类型 | 描述 | 输出 | 经典算法 |
|------|------|------|----------|
| **单源最短路径（SSSP）** | 从某起点到**所有其他节点** | `distTo[]` 一维数组 | Dijkstra / Bellman-Ford / SPFA |
| **点对点最短路径** | 从某起点到**某一目标** | 一个数（距离） | A* |
| **多源最短路径（APSP）** | **任意两节点**之间 | `dist[][]` 二维数组 | Floyd |

## 2. 单源最短路径（SSSP）

**问题**：从节点 s 出发，计算到图中**所有其他节点**的最短距离，输出 `distTo[v] = s → v 的最短路径长度`。

### 2.1 Dijkstra 算法

**核心思想**：BFS + 贪心——每次从未确定最短路的节点中，**选 dist 最小的那个**确定下来，然后**松弛**（relax）它的邻居。

> [!tip] 关键前提
> Dijkstra **不能处理负权重边**——因为贪心策略"dist 递增"会被负权边打破。

**算法流程**：

1. `dist[]` 初始化为 +∞，`dist[s] = 0`
2. 用**优先级队列**维护"未确定最短路的节点"
3. 取出 dist 最小的节点 v，确定 `dist[v]`
4. 对 v 的每条边 (v, u, w)：若 `dist[v] + w < dist[u]`，则更新 `dist[u] = dist[v] + w`
5. 重复 3-4 直到所有节点都确定

**复杂度**：

- 朴素 O(V²)
- 二叉堆优化 O((V + E) log V)
- 斐波那契堆 O(E + V log V)

**伪代码**：

```text
dijkstra(G, s):
    dist = [∞] * G.V
    dist[s] = 0
    pq = MinPriorityQueue()
    pq.push((0, s))
    while pq not empty:
        (d, v) = pq.pop()
        if d > dist[v]: continue
        for (u, w) in G.neighbors(v):
            if dist[v] + w < dist[u]:
                dist[u] = dist[v] + w
                pq.push((dist[u], u))
    return dist
```

### 2.2 Bellman-Ford / SPFA 算法

**核心思想**：和 Dijkstra 类似，但不限制"未确定节点"，**对所有边反复松弛**——能处理负权边，且能**检测负权重环**。

**算法流程**：

1. `dist[]` 初始化为 +∞，`dist[s] = 0`
2. 重复 V-1 次：遍历所有边 (u, v, w)，若 `dist[u] + w < dist[v]` 则更新 `dist[v]`
3. 再遍历一次所有边，若还能松弛 → 存在负权重环

**SPFA**（队列优化的 Bellman-Ford）：

- 用队列维护"待松弛的节点"
- 每次从队列取节点 v，松弛 v 的所有出边，若邻居 u 的 dist 被更新就把 u 入队
- **复杂度**：平均 O(E)，最坏 O(V × E)
- **优势**：常数小、能检测负环、在稀疏图上极快

**Bellman-Ford 复杂度**：O(V × E)

## 3. 点对点最短路径（A*）

**问题**：从起点 s 到**指定终点 t** 的最短路。

**A\* 思想**：Dijkstra + **启发式**——估计"目标在哪个方向"以加速搜索。

> [!tip] 关键优势
> A\* 充分利用了"已知终点"这一信息，比 Dijkstra **少扩展很多无用节点**。
> 启发式必须**可采纳（admissible）**——即估计值 ≤ 实际值，否则可能漏掉最优解。

**常用启发函数**：

- 曼哈顿距离（网格图）：`|dx| + |dy|`
- 欧氏距离：√(dx² + dy²)
- 对角线距离：max(|dx|, |dy|)

**伪代码**：

```text
a_star(G, s, t, h):
    g_score = [∞] * G.V       # 起点到 v 的实际距离
    f_score = [∞] * G.V       # g_score + h(v)
    g_score[s] = 0
    f_score[s] = h(s)
    open = MinPriorityQueue()
    open.push((f_score[s], s))
    while open not empty:
        v = open.pop().second
        if v == t: return g_score[v]
        for (u, w) in G.neighbors(v):
            tentative_g = g_score[v] + w
            if tentative_g < g_score[u]:
                g_score[u] = tentative_g
                f_score[u] = tentative_g + h(u)
                open.push((f_score[u], u))
    return -1
```

**复杂度**：在最坏情况下与 Dijkstra 相同（O(E log V)），但实际运行**常数小很多**。

## 4. 多源最短路径（Floyd）

**问题**：求**任意两节点**之间的最短路，输出 `dist[i][j]`。

**核心思想**：**动态规划**——`dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])`，枚举所有**中转点 k**。

**算法流程**：

```text
floyd(G):
    dist = G.adjacency_matrix（不连通处填 ∞，对角线 0）
    for k in 0..V-1:                  # 中转点
        for i in 0..V-1:
            for j in 0..V-1:
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist
```

**复杂度**：O(V³) 时间和 O(V²) 空间。

**优势**：

- 代码极短（三重循环）
- **能处理负权边**（但不能处理负权环）
- 适合 V ≤ 几百的小图

## 5. 负权重边的影响

### 5.1 为什么负权边会影响 Dijkstra？

Dijkstra 的贪心策略假设"dist 越大" → "路径越长"。**负权边打破了这个假设**：

- 假设 s 有邻居 a、b，`s→a = 3, s→b = 4`
- 没有负权边：`s→a = 3` 已经确定最小
- 有负权边：如果 `b→a = -10`，则 `s→b→a = -6 < 3`，前面的贪心错了

> **结论**：包含负权边时必须用 **Bellman-Ford / SPFA / Floyd**。

### 5.2 负权重环的破坏

如果图中存在**负权重环**（环上权重和 < 0），则**最短路问题无意义**——可以绕环无限圈使路径权无限小。

> **检测负环**：Bellman-Ford 第 V 次松弛仍能更新 → 存在负环。

## 6. 算法选型速查

| 场景 | 推荐算法 | 时间复杂度 | 能否负权 |
|------|----------|------------|----------|
| 单源、无负权 | **Dijkstra** | O((V+E) log V) | ❌ |
| 单源、有负权 | **SPFA** | 平均 O(E)，最坏 O(VE) | ✅ |
| 单源、需检测负环 | **Bellman-Ford** | O(VE) | ✅ |
| 点对点、有启发信息 | **A\*** | 通常 < Dijkstra | ❌（标准版） |
| 多源、V 较小 | **Floyd** | O(V³) | ✅ |
| 多源、V 较大 | **V 次 Dijkstra** | O(V(V+E) log V) | ❌ |

## 7. 完整对比

| 算法 | 思想 | 加权？ | 负权？ | 负环检测？ | 时间 |
|------|------|--------|--------|------------|------|
| **BFS** | 层序 | ❌无权 | N/A | N/A | O(V + E) |
| **Dijkstra** | BFS + 贪心 | ✅ | ❌ | ❌ | O((V+E) log V) |
| **SPFA** | BFS + 队列优化 | ✅ | ✅ | ✅ | 平均 O(E) |
| **Bellman-Ford** | DP | ✅ | ✅ | ✅ | O(VE) |
| **A\*** | Dijkstra + 启发 | ✅ | ❌ | ❌ | < Dijkstra |
| **Floyd** | DP（中转点） | ✅ | ✅ | ❌ | O(V³) |

## 8. 复杂度表

| 算法 | 时间 | 空间 | 适用 |
|------|------|------|------|
| BFS（无权） | O(V + E) | O(V) | 无权图最短路 |
| Dijkstra | O((V + E) log V) | O(V) | 单源、无负权 |
| SPFA | 平均 O(E) | O(V) | 单源、有负权 |
| Bellman-Ford | O(VE) | O(V) | 单源、负环检测 |
| A* | < Dijkstra | O(V) | 点对点、有启发 |
| Floyd | O(V³) | O(V²) | 多源、小图 |

## 9. 应用场景

- **地图导航**：Dijkstra / A*
- **网络路由**：OSPF 用 Dijkstra，BGP 用 Bellman-Ford 思想
- **社交网络**：计算"最短关系链"
- **生物信息**：序列比对、基因组组装
- **游戏 AI**：寻路（A* 经典场景）


## C++ 完整实现

> [!info] 📌 付费章节补全内容

### Dijkstra 单源最短路径（无负权图）

```cpp
#include <bits/stdc++.h>
using namespace std;

namespace dsa {

// Dijkstra 算法：单源最短路径，O((V+E) log V)
vector<int> dijkstra(vector<vector<pair<int,int>>>& graph, int src) {
    int n = graph.size();
    vector<int> dist(n, INT_MAX);
    priority_queue<pair<int,int>, vector<pair<int,int>>, greater<>> pq;

    dist[src] = 0;
    pq.push({0, src});

    while (!pq.empty()) {
        auto [d, u] = pq.top(); pq.pop();
        if (d > dist[u]) continue;  // 跳过旧条目
        for (auto [v, w] : graph[u]) {
            if (dist[u] + w < dist[v]) {
                dist[v] = dist[u] + w;
                pq.push({dist[v], v});
            }
        }
    }
    return dist;
}

// Floyd 多源最短路径（任意两点，O(V³)）
vector<vector<int>> floyd(vector<vector<int>>& graph) {
    int n = graph.size();
    const int INF = 1e9;
    vector<vector<int>> dist(n, vector<int>(n, INF));
    for (int i = 0; i < n; i++) {
        dist[i][i] = 0;
        for (int j = 0; j < n; j++) {
            dist[i][j] = graph[i][j];
        }
    }
    // 三重循环：k 是中转点
    for (int k = 0; k < n; k++) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
            }
        }
    }
    return dist;
}

} // namespace dsa
```

### 算法选择

| 场景 | 推荐算法 | 复杂度 |
|------|----------|--------|
| 单源、无负权 | Dijkstra + 堆 | O((V+E) log V) |
| 单源、有负权 | Bellman-Ford | O(V·E) |
| 任意两点、稠密图 | Floyd | O(V³) |
| 任意两点、稀疏图 | 跑 N 次 Dijkstra | O(N·E log V) |

## 下一章

→ [[38-eulerian-graph|欧拉图一笔画游戏]]

## 相关章节

- [[34-graph-traverse-basic|图遍历]] — Dijkstra / SPFA / A* 都是 BFS 的扩展
- [[36-graph-minimum-spanning-tree|最小生成树]] — 另一类图论核心问题
- [[22-binary-heap-implement|堆 / 优先级队列]] — Dijkstra / Prim / A* 的核心工具
- [[44-quick-sort|快速排序]] — Floyd 中"按中转点枚举"思想
- [[35-use-case-of-dfs-bfs|DFS/BFS 应用]] — 无权图 BFS 最短路模板
