---
title: 线段树核心原理及可视化
tags:
  - 线段树
  - 区间查询
  - 区间更新
  - 懒更新
  - 高级树
order: 26
prerequisites:
  - "[[23-binary-tree-basic]]"
  - "[[02-array-basic]]"
group: 高级树
subgroup: null
paywall: true
source: https://labuladong.online/zh/algo/data-structure-basic/segment-tree-basic/
---

# 线段树核心原理及可视化

## 学习目标

- 理解线段树（Segment Tree）的本质：一种「按区间划分」的二叉树
- 掌握 **区间查询 query** 与 **单点/区间更新 update** 的实现思路
- 理解线段树用 **tree 数组** 紧凑存储的索引公式
- 理解 **懒更新（Lazy Propagation）** 的核心思想
- 能够手写一个支持「区间求和 / 区间最值」的线段树 C++ 实现
- 了解线段树的两类典型应用：区间求和、滑动窗口最值

## 一句话总结

线段树是 [[23-binary-tree-basic|二叉树结构]] 在「按区间递归划分」上的延伸，它在 **O(log N)** 时间内完成 **区间聚合值查询** 与 **区间/单点更新**，是处理「区间 + 修改」问题的标配数据结构；其关键技巧是 **懒更新（Lazy Propagation）**，把区间更新「先记账、后结算」，从而保持 O(log N) 复杂度。

## 前置知识

阅读本文前，你需要先学习：

- [[23-binary-tree-basic|二叉树基本概念及特殊二叉树]]
- [[02-array-basic|数组（顺序存储）的原理]]

## 1. 线段树是什么

线段树（Segment Tree）是一种 **二叉树**，它的每个节点对应 **数组中的一段连续区间（线段）**：

- **根节点** 对应整个数组区间 `[0, n-1]`
- **叶子节点** 对应单个元素（长度为 1 的区间）
- **非叶子节点** 把父节点区间 **对半分**：左子节点对应左半段，右子节点对应右半段

正因每个节点代表一条「线段」（即一个区间），所以叫 **线段树**。

对于数组 `nums = [1, 3, 5, 7, 9, 11]`，线段树的结构如下：

```
                [0,5] sum=36
              /          \
         [0,2] 19      [3,5] 27
         /   \          /    \
      [0,1]4 [2,2]5  [3,4]16 [5,5]11
      /   \           /   \
   [0,0]1 [1,1]3   [3,3]7 [4,4]9
```

非叶子节点存储的就是 **子节点区间信息的聚合**（这里以「区间和」为例，所以 `sum[0..2] = 1+3+5 = 9`、`sum[0..5] = 36`）。

> [!tip] 线段树和堆的区别
> [[21-binary-heap-basic|二叉堆]] 也是用数组存储的二叉树，但堆的结构是 **按层紧凑** 排列，父子的下标关系是 `parent(i) = i/2`。线段树则是 **按区间对半分**，根节点存 `0`、左右子存 `1, 2`，这恰好也是完全二叉树，所以仍然可以用数组紧凑存储。两种树的存储形式相同，但「节点含义」不同：堆存的是「元素本身」，线段树存的是「区间聚合值」。

## 2. 区间查询 query

### 2.1 思想

要查询数组 `nums` 在区间 `[l, r]` 上的聚合值（比如求和、求最大值），思路是：

1. 从 **根节点** 出发，比较查询区间 `[l, r]` 和当前节点的区间 `[L, R]`
2. 如果 `[l, r]` 完全覆盖 `[L, R]`，就直接返回当前节点存的聚合值
3. 否则，把 `[l, r]` 拆给左右子节点递归处理，把结果再聚合

由于树的深度是 `O(log N)`，每次最多访问 `O(log N)` 个节点（从根到叶子的路径），所以单次查询的复杂度是 **O(log N)**。

### 2.2 代码骨架

```text
query(node, L, R, l, r):
    if l > R or r < L:       // 查询区间与当前节点区间无交集
        return identity       // 单位元（如求和返回 0，求最值返回 -inf/+inf）
    if l <= L and R <= r:    // 当前节点区间被完全包含
        return tree[node]
    mid = (L + R) / 2
    left_val  = query(node*2,   L, mid, l, r)
    right_val = query(node*2+1, mid+1, R, l, r)
    return merge(left_val, right_val)
```

这里的 `merge` 视业务而定：求和就是 `+`，求最大值就是 `max`，求最小值就是 `min`。

## 3. 单点更新 update

把数组 `nums[i]` 修改为 `val` 后，线段树需要把所有包含 `i` 的区间都更新一遍：

1. 从根出发，递归向下，直到叶子节点 `[i, i]`
2. 把 `tree[node]` 设为 `val`
3. 回溯时，把左右子节点的聚合值合并赋给父节点

单点更新最多访问 **O(log N)** 个节点（从根到叶子的路径），所以复杂度也是 **O(log N)**。

```text
update(node, L, R, i, val):
    if L == R:
        tree[node] = val
        return
    mid = (L + R) / 2
    if i <= mid:  update(node*2,   L, mid, i, val)
    else:         update(node*2+1, mid+1, R, i, val)
    tree[node] = merge(tree[node*2], tree[node*2+1])
```

## 4. 线段树的数组存储

线段树通常用 1-indexed 数组存储，原因与堆类似（避免父子关系中的 0 边界）。`tree` 数组至少需要 `4 * n` 大小（证明略，但这是业界通用的上界）：

| 关系 | 公式 |
|------|------|
| 父节点 | `parent(i) = i / 2` |
| 左子节点 | `left(i) = 2 * i` |
| 右子节点 | `right(i) = 2 * i + 1` |

为什么需要 `4 * n`？考虑 n=10 的情况，最坏情况下最后一层不一定会被填满，但安全起见取 4n。`4n` 是一个 **绝对够用** 的上界。

## 5. 懒更新（Lazy Propagation）—— 区间更新的关键


### 5.1 为什么需要懒更新

单点更新 `update(i, val)` 已经是 O(log N) 了，但 **区间更新** `update(l, r, val)` 怎么办？

最朴素的做法是遍历 `[l, r]` 中的每个元素都做一次单点更新，总复杂度 O((r-l+1) * log N)，最坏情况是 O(N log N)，效率不可接受。

懒更新的核心思想是 **"先记账、后结算"**：

- 维护一个与 `tree` 等大的数组 `lazy[]`，初始全为 0
- 当要更新区间 `[l, r]` 时，对路上经过的 **完全被 `[l, r]` 覆盖** 的节点，**只更新 `tree[node]`，并在 `lazy[node]` 中记录一个"待下发"的标记**，**不下推到子节点**
- 等到下次需要访问子节点时（比如查询或再次更新），再把 `lazy[node]` 的值 **pushdown** 给左右子节点

这样，每次区间更新最多访问 O(log N) 个节点（从根到叶子的路径上完全被覆盖的节点），且 `pushdown` 也不增加新的访问量，整体仍然是 O(log N)。

### 5.2 懒更新的关键操作

#### (1) pushdown：把懒标记下发到子节点

```text
pushdown(node, L, R):
    if lazy[node] != 0:
        mid = (L + R) / 2
        // 把懒值应用到左子节点
        tree[node*2]   += lazy[node] * (mid - L + 1)   // 求和场景
        lazy[node*2]   += lazy[node]
        // 把懒值应用到右子节点
        tree[node*2+1] += lazy[node] * (R - mid)       // 求和场景
        lazy[node*2+1] += lazy[node]
        lazy[node] = 0
```

注意 `tree[node] += lazy * len` 的写法：求和场景下，区间长度 `len` 个元素都加了 `lazy`，所以和增加 `lazy * len`。如果业务是「取最大值」，则不需要乘长度。

#### (2) rangeUpdate：区间更新

```text
rangeUpdate(node, L, R, l, r, val):
    if l > R or r < L:        return
    if l <= L and R <= r:     // 完全覆盖
        tree[node] += val * (R - L + 1)
        lazy[node] += val
        return
    pushdown(node, L, R)
    mid = (L + R) / 2
    rangeUpdate(node*2,   L, mid, l, r, val)
    rangeUpdate(node*2+1, mid+1, R, l, r, val)
    tree[node] = merge(tree[node*2], tree[node*2+1])
```

#### (3) rangeQuery：区间查询（带懒更新）

```text
rangeQuery(node, L, R, l, r):
    if l > R or r < L:  return identity
    if l <= L and R <= r:  return tree[node]
    pushdown(node, L, R)        // 关键：访问子节点前先 pushdown
    mid = (L + R) / 2
    left_val  = rangeQuery(node*2,   L, mid, l, r)
    right_val = rangeQuery(node*2+1, mid+1, R, l, r)
    return merge(left_val, right_val)
```

## 6. 完整 C++ 实现

> 以下是支持「区间求和 + 单点更新 + 区间加法懒更新 + 区间查询」的完整 C++ 实现。


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
