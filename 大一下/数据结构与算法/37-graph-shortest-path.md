---
title: 图结构最短路径算法概览
tags: [labuladong, 图, 算法, 数据结构与算法, 付费章节]
order: 37
prerequisites: [34-graph-traverse-basic]
group: 图 / 算法
paywall: true
source: labuladong.online
url: https://labuladong.online/zh/algo/data-structure-basic/graph-shortest-path/
---


前置知识

阅读本文前，你需要先学习：

图结构基础及通用代码实现

图结构的 DFS/BFS 遍历

一句话总结

Dijkstra 算法和 A* 算法是
图的 BFS 遍历
 的拓展，可以处理不包含负权重的单源最短路径问题。

SPFA 算法（基于队列的 Bellman-Ford 算法）是
图的 BFS 遍历
 的拓展，可以处理包含负权重的单源最短路径问题。

Floyd 算法是
动态规划
 的应用，可以处理多源最短路径问题。

由 BFS 算法扩展而来

不能处理负权重边

Dijkstra 算法

由 BFS 算法扩展而来

可以处理负权重边

基于队列的 Bellman-Ford 算法

（SPFA 算法）

可以处理负权重边

朴素 Bellman-Ford 算法

单源最短路径

由 Dijkstra 算法扩展而来

不能处理负权重边

A* 算法

点对点最短路径

动态规划算法

可以处理负权重边

Floyd 算法

多源最短路径

最短路径问题

初学者不要觉得图论算法有多难，因为它们都是基于简单的算法思想扩展出来的。你把基本的二叉树层序遍历玩明白，自己都能发明出来这些算法，没啥了不起的。

考虑到目前处在基础知识章节，所以本文并不会详细讲解每种算法的完整代码，具体的代码实现会安排在之后的章节。

本文的重点在这些算法的关键原理、适用场景，以及这些高级算法和基础知识的联系，帮助初学者对图结构的最短路径算法有一个整体的认识。

## 最短路径问题概览

最短路径问题在生活中应用广泛，比方说计算最小成本、最短路径长度、最少时间等。

在算法中，我们一般把这类问题抽象成计算
加权图
 中的最小路径权重。为了方便表述，在本文中「最短路径」和「最小路径权重和」是等价的。

最短路径问题大致可以分为「单源最短路径」和「多源最短路径」两类，下面会介绍几个经典的算法。

### 单源最短路径

所谓单源最短路径，就是让你计算从某个起点出发，到其他所有顶点的最短路径。

比方说一幅图中有 n 个节点，编号为 0, 1, 2, ..., n-1，让你计算从 2 号节点到其他节点的最短路径，这就是单源最短路径问题。

单源最短路径算法最终得到的输出应该是一个一维数组 distTo，distTo[i] 表示从起点到节点 i 的最短路径长度。

比较有代表性的单源最短路径算法有：

1、Dijkstra 算法，其本质是 BFS 算法 + 贪心思想，效率较高，但是不能处理带有负权重的图。

2、基于队列的 Bellman-Ford 算法，其本质也是 BFS 算法，可以处理带有负权重的图，但效率比 Dijkstra 算法低。

### 点对点最短路径

很多算法题中不需要我们计算起点到所有其他节点的最短路径，仅需要计算从起点 src 到某一个目标节点 dst 的最短路径。这类问题可以称为点对点最短路径问题。

一般来说，点对点最短路径问题可以视为单源最短路径问题的特例，你可以从 src 开始执行单源最短路径算法，当算出到达 dst 的最短路径时提前结束算法。

但是下面将介绍一种专门处理点对点问题的算法：
A* 算法
（A Star Algorithm）。

我经常讲，算法的本质是穷举，你想要提高穷举的效率，就得尽可能充分地利用信息。点对点最短路径问题（已知起点和终点）比单源最短路径问题（已知起点）多了终点信息，所以完全有可能利用这个信息来提高算法的效率。

比方说，如果我们知道终点在起点的右下方，那么我们有理由猜测：应该优先向右下方搜索，可能可以更快地到达终点。

A* 算法的关键就在这里：它能够充分利用已知信息，有方向性地进行搜索，更快地找到终点。我们称这类算法为启发式搜索算法（Heuristic Search Algorithm）。

但是请注意，这个猜测只是经验法则，并不一定总是正确。比方说右下方可能都是死路，偏偏就得经过左上角绕个大弯才能到达终点。

所以启发式算法需要合理设置启发函数（Heuristic Function），在经验法则和实际情况中找到平衡，确保在经验法则失效时，算法的效率也不会太差。

### 多源最短路径

所谓多源最短路径，就是让你计算任意两节点之间的最短路径。

比方说一幅图中有 n 个节点，编号为 0, 1, 2, ..., n-1，让你计算所有节点之间的最短路径，这就是多源最短路径问题。

多源最短路径算法最终得到的输出应该是一个二维数组 dist，dist[i][j] 表示从节点 i 到节点 j 的最短路径长度。

最有代表性的是 Floyd 算法，其本质是动态规划算法。

理论上，我们对所有节点都调用一次单源最短路径算法，就可以得到多源最短路径的解。

但具体实现时，要根据图结构的特点来选择。有些场景用 Floyd 这种多源最短路径算法效率更高，有些场景多次调用 Dijkstra 这种单源最短路径算法效率更高。后面讲到这些算法的复杂度时，你就能理解了。

### 负权重边的影响

在计算最短路径时，需要着重注意的是这幅图是否包含负权重边；一旦包含负权重边，一定要检查是否包含负权重环。

为啥负权重边会影响最短路径算法呢？因为负权重边会让问题变得复杂。举个最简单的例子就能直观地理解了：

比方说我们现在站在起点 s 上，相邻节点有 a 和 b，s->a 权重为 3，s->b 权重为 4。

如果这幅图不存在负权重边，那么根据上述信息，我就已经可以确定 s 到 a 的最短路径是 s->a，权重和为 3。因为你从 s->b 这条路径走出去，绕一圈到达 a 的路径权重和肯定是大于 4 的，不可能比 3 还小。

但如果这幅图存在负权重边，那可就不一定了。因为可能出现负权重边呀，比方说 b->a 的权重为 -10，那么从 s->b->a 的路径权重和为 -6，比 s->a 的路径权重和 3 还小。

想让 Dijkstra 这类包含贪心思想的算法成立，需要一个前提：它假设随着经过的边的数量增加，路径权重和一定也会增加。但负权重边的出现打破了这一假设，导致算法失效。

如果图中存在负权重环，最短路径问题就没有意义了。比方说 s 到 a 的路径上存在负权重环，那么你可以在这个负权重环上无限转圈，使得路径权重和无限减小下去。

常见最短路径算法中，Dijkstra 算法和 A* 算法不能处理含有负权重边的图，Floyd 算法和 Bellman-Ford 算法可以处理负权重边，Bellman-Ford 算法常用来检测负权重环。

下面，我们介绍这些算法的核心原理。


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

## 关联章节

- [[34-graph-traverse-basic|图结构的 DFS/BFS 遍历]]
