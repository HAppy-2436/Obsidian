---
title: 链表实现哈希表（LinkedHashMap）
tags: [labuladong, 哈希表, 实现, 数据结构与算法, 付费章节]
order: 12
prerequisites: [06-linkedlist-implement]
group: 哈希表 / 实现
paywall: true
source: labuladong.online
url: https://labuladong.online/zh/algo/data-structure-basic/hashtable-with-linked-list/
---

前置知识

阅读本文前，你需要先学习：

哈希表核心原理

前文
哈希表原理
 从原理上分析了，不能依赖哈希表遍历 key 的顺序，即哈希表中的 key 是无序的。

但结合实际的编程经验，你可能会有些疑问。

比如熟悉 Java 的读者可能知道，Java 标准库提供的 LinkedHashMap 就可以按照键的插入顺序来遍历。例如下面这段简单的代码：

```java
import java.util.LinkedHashMap;

public class Main {
    public static void main(String[] args) {
        LinkedHashMap<String, Integer> map = new LinkedHashMap<>();
        map.put("a", 1);
        map.put("b", 2);
        map.put("c", 3);
        System.out.println(map.keySet()); // [a, b, c]

        map.put("y", 4);
        System.out.println(map.keySet()); // [a, b, c, y]

        map.put("d", 5);
        System.out.println(map.keySet()); // [a, b, c, y, d]
    }
}
```

无论你插入多少键，keySet 方法返回的所有键都是按照插入顺序排列，感觉就好像在向数组尾部追加元素一样。这怎么可能呢？

如果你熟悉 Golang，你会发现一个更神奇的现象。比如下面这段测试代码：

```
package main

import (
	"fmt"
)

func main() {
	// 初始化 map
	myMap := map[string]int{
		"1":  1,
		"2": 2,
		"3":  3,
		"4": 4,
		"5":  5,
	}

	// 定义遍历 map 的函数
	printMapKeys := func(m map[string]int) {
		for key := range m {
			fmt.Print(key, " ")
		}
		fmt.Println()
	}

	// 多次遍历 map，观察键的顺序
	printMapKeys(myMap)
	printMapKeys(myMap)
	printMapKeys(myMap)
	printMapKeys(myMap)
}

// 我运行的结果如下：
// 1 2 3 4 5
// 5 1 2 3 4
// 2 3 4 5 1
// 1 2 3 4 5
```

也就是说，它每次遍历的顺序都是随机。但是按照前文
哈希表原理
 所说，虽然哈希表的键是无序的，但是没有对哈希表做任何操作，遍历得到的结果应该不会变才对，Golang 的 map 每次遍历的顺序咋都不一样？这也太离谱了吧？

你可以先自己思考下原因，下面我给出答案。

点击查看答案

了解会员权益


> [!warning] 付费章节
> 本章内容为 labuladong.online 付费会员内容。本笔记仅保留公开部分 + C++ 代码片段的整理（由 agent 自动从 C++ tab 提取）。完整讲解请见 [原网页](https://labuladong.online/zh/algo/data-structure-basic/hashtable-with-linked-list/)。


## 关联章节

- [[06-linkedlist-implement|链表的代码实现]]
