---
title: 二叉搜索树原理及应用技巧
tags:
  - 二叉搜索树
  - BST
  - TreeMap
  - TreeSet
  - 高级树
order: 27
prerequisites:
  - "[[23-binary-tree-basic]]"
group: 高级树
subgroup: null
paywall: false
source: https://labuladong.online/zh/algo/data-structure-basic/tree-map-basic/
---

# 二叉搜索树原理及应用技巧

## 学习目标

- 理解二叉搜索树（BST）的定义与「左小右大」性质
- 掌握 BST 上的增、删、查、改操作的时间复杂度
- 理解 TreeMap / TreeSet 是 BST 思想的具体应用
- 熟悉 TreeMap 提供的额外 API（floorKey / ceilingKey / rank / select 等）
- 理解为什么 BST 的「平衡性」直接决定了操作的效率
- 为学习 [[31-rbtree-basic|红黑树（自平衡 BST）]] 打下基础

## 一句话总结

二叉搜索树（Binary Search Tree，BST）是 [[23-binary-tree-basic|二叉树结构]] 的特例，它通过 **「左小右大」** 的约束让增删查改都达到 **O(log N)** 复杂度；它的工程化身就是 **TreeMap / TreeSet**——一种能按「键的大小」动态维护有序集合的数据结构。

## 前置知识

阅读本文前，你需要先学习：

- [[23-binary-tree-basic|二叉树基本概念及特殊二叉树]]
- [[25-n-ary-tree-traverse-basic|N 叉树的递归/层序遍历]]

## 1. 二叉搜索树的定义

二叉搜索树（BST）是一棵 **二叉树**，且对 **每个节点** 满足：

- 左子树中 **所有节点的值** 都 **小于** 该节点的值
- 右子树中 **所有节点的值** 都 **大于** 该节点的值
- 左右子树本身也分别是 BST

举例，下面就是一棵 BST：

```
        7
       / \
      4   9
     / \   \
    1   5   10
```

- 节点 7 的左子树 `{4, 1, 5}` 都 < 7；右子树 `{9, 10}` 都 > 7
- 节点 4 的左子树 `{1}` < 4；右子树 `{5}` > 4
- 节点 9 的右子树 `{10}` > 9

## 2. BST 的核心优势：O(log N) 的增删查改

### 2.1 为什么快？

普通 [[23-binary-tree-basic|二叉树]] 要找一个节点，必须 **遍历整棵树**，复杂度 O(N)。而 BST 利用「左小右大」的特性，**每访问一个节点就能砍掉一半的搜索空间**，类似二分查找：

- 想找 `target`，从 root 出发
- 如果 `target == node.val`，命中
- 如果 `target < node.val`，只可能在 **左子树** 中，递归左子树
- 如果 `target > node.val`，只可能在 **右子树** 中，递归右子树

树高是 `O(log N)`（理想情况下），所以单次查找复杂度是 **O(log N)**。

增、删、改操作都建立在「查找」的基础上：
- 改：先查找到节点，再改它的 value
- 增：先查找到「应该插入的位置」（即找到一个空位），再创建新节点挂上去
- 删：先查找到节点，再处理「删除后如何调整父子的指针」

所以三种操作也都是 **O(log N)**。

### 2.2 退化问题

理想情况下 BST 是一棵 **平衡树**（左右子树高度相近），此时高度 = `O(log N)`。

但如果按 **有序序列** 依次插入 `1, 2, 3, 4, 5, ...`，BST 会退化成 **链表**：

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
```

此时树高 = N，所有操作退化为 **O(N)**。

解决退化问题的方案就是 **自平衡 BST**——[[31-rbtree-basic|红黑树]]、AVL 树等。本节我们先讲普通 BST，下一节再讲自平衡版本。

## 3. TreeMap / TreeSet 是什么

### 3.1 概念

- **TreeMap**：键值对集合，底层是 BST，**按 key 的大小维护有序**
- **TreeSet**：键集合，底层就是一个 value 全为空的 TreeMap

和 [[13-hashmap-basic|哈希表（HashMap）]] 的对比：

| 维度 | HashMap | TreeMap |
|------|---------|---------|
| 底层结构 | 哈希表（数组 + 链表/树） | 二叉搜索树 |
| 时间复杂度（增删查改） | O(1) 平均 | O(log N) |
| 键是否有序 | ❌ 无序 | ✅ 按 key 有序 |
| 额外 API | 无 | firstKey / lastKey / floorKey / ceilingKey / rank / select / rangeKeys |
| 适用场景 | 仅需快速查 key | 需要按 key 排序、范围查询 |

### 3.2 TreeMap 的节点结构

普通 [[05-linkedlist-basic|链表]] 的 `ListNode` 只能存「值 + next 指针」；BST 的 `TreeNode` 需要存「值 + 左指针 + 右指针」；TreeMap 的节点需要存「键 + 值 + 左指针 + 右指针」：

```cpp
template <typename K, typename V>
struct TreeNode {
    K key;
    V value;
    TreeNode* left;
    TreeNode* right;
    TreeNode(K k, V v) : key(k), value(v), left(nullptr), right(nullptr) {}
};
```

### 3.3 TreeMap 的完整 API

```text
class MyTreeMap<K, V>:
    // ====== Map 键值映射的基本方法 ======
    put(K key, V value)             // 增/改，O(log N)
    V get(K key)                    // 查，O(log N)
    remove(K key)                   // 删，O(log N)
    bool containsKey(K key)         // 是否包含，O(log N)
    List<K> keys()                  // 返回所有键（有序），O(N)

    // ====== TreeMap 提供的额外方法（哈希表做不到） ======
    K firstKey()                    // 最小键，O(log N)
    K lastKey()                     // 最大键，O(log N)
    K floorKey(K key)               // ≤ key 的最大键，O(log N)
    K ceilingKey(K key)             // ≥ key 的最小键，O(log N)
    K selectKey(int k)              // 第 k 小的键（排名查询），O(log N)
    int rank(K key)                 // key 的排名，O(log N)
    List<K> rangeKeys(K low, K high) // 区间 [low, high] 内的所有键，O(log N + M)
```

最后这些「按大小关系」的 API 是 **TreeMap 独有的**，哈希表做不到（哈希表的 key 是无序的）。

## 4. BST 的核心操作

### 4.1 查找 get

```text
get(node, key):
    if node == null: return null
    if   key == node.key: return node.value
    elif key <  node.key: return get(node.left,  key)
    else:                 return get(node.right, key)
```

### 4.2 插入 put

插入的思路是「先查找插入位置，再挂新节点」：

```text
put(node, key, value):
    if node == null: return new TreeNode(key, value)
    if   key == node.key: node.value = value; return node
    elif key <  node.key: node.left  = put(node.left,  key, value)
    else:                 node.right = put(node.right, key, value)
    return node
```

### 4.3 删除 remove（最复杂）

删除有三种情况：

1. **被删节点是叶子**：直接删
2. **被删节点只有一个孩子**：用孩子替代自己
3. **被删节点有两个孩子**：找到 **右子树的最小节点**（或左子树的最大节点），用它的值顶替被删节点，然后删掉那个最小节点

```text
remove(node, key):
    if node == null: return null
    if   key <  node.key: node.left  = remove(node.left,  key)
    elif key >  node.key: node.right = remove(node.right, key)
    else:                                    // 找到 key
        if   node.left  == null: return node.right
        elif node.right == null: return node.left
        else:                                // 两个孩子
            successor = min(node.right)      // 右子树的最小节点
            node.key   = successor.key
            node.value = successor.value
            node.right = remove(node.right, successor.key)
    return node
```

`min(node)` 的实现是「一路向左走到最左下」：

```text
min(node):
    while node.left != null: node = node.left
    return node
```

## 5. 简单 C++ 实现

> [!info] 📌 概念演示
> 下面给出一个 **普通 BST 版本** 的 TreeMap 简化实现（**未做自平衡**，最坏情况会退化为 O(N)）。完整、可直接使用的版本在 [[28-tree-map-implement|下一章]] 会基于红黑树给出。

```cpp
#include <bits/stdc++.h>
using namespace std;

namespace dsa {

template <typename K, typename V>
class SimpleTreeMap {
private:
    struct Node {
        K key;
        V value;
        Node* left;
        Node* right;
        Node(K k, V v) : key(k), value(v), left(nullptr), right(nullptr) {}
    };
    Node* root = nullptr;
    int sz = 0;

    Node* put(Node* node, const K& key, const V& value) {
        if (!node) { ++sz; return new Node(key, value); }
        if (key < node->key)       node->left  = put(node->left,  key, value);
        else if (key > node->key)  node->right = put(node->right, key, value);
        else                       node->value = value;
        return node;
    }

    Node* get(Node* node, const K& key) const {
        if (!node) return nullptr;
        if      (key < node->key) return get(node->left,  key);
        else if (key > node->key) return get(node->right, key);
        else                      return node;
    }

    Node* minNode(Node* node) const {
        while (node && node->left) node = node->left;
        return node;
    }

    Node* remove(Node* node, const K& key) {
        if (!node) return nullptr;
        if (key < node->key)        node->left  = remove(node->left,  key);
        else if (key > node->key)   node->right = remove(node->right, key);
        else {
            if (!node->left)  { --sz; return node->right; }
            if (!node->right) { --sz; return node->left;  }
            Node* succ = minNode(node->right);
            node->key   = succ->key;
            node->value = succ->value;
            node->right = remove(node->right, succ->key);
        }
        return node;
    }

    void inorder(Node* node, vector<K>& out) const {
        if (!node) return;
        inorder(node->left, out);
        out.push_back(node->key);
        inorder(node->right, out);
    }

public:
    void put(const K& key, const V& value) { root = put(root, key, value); }
    bool get(const K& key, V& value) const {
        Node* n = get(root, key);
        if (!n) return false;
        value = n->value;
        return true;
    }
    void remove(const K& key) { root = remove(root, key); }
    bool containsKey(const K& key) const { return get(root, key) != nullptr; }
    int size() const { return sz; }
    vector<K> keys() const { vector<K> out; inorder(root, out); return out; }
};

} // namespace dsa

int main() {
    using namespace dsa;
    SimpleTreeMap<string, int> m;
    m.put("apple", 1);
    m.put("banana", 2);
    m.put("cherry", 3);

    int v;
    cout << (m.get("banana", v) ? to_string(v) : "not found") << endl;  // 2
    m.remove("banana");
    cout << (m.get("banana", v) ? to_string(v) : "not found") << endl;  // not found

    for (const auto& k : m.keys()) cout << k << " ";   // apple cherry
    cout << endl;
    return 0;
}
```

**输出**：

```text
2
not found
apple cherry
```

> [!warning] 重要提示
> 这个 `SimpleTreeMap` 只是为了演示 BST 的基本 API，**不保证 O(log N)**。当数据有序插入时会退化成链表。要在工程中使用，请用 [[28-tree-map-implement|基于红黑树的 TreeMap]]，即 C++ STL 的 `std::map` / `std::set`。

## 6. 复杂度表

| 操作 | 平均复杂度 | 最坏复杂度 | 备注 |
|------|-----------|-----------|------|
| get / containsKey | O(log N) | O(N) | 取决于树是否平衡 |
| put / remove | O(log N) | O(N) | 同上 |
| min / max | O(log N) | O(N) | 一路向左/右 |
| floor / ceiling | O(log N) | O(N) | 沿 BST 路径 |
| rank / select | O(N) | O(N) | 需要遍历统计子树大小 |
| 范围查询 rangeKeys | O(log N + M) | O(N + M) | M 是结果集大小 |

> [!tip] 为什么 rank / select 是 O(N)？
> 普通 BST **没有** 维护「以当前节点为根的子树有多少个节点」这个信息，所以无法在 O(log N) 内回答「排名第 k 的是谁」或「key 的排名是多少」。要支持这两个 API，需要在每个节点上额外存一个 `size` 字段（记录子树的节点数），这就是 **增强型 BST**（如 Order Statistic Tree）。

## 7. 应用场景

- **需要维护有序集合**：TreeMap / TreeSet 让你按 key 排序，Java 的 `TreeMap` / C++ 的 `std::map` / Python 的 `SortedDict` 都是这思想。
- **范围查询**：所有落在 `[low, high]` 区间的键，TreeMap 能在 O(log N + M) 内拿到（M 是结果数）。
- **滑动窗口 + 排序**：用 TreeMap 维护滑动窗口内的元素，可以同时支持 O(log N) 插入、删除、查询最值。
- **求解「中位数 / 第 k 小」**：用两个堆（[[22-binary-heap-implement|优先级队列]]）或一个增强型 BST。
- **LeetCode 经典题**：
  - [220. 存在重复元素 III](https://leetcode.cn/problems/contains-duplicate-iii/)：用 TreeSet 维护滑动窗口
  - [729. 我的日程安排表 I](https://leetcode.cn/problems/my-calendar-i/)：TreeMap 区间检测
  - [846. 一手顺子](https://leetcode.cn/problems/hand-of-straights/)：TreeMap 按 key 顺序消费

## 下一章

→ [[28-tree-map-implement|TreeMap/TreeSet 的代码实现（基于红黑树）]]

## 相关章节

- [[23-binary-tree-basic|二叉树基础]] — BST 的逻辑结构
- [[31-rbtree-basic|红黑树]] — 自平衡 BST，标准库 TreeMap 的底层
- [[13-hashmap-basic|哈希表]] — 与 TreeMap 对比：哈希表无序但 O(1)，TreeMap 有序但 O(log N)
- [[29-trie-map-basic|Trie 树]] — TreeMap 键是字符串时的特化版本
- [[22-binary-heap-implement|优先级队列]] — 另一种「按某种序维护元素」的数据结构
