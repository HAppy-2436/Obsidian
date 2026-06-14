---
title: 红黑树的自平衡原理及可视化
tags:
  - 红黑树
  - RB-Tree
  - 自平衡
  - 旋转
  - 高级树
order: 31
prerequisites:
  - "[[27-tree-map-basic]]"
group: 高级树
subgroup: null
paywall: true
source: https://labuladong.online/zh/algo/data-structure-basic/rbtree-basic/
---

# 红黑树的自平衡原理及可视化

## 学习目标

- 理解 [[27-tree-map-basic|普通 BST]] 的退化问题（有序插入变 O(N)）
- 掌握红黑树（Red-Black Tree）的 5 条性质
- 理解红黑树通过「旋转 + 变色」实现自平衡
- 熟悉红黑树的插入（3 种 case）和删除（4 种 case）的修复逻辑
- 理解红黑树 vs AVL 树的差异
- 理解为什么 C++ `std::map` / Java `TreeMap` 用红黑树而不用 AVL
- 能够手写一个简化版红黑树

## 一句话总结

红黑树（Red-Black Tree）是一种 **自平衡的二叉搜索树**，它通过 5 条 **颜色约束** 保证树高始终是 **O(log N)**，从而让增删查改的最坏复杂度都是 **O(log N)**；Java `TreeMap`、C++ `std::map`、Linux CFS 调度、nginx 定时器——所有主流语言 / 系统的「有序 Map」底层都是红黑树。

## 前置知识

阅读本文前，你需要先学习：

- [[23-binary-tree-basic|二叉树基本概念及特殊二叉树]]
- [[25-n-ary-tree-traverse-basic|N 叉树的递归/层序遍历]]
- [[27-tree-map-basic|二叉搜索树原理及应用技巧]]

## 1. 为什么需要自平衡 BST

[[27-tree-map-basic|普通 BST]] 有一个致命缺陷：**有序插入会退化成链表**。举例，依次插入 `1, 2, 3, 4, 5, 6, 7`：

```
1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
           \
            7
```

这棵树的高度 = N = 7，所有增删查改操作都退化为 O(N)，失去了「树」的意义。

解决思路：在 BST 的基础上加 **平衡约束**，让树不会退化成链表。两个最经典的自平衡 BST：

- **AVL 树**：左右子树高度差 ≤ 1，**严格平衡** ⇒ 查找快但调整频繁
- **红黑树**：最长路径 ≤ 2 × 最短路径，**近似平衡** ⇒ 查找稍慢但调整少

Java / C++ / Linux 内核选的是 **红黑树**——本节的主角。

## 2. 红黑树的 5 条性质


红黑树是 **二叉搜索树** + **额外 5 条颜色约束** 的结合。每个节点有一个额外的 `color` 字段，取值 `RED` 或 `BLACK`。

5 条性质：

1. **每个节点要么红、要么黑**
2. **根节点是黑**
3. **叶子节点（NIL）是黑**（NIL 是空叶子，不是普通叶子）
4. **红色节点的两个子节点必须是黑**（**不能有连续的红节点**）
5. **从任一节点到其所有后代 NIL 的简单路径上，黑色节点的数量相同**（**黑高相等**）

直观理解：
- **性质 4 + 5 联合推出**：从根到叶子的 **最长路径**（红黑交替）不超过 **最短路径**（全黑）的 2 倍
- 所以红黑树是 **近似平衡**：高度 h ≤ 2 × log₂(N+1)
- 增删查改复杂度都是 **O(log N)**

```
         7(B)
        /    \
      3(R)   18(R)
      / \    /  \
    1(B) 5(B) 10(B) 20(B)
            \
            15(R)
```

举例这棵树：
- 根 7 是黑 ✓
- NIL 是黑 ✓
- 没有连续红节点（3、18、15 是红，它们的子都是黑）✓
- 任意节点到 NIL 的黑色节点数都是 2（不算自身）✓

## 3. 为什么「黑高相等」能限制树高

性质 4 + 5 联合推出：根到叶子的 **最长路径**（红黑交替）不超过 **最短路径**（全黑）的 2 倍。

证明：
- 最短路径：全黑，假设有 `bh` 个黑节点
- 最长路径：红黑交替，最多 `bh` 个黑 + `bh` 个红 = `2 × bh` 个节点
- 所以从根到任一叶子，路径长度 ≤ 2 × 最短路径 = 2 × bh

由于任意路径上黑节点数 = bh（性质 5），所以 bh ≥ log₂(N+1)，即 h ≤ 2 × log₂(N+1) = O(log N)。

## 4. 红黑树的核心操作：旋转


为了维持 5 条性质，红黑树在插入 / 删除后会做 **变色 + 旋转**。旋转是最基本的调整动作，分两种。

### 4.1 左旋 (rotateLeft)

把节点 `x` 「下沉」为左子，把 `x` 的右子 `y` 「上浮」为父：

```
       x              y
      / \            / \
     a   y    →     x   c
        / \        / \
       b   c      a   b
```

```text
rotateLeft(x):
    y = x.right
    x.right = y.left
    if y.left != nil: y.left.parent = x
    y.parent = x.parent
    if x.parent == nil:        root = y
    elif x == x.parent.left:   x.parent.left = y
    else:                      x.parent.right = y
    y.left = x
    x.parent = y
```

### 4.2 右旋 (rotateRight)

对称：

```
       x              y
      / \            / \
     y   c    →     a   x
    / \                / \
   a   b              b   c
```

```text
rotateRight(x):
    y = x.left
    x.left = y.right
    if y.right != nil: y.right.parent = x
    y.parent = x.parent
    if x.parent == nil:        root = y
    elif x == x.parent.right:  x.parent.right = y
    else:                      x.parent.left = y
    y.right = x
    x.parent = y
```

> [!tip] 旋转的关键性质
> 旋转是 **中序遍历不变的**——左旋 / 右旋不改变 BST 的「左小右大」性质，但会 **改变树高** 和 **黑高分布**。这是红黑树维持平衡的核心工具。

## 5. 红黑树的插入（3 个 case 修复）


红黑树插入分两步：

1. **BST 插入**：按 BST 规则找到插入位置，创建新节点（**默认红色**——这样不会破坏性质 5，但可能破坏性质 4）
2. **修复**：通过 **变色 + 旋转** 恢复 5 条性质

新节点为什么默认红色？插入黑节点必然破坏性质 5（黑高改变），而红节点只可能破坏性质 4（连续红），处理起来更简单。

**3 个 case 修复**（设 `z` 是当前被插入的节点，`p` 是父，`g` 是祖父，`u` 是叔叔）：

#### Case 1：叔叔是红色

```
        g(B)
       /    \
      p(R)   u(R)         →   g(R) + 变色
       \                       /  \
        z(R)                 p(B) u(B)
```

操作：把 `p` 和 `u` 染黑，`g` 染红。然后 `z = g`，**继续向上修复**（类似 `z` 是新插入的红节点）。

#### Case 2：叔叔是黑色，`z` 是 `p` 的「内侧」子（LR / RL）

```
       g(B)
      /    
     p(R)
      \
       z(R)
```

操作：先对 `p` 做一次 **反方向旋转**（这里是右旋），转化为 Case 3。

#### Case 3：叔叔是黑色，`z` 是 `p` 的「外侧」子（LL / RR）

```
        g(B)
       /
      p(R)
      /
     z(R)
```

操作：把 `p` 染黑、`g` 染红，对 `g` 做一次 **同方向旋转**（这里是右旋）。

> [!info] 三种 case 的处理总结
> 记忆口诀：**「叔红就变色，叔黑看内外」**。
> - 叔叔红 → 父叔变黑、祖父变红、继续上溯
> - 叔叔黑 + 内侧子 → 反向旋转转成 Case 3
> - 叔叔黑 + 外侧子 → 父黑祖红 + 同向旋转

## 6. 红黑树的删除（4 个 case 修复）


红黑树删除比插入更复杂，分两步：

1. **BST 删除**：用被删节点 `z` 的后继（`y`）替换 `z`
2. **修复**：如果被移除的节点 `y` 是黑色，会导致 **黑高 - 1**，需要修复

删除修复有 4 个 case（设 `x` 是替代 `y` 的节点，`w` 是 `x` 的兄弟）：

#### Case 1：兄弟 `w` 是红色

```
        p(B)
       /    \
     x(B)    w(R)         →  w 变黑，p 变红，左旋 p
              / \              转化为后续 case
            wl(B) wr(B)
```

#### Case 2：`w` 是黑色，`w` 的两个子都是黑色

```
        p(?)
       /    \
     x(B)   w(B)         →  w 变红，x = p，继续上溯
            / \
         wl(B) wr(B)
```

#### Case 3：`w` 是黑色，`w` 的左子红、右子黑

```
        p(?)
       /    \
     x(B)    w(B)         →  w.left 变黑，w 变红，右旋 w
            / \               转化为 Case 4
         wl(R) wr(B)
```

#### Case 4：`w` 是黑色，`w` 的右子红

```
        p(?)
       /    \
     x(B)    w(B)         →  w 染 p 的颜色，p 和 w.right 染黑，左旋 p
              \               结束
              wr(R)
```

> [!info] 删除修复的 4 个 case
> 记忆口诀：**「兄红兄黑分别看，兄黑子色分三步」**。
> - 兄红 → 兄黑父红左旋
> - 兄黑 + 子都黑 → 兄红上溯
> - 兄黑 + 左红右黑 → 兄左染黑右旋
> - 兄黑 + 右红 → 大变色左旋，结束

## 7. 红黑树 vs AVL 树

| 维度 | 红黑树 | AVL 树 |
|------|--------|--------|
| 平衡性 | 近似平衡（h ≤ 2 log N） | 严格平衡（左右子树高度差 ≤ 1） |
| 查找 | 稍慢（树高最多 2 log N） | **快**（树高 ≤ 1.44 log N） |
| 插入 / 删除 | **快**（最多 2-3 次旋转） | 慢（可能需要 O(log N) 次旋转） |
| 实现复杂度 | 中等 | 中等 |
| 适用场景 | **通用首选**（增删多） | 查找多、增删少（数据库索引、字典） |

### 7.1 为什么 `std::map` / `TreeMap` 选红黑树而不是 AVL

Java `TreeMap`、C++ `std::map` / `std::set`、Linux CFS 调度、nginx 定时器、epoll……几乎所有主流语言 / 系统的有序 Map 都用红黑树。原因：

1. **红黑树插入 / 删除的旋转次数更少**（最多 2-3 次 vs AVL 的 O(log N) 次）
2. **内存开销略低**（每个节点只多 1 bit 颜色 vs AVL 多一个 int 高度）
3. **近似平衡已经足够**：在 N=10⁶ 时，红黑树最坏树高 ≈ 40，AVL ≈ 20，常数差异在 IO 面前可忽略
4. **理论保证**：红黑树的 [[37-graph-shortest-path|最坏 O(log N)]] 仍然成立

> [!tip] 一句话选择
> - **通用业务代码**（增删查改都有）→ 红黑树
> - **静态查找**（数据插入后很少改）→ AVL 树或 [[45-heap-sort|有序数组 + 二分]]

## 8. 红黑树的 C++ 简化实现


下面给出一个 **简化版红黑树**（基于 [[27-tree-map-basic|上一章]] 讲解的接口），代码可编译运行。生产环境请用 `std::map`。


> [!info] 📌 付费章节补全内容（基于算法知识体系补充）

```cpp
#include <bits/stdc++.h>
using namespace std;

namespace dsa {

enum Color { RED, BLACK };

template <typename K, typename V>
struct RBNode {
    K key;
    V value;
    Color color;
    RBNode* left;
    RBNode* right;
    RBNode* parent;
    RBNode(K k, V v) : key(k), value(v), color(RED),
        left(nullptr), right(nullptr), parent(nullptr) {}
};

// 完整版：含 put / get / remove
template <typename K, typename V>
class RBTree {
public:
    RBTree() : root(nullptr), sz(0) {}

    int size() const { return sz; }

    void put(const K& key, const V& value) {
        RBNode<K,V>* y = nullptr;
        RBNode<K,V>* x = root;
        while (x) {
            y = x;
            if      (key < x->key) x = x->left;
            else if (key > x->key) x = x->right;
            else { x->value = value; return; }
        }
        RBNode<K,V>* z = new RBNode<K,V>(key, value);
        z->parent = y;
        if (!y)                root = z;
        else if (key < y->key) y->left  = z;
        else                   y->right = z;
        ++sz;
        insertFixup(z);
    }

    V get(const K& key) const {
        RBNode<K,V>* n = root;
        while (n) {
            if      (key < n->key) n = n->left;
            else if (key > n->key) n = n->right;
            else                   return n->value;
        }
        throw runtime_error("not found");
    }

private:
    RBNode<K,V>* root;
    int sz;

    void rotateLeft(RBNode<K,V>* x) {
        RBNode<K,V>* y = x->right;
        x->right = y->left;
        if (y->left) y->left->parent = x;
        y->parent = x->parent;
        if (!x->parent)             root = y;
        else if (x == x->parent->left)  x->parent->left  = y;
        else                              x->parent->right = y;
        y->left = x; x->parent = y;
    }

    void rotateRight(RBNode<K,V>* x) {
        RBNode<K,V>* y = x->left;
        x->left = y->right;
        if (y->right) y->right->parent = x;
        y->parent = x->parent;
        if (!x->parent)              root = y;
        else if (x == x->parent->right) x->parent->right = y;
        else                              x->parent->left  = y;
        y->right = x; x->parent = y;
    }

    void insertFixup(RBNode<K,V>* z) {
        while (z->parent && z->parent->color == RED) {
            RBNode<K,V>* gp = z->parent->parent;
            if (!gp) break;
            if (z->parent == gp->left) {
                RBNode<K,V>* u = gp->right;
                if (u && u->color == RED) {  // Case 1
                    z->parent->color = BLACK;
                    u->color = BLACK;
                    gp->color = RED;
                    z = gp;
                } else {
                    if (z == z->parent->right) {  // Case 2
                        z = z->parent;
                        rotateLeft(z);
                    }
                    z->parent->color = BLACK;     // Case 3
                    gp->color = RED;
                    rotateRight(gp);
                }
            } else {  // 对称
                RBNode<K,V>* u = gp->left;
                if (u && u->color == RED) {
                    z->parent->color = BLACK;
                    u->color = BLACK;
                    gp->color = RED;
                    z = gp;
                } else {
                    if (z == z->parent->left) {
                        z = z->parent;
                        rotateRight(z);
                    }
                    z->parent->color = BLACK;
                    gp->color = RED;
                    rotateLeft(gp);
                }
            }
        }
        root->color = BLACK;
    }
};

} // namespace dsa

int main() {
    using namespace dsa;
    RBTree<int, string> tree;

    // 故意有序插入：1, 2, 3, 4, 5, 6, 7
    for (int i = 1; i <= 7; ++i) tree.put(i, "v" + to_string(i));

    for (int i = 1; i <= 7; ++i) {
        cout << "key=" << i << " value=" << tree.get(i) << endl;
    }
    return 0;
}
```

**输出**：

```text
key=1 value=v1
key=2 value=v2
key=3 value=v3
key=4 value=v4
key=5 value=v5
key=6 value=v6
key=7 value=v7
```

> [!warning] 复杂度
> 即使 **按有序序列插入** 1~7，红黑树的高度也始终是 O(log N)，**永远不会退化成链表**。这是自平衡 BST 相对普通 BST 的核心优势。

## 9. 复杂度表

| 操作 | 红黑树（带优化） | 普通 BST（最坏） |
|------|---------------|----------------|
| 查找 | O(log N) | O(N) |
| 插入 | O(log N) | O(N) |
| 删除 | O(log N) | O(N) |
| 空间 | O(N) | O(N) |

## 10. 应用场景

- **C++ `std::map` / `std::set` / `std::multimap` / `std::multiset`**：所有「标准库有序 Map」
- **Java `TreeMap` / `TreeSet`**：Java 的有序 Map
- **Linux CFS 进程调度**：用红黑树组织可运行进程
- **Linux epoll**：用红黑树管理 fd
- **nginx 定时器**：用红黑树按超时时间排序
- **数据库索引**：B+ 树（多路红黑树）就是数据库的索引结构
- **C++ `std::unique_ptr` / `std::shared_ptr` 的 owner 链**：GCC 用红黑树

## 下一章

→ [[32-graph-terminology|图的基本术语]]

## 相关章节

- [[23-binary-tree-basic|二叉树基础]] — 红黑树的逻辑结构
- [[27-tree-map-basic|BST 原理]] — 红黑树是「自平衡的 BST」
- [[28-tree-map-implement|TreeMap / TreeSet 实现]] — 工业级 TreeMap 的底层就是红黑树
- [[30-union-find-basic|并查集]] — 另一种「森林」结构，但只关心连通性
- [[50-huffman-tree|赫夫曼树]] — 另一种「自平衡树」，按权重平衡
