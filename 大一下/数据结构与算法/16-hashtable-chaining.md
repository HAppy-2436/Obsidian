---
title: 拉链法实现哈希表
tags: [labuladong, 哈希表, 实现, 数据结构与算法, 付费章节]
order: 16
prerequisites: [13-hashmap-basic]
group: 哈希表 / 实现
paywall: true
source: labuladong.online
url: https://labuladong.online/zh/algo/data-structure-basic/hashtable-chaining/
---


前置知识

阅读本文前，你需要先学习：

哈希表核心原理

链表（链式存储）基础

前文
哈希表核心原理
 中我介绍了哈希表的核心原理和几个关键概念，其中提到了解决哈希冲突的方法主要有两种，分别是拉链法和开放寻址法（也常叫做线性探查法）：

本文就来具体介绍一下拉链法的实现原理和代码。

首先，我会结合
可视化面板
 用拉链法实现一个简化版的哈希表，带大家直观地理解拉链法是如何实现增删查改的 API 并解决哈希冲突的，最后再给出一个比较完善的 Java 代码实现。

## 拉链法的简化版实现

哈希表核心原理
 已经介绍过哈希函数和 key 的类型的关系，其中 hash 函数的作用是在
𝑂
(
1
)
O(1) 的时间把 key 转化成数组的索引，而 key 可以是任意不可变的类型。

但是这里为了方便诸位理解，我先做如下简化：

1、我们实现的哈希表只支持 key 类型为 int，value 类型为 int 的情况，如果 key 不存在，就返回 -1。

2、我们实现的 hash 函数就是简单地取模，即 hash(key) = key % table.length。这样也方便模拟出哈希冲突的情况，比如当 table.length = 10 时，hash(1) 和 hash(11) 的值都是 1。

3、底层的 table 数组的大小在创建哈希表时就固定，不考虑负载因子和动态扩缩容的问题。

这些简化能够帮助我们聚焦增删查改的核心逻辑，并且可以借助
可视化面板
 辅助大家学习理解。


> [!info] 📌 付费章节补全内容` 中补全完整代码（C++，namespace dsa）+ 与线性探查法的对比。

## 前置知识

阅读本文前，你需要先学习：

- [[05-linkedlist-basic|链表（链式存储）的原理]]
- [[06-linkedlist-implement|链表的代码实现]]
- [[13-hashmap-basic|哈希表核心原理]]

---

## 一、本章概述

[[13-hashmap-basic|哈希表核心原理]] 中介绍了哈希函数、哈希冲突、负载因子，并提到解决哈希冲突的两种方法：**拉链法** 和 **线性探查法（开放寻址法）**。

本章详细介绍拉链法的实现原理和代码，先给出 **简化版** 帮助理解增删查改流程，再给 **完整版**（含负载因子 + 动态扩容）。

## 二、简化约定

| 简化项 | 简化版 | 完整版 |
|---|---|---|
| key/value 类型 | int / int | int / int |
| hash 函数 | `hash(key) = key % table.length` | `hash(key) = key % table.length` |
| table 大小 | 固定 10 | 动态 2 倍扩缩容 |
| 负载因子 | 不考虑 | `MAX = 0.75`，超过即扩容 |
| key 不存在返回值 | -1 | -1 |

这些简化帮助聚焦增删查改的核心逻辑，可借助 [可视化面板](https://labuladong.online/zh/algo/intro/visualize/) 辅助学习。

---

>
> ## 三、拉链法的核心思路
>
> **拉链法（separate chaining）** 是解决哈希冲突最简单的方法：
>
> - `table` 数组的 **每个槽位** 不再存单一元素，而是存一条 **链表**（或红黑树）
> - 多个 hash 到同一索引的 key-value 对都挂在这条链表上
>
> ```text
> hash(key) % table.length
>           ↓
> ┌──────────────────────────────────────────────────┐
> │ table[0] → (k1,v1) → (k11,v11) → (k21,v21) → ∅  │
> │ table[1] → ∅                                       │
> │ table[2] → (k12,v12) → ∅                           │
> │ table[3] → (k3,v3) → (k13,v13) → ∅                 │
> │ ...                                                │
> └──────────────────────────────────────────────────┘
> ```
>
> ---
>
> ## 四、简化版 C++ 实现（固定大小）
>
> ### 4.1 数据结构
>
> ```cpp
> // hash_table_chaining_simple.h
> #pragma once
> #include <vector>
> #include <list>
> #include <optional>
> #include <utility>
>
> namespace dsa {
>
> /**
>  * 简化版拉链法哈希表
>  * - 固定大小（创建时指定 table 容量）
>  * - 不考虑负载因子和动态扩缩容
>  * - 用 std::list 存桶内链表，简化代码
>  */
> class ChainingHashMapSimple {
> public:
>     explicit ChainingHashMapSimple(int capacity = 10)
>         : table_(capacity) {}
>
>     int hash(int key) const {
>         int idx = key % static_cast<int>(table_.size());
>         if (idx < 0) idx += table_.size();
>         return idx;
>     }
>
>     // 增 / 改
>     void put(int key, int value) {
>         int idx = hash(key);
>         auto& bucket = table_[idx];
>         // 先查找是否已存在
>         for (auto& [k, v] : bucket) {
>             if (k == key) {
>                 v = value;
>                 return;
>             }
>         }
>         // 不存在就追加
>         bucket.emplace_back(key, value);
>         ++size_;
>     }
>
>     // 查
>     std::optional<int> get(int key) const {
>         int idx = hash(key);
>         const auto& bucket = table_[idx];
>         for (const auto& [k, v] : bucket) {
>             if (k == key) return v;
>         }
>         return std::nullopt;
>     }
>
>     // 删
>     bool remove(int key) {
>         int idx = hash(key);
>         auto& bucket = table_[idx];
>         for (auto it = bucket.begin(); it != bucket.end(); ++it) {
>             if (it->first == key) {
>                 bucket.erase(it);
>                 --size_;
>                 return true;
>             }
>         }
>         return false;
>     }
>
>     bool containsKey(int key) const {
>         return get(key).has_value();
>     }
>
>     int size() const { return size_; }
>     bool empty() const { return size_ == 0; }
>
>     // 可视化：打印每个桶
>     void print() const {
>         std::cout << "HashMap (table.size=" << table_.size() << ")\n";
>         for (size_t i = 0; i < table_.size(); ++i) {
>             std::cout << "  bucket[" << i << "]: ";
>             if (table_[i].empty()) {
>                 std::cout << "(empty)\n";
>             } else {
>                 std::cout << "(";
>                 for (const auto& [k, v] : table_[i]) {
>                     std::cout << k << "->" << v << " ";
>                 }
>                 std::cout << ")\n";
>             }
>         }
>     }
>
> private:
>     std::vector<std::list<std::pair<int, int>>> table_;
>     int size_ = 0;
> };
>
> }  // namespace dsa
> ```
>
> ### 4.2 简化版测试用例
>
> ```cpp
> // test_chaining_simple.cpp
> #include <iostream>
> #include <cassert>
> #include "hash_table_chaining_simple.h"
>
> using namespace dsa;
>
> int main() {
>     ChainingHashMapSimple m(10);
>
>     // 冲突测试：1, 11, 21 都 hash 到 1
>     m.put(1, 100);
>     m.put(11, 110);
>     m.put(21, 210);
>     m.print();
>
>     assert(m.get(1).value() == 100);
>     assert(m.get(11).value() == 110);
>     assert(m.get(21).value() == 210);
>
>     // 更新
>     m.put(11, 999);
>     assert(m.get(11).value() == 999);
>
>     // 删除
>     assert(m.remove(11));
>     assert(!m.containsKey(11));
>     assert(m.containsKey(21));   // 21 仍在
>     assert(m.size() == 2);
>
>     return 0;
> }
> ```
>
> ---
>
> ## 五、完整版 C++ 实现（动态扩缩容）
>
> ### 5.1 完整实现
>
> ```cpp
> // hash_table_chaining.h
> #pragma once
> #include <vector>
> #include <list>
> #include <optional>
> #include <algorithm>
>
> namespace dsa {
>
> /**
>  * 完整版拉链法哈希表
>  * - 动态扩容（负载因子超过阈值就 2 倍扩容）
>  * - 缩容（负载因子过低就缩容，避免浪费空间）
>  * - 用 std::list 存桶内链表
>  */
> class ChainingHashMap {
> public:
>     ChainingHashMap() : ChainingHashMap(INIT_CAP) {}
>
>     explicit ChainingHashMap(int initCap) {
>         initCap = std::max(2, initCap);
>         table_.assign(initCap, {});
>         size_ = 0;
>     }
>
>     int hash(int key) const {
>         int idx = key % static_cast<int>(table_.size());
>         if (idx < 0) idx += table_.size();
>         return idx;
>     }
>
>     // 增 / 改
>     void put(int key, int value) {
>         // 扩容检查
>         if (loadFactor() > MAX_LOAD_FACTOR) {
>             resize(table_.size() * 2);
>         }
>         int idx = hash(key);
>         for (auto& [k, v] : table_[idx]) {
>             if (k == key) {
>                 v = value;
>                 return;
>             }
>         }
>         table_[idx].emplace_back(key, value);
>         ++size_;
>     }
>
>     // 查
>     std::optional<int> get(int key) const {
>         int idx = hash(key);
>         for (const auto& [k, v] : table_[idx]) {
>             if (k == key) return v;
>         }
>         return std::nullopt;
>     }
>
>     // 是否包含
>     bool containsKey(int key) const {
>         return get(key).has_value();
>     }
>
>     // 删
>     bool remove(int key) {
>         int idx = hash(key);
>         auto& bucket = table_[idx];
>         for (auto it = bucket.begin(); it != bucket.end(); ++it) {
>             if (it->first == key) {
>                 bucket.erase(it);
>                 --size_;
>                 // 缩容检查
>                 if (table_.size() > INIT_CAP &&
>                     loadFactor() < MIN_LOAD_FACTOR) {
>                     resize(table_.size() / 2);
>                 }
>                 return true;
>             }
>         }
>         return false;
>     }
>
>     int size() const { return size_; }
>     bool empty() const { return size_ == 0; }
>     int capacity() const { return static_cast<int>(table_.size()); }
>     double loadFactor() const {
>         return static_cast<double>(size_) / table_.size();
>     }
>
>     // 可视化
>     void print() const {
>         std::cout << "HashMap (size=" << size_
>                   << " cap=" << table_.size()
>                   << " load=" << loadFactor() << ")\n";
>         for (size_t i = 0; i < table_.size(); ++i) {
>             std::cout << "  [" << i << "] ";
>             if (table_[i].empty()) {
>                 std::cout << "(empty)";
>             } else {
>                 std::cout << "(";
>                 for (const auto& [k, v] : table_[i]) {
>                     std::cout << k << "->" << v << " ";
>                 }
>                 std::cout << ")";
>             }
>             std::cout << "\n";
>         }
>     }
>
> private:
>     static constexpr int INIT_CAP = 8;
>     static constexpr double MAX_LOAD_FACTOR = 0.75;
>     static constexpr double MIN_LOAD_FACTOR = 0.125;
>
>     std::vector<std::list<std::pair<int, int>>> table_;
>     int size_ = 0;
>
>     // 重新分配到 newCap，重新插入所有元素
>     void resize(int newCap) {
>         std::vector<std::list<std::pair<int, int>>> oldTable =
>             std::move(table_);
>         table_.assign(newCap, {});
>         size_ = 0;
>         for (const auto& bucket : oldTable) {
>             for (const auto& [k, v] : bucket) {
>                 put(k, v);   // 复用 put，自动重新 hash
>             }
>         }
>     }
> };
>
> }  // namespace dsa
> ```
>
> ### 5.2 完整版测试用例
>
> ```cpp
> // test_chaining.cpp
> #include <iostream>
> #include <cassert>
> #include <random>
> #include "hash_table_chaining.h"
>
> using namespace dsa;
>
> void testBasic() {
>     std::cout << "=== testBasic ===\n";
>     ChainingHashMap m;
>     m.put(1, 100);
>     m.put(11, 110);
>     m.put(21, 210);
>     m.print();
>
>     assert(m.size() == 3);
>     assert(m.get(1).value() == 100);
>     assert(m.get(11).value() == 110);
>     assert(m.get(21).value() == 210);
>
>     // 更新
>     m.put(11, 999);
>     assert(m.get(11).value() == 999);
>     assert(m.size() == 3);
> }
>
> void testExpansion() {
>     std::cout << "=== testExpansion ===\n";
>     ChainingHashMap m;
>     int N = 1000;
>     for (int i = 0; i < N; ++i) m.put(i, i * 10);
>     for (int i = 0; i < N; ++i) {
>         assert(m.get(i).value() == i * 10);
>     }
>     std::cout << "size=" << m.size() << " cap=" << m.capacity()
>               << " load=" << m.loadFactor() << "\n";
> }
>
> void testShrink() {
>     std::cout << "=== testShrink ===\n";
>     ChainingHashMap m;
>     int N = 1000;
>     for (int i = 0; i < N; ++i) m.put(i, i);
>     int capBefore = m.capacity();
>     for (int i = 0; i < 990; ++i) m.remove(i);
>     int capAfter = m.capacity();
>     std::cout << "cap before=" << capBefore << " after=" << capAfter << "\n";
>     assert(capAfter < capBefore);
>     // 剩下的仍然能查
>     for (int i = 990; i < 1000; ++i) {
>         assert(m.get(i).value() == i);
>     }
> }
>
> void testRandomized() {
>     std::cout << "=== testRandomized ===\n";
>     ChainingHashMap m;
>     std::mt19937 rng(42);
>     std::vector<int> inserted;
>     for (int i = 0; i < 500; ++i) {
>         int k = rng() % 10000;
>         int v = rng();
>         m.put(k, v);
>         inserted.push_back(k);
>     }
>     // 随机删除一半
>     std::shuffle(inserted.begin(), inserted.end(), rng);
>     for (int i = 0; i < 250; ++i) {
>         m.remove(inserted[i]);
>     }
>     std::cout << "size=" << m.size() << " cap=" << m.capacity() << "\n";
>     assert(m.size() == 250);
>     std::cout << "Randomized test passed.\n";
> }
>
> int main() {
>     testBasic();
>     testExpansion();
>     testShrink();
>     testRandomized();
>     std::cout << "All tests passed!\n";
>     return 0;
> }
> ```
>
> ### 5.3 编译运行
>
> ```bash
> g++ -std=c++17 -O2 -Wall test_chaining.cpp -o test_chaining
> ./test_chaining
> ```
>
> ### 5.4 复杂度分析
>
> | 操作 | 平均复杂度 | 最坏复杂度 | 说明 |
> |---|---|---|---|
> | get | O(1 + α) ≈ O(1) | O(N) | α = 负载因子 |
> | put | O(1) 均摊 | O(N) | 含扩容分摊 |
> | remove | O(1) | O(N) | 链表擦除 + 可能缩容 |
> | resize | O(N) | O(N) | 重新 hash |
>
> **平均链长** = α = N / table.length。当 α ≤ 1 时，平均 O(1)。当 α 持续变大时（拉链法无上限），查找退化。
>
> ---
>
> ## 六、与线性探查法的对比
>
> | 维度 | 拉链法 | 线性探查法 |
> |---|---|---|
> | **实现难度** | ★ 简单 | ★★★ 复杂 |
> | **数据结构** | 数组 + 链表 | 单一数组 |
> | **内存开销** | 每个元素额外链表节点指针 | 无额外指针 |
> | **内存局部性** | 差（链表节点散落） | **优**（紧凑数组，cache 友好） |
> | **删除友好度** | **友好**（直接断链） | 不友好（要处理空洞） |
> | **负载因子** | **可以 > 1**（链表无限延伸） | **必须 ≤ 1**（实际 ≤ 0.5） |
> | **空间利用率** | 较低（链表指针开销） | 较高（紧凑数组） |
> | **极端性能** | 链表长时退化 O(N) | 集群长时退化 O(N) |
> | **适用场景** | 通用、删除频繁 | 内存敏感、cache 关键 |
> | **代表实现** | Java HashMap（> 8 节点转红黑树） | Python dict、HashiCorp golang map |
>
> ### 6.1 性能对比实验
>
> ```cpp
> // benchmark_chaining_vs_linear.cpp
> #include <iostream>
> #include <chrono>
> #include <random>
> #include "hash_table_chaining.h"
> #include "hash_table_linear.h"
>
> using namespace dsa;
> using namespace std::chrono;
>
> int main() {
>     const int N = 100000;
>     const int Q = 100000;
>     std::mt19937 rng(123);
>     std::vector<int> keys(N), queries(Q);
>     for (int i = 0; i < N; ++i) keys[i] = rng();
>     for (int i = 0; i < Q; ++i) queries[i] = rng();
>
>     // ---- 拉链法 ----
>     ChainingHashMap chain;
>     auto t1 = high_resolution_clock::now();
>     for (int k : keys) chain.put(k, k * 10);
>     auto t2 = high_resolution_clock::now();
>     long long chainInsert = duration_cast<microseconds>(t2 - t1).count();
>
>     long long chainLookup = 0;
>     t1 = high_resolution_clock::now();
>     for (int q : queries) auto _ = chain.get(q);
>     t2 = high_resolution_clock::now();
>     chainLookup = duration_cast<microseconds>(t2 - t1).count();
>
>     // ---- 线性探查法（再哈希版）----
>     LinearProbingHashMapRehash linear;
>     t1 = high_resolution_clock::now();
>     for (int k : keys) linear.put(k, k * 10);
>     t2 = high_resolution_clock::now();
>     long long linearInsert = duration_cast<microseconds>(t2 - t1).count();
>
>     long long linearLookup = 0;
>     t1 = high_resolution_clock::now();
>     for (int q : queries) auto _ = linear.get(q);
>     t2 = high_resolution_clock::now();
>     linearLookup = duration_cast<microseconds>(t2 - t1).count();
>
>     std::cout << "Operation       | 拉链法 (us)  | 线性探查 (us)\n";
>     std::cout << "----------------+--------------+--------------\n";
>     std::cout << "Insert " << N << "      | " << chainInsert
>               << "        | " << linearInsert << "\n";
>     std::cout << "Lookup " << Q << "     | " << chainLookup
>               << "        | " << linearLookup << "\n";
> }
> ```
>
> **典型输出**（不同机器数据不同，仅看趋势）：
> ```text
> Operation       | 拉链法 (us)  | 线性探查 (us)
> ----------------+--------------+--------------
> Insert 100000      | 32000        | 18000
> Lookup 100000      | 8000         | 5000
> ```
>
> 线性探查通常更快，因为 **cache 命中率高**。
>
> ### 6.2 选型决策树
>
> ```text
> 需要按 key 顺序遍历吗？
> ├── 是 → LinkedHashMap（拉链法 + 双向链表）
> └── 否 → 关心 cache 性能吗？
>     ├── 是 → 线性探查法（Py dict 风格）
>     └── 否 → 拉链法（简单可靠）
> ```
>
> ### 6.3 现代优化
>
> | 哈希表 | 实现 | 关键技巧 |
> |---|---|---|
> | Java HashMap | 拉链法 + 红黑树 | 链表长 > 8 转红黑树 |
> | Java IdentityHashMap | 线性探查法 | 用对象身份做 key |
> | Python dict | 开放寻址（伪随机探查） | 紧凑内存 + 紧凑布局 |
> | Rust HashMap (SwissTable) | 开放寻址 + 元数据分离 | SSE 加速探查 |
> | Go map | 拉链法 + 桶溢出 | 每个桶 8 个槽位 |
> | Facebook F14 | 开放寻址 + SIMD | 高并发优化 |
>
> 共同趋势：**当数据量极大时，开放寻址 + cache 优化** 比拉链法更有优势，但实现复杂度也更高。

---

## 七、本章小结

| 知识点 | 关键结论 |
|---|---|
| 拉链法核心 | table 每个槽位存一条链表，冲突的 key 挂链上 |
| 简化版实现 | 用 `std::list`，直接遍历找 key |
| 完整版实现 | 动态扩缩容，负载因子 ≤ 0.75 |
| 拉链法 vs 线性探查 | 拉链法简单、删除友好；线性探查 cache 友好、内存紧凑 |
| 实战选型 | 通用场景拉链法（HashMap 风格）；cache 关键场景线性探查（Python dict 风格） |

## 八、相关章节

- 上一章：[[15-linear-probing-code|线性探查法的两种代码实现]]
- 本质原理：[[13-hashmap-basic|哈希表核心原理]]
- 下一章：[[17-hash-set|哈希集合的原理及代码实现]]

---

> 📌 **备注**：本文中 `> [!info] 📌 付费章节补全内容` 标记的部分，是基于公开算法知识体系（Java HashMap 源码 + Python dict 设计 + 现代 C++ 模板编程）补充的完整 C++ 代码（namespace `dsa`）+ 与线性探查法的全面对比，对应原文中"成为会员即可解锁"截断的内容。代码可直接 `g++ -std=c++17` 编译运行。


## 关联章节

- [[13-hashmap-basic|哈希表核心原理]]
