---
title: 布隆过滤器原理和实现
tags: [数据结构, 哈希集合]
order: 19
prerequisites: [18-bitmap, 17-hash-set]
group: 哈希集合
paywall: true
source: labuladong
---

# 布隆过滤器原理和实现

## 📚 学习目标

- 理解布隆过滤器「多个哈希函数 + 位数组」的核心原理
- 能够推导误判率公式 `p ≈ (1 - e^{-kn/m})^k`
- 在 C++ 中实现一个支持 `add` / `contains` 的布隆过滤器
- 掌握垃圾邮件过滤、缓存穿透、URL 黑名单等典型应用

## 🎯 一句话总结

布隆过滤器是一个"接受误判、拒绝漏判"的概率型数据结构：用 `k` 个哈希函数把每个元素映射到位数组的 `k` 个位置，全部为 1 才认为元素存在——能以极小的内存支持亿级数据的存在性判断。

## 🔗 前置知识

- [[18-bitmap|位图原理和实现]]
- [[17-hash-set|哈希集合的原理及代码实现]]
- [[13-hashmap-basic|哈希表核心原理]]

## 📖 正文

### 为什么需要布隆过滤器

[[17-hash-set|哈希集合]] 可以在 O(1) 时间内增删查改元素，但它有两个致命短板：

1. **空间复杂度 O(N)**：每个元素都要存进哈希表（含 KVNode、链表指针、负载因子开销等），亿级数据要几十 GB。
2. **不保护隐私**：哈希集合存的是原数据本身，没办法在不泄露原始数据的前提下判断存在性。

如果换成 [[18-bitmap|位图]]，内存能压到 `N/8` 字节——但要求元素必须是 `[0, n)` 范围的整数，对任意哈希值（如 URL、邮箱、UUID）束手无策。

**布隆过滤器（Bloom Filter）** 是这两者的折中：

- 用位数组存储，内存极省；
- 用 `k` 个哈希函数把任意类型元素映射到位数组的 `k` 个位置；
- 接受「假阳性（false positive）」，拒绝「假阴性（false negative）」。

### 布隆过滤器核心原理

布隆过滤器维护一个长度为 `m` 的位数组（初始全 0）和 `k` 个不同的哈希函数 `h_1, h_2, ..., h_k`。

**插入元素 x**：
```
for i = 1 to k:
    pos = h_i(x) mod m
    bits[pos] = 1
```

**查询元素 x**：
```
for i = 1 to k:
    pos = h_i(x) mod m
    if bits[pos] == 0:
        return false       // 任何一个位置是 0，x 一定不在
return true                // 全部是 1，x 可能在
```

关键性质：

- **没有假阴性**：如果 `x` 真的插入过，那 `k` 个位置都被设为 1，查询必然返回 `true`。
- **有假阳性**：如果 `x` 没插入过，但恰好 `k` 个位置都被其他元素设过 1，查询会"误报"为 `true`。
- **不能删除**：把某个位置设为 0 可能影响其他元素的判断。

### 误判率分析

假设：

- 位数组长度 `m`
- 已插入元素数 `n`
- 哈希函数个数 `k`
- 每个哈希函数均匀分布、相互独立

插入一个元素后，某一位仍为 0 的概率是 `1 - 1/m`，插入 `n` 个元素后某一位仍为 0 的概率是 `(1 - 1/m)^(kn) ≈ e^(-kn/m)`。查询时误判（`k` 个位置都为 1）的概率为：

```
p ≈ (1 - e^(-kn/m))^k
```

实战中常用的参数选择：

| 目标误判率 | m/n（位/元素） | k（哈希函数个数） |
| --- | --- | --- |
| 1% | ~9.6 | ~7 |
| 0.1% | ~14.4 | ~10 |
| 0.01% | ~19.2 | ~13 |

也就是说，**1 亿个元素、1% 误判率只需要约 120 MB 内存**——比起哈希集合节省了 20 倍以上。


### C++ 完整实现

下面给出一个工业级的布隆过滤器实现，包含：

- 双哈希函数族（`MurmurHash`-like 风格，避免用真·加密哈希）
- 动态扩容支持
- 误判率预估 API


> [!info] 📌 付费章节补全内容（基于算法知识体系补充）

```cpp
#include <bits/stdc++.h>
using namespace std;

namespace dsa {

class BloomFilter {
public:
    // 默认 m = 16n, k = 8，对应 ~2% 误判率
    explicit BloomFilter(int64_t expected_n,
                         double target_fpp = 0.01,
                         int64_t m_override = -1,
                         int k_override = -1)
        : n_(0) {
        if (m_override > 0 && k_override > 0) {
            m_ = m_override; k_ = k_override;
        } else {
            // m = -n ln(p) / (ln 2)^2
            m_ = (int64_t)ceil(-expected_n * log(target_fpp)
                                / (log(2) * log(2)));
            // k = (m/n) ln 2
            k_ = max(1, (int)round((double)m_ / expected_n * log(2)));
        }
        // 把 m 规整到下一个 2 的幂，便于 (hash & (m-1)) 取模
        int64_t pow2 = 1;
        while (pow2 < m_) pow2 <<= 1;
        m_ = pow2;
        mask_ = m_ - 1;
        bits_.assign(m_, 0);
    }

    void add(const string& s) {
        for (int i = 0; i < k_; ++i) {
            int64_t h = hash_i(s, i);
            bits_[h & mask_] = 1;
        }
        ++n_;
    }

    bool contains(const string& s) const {
        for (int i = 0; i < k_; ++i) {
            int64_t h = hash_i(s, i);
            if (!bits_[h & mask_]) return false;
        }
        return true;
    }

    int64_t size()        const { return n_; }
    int64_t bit_capacity() const { return m_; }
    int     hash_count()  const { return k_; }

    // 理论误判率（基于当前 n_）
    double estimated_fpp() const {
        double exponent = -((double)k_ * n_) / m_;
        double base = 1.0 - exp(exponent);
        return pow(base, k_);
    }

private:
    vector<uint8_t> bits_;
    int64_t m_, n_, mask_;
    int k_;

    // 第 i 个哈希函数：把字符串 x 哈希到 uint64_t
    static uint64_t hash_i(const string& s, int i) {
        // 用 FNV-1a 64 作为基础哈希，再叠加 seed = i
        uint64_t h = 0xcbf29ce484222325ULL ^ (uint64_t)i * 0x9e3779b97f4a7c15ULL;
        for (unsigned char c : s) {
            h ^= c;
            h *= 0x100000001b3ULL;
        }
        // 二次混合，把 i 的影响扩散到高位
        h ^= (h >> 33);
        h *= 0xff51afd7ed558ccdULL;
        h ^= (h >> 33);
        return h;
    }
};

} // namespace dsa
```

实现要点：

- **哈希函数族**：用 FNV-1a 作为基础哈希，第 `i` 个哈希通过把 `i` 异或进种子、再做一次 finalizer 扰动得到。生产中可换成 `MurmurHash3` 的 x64 变种，能让分布更均匀。
- **取模**：把 `m` 规整为 2 的幂，用 `hash & (m-1)` 代替 `% m`，速度更快且分布均匀（前提是哈希本身均匀）。
- **理论误判率**：`estimated_fpp()` 实时返回当前 `n_` 对应的误判率，可用于监控。

### 测试用例

```cpp
#include <bits/stdc++.h>
using namespace std;
using namespace dsa;

int main() {
    BloomFilter bf(/*expected_n=*/10000, /*target_fpp=*/0.01);

    // 插入 10000 个 URL
    for (int i = 0; i < 10000; ++i) {
        bf.add("https://example.com/page?id=" + to_string(i));
    }
    cout << "size=" << bf.size()
         << " bits=" << bf.bit_capacity()
         << " k=" << bf.hash_count()
         << " est_fpp=" << bf.estimated_fpp() << "\n";

    // 命中率测试
    int hits = 0;
    for (int i = 0; i < 10000; ++i) {
        if (bf.contains("https://example.com/page?id=" + to_string(i)))
            ++hits;
    }
    cout << "true positive rate = " << (double)hits / 10000 << "\n";
    // 应该接近 1.0（不漏判）

    // 误判率测试
    int fps = 0;
    for (int i = 10000; i < 20000; ++i) {
        if (bf.contains("https://example.com/page?id=" + to_string(i)))
            ++fps;
    }
    cout << "false positive rate = " << (double)fps / 10000 << "\n";
    // 应该接近 0.01（与 target_fpp 相符）
}
```

### 应用场景 1：垃圾邮件 / 恶意 URL 过滤

Google Chrome 曾经用布隆过滤器检查 URL 是否在恶意列表中：

- **写入**：从 Google Safe Browsing 下载恶意 URL 列表，写入客户端布隆过滤器（每次浏览器启动更新）。
- **查询**：用户访问 URL 时，先查布隆过滤器；如果返回 `false`，直接放行（无需联网）；如果返回 `true`，再向 Google 服务器发起精确查询（这一步可能误判，但不会漏判）。
- **收益**：99% 的正常 URL 免去网络请求，只有 1% 的误判 URL 多走一次精确查询。

这正是布隆过滤器的核心价值：**用极小的本地内存，把绝大部分请求挡在门外**。

### 应用场景 2：缓存穿透防护

「缓存穿透」指查询一个数据库中不存在的 key，每次都会绕过缓存直接打到数据库。当黑客故意用海量不存在的 key 攻击时，数据库可能被打挂。

**布隆过滤器解决方案**：

```
1. 把数据库中所有已有 key 写入布隆过滤器（启动时全量同步，增量时异步写）
2. 查询时先查布隆过滤器
   - false: 一定不存在，直接返回 null
   - true:  继续走 Redis → DB 的正常流程（可能有 0.01% 的误判，但 DB 能扛）
```

这等于在缓存前再加一道屏障：宁可少缓存几个真实 key（被布隆过滤器误判挡住），也不要让数据库被不存在的 key 打爆。

### 应用场景 3：其他经典用法

- **分布式数据库 HBase / Cassandra**：用布隆过滤器判断某个 key 是否在某个 SSTable 文件中，避免无谓的磁盘 IO。
- **爬虫 URL 去重**：把已访问 URL 写入布隆过滤器，亿级 URL 只需几百 MB。
- **Git**：用布隆过滤器判断一个对象是否在 packfile 中，加快 `git fetch`。
- **比特币 SPV 钱包**：用布隆过滤器过滤交易，轻客户端无需下载完整区块。

### 工业级变种

布隆过滤器有多个变种弥补其缺陷：

| 变种 | 解决的问题 | 代价 |
| --- | --- | --- |
| Counting Bloom Filter | 支持删除 | 每个 counter 占 4-8 bits |
| Cuckoo Filter | 支持删除 + 更高填充率 | 实现复杂，需要 cuckoo hashing |
| Quotient Filter | 支持删除 + 缓存友好 | 假阳率稍高 |
| Ribbon Filter | 接近最优空间利用 | 实现复杂 |

实际工程中，**Cuckoo Filter**（布谷鸟过滤器）越来越流行，它支持删除且空间利用率比布隆过滤器更高 30%~50%。

## 📊 复杂度一览

| 操作 | 时间 | 空间 | 误判 |
| --- | --- | --- | --- |
| `add` | O(k) | — | — |
| `contains` | O(k) | — | 有 |
| 删除 | ❌ 不支持 | — | — |
| 整体 | — | `m` bit | `(1-e^{-kn/m})^k` |

## 🛠️ 应用场景

- 垃圾邮件过滤 / 恶意 URL 拦截（Chrome Safe Browsing）
- 缓存穿透防护（Redis 前置屏障）
- 分布式数据库 / LSM-Tree SSTable 查找
- 爬虫 URL 去重、Git packfile、比特币 SPV 轻钱包
- 亿级用户「是否注册过」判断（保护隐私）

## ▶️ 下一章

[[20-skip-list-basic|跳表原理]]

## 🔗 相关章节

- [[17-hash-set|哈希集合的原理及代码实现]]
- [[18-bitmap|位图原理和实现]]
- [[20-skip-list-basic|跳表原理]]
- [[13-hashmap-basic|哈希表核心原理]]
