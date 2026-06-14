---
title: 线性探查法的两个难点
tags: [labuladong, 哈希表, 开放定址, 数据结构与算法, 付费章节]
order: 14
prerequisites: [13-hashmap-basic]
group: 哈希表 / 开放定址
paywall: true
source: labuladong.online
url: https://labuladong.online/zh/algo/data-structure-basic/linear-probing-key-point/
---

前置知识

阅读本文前，你需要先学习：

哈希表核心原理

前文
哈希表核心原理
 中我介绍了哈希表的核心原理和几个关键概念，其中提到了解决哈希冲突的方法主要有两种，分别是拉链法和线性探查法（也常叫做开放寻址法）：

由于线性探查法稍微复杂一些，本文先讲解实现线性探查法的几个难点，下篇文章再给出具体的代码实现。

## 简化场景

之前介绍的拉链法应该是比较简单的，无非就是 table 中每个元素都是一个链表，出现哈希冲突的话往链表里塞元素就行了。

而线性探查法会更复杂，主要有两个难点，涉及到多种数组操作技巧。在讲清楚这两个难点之前，我们先设定一个简化的场景：

假设我们的哈希表只支持 key 类型为 int，value 类型为 int 的情况，且 table.length 固定为 10，hash 函数的实现是 hash(key) = key % 10。因为这样比较容易模拟出哈希冲突，比如 hash(1) 和 hash(11) 的值都是 1。

线性探查法的大致逻辑如下：

```cpp
// 线性探查法的基本逻辑，伪码实现

class KVNode {
public:
    int key;
    int value;
    KVNode(int k, int v) : key(k), value(v) {}
};

class MyLinearProbingHashMap {
private:
    // 数组中每个元素都存储一个键值对
    KVNode* table[10] = {nullptr};

    int hash(int key) {
        return key % 10;
    }

public:
    // 析构函数
    ~MyLinearProbingHashMap() {
        for (int i = 0; i < 10; i++) {
            if (table[i] != nullptr) {
                delete table[i];
                table[i] = nullptr;
            }
        }
    }

    void put(int key, int value) {
        int index = hash(key);
        KVNode* node = table[index];
        if (node == nullptr) {
            table[index] = new KVNode(key, value);
        } else {
            // 线性探查法的逻辑
            // 向后探查，直到找到 key 或者找到空位
            while (index < 10 && table[index] != nullptr && table[index]->key != key) {
                index++;
            }
            delete table[index];
            table[index] = new KVNode(key, value);
        }
    }

    int get(int key) {
        int index = hash(key);
        // 向后探查，直到找到 key 或者找到空位
        while (index < 10 && table[index] != nullptr && table[index]->key != key) {
            index++;
        }
        if (index >= 10 || table[index] == nullptr) {
            return -1;
        }
        return table[index]->value;
    }

    void remove(int key) {
        int index = hash(key);
        // 向后探查，直到找到 key 或者找到空位
        while (index < 10 && table[index] != nullptr && table[index]->key != key) {
            index++;
        }
        // 删除 table[index]
        // ...
    }
};
```

基于这个假设场景，我们来看看线性探查法的两个难点。

了解会员权益


> [!warning] 付费章节
> 本章内容为 labuladong.online 付费会员内容。本笔记仅保留公开部分 + C++ 代码片段的整理（由 agent 自动从 C++ tab 提取）。完整讲解请见 [原网页](https://labuladong.online/zh/algo/data-structure-basic/linear-probing-key-point/)。


## 关联章节

- [[13-hashmap-basic|哈希表核心原理]]
