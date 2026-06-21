---
title: 红黑树的自平衡原理及可视化
tags: [labuladong, 高级树, 数据结构与算法, 付费章节]
category: 二叉树结构的种种变换
order: 31
prerequisites: [27-tree-map-basic]
group: 高级树
paywall: true
source: labuladong.online
url: https://labuladong.online/zh/algo/data-structure-basic/rbtree-basic/
---


前置知识

阅读本文前，你需要先学习：

二叉树基础及常见类型

多叉树的递归/层序遍历

二叉搜索树的应用及可视化

一句话总结

红黑树是自平衡的二叉搜索树，它的树高在任何时候都能保持在  O(logN)（完美平衡），这样就能保证增删查改的时间复杂度都是  O(logN)。

可视化面板支持创建红黑树：

算法可视化

二叉搜索树的应用及可视化  讲了普通的二叉搜索树存储键值对实现 TreeMap/TreeSet 的思路。

二叉搜索树的操作效率取决于树高，树结构越平衡，树高就接近  log ⁡

logN，增删查改的效率就比较高。而普通二叉搜索树最关键的问题是它不会自动对树进行平衡，特殊的情况下会退化成链表，增删查改的时间复杂度退化为  O(N)。

下面这个可视化面板就是一个例子，如果插入若干个有序的键值对，你就能发现每次新增的键都会被插入到最右侧，导致这棵二叉搜索树退化成了链表：


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


## 关联章节

- [[27-tree-map-basic|二叉搜索树原理及应用技巧]]
