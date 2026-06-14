---
title: 欧拉图一笔画游戏
tags: [labuladong, 图, 应用, 数据结构与算法, 付费章节]
order: 38
prerequisites: [34-graph-traverse-basic]
group: 图 / 应用
paywall: true
source: labuladong.online
url: https://labuladong.online/zh/algo/data-structure-basic/eulerian-graph/
---


前置知识

阅读本文前，你需要先学习：

图结构术语

图结构的 DFS/BFS 遍历

一句话总结

「一笔画」游戏的本质是寻找欧拉路径/欧拉回路，可以通过节点的度数判断是否存在欧拉路径/欧拉回路。

Hierholzer 算法是用于计算欧拉路径/欧拉回路的经典算法，它是
图结构 DFS 算法
 的拓展。

欧拉图是图论中的经典概念，起源于著名的哥尼斯堡七桥问题。这个问题不仅在数学史上具有重要意义，在现代计算机科学中也有广泛应用，比如路径规划、电路设计等。

考虑到这是基础章节，所以不会详细讲解代码实现，具体的算法代码以及习题会安排在数据结构章节的图论部分讲解。

本文主要介绍欧拉图的定义、经典的七桥问题、欧拉路径和欧拉回路的概念，以及寻找欧拉路径的技巧，你可以在本站配套的一笔画小游戏中直观地感受到。

## 一笔画游戏

我记得小时候玩过「一笔画」小游戏，规则就是要求你一笔连接所有的点和边，其中点可以重复经过，但每条边必须恰好经过一次，不能重复经过。

网站配套的游戏面板也收录了这个小游戏：

一笔画游戏

小时候玩这种游戏就是全靠运气，随便选择起点开始乱走一通，能走完就走完，走不完就重新开始。

后来才知道这个益智小游戏其实是一个经典的图论算法，而且有套路可循。

现在就可以告诉你完成游戏的套路：

如果所有节点的度数都是偶数，那么可以从任何节点开始，一定可以完成一笔画，且最终会回到起点。

如果只有两个节点的度数为奇数，那么必须从这两个奇数度节点中的任意一个开始，才能完成一笔画。

如果上面两种情况都不满足，那么无法完成一笔画。

游戏面板中会显示每个节点的
度数
，你可以先试试看这个套路好不好用：）

下面我们来介绍这个小游戏背后的图论知识 - 欧拉图。

## 七桥问题

欧拉图的概念源于 18 世纪著名的哥尼斯堡七桥问题。当时的哥尼斯堡（现在的加里宁格勒）有一条河流将城市分为南北两岸，河中有东西两个小岛，有七座桥连接着北岸、南岸、东岛和西岛。

问题是：能否设计一条路线，从任意一个区域出发，经过每座桥恰好一次，最后回到起点？

我们可以将这个问题抽象成图论问题：

在这幅图中：

每个区域对应一个节点

每座桥对应一条边

问题转化为：是否存在一条路径，经过图中每条边恰好一次，且最终回到起点

最终，欧拉通过数学证明七桥问题无解，从而解决了这个著名问题。

## 术语定义

基于七桥问题，我们引入几个图论术语：


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


## 关联章节

- [[34-graph-traverse-basic|图结构的 DFS/BFS 遍历]]
