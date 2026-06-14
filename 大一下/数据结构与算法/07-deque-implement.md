---
title: 双端队列（Deque）原理和实现
tags: [labuladong, 数组链表技巧, 数据结构与算法]
order: 7
prerequisites: [06-linkedlist-implement, 03-array-implement]
group: 数组链表技巧
paywall: false
source: labuladong.online
url: https://labuladong.online/zh/algo/data-structure-basic/deque-implement/
---

# 双端队列（Deque）原理和实现

前置知识

阅读本文前，你需要先学习：

队列/栈基本原理

环形数组技巧

## 基本原理

如果你理解了前面讲解的内容，这个双端队列其实没啥可讲的了。所谓双端队列，主要是对比标准队列（FIFO 先进先出队列）多了一些操作罢了：

```cpp
template<typename E>
class MyDeque {
public:
    // 从队头插入元素，时间复杂度 O(1)
    void addFirst(E e);

    // 从队尾插入元素，时间复杂度 O(1)
    void addLast(E e);

    // 从队头删除元素，时间复杂度 O(1)
    E removeFirst();

    // 从队尾删除元素，时间复杂度 O(1)
    E removeLast();

    // 查看队头元素，时间复杂度 O(1)
    E peekFirst();

    // 查看队尾元素，时间复杂度 O(1)
    E peekLast();
};
```

标准队列
 只能在队尾插入元素，队头删除元素，而双端队列的队头和队尾都可以插入或删除元素。

普通队列就好比排队买票，先来的先买，后来的后买；而双端队列就好比一个过街天桥，两端都可以随意进出。当然，双端队列的元素就不再满足「先进先出」了，因为它比较灵活嘛。

在做算法题的场景中，双端队列用的不算很多。感觉只有 Python 用到的多一些，因为 Python 标准库没有提供内置的栈和队列，一般会用双端队列来模拟标准队列。

## 用链表实现双端队列

很简单吧，直接复用我们之前实现的
MyLinkedList
 类，或者使用编程语言标准库提供的双链表结构就行了。因为双链表本就支持
𝑂
(
1
)
O(1) 时间复杂度在链表的头尾增删元素：

```cpp
#include <iostream>
#include <list>

template<typename E>
class MyListDeque {
    list<E> list;

public:
    // 从队头插入元素，时间复杂度 O(1)
    void addFirst(const E &e) {
        list.push_front(e);
    }

    // 从队尾插入元素，时间复杂度 O(1)
    void addLast(const E &e) {
        list.push_back(e);
    }

    // 从队头删除元素，时间复杂度 O(1)
    E removeFirst() {
        E firstElement = list.front();
        list.pop_front();
        return firstElement;
    }

    // 从队尾删除元素，时间复杂度 O(1)
    E removeLast() {
        E lastElement = list.back();
        list.pop_back();
        return lastElement;
    }

    // 查看队头元素，时间复杂度 O(1)
    E peekFirst() {
        return list.front();
    }

    // 查看队尾元素，时间复杂度 O(1)
    E peekLast() {
        return list.back();
    }
};

int main() {
    MyListDeque<int> deque;
    deque.addFirst(1);
    deque.addFirst(2);
    deque.addLast(3);
    deque.addLast(4);

    cout << deque.removeFirst() << endl; // 2
    cout << deque.removeLast() << endl; // 4
    cout << deque.peekFirst() << endl; // 1
    cout << deque.peekLast() << endl; // 3
    return 0;
}
```

## 用数组实现双端队列

也很简单吧，直接复用我们在
环形数组技巧
 中实现的 CycleArray 提供的方法就行了。环形数组头尾增删元素的复杂度都是
𝑂
(
1
)
O(1)：

```cpp
template <typename E>
class CycleArray {
public:
    void addFirst(E e);
    void addLast(E e);
    E removeFirst();
    E removeLast();
    E getFirst();
    E getLast();
};

template <typename E>
class MyArrayDeque {
private:
    CycleArray<E> arr;

public:
    // 从队头插入元素，时间复杂度 O(1)
    void addFirst(E e) {
        arr.addFirst(e);
    }

    // 从队尾插入元素，时间复杂度 O(1)
    void addLast(E e) {
        arr.addLast(e);
    }

    // 从队头删除元素，时间复杂度 O(1)
    E removeFirst() {
        return arr.removeFirst();
    }

    // 从队尾删除元素，时间复杂度 O(1)
    E removeLast() {
        return arr.removeLast();
    }

    // 查看队头元素，时间复杂度 O(1)
    E peekFirst() {
        return arr.getFirst();
    }

    // 查看队尾元素，时间复杂度 O(1)
    E peekLast() {
        return arr.getLast();
    }
};
```

更新时间：2026/06/12 00:27

## 评论

请登录后查看/发表评论

## 关联章节

- [[06-linkedlist-implement|链表的代码实现]]
- [[03-array-implement|动态数组的代码实现]]
