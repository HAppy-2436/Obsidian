---
title: Union Find 并查集原理
tags: [labuladong, 高级树, 数据结构与算法, 付费章节]
order: 30
prerequisites: [02-array-basic]
group: 高级树
paywall: true
source: labuladong.online
url: https://labuladong.online/zh/algo/data-structure-basic/union-find-basic/
---


前置知识

阅读本文前，你需要先学习：

二叉树基础及常见类型

图结构基础及通用代码实现

一句话总结

并查集（Union Find）结构是  二叉树结构  的衍生，用于高效解决无向图的连通性问题，可以在  O(1) 时间内合并两个连通分量，在  O(1) 时间内查询两个节点是否连通，在  O(1) 时间内查询连通分量的数量。

并查集算法有几种优化方法，可视化面板都做了支持。下面展示一个未经优化的并查集实现，最终多叉树几乎退化成单链表，导致算法效率降低。对于这个问题的优化思路和可视化展示，在下文中会详细介绍。

算法可视化

本文将介绍什么是图的动态连通性问题，以及为什么并查集（Union Find）算法能够高效解决动态连通性问题。

本文会结合  可视化面板  直观展示 Union Find 算法的核心原理，以及几种优化思路的效果。

考虑到这是基础章节，本文不涉及算法代码的实现细节。具体的代码实现和算法题的运用放在后面的  Union Find 算法实现及应用  和  并查集经典习题  章节中，建议初学者按照目录顺序循序渐进地学习。

## 动态连通性及术语

图论算法中专业术语比较多，我就用一个简单的例子来介绍几个专业术语。

比如下面这个例子，其中有 10 个节点，分别用 0~9 标记，虽然其中没有边，但它依然是一个图结构：

我们可以说这个图结构中，有 10 个「连通分量」，每个节点自身都是一个连通分量，因为它们自成一派，没有和其他节点相连。

现在将其中的一些节点进行「连接操作」，比如连接节点 0,1 和 1,2：

此时，图结构中的节点 0,1,2 之间就连通了，它们三个节点共同构成了一个连通分量，我们可以说这三个节点是「连通」的。

同时，这个图结构中的连通分量的数量从 10 减少到了 8，因为连接操作将 0,1,2 三个连通分量合并成了一个。

连通关系的性质

1、自反性：节点 p 和 p 自身是连通的。

2、对称性：如果节点 p 和 q 连通，那么 q 和 p 也连通。

3、传递性：如果节点 p 和 q 连通，q 和 r 连通，那么 p 和 r 也连通。

判断这种「等价关系」非常实用，比如说编译器判断同一个内存对象的不同变量引用，比如社交网络中的朋友圈计算等等。

那么动态连通性问题就是说，给你输入一个图结构，然后进行若干次「连接操作」，同时可能会查询任意两个节点是否「连通」，或者查询当前图中有多少个「连通分量」。

我们的目标是设计一种数据结构，在尽可能小的时间复杂度下完成连接操作和查询操作。

## 为什么需要并查集算法

并查集（Union Find）结构提供如下 API：

```
class UF {  // 初始化并查集，包含 n 个节点，时间复杂度 O(n)  public UF(int n);

  // 连接节点 p 和节点 q，时间复杂度 O(1)  public void union(int p, int q);

  // 查询节点 p 和节点 q 是否连通（是否在同一个连通分量内），时间复杂度 O(1)  public boolean connected(int p, int q);

  // 查询当前的连通分量数量，时间复杂度 O(1)  public int count(); }
```

其中 union 方法用于连接两个节点，connected 方法用于查询两个节点是否连通，count 方法用于查询当前图中的连通分量数量。它们都可以在  O(1) 时间内完成。

O(1) 的时间复杂度是最牛逼的，假设你没学过并查集算法，你应该如何实现上述几个方法呢？

也不是完全没办法，比如  图结构基础及通用代码实现  中已经介绍了图结构邻接表/邻接矩阵的代码实现，这个 union 方法其实就是在图中添加一条无向边，时间复杂度可以做到  O(1)。

这个 connected 方法怎么实现呢？你是不是想说，去查一下邻接表/邻接矩阵，看看这两个节点是否相连就行了？

不对，别忘了上面讲的「连通」的性质，其中有有一条是「传递性」：如果节点 p 和 q 连通，q 和 r 连通，那么 p 和 r 也连通。

你单纯去查邻接表/邻接矩阵，只能判断两个节点是否直接相连，而无法处理这种传递的连通关系。

所以，要想实现 connected(a, b)，我们只能使用  图结构的 DFS/BFS 遍历算法 ，从 a 节点开始遍历所有可达的节点，看看 b 节点是否在其中，才能判断 a,b 两个节点是否连通。

这样的话，connected 方法的最坏时间复杂度就是图遍历的复杂度  O(V+E)，其中

V 是节点数量，

E 是边数量。

接下来，count 方法如何实现呢？

还得依赖  图结构的 DFS/BFS 遍历算法 ，但是更麻烦。

你得用 BFS/DFS 遍历整幅图，将所有节点分类到不同的连通分量中，最后统计连通分量的数量。这个过程的时间复杂度是  O(V+E)。

所以说并查集算法非常巧妙，它不仅可以在  O(1) 时间内完成上述操作，而且它根本不需要真的用邻接表/邻接矩阵构造图结构，只需要一个数组就可以了。

下面具体介绍。


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

## 关联章节

- [[02-array-basic|数组（顺序存储）的原理]]
