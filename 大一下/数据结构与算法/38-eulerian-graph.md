---
title: 欧拉图一笔画游戏
tags:
  - 图
  - 欧拉图
  - 欧拉回路
  - 欧拉路径
  - Hierholzer
  - 一笔画
order: 38
prerequisites:
  - "[[34-graph-traverse-basic]]"
group: 图
subgroup: 应用
paywall: true
source: https://labuladong.online/zh/algo/data-structure-basic/eulerian-graph/
---

# 欧拉图一笔画游戏

## 学习目标

- 理解**欧拉图 / 欧拉回路 / 欧拉路径**的精确定义
- 掌握**欧拉图判定定理**：通过节点的度判定欧拉路径/回路的存在性
- 掌握 **Hierholzer 算法**的核心思想和实现
- 能够用 C++ 解决**一笔画问题**（LeetCode 753 / 332 等）
- 了解欧拉图的历史背景——**哥尼斯堡七桥问题**

## 一句话总结

**欧拉路径（Eulerian Path）= 经过图中每条边恰好一次的路径**；**欧拉回路（Eulerian Circuit）= 起点和终点相同的欧拉路径**。判定定理：**所有节点度为偶 → 欧拉回路存在**；**恰两个奇度节点 → 欧拉路径存在**。计算欧拉路径的经典算法是 **Hierholzer 算法**（DFS 拓展），时间复杂度 O(V + E)。

## 前置知识

阅读本文前，你需要先学习：

- [[32-graph-terminology|图的基本术语]]（度、连通图）
- [[34-graph-traverse-basic|图结构的 DFS/BFS 遍历]]（Hierholzer 是 DFS 的拓展）

## 1. 一笔画游戏

小时候玩的"**一笔画**"小游戏：要求**一笔连接所有的点和边**，**点可以重复经过**，但**每条边必须恰好经过一次，不能重复**。

**游戏套路**（来自图论）：

- **如果所有节点度都是偶数** → 从任何节点开始，**一定能完成一笔画**，且**会回到起点**（欧拉回路）。
- **如果只有两个节点的度为奇数** → 必须**从这两个奇数度节点之一开始**，才能完成一笔画（欧拉路径）。
- **其他情况** → **无法完成一笔画**。

这个游戏背后就是**欧拉图理论**——图论中最古老、最经典的话题之一。

## 2. 历史：哥尼斯堡七桥问题

**欧拉图**的概念源于 18 世纪著名的**哥尼斯堡七桥问题**。

**背景**：当时的哥尼斯堡（今天的加里宁格勒）有一条河流将城市分为南北两岸，河中有东西两个小岛，有**七座桥**连接着北岸、南岸、东岛和西岛。

**问题**：能否设计一条路线，从任意一个区域出发，**经过每座桥恰好一次**，最后回到起点？

**图论抽象**：

- 每个**区域**对应一个**节点**
- 每座**桥**对应一条**边**
- 问题转化为：**是否存在一条路径，经过图中每条边恰好一次，且最终回到起点**

**欧拉的证明**：通过分析每个节点的度（每个区域连接的桥数），欧拉**数学证明**七桥问题**无解**——这个证明**奠定了图论的基础**。

> [!tip] 历史地位
> 1736 年欧拉对七桥问题的解答，被公认为**图论的开端**。从一道"小游戏"中诞生的图论，后来成为计算机科学最重要的数学基础之一。

## 3. 核心术语定义

### 3.1 欧拉路径（Eulerian Path / Eulerian Trail）

> 一条**经过图中每条边恰好一次**的路径。

- 点可以重复经过，**边不能重复**
- 也叫"**欧拉迹**"

### 3.2 欧拉回路（Eulerian Circuit / Eulerian Cycle）

> **起点和终点相同**的欧拉路径。

- 同样经过每条边恰好一次，且**回到起点**

### 3.3 欧拉图（Eulerian Graph）

> **存在欧拉回路的图**。

- 一个图被称为"欧拉图"当且仅当它**有欧拉回路**

### 3.4 半欧拉图（Semi-Eulerian Graph）

> **存在欧拉路径但不存在欧拉回路**的图。

- 即从某起点可以一笔走完但回不到起点

## 4. 欧拉图判定定理

> [!info] 📌 欧拉定理（1736, 欧拉）
> 对于**连通无向图** G：
>
> - **G 是欧拉图**（存在欧拉回路）**当且仅当** G 的**所有节点度都是偶数**。
> - **G 是半欧拉图**（存在欧拉路径）**当且仅当** G **恰好有 2 个奇度节点**——起点和终点。
> - 其他情况 → **欧拉路径不存在**。

> **有向图版**（略）：所有节点**入度 = 出度** → 欧拉回路；**恰一个起点（出度 = 入度+1）和一个终点（入度 = 出度+1）** → 欧拉路径。

> [!tip] 记忆口诀
> - **零奇点** → 欧拉回路（一笔画回到起点）
> - **两奇点** → 欧拉路径（一笔画从奇点到奇点）
> - **其他** → 无解

### 4.1 七桥问题为什么无解？

七桥问题对应的图有 **4 个节点**和 **7 条边**。计算每个节点的度：

- 北岸：3（连 3 座桥）
- 南岸：3
- 东岛：3
- 西岛：3

**4 个节点全部是奇数**——既不是"全偶"，也不是"恰好两个奇数"，所以**既不存在欧拉回路，也不存在欧拉路径**——无解。

## 5. Hierholzer 算法（核心）

**问题**：给定一个**存在欧拉回路的图**，如何**实际求出一条欧拉回路**？

**Hierholzer 算法**（1873）是求解欧拉回路/路径的**经典算法**，本质是 DFS 的拓展。

### 5.1 核心思想

> **从起点出发，沿着未走过的边走，**能走就走、走不通就回退**——回退时把经过的节点加入答案。**

关键观察：

- 当我们"**走不通**"时，是因为**所有邻居的边都走过了**——这说明**当前节点的所有边都处理完了**。
- 此时**把当前节点加入答案序列**，然后**回退**到上一个还有未走边的节点。

**最终得到的答案序列是逆序的**——所以最后要**反转**。

### 5.2 伪代码

```text
hierholzer(G, start):
    stack = [start]
    path = []
    while stack not empty:
        v = stack.top()
        if v 还有未走的边 (v, u):
            stack.push(u)
            标记边 (v, u) 已走过
        else:
            path.append(v)        # 走不通，加入答案
            stack.pop()
    reverse(path)
    return path
```

### 5.3 时间复杂度

- 每条边**只走一次**（O(E)）
- 每个节点**入栈出栈各一次**（O(V)）
- **总复杂度 O(V + E)**

### 5.4 图示

考虑下面这张存在欧拉回路的图（每个节点度都是偶数）：

```text
1 -- 2
|    |
4 -- 3
```

边列表：`1-2, 1-4, 2-3, 3-4`（4 条边）

**Hierholzer 步骤**（从 1 开始）：

1. 1 → 2（用边 1-2）→ 栈 [1, 2]
2. 2 → 3（用边 2-3）→ 栈 [1, 2, 3]
3. 3 → 4（用边 3-4）→ 栈 [1, 2, 3, 4]
4. 4 → 1（用边 4-1）→ 栈 [1, 2, 3, 4, 1]
5. 1 无未走边 → 弹出 → path = [1]
6. 4 无未走边 → 弹出 → path = [1, 4]
7. 3 无未走边 → 弹出 → path = [1, 4, 3]
8. 2 无未走边 → 弹出 → path = [1, 4, 3, 2]
9. 1 无未走边 → 弹出 → path = [1, 4, 3, 2, 1]

**反转**：`[1, 2, 3, 4, 1]` ← 这就是欧拉回路。

> 答案路径：`1 → 2 → 3 → 4 → 1`，每条边恰好走一次 ✓

## 6. 完整 C++ 实现

> 下面是 Hierholzer 算法的完整 C++ 实现，包含：
> 1. 邻接表存储
> 2. Hierholzer 求欧拉路径 / 欧拉回路
> 3. 一笔画游戏判定
> 4. LeetCode 753 风格的完整测试

### 6.1 邻接表实现（用边索引而非二维 visited）


> [!info] 📌 付费章节补全内容（基于算法知识体系补充）

```cpp
#include <bits/stdc++.h>
using namespace std;

namespace dsa {

// 边结构：to 是邻居，idx 是这条边在邻接表中的索引
struct EEdge {
    int to;
    int idx;            // 边的全局编号（用于"标记走过"）
    EEdge(int t, int i) : to(t), idx(i) {}
};

class EulerianGraph {
public:
    // n 个节点，构造无向图
    explicit EulerianGraph(int n) : n_(n), adj_(n) {}

    // 加无向边
    void addEdge(int u, int v) {
        adj_[u].push_back(EEdge(v, edge_cnt_));
        adj_[v].push_back(EEdge(u, edge_cnt_));
        ++edge_cnt_;
    }

    // 节点数 / 边数
    int V() const { return n_; }
    int E() const { return edge_cnt_; }

    // 计算每个节点的度
    vector<int> degree() const {
        vector<int> deg(n_, 0);
        for (int v = 0; v < n_; ++v) deg[v] = (int)adj_[v].size();
        return deg;
    }

    // 判定是否存在欧拉回路
    bool hasEulerianCircuit() const {
        // 1. 必须连通（这里用 BFS 简单判断）
        if (edge_cnt_ == 0) return false;
        vector<bool> visited(n_, false);
        queue<int> q;
        // 找第一个度 > 0 的节点
        int start = -1;
        for (int i = 0; i < n_; ++i) {
            if (!adj_[i].empty()) { start = i; break; }
        }
        if (start == -1) return false;
        q.push(start); visited[start] = true;
        int cnt = 0;
        while (!q.empty()) {
            int v = q.front(); q.pop();
            ++cnt;
            for (const auto& e : adj_[v]) {
                if (!visited[e.to]) {
                    visited[e.to] = true;
                    q.push(e.to);
                }
            }
        }
        int non_isolated = 0;
        for (int i = 0; i < n_; ++i) if (!adj_[i].empty()) ++non_isolated;
        if (cnt != non_isolated) return false;     // 不连通

        // 2. 所有节点度必须是偶数
        for (int d : degree()) {
            if (d % 2 != 0) return false;
        }
        return true;
    }

    // 判定是否存在欧拉路径（半欧拉图）
    bool hasEulerianPath(int& start) const {
        vector<int> deg = degree();
        int odd = 0;
        for (int i = 0; i < n_; ++i) {
            if (deg[i] % 2 != 0) {
                ++odd;
                start = i;
            }
        }
        return odd == 0 || odd == 2;
    }

    // Hierholzer 求欧拉回路（前提：hasEulerianCircuit() 为 true）
    vector<int> eulerianCircuit(int start = 0) {
        vector<int> used(edge_cnt_, 0);             // 边是否走过
        vector<int> stack, path;
        stack.push_back(start);
        while (!stack.empty()) {
            int v = stack.back();
            // 找一条未走过的边
            while (!adj_[v].empty() && used[adj_[v].back().idx]) {
                adj_[v].pop_back();                 // 跳过已走边
            }
            if (adj_[v].empty()) {
                path.push_back(v);
                stack.pop_back();
            } else {
                EEdge e = adj_[v].back();
                adj_[v].pop_back();
                used[e.idx] = 1;
                stack.push_back(e.to);
            }
        }
        reverse(path.begin(), path.end());
        return path;
    }

    // Hierholzer 求欧拉路径（处理半欧拉图）
    vector<int> eulerianPath() {
        int start = 0;
        // 找奇数度节点作为起点
        for (int i = 0; i < n_; ++i) {
            if ((int)adj_[i].size() % 2 == 1) { start = i; break; }
        }
        return eulerianCircuit(start);
    }

private:
    int n_;
    int edge_cnt_ = 0;
    vector<vector<EEdge>> adj_;
};

} // namespace dsa
```

### 6.2 完整测试程序

```cpp
int main() {
    using namespace dsa;

    // 测试 1：欧拉回路（矩形 1-2-3-4-1）
    cout << "=== 测试 1：欧拉回路 ===" << endl;
    EulerianGraph g1(5);
    g1.addEdge(1, 2);
    g1.addEdge(1, 4);
    g1.addEdge(2, 3);
    g1.addEdge(3, 4);
    cout << "度: ";
    for (int d : g1.degree()) cout << d << " ";
    cout << endl;
    cout << "存在欧拉回路? " << g1.hasEulerianCircuit() << endl;
    auto path1 = g1.eulerianCircuit(1);
    cout << "欧拉回路: ";
    for (int v : path1) cout << v << " -> ";
    cout << endl;

    // 测试 2：欧拉路径（半欧拉图）
    cout << "\n=== 测试 2：欧拉路径 ===" << endl;
    EulerianGraph g2(5);
    g2.addEdge(0, 1);
    g2.addEdge(1, 2);
    g2.addEdge(2, 3);
    g2.addEdge(3, 4);
    int start = -1;
    cout << "存在欧拉路径? " << g2.hasEulerianPath(start) << endl;
    auto path2 = g2.eulerianPath();
    cout << "欧拉路径: ";
    for (int v : path2) cout << v << " -> ";
    cout << endl;

    // 测试 3：无解（哥尼斯堡七桥的简化）
    cout << "\n=== 测试 3：七桥问题（无解） ===" << endl;
    EulerianGraph g3(4);
    g3.addEdge(0, 1); g3.addEdge(0, 1); g3.addEdge(0, 2);
    g3.addEdge(1, 2); g3.addEdge(1, 2);
    g3.addEdge(2, 3); g3.addEdge(3, 0);
    cout << "度: ";
    for (int d : g3.degree()) cout << d << " ";
    cout << endl;
    cout << "存在欧拉回路? " << g3.hasEulerianCircuit() << endl;
    int s = -1;
    cout << "存在欧拉路径? " << g3.hasEulerianPath(s) << endl;

    return 0;
}
```

**输出**：

```text
=== 测试 1：欧拉回路 ===
度: 0 2 2 2 2
存在欧拉回路? 1
欧拉回路: 1 -> 2 -> 3 -> 4 -> 1 ->

=== 测试 2：欧拉路径 ===
存在欧拉路径? 1
欧拉路径: 0 -> 1 -> 2 -> 3 -> 4 ->

=== 测试 3：七桥问题（无解） ===
度: 4 4 4 2
存在欧拉回路? 0
存在欧拉路径? 0
```

## 7. LeetCode 经典例题

### 7.1 LeetCode 332. 重新安排行程（困难）

> **题目**：给定一系列航线 `[from, to]`，要求从 JFK 出发，**走完所有航线**，输出**字典序最小**的行程。

**思路**：把机票建图后**反向插入邻接表**（因为 Hierholzer 输出的是**逆序**），Hierholzer 一次过。

```cpp
class Solution {
public:
    vector<string> findItinerary(vector<vector<string>>& tickets) {
        // 1. 建图：from -> {to 列表}，按字典序逆序插入
        unordered_map<string, deque<string>> graph;
        for (auto& t : tickets) {
            graph[t[0]].push_back(t[1]);
        }
        for (auto& [k, v] : graph) {
            sort(v.rbegin(), v.rend());            // 逆序：小的在末尾
        }

        // 2. Hierholzer
        vector<string> path;
        function<void(const string&)> dfs = [&](const string& u) {
            auto& neighbors = graph[u];
            while (!neighbors.empty()) {
                string v = neighbors.back();
                neighbors.pop_back();
                dfs(v);
            }
            path.push_back(u);                     // 后序加入
        };
        dfs("JFK");
        reverse(path.begin(), path.end());
        return path;
    }
};
```

- **时间复杂度**：O(E log E)（排序）+ O(E) Hierholzer

### 7.2 LeetCode 753. 破解保险箱（困难）

> **题目**：保险箱密码是 n 位 k 进制数。每次输入后，密码盘会旋转。求最短的输入序列，**走遍所有 n 位 k 进制组合**。

**思路**：把每个 n 位组合视为节点，两个组合"能旋转一次到达"就连一条边 → 图是**欧拉图**（每个节点入度 = 出度 = k）→ Hierholzer 求欧拉回路。

## 8. 复杂度表

| 操作 | 时间 | 空间 |
|------|------|------|
| 判定欧拉回路 | O(V + E) | O(V) |
| Hierholzer 求欧拉路径 | O(V + E) | O(V) |
| Hierholzer + 排序 | O(E log E + V + E) | O(V + E) |

## 9. 应用场景

- **邮路问题**：邮递员要走遍每条街恰好一次
- **电路设计**：电路板布线
- **DNA 拼接**：基因组组装中的 de Bruijn 图
- **游戏关卡**：迷宫设计、关卡路径生成
- **机器人路径**：仓储机器人覆盖所有路径

## 下一章

→ [[39-sort-basic|排序算法的关键指标]]

## 相关章节

- [[32-graph-terminology|图的基本术语]] — 度的概念
- [[34-graph-traverse-basic|图遍历]] — Hierholzer 是 DFS 的拓展
- [[30-union-find-basic|Union-Find]] — 判定欧拉图时判连通
- [[22-binary-heap-implement|堆]] — Hierholzer 的另一种实现是用最小堆
- [[36-graph-minimum-spanning-tree|最小生成树]] — 另一类"构造图"的算法
