# 数据结构与算法 · 王丽萍课件笔记 INDEX（高级部分 Chapter10-12 + 补充）

- 源目录：`C:\Users\Li\OneDrive\Backup\1\大一下\2024数据结构与算法wlp\历年\王丽i萍 数据结构与算法\王丽i萍 数据结构与算法\`
- 输出目录：`E:\Obsidian\Obsidian\大一下\数据结构与算法\课件笔记\王丽萍\`
- 处理文件总数：12（10 .ppt + 2 .ppt.pdf）；成功 10，失败 2
- 累计提取文本：约 13.4 万字符（成功文件）

> 提取方式：直接扫描 .ppt 二进制 OLE2 格式中的 TextCharsAtom (0x0FA0) / TextBytesAtom (0x0FA8) / TextBytesAtomAnsi (0x0FAE) / TextCharsAtomAnsi (0x0FAF) 原子，使用 0x0F9F TextContainerAtom 作为父记录校验；UTF-16LE / Latin-1 / GBK 三种编码自动适配。补充课件（.ppt.pdf 后缀实际是 PDF）用 pdfplumber 提取。

> ⚠️ 失败的两个文件（chapter10-03 平衡二分查找树 / 7.3.1 图的深度优先遍历）实际是 504 Gateway HTML 错误页面（6344 字节），并非真正的 PPT/PDF，需重新下载。


## Chapter 10 · 二叉树与平衡查找树

### [ch10-01-二叉树](Chapter10/ch10-01-二叉树.md)
- 段数：244 · 字符：16,638
- 核心概念：二叉树 (Binary Tree)、树 (Tree)、前序 / 中序 / 后序遍历、满二叉树、完全二叉树、结点度 / 深度 / 高度
- 内容要点：二叉树的递归定义、5 种基本形态、3 种遍历（前序 NLR / 中序 LNR / 后序 LRN）、线索二叉树概念、表达式树

### [ch10-02-二分查找树](Chapter10/ch10-02-二分查找树.md)
- 段数：222 · 字符：10,443
- 核心概念：二叉搜索树 / BST、查找 (Search)、插入 (Insertion)、删除 (Deletion)、中序遍历
- 内容要点：BST 性质（左 < 根 < 右）、Search/Insert 递归与非递归实现、Delete 三种情况（叶节点 / 单子树 / 双子树）、平均 / 最坏复杂度分析

### [ch10-03-AVL 树](Chapter10/ch10-03-AVL树.md)
- 段数：579 · 字符：20,653
- 核心概念：AVL 树、平衡因子 (Balance Factor)、旋转 (Rotation)、LL / LR / RR / RL 调整
- 内容要点：AVL 定义（左右子树高度差 ≤1）、4 种失衡与对应旋转、单旋转 / 双旋转、插入的 rebalance 流程、删除与重建、C++ 实现（Binary_node / AVL_node）

### [ch10-04-伸展树](Chapter10/ch10-04-伸展树.md)
- 段数：284 · 字符：11,818
- 核心概念：伸展树 (Splay Tree)、自调整、摊还分析 (Amortized Analysis)
- 内容要点：Splay 操作（zig / zig-zig / zig-zag）、将访问节点旋转到根、均摊 O(log n)、与 AVL 对比


## Chapter 11 · 多路树与多路查找树

### [ch11-01-多路树](Chapter11/ch11-01-多路树.md)
- 段数：200 · 字符：8,795
- 核心概念：多路树 (Multiway Tree)、M 阶树、度 (Degree)
- 内容要点：多路树定义、为什么需要多路树（磁盘 I/O 优化）、与二叉树的对比、相关术语

### [ch11-02-多路查找树](Chapter11/ch11-02-多路查找树.md)
- 段数：264 · 字符：15,345
- 核心概念：B 树、B+ 树、2-3 树、2-3-4 树、阶 (Order)、分裂 (Split)
- 内容要点：B-Tree 定义与性质（每个节点最多 m 个关键字、子树数 = 关键字数 +1）、B-Tree 插入与分裂、B+ 树（数据只在叶子、叶子链表）、与 B-Tree 区别


## Chapter 12 · 图基础与拓扑排序

### [ch12-01-图基础](Chapter12/ch12-01-图基础.md)
- 段数：834 · 字符：15,848
- 核心概念：图 (Graph)、有向图、无向图、邻接矩阵 (Adjacency Matrix)、邻接表 (Adjacency List)、边 (Edge)、顶点 (Vertex)
- 内容要点：图的基本定义、术语（路径 / 环 / 连通 / 强连通 / 度）、存储结构（邻接矩阵 / 邻接表）、加权图

### [ch12-02-拓扑排序](Chapter12/ch12-02-拓扑排序.md)
- 段数：185 · 字符：10,338
- 核心概念：拓扑排序 (Topological Sort)、有向无环图 (DAG)、入度 (In-degree)
- 内容要点：AOV 网络、拓扑排序算法（每次取入度为 0 的顶点）、检测环、关键路径初步


## 补充 · 图遍历与堆排序

### [supp-01-图的广度优先遍历 BFS](补充/supp-01-图的广度优先遍历.md)
- 来源：7.3.2图的广度优先遍历.ppt.pdf · 页数：51 · 字符：6,653
- 核心概念：广度优先搜索 (BFS)、队列 (Queue)、邻接表
- 内容要点：BFS 算法框架（Visited 数组 + 队列）、邻接表 + 邻接矩阵两种实现的代码、算法演示样例

### [supp-02-堆排序](补充/supp-02-堆排序.md)
- 来源：堆排序补充.ppt.pdf · 页数：18 · 字符：3,439
- 核心概念：堆 (Heap)、二叉堆、堆排序 (Heap Sort)、大顶堆 / 小顶堆
- 内容要点：堆的定义与数组表示、堆的调整（sift-down / sift-up）、建堆、堆排序步骤与复杂度


## 已失败文件（需重新下载）

### ❌ ch10-04-平衡二分查找树（源文件损坏）
- 路径：`chapter10-03/数据结构与程序设计(26)平衡二分查找树.ppt`
- 状态：6344 字节，文件实际是 Cloudflare 504 Gateway Timeout 的 HTML 错误页面（`<!DOCTYPE html>...504 Gateway time-out...`），不是真正的 PPT
- 建议：重新从原下载链接获取，或参考 BST → AVL → Splay 的笔记自行总结

### ❌ supp-03-图的深度优先遍历 DFS（PDF 损坏）
- 路径：`lzl大一下 数据结构与算法/7.3.1图的深度优先遍历.ppt.pdf`
- 状态：6344 字节，文件实际是同样的 504 HTML 错误页面
- 建议：重新下载该 PDF，或参考图基础课件 + BFS 课件中的遍历章节


## 全部核心概念（去重后汇总）

按出现频次排序（多课件共有的概念靠前）：

### 树结构基础
- 二叉树 (Binary Tree)
- 二叉搜索树 / BST
- 树 (Tree)
- 遍历（前序 Preorder / 中序 Inorder / 后序 Postorder / 层次 Level-order）
- 结点：度 / 深度 / 高度 / 父 / 子 / 兄弟 / 祖先 / 后裔

### 平衡树与自调整树
- AVL 树
- 平衡因子 (Balance Factor)
- 旋转 (Rotation)：LL / RR / LR / RL 单旋转与双旋转
- 伸展树 (Splay Tree)：zig / zig-zig / zig-zag
- 摊还分析 (Amortized Analysis)

### 多路树 / 磁盘存储
- 多路树 (Multiway Tree)
- B 树 (B-Tree)
- B+ 树 (B+ Tree)
- 2-3 树 / 2-3-4 树
- 阶 (Order)、分裂 (Split)

### 图基础
- 图 (Graph)
- 有向图 / 无向图
- 顶点 (Vertex) / 边 (Edge)
- 度 (Degree)、路径、环、连通性
- 邻接矩阵 (Adjacency Matrix)
- 邻接表 (Adjacency List)
- 加权图

### 图算法
- 深度优先搜索 (DFS)
- 广度优先搜索 (BFS)
- 拓扑排序 (Topological Sort)
- 有向无环图 (DAG)
- 入度 (In-degree)

### 堆与排序
- 堆 (Heap)
- 大顶堆 / 小顶堆
- 二叉堆 (Binary Heap)
- 堆排序 (Heap Sort)
- 优先队列 (Priority Queue)

### 通用数据结构与概念
- 数组 (Array)
- 链表 (Linked List)
- 栈 (Stack)
- 队列 (Queue)
- 递归 (Recursion)
- 时间复杂度 O(...) / 空间复杂度
- 插入 / 删除 / 查找 三种基本操作


## 学习路径建议（按王丽萍课件顺序）

1. **二叉树 → BST**：先掌握递归遍历、插入与删除
2. **AVL → Splay**：理解为什么需要平衡、平衡因子与旋转的代价
3. **多路树 → B-Tree → B+ Tree**：从磁盘 I/O 角度理解多路树的价值
4. **图基础 → DFS / BFS → 拓扑排序**：图的核心遍历与最早的应用

建议先把 chapter10-01~04 完整过一遍（树的核心），再看 chapter11（多路树）和 chapter12（图）。