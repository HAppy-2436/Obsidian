---
title: Trie/字典树/前缀树原理及可视化
tags: [labuladong, 高级树, 数据结构与算法, 付费章节]
order: 29
prerequisites: [27-tree-map-basic]
group: 高级树
paywall: true
source: labuladong.online
url: https://labuladong.online/zh/algo/data-structure-basic/trie-map-basic/
---


前置知识

阅读本文前，你需要先学习：

二叉树基础及常见类型

一句话总结

Trie 树就是  多叉树结构  的延伸，是一种针对字符串进行特殊优化的数据结构。

Trie 树在处理字符串相关操作时有诸多优势，比如节省公共字符串前缀的内存空间、方便处理前缀操作、支持通配符匹配等。

下面这个可视化面板展示了 Trie 树的结构和主要 API，你可以逐行点击代码，观察 console 输出和右侧的 Trie 树结构变化：

算法可视化

本文仅是 Trie 树（也叫做字典树、前缀树）的原理介绍， 动手实现 TrieMap/TrieSet  我放到了 二叉树系列习题章节  后面的数据结构设计章节。理由和上篇  TreeMap/TreeSet 原理  相同，在基础知识章节我不准备讲解这种复杂结构的具体实现，初学者也没必要在这个阶段理解 Trie 树的代码实现。

但是我依然把 Trie 树的原理讲解放在这里，有两个目的：

1、让你直观地感受到二叉树结构的种种幻化，你也许能理解我的教程特别强调二叉树结构的原因了。

2、在开头让你知道有这么一种数据结构，了解它的 API 以及适用的场景。未来你遇到相关的问题，也许就能想到用 Trie 树来解决，最起码有个思路，大不了回来复制代码模板嘛。这种数据结构的实现都是固定的，笔试面试也不会让你从头手搓 Trie 树，复制粘贴直接拿去用就可以了。

好了，废话不多说，让我们开始吧。

本站将会带你实现一个 TrieMap 和 TrieSet，先来梳理一下我们已经实现过的 Map/Set 类型：

标准的  哈希表 HashMap ，底层借助一个哈希函数把键值对存在 table 数组中，有两种解决哈希冲突的方法。它的特点是快，即基本的增删查改操作时间复杂度都是  O(1)。 哈希集合 HashSet  是 HashMap 的简单封装。

哈希链表 LinkedHashMap ，是  双链表结构  对标准哈希表的加强。它继承了哈希表的操作复杂度，并且可以让哈希表中的所有键保持「插入顺序」。LinkedHashSet 是 LinkedHashMap 的简单封装。

哈希数组 ArrayHashMap ，是  数组结构  对标准哈希表的加强。它继承了哈希表的操作复杂度，并且提供了一个额外的 randomKey 函数，可以在  O(1) 的时间返回一个随机键。ArrayHashSet 是 ArrayHashMap 的简单封装。

TreeMap 映射 ，底层是一棵二叉搜索树（编程语言标准库一般使用经过改良的自平衡  红黑树 ），基本增删查改操作复杂度是  O(logN)，它的特点是可以动态维护键值对的大小关系，有很多额外的 API 操作键值对。TreeSet 集合是 TreeMap 映射的简单封装。

TrieSet 也是 TrieMap 的简单封装，所以下面我们聚焦 TrieMap 的实现原理即可。

## Trie 树的主要应用场景

Trie 树是一种针对字符串有特殊优化的数据结构，这也许它又被叫做字典树的原因。Trie 树针对字符串的处理有若干优势，下面一一列举。

### 节约存储空间

用 HashMap 对比吧，比如说这样存储几个键值对：

```
Map<String, Integer> map = new HashMap<>(); map.put("apple", 1); map.put("app", 2); map.put("appl", 3);
```

回想哈希表的实现原理，键值对会被存到 table 数组中，也就是说它真的创建 "apple"、"app"、"appl" 这三个字符串，占用了 12 个字符的内存空间。

但是注意，这三个字符串拥有共同的前缀，"app" 这个前缀被重复存储了三次，"l" 也被重复存储了两次。

如果换成 TrieMap 来存储：

```
// Trie 树的键类型固定为 String 类型，值类型可以是泛型 TrieMap<Integer> map = new TrieMap<>(); map.put("apple", 1); map.put("app", 2); map.put("appl", 3);
```

Trie 树底层并不会重复存储公共前缀，所以只需要 "apple" 这 5 个字符的内存空间来存储键。

这个例子数据量很小，你感觉重复存储几次没啥大不了，但如果键非常多、非常长，且存在大量公共前缀（现实中确实经常有这种情况，比如证件号），那么 Trie 树就能节约大量的内存空间。

### 方便处理前缀操作

举个例子就明白了：

```
// Trie 树的键类型固定为 String 类型，值类型可以是泛型 TrieMap<Integer> map = new TrieMap<>(); map.put("that", 1); map.put("the", 2); map.put("them", 3); map.put("apple", 4);

// "the" 是 "themxyz" 的最短前缀 System.out.println(map.shortestPrefixOf("themxyz")); // "the"

// "them" 是 "themxyz" 的最长前缀 System.out.println(map.longestPrefixOf("themxyz")); // "them"

// "tha" 是 "that" 的前缀 System.out.println(map.hasKeyWithPrefix("tha")); // true

// 没有以 "thz" 为前缀的键 System.out.println(map.hasKeyWithPrefix("thz")); // false

// "that", "the", "them" 都是 "th" 的前缀 System.out.println(map.keysWithPrefix("th")); // ["that", "the", "them"]
```

除了 keysWithPrefix 方法的复杂度取决于返回结果的长度，其他前缀操作的复杂度都是  O(L)，其中

L 是前缀字符串长度。

你想想上面这几个操作，用 HashMap 或者 TreeMap 能做到吗？应该只能强行遍历所有键，然后一个个比较字符串前缀，复杂度非常高。

话说，这个 keysWithPrefix 方法，是不是很适合做自动补全功能呢？


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

## 关联章节

- [[27-tree-map-basic|二叉搜索树原理及应用技巧]]
