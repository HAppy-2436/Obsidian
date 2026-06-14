---
title: 链表（链式存储）的原理
tags: [数据结构, 链表, 链式存储]
order: 5
prerequisites: [02-array-basic]
group: 链表
paywall: false
source: labuladong
---

# 链表（链式存储）的原理

> [!info] 章节定位
> 数组靠「**连续内存**」实现 O(1) 随机访问，但被「搬移 / 扩容」拖累；本章介绍的链表是另一种思路——元素**分散在内存中**，靠**指针串起来**。理解链表后，[[06-linkedlist-implement|链表完整实现]]、[[07-deque-implement|Deque]]、LRU 缓存、图的邻接表 等都顺理成章。

## 📚 学习目标

- 理解「链式存储」与「顺序存储」的本质区别
- 掌握单链表 / 双链表的节点结构和指针操作
- 能在单/双链表上独立完成「增、删、查、改」并分析时间复杂度
- 理解为什么「双链表有 prev 指针」是值得的代价
- 知道「虚拟头结点」技巧存在的意义（为 [[06-linkedlist-implement|下一章]] 铺垫）

## 🎯 一句话总结

> 链表是「**用指针把零散的内存块串起来**」，单链表用 `next` 串、双链表用 `prev/next` 双向串；增删只要改指针，但**无法随机访问**——访问第 k 个节点必须从头走 k 步。

## 🔗 前置知识

- [[00-intro|本章导读]]
- [[01-complexity|时间空间复杂度入门]]
- [[02-array-basic|数组原理]] — **强烈建议先读**，对照看
- C/C++ 指针基础

## 📖 正文

### 1. 力扣上的「单链表」 vs 工程中的「双链表」

力扣的链表节点定义**简化**到极致：

```cpp
struct ListNode {
    int val;
    ListNode* next;
    ListNode(int x) : val(x), next(nullptr) {}
};
```

工程中（Java `LinkedList`、C++ `std::list`、Python `collections.deque`）用的是**双链表**节点：

```cpp
template <typename E>
struct Node {
    E val;
    Node* prev;
    Node* next;
    Node(Node* p, E v, Node* n) : prev(p), val(v), next(n) {}
};
```

区别主要有两点：

| 维度 | 力扣风格 | 工程风格 |
| --- | --- | --- |
| 泛型 | `int` 硬编码 | 模板 `E` 任意类型 |
| 指针 | 只有 `next` | `prev + next` 双向 |
| 适用场景 | 算法题 | 实际容器 |

> [!tip] 为什么工程用双链表？
> 1. 持**双向遍历**：从尾向前找 / 找倒数第 k 个节点 / 反转 / LRU 等操作变容易。
> 2. **删除节点**更简单：已知节点引用时，双链表 O(1) 删除；单链表要先找前驱，O(n)。

### 2. 为什么需要链表

回忆 [[02-array-basic|数组]] 的痛点：

- 长度固定 → 满了要扩容 → 拷贝。
- 头部插入 → 全部搬移。
- 内存必须连续 → 大数组可能申请失败。

链表换了一种思路：

- 节点**分散**在内存中：每个节点 `new` 出来一个，不要求相邻。
- 节点之间靠**指针**串起来：节点 A 的 `next` 指向节点 B。
- 理论上**没有容量上限**（只要内存允许）。

缺点也很直接：

- **无法随机访问**：要找第 k 个节点，必须从 head 走 k 次。
- **额外指针开销**：双链表每个节点多 1 个指针（64 位系统多 8 字节）。
- **cache 不友好**：节点分散在内存中，CPU 预取失效，性能可能比数组差几倍。

### 3. 单链表的基本操作

#### 3.0 工具函数：从数组创建单链表

```cpp
#include <bits/stdc++.h>
using namespace std;

struct ListNode {
    int val;
    ListNode* next;
    ListNode(int x) : val(x), next(nullptr) {}
};

namespace dsa {
ListNode* createLinkedList(const vector<int>& arr) {
    if (arr.empty()) return nullptr;
    ListNode* head = new ListNode(arr[0]);
    ListNode* cur = head;
    for (size_t i = 1; i < arr.size(); ++i) {
        cur->next = new ListNode(arr[i]);
        cur = cur->next;
    }
    return head;
}
} // namespace dsa
```

#### 3.1 查 / 改：必须遍历

```cpp
// 遍历
for (ListNode* p = head; p != nullptr; p = p->next) {
    cout << p->val << " ";
}
```

- 「按索引访问第 k 个」是 `O(k)`，最坏 `O(n)`。
- 链表**没有任何形式的随机访问**。

#### 3.2 增：改指针即可

**头部插入** O(1)：

```cpp
ListNode* newNode = new ListNode(0);
newNode->next = head;
head = newNode;
```

**尾部插入**（无尾指针）O(n)：

```cpp
ListNode* p = head;
while (p->next != nullptr) p = p->next;   // 走 n-1 步
p->next = new ListNode(6);
```

> 有「尾指针」可优化到 O(1)，但删除尾结点后尾指针失效，要再遍历找新尾——见 [[06-linkedlist-implement|链表完整实现]]。

**中间插入**（在第 k 个节点后） O(n)：

```cpp
// 找到第 k 个节点（其实是它的前驱）
ListNode* p = head;
for (int i = 0; i < k - 1; ++i) p = p->next;

ListNode* newNode = new ListNode(66);
newNode->next = p->next;
p->next = newNode;
```

#### 3.3 删：改指针即可

**删除第 k 个节点** O(n)：

```cpp
// 先找前驱
ListNode* p = head;
for (int i = 0; i < k - 2; ++i) p = p->next;   // p 指向第 k-1 个
p->next = p->next->next;
```

**头部删除** O(1)：

```cpp
ListNode* toDel = head;
head = head->next;
delete toDel;       // C++ 必须显式释放；Java/Go 交给 GC
```

**尾部删除** O(n)：

```cpp
// 单链表必须找到倒数第二个
ListNode* p = head;
while (p->next->next != nullptr) p = p->next;
delete p->next;
p->next = nullptr;
```

> [!warning] 单链表删除尾结点的代价
> 单链表**没有 prev 指针**，所以要删尾必须遍历到 `p->next->next == null` 的位置。**双链表**就完全没这个问题。

### 4. 双链表的基本操作

#### 4.0 工具函数

```cpp
#include <bits/stdc++.h>
using namespace std;

template <typename E>
struct DNode {
    E val;
    DNode* prev;
    DNode* next;
    DNode(E v) : val(v), prev(nullptr), next(nullptr) {}
};

namespace dsa {
template <typename E>
DNode<E>* createDoublyList(const vector<E>& arr) {
    if (arr.empty()) return nullptr;
    DNode<E>* head = new DNode<E>(arr[0]);
    DNode<E>* cur = head;
    for (size_t i = 1; i < arr.size(); ++i) {
        DNode<E>* n = new DNode<E>(arr[i]);
        cur->next = n;
        n->prev  = cur;
        cur = n;
    }
    return head;
}
} // namespace dsa
```

#### 4.1 查 / 改：双向遍历

```cpp
// 从头向后
for (DNode<int>* p = head; p != nullptr; p = p->next)
    cout << p->val;

// 从尾向前
DNode<int>* tail = head;
while (tail->next != nullptr) tail = tail->next;
for (DNode<int>* p = tail; p != nullptr; p = p->prev)
    cout << p->val;
```

- 「按索引访问」可以根据 `k` 离 `head` 还是 `tail` 近，从近的那头遍历，省一半时间（仍是 O(n) 最坏）。

#### 4.2 增：四指针联动

**头部插入** O(1)：

```cpp
DNode<int>* newHead = new DNode<int>(0);
newHead->next = head;
head->prev    = newHead;
head = newHead;
```

**尾部插入**（有尾指针）O(1)：

```cpp
DNode<int>* newTail = new DNode<int>(6);
newTail->prev = tail;
tail->next    = newTail;
tail          = newTail;
```

**中间插入**（在第 k 个位置前） O(n)：

```cpp
// 先找第 k 个节点
DNode<int>* p = head;
for (int i = 0; i < k - 1; ++i) p = p->next;

DNode<int>* x = new DNode<int>(66);
x->prev = p->prev;
x->next = p;
p->prev->next = x;
p->prev = x;
```

#### 4.3 删：把目标节点「从链上摘下」

**删除已知节点 `toDel`**（双链表特有 O(1) 操作）：

```cpp
toDel->prev->next = toDel->next;
toDel->next->prev = toDel->prev;
delete toDel;
```

**头部删除** O(1)：

```cpp
DNode<int>* toDel = head;
head = head->next;
head->prev = nullptr;
delete toDel;
```

**尾部删除**（有尾指针） O(1)：

```cpp
DNode<int>* toDel = tail;
tail = tail->prev;
tail->next = nullptr;
delete toDel;
```

### 5. 单链表 vs 双链表：一张表说透

| 操作 | 单链表 | 双链表 |
| --- | --- | --- |
| 头部增删 | `O(1)` | `O(1)` |
| 尾部增删 | `O(n)`（无尾指针） | `O(1)`（有尾指针） |
| 中间插入 / 删除 | `O(n)` | `O(n)` 找位置；删除已知节点 `O(1)` |
| 随机访问 | `O(n)` | `O(n)`（可双向逼近） |
| 每节点额外空间 | `next`（8 字节） | `prev + next`（16 字节） |
| 实现复杂度 | 简单 | 容易写挂（4 个指针要同步改） |
| 反向遍历 | 不支持 | 支持 |
| 适用场景 | 算法题（力扣风格）、嵌入式内存敏感 | 工程容器、LRU、Undo/Redo |

### 6. 链表 vs 数组：终极对照

| 维度 | 数组 | 链表 |
| --- | --- | --- |
| 内存布局 | 连续 | 分散 |
| 随机访问 | **O(1)** | O(n) |
| 头部增删 | O(n) 搬移 | **O(1)** |
| 尾部增删 | 摊销 O(1)（扩容） | O(1) 双链表 / O(n) 单链表 |
| 中间增删 | O(n) 搬移 | O(1) 已知位置 |
| 内存开销 | 紧凑 | +1~2 个指针 / 节点 |
| Cache 友好 | **是** | 否（指针追逐） |
| 适合 | 读多写少、尺寸可预估 | 频繁增删、尺寸多变 |

> 现实里：90% 的业务场景下**数组（动态数组）都够用**。链表的优势场景是「**LRU / Undo / 图的邻接表 / 哈希冲突链**」等。

### 7. 为什么「增删」看起来简单，写起来总挂？

链表的增删比数组复杂，因为：

1. **空指针**：要删的节点可能是 head（没有前驱），要删的可能是 tail（单链表没有后驱的 next 引用）。
2. **顺序问题**：改指针时必须**先保存后继**，再断开。
3. **双向链表**要同时维护 `prev` 和 `next`，**4 个指针**必须同步改。
4. **删完要 free**（C++），但 Java/Go 不用。

应对：**使用「虚拟头尾节点」**——下一章 [[06-linkedlist-implement|链表完整实现]] 会详细展开。

> [!tip] 调试建议
> 链表写挂时，画图 + `printList(head)` 辅助。常用 debug 工具函数：
> ```cpp
> void printList(ListNode* head) {
>     for (ListNode* p = head; p; p = p->next) cout << p->val << " -> ";
>     cout << "nullptr\n";
> }
> ```

## 📊 复杂度一览

| 操作 | 单链表 | 双链表 | 数组（对比） |
| --- | --- | --- | --- |
| 头部增 | O(1) | O(1) | O(n) |
| 头部删 | O(1) | O(1) | O(n) |
| 尾部增 | O(n) 无尾指针 / O(1) 有 | O(1) | 摊销 O(1) |
| 尾部删 | O(n) | O(1) | 摊销 O(1) |
| 中间增 | O(n) | O(n) 找 + O(1) 改 | O(n) |
| 中间删 | O(n) | O(n) 找 + O(1) 改 | O(n) |
| 按索引读 | O(n) | O(n) | O(1) |
| 按值查 | O(n) | O(n) | O(n) |
| 每节点空间 | +1 ptr | +2 ptr | 紧凑 |

## 🛠️ 应用场景

- **LRU 缓存淘汰**：用双链表维护访问顺序，O(1) 移动到头部。
- **图的邻接表**：每个节点的「邻居」就是一条链表。
- **哈希冲突链**：见 [[16-hashtable-chaining|拉链法哈希表]]。
- **Undo/Redo 历史记录**：用双链表存命令。
- **操作系统任务队列**：PCB 链表、内存空闲块链表。
- **算法题**：链表反转、合并、检测环、相交链表（LeetCode 206/21/141/160）。

## ▶️ 下一章

[[06-linkedlist-implement|链表的代码实现]] — 亲手实现一个完整 `MyLinkedList<E>`，重点是「**虚拟头尾节点**」技巧：用 dummy 节点消除所有空指针特例。

## 🔗 相关章节

- [[02-array-basic|数组原理]] — 对照学习
- [[06-linkedlist-implement|链表实现]] — 下一章
- [[07-deque-implement|双端队列]] — 链表 + 头尾 API
- [[10-linked-queue-stack|链表实现队列/栈]] — 链表的最常见应用
- [[11-hashtable-with-array|数组哈希表]] vs [[12-hashtable-with-linked-list|链表哈希表]] — 链表的另一个工程应用
- [[20-skip-list-basic|跳表]] — 链表 + 多级索引，O(log n) 查找
