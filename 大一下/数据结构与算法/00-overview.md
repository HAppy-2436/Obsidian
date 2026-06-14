---
title: 数据结构与算法 - 知识网总览
tags: [MOC, 数据结构]
---

# 数据结构与算法 - 知识网总览

> 本知识网基于 labuladong.online "基础：数据结构及排序精讲" 章节整理，共 51 个知识点（其中 17 个付费章节已由 AI 基于公开知识体系补全完整内容），每个知识点独立一个笔记，使用 Obsidian wikilink 双向链接串联。所有示例代码统一使用 C++17。

## 学习路径

按 labuladong 推荐的章节顺序学习（51 章）：

1. [[00-intro|01. 本章导读]]
2. [[01-complexity|02. 时间空间复杂度入门]]
3. [[02-array-basic|03. 数组（顺序存储）的原理]]
4. [[03-array-implement|04. 动态数组的代码实现]]
5. [[04-cycle-array|05. 循环数组技巧及实现]]
6. [[05-linkedlist-basic|06. 链表（链式存储）的原理]]
7. [[06-linkedlist-implement|07. 链表的代码实现]]
8. [[07-deque-implement|08. 双端队列（Deque）原理和实现]]
9. [[08-queue-stack-basic|09. 队列/栈的基本原理]]
10. [[09-array-queue-stack|10. 数组实现队列/栈]]
11. [[10-linked-queue-stack|11. 链表实现队列/栈]]
12. [[11-hashtable-with-array|12. 数组实现哈希表（ArrayHashMap）]]
13. [[12-hashtable-with-linked-list|13. 链表实现哈希表（LinkedHashMap）]]
14. [[13-hashmap-basic|14. 哈希表核心原理]]
15. [[14-linear-probing-key-point|15. 线性探查法的两个难点]]
16. [[15-linear-probing-code|16. 线性探查法的两种代码实现]] 🔒
17. [[16-hashtable-chaining|17. 拉链法实现哈希表]] 🔒
18. [[17-hash-set|18. 哈希集合的原理及代码实现]] 🔒
19. [[18-bitmap|19. 位图原理和实现]] 🔒
20. [[19-bloom-filter|20. 布隆过滤器原理和实现]] 🔒
21. [[20-skip-list-basic|21. 跳表原理]]
22. [[21-binary-heap-basic|22. 二叉堆核心原理及可视化]] 🔒
23. [[22-binary-heap-implement|23. 堆排序/优先级队列的代码实现]] 🔒
24. [[23-binary-tree-basic|24. 二叉树基本概念及特殊二叉树]]
25. [[24-binary-tree-traverse-basic|25. 二叉树的递归/层序遍历]]
26. [[25-n-ary-tree-traverse-basic|26. N 叉树的递归/层序遍历]] 🔒
27. [[26-segment-tree-basic|27. 线段树核心原理及可视化]] 🔒
28. [[27-tree-map-basic|28. 二叉搜索树原理及应用技巧]]
29. [[28-tree-map-implement|29. TreeMap/TreeSet 的代码实现]] 🔒
30. [[29-trie-map-basic|30. Trie/字典树/前缀树原理及可视化]]
31. [[30-union-find-basic|31. Union Find 并查集原理]]
32. [[31-rbtree-basic|32. 红黑树的自平衡原理及可视化]] 🔒
33. [[32-graph-terminology|33. 图的基本术语]]
34. [[33-graph-basic|34. 图结构的通用代码实现]] 🔒
35. [[34-graph-traverse-basic|35. 图结构的 DFS/BFS 遍历]]
36. [[35-use-case-of-dfs-bfs|36. DFS 和 BFS 的常用场景]] 🔒
37. [[36-graph-minimum-spanning-tree|37. 最小生成树算法概览]]
38. [[37-graph-shortest-path|38. 图结构最短路径算法概览]]
39. [[38-eulerian-graph|39. 欧拉图一笔画游戏]] 🔒
40. [[39-sort-basic|40. 排序算法的关键指标]]
41. [[40-bubble-sort|41. 拥有稳定性：冒泡排序]]
42. [[41-insertion-sort|42. 插入排序的链表思维]]
43. [[42-select-sort|43. 选择排序：最慢的排序]]
44. [[43-merge-sort|44. 利用后序位置：归并排序]] 🔒
45. [[44-quick-sort|45. 利用前序位置：快速排序]] 🔒
46. [[45-heap-sort|46. 堆结构妙用：堆排序]]
47. [[46-shell-sort|47. 突破 O(N^2)：希尔排序]] 🔒
48. [[47-counting-sort|48. 全新的排序原理：计数排序]]
49. [[48-bucket-sort|49. 善用区间：桶排序]]
50. [[49-radix-sort|50. 基数排序（Radix Sort）]]
51. [[50-huffman-tree|51. 数据压缩和赫夫曼编码]]

## 分组索引

### 入门
本章导读与复杂度分析

- [[00-intro|本章导读]]
- [[01-complexity|时间空间复杂度入门]]

### 数组
顺序存储：动态数组、循环数组

- [[02-array-basic|数组（顺序存储）的原理]]
- [[03-array-implement|动态数组的代码实现]]
- [[04-cycle-array|循环数组技巧及实现]]

### 链表
链式存储：单链表、双链表

- [[05-linkedlist-basic|链表（链式存储）的原理]]
- [[06-linkedlist-implement|链表的代码实现]]

### 数组链表技巧
双端队列、循环数组

- [[07-deque-implement|双端队列（Deque）原理和实现]]

### 队列/栈
FIFO/LIFO：数组/链表实现

- [[08-queue-stack-basic|队列/栈的基本原理]]
- [[09-array-queue-stack|数组实现队列/栈]]
- [[10-linked-queue-stack|链表实现队列/栈]]

### 哈希表
哈希映射：拉链法、线性探查法

- [[11-hashtable-with-array|数组实现哈希表（ArrayHashMap）]]
- [[12-hashtable-with-linked-list|链表实现哈希表（LinkedHashMap）]]
- [[13-hashmap-basic|哈希表核心原理]]
- [[14-linear-probing-key-point|线性探查法的两个难点]]
- [[15-linear-probing-code|线性探查法的两种代码实现]] 🔒 付费补全
- [[16-hashtable-chaining|拉链法实现哈希表]] 🔒 付费补全

### 哈希集合
哈希集合、位图、布隆过滤器、跳表

- [[17-hash-set|哈希集合的原理及代码实现]] 🔒 付费补全
- [[18-bitmap|位图原理和实现]] 🔒 付费补全
- [[19-bloom-filter|布隆过滤器原理和实现]] 🔒 付费补全
- [[20-skip-list-basic|跳表原理]]

### 二叉堆
堆结构、优先级队列

- [[21-binary-heap-basic|二叉堆核心原理及可视化]] 🔒 付费补全
- [[22-binary-heap-implement|堆排序/优先级队列的代码实现]] 🔒 付费补全

### 二叉树
二叉树概念、遍历

- [[23-binary-tree-basic|二叉树基本概念及特殊二叉树]]
- [[24-binary-tree-traverse-basic|二叉树的递归/层序遍历]]
- [[25-n-ary-tree-traverse-basic|N 叉树的递归/层序遍历]] 🔒 付费补全

### 高级树
线段树、搜索树、Trie、并查集、红黑树

- [[26-segment-tree-basic|线段树核心原理及可视化]] 🔒 付费补全
- [[27-tree-map-basic|二叉搜索树原理及应用技巧]]
- [[28-tree-map-implement|TreeMap/TreeSet 的代码实现]] 🔒 付费补全
- [[29-trie-map-basic|Trie/字典树/前缀树原理及可视化]]
- [[30-union-find-basic|Union Find 并查集原理]]
- [[31-rbtree-basic|红黑树的自平衡原理及可视化]] 🔒 付费补全

### 图
图基础、遍历、最短路、生成树

- [[32-graph-terminology|图的基本术语]]
- [[33-graph-basic|图结构的通用代码实现]] 🔒 付费补全
- [[34-graph-traverse-basic|图结构的 DFS/BFS 遍历]]
- [[35-use-case-of-dfs-bfs|DFS 和 BFS 的常用场景]] 🔒 付费补全
- [[36-graph-minimum-spanning-tree|最小生成树算法概览]]
- [[37-graph-shortest-path|图结构最短路径算法概览]]
- [[38-eulerian-graph|欧拉图一笔画游戏]] 🔒 付费补全

### 排序
十大排序算法

- [[39-sort-basic|排序算法的关键指标]]
- [[40-bubble-sort|拥有稳定性：冒泡排序]]
- [[41-insertion-sort|插入排序的链表思维]]
- [[42-select-sort|选择排序：最慢的排序]]
- [[43-merge-sort|利用后序位置：归并排序]] 🔒 付费补全
- [[44-quick-sort|利用前序位置：快速排序]] 🔒 付费补全
- [[45-heap-sort|堆结构妙用：堆排序]]
- [[46-shell-sort|突破 O(N^2)：希尔排序]] 🔒 付费补全
- [[47-counting-sort|全新的排序原理：计数排序]]
- [[48-bucket-sort|善用区间：桶排序]]
- [[49-radix-sort|基数排序（Radix Sort）]]

### 应用
赫夫曼编码等综合应用

- [[50-huffman-tree|数据压缩和赫夫曼编码]]

## 学习建议

1. **按章节顺序学**：每章都依赖前面章节，建议顺着 [[00-intro]] 一路读下来
2. **付费章节已补全**：带 🔒 标记的章节原网站需要 VIP，本知识网已基于算法知识体系补全完整 C++ 实现
3. **C++ 代码规范**：
   - 命名空间 `dsa`（data structures and algorithms）
   - `#include <bits/stdc++.h>`
   - 类名 PascalCase，函数名 camelCase
4. **Wikilink 串联**：用 `[[章节tag]]` 或 `[[章节tag|显示文本]]` 跳转

## 学习进度

- 总章节数：**51**
- 已生成独立笔记：**51** ✅
- 付费章节补全：**17** 🔒

## 工具栏

- [[00-intro|回到本章导读]]
- [[51-chapter-summary|查看学习总结]]
