---
title: 哈希集合的原理及代码实现
tags: [labuladong, 哈希集合, 数据结构与算法, 付费章节]
category: 哈希表结构的种种变换
order: 17
prerequisites: [13-hashmap-basic]
group: 哈希集合
paywall: true
source: labuladong.online
url: https://labuladong.online/zh/algo/data-structure-basic/hash-set/
---


前置知识

阅读本文前，你需要先学习：

哈希表核心原理

我讲解前面每种数据结构时，都会把原理和代码实现分到两篇文章里讲解，而这里讲哈希集合时，把原理和实现同时放在本文讲解，且本章节只有本文一篇文章，你有没有觉得奇怪？

哈哈，因为哈希集合没什么好讲的，它就是把前文讲的哈希表简单封装了一下：哈希表的键，其实就是哈希集合。

这么一句话就可以讲完了，不过我们还是稍微具体讲一下，照顾一下哈希集合的面子。


> [!info] 📌 付费章节补全内容（基于算法知识体系补充）

```cpp
#include <bits/stdc++.h>
using namespace std;

namespace dsa {

// 集合节点：只存 key
template <typename K>
struct KNode {
    K key;
    KNode* next;
    KNode(const K& k, KNode* n = nullptr) : key(k), next(n) {}
};

// 基于拉链法的 HashSet
template <typename K>
class HashSetChaining {
public:
    HashSetChaining(int init_cap = 16, double lf = 0.75)
        : size_(0), load_factor_(lf) {
        cap_ = 1;
        while (cap_ < init_cap) cap_ <<= 1;
        buckets_.assign(cap_, nullptr);
    }

    ~HashSetChaining() { clear(); }

    // ---- 增 ----
    void add(const K& key) {
        if (contains(key)) return;        // 去重
        if (size_ > cap_ * load_factor_) resize(cap_ << 1);
        int idx = hash_(key) & (cap_ - 1);
        buckets_[idx] = new KNode<K>(key, buckets_[idx]);
        ++size_;
    }

    // ---- 删 ----
    void remove(const K& key) {
        int idx = hash_(key) & (cap_ - 1);
        KNode<K>* cur = buckets_[idx], *prev = nullptr;
        while (cur) {
            if (cur->key == key) {
                if (prev) prev->next = cur->next;
                else      buckets_[idx] = cur->next;
                delete cur; --size_; return;
            }
            prev = cur; cur = cur->next;
        }
    }

    // ---- 查 ----
    bool contains(const K& key) const {
        int idx = hash_(key) & (cap_ - 1);
        for (KNode<K>* p = buckets_[idx]; p; p = p->next)
            if (p->key == key) return true;
        return false;
    }

    int size() const { return size_; }
    bool empty() const { return size_ == 0; }

private:
    vector<KNode<K>*> buckets_;
    int size_, cap_;
    double load_factor_;
    hash<K> hash_;

    void clear() {
        for (auto p : buckets_) {
            while (p) { auto n = p->next; delete p; p = n; }
        }
        buckets_.clear(); size_ = 0;
    }

    void resize(int new_cap) {
        vector<KNode<K>*> old = move(buckets_);
        cap_ = new_cap;
        buckets_.assign(cap_, nullptr);
        size_ = 0;
        for (auto p : old) {
            while (p) { auto n = p->next; add(p->key); delete p; p = n; }
        }
    }
};

} // namespace dsa
```

代码要点：

1. `add` 时先 `contains` 去重，这是「集合」语义的核心：同一个 key 不允许出现两次。
2. `buckets_` 是 `vector<KNode<K>*>`，拉链法天然适合集合的"键值对→键"的退化。
3. `resize` 用「重新插入」而不是「重新链接」——这是哈希表通用的扩容套路，因为原链表节点挂在新桶的哪个位置，取决于新桶大小，所以不如全部清空重新算。

### 集合 vs 映射：何时用哪个

| 场景 | 用 HashSet | 用 HashMap |
| --- | --- | --- |
| 判断元素是否存在（如 [[19-bloom-filter|布隆过滤器]] 的退化版） | ✅ | ❌ |
| 维护「元素 → 计数」或「元素 → 另一个值」 | ❌ | ✅ |
| 去重 + 保留原始顺序 | ❌（用 `LinkedHashSet`） | ❌（用 `LinkedHashMap`） |
| 排序遍历 | ❌（用 `TreeSet`） | ❌（用 `TreeMap`） |

### Java `HashSet` 源码分析

打开 JDK 源码，`java.util.HashSet` 的实现会让你会心一笑：

```java
public class HashSet<E>
    extends AbstractSet<E>
    implements Set<E>, Cloneable, java.io.Serializable {

    private transient HashMap<E, Object> map;

    // Dummy value to associate with an Object in the backing Map
    private static final Object PRESENT = new Object();

    public HashSet() { map = new HashMap<>(); }
    public HashSet(int initialCapacity, float loadFactor) {
        map = new HashMap<>(initialCapacity, loadFactor);
    }

    public boolean add(E e) { return map.put(e, PRESENT) == null; }
    public boolean remove(Object o) { return map.remove(o) == PRESENT; }
    public boolean contains(Object o) { return map.containsKey(o); }
    public int size() { return map.size(); }
    // ...
}
```

精髓：

- `HashSet` 内部持有一个 `HashMap`，键是真正要存的元素，值是一个静态空对象 `PRESENT`。
- `add` 通过 `map.put(e, PRESENT) == null` 判断"之前不存在"——因为之前不存在时 `put` 会返回 `null`。
- 集合的所有 API 都是哈希表 API 的"键视图"——所以 `HashSet` 的时间复杂度等价于 `HashMap`。

### C++ `std::unordered_set` 原理

C++ 的 `std::unordered_set` 与 Java `HashSet` 思路一致，但实现细节略有不同：

- **底层结构**：GCC libstdc++ 用 **拉链法**（buckets 数组 + 链表）；MSVC STL 也用拉链法；libc++（Clang）从早期版本开始用 **开放定址**（线性探查）。
- **哈希函数**：使用 `std::hash<T>`，对常见类型（int、string、自定义结构体）有特化版本。
- **负载因子**：默认 `max_load_factor = 1.0`，超过即触发 `rehash(capacity * 2)`。
- **迭代顺序**：**不保证**有序，仅保证「同一桶内迭代器失效」之外的其他迭代器在 rehash 后仍有效（C++11 起的节点句柄稳定性）。

下面是一段工业级用法示例：

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    unordered_set<string> seen;
    vector<string> words = {"apple", "banana", "apple", "cherry"};

    for (const auto& w : words) {
        if (seen.insert(w).second) {  // .second == true 表示新插入
            cout << "new: " << w << "\n";
        } else {
            cout << "dup: " << w << "\n";
        }
    }
    cout << "size = " << seen.size() << "\n";
    // 输出: new apple / new banana / dup apple / new cherry / size = 3
}
```

注意 `insert(...).second` 是「插入是否成功」的布尔值，比 `seen.count(w) == 0` 更快，因为后者会做两次哈希查询。

### 基于开放定址法的 HashSet（线性探查）

除了拉链法，开放定址（线性探查）也能实现 HashSet，结构更紧凑：

```cpp
#include <bits/stdc++.h>
using namespace std;

namespace dsa {

enum class Slot { EMPTY, OCCUPIED, DELETED };

template <typename K>
class HashSetOpenAddr {
public:
    explicit HashSetOpenAddr(int cap = 1024, double lf = 0.5)
        : size_(0), load_factor_(lf) {
        cap_ = 1;
        while (cap_ < cap) cap_ <<= 1;
        keys_.assign(cap_, K{});
        state_.assign(cap_, Slot::EMPTY);
    }

    void add(const K& key) {
        if (contains(key)) return;
        if (size_ >= cap_ * load_factor_) resize(cap_ << 1);
        int i = probe(key);
        keys_[i] = key;
        state_[i] = Slot::OCCUPIED;
        ++size_;
    }

    void remove(const K& key) {
        int i = probe(key);
        if (state_[i] == Slot::OCCUPIED && keys_[i] == key) {
            state_[i] = Slot::DELETED;
            --size_;
        }
    }

    bool contains(const K& key) const {
        int i = probe(key);
        return state_[i] == Slot::OCCUPIED && keys_[i] == key;
    }

    int size() const { return size_; }

private:
    vector<K> keys_;
    vector<Slot> state_;
    int size_, cap_;
    double load_factor_;
    hash<K> h_;

    int probe(const K& key) const {
        int i = h_(key) & (cap_ - 1);
        int first_del = -1;
        while (state_[i] != Slot::EMPTY) {
            if (state_[i] == Slot::DELETED && first_del < 0) first_del = i;
            else if (state_[i] == Slot::OCCUPIED && keys_[i] == key) return i;
            i = (i + 1) & (cap_ - 1);
        }
        return first_del >= 0 ? first_del : i;
    }

    void resize(int new_cap) {
        vector<K> old_keys = move(keys_);
        vector<Slot> old_state = move(state_);
        cap_ = new_cap;
        keys_.assign(cap_, K{});
        state_.assign(cap_, Slot::EMPTY);
        size_ = 0;
        for (int i = 0; i < (int)old_keys.size(); ++i) {
            if (old_state[i] == Slot::OCCUPIED) add(old_keys[i]);
        }
    }
};

} // namespace dsa
```

注意 `Slot::DELETED` 这个"墓碑标记"——这是线性探查法支持删除的关键，详见 [[14-linear-probing-key-point|线性探查法的两个难点]]。

## 📊 复杂度一览

| 操作 | 平均时间 | 最坏时间 | 空间 |
| --- | --- | --- | --- |
| `add` | O(1) | O(N)（全部冲突到一个桶） | O(N) |
| `remove` | O(1) | O(N) | O(1) |
| `contains` | O(1) | O(N) | O(1) |
| 遍历 | O(N) | O(N) | O(1) |

## 🛠️ 应用场景

- **去重**：把数组丢进 `unordered_set`，剩下的就是去重结果（LeetCode 217）。
- **存在性判断**：判断某个元素是否在集合中（LeetCode 1 两数之和就是 `HashMap` 版本，等价集合变体也能写）。
- **集合运算**：求两个集合的交集、并集、差集（力扣 349 / 350）。
- **作为 [[19-bloom-filter|布隆过滤器]] 的退化版**：当数据规模不大、内存够时，哈希集合比布隆过滤器更精确（零误判）。

## ▶️ 下一章

[[18-bitmap|位图原理和实现]]

## 🔗 相关章节

- [[13-hashmap-basic|哈希表核心原理]]
- [[16-hashtable-chaining|拉链法实现哈希表]]
- [[15-linear-probing-code|线性探查法的两种代码实现]]
- [[18-bitmap|位图原理和实现]]
- [[19-bloom-filter|布隆过滤器原理和实现]]


## HashSet 与 HashMap 的关系

### 两种实现策略

```cpp
#include <bits/stdc++.h>
using namespace std;

namespace dsa {

// 策略 1：HashSet 内部封装 HashMap（Java HashSet 风格）
class HashSetViaMap {
private:
    unordered_map<int, char> map_;  // key 是元素，value 是占位符
public:
    void add(int x) { map_[x] = 0; }
    bool contains(int x) { return map_.count(x) > 0; }
    void remove(int x) { map_.erase(x); }
    int size() { return map_.size(); }
};

// 策略 2：直接实现（节省内存）
class DirectHashSet {
private:
    vector<list<int>> buckets_;  // 链地址法
    int size_ = 0;
    int hash(int x) const { return abs(x) % buckets_.size(); }
public:
    DirectHashSet(int cap = 16) : buckets_(cap) {}
    void add(int x) {
        int h = hash(x);
        for (int v : buckets_[h]) if (v == x) return;
        buckets_[h].push_back(x);
        size_++;
        // 实际需要负载因子检查 + rehash
    }
    bool contains(int x) const {
        for (int v : buckets_[hash(x)]) if (v == x) return true;
        return false;
    }
    void remove(int x) {
        auto& b = buckets_[hash(x)];
        b.remove_if([x](int v) { return v == x; });
        size_--;
    }
};

} // namespace dsa
```

### Java HashSet 源码剖析

```java
// Java HashSet 内部就是一个 HashMap<E, Object>
// value 永远是一个固定的 PRESENT 占位对象
public class HashSet<E> {
    private transient HashMap<E, Object> map;
    private static final Object PRESENT = new Object();

    public boolean add(E e) {
        return map.put(e, PRESENT) == null;  // 复用 HashMap 的 put
    }
    public boolean contains(Object o) {
        return map.containsKey(o);
    }
    public boolean remove(Object o) {
        return map.remove(o) == PRESENT;
    }
}
```

**关键洞察**：HashSet 不是独立的数据结构，而是 HashMap 的"轻量包装"。所有操作都委托给底层的 HashMap，value 永远是个无意义的占位对象。这样实现简单、复用代码，但浪费一个 value 的内存。

### C++ std::unordered_set 原理

C++ 标准库的 `unordered_set` 内部采用**单独的哈希表**实现（不是基于 unordered_map），但底层数据结构类似：桶数组 + 链地址法或开放定址。

### 应用场景

- **去重**：判断元素是否存在（不关心次数）
- **集合运算**：求交集、并集、差集
- **图算法**：visited 集合、邻接集合


## 关联章节

- [[13-hashmap-basic|哈希表核心原理]]
