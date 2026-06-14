---
title: 二叉堆核心原理及可视化
tags: [labuladong, 二叉堆, 数据结构与算法, 付费章节]
order: 21
prerequisites: [02-array-basic]
group: 二叉堆
paywall: true
source: labuladong.online
url: https://labuladong.online/zh/algo/data-structure-basic/binary-heap-basic/
---


前置知识

阅读本文前，你需要先学习：

二叉树基础及常见类型

二叉树的递归/层序遍历

一句话总结

二叉堆是一种能够动态排序的数据结构，是
二叉树结构
 的延伸。

二叉堆的主要操作就两个，sink（下沉）和 swim（上浮），用以维护二叉堆的性质。

二叉堆的主要应用有两个，首先是一种很有用的数据结构优先级队列（Priority Queue），第二是一种排序方法堆排序（Heap Sort）。

这个可视化面板直观地展示了二叉堆的基本操作，你可以点击跳转执行其中的代码，或自己修改代码玩一玩：

算法可视化

下面我就结合可视化面板来展示二叉堆的原理，最后以优先级队列为例，展示二叉堆的代码实现。


> [!info] 📌 付费章节补全内容（基于算法知识体系补充）

```cpp
#include <bits/stdc++.h>
using namespace std;

namespace dsa {

// 大顶堆（Max Heap）：父节点 ≥ 子节点，堆顶为最大值
class MaxHeap {
public:
    // 1. 插入新元素：放到末尾，然后 swim 上浮
    void push(int x) {
        data.push_back(x);
        swim(size() - 1);
    }

    // 2. 弹出堆顶（最大值）：把末尾元素提到 root，然后 sink 下沉
    int pop() {
        int top = data[0];
        data[0] = data.back();
        data.pop_back();
        if (!data.empty()) sink(0);
        return top;
    }

    // 3. 查看堆顶（不删除）
    int top() const { return data[0]; }

    // 4. 判空和大小
    bool empty() const { return data.empty(); }
    int size() const { return (int)data.size(); }

    // 5. heapify：把一个无序数组变成堆（从最后一个非叶子节点开始 sink）
    //    时间复杂度 O(N)，比逐个 push 的 O(N log N) 更快
    MaxHeap(const vector<int>& arr) : data(arr) {
        for (int i = parent(size() - 1); i >= 0; --i) {
            sink(i);
        }
    }

private:
    vector<int> data;

    // 0-indexed 下的父子关系
    static int parent(int i) { return (i - 1) / 2; }
    static int left(int i)   { return 2 * i + 1; }
    static int right(int i)  { return 2 * i + 2; }

    // swim：把下标 k 处的元素上浮到正确位置（大顶堆版本）
    void swim(int k) {
        while (k > 0 && data[k] > data[parent(k)]) {
            swap(data[k], data[parent(k)]);
            k = parent(k);
        }
    }

    // sink：把下标 k 处的元素下沉到正确位置（大顶堆版本）
    void sink(int k) {
        int n = size();
        while (true) {
            int l = left(k), r = right(k), j = k;
            if (l < n && data[l] > data[j]) j = l;
            if (r < n && data[r] > data[j]) j = r;
            if (j == k) break;
            swap(data[k], data[j]);
            k = j;
        }
    }
};

} // namespace dsa

int main() {
    using namespace dsa;

    // 演示 1：逐个 push + pop
    MaxHeap h;
    for (int x : {5, 3, 8, 1, 9}) h.push(x);
    cout << "堆顶: " << h.top() << endl;   // 输出 9
    cout << "pop 顺序: ";
    while (!h.empty()) cout << h.pop() << " ";  // 输出 9 8 5 3 1
    cout << endl;

    // 演示 2：heapify（O(N) 建堆）
    MaxHeap h2({5, 3, 8, 1, 9, 7, 6});
    cout << "heapify 后堆顶: " << h2.top() << endl;  // 输出 9

    return 0;
}
```

**输出**：

```text
堆顶: 9
pop 顺序: 9 8 5 3 1
heapify 后堆顶: 9
```

## 6. 复杂度表

| 操作 | 时间复杂度 | 空间复杂度 |
|------|-----------|-----------|
| top() / peek() | O(1) | O(1) |
| push() | O(log N) | O(1) |
| pop() | O(log N) | O(1) |
| heapify（建堆） | O(N) | O(1) |
| 整体存储 | — | O(N) |

## 7. 应用场景

- **堆排序（Heap Sort）**：见 [[45-heap-sort|堆排序]]，基于 `push` + `pop` 或原地 heapify 实现，复杂度 O(N log N)、原地排序。
- **优先级队列（Priority Queue）**：见 [[22-binary-heap-implement|优先级队列实现]]，任务调度、Dijkstra 算法、Huffman 编码都需要它。
- **Top K 问题**：维护一个大小为 K 的小顶堆，可在 O(N log K) 内找到第 K 大/小的元素。
- **流式数据的中位数**：用一个大顶堆 + 一个小顶堆，可以在 O(log N) 内维护中位数。

## 下一章

→ [[22-binary-heap-implement|堆排序/优先级队列的代码实现]]

## 相关章节

- [[02-array-basic|数组原理]] — 二叉堆的底层存储结构
- [[23-binary-tree-basic|二叉树基础]] — 二叉堆的逻辑结构
- [[45-heap-sort|堆排序]] — 二叉堆最重要的应用之一
- [[27-tree-map-basic|二叉搜索树原理]] — 另一种「动态排序」数据结构，对比学习


## 关联章节

- [[02-array-basic|数组（顺序存储）的原理]]
