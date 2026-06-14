---
title: 数据结构速查表
tags: [Cheatsheet, 数据结构]
---

# 数据结构与算法速查表

> 一页纸复习所有数据结构的复杂度、特性和应用场景。

## 基础数据结构

| 数据结构 | 增 | 删 | 查 | 改 | 空间 | 特点 |
|----------|----|----|----|----|------|------|
| [[02-array-basic|数组]] | O(1) 末尾 / O(N) 中间 | O(N) | O(1) | O(1) | O(N) | 顺序存储、随机访问 |
| [[05-linkedlist-basic|链表]] | O(1) | O(1) 已知节点 / O(N) | O(N) | O(N) | O(N) | 链式存储、插入删除快 |
| [[09-array-queue-stack|栈]] | O(1) push | O(1) pop | O(1) top | - | O(N) | LIFO |
| [[09-array-queue-stack|队列]] | O(1) enqueue | O(1) dequeue | O(1) front | - | O(N) | FIFO |
| [[07-deque-implement|双端队列]] | O(1) 两端 | O(1) 两端 | O(1) 两端 | - | O(N) | 双向进出 |

## 哈希结构

| 数据结构 | 增删查改 | 空间 | 特点 |
|----------|----------|------|------|
| [[11-hashtable-with-array|哈希表]] | 平均 O(1)，最坏 O(N) | O(N) | key-value |
| [[17-hash-set|哈希集合]] | 平均 O(1) | O(N) | 去重 + 存在性 |
| [[18-bitmap|位图]] | O(1) | O(K) | 整数去重，节省空间 |
| [[19-bloom-filter|布隆过滤器]] | O(1) 查询（有误判） | O(N) | 允许误判的快速过滤 |
| [[20-skip-list-basic|跳表]] | O(log N) | O(N log N) | 有序集合，Redis ZSet |

## 树结构

| 数据结构 | 增 | 删 | 查 | 空间 | 特点 |
|----------|----|----|----|------|------|
| [[21-binary-heap-basic|二叉堆]] | O(log N) | O(log N) | O(1) 顶 / O(N) 其他 | O(N) | 优先级队列 |
| [[23-binary-tree-basic|二叉树]] | O(N) | O(N) | O(N) | O(N) | 通用树结构 |
| [[27-tree-map-basic|搜索树]] | O(log N)* | O(log N)* | O(log N)* | O(N) | 有序 key-value |
| [[29-trie-map-basic|Trie 树]] | O(L) | O(L) | O(L) | O(ΣNL) | 字符串前缀 |
| [[30-union-find-basic|并查集]] | 接近 O(1) | - | 接近 O(1) | O(N) | 连通性 |
| [[31-rbtree-basic|红黑树]] | O(log N) | O(log N) | O(log N) | O(N) | 自平衡搜索树 |

*平衡时

## 图结构

| 数据结构 | 存储 | 遍历 | 特点 |
|----------|------|------|------|
| [[32-graph-terminology|图]] | 邻接表 / 邻接矩阵 | [[34-graph-traverse-basic|DFS/BFS]] | 节点 + 边 |

## 排序算法

| 排序 | 最好 | 平均 | 最坏 | 空间 | 稳定 | 备注 |
|------|------|------|------|------|------|------|
| [[40-bubble-sort|冒泡]] | O(N) | O(N²) | O(N²) | O(1) | ✅ | 入门 |
| [[41-insertion-sort|插入]] | O(N) | O(N²) | O(N²) | O(1) | ✅ | 适合小数据 |
| [[42-select-sort|选择]] | O(N²) | O(N²) | O(N²) | O(1) | ❌ | 最慢的 |
| [[43-merge-sort|归并]] | O(N log N) | O(N log N) | O(N log N) | O(N) | ✅ | 分治 |
| [[44-quick-sort|快排]] | O(N log N) | O(N log N) | O(N²) | O(log N) | ❌ | 最常用 |
| [[45-heap-sort|堆排]] | O(N log N) | O(N log N) | O(N log N) | O(1) | ❌ | 原地 |
| [[46-shell-sort|希尔]] | O(N log² N) | O(N^1.3) | O(N²) | O(1) | ❌ | 插入改进 |
| [[47-counting-sort|计数]] | O(N+K) | O(N+K) | O(N+K) | O(K) | ✅ | 线性、整数 |
| [[48-bucket-sort|桶排]] | O(N+K) | O(N+K) | O(N²) | O(N+K) | ✅ | 均匀分布 |
| [[49-radix-sort|基数]] | O(DN) | O(DN) | O(DN) | O(N+K) | ✅ | 按位排序 |

## 学习路径图

```
入门 → 数组 → 链表 → 队列/栈 → 哈希 → 堆 → 二叉树 → 高级树 → 图 → 排序
 ↓      ↓      ↓       ↓        ↓      ↓       ↓         ↓       ↓      ↓
复杂度  数组  单/双链   队列   哈希表   二叉堆  遍历    线段树    术语   十大排序
基础   实现   链表    栈    哈希集   二叉堆  搜索    红黑树   遍历   应用
```

## 下一章

回到 [[00-overview|总览]] 继续学习。
