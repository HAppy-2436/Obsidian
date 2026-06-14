---
title: 二叉树的递归/层序遍历
tags:
  - 二叉树
  - DFS
  - BFS
  - 遍历
  - 前序
  - 中序
  - 后序
order: 24
prerequisites:
  - "[[23-binary-tree-basic]]"
group: 二叉树
subgroup: 遍历
paywall: false
source: https://labuladong.online/zh/algo/data-structure-basic/binary-tree-traverse-basic/
---

# 二叉树的递归/层序遍历

## 学习目标

- 理解二叉树的遍历只有 **两种本质方式**：递归遍历（DFS） + 层序遍历（BFS）
- 掌握 DFS 的代码模板，理解 **前 / 中 / 后序位置** 的差异及各自适用场景
- 掌握 BFS 的 **三种写法**（不记录层 / 记录层 / 带 State），各自适用场景
- 理解 **递归遍历节点的顺序是固定的**，「前中后序」只是把代码放在不同位置产生不同效果
- 理解 BST 的中序遍历结果是 **有序的**

## 一句话总结

二叉树只有 **递归遍历（DFS）** 和 **层序遍历（BFS）** 两种本质方式，再无其他。DFS 在框架的不同位置（前/中/后序）插入代码，会产生不同的效果；BFS 有三种写法（简单 / 记录层 / 带 State），对应不同的需求。

## 前置知识

阅读本文前，你需要先学习：

- [[23-binary-tree-basic|二叉树基本概念及特殊二叉树]]
- [[02-array-basic|数组原理]]（理解数组模拟队列）

## 1. 递归遍历（DFS）：固定顺序，三个关键位置

### 1.1 遍历框架

二叉树的递归遍历可以用一个极短的模板概括：

```cpp
#include <bits/stdc++.h>
using namespace std;

namespace dsa {

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

// 二叉树递归遍历框架（DFS 模板）
void traverse(TreeNode* root) {
    if (root == nullptr) return;

    // 前序位置：刚进入节点时
    traverse(root->left);

    // 中序位置：左子树遍历完、即将遍历右子树时
    traverse(root->right);

    // 后序位置：左右子树都遍历完，即将离开节点时
}

} // namespace dsa
```

### 1.2 遍历顺序是固定的

递归遍历节点的顺序（即 `traverse` 函数访问节点的顺序）只取决于 **左右子节点的递归调用顺序**，与其他代码无关。永远都是「先一路向左，走不动了再向右一步，再一路向左」。

> [!tip] 「前中后序」的真正含义
> 很多初学者以为前中后序是「三种不同的遍历顺序」，其实 **递归遍历节点的顺序是固定的**。所谓「前中后序」，只是 **把代码写在了 `traverse` 函数的不同位置**，所以产生了不同的效果：
>
> - **前序位置**：刚进入节点，立即执行。
> - **中序位置**：左子树遍历完、右子树遍历前，执行。
> - **后序位置**：左右子树都遍历完，即将离开节点时，执行。

### 1.3 三个位置的区别

把相同的 `cout << root->val` 放在三个位置，得到的就是前/中/后序遍历的结果：

```cpp
// 前序遍历：根 → 左 → 右
void preorder(TreeNode* root) {
    if (!root) return;
    cout << root->val << " ";   // 前序位置
    preorder(root->left);
    preorder(root->right);
}

// 中序遍历：左 → 根 → 右
void inorder(TreeNode* root) {
    if (!root) return;
    inorder(root->left);
    cout << root->val << " ";   // 中序位置
    inorder(root->right);
}

// 后序遍历：左 → 右 → 根
void postorder(TreeNode* root) {
    if (!root) return;
    postorder(root->left);
    postorder(root->right);
    cout << root->val << " ";   // 后序位置
}
```

对下面这棵树：

```
        1
       / \
      2   3
     / \   \
    4   5   6
```

三种遍历结果：

- **前序**：1 2 4 5 3 6
- **中序**：4 2 5 1 3 6
- **后序**：4 5 2 6 3 1

### 1.4 三个位置的适用场景

| 位置 | 执行时机 | 典型用途 |
|------|---------|---------|
| **前序** | 进入节点时 | 路径相关问题（如 [[27-tree-map-basic|BST 插入]]、路径和） |
| **中序** | 左子树遍历后 | BST 的有序输出、LeetCode 230「BST 第 K 小」 |
| **后序** | 离开节点时 | 子树汇总问题（如子树和、节点个数、最大深度） |

> [!warning] 算法题的关键
> 实际的算法题不是让你打印遍历顺序，而是让你把 **正确的代码写到正确的位置**。如果你不理解三个位置的差异，就无法判断「这道题应该在哪里收集答案」。

### 1.5 BST 的中序遍历是有序的

**二叉搜索树（BST）的中序遍历结果是升序序列**——这是 BST 的一个核心性质。比如 BST：

```
        4
       / \
      2   6
     / \ / \
    1  3 5  7
```

中序遍历输出：`1 2 3 4 5 6 7`。这就是 LeetCode 230「BST 中第 K 小的元素」能用中序遍历解决的原因。

## 2. 层序遍历（BFS）：三种写法

层序遍历需要借助 **队列**（[[08-queue-stack-basic|队列]]），按「一层一层、从左到右」的顺序访问节点。根据需求不同，有三种写法：

### 2.1 写法一：最简单（不记录层数）

```cpp
#include <bits/stdc++.h>
using namespace std;

void bfs_simple(TreeNode* root) {
    if (!root) return;
    queue<TreeNode*> q;
    q.push(root);
    while (!q.empty()) {
        TreeNode* cur = q.front(); q.pop();
        cout << cur->val << " ";          // 访问 cur
        if (cur->left)  q.push(cur->left);
        if (cur->right) q.push(cur->right);
    }
}
```

**优缺点**：最简单，但 **无法知道当前节点在哪一层**。多数算法题需要层数信息，所以这种写法用的不多。

### 2.2 写法二：记录层数（最常用）

在写法一的基础上，在每一轮循环开始时 **记录当前队列长度 `sz`**，这就是当前层的节点个数；遍历完一层后再 `depth++`：

```cpp
void bfs_with_depth(TreeNode* root) {
    if (!root) return;
    queue<TreeNode*> q;
    q.push(root);
    int depth = 1;  // 根节点视为第 1 层
    while (!q.empty()) {
        int sz = (int)q.size();      // 当前层的节点个数（必须先保存！）
        for (int i = 0; i < sz; ++i) {
            TreeNode* cur = q.front(); q.pop();
            cout << "depth=" << depth << " val=" << cur->val << "\n";
            if (cur->left)  q.push(cur->left);
            if (cur->right) q.push(cur->right);
        }
        depth++;
    }
}
```

**关键点**：`sz = q.size()` 必须在 `for` 循环开始前保存，因为循环过程中队列长度会变化。

> [!info] 适用场景
> 写法二可以解决「二叉树最小深度」「收集每一层的节点」「LeetCode 102 层序遍历」「LeetCode 199 右视图」等绝大多数层序遍历问题。**这是最常用的写法。**

### 2.3 写法三：带 State（最灵活，适用于加权图）

如果每条「树枝」的权重是任意值（比如图结构中的边权），同一层节点的「路径权重和」就不再相同，简单的 `depth` 变量就不够用了。这种情况下可以让每个节点 **自己携带** 路径权重和：

```cpp
struct State {
    TreeNode* node;
    int pathWeight;  // 从根到该节点的路径权重和
    State(TreeNode* n, int w) : node(n), pathWeight(w) {}
};

void bfs_with_state(TreeNode* root) {
    if (!root) return;
    queue<State> q;
    q.push(State(root, 1));  // 根节点的路径权重是 1
    while (!q.empty()) {
        State cur = q.front(); q.pop();
        cout << "weight=" << cur.pathWeight << " val=" << cur.node->val << "\n";
        if (cur.node->left)  q.push(State(cur.node->left,  cur.pathWeight + 1));
        if (cur.node->right) q.push(State(cur.node->right, cur.pathWeight + 1));
    }
}
```

**适用场景**：这种写法虽然灵活，但要额外定义 `State` 类，比较麻烦。非必要的话用写法二就够了。**真正大量用到这种写法的是 [[37-graph-shortest-path|图的最短路径算法]]**（比如 Dijkstra）。

## 3. 完整 C++ 示例：四种遍历的对比

```cpp
#include <bits/stdc++.h>
using namespace std;

namespace dsa {

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

vector<int> preorderVec, inorderVec, postorderVec, levelorderVec;

void preorder(TreeNode* root) {
    if (!root) return;
    preorderVec.push_back(root->val);   // 前序
    preorder(root->left);
    preorder(root->right);
}

void inorder(TreeNode* root) {
    if (!root) return;
    inorder(root->left);
    inorderVec.push_back(root->val);    // 中序
    inorder(root->right);
}

void postorder(TreeNode* root) {
    if (!root) return;
    postorder(root->left);
    postorder(root->right);
    postorderVec.push_back(root->val);  // 后序
}

void levelOrder(TreeNode* root) {
    if (!root) return;
    queue<TreeNode*> q;
    q.push(root);
    while (!q.empty()) {
        int sz = (int)q.size();
        for (int i = 0; i < sz; ++i) {
            TreeNode* cur = q.front(); q.pop();
            levelorderVec.push_back(cur->val);
            if (cur->left)  q.push(cur->left);
            if (cur->right) q.push(cur->right);
        }
    }
}

} // namespace dsa

int main() {
    using namespace dsa;
    // 构造:    1
    //         / \
    //        2   3
    //       / \   \
    //      4   5   6
    TreeNode* root = new TreeNode(1);
    root->left = new TreeNode(2);
    root->right = new TreeNode(3);
    root->left->left = new TreeNode(4);
    root->left->right = new TreeNode(5);
    root->right->right = new TreeNode(6);

    preorder(root);   // 1 2 4 5 3 6
    inorder(root);    // 4 2 5 1 3 6
    postorder(root);  // 4 5 2 6 3 1
    levelOrder(root); // 1 2 3 4 5 6

    cout << "前序: "; for (int x : preorderVec)    cout << x << " "; cout << "\n";
    cout << "中序: "; for (int x : inorderVec)     cout << x << " "; cout << "\n";
    cout << "后序: "; for (int x : postorderVec)   cout << x << " "; cout << "\n";
    cout << "层序: "; for (int x : levelorderVec)  cout << x << " "; cout << "\n";
    return 0;
}
```

**输出**：

```text
前序: 1 2 4 5 3 6
中序: 4 2 5 1 3 6
后序: 4 5 2 6 3 1
层序: 1 2 3 4 5 6
```

## 4. 其他「遍历」？

二叉树的遍历方式只有上面两种。也许有「用栈迭代」「递归地一层层遍历」等其他写法，但它们本质都是 **「手动维护栈模拟递归」** 或 **「用递归模拟 BFS 的层序循环」**，本质上没有跳出 DFS / BFS 这两种方式。

不要被表象迷惑：二叉树遍历 = DFS + BFS，其他都是变体。

## 5. 复杂度表

| 遍历方式 | 时间复杂度 | 空间复杂度 |
|---------|-----------|-----------|
| 前/中/后序（DFS） | O(N) | O(h)（递归栈，h = 树高） |
| 层序（BFS） | O(N) | O(w)（队列，w = 最大层宽） |
| 整棵树访问 | O(N) | O(N)（结果数组） |

在最坏情况下（树退化成链表），h = N，空间复杂度可能 O(N)；平衡二叉树中 h = O(log N)，空间复杂度稳定在 O(log N)。

## 6. 应用场景

- **DFS（前/中/后序）**：
  - [[43-merge-sort|归并排序]]（后序：先合并左右子数组，再合并到当前）
  - [[44-quick-sort|快速排序]]（前序：先 partition，再递归左右）
  - [[27-tree-map-basic|BST 增删查改]]（中序得到有序序列）
  - 回溯算法（DFS + 路径记录）
  - 动态规划（树形 DP，常见于子树汇总问题）

- **BFS（层序）**：
  - 二叉树最小深度（LeetCode 111）
  - 二叉树层序遍历（LeetCode 102）
  - 二叉树右视图（LeetCode 199）
  - [[34-graph-traverse-basic|图的 BFS 遍历]]（核心数据结构是队列）
  - 最短路径问题（在无权图中）

## 下一章

→ [[25-n-ary-tree-traverse-basic|N 叉树的递归/层序遍历]]

## 相关章节

- [[23-binary-tree-basic|二叉树基础]] — 理解节点、深度、叶子等术语
- [[34-graph-traverse-basic|图的 DFS/BFS 遍历]] — DFS/BFS 在图上的应用
- [[27-tree-map-basic|BST 原理]] — 中序遍历的特殊性质
- [[43-merge-sort|归并排序]] — 利用后序位置的典型例子
- [[44-quick-sort|快速排序]] — 利用前序位置的典型例子
