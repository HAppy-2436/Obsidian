---
tag: 14-linear-probing-key-point
title: 线性探查法的两个难点
group: 哈希表
subgroup: 开放定址
order: 14
paywall: false
prerequisites:
  - 13-hashmap-basic
source_url: https://labuladong.online/zh/algo/data-structure-basic/linear-probing-key-point/
generated_at: 2026-06-13
---

# 线性探查法的两个难点

> 原文链接：<https://labuladong.online/zh/algo/data-structure-basic/linear-probing-key-point/>

## 前置知识

阅读本文前，你需要先学习：

- [[02-array-basic|数组（顺序存储）的原理]]
- [[03-array-implement|动态数组的代码实现]]
- [[13-hashmap-basic|哈希表核心原理]]

> 说明：本文结构基于 [labuladong online 教程](https://labuladong.online/zh/algo/data-structure-basic/linear-probing-key-point/) 整理。文中"
---

## 一、为什么这章先讲难点

前文 [[13-hashmap-basic|哈希表核心原理]] 提到，解决哈希冲突主要有两种方法：**拉链法** 和 **线性探查法（开放定址法）**。

- **拉链法** 简单：table 每个槽位存一条链表，冲突的 key 塞进链表就行
- **线性探查法** 复杂：涉及多种数组操作技巧，有 **两个核心难点**

本章先讲清楚这两个难点，下章再给具体代码。

---

## 二、简化场景

为了聚焦核心逻辑，先做一个简化假设：

| 假设项 | 简化值 |
|---|---|
| key 类型 | int |
| value 类型 | int |
| table 长度 | 固定 10 |
| hash 函数 | `hash(key) = key % 10` |
| key 不存在返回值 | -1 |

这样很容易模拟冲突：比如 `hash(1) = 1`，`hash(11) = 1`，`hash(21) = 1`，都撞到同一索引。

线性探查法伪码：

```java
class MyLinearProbingHashMap {
    private KVNode[] table = new KVNode[10];

    private int hash(int key) {
        return key % table.length;
    }

    public void put(int key, int value) {
        int index = hash(key);
        KVNode node = table[index];
        if (node == null) {
            table[index] = new KVNode(key, value);
        } else {
            // 线性探查：向后找 key 或空位
            while (index < table.length && table[index] != null && table[index].key != key) {
                index++;
            }
            table[index] = new KVNode(key, value);
        }
    }

    public int get(int key) {
        int index = hash(key);
        while (index < table.length && table[index] != null && table[index].key != key) {
            index++;
        }
        if (table[index] == null) return -1;
        return table[index].value;
    }

    public void remove(int key) {
        int index = hash(key);
        while (index < table.length && table[index] != null && table[index].key != key) {
            index++;
        }
        // 删 table[index]，但这里有难点！见下文
    }
}
```

> 上面这段简化版代码看起来挺正常，但其实 **隐藏了多个 bug**。下面就来拆解两个真正的难点。

---

## 三、难点一：数组下标越界 + 环形探查

### 3.1 问题描述

线性探查的 while 循环条件：

```java
while (index < table.length && table[index] != null && table[index].key != key) {
    index++;
}
```

**三个问题**：

1. `index < table.length`：走到末尾时越界怎么办？要么扩容、要么 **环形回到 0**
2. `table[index] != null`：遇到空位说明 key 不存在（put 场景）或已删除（get 场景）
3. `table[index].key != key`：找到目标 key

### 3.2 环形探查

如果 table 末尾被占满了，但目标 key 不存在，while 循环会从尾部探查到头部，再回到 0——这就是 **环形数组技巧**（见 [[04-cycle-array|循环数组技巧及实现]]）。

```java
// 探查 index, index+1, ..., table.length-1, 0, 1, ...
private int probe(int start, int key) {
    int i = start;
    do {
        if (table[i] == null || table[i].key == key) {
            return i;
        }
        i = (i + 1) % table.length;
    } while (i != start);   // 最多绕一圈（table 满了）
    return -1;
}
```

> [!warning] 必须限制探查次数
> 如果 table 已满（`size == table.length`），线性探查会陷入死循环。**插入前必须检查负载因子**——一旦达到上限就触发 **扩容**。

---

>
> ## 四、难点二：删除元素产生的"空洞"问题
>
> 这是线性探查法 **最容易出错** 的地方。
>
> ### 4.1 问题描述
>
> 假设 table 状态如下（`hash(x) = x % 10`）：
>
> ```text
> index:  0  1  2  3  4  5  6  7  8  9
> value: [ ][1][11][21][ ][ ][ ][ ][ ][ ]
> ```
>
> 我们想 `remove(1)`。朴素做法：`table[1] = null`
>
> 现在变成：
>
> ```text
> index:  0  1  2  3  4  5  6  7  8  9
> value: [ ][ ][11][21][ ][ ][ ][ ][ ][ ]
> ```
>
> 然后我们 `get(21)`：从 `hash(21) = 1` 开始探查
>
> ```text
> table[1] = null → 遇到空位 → 直接返回 -1 ❌
> ```
>
> **bug**：`21` 还在 table[3] 里，但被 null 拦住了，**查不到了**！
>
> 这就是 **删除产生的"空洞"问题**——空位会"截断"探查链。
>
> ### 4.2 两种解决方案
>
> #### 方案 A：标记墓碑（tombstone）
>
> 不直接置 null，而是标记为"已删除"（tombstone）。后续探查时遇到 tombstone **继续往后探**，而不是停下来。
>
> ```text
> index:  0  1  2  3  4  5  6  7  8  9
> value: [ ][墓][11][21][ ][ ][ ][ ][ ][ ]
> ```
>
> **优点**：
> - 简单，不破坏探查链
> - 单次删除 O(1)
>
> **缺点**：
> - 墓碑也算"占用"，导致实际可用槽位减少
> - 探查路径上墓碑越多，**查找性能越差**
> - 需要 **定期 rehash** 来清理墓碑
>
> Java ThreadLocalMap、WeakHashMap 都用 tombstone。
>
> #### 方案 B：再哈希（rehash 后续元素）
>
> 删除后，把探查链上后续元素 **重新插入**。
>
> 步骤（删除 `table[i] = null` 后）：
>
> 1. `i = (i + 1) % table.length`
> 2. 循环：如果 `table[i] == null`，退出
> 3. 取出 `node = table[i]`，`table[i] = null`
> 4. 重新计算 `node` 的"应该位置"——但 **不能直接用 hash(node.key)**，因为该位置可能被占了
> 5. 从 `hash(node.key) % table.length` 开始向后探查，找到第一个空位插入
> 6. 回到步骤 1
>
> **示例**：删除 `table[1]` 后
>
> ```text
> 原状态：[ ][1][11][21][ ][ ][ ][ ][ ][ ]
>
> i=2: 取出 11, table[2] = null
>    hash(11)=1，从 1 开始探查 → 找到 1 是 null → 插入 table[1]
>    [11][ ][ ][21][ ][ ][ ][ ][ ][ ]
>
> i=3: 取出 21, table[3] = null
>    hash(21)=1，从 1 开始探查 → table[1]=11 → 2 空 → 插入 table[2]
>    [11][21][ ][ ][ ][ ][ ][ ][ ][ ]
>
> 完成！所有元素都"向左收紧"了，没有空洞。
> ```
>
> **优点**：
> - 没有任何空洞，查找性能始终最优
> - 不需要 tombstone，逻辑统一
>
> **缺点**：
> - 单次删除可能触发多次再哈希，最坏 O(N)
> - 但 **均摊** 仍是 O(1)（因为每次被搬移的元素不会再被搬移）
>
> ### 4.3 复杂度对比
>
> | 方案 | put | get | remove | 查找性能 |
> |---|---|---|---|---|
> | A. 墓碑 | O(1) 均摊 | O(1) 平均（可能退化） | O(1) | 长期需要 rehash 清理 |
> | B. 再哈希 | O(1) 均摊 | **始终 O(1) 平均** | O(1) 均摊 | **始终最优** |
>
> > [!tip] 实战建议
> > - 内存紧张、删除少：**用墓碑**（如 ThreadLocalMap）
> > - 频繁删除、追求稳定性能：**用再哈希**（如 Rust HashMap 用类似思路）
> > - 教学场景：**两种都要掌握**，下章会分别给出代码实现
>
> ### 4.4 还有第 3 个隐藏难点：扩容
>
> 除了上述两个难点，线性探查法还有一个易错点：**扩容时的负载因子**。
>
> - 拉链法负载因子可以 > 1（链表能延伸）
> - 线性探查法负载因子必须 ≤ 1，**实际控制在 0.5 ~ 0.75** 之间
>
> 为什么？因为负载因子越高，"集群"（cluster）越长——连续的占用块越长，探查时跳过的位置越多，性能越差。
>
> ```text
> 负载因子 0.5：探查平均 < 1.5 次
> 负载因子 0.75：探查平均 ~ 2.5 次
> 负载因子 0.9：探查平均 ~ 5.5 次
> 负载因子 1.0：可能找不到空位，扩容死循环
> ```
>
> **经验值**：
> - Java HashMap 用拉链法，默认负载因子 0.75
> - C++ `std::unordered_map` 拉链法，max_load_factor 默认 1.0
> - Python dict 开放寻址，负载因子保持在 **2/3** 左右
> - Rust HashMap SwissTable，负载因子 **7/8 ≈ 0.875**
>
> 因此实现线性探查法时，建议 `MAX_LOAD_FACTOR = 0.5`，超过就触发 **2 倍扩容**。
>
> ### 4.5 选型：拉链法 vs 线性探查法
>
> | 维度 | 拉链法 | 线性探查法 |
> |---|---|---|
> | 实现难度 | 简单 | 较难（要处理空洞） |
> | 内存碎片 | 链表节点额外开销 | 紧凑数组，cache 友好 |
> | 删除友好度 | 友好（直接断链） | 不友好（要处理空洞） |
> | 负载因子 | 可以 > 1 | 必须 < 1 |
> | 极端性能 | 链表长时退化 | 集群长时退化 |
> | 适用场景 | 通用 | 内存敏感、cache 关键 |

---

## 五、本章小结

| 难点 | 解决方案 |
|---|---|
| 难点一：探查越界 + 死循环 | 环形数组 + 探查上限 ≤ table.length；提前扩容 |
| 难点二：删除空洞 | ① 墓碑标记；② 再哈希后续元素 |
| 隐藏难点：负载因子 | 控制在 0.5 ~ 0.75，超过就 2 倍扩容 |

## 六、相关章节

- 上一章：[[13-hashmap-basic|哈希表核心原理]]
- 代码实现：[[15-linear-probing-code|线性探查法的两种代码实现]]
- 对比方案：[[16-hashtable-chaining|用拉链法实现哈希表]]

---

> 📌 **备注**：本文中 `> [!info] 📌 付费章节补全内容` 标记的部分，是基于公开算法知识体系（Java ThreadLocalMap 源码 + Rust HashMap 设计 + 算法导论教科书）补充的难点解决方案分析，对应原文中"成为会员即可解锁"截断的内容。


## C++ 线性探查法实现要点

> [!info] 📌 付费章节补全内容

```cpp
#include <bits/stdc++.h>
using namespace std;

namespace dsa {

// 线性探查法的两个核心难点：
// 1. 删除时不能直接把槽位置空（会断链），要用墓碑标记
// 2. 查找时遇到墓碑要继续往后找

template <typename K, typename V>
class LinearProbingHashMap {
private:
    enum State { EMPTY, OCCUPIED, TOMBSTONE };
    struct Slot { K key; V val; State state = EMPTY; };
    vector<Slot> table_;
    int cap_;
    function<int(K)> hash_;
    function<bool(K,K)> eq_;

    int probe(const K& key) const {
        int h = hash_(key) % cap_;
        while (table_[h].state != EMPTY &&
               (table_[h].state != OCCUPIED || !eq_(table_[h].key, key))) {
            h = (h + 1) % cap_;
        }
        return h;
    }

public:
    LinearProbingHashMap(int cap, function<int(K)> h, function<bool(K,K)> e)
        : cap_(cap), hash_(h), eq_(e) {
        table_.resize(cap);
    }

    V* get(const K& key) {
        int h = probe(key);  // 找到的就是目标位置（即使有墓碑）
        if (table_[h].state != OCCUPIED) return nullptr;
        return &table_[h].val;
    }

    void put(const K& key, const V& val) {
        int h = probe(key);
        if (table_[h].state == OCCUPIED) {
            table_[h].val = val;
        } else {
            table_[h] = {key, val, OCCUPIED};
        }
    }

    void remove(const K& key) {
        int h = probe(key);
        if (table_[h].state != OCCUPIED) return;
        table_[h].state = TOMBSTONE;  // 墓碑标记！

        // 注意：后面的元素可能因为这个删除而"不可达"，需要后续 rehash
        // 这里简化处理
    }
};

} // namespace dsa
```

**关键洞察**：
1. **删除墓碑**：直接把槽位置空会导致"断链"，让原本可达的元素变成不可达
2. **查找遇到墓碑要继续**：因为墓碑后面可能还有要找的元素
3. **墓碑累积**：太多墓碑会影响性能，需要定期 rehash
