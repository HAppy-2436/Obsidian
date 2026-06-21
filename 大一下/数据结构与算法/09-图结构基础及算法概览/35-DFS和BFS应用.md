---
title: DFS 和 BFS 的常用场景
tags: [labuladong, 图, 遍历, 数据结构与算法, 付费章节]
category: 图结构基础及算法概览
order: 35
prerequisites: [34-图的遍历]
group: 图 / 遍历
paywall: true
source: labuladong.online
url: https://labuladong.online/zh/algo/data-structure-basic/use-case-of-dfs-bfs/
---


读完本文，你不仅学会了算法套路，还可以顺便解决如下题目：

LeetCode

力扣

难度

111. Minimum Depth of Binary Tree

111. 二叉树的最小深度

前置知识

阅读本文前，你需要先学习：

二叉树的递归/层序遍历

在实际的算法问题中，DFS 算法常用来穷举所有路径，BFS 算法常用来寻找最短路径，这是什么原因呢？

因为二叉树的递归遍历和层序遍历就是最简单的 DFS 算法和 BFS 算法，所以本文就用一道简单的二叉树例题，说明其中的道理。


> [!info] 📌 付费章节补全内容（基于算法知识体系补充）

```cpp
// DFS 排列模板：枚举 nums 的所有排列
void permute(vector<int>& nums, int start, vector<int>& path,
             vector<vector<int>>& res) {
    if (start == nums.size()) {                // 走完了
        res.push_back(path);
        return;
    }
    for (int i = 0; i < nums.size(); ++i) {
        if (used[i]) continue;                 // 剪枝：跳过已用元素
        used[i] = true;
        path.push_back(nums[i]);
        permute(nums, start + 1, path, res);
        path.pop_back();                       // 撤销
        used[i] = false;
    }
}
```

## 2. 为什么 BFS 适合"最短路"？

[[24-二叉树遍历|二叉树层序遍历]]本质就是 BFS——队列天然支持"先入先出"，所以**先入队的节点就先被处理**。

**关键事实**：在**无权图**中，BFS 按层访问节点——**第一次到达某个节点时经过的路径就是最短路径**。

> [!tip] 直观理解
> BFS 像水波纹——波纹**先扩散到近处**。第一次"拍到"目标点时，路径长度 = 波纹扩散的层数 = 最短距离。

```cpp
// BFS 求无权图最短路（返回从 s 到 t 的距离）
int bfsShortestPath(const GraphAdjList& g, int s, int t) {
    vector<int> dist(g.size(), -1);             // -1 表示未访问
    queue<int> q;
    q.push(s);
    dist[s] = 0;

    while (!q.empty()) {
        int v = q.front(); q.pop();
        if (v == t) return dist[v];            // 第一次到达 t
        for (const Edge& e : g.neighbors(v)) {
            if (dist[e.to] == -1) {
                dist[e.to] = dist[v] + 1;      // 距离 = 父节点 + 1
                q.push(e.to);
            }
        }
    }
    return -1;                                  // 不可达
}
```

## 3. 核心框架总结

### 3.1 DFS 框架

```text
dfs(节点, 状态):
    if 满足终止条件: 记录答案; return
    for 每个选择:
        修改状态（前序位置）        ← 进入
        dfs(下一个节点, 新状态)
        撤销状态（后序位置）        ← 退出
```

### 3.2 BFS 框架

```text
bfs(起点):
    queue ← {起点}
    visited ← {起点}
    while queue 不空:
        v ← queue.pop()
        if v == 目标: 记录答案
        for v 的每个邻居 u:
            if u not in visited:
                visited.add(u)
                queue.push(u)
```

## 4. 经典 LeetCode 题目与 C++ 实现

> 以下 5 道题目是 DFS / BFS 的高频经典题，覆盖了**连通块、岛屿、排列、拓扑序、最短路**五个核心场景。

### 4.1 LeetCode 200. 岛屿数量（中等）— DFS / BFS 均可

> **题目**：给定一个二维网格 `grid`，`'1'` 表示陆地、`'0'` 表示水。岛屿是由相邻（上下左右）的陆地组成的连通块。求岛屿数量。

**思路**：遍历整个网格，每遇到一个未访问的 `'1'`，就启动一次 DFS/BFS 把整座岛屿"淹没"（标记为 `'0'`），计数器 +1。

**DFS 实现**：

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int m = grid.size(), n = grid[0].size();
        int count = 0;
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (grid[i][j] == '1') {
                    ++count;
                    dfs(grid, i, j);
                }
            }
        }
        return count;
    }

private:
    void dfs(vector<vector<char>>& grid, int i, int j) {
        int m = grid.size(), n = grid[0].size();
        if (i < 0 || i >= m || j < 0 || j >= n) return;
        if (grid[i][j] != '1') return;             // 不是陆地就返回
        grid[i][j] = '0';                          // 标记为水（剪枝+淹没）
        // 上下左右
        dfs(grid, i + 1, j);
        dfs(grid, i - 1, j);
        dfs(grid, i, j + 1);
        dfs(grid, i, j - 1);
    }
};
```

- **时间复杂度**：O(M × N)
- **空间复杂度**：O(M × N)（最坏递归栈）

### 4.2 LeetCode 547. 省份数量（中等）— DFS / BFS

> **题目**：有 n 个城市，如果 `isConnected[i][j] = 1` 则城市 i 和 j 直接相连。求**连通分量**的个数（省份数）。

**思路**：和岛屿问题几乎一样——只是数据是邻接矩阵而不是网格。

```cpp
class Solution {
public:
    int findCircleNum(vector<vector<int>>& isConnected) {
        int n = isConnected.size();
        vector<bool> visited(n, false);
        int count = 0;
        for (int i = 0; i < n; ++i) {
            if (!visited[i]) {
                ++count;
                dfs(isConnected, i, visited);
            }
        }
        return count;
    }

private:
    void dfs(vector<vector<int>>& g, int s, vector<bool>& visited) {
        visited[s] = true;
        for (int j = 0; j < (int)g.size(); ++j) {
            if (g[s][j] == 1 && !visited[j]) {
                dfs(g, j, visited);
            }
        }
    }
};
```

- **时间复杂度**：O(V²)
- **空间复杂度**：O(V)

> **进阶**：本题也可直接用[[30-并查集原理|并查集]]做。

### 4.3 LeetCode 46. 全排列（中等）— DFS + 回溯

> **题目**：给定一个不含重复数字的数组 `nums`，返回其所有可能的全排列。

**思路**：标准的 DFS 模板——枚举每个位置放哪个数，路径用 `used[]` 防止重复选。

```cpp
class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> res;
        vector<int> path;
        vector<bool> used(nums.size(), false);
        dfs(nums, used, path, res);
        return res;
    }

private:
    void dfs(vector<int>& nums, vector<bool>& used,
             vector<int>& path, vector<vector<int>>& res) {
        if (path.size() == nums.size()) {
            res.push_back(path);                  // 完整排列
            return;
        }
        for (int i = 0; i < (int)nums.size(); ++i) {
            if (used[i]) continue;
            used[i] = true;
            path.push_back(nums[i]);
            dfs(nums, used, path, res);
            path.pop_back();                      // 撤销
            used[i] = false;
        }
    }
};
```

- **时间复杂度**：O(N × N!)
- **空间复杂度**：O(N)（递归栈）

### 4.4 LeetCode 210. 课程表 II（中等）— DFS / BFS 拓扑排序

> **题目**：有 n 门课程，编号 0 ~ n-1。`prerequisites[i] = [a, b]` 表示"必须先修 b 才能修 a"。返回一个**可行的修课顺序**。

**思路**：这是**拓扑排序**的经典题——本质是"对有向无环图（DAG）做 DFS，**后序遍历的逆序**就是拓扑序"。

```cpp
class Solution {
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        // 1. 建图（邻接表）
        vector<vector<int>> graph(numCourses);
        vector<int> indeg(numCourses, 0);
        for (auto& p : prerequisites) {
            graph[p[1]].push_back(p[0]);         // b -> a
            ++indeg[p[0]];                      // a 的入度 +1
        }
        // 2. BFS：每次选入度为 0 的节点
        queue<int> q;
        for (int i = 0; i < numCourses; ++i) {
            if (indeg[i] == 0) q.push(i);
        }
        vector<int> order;
        while (!q.empty()) {
            int v = q.front(); q.pop();
            order.push_back(v);
            for (int u : graph[v]) {
                if (--indeg[u] == 0) q.push(u);  // 邻居入度减 1
            }
        }
        return order.size() == numCourses ? order : vector<int>{};
    }
};
```

- **时间复杂度**：O(V + E)
- **空间复杂度**：O(V + E)

> [!tip] 拓扑排序的两种写法
> 1. **BFS 写法**（如上）：每次取入度为 0 的点；
> 2. **DFS 写法**：DFS 后序遍历，**结果反转**就是拓扑序——同样 O(V + E)。

### 4.5 LeetCode 111. 二叉树的最小深度（简单）— BFS

> **题目**：求根节点到最近叶子节点的路径长度（节点数）。

**思路**：BFS 一层层向下，**第一次遇到叶子节点**时的层数就是最小深度。

```cpp
class Solution {
public:
    int minDepth(TreeNode* root) {
        if (!root) return 0;
        queue<TreeNode*> q;
        q.push(root);
        int depth = 1;
        while (!q.empty()) {
            int sz = q.size();
            for (int i = 0; i < sz; ++i) {
                TreeNode* v = q.front(); q.pop();
                if (!v->left && !v->right) return depth;  // 叶子
                if (v->left)  q.push(v->left);
                if (v->right) q.push(v->right);
            }
            ++depth;
        }
        return depth;
    }
};
```

- **时间复杂度**：O(N)
- **空间复杂度**：O(N)

> **对比**：用 DFS 也能做（min(左深度, 右深度) + 1），但 DFS 必须遍历完整棵树；而 BFS **遇到第一个叶子就退出**，平均更快。

## 5. DFS vs BFS：一张表对比

| 维度 | DFS | BFS |
|------|-----|-----|
| **数据结构** | 递归 / 栈 | 队列 |
| **空间复杂度** | O(树高) | O(宽度) |
| **访问顺序** | 一条路走到黑 | 一圈圈扩散 |
| **适合穷举** | ✅ **路径 / 排列 / 子集** | ❌ |
| **适合最短路** | ❌（要遍历所有路径） | ✅ **无权图最短路** |
| **适合连通性** | ✅ 连通块 / 岛屿数 | ✅ 同样可以 |
| **适合拓扑序** | ✅ 后序遍历反转 | ✅ 入度为 0 入队 |
| **遇到目标就停** | ❌ | ✅ |

## 6. 复杂度表

| 应用 | 时间 | 空间 | 算法 |
|------|------|------|------|
| 连通分量数 | O(V + E) | O(V) | DFS / BFS |
| 岛屿数 | O(M × N) | O(M × N) | DFS / BFS |
| 排列 | O(N × N!) | O(N) | DFS 回溯 |
| 拓扑排序 | O(V + E) | O(V + E) | DFS / BFS |
| 无权图最短路 | O(V + E) | O(V) | BFS |
| 二叉树最小深度 | O(N) | O(N) | BFS |

## 7. 应用场景

- **DFS**：连通块、岛屿、排列、子集、N 皇后、数独、拓扑排序、回溯
- **BFS**：无权图最短路、扩散（腐烂的橘子）、IP 地址、单词接龙、二叉树最小深度


## LeetCode 经典例题实战

### 200. 岛屿数量（DFS 入门）

```cpp
#include <bits/stdc++.h>
using namespace std;

namespace dsa {

class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int m = grid.size(), n = grid[0].size();
        int count = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == '1') {
                    dfs(grid, i, j);
                    count++;
                }
            }
        }
        return count;
    }
private:
    void dfs(vector<vector<char>>& g, int i, int j) {
        if (i < 0 || i >= g.size() || j < 0 || j >= g[0].size()) return;
        if (g[i][j] != '1') return;
        g[i][j] = '0';  // 标记已访问
        dfs(g, i+1, j);
        dfs(g, i-1, j);
        dfs(g, i, j+1);
        dfs(g, i, j-1);
    }
};

} // namespace dsa
```

### 547. 朋友圈（连通分量）

```cpp
namespace dsa {

class Solution {
public:
    int findCircleNum(vector<vector<int>>& M) {
        int n = M.size();
        vector<bool> visited(n, false);
        int count = 0;
        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                dfs(M, visited, i);
                count++;
            }
        }
        return count;
    }
private:
    void dfs(vector<vector<int>>& M, vector<bool>& v, int i) {
        v[i] = true;
        for (int j = 0; j < M.size(); j++) {
            if (M[i][j] == 1 && !v[j]) dfs(M, v, j);
        }
    }
};

} // namespace dsa
```

### 743. 网络延迟时间（Dijkstra）

```cpp
namespace dsa {

class Solution {
public:
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        vector<vector<pair<int,int>>> graph(n + 1);
        for (auto& t : times) graph[t[0]].push_back({t[1], t[2]});

        vector<int> dist(n + 1, INT_MAX);
        dist[k] = 0;
        priority_queue<pair<int,int>, vector<pair<int,int>>, greater<>> pq;
        pq.push({0, k});

        while (!pq.empty()) {
            auto [d, u] = pq.top(); pq.pop();
            if (d > dist[u]) continue;
            for (auto [v, w] : graph[u]) {
                if (dist[u] + w < dist[v]) {
                    dist[v] = dist[u] + w;
                    pq.push({dist[v], v});
                }
            }
        }
        int ans = *max_element(dist.begin() + 1, dist.end());
        return ans == INT_MAX ? -1 : ans;
    }
};

} // namespace dsa
```

### 1091. 二进制矩阵中的最短路径（BFS）

```cpp
namespace dsa {

class Solution {
public:
    int shortestPathBinaryMatrix(vector<vector<int>>& grid) {
        int n = grid.size();
        if (grid[0][0] == 1) return -1;
        queue<pair<int,int>> q;
        q.push({0, 0});
        grid[0][0] = 1;
        int dirs[8][2] = {{-1,-1},{-1,0},{-1,1},{0,-1},{0,1},{1,-1},{1,0},{1,1}};
        int steps = 1;
        while (!q.empty()) {
            int sz = q.size();
            while (sz--) {
                auto [x, y] = q.front(); q.pop();
                if (x == n-1 && y == n-1) return steps;
                for (auto& d : dirs) {
                    int nx = x + d[0], ny = y + d[1];
                    if (nx < 0 || nx >= n || ny < 0 || ny >= n || grid[nx][ny] == 1) continue;
                    grid[nx][ny] = 1;
                    q.push({nx, ny});
                }
            }
            steps++;
        }
        return -1;
    }
};

} // namespace dsa
```

## DFS vs BFS 选择指南

| 场景 | 选择 | 原因 |
|------|------|------|
| 连通块计数、岛屿 | DFS | 递归简洁 |
| 最短路径（无权图） | BFS | BFS 按层扩展，第一次到达就是最短 |
| 最短路径（带权图） | Dijkstra | 优先队列 |
| 拓扑排序 | DFS 或 BFS（Kahn） | 都行 |
| 连通性问题 | DFS / BFS / Union-Find | 都可以 |
| 二叉树遍历 | DFS（递归） | 自然结构 |
| 棋盘最少步数 | BFS | 最短路径 |


## 下一章

→ [[36-最小生成树|最小生成树算法概览]]

## 相关章节

- [[24-二叉树遍历|二叉树遍历]] — DFS/BFS 的最简形态
- [[34-图的遍历|图遍历]] — DFS/BFS 的图版本
- [[30-并查集原理|并查集]] — 求连通分量的另一种思路
- [[37-最短路径算法|最短路径]] — BFS 的加权扩展（Dijkstra）
- [[36-最小生成树|最小生成树]] — 图论核心应用
- [[38-欧拉图|欧拉图]] — 遍历所有边的应用


## 关联章节

- [[34-图的遍历|图结构的 DFS/BFS 遍历]]
