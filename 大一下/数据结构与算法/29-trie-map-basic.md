---
title: Trie/字典树/前缀树原理及可视化
tags:
  - Trie
  - 字典树
  - 前缀树
  - 字符串
  - 高级树
order: 29
prerequisites:
  - "[[27-tree-map-basic]]"
group: 高级树
subgroup: null
paywall: false
source: https://labuladong.online/zh/algo/data-structure-basic/trie-map-basic/
---

# Trie/字典树/前缀树原理及可视化

## 学习目标

- 理解 Trie（字典树 / 前缀树）的节点结构和树形表示
- 掌握 Trie 的三个核心优势：节省空间、前缀操作、O(L) 查询
- 熟悉 TrieMap / TrieSet 的常用 API
- 理解 Trie 与 HashMap / TreeMap 的差异
- 掌握 Trie 的经典应用：自动补全、拼写检查、IP 路由

## 一句话总结

Trie（又称 **字典树 / 前缀树**）是 [[25-n-ary-tree-traverse-basic|多叉树结构]] 在「字符串」场景下的特化版本，它把每个字符作为一层，从而在 **O(L)** 时间内完成键的增删查改（L 为字符串长度），并天然支持 **前缀操作** 和 **公共前缀压缩**。

## 前置知识

阅读本文前，你需要先学习：

- [[23-binary-tree-basic|二叉树基本概念及特殊二叉树]]
- [[25-n-ary-tree-traverse-basic|N 叉树的递归/层序遍历]]
- [[27-tree-map-basic|二叉搜索树原理及应用技巧]]

## 1. Trie 是什么

Trie（取自 re**trie**val）是一种 **多叉树**，专门为「字符串集合」设计。它的特点是：

- **根节点** 不存字符
- 从根到某个节点的路径上的字符 **拼接起来** 就是该节点对应的字符串
- 一个节点可以存一个标记 `isEnd`，表示「从根到当前节点的路径是否构成一个完整的键」

举例，Trie 存储了 `{"that", "the", "them", "they", "apple"}` 这 5 个键后的结构：

```
              root
             /    \
            t      a
            |      |
            h      p
            |      |
            a ─e   p
            |  |   |
            t  m-y l
                  |
                  e
```

- 根 → t → h → a → t（isEnd = true） = "that"
- 根 → t → h → e（isEnd = true） = "the"
- 根 → t → h → e → m（isEnd = true） = "them"
- 根 → a → p → p → l → e（isEnd = true） = "apple"
- 节点 a 下还有 p → p → l → e 这条分支

## 2. Trie 的节点结构

```cpp
struct TrieNode {
    // 字符到子节点的映射：'a'~'z' 共 26 个字符
    TrieNode* children[26] = {nullptr};
    bool isEnd = false;  // 从根到当前节点的路径是否构成一个完整的键
};
```

也可以用 [[13-hashmap-basic|哈希表]] 代替数组（节省空间，但常数更大）：

```cpp
struct TrieNode {
    unordered_map<char, TrieNode*> children;
    bool isEnd = false;
};
```

如果是 [[29-trie-map-basic|TrieMap]]（存键值对而非仅键），再加一个 `V value` 字段。

## 3. Trie 的核心优势

### 3.1 节约公共前缀的存储空间

举例，往 [[13-hashmap-basic|HashMap]] 里插入 `"apple"`、`"app"`、`"appl"` 三个键：

- HashMap 真的在内存里创建了 **三份字符串** `"apple"` / `"app"` / `"appl"`，占用 5+3+4 = 12 个字符
- 重复存储了 `"app"`（3 次）和 `"l"`（2 次）

如果用 TrieMap 存，只需要存 `"apple"` 一份（5 个字符），因为 `"app"` 和 `"appl"` 都是 `"apple"` 的前缀。

> [!tip] 何时收益最大？
> 当键 **很长且共享大量公共前缀**（如身份证号、URL、IP 地址）时，Trie 的空间优势最明显。

### 3.2 方便处理前缀操作

TrieMap 天然支持「以前缀为单位的查询」，这在 [[13-hashmap-basic|HashMap]] / [[27-tree-map-basic|TreeMap]] 上做要付出极高代价：

```cpp
TrieMap<int> m;
m.put("that", 1);
m.put("the",  2);
m.put("them", 3);
m.put("apple", 4);

m.shortestPrefixOf("themxyz");  // "the"   — 最短前缀
m.longestPrefixOf("themxyz");   // "them"  — 最长前缀
m.hasKeyWithPrefix("tha");      // true    — 是否有以 "tha" 为前缀的键
m.hasKeyWithPrefix("thz");      // false
m.keysWithPrefix("th");         // ["that", "the", "them"]  — 所有 "th" 前缀的键
```

所有这些前缀操作的复杂度都是 **O(L)**，其中 L 是前缀长度；只有 `keysWithPrefix` 还需要加上结果集大小 M（遍历子树）。

| API | 复杂度 | 说明 |
|-----|--------|------|
| shortestPrefixOf | O(L) | 在 Trie 上逐字符下移，找到第一个 `isEnd=true` 的节点 |
| longestPrefixOf | O(L) | 尽量下移，能下就下 |
| hasKeyWithPrefix | O(L) | 看前缀是否是一条从根出发的路径 |
| keysWithPrefix | O(L + M) | 从前缀对应的节点出发，遍历子树（M 是子树大小） |

> [!tip] 自动补全
> `keysWithPrefix` 天然适合做 **搜索引擎的自动补全**——用户每输入一个字符，重新调用一次 `keysWithPrefix`，立即获得「以当前输入为前缀的 10 个候选词」。

### 3.3 O(L) 的增删查改

不像 HashMap 的 O(1) 是基于「哈希函数」实现的，Trie 的 O(L) 是基于「**沿着字符路径逐层下移**」：

- 插入：沿着字符串的字符逐层下移，最后一个节点标记 `isEnd = true`
- 查找：沿着字符逐层下移，**任何一层缺失**就返回 false；末尾节点 `isEnd = true` 才算找到
- 删除：找到末尾节点，`isEnd = false`；如果该节点没有子节点，可以 **自底向上删除空节点**（可选优化）

```
put("apple", 1)  →  5 次下移，每层 1 次 O(1) 查找
get("apple")     →  5 次下移
delete("apple")  →  5 次下移（O(L)）
```

## 4. TrieMap 的 C++ 实现

下面给出一个 **完整的、可编译的** TrieMap（存键值对），包含 6 个核心 API。

```cpp
#include <bits/stdc++.h>
using namespace std;

namespace dsa {

template <typename V>
class TrieMap {
private:
    struct Node {
        array<Node*, 256> children;
        V* val = nullptr;  // 用指针，nullptr 表示「不是完整键的结尾」
        bool isEnd() const { return val != nullptr; }
        Node() : children{} { children.fill(nullptr); }
        ~Node() { delete val; for (auto* c : children) delete c; }
    };
    Node* root = nullptr;
    int sz = 0;

    Node* put(Node* node, const string& s, int i, V value) {
        if (!node) node = new Node();
        if (i == s.size()) {
            if (!node->val) { node->val = new V(value); ++sz; }
            else            { *node->val = value; }
            return node;
        }
        unsigned char c = s[i];
        node->children[c] = put(node->children[c], s, i + 1, value);
        return node;
    }

    Node* getNode(Node* node, const string& s) const {
        Node* cur = node;
        for (char c : s) {
            if (!cur) return nullptr;
            cur = cur->children[(unsigned char)c];
        }
        return cur;
    }

    bool containsKey(const string& s) const {
        Node* n = getNode(root, s);
        return n && n->isEnd();
    }

    V get(const string& s) const {
        Node* n = getNode(root, s);
        if (n && n->isEnd()) return *n->val;
        throw runtime_error("not found: " + s);
    }

    vector<string> collect(Node* node, string path, vector<string>& out) const {
        if (!node) return out;
        if (node->isEnd()) out.push_back(path);
        for (int i = 0; i < 256; ++i) {
            if (node->children[i]) {
                path.push_back((char)i);
                collect(node->children[i], path, out);
                path.pop_back();
            }
        }
        return out;
    }

public:
    TrieMap() : root(nullptr) {}
    ~TrieMap() { delete root; }

    int size() const { return sz; }
    void put(const string& s, V v) { root = put(root, s, 0, v); }
    bool containsKey(const string& s) const { return containsKey(s); }
    V    get(const string& s) const { return get(s); }

    // 是否有以 prefix 为前缀的键
    bool hasKeyWithPrefix(const string& prefix) const {
        return getNode(root, prefix) != nullptr;
    }

    // 所有以 prefix 为前缀的键
    vector<string> keysWithPrefix(const string& prefix) const {
        Node* n = getNode(root, prefix);
        vector<string> out;
        if (!n) return out;
        collect(n, prefix, out);
        return out;
    }
};

} // namespace dsa

int main() {
    using namespace dsa;
    TrieMap<int> m;
    m.put("that",  1);
    m.put("the",   2);
    m.put("them",  3);
    m.put("apple", 4);

    cout << "size: " << m.size() << endl;                 // 4
    cout << "the=" << m.get("the") << endl;              // 2
    cout << "has(apple): " << m.containsKey("apple") << endl;  // 1
    cout << "has(apples): " << m.containsKey("apples") << endl; // 0

    cout << "hasPrefix(tha): " << m.hasKeyWithPrefix("tha") << endl; // 1
    cout << "hasPrefix(thz): " << m.hasKeyWithPrefix("thz") << endl; // 0

    cout << "keysWithPrefix(th): ";
    for (auto& k : m.keysWithPrefix("th")) cout << k << " ";  // that the them
    cout << endl;
    return 0;
}
```

**输出**：

```text
size: 4
the=2
has(apple): 1
has(apples): 0
hasPrefix(tha): 1
hasPrefix(thz): 0
keysWithPrefix(th): that the them
```

> [!info] 为什么用 `array<Node*, 256>` 而不是固定 26？
> `array<Node*, 256>` 是 **ASCII 全字符集**，支持任意字符（中文 UTF-8 字节也行）。如果只考虑 a-z，可以改成 `array<Node*, 26>` 节省 10 倍空间。

## 5. TrieSet

TrieSet 就是「只用 key、不用 value」的 TrieMap，所以实现是一层封装：

```cpp
class TrieSet {
private:
    TrieMap<bool> m;
public:
    void add(const string& s)        { m.put(s, true); }
    bool contains(const string& s)   { return m.containsKey(s); }
    void remove(const string& s)     { /* 略 */ }
    int  size() const                { return m.size(); }
    bool hasKeyWithPrefix(const string& p) const { return m.hasKeyWithPrefix(p); }
    vector<string> keysWithPrefix(const string& p) const { return m.keysWithPrefix(p); }
};
```

## 6. Trie vs HashMap vs TreeMap

| 维度 | Trie | HashMap | TreeMap |
|------|------|---------|---------|
| 底层 | 多叉树 | 哈希表 | BST / 红黑树 |
| 单次操作复杂度 | O(L) | O(1) | O(log N) |
| key 是否有序 | 按字典序 | 无序 | 有序 |
| 公共前缀压缩 | ✅ 天然支持 | ❌ 不支持 | ❌ 不支持 |
| 前缀查询 | ✅ O(L + M) | ❌ 必须遍历所有键 | ⚠️ O(log N + M) |
| 空间开销 | 节点指针较多 | 中 | 中 |
| 适用场景 | 字符串 + 前缀 | 任意 key + 只要快 | 任意 key + 有序 |

> [!tip] 一句话选择
> - **字符串 + 需要前缀 / 自动补全** → Trie
> - **任意 key + 速度至上** → HashMap
> - **任意 key + 范围查询** → TreeMap

## 7. 应用场景

- **自动补全 / 搜索建议**：搜索引擎、IDE 的代码补全、输入法
- **拼写检查**：编辑距离 + Trie
- **IP 路由**：把 IP 前缀存到 Trie，O(32) 完成最长前缀匹配
- **单词游戏**：Word Search、单词接龙
- **词频统计**：TrieMap 存「单词 → 出现次数」
- **T9 输入法**：把数字键映射到字符集合
- **LeetCode 经典题**：
  - [208. 实现 Trie（前缀树）](https://leetcode.cn/problems/implement-trie-prefix-tree/)
  - [211. 添加与搜索单词 - 数据结构设计](https://leetcode.cn/problems/design-add-and-search-words-data-structure/)
  - [212. 单词搜索 II](https://leetcode.cn/problems/word-search-ii/)：Trie + DFS
  - [648. 单词替换](https://leetcode.cn/problems/replace-words/)
  - [720. 词典中最长的单词](https://leetcode.cn/problems/longest-word-in-dictionary/)

## 8. Trie 的局限与变体

### 8.1 局限

- **每个节点的指针数组占空间**：即使是 `array<Node*, 26>`，N 个节点的 Trie 也需要 26N 个指针
- **常数大**：实际跑起来往往比 HashMap 慢

### 8.2 常见变体

- **压缩 Trie**（Radix Tree / Patricia Trie）：把只有一个孩子的中间节点合并
- **双数组 Trie（DAT）**：用两个数组 `base[]` 和 `check[]` 模拟 Trie 节点转移，节省空间
- **AC 自动机**：Trie + KMP 思想，多模式串匹配
- **后缀 Trie / 后缀树 / 后缀数组**：字符串后缀的特殊 Trie

## 下一章

→ [[30-union-find-basic|Union Find 并查集原理]]

## 相关章节

- [[25-n-ary-tree-traverse-basic|N 叉树遍历]] — Trie 的逻辑结构
- [[27-tree-map-basic|BST / TreeMap]] — Trie 是 TreeMap 在「字符串 + 前缀」场景下的特化
- [[13-hashmap-basic|HashMap]] — Trie 的「无前缀」替代品
- [[19-bloom-filter|布隆过滤器]] — Trie 的概率版本
