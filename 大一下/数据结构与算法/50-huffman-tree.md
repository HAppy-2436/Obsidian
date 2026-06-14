---
title: 数据压缩和赫夫曼编码
tags: [应用, 数据结构]
order: 50
prerequisites:
  - "[[23-binary-tree-basic]]"
group: 应用
paywall: false
source: https://labuladong.online/zh/algo/data-structure-basic/huffman-tree/
---

# 数据压缩和赫夫曼编码

> 一句话总结：数据压缩和赫夫曼编码 是 应用 模块的核心知识点。

## 学习目标

读完本文，你应该能：
- 理解 数据压缩和赫夫曼编码 的核心原理
- 用 C++ 实现该数据结构/算法
- 掌握时间/空间复杂度分析
- 知道典型的应用场景

## 前置知识

阅读本文前，建议先学习：

- [[23-binary-tree-basic]]

## 赫夫曼编码原理

赫夫曼编码（Huffman Coding）是一种**无损数据压缩**算法，由 David Huffman 于 1952 年提出。它根据字符出现频率构造最优的二进制前缀编码。

### 为什么需要前缀编码？
- 普通定长编码（ASCII）：每个字符 8 bit，浪费空间
- **变长编码**：高频字符短码，低频字符长码 → 节省空间
- **前缀编码**：没有任何编码是另一个编码的前缀 → 保证解码唯一性

## 完整 C++ 实现

```cpp
#include <bits/stdc++.h>
using namespace std;

namespace dsa {

// 赫夫曼树节点
struct HuffmanNode {
    char ch;
    int freq;
    HuffmanNode *left, *right;
    HuffmanNode(char c, int f) : ch(c), freq(f), left(nullptr), right(nullptr) {}
    HuffmanNode(int f) : ch(0), freq(f), left(nullptr), right(nullptr) {}
};

struct Compare {
    bool operator()(HuffmanNode* a, HuffmanNode* b) {
        return a->freq > b->freq; // 最小堆
    }
};

// 构建赫夫曼树
HuffmanNode* buildHuffmanTree(const unordered_map<char, int>& freq) {
    priority_queue<HuffmanNode*, vector<HuffmanNode*>, Compare> pq;
    for (auto& [ch, f] : freq) {
        pq.push(new HuffmanNode(ch, f));
    }

    while (pq.size() > 1) {
        HuffmanNode* left = pq.top(); pq.pop();
        HuffmanNode* right = pq.top(); pq.pop();
        HuffmanNode* parent = new HuffmanNode(left->freq + right->freq);
        parent->left = left;
        parent->right = right;
        pq.push(parent);
    }
    return pq.top();
}

// 生成赫夫曼编码表（左 0 右 1）
void generateCodes(HuffmanNode* root, const string& prefix,
                   unordered_map<char, string>& codes) {
    if (!root) return;
    if (!root->left && !root->right) {
        codes[root->ch] = prefix.empty() ? "0" : prefix;
        return;
    }
    generateCodes(root->left, prefix + "0", codes);
    generateCodes(root->right, prefix + "1", codes);
}

// 编码
string huffmanEncode(const string& text) {
    if (text.empty()) return "";

    // 统计频率
    unordered_map<char, int> freq;
    for (char c : text) freq[c]++;

    // 构建树和编码表
    HuffmanNode* root = buildHuffmanTree(freq);
    unordered_map<char, string> codes;
    generateCodes(root, "", codes);

    // 编码
    string encoded;
    for (char c : text) encoded += codes[c];

    // 清理内存
    // (实际使用中应当递归释放)
    return encoded;
}

} // namespace dsa

int main() {
    string text = "hello world hello huffman";
    string encoded = dsa::huffmanEncode(text);
    cout << "Encoded: " << encoded << endl;
    cout << "Length: " << encoded.size() << " bits" << endl;
    return 0;
}
```

## 复杂度分析

| 项目 | 复杂度 |
|------|--------|
| 构建赫夫曼树 | O(N log N)（N 为不同字符数，优先队列操作）|
| 编码 | O(M)（M 为文本长度）|
| 空间复杂度 | O(N)（编码表 + 树）|

## 压缩原理

### 举例：文本 "ABRACADABRA"
字符频率：
- A: 5 次
- B: 2 次
- R: 2 次
- C: 1 次
- D: 1 次

赫夫曼编码：
- A: 0（高频 → 短码）
- B: 10
- R: 11
- C: 100
- D: 101

原始长度：11 字符 × 8 bit = 88 bit
压缩后长度：5×1 + 2×2 + 2×2 + 1×3 + 1×3 = 21 bit
压缩率：76%

## 应用场景

- **文件压缩**：gzip、bzip2、PNG、JPEG 等都用了类似思想
- **网络传输**：HTTP/2 的 HPACK 压缩
- **数据库**：列存储压缩
- **数据存储**：节省磁盘空间

## 局限性

1. **两次扫描**：需要先统计频率再编码
2. **需要传输编码表**：接收方需要知道编码表才能解码
3. **不适合小文件**：开销大于收益

## 下一章

本章数据结构及排序精讲全部完成！建议复习：
- [[00-intro|本章导读]]
- [[39-sort-basic|排序算法关键指标]] - 巩固排序理论
- [[23-binary-tree-basic|二叉树]] - 巩固赫夫曼树的二叉树基础


## 相关章节

- 同分组：应用
- 前置：[[23-binary-tree-basic]]
- 下一章：学完啦～

## 下一章

本章数据结构及排序精讲全部完成！
