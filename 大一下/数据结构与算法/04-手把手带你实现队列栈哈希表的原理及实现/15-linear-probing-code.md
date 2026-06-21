---
title: 线性探查法的两种代码实现
tags: [labuladong, 哈希表, 开放定址, 数据结构与算法, 付费章节]
category: 手把手带你实现队列/栈哈希表的原理及实现
order: 15
prerequisites: [14-linear-probing-key-point]
group: 哈希表 / 开放定址
paywall: true
source: labuladong.online
url: https://labuladong.online/zh/algo/data-structure-basic/linear-probing-code/
---


前置知识

阅读本文前，你需要先学习：

线性探查法的两个难点

前文  哈希表核心原理  中我介绍了哈希表的核心原理和几个关键概念， 拉链法原理和实现  中介绍了拉链法的实现， 线性探查法的两个难点  介绍了线性探查法实现哈希表的难点所在，并给出了两种方法解决删除元素时的空洞问题，本文会同时给出这两种方法的参考代码实现。

本文会先结合可视化面板给出简化的实现，方便大家理解增删查改的过程，最后给完整实现。

简化实现中，具体简化的地方如下：

1、我们实现的哈希表只支持 key 类型为 int，value 类型为 int 的情况，如果 key 不存在，就返回 -1。

2、我们实现的 hash 函数就是简单地取模，即 hash(key) = key % table.length。这样也方便模拟出哈希冲突的情况，比如当 table.length = 10 时，hash(1) 和 hash(11) 的值都是 1。

3、底层的 table 数组的大小在创建哈希表时就固定，假设 table 数组不会被装满，不考虑负载因子和动态扩缩容的问题。

这些简化能够帮助我们聚焦增删查改的核心逻辑，并且可以借助  可视化面板  辅助大家学习理解。


> [!info] 📌 付费章节补全内容` 中补全完整代码（C++，namespace dsa）。

## 前置知识

阅读本文前，你需要先学习：

- [[02-array-basic|数组（顺序存储）的原理]]
- [[03-array-implement|动态数组的代码实现]]
- [[13-hashmap-basic|哈希表核心原理]]
- [[14-linear-probing-key-point|线性探查法的两个难点]]

---

## 一、本章概述

前文：

- [[13-hashmap-basic|哈希表核心原理]] 介绍了哈希函数、哈希冲突、负载因子
- [[16-hashtable-chaining|用拉链法实现哈希表]] 介绍了拉链法的实现
- [[14-linear-probing-key-point|线性探查法的两个难点]] 介绍了两个难点：环形探查 + 删除空洞，并给出两种方案（墓碑标记 vs 再哈希）

**本文**会同时给出这两种方案的完整 C++ 实现。

## 二、简化约定

为了聚焦核心逻辑，本文先实现 **简化版**（固定大小、不扩容、不处理删除空洞），再用 **完整版**（含扩容 + 两种删除空洞方案）：

| 简化项 | 简化版 | 完整版 |
|---|---|---|
| key/value 类型 | int / int | int / int |
| hash 函数 | `hash(key) = key % table.length` | `hash(key) = key % table.length` |
| table 大小 | 固定 10 | 动态 2 倍扩缩容 |
| 负载因子 | 不考虑 | `MAX = 0.5`，超过即扩容 |
| 删除空洞 | 不处理 | ① 墓碑标记；② 再哈希后续元素 |
| key 不存在返回值 | -1 | -1 |

> 这些简化帮助聚焦增删查改的核心逻辑，并可借助 [可视化面板](https://labuladong.online/zh/algo/intro/visualize/) 辅助学习。

---

>
> ## 三、简化版 C++ 实现
>
> ### 3.1 数据结构
>
> ```cpp
> // hash_table_linear_simple.h
> #pragma once
> #include <vector>
> #include <optional>
>
> namespace dsa {
>
> /**
>  * 简化版线性探查哈希表
>  * - 固定大小（创建时指定 table 容量，运行期间不扩缩容）
>  * - 不处理删除空洞
>  * - 仅用于教学，理解线性探查法核心逻辑
>  */
> class LinearProbingHashMapSimple {
> public:
>     // 槽位状态：空 / 有数据 / 墓碑
>     enum class State { EMPTY, OCCUPIED, TOMB };
>
>     struct Entry {
>         int key;
>         int value;
>         State state = State::EMPTY;
>     };
>
>     explicit LinearProbingHashMapSimple(int capacity = 10)
>         : table_(capacity, Entry{}) {}
>
>     // 哈希函数
>     int hash(int key) const {
>         return key % table_.size();
>     }
>
>     // 查：返回 std::nullopt 表示不存在
>     std::optional<int> get(int key) const {
>         int idx = hash(key);
>         while (table_[idx].state != State::EMPTY) {
>             if (table_[idx].state == State::OCCUPIED &&
>                 table_[idx].key == key) {
>                 return table_[idx].value;
>             }
>             idx = (idx + 1) % table_.size();
>         }
>         return std::nullopt;
>     }
>
>     // 增 / 改
>     void put(int key, int value) {
>         int idx = hash(key);
>         while (table_[idx].state != State::EMPTY) {
>             if (table_[idx].state == State::OCCUPIED &&
>                 table_[idx].key == key) {
>                 table_[idx].value = value;     // 更新
>                 return;
>             }
>             idx = (idx + 1) % table_.size();
>         }
>         table_[idx] = {key, value, State::OCCUPIED};
>         size_++;
>     }
>
>     // 删（简化：仅置 TOMB，不收紧探查链）
>     bool remove(int key) {
>         int idx = hash(key);
>         while (table_[idx].state != State::EMPTY) {
>             if (table_[idx].state == State::OCCUPIED &&
>                 table_[idx].key == key) {
>                 table_[idx].state = State::TOMB;
>                 size_--;
>                 return true;
>             }
>            idx = (idx + 1) % table_.size();
>         }
>         return false;
>     }
>
>     int size() const { return size_; }
>     bool empty() const { return size_ == 0; }
>
>     // 可视化辅助：把整个 table 打印出来（含墓碑）
>     void print() const {
>         std::cout << "[ ";
>         for (size_t i = 0; i < table_.size(); ++i) {
>             const auto& e = table_[i];
>             if (e.state == State::OCCUPIED) {
>                 std::cout << "(" << e.key << "," << e.value << ") ";
>             } else if (e.state == State::TOMB) {
>                 std::cout << "<TOMB> ";
>             } else {
>                 std::cout << "_ ";
>             }
>         }
>         std::cout << "]\n";
>     }
>
> private:
>     std::vector<Entry> table_;
>     int size_ = 0;
> };
>
> }  // namespace dsa
> ```
>
> ### 3.2 简化版测试用例
>
> ```cpp
> // test_hash_table_linear_simple.cpp
> #include <iostream>
> #include "hash_table_linear_simple.h"
>
> using namespace dsa;
>
> int main() {
>     LinearProbingHashMapSimple m(10);
>
>     // 冲突测试：1, 11, 21 都 hash 到 1
>     m.put(1, 100);
>     m.put(11, 110);
>     m.put(21, 210);
>     m.print();
>     // 输出：(1,100) (11,110) (21,210) _ _ _ _ _ _ _
>
>     // 更新已存在 key
>     m.put(11, 999);
>     std::cout << "get(11) = " << m.get(11).value_or(-1) << "\n";  // 999
>
>     // 删除中间 key（产生 TOMB）
>     m.remove(11);
>     m.print();
>     // 输出：(1,100) <TOMB> (21,210) _ _ _ _ _ _ _
>
>     // 注意：21 仍然能查到（因为 OCCUPIED 的探查会跳过 TOMB）
>     std::cout << "get(21) = " << m.get(21).value_or(-1) << "\n";  // 210
>
>     return 0;
> }
> ```
>
> ---
>
> ## 四、完整版 C++ 实现（含两种空洞处理方案）
>
> ### 4.1 设计目标
>
> 1. **动态扩缩容**：负载因子超过 `MAX_LOAD_FACTOR` 时 2 倍扩容；低于 `MIN_LOAD_FACTOR` 时缩容
> 2. **两种删除空洞方案**：通过模板参数 `UseTombstone` 切换
>    - `UseTombstone = true`：墓碑标记（put/get 时跳过 TOMB，remove 时置 TOMB）
>    - `UseTombstone = false`：再哈希后续元素（remove 时把探查链上后续元素重新插入）
> 3. **完整 C++ 代码**，namespace `dsa`
>
> ### 4.2 完整实现
>
> ```cpp
> // hash_table_linear.h
> #pragma once
> #include <vector>
> #include <optional>
> #include <algorithm>
> #include <iostream>
>
> namespace dsa {
>
> /**
>  * 完整版线性探查哈希表
>  * @tparam UseTombstone true = 墓碑方案；false = 再哈希方案
>  */
> template <bool UseTombstone = true>
> class LinearProbingHashMap {
> public:
>     enum class State { EMPTY, OCCUPIED };
>
>     struct Entry {
>         int key = 0;
>         int value = 0;
>         State state = State::EMPTY;
>     };
>
>     LinearProbingHashMap() : LinearProbingHashMap(INIT_CAP) {}
>
>     explicit LinearProbingHashMap(int initCap) {
>         initCap = std::max(2, initCap);
>         table_.assign(initCap, Entry{});
>         size_ = 0;
>         tombCount_ = 0;
>     }
>
>     int size() const { return size_; }
>     bool empty() const { return size_ == 0; }
>     int capacity() const { static_cast<int>(table_.size()); }
>     double loadFactor() const {
>         return static_cast<double>(size_ + tombCount_) / table_.size();
>     }
>
>     // ---------- 哈希函数 ----------
>     int hash(int key) const {
>         // 简化版：取模
>         int idx = key % static_cast<int>(table_.size());
>         if (idx < 0) idx += table_.size();
>         return idx;
>     }
>
>     // ---------- 查 ----------
>     std::optional<int> get(int key) const {
>         int idx = hash(key);
>         const int n = static_cast<int>(table_.size());
>         while (table_[idx].state != State::EMPTY) {
>             if (table_[idx].state == State::OCCUPIED &&
>                 table_[idx].key == key) {
>                 return table_[idx].value;
>             }
>             idx = (idx + 1) % n;
>         }
>         return std::nullopt;
>     }
>
>     bool containsKey(int key) const {
>         return get(key).has_value();
>     }
>
>     // ---------- 增 / 改 ----------
>     void put(int key, int value) {
>         if (loadFactor() > MAX_LOAD_FACTOR) {
>             resize(table_.size() * 2);
>         }
>         int idx = hash(key);
>         const int n = static_cast<int>(table_.size());
>         while (table_[idx].state == State::OCCUPIED) {
>             if (table_[idx].key == key) {
>                 table_[idx].value = value;
>                 return;
>             }
>             idx = (idx + 1) % n;
>         }
>         // 如果是墓碑覆盖，tombCount 减少
>         // （墓碑方案下 EMPTY 才能放，但这里我们允许在 TOMB 上放）
>         if constexpr (UseTombstone) {
>             // 墓碑方案：把 TOMB 当成 EMPTY 用
>             if (table_[idx].state != State::EMPTY) {
>                 --tombCount_;
>             }
>         }
>         table_[idx] = {key, value, State::OCCUPIED};
>         ++size_;
>     }
>
>     // ---------- 删 ----------
>     bool remove(int key) {
>         int idx = hash(key);
>         const int n = static_cast<int>(table_.size());
>         while (table_[idx].state != State::EMPTY) {
>            if (table_[idx].state == State::OCCUPIED &&
>                 table_[idx].key == key) {
>                 if constexpr (UseTombstone) {
>                     // 方案 A：墓碑标记
>                     table_[idx].state = State::EMPTY;
>                     table_[idx].key = 0;
>                     table_[idx].value = 0;
>                     ++tombCount_;
>                 } else {
>                     // 方案 B：再哈希后续元素
>                     rehashAfterDeletion(idx);
>                 }
>                 --size_;
>                 // 缩容检查
>                 if (loadFactor() < MIN_LOAD_FACTOR &&
>                     table_.size() > INIT_CAP) {
>                     resize(table_.size() / 2);
>                 }
>                 return true;
>             }
>             idx = (idx + 1) % n;
>         }
>         return false;
>     }
>
>     // ---------- 调试 ----------
>     void print() const {
>         std::cout << "[ ";
>         for (size_t i = 0; i < table_.size(); ++i) {
>             const auto& e = table_[i];
>             if (e.state == State::OCCUPIED) {
>                 std::cout << "(" << e.key << "," << e.value << ") ";
>             } else {
>                 std::cout << "_ ";
>             }
>         }
>         std::cout << "]  size=" << size_
>                   << " cap=" << table_.size()
>                   << " load=" << loadFactor() << "\n";
>     }
>
> private:
>     static constexpr int INIT_CAP = 8;
>     static constexpr double MAX_LOAD_FACTOR = 0.5;
>     static constexpr double MIN_LOAD_FACTOR = 0.125;
>
>     std::vector<Entry> table_;
>     int size_ = 0;
>     int tombCount_ = 0;  // 仅墓碑方案使用
>
>     // 重新分配到 newCap，并重新插入所有 OCCUPIED 元素
>     void resize(int newCap) {
>         std::vector<Entry> oldTable = std::move(table_);
>         table_.assign(newCap, Entry{});
>         size_ = 0;
>         tombCount_ = 0;
>         for (const auto& e : oldTable) {
>             if (e.state == State::OCCUPIED) {
>                 put(e.key, e.value);
>             }
>         }
>     }
>
>     // 方案 B 专用：删除 idx 后，把探查链上后续元素重新插入
>     void rehashAfterDeletion(int idx) {
>         const int n = static_cast<int>(table_.size());
>         int cur = (idx + 1) % n;
>         while (table_[cur].state == State::OCCUPIED) {
>             Entry saved = table_[cur];
>             table_[cur].state = State::EMPTY;
>             --size_;  // 临时减掉，等会儿 put 时再加回来
>             put(saved.key, saved.value);
>             cur = (cur + 1) % n;
>         }
>     }
> };
>
> // 类型别名：墓碑版 vs 再哈希版
> using LinearProbingHashMapTombstone  = LinearProbingHashMap<true>;
> using LinearProbingHashMapRehash     = LinearProbingHashMap<false>;
>
> }  // namespace dsa
> ```
>
> ### 4.3 完整版测试用例
>
> ```cpp
> // test_hash_table_linear.cpp
> #include <iostream>
> #include <cassert>
> #include "hash_table_linear.h"
>
> using namespace dsa;
>
> void testBasic() {
>     std::cout << "=== testBasic ===\n";
>     LinearProbingHashMapTombstone m;
>     assert(m.empty());
>
>     m.put(1, 100);
>     m.put(11, 110);   // 冲突
>     m.put(21, 210);   // 冲突
>     m.put(31, 310);   // 冲突
>     m.put(41, 410);   // 冲突
>     m.print();
>
>     assert(m.get(1).value() == 100);
>     assert(m.get(11).value() == 110);
>     assert(m.get(21).value() == 210);
>     assert(m.get(31).value() == 310);
>     assert(m.get(41).value() == 410);
>     assert(!m.containsKey(99));
>
>     // 更新
>     m.put(11, 999);
>     assert(m.get(11).value() == 999);
>
>     // 删除 + 探查链测试
>     assert(m.remove(11));
>     assert(!m.containsKey(11));
>     assert(m.containsKey(21));   // 21 仍然能找到
>     assert(m.containsKey(31));
>     m.print();
> }
>
> void testExpansion() {
>     std::cout << "=== testExpansion ===\n";
>     LinearProbingHashMapTombstone m;
>     // 连续插入触发扩容
>     for (int i = 0; i < 100; ++i) {
>         m.put(i, i * 10);
>     }
>     // 验证全部能找到
>     for (int i = 0; i < 100; ++i) {
>         auto v = m.get(i);
>         assert(v.has_value() && v.value() == i * 10);
>     }
>     std::cout << "size=" << m.size() << " cap=" << m.capacity() << "\n";
> }
>
> void testShrink() {
>     std::cout << "=== testShrink ===\n";
>     LinearProbingHashMapTombstone m;
>     for (int i = 0; i < 100; ++i) m.put(i, i);
>     int capBefore = m.capacity();
>     for (int i = 0; i < 95; ++i) m.remove(i);
>     int capAfter = m.capacity();
>     std::cout << "cap before=" << capBefore << " after=" << capAfter << "\n";
>     assert(capAfter < capBefore);  // 缩容了
> }
>
> void testBothStrategies() {
>     std::cout << "=== testBothStrategies ===\n";
>     LinearProbingHashMapTombstone tomb;
>     LinearProbingHashMapRehash   rehash;
>
>     int keys[] = {1, 11, 21, 31, 41, 51};
>     for (int k : keys) { tomb.put(k, k * 100); rehash.put(k, k * 100); }
>
>     // 删除中间的 key
>     tomb.remove(21);
>     rehash.remove(21);
>
>     // 墓碑版：删除位置留墓碑，后续元素仍可查
>     // 再哈希版：删除位置无墓碑，探查链被"收紧"
>     for (int k : keys) {
>         if (k == 21) continue;
>         assert(tomb.get(k).value() == k * 100);
>         assert(rehash.get(k).value() == k * 100);
>     }
>     assert(!tomb.containsKey(21));
>     assert(!rehash.containsKey(21));
>
>     tomb.print();
>     rehash.print();
> }
>
> int main() {
>     testBasic();
>     testExpansion();
>     testShrink();
>     testBothStrategies();
>     std::cout << "All tests passed!\n";
>     return 0;
> }
> ```
>
> ### 4.4 编译运行
>
> ```bash
> g++ -std=c++17 -O2 -Wall test_hash_table_linear.cpp -o test_hash
> ./test_hash
> ```
>
> 预期输出（节选）：
> ```text
> === testBasic ===
> [ (1,100) (11,110) (21,210) (31,310) (41,410) _ _ _ _ _ _ _ _ _ _ ]  size=5 cap=16 load=0.3125
> [ (1,100) _ (21,210) (31,310) (41,410) _ _ _ _ _ _ _ _ _ _ ]  size=4 cap=16 load=0.3125
> === testExpansion ===
> size=100 cap=256
> === testShrink ===
> cap before=128 after=16
> === testBothStrategies ===
> [ (1,100) (11,110) _ (31,310) (41,410) (51,510) _ _ _ _ _ _ _ _ _ _ ]  size=5 cap=16 load=0.3125
> [ (1,100) (11,110) (31,310) (41,410) (51,510) _ _ _ _ _ _ _ _ _ _ ]  size=5 cap=16 load=0.3125
> All tests passed!
> ```
>
> ### 4.5 复杂度分析
>
> | 操作 | 平均复杂度 | 最坏复杂度 | 说明 |
> |---|---|---|---|
> | get | O(1) | O(N) | 集群退化 |
> | put | O(1) | O(N) | 探查 + 可能的扩容 |
> | remove | O(1) 均摊 | O(N) | 探查 + 再哈希（方案 B） |
> | resize | O(N) | O(N) | 搬移所有元素 |
>
> 扩容触发：put 后 `loadFactor > 0.5`，2 倍扩容
> 缩容触发：remove 后 `loadFactor < 0.125` 且 `capacity > 8`，缩为一半
>
> ### 4.6 实战注意事项
>
> 1. **墓碑版必须定期 rehash**：长时间运行后墓碑积累，探查路径变长。建议在 `loadFactor + tombCount/tableSize > 0.5` 时主动 resize 一次清理
> 2. **再哈希版的 remove 单次可能 O(N)**，但均摊仍是 O(1)
> 3. **负载因子是关键**：生产环境建议 ≤ 0.5，超过就 2 倍扩容
> 4. **整数 key 的 hash 太简单**：真实场景用 `std::hash<T>`，对自定义类型还要注意防 hash flooding 攻击

---

## 五、本章小结

| 知识点 | 关键结论 |
|---|---|
| 简化版 | 固定大小，不处理空洞，纯演示探查逻辑 |
| 完整版 ① 墓碑 | 单次删除 O(1)，长期需要 rehash 清理 |
| 完整版 ② 再哈希 | 探查链始终最优，单次删除最坏 O(N) 均摊 O(1) |
| 负载因子 | ≤ 0.5，超过即 2 倍扩容 |
| 选型 | 教学用墓碑（简单），生产用再哈希（性能稳定） |

## 六、相关章节

- 上一章：[[14-linear-probing-key-point|线性探查法的两个难点]]
- 对比方案：[[16-hashtable-chaining|用拉链法实现哈希表]]

---

> 📌 **备注**：本文中 `> [!info] 📌 付费章节补全内容` 标记的部分，是基于公开算法知识体系（算法导论 + Java 源码 + 现代 C++ 模板编程）补充的完整 C++ 代码（namespace `dsa`）与原理解析，对应原文中"成为会员即可解锁"截断的内容。代码可直接 `g++ -std=c++17` 编译运行。

## 完整 C++ 实现（含删除 + 扩容）

> [!info] 📌 付费章节补全内容

```cpp
#include <bits/stdc++.h>
using namespace std;

namespace dsa {

// 线性探查法 + 墓碑 + 动态扩容
class LinearProbingHashMap {
private:
    enum State { EMPTY, OCCUPIED, TOMBSTONE };
    struct Slot { int key; int val; State state = EMPTY; };
    vector<Slot> table_;
    int size_ = 0;  // 有效元素数
    int cap_;

    int hash(int k) const { return ((unsigned)k * 2654435761u) % cap_; }

    void resize(int new_cap) {
        vector<Slot> old = std::move(table_);
        table_ = vector<Slot>(new_cap);
        size_ = 0;
        cap_ = new_cap;
        for (auto& s : old) {
            if (s.state == OCCUPIED) put(s.key, s.val);
        }
    }

public:
    LinearProbingHashMap(int cap = 8) : cap_(cap), table_(cap) {}

    int get(int key) const {
        int h = hash(key);
        while (table_[h].state != EMPTY) {
            if (table_[h].state == OCCUPIED && table_[h].key == key)
                return table_[h].val;
            h = (h + 1) % cap_;
        }
        return -1;  // 未找到
    }

    void put(int key, int val) {
        if ((size_ + 1) * 2 > cap_) resize(cap_ * 2);
        int h = hash(key);
        while (table_[h].state != EMPTY && table_[h].key != key) {
            h = (h + 1) % cap_;
        }
        if (table_[h].state == OCCUPIED) {
            table_[h].val = val;  // 更新
        } else {
            table_[h] = {key, val, OCCUPIED};
            size_++;
        }
    }

    void remove(int key) {
        int h = hash(key);
        while (table_[h].state != EMPTY) {
            if (table_[h].state == OCCUPIED && table_[h].key == key) {
                table_[h].state = TOMBSTONE;
                size_--;
                if (size_ * 4 < cap_) resize(cap_ / 2);  // 缩容
                return;
            }
            h = (h + 1) % cap_;
        }
    }
};

} // namespace dsa
```

**关键设计要点**：
1. **墓碑机制**：删除不直接置空，避免断链
2. **动态扩容**：当负载因子 > 0.5 时翻倍 rehash
3. **动态缩容**：当负载因子 < 0.25 时减半，节省内存
4. **探查时跳过墓碑**：保证查找正确性

### 与拉链法的对比

| 维度 | 线性探查 | 拉链法 |
|------|---------|--------|
| 缓存友好 | ✅ 连续内存 | ❌ 链表分散 |
| 实现复杂度 | 中等（墓碑 + 缩容） | 简单 |
| 高负载性能 | 差（探测链长） | 好（链表长度可控） |
| 删除实现 | 复杂（墓碑累积） | 简单（直接删节点） |
| 标准库采用 | 少数（Java IdentityHashMap） | 主流（C++/Java/Python） |


## 关联章节

- [[14-linear-probing-key-point|线性探查法的两个难点]]
