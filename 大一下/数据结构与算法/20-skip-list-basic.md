---
title: 跳表原理
tags: [数据结构, 哈希集合]
order: 20
prerequisites: [06-linkedlist-implement]
group: 哈希集合
paywall: false
source: labuladong
---

# 跳表原理

## 📚 学习目标

- 理解跳表（Skip List）通过「多层索引」优化链表查询的核心思想
- 掌握跳表查询/插入/删除的时间复杂度 O(log N) 分析
- 对比跳表与 [[27-tree-map-basic|二叉搜索树]] 的优劣
- 了解 Redis ZSet 用跳表而非红黑树的原因

## 🎯 一句话总结

跳表是「空间换时间」思想在链表上的极致应用：在原始链表上叠加多层稀疏索引，使增删查改的时间复杂度从 O(N) 优化到 O(log N)，同时保持链表的有序性和实现简洁性。

## 🔗 前置知识

- [[06-linkedlist-implement|链表的代码实现]]
- [[01-complexity|时间空间复杂度入门]]

## 📖 正文

### 单链表的痛点：查询是 O(N)

在 [[05-linkedlist-basic|链表（链式存储）的原理]] 中我们学过：单链表增删节点（拿到指针后）只需要 O(1)，但**查找指定索引的节点必须从头遍历到目标位置**，时间复杂度 O(N)。

当我们需要「按索引访问」或「按键值有序遍历」时，单链表的 O(N) 查询就成了瓶颈。

两条主流优化路径：

1. **键值映射**：在链表上外挂哈希表，让"按 key 查节点"变成 O(1)，即 [[12-hashtable-with-linked-list|哈希链表（LinkedHashMap）]]。代价：失去有序性。
2. **多层索引（本文主角）**：在链表上叠加多层稀疏索引，把查找路径压缩到 O(log N)。代价：额外的索引节点开销。

跳表属于第二条路径。

### 跳表核心原理：可视化

假设有一条包含 11 个节点的单链表 `a..k`：

```
index  0  1  2  3  4  5  6  7  8  9  10
node   a->b->c->d->e->f->g->h->i->j->k
```

要查索引 7 的节点 `h`，从头遍历要走 8 步。

跳表的解决方案是「抽索引」：

```
indexLevel   0-----------------------8-----10
indexLevel   0-----------4-----------8-----10
indexLevel   0-----2-----4-----6-----8-----10
indexLevel   0--1--2--3--4--5--6--7--8--9--10
nodeLevel    a->b->c->d->e->f->g->h->i->j->k
```

即从下往上，每一层索引的节点数大约是下一层的一半。索引高度 `H = log_2(N)`。

**查索引 7 的过程**：

1. 第 4 层（最上）：起点 `[0,8]` 包含 7 → 下降到第 3 层节点 0。
2. 第 3 层：节点 0 → `[0,4]` 不含 7 → 节点 4 → `[4,8]` 含 7 → 下降到第 2 层节点 4。
3. 第 2 层：节点 4 → `[4,6]` 不含 7 → 节点 6 → `[6,8]` 含 7 → 下降到第 1 层节点 6。
4. 第 1 层：节点 6 → `[6,7]` 含 7 → 命中节点 `h`。

每层最多移动 2 步（因为上层区间在下一层被一分为二），共 `log N` 层 → **总时间 O(log N)**。

### 索引层数分析

设链表节点数为 `N`，则索引层数 `H = ⌈log_2 N⌉`。

索引总节点数 = `N/2 + N/4 + N/8 + ... + 1 ≈ N`。也就是说，**索引层只比原始链表多用了约 1 倍空间**（常数倍），换来 O(log N) 的查询。

### 跳表的动态操作

跳表之所以能在工业级场景（Redis ZSet、LevelDB MemTable）广泛使用，关键在于它支持**动态增删且索引层能自适应**。

#### 插入：随机层高

新节点插入时，通过**随机函数**决定它的层高——最朴素的实现是「每升一层的概率为 1/2」，这样期望层高 = 1，索引总节点数 ≈ `2N`，但最坏层高可能到 log N。

```cpp
#include <bits/stdc++.h>
using namespace std;

namespace dsa {

struct SkipNode {
    int val;
    vector<SkipNode*> next;  // next[i] 指向第 i 层的下一个节点
    SkipNode(int v, int level) : val(v), next(level, nullptr) {}
};

class SkipList {
public:
    SkipList(int max_level = 16) : max_level_(max_level) {
        head_ = new SkipNode(INT_MIN, max_level_);
    }

    ~SkipList() {
        SkipNode* p = head_;
        while (p) {
            SkipNode* n = p->next.empty() ? nullptr : p->next[0];
            delete p;
            p = n;
        }
    }

    bool search(int target) const {
        SkipNode* cur = head_;
        for (int i = max_level_ - 1; i >= 0; --i) {
            while (cur->next[i] && cur->next[i]->val < target)
                cur = cur->next[i];
        }
        cur = cur->next[0];
        return cur && cur->val == target;
    }

    void add(int num) {
        vector<SkipNode*> update(max_level_, head_);
        SkipNode* cur = head_;
        for (int i = max_level_ - 1; i >= 0; --i) {
            while (cur->next[i] && cur->next[i]->val < num)
                cur = cur->next[i];
            update[i] = cur;
        }
        int lvl = random_level();
        SkipNode* node = new SkipNode(num, lvl);
        for (int i = 0; i < lvl; ++i) {
            node->next[i] = update[i]->next[i];
            update[i]->next[i] = node;
        }
    }

    void remove(int num) {
        vector<SkipNode*> update(max_level_, head_);
        SkipNode* cur = head_;
        for (int i = max_level_ - 1; i >= 0; --i) {
            while (cur->next[i] && cur->next[i]->val < num)
                cur = cur->next[i];
            update[i] = cur;
        }
        SkipNode* target = cur->next[0];
        if (!target || target->val != num) return;
        for (int i = 0; i < (int)target->next.size(); ++i)
            update[i]->next[i] = target->next[i];
        delete target;
    }

private:
    SkipNode* head_;
    int max_level_;
    mt19937 rng_{random_device{}()};

    int random_level() {
        int lvl = 1;
        // 概率 1/2 上升一层
        while (lvl < max_level_ && (rng_() & 1)) ++lvl;
        return lvl;
    }
};

} // namespace dsa
```

#### 随机层高的数学保证

设每升一层的概率 `p = 1/2`：

- 一个节点层高 `≥ 1` 的概率 = 1
- 层高 `≥ 2` 的概率 = `1/2`
- 层高 `≥ k` 的概率 = `(1/2)^(k-1)`

期望层高 = `1 + 1/2 + 1/4 + ... = 2`。索引总节点数 ≈ `2N`，查询复杂度仍为 `O(log N)`（概率意义上）。

实际工程中常用 `p = 1/4`（Redis）或 `p = 1/e`（LevelDB），进一步压低索引开销。

#### 删除：拆指针 + GC

删除和插入对称：从上往下找到每一层 `update[i]`，把 `update[i]->next[i]` 跨过目标节点即可。注意 Redis 的 ZSet 是**双向跳表**，每个节点还有 `prev[i]`，删除时同时维护反向指针。

### 跳表与 [[27-tree-map-basic|二叉搜索树]] 的对比

| 维度 | 跳表 | 自平衡 BST（AVL/红黑树） |
| --- | --- | --- |
| 时间复杂度 | O(log N) 期望 | O(log N) 最坏 |
| 实现难度 | 简单（~100 行） | 复杂（旋转/变色，500+ 行） |
| 范围查询 | ✅ 直接遍历底层链表 | ❌ 中序遍历 |
| 顺序输出 | ✅ 天然有序 | ✅ 中序遍历 |
| 内存占用 | ~2N（多 1 倍指针） | ~1N |
| 并发友好度 | ✅ 局部锁即可 | ❌ 旋转涉及祖先，锁粒度大 |
| 最坏情况 | 随机层高运气差时退化 | 永远不会退化 |

这就是 Redis ZSet 选择跳表而非红黑树的原因：实现简单 + 范围查询/顺序遍历天然 + 并发友好。

### 工业应用

- **Redis ZSet（Sorted Set）**：zadd / zrange / zrank 全部基于跳表，时间复杂度 O(log N)。
- **LevelDB / RocksDB MemTable**：用跳表做内存索引，flush 到磁盘后转为 SSTable。
- **Apache HBase 存储索引**：Region Server 内的 MemStore 用 ConcurrentSkipListMap（Java 版跳表）。
- **Apache Kafka**：每个分区的索引文件 `.index` 用跳表结构做 offset → position 映射。

### 跳表能替代 [[27-tree-map-basic|二叉搜索树]] 吗

基本可以。跳表能做到 BST 能做的几乎所有事（增删查改、范围查询、第 k 大），且实现更简单、并发更友好。**面试中如果让你实现一个「有序集合」，跳表通常是更好的选择**——除非明确要求红黑树（如 [[31-rbtree-basic|红黑树]]）。

## 📊 复杂度一览

| 操作 | 平均时间 | 最坏时间 | 空间 |
| --- | --- | --- | --- |
| 插入 | O(log N) | O(N)（随机运气差） | O(1) |
| 删除 | O(log N) | O(N) | O(1) |
| 查找 | O(log N) | O(N) | O(1) |
| 范围查询 | O(log N + k) | O(N) | O(1) |
| 整体 | — | — | ~2N |

## 🛠️ 应用场景

- **有序集合**：Redis ZSet、Java `ConcurrentSkipListMap`、C++ `std::map`（红黑树）之外的轻量选择
- **范围查询**：查找分数在 `[L, R]` 之间的所有元素
- **第 k 大 / 排行榜**：跳表底层链表天然有序
- **数据库内存索引**：LevelDB MemTable、HBase MemStore
- **分布式协调服务**：ZooKeeper / etcd 的部分内部数据结构

## ▶️ 下一章

[[21-binary-heap-basic|二叉堆核心原理及可视化]]

## 🔗 相关章节

- [[06-linkedlist-implement|链表的代码实现]]
- [[05-linkedlist-basic|链表（链式存储）的原理]]
- [[27-tree-map-basic|二叉搜索树原理及应用技巧]]
- [[31-rbtree-basic|红黑树的自平衡原理及可视化]]
- [[21-binary-heap-basic|二叉堆核心原理及可视化]]
