---
title: 位图原理和实现
tags: [labuladong, 哈希集合, 数据结构与算法, 付费章节]
order: 18
prerequisites: [17-hash-set]
group: 哈希集合
paywall: true
source: labuladong.online
url: https://labuladong.online/zh/algo/data-structure-basic/bitmap/
---


一句话总结

位图（BitMap）是一种非常节省空间的数据结构，它用一个比特位（bit）的 0 和 1 来标记某个元素是否存在。

在后面做算法题时，我们会经常用到类似 boolean[] visited 这样的布尔数组，来记录数组中那些元素已经被访问过。

```
// 假设 nums 是一个包含 1000 个整数的数组 int[] nums = {...}

// 我们在写算法时 // 可能会用一个布尔数组来记录 nums 中那些元素已经被访问过 boolean[] visited = new boolean[nums.length]; visited[10] = true; visited[100] = true;
```

我们来仔细观察这个场景，是否存在优化空间？

布尔类型只有 true 和 false 两种状态，理论上只需要 1 个比特位（bit）的 0 和 1 就可以表示。

但在大部分编程语言中，由于内存寻址等原因，一个布尔元素通常会占用 1 字节（byte），也就是 8 个比特位的内存。

这就意味着，编程语言内置的布尔数组 boolean[] 实际上浪费了 7/8 的内存空间。

那么我们是否可以优化？答案是肯定的。

提示

在实际开发和求解算法题的过程中，我们使用编程语言提供的布尔数组就够了，除非需要处理的数据规模非常大，否则没必要为了节省这一点内存空间而引入位图这种结构。

比如后文介绍的  布隆过滤器 ，专门为了处理超大规模数据而设计，才需要使用位图这种结构进行优化。


> [!info] 📌 付费章节补全内容（基于算法知识体系补充）

```cpp
// nums 是 1000 个整数
vector<int> nums = {...};

// 用布尔数组记录哪些下标已经被访问过
vector<bool> visited(nums.size(), false);
visited[10] = true;
visited[100] = true;
```

`visited[10] = true` 这个赋值其实只需要 1 个 bit 就够了——`true/false` 两种状态本质就是二进制的 0/1。但 `vector<bool>` 在 C++ 标准库中被特化为"位打包"实现（虽然被诟病为 STL 历史上最差设计），而在更底层的语言（如 C、Java `boolean[]`）中，一个 `bool` 元素通常占 1 字节 = 8 bits，**浪费了 7/8 的内存**。

> 这是位图思想最直接的动因：把 `bool[]` 的存储密度从「1 字节/元素」压缩到「1 bit/元素」。

### 位图核心思想

位图用一个长度为 `n` 的二进制位序列 `bits[0..n-1]` 表示 `[0, n)` 范围内整数的存在性：

- `bits[i] = 1`：整数 `i` 存在
- `bits[i] = 0`：整数 `i` 不存在

要在内存中表示 `n` 个 bit，需要 `ceil(n/8)` 字节（外加几位可能的对齐开销）。

地址映射的经典公式（假设底层是 `vector<uint8_t>`）：

```
byte_index = i / 8           // 第几字节
bit_pos    = i % 8           // 在该字节的第几位（0-7，0 为最低位）
```

把第 `i` 个 bit 置 1：

```
bits[byte_index] |= (1 << bit_pos);
```

把第 `i` 个 bit 置 0：

```
bits[byte_index] &= ~(1 << bit_pos);
```

查询第 `i` 个 bit：

```
(bits[byte_index] >> bit_pos) & 1
```

### 节省空间分析

| 数据规模 | 布尔数组（1B/元素） | 位图（1bit/元素） | 节省比 |
| --- | --- | --- | --- |
| 1 万 | 10 KB | 1.25 KB | 8× |
| 100 万 | 1 MB | 125 KB | 8× |
| 1 亿 | 100 MB | 12.5 MB | 8× |
| **10 亿** | **1 GB** | **125 MB** | **8×** |

这就是为什么当数据规模达到亿级、十亿级时，`bool[]` 撑不住而位图绰绰有余——10 亿用户的去重需求，只需 125 MB 内存就能搞定。


### C++ 实现：`std::vector<uint8_t>` 版（位运算）

这是手写位图最常见的写法，把位运算的细节暴露给读者，对理解原理最友好：

```cpp
#include <bits/stdc++.h>
using namespace std;

namespace dsa {

class BitMap {
public:
    explicit BitMap(int n) : n_(n) {
        bytes_.assign((n + 7) / 8, 0);
    }

    // 添加整数 x（即 bits[x] = 1）
    void add(int x) {
        assert(x >= 0 && x < n_);
        bytes_[x / 8] |= (1u << (x % 8));
    }

    // 删除整数 x（即 bits[x] = 0）
    void remove(int x) {
        assert(x >= 0 && x < n_);
        bytes_[x / 8] &= ~(1u << (x % 8));
    }

    // 查询 x 是否存在
    bool contains(int x) const {
        assert(x >= 0 && x < n_);
        return (bytes_[x / 8] >> (x % 8)) & 1u;
    }

    int size() const { return n_; }

    // 调试：把位图打印成 "010110..." 的字符串
    string to_string() const {
        string s;
        s.reserve(n_);
        for (int i = 0; i < n_; ++i)
            s.push_back(contains(i) ? '1' : '0');
        return s;
    }

private:
    int n_;
    vector<uint8_t> bytes_;
};

} // namespace dsa
```

要点：

- `(1u << (x % 8))` 用 `unsigned` 防止 `x % 8 == 7` 时符号位溢出。
- 删除操作直接清零，不会留下"墓碑"（位图没有冲突，所以不需要 `DELETED` 状态）。
- 适用场景：x 必须在 `[0, n)` 范围内；范围之外的整数无法直接放入。

### C++ 实现：`std::vector<bool>` 版（封装版）

`std::vector<bool>` 是 STL 中"位打包"的特化版本，运算符 `[]` 返回一个代理对象，可以像普通 bool 一样读写。对追求简洁、不在意位运算细节的代码，可以用它实现位图：

```cpp
#include <bits/stdc++.h>
using namespace std;

namespace dsa {

class BitMapVB {
public:
    explicit BitMapVB(int n) : bits_(n, false) {}

    void add(int x) { bits_[x] = true; }
    void remove(int x) { bits_[x] = false; }
    bool contains(int x) const { return bits_[x]; }
    int size() const { return (int)bits_.size(); }

private:
    vector<bool> bits_;
};

} // namespace dsa
```

注意：`std::vector<bool>` 因为代理引用的设计，速度往往比 `vector<uint8_t>` 还慢，且不满足 `Container` 概念的一些要求（`&bits_[i]` 拿不到 `bool*`）。在生产代码中，更推荐 `boost::dynamic_bitset` 或 `absl::bitset`，但学习目的下两个版本都值得一看。

### 完整测试用例

```cpp
#include <bits/stdc++.h>
using namespace std;
using namespace dsa;

int main() {
    BitMap bm(16);  // 表示 [0, 16) 范围的整数
    bm.add(3); bm.add(7); bm.add(15);
    cout << bm.to_string() << "\n";
    // 输出: 0001000100000001   (bit 3, 7, 15 是 1)

    cout << bm.contains(7) << "\n";   // 1
    cout << bm.contains(8) << "\n";   // 0

    bm.remove(7);
    cout << bm.contains(7) << "\n";   // 0
    cout << bm.to_string() << "\n";
    // 输出: 0001000000000001
}
```

### 应用场景 1：10 亿用户去重

问题描述：服务器每天接收 10 亿条用户 ID（int32 范围），需要判断一个新来的 ID 之前是否出现过。`unordered_set<int>` 内存撑不住（每个节点 ~32 字节 + 哈希表指针开销，10 亿个至少 32 GB），位图只需 2^31 bits = 256 MB。

```cpp
#include <bits/stdc++.h>
using namespace std;
using namespace dsa;

int main() {
    // 给 int32 留 2^31 个 bit = 256 MB
    BitMap seen(INT_MAX);
    // 模拟 10 亿条数据流
    for (int i = 0; i < 100; ++i) {
        int x = rand() % 1000;
        if (seen.contains(x))
            cout << x << " 重复\n";
        else
            seen.add(x);
    }
}
```

如果 ID 是 int64，位图就需要 2^64 bits ≈ 2 EB（不可能）。这时候有两个选择：

1. **哈希映射 + 多次位图**：用多个 hash 函数把 int64 映射到 [0, m)，即 [[19-bloom-filter|布隆过滤器]]。
2. **磁盘外排序**：把 ID 排序后扫描相邻是否相等，O(N log N) 时间、O(1) 内存（除文件缓冲）。

### 应用场景 2：排序加速（位图排序 / 计数排序的极端版）

问题描述：对一个取值范围 `[0, n)` 的整数数组排序。位图排序只需 `O(n + N)` 时间（`N` 是值域上限）和 `O(N)` 空间。当 `N ≤ 10n` 时，位图排序比任何比较排序都快。

```cpp
#include <bits/stdc++.h>
using namespace std;
using namespace dsa;

vector<int> bitmap_sort(vector<int> arr, int N) {
    BitMap bm(N);
    for (int x : arr) bm.add(x);
    vector<int> sorted;
    sorted.reserve(arr.size());
    for (int i = 0; i < N; ++i)
        if (bm.contains(i)) sorted.push_back(i);
    return sorted;
}

int main() {
    vector<int> a = {5, 3, 7, 3, 5, 9, 1};
    auto s = bitmap_sort(a, 10);
    for (int x : s) cout << x << " ";
    cout << "\n";   // 1 3 5 7 9
}
```

这其实就是 [[47-counting-sort|计数排序]] 的"位图版"——区别在于计数排序用 `int[] count` 记录每个值出现多少次，位图用 `bool[]` 只关心是否出现。

### 应用场景 3：其他典型用法

- **快速查询 / IP 黑名单**：把恶意 IP 列表装进位图，O(1) 判断。
- **操作系统页表 / 位示图**：磁盘块管理用位图记录"哪些块已分配"。
- **数据库 bitmap 索引**：列式存储中用位图加速 `WHERE col IN (...)` 查询。
- **图算法**：BFS 中用位图记录访问过的节点，省内存。

### 位图的局限

位图不是万能的，使用前先确认这三点：

1. **元素必须是整数（或可哈希到 `[0, n)` 的非负整数）**。字符串、浮点数、自定义结构体都不能直接放入。
2. **值域不能太大**。`n = 10^9` 时位图 125 MB 没问题；`n = 10^18` 就崩了。
3. **不支持范围统计**。想知道"值在 [L, R] 内的元素有几个"，位图需要遍历 O(R-L+1) 个 bit；用线段树或 [[47-counting-sort|计数排序]] 用的 `int[]` 更合适。

## 📊 复杂度一览

| 操作 | 时间 | 空间（n 个 bit） |
| --- | --- | --- |
| `add` | O(1) | — |
| `remove` | O(1) | — |
| `contains` | O(1) | — |
| 遍历所有存在的整数 | O(N) | O(N/8) |
| 整个结构 | — | `ceil(n/8)` 字节 |

## 🛠️ 应用场景

- 10 亿用户去重（int32 范围只需 256 MB）
- 位图排序（值域小时比快速排序更快）
- IP 黑名单 / 恶意 URL 过滤（与 [[19-bloom-filter|布隆过滤器]] 互补）
- 操作系统页表、磁盘块管理
- 数据库 bitmap 索引（加速 `IN` 查询）

## ▶️ 下一章

[[19-bloom-filter|布隆过滤器原理和实现]]

## 🔗 相关章节

- [[17-hash-set|哈希集合的原理及代码实现]]
- [[19-bloom-filter|布隆过滤器原理和实现]]
- [[47-counting-sort|全新的排序原理：计数排序]]


## 关联章节

- [[17-hash-set|哈希集合的原理及代码实现]]
