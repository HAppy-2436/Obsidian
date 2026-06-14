---
title: 线段树核心原理及可视化
tags: [labuladong, 高级树, 数据结构与算法, 付费章节]
order: 26
prerequisites: [23-binary-tree-basic, 02-array-basic]
group: 高级树
paywall: true
source: labuladong.online
url: https://labuladong.online/zh/algo/data-structure-basic/segment-tree-basic/
---


前置知识

阅读本文前，你需要先学习：

二叉树基础及常见类型

二叉树的递归/层序遍历

一句话总结

线段树是  二叉树结构  的衍生，用于高效解决数组的区间查询和区间动态修改问题。

线段树可以在  O(logN) 的时间复杂度查询任意长度的区间元素聚合值，在  O(logN) 的时间复杂度对任意长度的区间元素进行动态修改，其中

N 为数组中的元素个数。

考虑到这是第一章，我并不准备深入讲解线段树的实现细节，具体代码会在后面的数据结构设计章节介绍。不过这里可以借助可视化面板帮你直观感受一下线段树的几种变化。

首先， 基本的线段树  包含区间查询 query 和单点修改 update 方法，你可以打开这个可视化面板，逐行点击代码，观察 query 和 update 方法的执行过程：

算法可视化

可以看到这棵二叉树的叶子节点是数组中的元素，非叶子节点就是索引区间（线段）的汇总信息，也就是「线段树」这个名字的由来。

但上面这个线段树有个问题，就是必须输入 nums 数组进行构建，如果我们想在一个非常长的区间上进行区间操作，比如 [0, 10^9]，那么上来就需要  10 9 10 9  的空间复杂度构建线段树，这是非常浪费的。

动态线段树的实现  运用「动态开点」技巧优化线段树处理稀疏数据的内存开销。你可以打开这个可视化面板，逐行点击代码，观察线段树的动态构建过程：

算法可视化

上面的实现都只支持「单点更新」，但更通用的需求是区间更新，比如把索引区间 [i, j] 的元素都更新为 val。 懒更新线段树的实现  运用「懒更新」技巧，给线段树新增 rangeAdd/rangeUpdate 方法，可以在  O(logN) 时间复杂度内完成任意长度的区间更新。

你可以打开这个可视化面板，逐行点击代码，观察懒更新线段树的运行过程。rangeUpdate 方法更新区间时，并不需要立即更新区间内的所有叶子节点，而是将更新的值缓存在某个非叶子节点中，当调用 query 方法进行区间查询时，才逐渐将更新的值向叶子节点传播：

算法可视化

下面我们来介绍线段树的使用场景和核心原理。

## 使用场景

在  选择排序  中，我们会尝试解决一个需求，就是计算 nums 数组中从索引 i 开始到末尾的最小值。

我们将提出一种使用 suffixMin 数组的优化尝试，即提前预计算一个 suffixMin 数组，使得 suffixMin[i] = min(nums[i..])，这样就可以在  O(1) 时间内查询 nums[i..] 的最小值：


> [!info] 📌 付费章节补全内容（基于算法知识体系补充）

```cpp
#include <bits/stdc++.h>
using namespace std;

namespace dsa {

// 线段树：支持「区间求和」「单点更新」「区间加法懒更新」「区间查询」
class SegmentTree {
public:
    // 构造函数：传入原始数组，构建线段树
    SegmentTree(const vector<int>& nums) : n((int)nums.size()) {
        tree.assign(4 * n, 0);
        lazy.assign(4 * n, 0);
        if (n > 0) build(1, 0, n - 1, nums);
    }

    // 区间查询 [l, r] 的元素和
    long long query(int l, int r) {
        return rangeQuery(1, 0, n - 1, l, r);
    }

    // 单点更新：把 nums[i] 设为 val
    void update(int i, int val) {
        pointUpdate(1, 0, n - 1, i, val);
    }

    // 区间更新：[l, r] 上的每个元素都加上 val
    void rangeAdd(int l, int r, int val) {
        rangeUpdate(1, 0, n - 1, l, r, val);
    }

private:
    int n;
    vector<long long> tree;   // tree[node] 存 node 节点对应区间的元素和
    vector<long long> lazy;   // lazy[node] 存 node 节点待下发的加法标记

    // 合并函数：求和
    static long long merge(long long a, long long b) { return a + b; }

    // 构建线段树
    void build(int node, int L, int R, const vector<int>& nums) {
        if (L == R) {
            tree[node] = nums[L];
            return;
        }
        int mid = (L + R) / 2;
        build(node * 2,     L, mid, nums);
        build(node * 2 + 1, mid + 1, R, nums);
        tree[node] = merge(tree[node * 2], tree[node * 2 + 1]);
    }

    // 单点更新
    void pointUpdate(int node, int L, int R, int i, int val) {
        if (L == R) {
            tree[node] = val;
            return;
        }
        int mid = (L + R) / 2;
        if (i <= mid) pointUpdate(node * 2,     L, mid, i, val);
        else          pointUpdate(node * 2 + 1, mid + 1, R, i, val);
        tree[node] = merge(tree[node * 2], tree[node * 2 + 1]);
    }

    // pushdown：把懒标记下发到子节点
    void pushdown(int node, int L, int R) {
        if (lazy[node] == 0) return;
        int mid = (L + R) / 2;
        // 左子节点
        tree[node * 2]     += lazy[node] * (mid - L + 1);
        lazy[node * 2]     += lazy[node];
        // 右子节点
        tree[node * 2 + 1] += lazy[node] * (R - mid);
        lazy[node * 2 + 1] += lazy[node];
        lazy[node] = 0;
    }

    // 区间更新（带懒更新）
    void rangeUpdate(int node, int L, int R, int l, int r, int val) {
        if (l > R || r < L) return;            // 无交集
        if (l <= L && R <= r) {                // 完全覆盖
            tree[node] += (long long)val * (R - L + 1);
            lazy[node] += val;
            return;
        }
        pushdown(node, L, R);
        int mid = (L + R) / 2;
        rangeUpdate(node * 2,     L,     mid, l, r, val);
        rangeUpdate(node * 2 + 1, mid + 1, R, l, r, val);
        tree[node] = merge(tree[node * 2], tree[node * 2 + 1]);
    }

    // 区间查询（带懒更新）
    long long rangeQuery(int node, int L, int R, int l, int r) {
        if (l > R || r < L) return 0;          // 无交集：返回单位元
        if (l <= L && R <= r) return tree[node];
        pushdown(node, L, R);
        int mid = (L + R) / 2;
        long long left_val  = rangeQuery(node * 2,     L,     mid, l, r);
        long long right_val = rangeQuery(node * 2 + 1, mid + 1, R, l, r);
        return merge(left_val, right_val);
    }
};

// 区间最值（最大值）版本：懒更新语义为「区间取 max」时需另行实现
class SegmentTreeMax {
public:
    SegmentTreeMax(const vector<int>& nums) : n((int)nums.size()) {
        tree.assign(4 * n, INT_MIN);
        build(1, 0, n - 1, nums);
    }
    int query(int l, int r) { return rangeQuery(1, 0, n - 1, l, r); }
    void update(int i, int val) { pointUpdate(1, 0, n - 1, i, val); }

private:
    int n;
    vector<int> tree;
    static int merge(int a, int b) { return max(a, b); }

    void build(int node, int L, int R, const vector<int>& nums) {
        if (L == R) { tree[node] = nums[L]; return; }
        int mid = (L + R) / 2;
        build(node * 2,     L,     mid, nums);
        build(node * 2 + 1, mid + 1, R, nums);
        tree[node] = merge(tree[node * 2], tree[node * 2 + 1]);
    }
    void pointUpdate(int node, int L, int R, int i, int val) {
        if (L == R) { tree[node] = val; return; }
        int mid = (L + R) / 2;
        if (i <= mid) pointUpdate(node * 2,     L,     mid, i, val);
        else          pointUpdate(node * 2 + 1, mid + 1, R, i, val);
        tree[node] = merge(tree[node * 2], tree[node * 2 + 1]);
    }
    int rangeQuery(int node, int L, int R, int l, int r) {
        if (l > R || r < L) return INT_MIN;
        if (l <= L && R <= r) return tree[node];
        int mid = (L + R) / 2;
        return merge(rangeQuery(node * 2,     L,     mid, l, r),
                     rangeQuery(node * 2 + 1, mid + 1, R, l, r));
    }
};

} // namespace dsa

int main() {
    using namespace dsa;

    // 演示 1：区间求和 + 单点更新
    SegmentTree st({1, 3, 5, 7, 9, 11});
    cout << "query(0, 2) = " << st.query(0, 2) << endl;     // 1+3+5 = 9
    cout << "query(3, 5) = " << st.query(3, 5) << endl;     // 7+9+11 = 27

    st.update(1, 10);  // 把 nums[1] 改成 10
    cout << "update(1,10) 后 query(0, 2) = " << st.query(0, 2) << endl;  // 1+10+5 = 16

    // 演示 2：区间加法懒更新
    SegmentTree st2({0, 0, 0, 0, 0});
    st2.rangeAdd(1, 3, 5);  // 把 [1,3] 都加 5
    cout << "区间加 5 后 query(0, 4) = " << st2.query(0, 4) << endl;       // 0+5+5+5+0 = 15
    cout << "query(2, 4) = " << st2.query(2, 4) << endl;                  // 5+5+0 = 10

    // 演示 3：区间最大值
    SegmentTreeMax stm({3, 1, 4, 1, 5, 9, 2, 6});
    cout << "max(0, 7) = " << stm.query(0, 7) << endl;  // 9
    cout << "max(2, 5) = " << stm.query(2, 5) << endl;  // 9
    return 0;
}
```

**输出**：

```text
query(0, 2) = 9
query(3, 5) = 27
update(1,10) 后 query(0, 2) = 16
区间加 5 后 query(0, 4) = 15
query(2, 4) = 10
max(0, 7) = 9
max(2, 5) = 9
```

## 7. 复杂度表

| 操作 | 时间复杂度 | 空间复杂度 |
|------|-----------|-----------|
| build（建树） | O(N) | O(N) |
| pointUpdate（单点更新） | O(log N) | O(1) |
| rangeUpdate（区间更新，带懒更新） | O(log N) | O(log N)（栈） |
| rangeQuery（区间查询） | O(log N) | O(log N)（栈） |
| 整体存储 | — | O(4N) = O(N) |

> [!warning] 为什么是 4N 而不是 2N？
> 线段树是一棵 **完全二叉树**，按理说 N 个叶子节点的完全二叉树最多有 2N 个节点。但由于线段树的 build 过程会把区间 **对半分**，最后一层可能不是完全填满（取决于 N 的奇偶性）。安全起见业界约定 4N 是绝对够用的上界。

## 8. 应用场景

- **区间求和 / 区间最值**：[[26-segment-tree-basic|线段树]] 最经典的应用，比如「求数组 `nums[i..j]` 的元素和」或「滑动窗口最大值」。
- **区间染色 / 区间赋值**：将一个区间全部染成某种颜色、或者全部加一个值，这就是懒更新（Lazy Propagation）的核心场景。
- **二维线段树 / 树套树**：把一维线段树扩展到二维，可以做「子矩阵和查询 + 子矩阵加法更新」。
- **LeetCode 经典题**：
  - [307. 区域和检索 - 数组可修改](https://leetcode.cn/problems/range-sum-query-mutable/)：单点更新 + 区间求和
  - [303. 区域和检索 - 数组不可变](https://leetcode.cn/problems/range-sum-query-immutable/)：用前缀和即可，不一定要线段树
  - [699. 掉落的方块](https://leetcode.cn/problems/falling-squares/)：区间更新 + 单点查询
  - [732. 我的日程安排表 III](https://leetcode.cn/problems/my-calendar-iii/)：区间染色计数

## 9. 线段树 vs 其他区间结构

| 方案 | 区间查询 | 区间更新 | 适用场景 |
|------|---------|---------|---------|
| **前缀和** | O(1) | O(N) 重建 | 静态数组 |
| **树状数组 (BIT)** | O(log N) | O(log N)（单点更新 / 区间查询） | 求和类问题，代码更短 |
| **线段树** | O(log N) | O(log N)（区间更新 + 区间查询） | 任意可聚合的「区间 + 修改」 |
| **平衡 BST** | O(log N) | O(log N) | 「单点 + 排名」类问题 |

> [!tip] 线段树 vs 树状数组 (Fenwick Tree)
> 如果你只需要 **「单点更新 + 区间求和」** 或 **「区间更新 + 单点查询」**，[[46-shell-sort|树状数组]]（BIT，Binary Indexed Tree）可以用 **一半的代码量** 实现同样 O(log N) 的复杂度。但如果你需要 **「区间更新 + 区间查询」** 或 **「区间最值 / 区间 GCD」** 等更复杂的聚合，线段树是更通用的选择。

## 下一章

→ [[27-tree-map-basic|二叉搜索树原理及应用技巧]]

## 相关章节

- [[23-binary-tree-basic|二叉树基础]] — 线段树的逻辑结构
- [[02-array-basic|数组原理]] — 线段树用数组紧凑存储
- [[21-binary-heap-basic|二叉堆]] — 另一种「用数组实现的树」，对比学习
- [[22-binary-heap-implement|堆的代码实现]] — 树形结构的代码实现技巧
- [[45-heap-sort|堆排序]] — 区间排序的另一种实现


## 关联章节

- [[23-binary-tree-basic|二叉树基本概念及特殊二叉树]]
- [[02-array-basic|数组（顺序存储）的原理]]
