---
title: Union Find 并查集原理
tags:
  - 并查集
  - Union Find
  - 连通性
  - 图
  - 高级树
order: 30
prerequisites:
  - "[[02-array-basic]]"
group: 高级树
subgroup: null
paywall: false
source: https://labuladong.online/zh/algo/data-structure-basic/union-find-basic/
---

# Union Find 并查集原理

## 学习目标

- 理解「动态连通性」问题的定义
- 理解并查集（Union Find）的核心思想：用一个 **森林** 表示集合
- 掌握并查集的两个核心 API：`union(p, q)` 和 `connected(p, q)`
- 理解并查集的两种优化：**路径压缩** 和 **按秩合并**
- 能够手写一个完整的并查集 C++ 实现
- 熟悉并查集的常见应用：朋友圈、最小生成树 Kruskal、岛屿问题

## 一句话总结

并查集（Union Find）是 [[23-binary-tree-basic|树形结构]] 的衍生，专门用于解决 **动态连通性问题**：它用一棵「父指针森林」表示若干集合，在 **O(1)** 平均时间内完成两个节点的 **合并（union）** 和 **连通判断（connected）**，是图论算法（Kruskal、岛屿问题）的基础工具。

## 前置知识

阅读本文前，你需要先学习：

- [[23-binary-tree-basic|二叉树基本概念及特殊二叉树]]
- [[02-array-basic|数组（顺序存储）的原理]]
- [[32-graph-terminology|图的基本术语]]（推荐）

## 1. 什么是动态连通性

### 1.1 术语引入

举例：一个图有 10 个节点 `0..9`，初始时它们 **互不相连**：

- 此时有 **10 个连通分量**，每个节点自己是一个分量
- 之后连接 `0-1`、`1-2`，`0, 1, 2` 就合并为 **1 个分量**
- 当前图有 8 个分量

「**连通关系**」是图论中的 **等价关系**，具有三个性质：

1. **自反性**：`p` 和 `p` 自身连通
2. **对称性**：`p` 和 `q` 连通 ⇒ `q` 和 `p` 连通
3. **传递性**：`p` 和 `q` 连通、`q` 和 `r` 连通 ⇒ `p` 和 `r` 连通

判断这种「等价关系」在现实中非常有用：编译器判断「同一内存对象的不同引用」、社交网络的「朋友圈」计算、路由表的「网络分区」等等。

### 1.2 动态连通性问题

**输入**：一个图结构 + 若干操作
**操作类型**：
- **union(p, q)**：连接节点 `p` 和 `q`（添加一条无向边）
- **connected(p, q)**：查询 `p` 和 `q` 是否连通
- **count()**：查询当前图中有多少个连通分量

**目标**：用尽量小的时间复杂度完成这些操作。

## 2. 为什么需要并查集

如果用 [[33-graph-basic|图的邻接表 / 邻接矩阵]]：

- **union(p, q)**：O(1)，添加一条无向边即可
- **connected(p, q)**：需要从 `p` 出发 [[34-graph-traverse-basic|DFS / BFS]] 遍历，看 `q` 是否可达 ⇒ 最坏 O(V + E)
- **count()**：必须用 DFS / BFS 遍历整张图，把节点分类到不同连通分量 ⇒ O(V + E)

并查集可以做到 **O(1)** 完成上述所有操作，**根本不需要**真的用邻接表 / 邻接矩阵构造图，只需要 **一个数组** 即可。

## 3. 并查集的核心思想

### 3.1 用「父指针森林」表示集合

并查集维护一个 **`parent` 数组**：

- `parent[i]` 表示节点 `i` 的「父节点」
- 初始时 `parent[i] = i`，每个节点自成一个集合（自己是自己的根）
- `union(p, q)` 时，把 `p` 的根指向 `q` 的根（或者反过来），于是两个集合合并

举例：`union(1, 2)` 之后，假设 `2` 当根：

```
1 → 2
```

再 `union(2, 3)` 之后：

```
1 → 2 → 3
```

再 `union(0, 1)` 之后：

```
0 → 1 → 2 → 3
```

这就是一棵「多叉树」：每个节点的 `parent` 指向它的父亲，树根就是 **集合的标识**。

判断 `connected(p, q)` 很简单——**从 `p` 一路找父到根，再从 `q` 一路找父到根，看根是否相同**。如果根相同，就在同一个集合里。

### 3.2 朴素实现的复杂度问题

朴素实现中，每次 `find(p)` 都要沿着 `parent` 链一路上溯到根。如果树退化成链表（极端情况），单次 `find` 的复杂度是 O(N)。

下面这张图演示了**未优化的并查集**：

```
1 → 2 → 3 → 4 → 5    (一条链，深度 5)
```

**5 次 find 操作** 最坏要访问 5 层树。

两种优化可以解决：
1. **路径压缩**（Path Compression）：`find` 时把所有经过的节点直接指向根，下次再 `find` 就 O(1)
2. **按秩合并**（Union by Rank / Size）：`union` 时总是把 **矮树接到高树** 下，避免链状结构

这两个优化都做之后，**单次操作的均摊复杂度接近 O(1)**，准确说是 `O(α(N))`（α 是 Ackermann 函数的反函数，增长极慢，实际就是 O(1)）。

## 4. 并查集的核心 API

```text
class UnionFind:
    UnionFind(int n)              // 初始化 n 个节点的并查集
    void union(int p, int q)      // 合并 p 和 q 所在的集合
    boolean connected(int p, int q) // 查询 p 和 q 是否连通
    int find(int p)               // 找 p 的根（集合标识）
    int count()                   // 返回连通分量数量
```

## 5. 路径压缩 + 按秩合并的 C++ 实现

```cpp
#include <bits/stdc++.h>
using namespace std;

namespace dsa {

// 完整版并查集：路径压缩 + 按秩合并
class UnionFind {
public:
    UnionFind(int n) : parent(n), rank_(n, 0), cnt(n) {
        iota(parent.begin(), parent.end(), 0);  // parent[i] = i
    }

    // 找 p 的根（带路径压缩）
    int find(int p) {
        if (parent[p] == p) return p;
        return parent[p] = find(parent[p]);  // 递归压缩
    }

    // 合并 p 和 q 所在的集合（按秩合并）
    void unite(int p, int q) {
        int rootP = find(p), rootQ = find(q);
        if (rootP == rootQ) return;  // 已经在同一集合
        // 把矮树接到高树
        if (rank_[rootP] < rank_[rootQ])       parent[rootP] = rootQ;
        else if (rank_[rootP] > rank_[rootQ])  parent[rootQ] = rootP;
        else { parent[rootQ] = rootP; ++rank_[rootP]; }
        --cnt;
    }

    bool connected(int p, int q) { return find(p) == find(q); }
    int  count() const          { return cnt; }

private:
    vector<int> parent;   // parent[i] = i 的父节点
    vector<int> rank_;    // 近似树高（只增不减）
    int cnt;              // 当前连通分量数量
};

} // namespace dsa

int main() {
    using namespace dsa;
    UnionFind uf(10);
    cout << "初始分量数: " << uf.count() << endl;     // 10

    uf.unite(0, 1);
    uf.unite(1, 2);
    cout << "合并 0-1, 1-2 后分量数: " << uf.count() << endl;  // 8

    cout << "0 和 2 连通: " << uf.connected(0, 2) << endl;     // 1
    cout << "0 和 3 连通: " << uf.connected(0, 3) << endl;     // 0

    uf.unite(3, 4);
    uf.unite(2, 4);   // 0/1/2/3/4 现在都在同一集合
    cout << "合并 0/1/2/3/4 后: " << uf.count() << endl;        // 6
    cout << "0 和 4 连通: " << uf.connected(0, 4) << endl;      // 1
    return 0;
}
```

**输出**：

```text
初始分量数: 10
合并 0-1, 1-2 后分量数: 8
0 和 2 连通: 1
0 和 3 连通: 0
合并 0/1/2/3/4 后: 6
0 和 4 连通: 1
```

> [!tip] 路径压缩详解
> `parent[p] = find(parent[p])` 这一行的巧妙之处：它把 `p` 的父节点 **直接** 设为根，下次再 `find(p)` 就一步到位。反复调用几次后，整棵树会被「压平」到几乎只剩 2 层。

> [!tip] 按秩合并详解
> `rank_[root]` 是「近似树高」。合并时把 `rank` 小的根接到 `rank` 大的根下面，避免链状结构。**理论上**这是反 Ackermann 函数复杂度保证的关键，实际工程中可以省略（只做路径压缩就足够）。

## 6. 复杂度分析

| 操作 | 朴素复杂度 | 路径压缩 | 路径压缩 + 按秩合并 |
|------|-----------|----------|-------------------|
| find | O(N) | O(log N) 平均 | O(α(N)) ≈ O(1) |
| union | O(N) | O(log N) 平均 | O(α(N)) ≈ O(1) |
| connected | O(N) | O(log N) 平均 | O(α(N)) ≈ O(1) |
| 空间 | O(N) | O(N) | O(N) |

> [!info] α(N) 是「Ackermann 函数的反函数」
> `A(n, n)` 增长极其缓慢，N = 宇宙原子数时，α(N) 仍然 < 5。所以工程上并查集就是 O(1)。

## 7. 并查集的应用场景

### 7.1 朋友圈 / 社交网络

- 每个人是节点
- `union(u, v)` 表示「u 和 v 是朋友」
- `connected(u, v)` 查询「u 和 v 是否是朋友（直接或间接）」

### 7.2 最小生成树 Kruskal 算法

Kruskal 是 [[36-graph-minimum-spanning-tree|最小生成树]] 的算法之一：
- 把所有边按权重排序
- 从小到大遍历每条边，如果这条边 **不会让图形成环**（即两端节点已经连通），就加入 MST
- 关键判断「是否会形成环」用并查集的 `connected`：O(1)

### 7.3 岛屿问题

[[35-use-case-of-dfs-bfs|DFS / BFS 经典题]]：[200. 岛屿数量](https://leetcode.cn/problems/number-of-islands/)
- 把二维网格的每个格子当节点
- `union(相邻的 1 格子)` 把相邻的陆地合并
- 最终 `count()` 就是岛屿数

### 7.4 网络连通性 / 冗余连接

[684. 冗余连接](https://leetcode.cn/problems/redundant-connection/)：
- 给你一棵树加一条边，问是哪条边造成环
- 遍历边，对每条边 `union(u, v)`，如果发现 `connected(u, v)` 已经为 true，说明这条边是冗余的

### 7.5 离线 LCA / Tarjan 算法

进阶应用：处理大量「求两个节点的最近公共祖先」的离线查询

### 7.6 LeetCode 经典题清单

- [200. 岛屿数量](https://leetcode.cn/problems/number-of-islands/)：经典入门
- [547. 省份数量](https://leetcode.cn/problems/number-of-provinces/)：基础 union
- [684. 冗余连接](https://leetcode.cn/problems/redundant-connection/)
- [721. 账户合并](https://leetcode.cn/problems/accounts-merge/)
- [990. 等式方程的可满足性](https://leetcode.cn/problems/satisfiability-of-equality-equations/)：带反集
- [1061. 按字典序排列最小的等效字符串](https://leetcode.cn/problems/lexicographically-smallest-equivalent-string/)
- [1579. 保证图可完全遍历](https://leetcode.cn/problems/find-a-good-edge-set-in-a-tree/)

## 8. 并查集 vs BFS / DFS

| 维度 | 并查集 | BFS / DFS |
|------|--------|-----------|
| 适用场景 | 动态连通性（边陆续加入） | 静态连通性（边已给定） |
| `connected(p, q)` | O(1) 平均 | O(V + E) |
| `count()` | O(1) | O(V + E) 需遍历整图 |
| 处理「加权图」 | 只能用 [[37-graph-shortest-path|Dijkstra]] 等 | 可以 |
| 空间 | O(N) | O(V + E) |

> [!tip] 一句话选择
> - 边 **陆续加入**（动态）→ 并查集
> - 边 **一次性给定**（静态）→ BFS / DFS
> - 需要 **最短路** → Dijkstra / BFS

## 下一章

→ [[31-rbtree-basic|红黑树的自平衡原理及可视化]]

## 相关章节

- [[23-binary-tree-basic|二叉树基础]] — 并查集的逻辑结构是「多叉树」
- [[32-graph-terminology|图的基本术语]] — 连通性的图论基础
- [[34-graph-traverse-basic|图的 DFS / BFS]] — 静态连通性用 DFS / BFS
- [[36-graph-minimum-spanning-tree|最小生成树]] — Kruskal 用到并查集
- [[13-hashmap-basic|哈希表]] — 另一个「集合 + 关系」的数据结构
