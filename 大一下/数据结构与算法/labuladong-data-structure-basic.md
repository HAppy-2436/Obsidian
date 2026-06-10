# 基础：数据结构及排序精讲

> 抓取自 labuladong.online，共 51 个子页面（按侧边栏顺序排列）。

## 目录

### 1. 本章导读
- [1. 本章导读](#1-本章导读)

### 2. 时间空间复杂度入门
- [2. 时间空间复杂度入门](#2-时间空间复杂度入门)

### 3. 手把手带你实现动态数组
- [3. 数组（顺序存储）基本原理](#3-数组顺序存储基本原理)
- [4. 动态数组代码实现](#4-动态数组代码实现)

### 4. 手把手带你实现单/双链表
- [5. 链表（链式存储）基本原理](#5-链表链式存储基本原理)
- [6. 链表代码实现](#6-链表代码实现)

### 5. 数组链表的种种变换
- [7. 环形数组技巧及实现](#7-环形数组技巧及实现)
- [8. 双端队列（Deque）原理及实现](#8-双端队列deque原理及实现)

### 6. 手把手带你实现队列/栈
- [9. 队列/栈基本原理](#9-队列栈基本原理)
- [10. 用数组实现队列/栈](#10-用数组实现队列栈)
- [11. 用链表实现队列/栈](#11-用链表实现队列栈)

### 7. 哈希表的原理及实现
- [12. 用数组加强哈希表（ArrayHashMap）](#12-用数组加强哈希表arrayhashmap)
- [13. 用链表加强哈希表（LinkedHashMap）](#13-用链表加强哈希表linkedhashmap)
- [14. 用拉链法实现哈希表](#14-用拉链法实现哈希表)
- [15. 线性探查法的两个难点](#15-线性探查法的两个难点)
- [16. 线性探查法的两种代码实现](#16-线性探查法的两种代码实现)
- [17. 哈希表核心原理](#17-哈希表核心原理)
- [18. 哈希集合的原理及代码实现](#18-哈希集合的原理及代码实现)

### 8. 哈希表结构的种种变换
- [19. 跳表核心原理](#19-跳表核心原理)
- [20. 位图原理及实现](#20-位图原理及实现)
- [21. 布隆过滤器原理及实现](#21-布隆过滤器原理及实现)

### 9. 二叉树结构及遍历
- [22. 二叉堆核心原理及可视化](#22-二叉堆核心原理及可视化)
- [23. 二叉堆/优先级队列代码实现](#23-二叉堆优先级队列代码实现)
- [24. 二叉树基础及常见类型](#24-二叉树基础及常见类型)
- [25. 二叉树的递归/层序遍历](#25-二叉树的递归层序遍历)
- [26. 多叉树的递归/层序遍历](#26-多叉树的递归层序遍历)

### 10. 二叉树结构的种种变换
- [27. 线段树核心原理及可视化](#27-线段树核心原理及可视化)
- [28. 二叉搜索树的应用及可视化](#28-二叉搜索树的应用及可视化)
- [29. TreeMap/TreeSet 代码实现](#29-treemaptreeset-代码实现)
- [30. Trie/字典树/前缀树原理及可视化](#30-trie字典树前缀树原理及可视化)
- [31. Union Find 并查集原理](#31-union-find-并查集原理)
- [32. 红黑树的完美平衡及可视化](#32-红黑树的完美平衡及可视化)

### 11. 图结构基础及算法概览
- [33. 图论中的基本术语](#33-图论中的基本术语)
- [34. 图结构的通用代码实现](#34-图结构的通用代码实现)
- [35. 图结构的 DFS/BFS 遍历](#35-图结构的-dfsbfs-遍历)
- [36. DFS 和 BFS 的适用场景](#36-dfs-和-bfs-的适用场景)
- [37. 最小生成树算法概览](#37-最小生成树算法概览)
- [38. 图结构最短路径算法概览](#38-图结构最短路径算法概览)
- [39. 欧拉图和一笔画游戏](#39-欧拉图和一笔画游戏)

### 12. 十大排序算法原理及可视化
- [40. 排序算法的关键指标](#40-排序算法的关键指标)
- [41. 拥有稳定性：冒泡排序](#41-拥有稳定性冒泡排序)
- [42. 运用逆向思维：插入排序](#42-运用逆向思维插入排序)
- [43. 选择排序所面临的问题](#43-选择排序所面临的问题)
- [44. 妙用二叉树后序位置：归并排序](#44-妙用二叉树后序位置归并排序)
- [45. 妙用二叉树前序位置：快速排序](#45-妙用二叉树前序位置快速排序)
- [46. 二叉堆结构的运用：堆排序](#46-二叉堆结构的运用堆排序)
- [47. 突破 O(N^2)：希尔排序](#47-突破-on^2希尔排序)
- [48. 全新的排序原理：计数排序](#48-全新的排序原理计数排序)
- [49. 博采众长：桶排序](#49-博采众长桶排序)
- [50. 基数排序（Radix Sort）](#50-基数排序radix-sort)

### 13. 补充:哈夫曼树
- [51. 数据压缩和霍夫曼树](#51-数据压缩和霍夫曼树)

---

## 1. 本章导读

### 1. 本章导读

原文链接: <https://labuladong.online/zh/algo/intro/data-structure-basic/>

## 本章适合谁

对于希望系统掌握数据结构和算法的读者，都建议学习本章。

对于希望速成刷题能力应对笔试的读者，不需要完整学习本章，请参考 [速成目录](https://labuladong.online/zh/algo/intro/quick-learning-plan/)。

## 本章导读

本章的重点在数据结构和排序算法，涵盖所有基本数据结构，也会讲解一些算法题中常用的高级数据结构，最后讲解十种排序算法。

基本数据结构包括数组链表、队列、栈、哈希表、二叉堆等，本章会讲解他们的原理、代码实现和常见变体。

高级数据结构包括图、线段树、树状数组、字典树、并查集等。考虑这是基础章节，本章把重点放在它们的原理和使用场景，具体代码实现安排在后面的数据结构设计章节中。

**了解了这些数据结构的底层原理和适用场景，你才能充分利用每个数据结构的特点解决算法问题，并准确理解代码的时间复杂度**。

在本章节中，会经常用到 [算法可视化面板](https://labuladong.online/zh/algo/intro/visualize/) 对稍微复杂的数据结构操作进行可视化。可视化代码是用 JavaScript 写的，但是都比较简单，无论你是否了解 JavaScript 都应该很容易看懂。

提示

本章的重点在于让读者理解每个数据结构的实现原理、优缺点和局限性，给出的 Java/C++/C/Golang/Python/JavaScript 代码实现只确保正确性和可读性。

至于编程语言层面的极致优化和最佳实践，不在本站的教学范围。如果你追求更深入地理解，可以参考对应编程语言的标准库。

当然，我给出的多语言代码难免也可能出现细节错误，欢迎大家批评指正，让我们共同进步！

[上一篇本站付费会员](https://labuladong.online/zh/algo/intro/site-vip/)[下一篇时间空间复杂度入门](https://labuladong.online/zh/algo/intro/complexity-basic/)

---

## 2. 时间空间复杂度入门

### 2. 时间空间复杂度入门

原文链接: <https://labuladong.online/zh/algo/intro/complexity-basic/>

考虑到这是第一章，我不会对时空复杂度做面面俱到的讲解，详细的 [算法时空复杂度分析实用指南](https://labuladong.online/zh/algo/essential-technique/complexity-analysis/) 安排在你学完几种常见算法的核心框架之后，那时候你的知识储备可以轻松理解时空复杂度分析的各种场景。

因为本章后面的内容会带你实现常见的排序算法和数据结构，我会分析它们的时间复杂度，所以这里还是要提前介绍一下时间/空间复杂度的概念，以及分析时间/空间复杂度的**简化方法**，避免初学者疑惑。

对于初学者，你只需要记住以下几点：

1、时空复杂度用 Big O 表示法表示（类似 O(1),O(n2),O(logn)O(1), O(n^2), O(logn)O(1),O(n2),O(logn) 等）。**它们都是估计值，不需要精确计算，常数项和低增长项都可以忽略，仅需保留最高增长项**。

比方说 O(2n2+3n+1)O(2n^2 + 3n + 1)O(2n2+3n+1) 等同于 O(n2)O(n^2)O(n2)，O(1000n+1000)O(1000n + 1000)O(1000n+1000) 等同于 O(n)O(n)O(n)。

2、我们分析算法复杂度时，分析的是最坏情况的复杂度。这一点会在下面的示例中体现。

3、时间复杂度用来衡量一个算法的执行效率，空间复杂度用来衡量算法的内存消耗，它们都是越小越好。

比方说时间复杂度 O(n)O(n)O(n) 的算法比 O(n2)O(n^2)O(n2) 的算法执行效率高，空间复杂度 O(1)O(1)O(1) 的算法比 O(n)O(n)O(n) 的算法内存消耗小。

当然，一般我们要说明这个 nnn 代表什么，比如 nnn 代表输入的数组的长度。

4、如何估算？**现在你可以简单理解：时间复杂度大部分情况下就是看 for 循环的最大嵌套层数；空间复杂度就看算法申请了多少空间来存储数据**。

注意

以上的分析方法中，有些细节并不严谨：

1、按照 for 循环的嵌套层数来估算时间复杂度是简化的方法，其实不完全准确。

2、大部分时候我们是分析最坏情况下的复杂度，但是对于数据结构 API 的复杂度衡量，我们会分析平均复杂度。

完善的复杂度分析方法会在 [算法时空复杂度分析实用指南](https://labuladong.online/zh/algo/essential-technique/complexity-analysis/) 具体介绍，以上估算方法对于学习本章内容足够了。

举几个例子来说比较直观。

## 时间/空间复杂度案例分析

**示例一，时间复杂度 O(n)O(n)O(n)，空间复杂度 O(1)O(1)O(1)**：

```java
// 输入一个整数数组，返回所有元素的和
int getSum(int[] nums) {
    int sum = 0;
    for (int i = 0; i < nums.length; i++) {
        sum += nums[i];
    }
    return sum;
}
```

算法包含一个 for 循环遍历 `nums` 数组，所以时间复杂度是 O(n)O(n)O(n)，其中 `n` 代表 `nums` 数组的长度。

我们的算法只使用了一个 `sum` 变量，这个 `nums` 是题目给的输入，不算在我们算法的空间复杂度里面，所以空间复杂度是 O(1)O(1)O(1)。

**示例二，时间复杂度 O(n)O(n)O(n)，空间复杂度 O(1)O(1)O(1)**：

```java
// 当 n 是 10 的倍数时，计算累加和，否则返回 -1
int sum(int n) {
    if (n % 10 != 0) {
        return -1;
    }
    int sum = 0;
    for (int i = 0; i <= n; i++) {
        sum += i;
    }
    return sum;
}
```

其实只有当 `n` 是 10 的倍数时，算法才会执行 for 循环，时间复杂度是 O(n)O(n)O(n)。其他情况下算法会直接返回，时间复杂度是 O(1)O(1)O(1)。

但是算法复杂度只考察最坏情况，所以这个算法的时间复杂度是 O(n)O(n)O(n)，空间复杂度是 O(1)O(1)O(1)。

**示例三，时间复杂度 O(n2)O(n^2)O(n2)，空间复杂度 O(1)O(1)O(1)**：

```java
// 数组是否存在两个数，它们的和为 target？
boolean hasTargetSum(int[] nums, int target) {
    for (int i = 0; i < nums.length; i++) {
        for (int j = i + 1; j < nums.length; j++) {
            if (nums[i] + nums[j] == target) {
                return true;
            }
        }
    }
    return false;
}
```

算法嵌套了两层 for 循环，所以时间复杂度是 O(n2)O(n^2)O(n2)，其中 nnn 代表 `nums` 数组的长度。

我们的算法只使用了 `i, j` 两个变量，这是常数级别的空间消耗，所以空间复杂度是 O(1)O(1)O(1)。

你也许会说，内层的 for 循环并没有遍历整个数组，且有可能提前 return，算法实际执行的次数应该是小于 n2n^2n2 的，时间复杂度还是 O(n2)O(n^2)O(n2) 吗？

是的，还是 O(n2)O(n^2)O(n2)。具体到不同的输入，算法的实际执行次数确实会小于 n2n^2n2，但我们不需要关心这些细节，估算一个最坏情况的时间复杂度就可以了。

每层 for 循环在最坏情况下都是 O(n)O(n)O(n) 的时间复杂度，套在一起，总的时间复杂度是 O(n2)O(n^2)O(n2)。

**示例四，时间复杂度 O(n)O(n)O(n)，空间复杂度 O(n)O(n)O(n)**：

```java
void exampleFn(int n) {
    int[] nums = new int[n];
}
```

这个函数中创建了一个大小为 `n` 的数组，所以空间复杂度是 O(n)O(n)O(n)。

上述代码申请数组空间并将 `n` 个元素初始化为 0。内存申请操作的时间复杂度可以认为是 O(1)O(1)O(1)，但为所有元素赋值的操作相当于一个隐藏的 for 循环（由编程语言为我们自动完成），时间复杂度是 O(n)O(n)O(n)。所以总的时间复杂度是 O(n)O(n)O(n)。

时间复杂度并不仅仅体现在你看得到的 for 循环，每一行代码都可能有隐藏的时间复杂度。所以说要了解编程语言提供的常用数据结构实现原理，这是准确分析时间复杂度的基础。

**示例五，时间复杂度 O(n)O(n)O(n)，空间复杂度 O(n)O(n)O(n)**：

```java
// 输入一个整数数组，返回一个新的数组，新数组的每个元素是原数组对应元素的平方
int[] squareArray(int[] nums) {
    int[] res = new int[nums.length];
    for (int i = 0; i < nums.length; i++) {
        res[i] = nums[i] * nums[i];
    }
    return res;
}
```

算法初始化 `res` 数组需要 O(n)O(n)O(n) 的时间复杂度，包含一个 for 循环，时间复杂度也是 O(n)O(n)O(n)，总的时间复杂度是还是 O(n)O(n)O(n) 其中 `n` 代表 `nums` 数组的长度。

我们声明了一个新的数组 `res`，这个数组的长度和 `nums` 数组一样，所以空间复杂度是 O(n)O(n)O(n)。

好了，初学者明白上面这些基本的时间、空间复杂度分析暂时就够用了，继续往下学习吧。

[上一篇本章导读](https://labuladong.online/zh/algo/intro/data-structure-basic/)[下一篇数组（顺序存储）基本原理](https://labuladong.online/zh/algo/data-structure-basic/array-basic/)

---

## 3. 手把手带你实现动态数组

### 3. 数组（顺序存储）基本原理

原文链接: <https://labuladong.online/zh/algo/data-structure-basic/array-basic/>

我们在说「数组」的时候有多种不同的语境，因为不同的编程语言提供的数组类型和 API 是不一样的，所以开头先统一一下说辞，方便后面的讲解。

我认为暂且可以把「数组」分为两大类，一类是「静态数组」，一类是「动态数组」。

**「静态数组」就是一块连续的内存空间，我们可以通过索引来访问这块内存空间中的元素，这才是数组的原始形态**。

而「动态数组」是编程语言为了方便我们使用，在静态数组的基础上帮我们添加了一些常用的 API，比如 `push, insert, remove` 等等方法，这些 API 可以让我们更方便地操作数组元素，不用自己去写代码实现这些操作。

本章的内容就是带大家仅仅使用最原始的静态数组，自己实现一个动态数组，实现增删查改的常见 API。以后你在使用标准库提供的数据结构时，就知道它们的底层运行原理了。

有了动态数组，后面讲到的队列、栈、哈希表等复杂数据结构都会依赖它进行实现。

## 静态数组

静态数组在创建的时候就要确定数组的元素类型和元素数量。只有在 C++、Java、Golang 这类语言中才提供了创建静态数组的方式，类似 Python、JavaScript 这类语言并没有提供静态数组的定义方式。

静态数组的用法比较原始，实际软件开发中很少用到，写算法题也没必要用，我们一般直接用动态数组。但为了理解原理，在这里还是要讲解一下。

定义一个静态数组的方法如下：

```java
// 定义一个大小为 10 的静态数组
int[] arr = new int[10];

// 使用索引赋值
arr[0] = 1;
arr[1] = 2;

// 使用索引取值
int a = arr[0];
```

就这，没有其他什么操作了。

拿 C++ 来举例吧，`int arr[10]` 这段代码到底做了什么事情呢？主要有这么几件事：

1、在内存中开辟了一段**连续的内存空间**，大小是 `10 * sizeof(int)` 字节。一个 int 在计算机内存中占 4 字节，也就是总共 40 字节。

2、定义了一个名为 `arr` 的数组指针，指向这段内存空间的首地址。

那么 `arr[1] = 2` 这段代码又做了什么事情呢？主要有这么几件事：

1、计算 `arr` 的首地址加上 `1 * sizeof(int)` 字节（4 字节）的偏移量，找到了内存空间中的第二个元素的**首地址**。

2、从这个地址开始的 4 个字节的内存空间中写入了整数 `2`。

写给初学者

我记得以前刚上大学的时候要学 C 语言基础，有些同学就绕不清楚什么指针的数组，数组的指针，绕来绕去的。其实只要明白了上面这个简单的流程，一切就很清楚了。

1、为什么数组的索引从 0 开始？就是方便取地址。`arr[0]` 就是 `arr` 的首地址，从这个地址往后的 4 个字节存储着第一个元素的值；`arr[1]` 就是 `arr` 的首地址加上 `1 * 4` 字节，也就是第二个元素的首地址，这个地址往后的 4 个字节存储着第二个元素的值。`arr[2], arr[3]` 以此类推。

2、因为数组的名字 `arr` 就指向整块内存的首地址，所以数组名 `arr` 就是一个指针。你直接取这个地址的值，就是第一个元素的值。也就是说，`*arr` 的值就是 `arr[0]`，即第一个元素的值。

3、如果不用 `memset` 这种函数初始化数组的值，那么数组内的值是不确定的。因为 `int arr[10]` 这个语句只是请操作系统在内存中开辟了一块连续的内存空间，你也不知道这块空间是谁使用过的二手内存，你也不知道里面存了什么奇奇怪怪的东西。所以一般我们会用 `memset` 函数把这块内存空间的值初始化一下再使用。

当然，上面讲的这些内容都是针对 C/C++，因为大家学习计算机基础的时候都接触过。其他比如 Java Golang 这种语言，静态数组创建出来后会自动帮你把元素值都初始化为 0，所以不需要再显式进行初始化。

我梳理一下上面的因果逻辑，静态数组本质上就是一块**连续的**内存空间，`int arr[10]` 这个语句我们可以得知：

1、我们知道这块内存空间的首地址（数组名 `arr` 就指向这块内存空间的首地址）。

2、我们知道了每个元素的类型（比如 int），也就是知道了每个元素占用的内存空间大小（比如一个 int 占 4 字节，32 bit）。

3、这块内存空间是连续的，其大小为 `10 * sizeof(int)` 即 40 字节。

**所以，我们获得了数组的超能力「随机访问」：只要给定任何一个数组索引，我可以在 O(1)O(1)O(1) 的时间内直接获取到对应元素的值**。

因为我可以通过首地址和索引直接计算出目标元素的内存地址。计算机的内存寻址时间可以认为是 O(1)O(1)O(1)，所以数组的随机访问时间复杂度是 O(1)O(1)O(1)。

但是，一个人最大的优势往往也是他的最大劣势。数组连续内存的特性给了他随机访问的超能力，但它也因此吃了不少苦，下面介绍。

## 增删查改

**数据结构的职责就是增删查改**，再无其他。

那么刚刚介绍数组这种数据结构的底层原理，我们其实只介绍了「查」和「改」的部分，也就是通过索引修改和访问对应元素的值。那么「增删」这两个操作又是如何实现的呢？

### 增

要想给静态数组增加元素，这就有些复杂了，需要分情况讨论。

情况一，数组末尾追加（append）元素

比方说，我有一个大小为 10 的数组，里面装了 4 个元素，现在想在末尾追加一个元素，怎么办？

比较简单，直接在对应的索引赋值就行了，这是大概的代码逻辑：

```java
// 大小为 10 的数组已经装了 4 个元素
int[] arr = new int[10];
for (int i = 0; i < 4; i++) {
    arr[i] = i;
}

// 现在想在数组末尾追加一个元素 4
arr[4] = 4;

// 再在数组末尾追加一个元素 5
arr[5] = 5;

// 依此类推
// ...
```

**可以看到，由于只是对索引赋值，所以在数组末尾追加元素的时间复杂度是 O(1)O(1)O(1)**。

情况二，数组中间插入（insert）元素

比方说，我有一个大小为 10 的数组 `arr`，前 4 个位置装了元素，现在想在第 3 个位置（索引 2 `arr[2]`）插入一个新元素，怎么办？

这就要涉及「数据搬移」，给新元素腾出空位，然后再才能插入新元素。大概的代码逻辑是这样的：

```java
// 大小为 10 的数组已经装了 4 个元素
int[] arr = new int[10];
for (int i = 0; i < 4; i++) {
    arr[i] = i;
}

// 在索引 2 置插入元素 666
// 需要把索引 2 以及之后的元素都往后移动一位
// 注意要倒着遍历数组中已有元素避免覆盖，不懂的话请看下方可视化面板
for (int i = 4; i > 2; i--) {
    arr[i] = arr[i - 1];
}

// 现在第 3 个位置空出来了，可以插入新元素
arr[2] = 666;
```

算法可视化

**综上，在数组中间插入元素的时间复杂度是 O(N)O(N)O(N)，因为涉及到数据搬移，给新元素腾地方**。

情况三，数组空间已满

静态数组在创建时就要确定大小，比方说现在我创建了一个数组 `int arr[10]`（一块 40 字节的连续内存空间），然后往里面存了 10 个元素，这时候我想再插入一个元素，怎么办？无论是追加在尾部还是插入到中间，都没有位置留给新元素了。

有的读者可能说，这个简单呀，在这 40 字节后面再加上 4 个字节的连续内存空间，用来存储新的元素，不就行了吗？

**不行的，连续内存必须一次性分配，分配完了之后就不能随意增减了**。因为你这块连续内存后面的内存空间可能已经被其他程序占用了，不能说你想要就给你。

那怎么办呢？只能重新申请一块更大的内存空间，把原来的数据复制过去，再插入新的元素，这就是数组的「扩容」操作。

比方说，我重新创建一个更大的数组 `int arr[20]`，然后把原来的 10 个元素复制过去，这样就有空余位置插入新的元素了。

大概的逻辑是这样的：

```java
// 大小为 10 的数组已经装满了
int[] arr = new int[10];
for (int i = 0; i < 10; i++) {
    arr[i] = i;
}

// 现在想在数组末尾追加一个元素 10
// 需要先扩容数组
int[] newArr = new int[20];
// 把原来的 10 个元素复制过去
for (int i = 0; i < 10; i++) {
    newArr[i] = arr[i];
}

// 旧数组的内存空间将由垃圾收集器处理
// ...

// 在新的大数组中追加新元素
newArr[10] = 10;
```

**综上，数组的扩容操作会涉及到新数组的开辟和数据的复制，时间复杂度是 O(N)O(N)O(N)**。

### 删

删除元素的操作和增加元素的操作类似，也需要分情况讨论。

情况一，删除末尾元素

比方说，我有一个大小为 10 的数组，里面装了 5 个元素，现在想删除末尾的元素，怎么办？

很简单，直接把末尾元素标记为一个特殊值代表已删除就行了，我们这里简单举例，就用 -1 作为特殊值代表已删除好了。后面带大家具体实现动态数组的时候，会有更完善的方法删除数组元素，**这里只是为了说明删除数组尾部元素的本质就是进行一次随机访问，时间复杂度是 O(1)O(1)O(1)**。

大概的代码逻辑是这样的：

```java
// 大小为 10 的数组已经装了 5 个元素
int[] arr = new int[10];
for (int i = 0; i < 5; i++) {
    arr[i] = i;
}

// 删除末尾元素，暂时用 -1 代表元素已删除
arr[4] = -1;
```

情况二，删除中间元素

比方说，我有一个大小为 10 的数组，里面装了 5 个元素，现在想删除第 2 个元素（`arr[1]`），怎么办？

这也要涉及「数据搬移」，把被删元素后面的元素都往前移动一位，保持数组元素的连续性。

大概的代码逻辑是这样的：

```java
// 大小为 10 的数组已经装了 5 个元素
int[] arr = new int[10];
for (int i = 0; i < 5; i++) {
    arr[i] = i;
}

// 删除 arr[1]
// 需要把 arr[1] 之后的元素都往前移动一位
// 注意要正着遍历数组中已有元素避免覆盖，不懂的话请看下方可视化面板
for (int i = 1; i < 4; i++) {
    arr[i] = arr[i + 1];
}

// 最后一个元素置为 -1 代表已删除
arr[4] = -1;
```

算法可视化

**综上，在数组中间删除元素的时间复杂度是 O(N)O(N)O(N)，因为涉及到数据搬移**。

### 总结

综上，静态数组的增删查改操作的时间复杂度是：

- 增：
  - 在末尾追加元素：O(1)O(1)O(1)。
  - 在中间（非末尾）插入元素：O(N)O(N)O(N)。
- 删：
  - 删除末尾元素：O(1)O(1)O(1)。
  - 删除中间（非末尾）元素：O(N)O(N)O(N)。
- 查：给定指定索引，查询索引对应的元素的值，时间复杂度 O(1)O(1)O(1)。
- 改：给定指定索引，修改索引对应的元素的值，时间复杂度 O(1)O(1)O(1)。

有读者可能问，刚才不是还探讨过数组的扩容操作吗，扩容涉及到新数组空间的开辟和数据的复制，时间复杂度是 O(N)O(N)O(N)，这个复杂度为什么没有算到「增」的复杂度里面呢？

这个问题很好，但并不是每次增加元素的时候都会触发扩容，所以扩容的复杂度要用「均摊时间复杂度」来分析，这个概念我在 [时空复杂度分析方法](https://labuladong.online/zh/algo/essential-technique/complexity-analysis/) 中有详细的讲解，这里就不展开了。

还有个问题初学者要注意，我们说数组的查、改复杂度是 O(1)O(1)O(1)，这个仅仅适用于给定索引的情况。如果反过来，比方说给你一个值，让你去找这个值在数组中对应的索引，那你只能遍历整个数组去寻找对吧，这个复杂度就是 O(N)O(N)O(N) 了。

所以说要搞清楚原理，而不要去背概念。原理懂了，概念你自己都能推导出来的。

## 动态数组

刚才讲了静态数组的超能力和种种局限性，现在讲动态数组，动态数组是静态数组的强化版，也是我们在实际软件开发或者写算法题时最常用的数据结构之一。

首先，你不要以为动态数组可以解决静态数组在中间增删元素效率差的问题，不可能解决的。数组随机访问的超能力源于数组连续的内存空间，而连续的内存空间就不可避免地面对数据搬移和扩缩容的问题。

**动态数组底层还是静态数组，只是自动帮我们进行数组空间的扩缩容，并把增删查改操作进行了封装，让我们使用起来更方便而已**。

简单列举一下各个语言的动态数组使用方法：

```java
// 创建动态数组
// 不用显式指定数组大小，它会根据实际存储的元素数量自动扩缩容
ArrayList<Integer> arr = new ArrayList<>();

for (int i = 0; i < 10; i++) {
    // 在末尾追加元素，时间复杂度 O(1)
    arr.add(i);
}

// 在中间插入元素，时间复杂度 O(N)
// 在索引 2 的位置插入元素 666
arr.add(2, 666);

// 在头部插入元素，时间复杂度 O(N)
arr.add(0, -1);

// 删除末尾元素，时间复杂度 O(1)
arr.remove(arr.size() - 1);

// 删除中间元素，时间复杂度 O(N)
// 删除索引 2 的元素
arr.remove(2);

// 根据索引查询元素，时间复杂度 O(1)
int a = arr.get(0);

// 根据索引修改元素，时间复杂度 O(1)
arr.set(0, 100);

// 根据元素值查找索引，时间复杂度 O(N)
int index = arr.indexOf(666);
```

在后面的章节，我会手把手带大家实现一个动态数组，让大家更加深入地理解动态数组的原理。

[上一篇时间空间复杂度入门](https://labuladong.online/zh/algo/intro/complexity-basic/)[下一篇动态数组代码实现](https://labuladong.online/zh/algo/data-structure-basic/array-implement/)

---

### 4. 动态数组代码实现

原文链接: <https://labuladong.online/zh/algo/data-structure-basic/array-implement/>

前置知识

阅读本文前，你需要先学习：

- [数组（顺序存储）基础](https://labuladong.online/zh/algo/data-structure-basic/array-basic/)

## 几个关键点

下面我会直接给出一个简单的动态数组代码实现，包含了基本的增删查改功能。这里先给出几个关键点，等会你看代码的时候可以着重注意一下。

### 关键点一、自动扩缩容

在上一章 [数组基础](https://labuladong.online/zh/algo/data-structure-basic/array-basic/) 中只提到了数组添加元素时可能需要扩容，并没有提到缩容。

在实际使用动态数组时，缩容也是重要的优化手段。比方说一个动态数组开辟了能够存储 1000 个元素的连续内存空间，但是实际只存了 10 个元素，那就有 990 个空间是空闲的。为了避免资源浪费，我们其实可以适当缩小存储空间，这就是缩容。

我们这里就实现一个简单的扩缩容的策略：

- 当数组元素个数达到底层静态数组的容量上限时，扩容为原来的 2 倍；
- 当数组元素个数缩减到底层静态数组的容量的 1/4 时，缩容为原来的 1/2。

### 关键点二、索引越界的检查

下面的代码实现中，有两个检查越界的方法，分别是 `checkElementIndex` 和 `checkPositionIndex`，你可以看到它俩的区别仅仅在于 `index < size` 和 `index <= size`。

为什么 `checkPositionIndex` 可以允许 `index == size` 呢，因为这个 `checkPositionIndex` 是专门用来处理在数组中插入元素的情况。

比方说有这样一个 `nums` 数组，对于每个元素来说，合法的索引一定是 `index < size`：

```text
nums = [5, 6, 7, 8]
index   0  1  2  3
```

但如果是要在数组中插入新元素，那么新元素可能的插入位置并不是元素的索引，而是索引之间的空隙：

```text
nums = [ | 5 | 6 | 7 | 8 | ]
index    0   1   2   3   4
```

这些空隙都是合法的插入位置，所以说 `index == size` 也是合法的。这就是 `checkPositionIndex` 和 `checkElementIndex` 的区别。

### 关键点三、删除元素谨防内存泄漏

单从算法的角度，其实并不需要关心被删掉的元素应该如何处理，但是具体到代码实现，我们需要注意可能出现的内存泄漏。

在我给出的代码实现中，删除元素时，我都会把被删除的元素置为 `null`，以 Java 为例：

```text
// 删
public E removeLast() {
    E deletedVal = data[size - 1];
    // 删除最后一个元素
    // 必须给最后一个元素置为 null，否则会内存泄漏
    data[size - 1] = null;
    size--;

    return deletedVal;
}
```

Java 的垃圾回收机制是基于 [图算法](https://labuladong.online/zh/algo/data-structure-basic/graph-basic/) 的可达性分析，如果一个对象再也无法被访问到，那么这个对象占用的内存才会被释放；否则，垃圾回收器会认为这个对象还在使用中，就不会释放这个对象占用的内存。

如果你不执行 `data[size - 1] = null` 这行代码，那么 `data[size - 1]` 这个引用就会一直存在，你可以通过 `data[size - 1]` 访问这个对象，所以这个对象被认为是可达的，它的内存就一直不会被释放，进而造成内存泄漏。

其他带垃圾回收功能的语言应该也是类似的，你可以具体了解一下你使用的编程语言的垃圾回收机制，这是写出无 bug 代码的基本要求。

### 其他细节优化

下面的代码当然不会是一个很完善的实现，会有不少可以进一步优化的点。比方说，我是用 for 循环复制数组数据的，实际上这种方式复制的效率比较差，大部分编程语言会提供更高效的数组复制方法，比如 Java 的 `System.arraycopy`。

不过它再怎么优化，本质上也是要搬移数据，时间复杂度都是 O(n)O(n)O(n)。本文的重点在于让你理解数组增删查改 API 的基本实现思路以及时间复杂度，如果对这些细节感兴趣，可以找到编程语言标准库的源码深入研究。

如何验证你的实现？

你可以借助力扣第 707 题「[设计链表](https://leetcode.cn/problems/design-linked-list/)」来验证自己的实现是否正确。虽然这道题是关于链表的，但是它其实也不知道你底层到底是不是用链表实现的。咱主要是借用它的测试用例，来验证你的增删查改功能是否正确。

## 动态数组代码实现

```java
import java.util.Arrays;
import java.util.Iterator;
import java.util.NoSuchElementException;

public class MyArrayList<E> {
    // 真正存储数据的底层数组
    private E[] data;
    // 记录当前元素个数
    private int size;
    // 默认初始容量
    private static final int INIT_CAP = 1;

    public MyArrayList() {
        this(INIT_CAP);
    }

    public MyArrayList(int initCapacity) {
        data = (E[]) new Object[initCapacity];
        size = 0;
    }

    // 增
    public void addLast(E e) {
        int cap = data.length;
        // 看 data 数组容量够不够
        if (size == cap) {
            resize(2 * cap);
        }
        // 在尾部插入元素
        data[size] = e;
        size++;
    }

    public void add(int index, E e) {
        // 检查索引越界
        checkPositionIndex(index);

        int cap = data.length;
        // 看 data 数组容量够不够
        if (size == cap) {
            resize(2 * cap);
        }

        // 搬移数据 data[index..] -> data[index+1..]
        // 给新元素腾出位置
        for (int i = size - 1; i >= index; i--) {
            data[i + 1] = data[i];
        }

        // 插入新元素
        data[index] = e;

        size++;
    }

    public void addFirst(E e) {
        add(0, e);
    }

    // 删
    public E removeLast() {
        if (size == 0) {
            throw new NoSuchElementException();
        }
        int cap = data.length;
        // 可以缩容，节约空间
        if (size == cap / 4) {
            resize(cap / 2);
        }

        E deletedVal = data[size - 1];
        // 删除最后一个元素
        // 必须给最后一个元素置为 null，否则会内存泄漏
        data[size - 1] = null;
        size--;

        return deletedVal;
    }

    public E remove(int index) {
        // 检查索引越界
        checkElementIndex(index);

        int cap = data.length;
        // 可以缩容，节约空间
        if (size == cap / 4) {
            resize(cap / 2);
        }

        E deletedVal = data[index];

        // 搬移数据 data[index+1..] -> data[index..]
        for (int i = index + 1; i < size; i++) {
            data[i - 1] = data[i];
        }

        data[size - 1] = null;
        size--;

        return deletedVal;
    }

    public E removeFirst() {
        return remove(0);
    }

    // 查
    public E get(int index) {
        // 检查索引越界
        checkElementIndex(index);

        return data[index];
    }

    // 改
    public E set(int index, E element) {
        // 检查索引越界
        checkElementIndex(index);
        // 修改数据
        E oldVal = data[index];
        data[index] = element;
        return oldVal;
    }

    // 工具方法
    public int size() {
        return size;
    }

    public boolean isEmpty() {
        return size == 0;
    }

    // 将 data 的容量改为 newCap
    private void resize(int newCap) {
        E[] temp = (E[]) new Object[newCap];

        for (int i = 0; i < size; i++) {
            temp[i] = data[i];
        }

        data = temp;
    }

    private boolean isElementIndex(int index) {
        return index >= 0 && index < size;
    }

    private boolean isPositionIndex(int index) {
        return index >= 0 && index <= size;
    }

    
    // 检查 index 索引位置是否可以存在元素
    private void checkElementIndex(int index) {
        if (!isElementIndex(index))
            throw new IndexOutOfBoundsException("Index: " + index + ", Size: " + size);
    }

    
    // 检查 index 索引位置是否可以添加元素
    private void checkPositionIndex(int index) {
        if (!isPositionIndex(index))
            throw new IndexOutOfBoundsException("Index: " + index + ", Size: " + size);
    }

    private void display() {
        System.out.println("size = " + size + " cap = " + data.length);
        System.out.println(Arrays.toString(data));
    }

    public static void main(String[] args) {
        // 初始容量设置为 3
        MyArrayList<Integer> arr = new MyArrayList<>(3);

        // 添加 5 个元素
        for (int i = 1; i <= 5; i++) {
            arr.addLast(i);
        }

        arr.remove(3);
        arr.add(1, 9);
        arr.addFirst(100);
        int val = arr.removeLast();

        for (int i = 0; i < arr.size(); i++) {
            System.out.println(arr.get(i));
        }
    }

}
```

[上一篇数组（顺序存储）基本原理](https://labuladong.online/zh/algo/data-structure-basic/array-basic/)[下一篇链表（链式存储）基本原理](https://labuladong.online/zh/algo/data-structure-basic/linkedlist-basic/)

---

## 4. 手把手带你实现单/双链表

### 5. 链表（链式存储）基本原理

原文链接: <https://labuladong.online/zh/algo/data-structure-basic/linkedlist-basic/>

刷过力扣的读者肯定对单链表非常熟悉，力扣上的单链表节点定义如下：

```java
class ListNode {
    int val;
    ListNode next;
    ListNode(int x) { val = x; }
}
```

这仅仅是一个最简单的**单链表节点**，方便力扣出算法题来考你。在实际的编程语言中，我们使用的链表节点会稍微复杂一点，类似这样：

```java
class Node<E> {
    E val;
    Node<E> next;
    Node<E> prev;

    Node(Node<E> prev, E element, Node<E> next) {
        this.val = element;
        this.next = next;
        this.prev = prev;
    }
}
```

主要区别有两个：

1、编程语言标准库一般都会提供泛型，即你可以指定 `val` 字段为任意类型，而力扣的单链表节点的 `val` 字段只有 int 类型。

2、编程语言标准库一般使用的都是双链表而非单链表。单链表节点只有一个 `next` 指针，指向下一个节点；而双链表节点有两个指针，`prev` 指向前一个节点，`next` 指向下一个节点。

有了 `prev` 前驱指针，链表支持双向遍历，但由于要多维护一个指针，增删查改时会稍微复杂一些，后面带大家实现双链表时会具体介绍。

## 为什么需要链表

前面介绍了 [数组（顺序存储）的底层原理](https://labuladong.online/zh/algo/data-structure-basic/array-basic/)，说白了就是一块连续的内存空间，有了这块内存空间的首地址，就能直接通过索引计算出任意位置的元素地址。

链表不一样，一条链表并不需要一整块连续的内存空间存储元素。链表的元素可以分散在内存空间的天涯海角，通过每个节点上的 `next, prev` 指针，将零散的内存块串联起来形成一个链式结构。

这样做的好处很明显，首先就是可以提高内存的利用效率，链表的节点不需要挨在一起，给点内存 new 出来一个节点就能用，操作系统会觉得这娃好养活。

另外一个好处，它的节点要用的时候就能接上，不用的时候拆掉就行了，从来不需要考虑扩缩容和数据搬移的问题，理论上讲，链表是没有容量限制的（除非把所有内存都占满，这不太可能）。

当然，不可能只有好处没有局限性。数组最大的优势是支持通过索引快速访问元素，而链表就不支持。

这个不难理解吧，因为元素并不是紧挨着的，所以如果你想要访问第 3 个链表元素，你就只能从头结点开始往顺着 `next` 指针往后找，直到找到第 3 个节点才行。

上面是对链表这种数据结构的基本介绍，接下来我们就结合代码实现单/双链表的几个基本操作。

## 单链表的基本操作

我先写一个工具函数，用于创建一条单链表，方便后面的讲解：

```java
class ListNode {
    int val;
    ListNode next;
    ListNode(int x) { val = x; }
}

// 输入一个数组，转换为一条单链表
ListNode createLinkedList(int[] arr) {
    if (arr == null || arr.length == 0) {
        return null;
    }
    ListNode head = new ListNode(arr[0]);
    ListNode cur = head;
    for (int i = 1; i < arr.length; i++) {
        cur.next = new ListNode(arr[i]);
        cur = cur.next;
    }
    return head;
}
```

### 查/改

单链表的遍历/查找/修改

比方说，我想访问单链表的每一个节点，并打印其值，可以这样写：

```java
// 创建一条单链表
ListNode head = createLinkedList(new int[]{1, 2, 3, 4, 5});

// 遍历单链表
for (ListNode p = head; p != null; p = p.next) {
    System.out.println(p.val);
}
```

类似的，如果是要通过索引访问或修改链表中的某个节点，也只能用 for 循环从头结点开始往后找，直到找到索引对应的节点，然后进行访问或修改。

这个操作的最坏时间复杂度是 O(n)O(n)O(n)，其中 nnn 是链表的长度。

### 增

在单链表头部插入新元素

我们会持有单链表的头结点，所以只需要将插入的节点接到头结点之前，并将新插入的节点作为头结点即可。

```java
// 创建一条单链表
ListNode head = createLinkedList(new int[]{1, 2, 3, 4, 5});

// 在单链表头部插入一个新节点 0
ListNode newNode = new ListNode(0);
newNode.next = head;
head = newNode;

// 现在链表变成了 0 -> 1 -> 2 -> 3 -> 4 -> 5
```

这个操作的时间复杂度是 O(1)O(1)O(1)。

在单链表尾部插入新元素

直接看代码吧，很简单：

```java
// 创建一条单链表
ListNode head = createLinkedList(new int[]{1, 2, 3, 4, 5});

// 在单链表尾部插入一个新节点 6
ListNode p = head;
// 先走到链表的最后一个节点
while (p.next != null) {
    p = p.next;
}
// 现在 p 就是链表的最后一个节点
// 在 p 后面插入新节点
p.next = new ListNode(6);

// 现在链表变成了 1 -> 2 -> 3 -> 4 -> 5 -> 6
```

这个操作的时间复杂度是 O(n)O(n)O(n)，因为需要先遍历到链表尾部。当然，如果我们持有对链表尾节点的引用，那么在尾部插入新节点的操作就会变得非常简单，不用每次从头去遍历了。这个优化会在后面具体实现双链表时介绍。

在单链表尾部插入新元素
在单链表中间插入新元素

这个操作稍微有点复杂，我们还是要先找到要插入位置的前驱节点，然后操作前驱节点把新节点插入进去：

```java
// 创建一条单链表
ListNode head = createLinkedList(new int[]{1, 2, 3, 4, 5});

// 在第 3 个节点后面插入一个新节点 66
// 先要找到前驱节点，即第 3 个节点
ListNode p = head;
for (int i = 0; i < 2; i++) {
    p = p.next;
}
// 此时 p 指向第 3 个节点
// 组装新节点的后驱指针
ListNode newNode = new ListNode(66);
newNode.next = p.next;

// 插入新节点
p.next = newNode;

// 现在链表变成了 1 -> 2 -> 3 -> 66 -> 4 -> 5
```

这个操作的时间复杂度是 O(n)O(n)O(n)，因为需要先找到插入位置的前驱节点。

在单链表中间插入新元素
### 删

在单链表中删除一个节点

删除一个节点，首先要找到要被删除节点的前驱节点，然后把这个前驱节点的 `next` 指针指向被删除节点的下一个节点。这样就能把被删除节点从链表中摘除了。

```java
// 创建一条单链表
ListNode head = createLinkedList(new int[]{1, 2, 3, 4, 5});

// 删除第 4 个节点，要操作前驱节点
ListNode p = head;
for (int i = 0; i < 2; i++) {
    p = p.next;
}

// 此时 p 指向第 3 个节点，即要删除节点的前驱节点
// 把第 4 个节点从链表中摘除
p.next = p.next.next;

// 现在链表变成了 1 -> 2 -> 3 -> 5
```

这个操作的时间复杂度是 O(n)O(n)O(n)，因为需要先找到被删除节点的前驱节点。

在单链表中删除一个节点
在单链表尾部删除元素

这个操作比较简单，找到倒数第二个节点，然后把它的 `next` 指针置为 null 就行了：

```java
// 创建一条单链表
ListNode head = createLinkedList(new int[]{1, 2, 3, 4, 5});

// 删除尾节点
ListNode p = head;
// 找到倒数第二个节点
while (p.next.next != null) {
    p = p.next;
}

// 此时 p 指向倒数第二个节点
// 把尾节点从链表中摘除
p.next = null;

// 现在链表变成了 1 -> 2 -> 3 -> 4
```

这个操作的时间复杂度是 O(n)O(n)O(n)，因为需要先遍历到倒数第二个节点。

在单链表尾部删除元素
在单链表头部删除元素

这个操作比较简单，直接把 `head` 移动到下一个节点就行了，直接看代码吧：

```java
// 创建一条单链表
ListNode head = createLinkedList(new int[]{1, 2, 3, 4, 5});

// 删除头结点
head = head.next;

// 现在链表变成了 2 -> 3 -> 4 -> 5
```

这个操作的时间复杂度是 O(1)O(1)O(1)。

不过可能有读者疑惑，之前那个旧的头结点 `1` 的 next 指针依然指向着节点 `2`，这样会不会造成内存泄漏？

不会的，这个节点 `1` 指向其他的节点是没关系的，只要保证没有其他引用指向这个节点 `1`，它就能被垃圾回收器回收掉。

当然，如果你非要显式把节点 `1` 的 next 指针置为 null，这是个很好的习惯，在其他场景中可能可以避免指针错乱的潜在问题。

在下面这个可视化面板中，我显式地把待删除节点的 next 指针置为 null 了：

在单链表头部删除元素
是不是觉得复杂？

链表的增删查改操作确实比数组复杂。这是因为链表的节点不是紧挨着的，所以要增删一个节点，必须先找到它的前驱和后驱节点进行协同，然后才能通过指针操作把它插入或删除。

上面给出的代码还仅仅是最简单的例子，你会发现在头部、尾部、中间增删元素的代码都不一样。如果要实现一个真正可用的链表，你还要考虑到很多边界情况，比如链表可能为空、前后驱节点可能为空等，这些情况都得保证不出错。

而且，上面只是介绍了「单链表」，而我们下一章要实现的是「双链表」，双链表要同时维护前驱和后驱指针，指针操作会更复杂一些。

是不是已经不敢想了？不要怕，其实没你想的那么难，几个原因：

1、其实搞来搞去就那几个操作，等会儿带你动手实现链表 API 的时候，你亲自写一写，就会了。

2、复杂操作我都配了可视化面板，你可以结合面板中的代码和动画进行理解。

3、最重要的，我们会使用「**虚拟头结点**」技巧，把头、尾、中部的操作统一起来，同时还能避免处理头尾指针为空情况的边界情况。

虚拟节点技巧在 [单链表经典算法技巧](https://labuladong.online/zh/algo/essential-technique/linked-list-skills-summary/) 中也会经常运用，这里仅仅简单提一下，具体实现会在后面讲到。

## 双链表的基本操作

我先写一个工具函数，用于创建一条双链表，方便后面的讲解：

```java
class DoublyListNode {
    int val;
    DoublyListNode next, prev;
    DoublyListNode(int x) { val = x; }
}

DoublyListNode createDoublyLinkedList(int[] arr) {
    if (arr == null || arr.length == 0) {
        return null;
    }
    DoublyListNode head = new DoublyListNode(arr[0]);
    DoublyListNode cur = head;
    // for 循环迭代创建双链表
    for (int i = 1; i < arr.length; i++) {
        DoublyListNode newNode = new DoublyListNode(arr[i]);
        cur.next = newNode;
        newNode.prev = cur;
        cur = cur.next;
    }
    return head;
}
```

### 查/改

双链表的遍历/查找/修改

对于双链表的遍历和查找，我们可以从头节点或尾节点开始，根据需要向前或向后遍历：

```java
// 创建一条双链表
DoublyListNode head = createDoublyLinkedList(new int[]{1, 2, 3, 4, 5});
DoublyListNode tail = null;

// 从头节点向后遍历双链表
for (DoublyListNode p = head; p != null; p = p.next) {
    System.out.println(p.val);
    tail = p;
}

// 从尾节点向前遍历双链表
for (DoublyListNode p = tail; p != null; p = p.prev) {
    System.out.println(p.val);
}
```

这个操作的最坏时间复杂度是 O(n)O(n)O(n)。访问或修改节点时，可以根据索引是靠近头部还是尾部，选择合适的方向遍历，这样可以一定程度上提高效率。

### 增

在双链表头部插入新元素

在双链表头部插入元素，需要调整新节点和原头节点的指针：

```java
// 创建一条双链表
DoublyListNode head = createDoublyLinkedList(new int[]{1, 2, 3, 4, 5});

// 在双链表头部插入新节点 0
DoublyListNode newHead = new DoublyListNode(0);
newHead.next = head;
head.prev = newHead;
head = newHead;
// 现在链表变成了 0 -> 1 -> 2 -> 3 -> 4 -> 5
```

这个操作的时间复杂度是 O(1)O(1)O(1)。

在双链表头部插入新元素
在双链表尾部插入新元素

在双链表尾部插入元素时，如果我们持有尾节点的引用，这个操作会非常简单：

```java
// 创建一条双链表
DoublyListNode head = createDoublyLinkedList(new int[]{1, 2, 3, 4, 5});

DoublyListNode tail = head;
// 先走到链表的最后一个节点
while (tail.next != null) {
    tail = tail.next;
}

// 在双链表尾部插入新节点 6
DoublyListNode newNode = new DoublyListNode(6);
tail.next = newNode;
newNode.prev = tail;
// 更新尾节点引用
tail = newNode;

// 现在链表变成了 1 -> 2 -> 3 -> 4 -> 5 -> 6
```

这个操作的时间复杂度是 O(n)O(n)O(n)，因为需要先遍历到尾节点。如果持有尾节点引用，则是 O(1)O(1)O(1)。

在双链表尾部插入新元素
在双链表中间插入新元素

在双链表的指定位置插入新元素，需要调整前驱节点和后继节点的指针。

比如下面的例子，把元素 66 插入到索引 3（第 4 个节点）的位置：

```java
// 创建一条双链表
DoublyListNode head = createDoublyLinkedList(new int[]{1, 2, 3, 4, 5});

// 想要插入到索引 3（第 4 个节点）
// 需要操作索引 2（第 3 个节点）的指针
DoublyListNode p = head;
for (int i = 0; i < 2; i++) {
    p = p.next;
}

// 组装新节点
DoublyListNode newNode = new DoublyListNode(66);
newNode.next = p.next;
newNode.prev = p;

// 插入新节点
p.next.prev = newNode;
p.next = newNode;

// 现在链表变成了 1 -> 2 -> 3 -> 66 -> 4 -> 5
```

这个操作的时间复杂度是 O(n)O(n)O(n)，因为需要先找到插入位置。

在双链表中间插入新元素
### 删

在双链表中删除一个节点

在双链表中删除节点时，需要调整前驱节点和后继节点的指针来摘除目标节点：

```java
// 创建一条双链表
DoublyListNode head = createDoublyLinkedList(new int[]{1, 2, 3, 4, 5});

// 删除第 4 个节点
// 先找到第 3 个节点
DoublyListNode p = head;
for (int i = 0; i < 2; i++) {
    p = p.next;
}

// 现在 p 指向第 3 个节点，我们它后面那个节点摘除出去
DoublyListNode toDelete = p.next;

// 把 toDelete 从链表中摘除
p.next = toDelete.next;
toDelete.next.prev = p;

// 把 toDelete 的前后指针都置为 null 是个好习惯（可选）
toDelete.next = null;
toDelete.prev = null;

// 现在链表变成了 1 -> 2 -> 3 -> 5
```

这个操作的时间复杂度是 O(n)O(n)O(n)，因为需要先找到被删除节点的位置。如果已知被删除节点的引用，则删除操作本身是 O(1)O(1)O(1)。

在双链表中删除一个节点
在双链表头部删除元素

在双链表头部删除元素需要调整头节点的指针：

```java
// 创建一条双链表
DoublyListNode head = createDoublyLinkedList(new int[]{1, 2, 3, 4, 5});

// 删除头结点
DoublyListNode toDelete = head;
head = head.next;
head.prev = null;

// 清理已删除节点的指针
toDelete.next = null;

// 现在链表变成了 2 -> 3 -> 4 -> 5
```

这个操作的时间复杂度是 O(1)O(1)O(1)。

在双链表头部删除元素
在双链表尾部删除元素

在单链表中，由于缺乏前驱指针，所以删除尾节点时需要遍历到倒数第二个节点，操作它的 `next` 指针，才能把尾节点摘除出去。

但在双链表中，由于每个节点都存储了前驱节点的指针，所以我们可以直接操作尾节点，把它自己从链表中摘除：

```java
// 创建一条双链表
DoublyListNode head = createDoublyLinkedList(new int[]{1, 2, 3, 4, 5});

// 删除尾节点
DoublyListNode p = head;
// 找到尾结点
while (p.next != null) {
    p = p.next;
}

// 现在 p 指向尾节点
// 把尾节点从链表中摘除
p.prev.next = null;

// 把被删结点的指针都断开是个好习惯（可选）
p.prev = null;

// 现在链表变成了 1 -> 2 -> 3 -> 4
```

这个操作的时间复杂度是 O(n)O(n)O(n)，因为需要先遍历到尾节点。如果持有尾节点引用，则是 O(1)O(1)O(1)。

在双链表尾部删除元素
## 接下来

在下一篇文章中，我们分别用单链表和双链表实现一个拥有增删查改等基本操作的 `MyLinkedList`，并且会使用「虚拟头结点」技巧简化代码逻辑，避免处理头尾指针为空情况的边界情况。

[上一篇动态数组代码实现](https://labuladong.online/zh/algo/data-structure-basic/array-implement/)[下一篇链表代码实现](https://labuladong.online/zh/algo/data-structure-basic/linkedlist-implement/)

---

### 6. 链表代码实现

原文链接: <https://labuladong.online/zh/algo/data-structure-basic/linkedlist-implement/>

读完本文，你不仅学会了算法套路，还可以顺便解决如下题目：

| LeetCode | 力扣 | 难度 |
| --- | --- | --- |
| [707. Design Linked List](https://leetcode.com/problems/design-linked-list/) | [707. 设计链表](https://leetcode.cn/problems/design-linked-list/) |  |

前置知识

阅读本文前，你需要先学习：

- [链表（链式存储）基础](https://labuladong.online/zh/algo/data-structure-basic/linkedlist-basic/)

## 几个关键点

下面我会分别用双链表和单链给出一个简单的 `MyLinkedList` 代码实现，包含了基本的增删查改功能。这里给出几个关键点，等会你看代码的时候可以着重注意一下。

### 关键点一、同时持有头尾节点的引用

在力扣做题时，一般题目给我们传入的就是单链表的头指针。但是在实际开发中，用的都是双链表，而双链表一般会同时持有头尾节点的引用。

因为在软件开发中，在容器尾部添加元素是个非常高频的操作，双链表持有尾部节点的引用，就可以在 O(1)O(1)O(1) 的时间复杂度内完成尾部添加元素的操作。

对于单链表来说，持有尾部节点的引用也有优化效果。比如你要在单链表尾部添加元素，如果没有尾部节点的引用，你就需要遍历整个链表找到尾部节点，时间复杂度是 O(n)O(n)O(n)；如果有尾部节点的引用，就可以在 O(1)O(1)O(1) 的时间复杂度内完成尾部添加元素的操作。

细心的读者可能会说，即便如此，如果删除一次单链表的尾结点，那么之前尾结点的引用就失效了，还是需要遍历一遍链表找到尾结点。

是的，但你再仔细想想，删除单链表尾结点的时候，是不是也得遍历到倒数第二个节点（尾结点的前驱），才能通过指针操作把尾结点删掉？那么这个时候，你不就可以顺便把尾结点的引用给更新了吗？

### 关键点二、虚拟头尾节点

在上一篇文章 [链表基础](https://labuladong.online/zh/algo/data-structure-basic/linkedlist-basic/) 中我提到过「虚拟头尾节点」技巧，它的原理很简单，就是在创建双链表时就创建一个虚拟头节点和一个虚拟尾节点，无论双链表是否为空，这两个节点都存在。这样就不会出现空指针的问题，可以避免很多边界情况的处理。

举例来说，假设虚拟头尾节点分别是 `dummyHead` 和 `dummyTail`，那么一条空的双链表长这样：

```text
dummyHead <-> dummyTail
```

如果你添加 `1,2,3` 几个元素，那么链表长这样：

```text
dummyHead <-> 1 <-> 2 <-> 3 <-> dummyTail
```

你以前要把在头部插入元素、在尾部插入元素和在中间插入元素几种情况分开讨论，现在有了头尾虚拟节点，无论链表是否为空，都只需要考虑在中间插入元素的情况就可以了，这样代码会简洁很多。

当然，虚拟头结点会多占用一点内存空间，但是比起给你解决的麻烦，这点空间消耗是划算的。

对于单链表，虚拟头结点有一定的简化作用，但虚拟尾节点没有太大作用。

虚拟节点是内部实现，对外不可见

虚拟节点是你内部实现数据结构的技巧，对外是不可见的。比如按照索引获取元素的 `get(index)` 方法，都是从真实节点开始计算索引，而不是从虚拟节点开始计算。

### 关键点三、内存泄露？

在前文 [动态数组实现](https://labuladong.online/zh/algo/data-structure-basic/array-implement/) 中，我提到了删除元素时，要注意内存泄露的问题。那么在链表中，删除元素会不会也有内存泄露的问题呢？

尤其是这样的写法，你觉得有没有问题：

```text
// 假设单链表头结点 head = 1 -> 2 -> 3 -> 4 -> 5

// 删除单链表头结点
head = head.next;

// 此时 head = 2 -> 3 -> 4 -> 5
```

细心的读者可能认为这样写会有内存泄露的问题，因为原来的那个头结点 `1` 的 `next` 指针没有断开，依然指向着节点 `2`。

但实际上这样写是 OK 的，因为 Java 的垃圾回收的判断机制是看这个对象是否被别人引用，而并不会 care 这个对象是否还引用着别人。

那个节点 `1` 的 `next` 指针确实还指向着节点 `2`，但是并没有别的指针引用节点 `1` 了，所以节点 `1` 最终会被垃圾回收器回收释放。所以说这个场景和数组中删除元素的场景是不一样的，你可以再仔细思考一下。

不过呢，删除节点时，最好还是把被删除节点的指针都置为 null，这是个好习惯，不会有什么代价，还可能避免一些潜在的问题。所以在下面的实现中，无论是否有必要，我都会把被删除节点上的指针置为 null。

如何验证你的实现？

你可以借助力扣第 707 题「[设计链表](https://leetcode.cn/problems/design-linked-list/)」来验证自己的实现是否正确。注意 707 题要求的增删查改 API 名字和本文给出的不一样，所以需要修改一下才能通过。

## 双链表代码实现

```java
import java.util.NoSuchElementException;

public class MyLinkedList<E> {
    // 虚拟头尾节点
    final private Node<E> head, tail;
    private int size;

    // 双链表节点
    private static class Node<E> {
        E val;
        Node<E> next;
        Node<E> prev;

        Node(E val) {
            this.val = val;
        }
    }

    // 构造函数初始化虚拟头尾节点
    public MyLinkedList() {
        this.head = new Node<>(null);
        this.tail = new Node<>(null);
        head.next = tail;
        tail.prev = head;
        this.size = 0;
    }

    // ***** 增 *****

    public void addLast(E e) {
        Node<E> x = new Node<>(e);
        Node<E> temp = tail.prev;
        // temp <-> x
        temp.next = x;
        x.prev = temp;

        x.next = tail;
        tail.prev = x;
        // temp <-> x <-> tail
        size++;
    }

    public void addFirst(E e) {
        Node<E> x = new Node<>(e);
        Node<E> temp = head.next;
        // head <-> temp
        temp.prev = x;
        x.next = temp;

        head.next = x;
        x.prev = head;
        // head <-> x <-> temp
        size++;
    }

    public void add(int index, E element) {
        checkPositionIndex(index);
        if (index == size) {
            addLast(element);
            return;
        }

        // 找到 index 对应的 Node
        Node<E> p = getNode(index);
        Node<E> temp = p.prev;
        // temp <-> p

        // 新要插入的 Node
        Node<E> x = new Node<>(element);

        p.prev = x;
        temp.next = x;

        x.prev = temp;
        x.next = p;

        // temp <-> x <-> p

        size++;
    }

    // ***** 删 *****

    public E removeFirst() {
        if (size < 1) {
            throw new NoSuchElementException();
        }
        // 虚拟节点的存在是我们不用考虑空指针的问题
        Node<E> x = head.next;
        Node<E> temp = x.next;
        // head <-> x <-> temp
        head.next = temp;
        temp.prev = head;

        E val = x.val;
        x.prev = null;
        x.next = null;
        // head <-> temp

        size--;
        return val;
    }

    public E removeLast() {
        if (size < 1) {
            throw new NoSuchElementException();
        }
        Node<E> x = tail.prev;
        Node<E> temp = tail.prev.prev;
        // temp <-> x <-> tail

        tail.prev = temp;
        temp.next = tail;

        E val = x.val;
        x.prev = null;
        x.next = null;
        // temp <-> tail

        size--;
        return val;
    }

    public E remove(int index) {
        checkElementIndex(index);
        // 找到 index 对应的 Node
        Node<E> x = getNode(index);
        Node<E> prev = x.prev;
        Node<E> next = x.next;
        // prev <-> x <-> next
        prev.next = next;
        next.prev = prev;

        E val = x.val;
        x.prev = null;
        x.next = null;
        // prev <-> next

        size--;
        return val;
    }

    // ***** 查 *****

    public E get(int index) {
        checkElementIndex(index);
        // 找到 index 对应的 Node
        Node<E> p = getNode(index);

        return p.val;
    }

    public E getFirst() {
        if (size < 1) {
            throw new NoSuchElementException();
        }

        return head.next.val;
    }

    public E getLast() {
        if (size < 1) {
            throw new NoSuchElementException();
        }

        return tail.prev.val;
    }

    // ***** 改 *****

    public E set(int index, E val) {
        checkElementIndex(index);
        // 找到 index 对应的 Node
        Node<E> p = getNode(index);

        E oldVal = p.val;
        p.val = val;

        return oldVal;
    }

    // ***** 其他工具函数 *****

    public int size() {
        return size;
    }

    public boolean isEmpty() {
        return size == 0;
    }

    private Node<E> getNode(int index) {
        checkElementIndex(index);
        Node<E> p = head.next;
        // TODO: 可以优化，通过 index 判断从 head 还是 tail 开始遍历
        for (int i = 0; i < index; i++) {
            p = p.next;
        }
        return p;
    }

    private boolean isElementIndex(int index) {
        return index >= 0 && index < size;
    }

    private boolean isPositionIndex(int index) {
        return index >= 0 && index <= size;
    }

    // 检查 index 索引位置是否可以存在元素
    private void checkElementIndex(int index) {
        if (!isElementIndex(index))
            throw new IndexOutOfBoundsException("Index: " + index + ", Size: " + size);
    }

    // 检查 index 索引位置是否可以添加元素
    private void checkPositionIndex(int index) {
        if (!isPositionIndex(index))
            throw new IndexOutOfBoundsException("Index: " + index + ", Size: " + size);
    }

    private void display() {
        System.out.println("size = " + size);
        for (Node<E> p = head.next; p != tail; p = p.next) {
            System.out.print(p.val + " <-> ");
        }
        System.out.println("null");
        System.out.println();
    }

    public static void main(String[] args) {
        MyLinkedList<Integer> list = new MyLinkedList<>();
        list.addLast(1);
        list.addLast(2);
        list.addLast(3);
        list.addFirst(0);
        list.add(2, 100);

        list.display();
        // size = 5
        // 0 <-> 1 <-> 100 <-> 2 -> 3 -> null
    }
}
```

## 单链表代码实现

```java
import java.util.NoSuchElementException;

public class MyLinkedList2<E> {

    private static class Node<E> {
        E val;
        Node<E> next;

        Node(E val) {
            this.val = val;
            this.next = null;
        }
    }

    private Node<E> head;
    // 实际的尾部节点引用
    private Node<E> tail;
    private int size;

    public MyLinkedList2() {
        this.head = new Node<>(null);
        this.tail = head;
        this.size = 0;
    }

    public void addFirst(E e) {
        Node<E> newNode = new Node<>(e);
        newNode.next = head.next;
        head.next = newNode;
        if (size == 0) {
            tail = newNode;
        }
        size++;
    }

    public void addLast(E e) {
        Node<E> newNode = new Node<>(e);
        tail.next = newNode;
        tail = newNode;
        size++;
    }

    public void add(int index, E element) {
        checkPositionIndex(index);

        if (index == size) {
            addLast(element);
            return;
        }

        Node<E> prev = head;
        for (int i = 0; i < index; i++) {
            prev = prev.next;
        }
        Node<E> newNode = new Node<>(element);
        newNode.next = prev.next;
        prev.next = newNode;
        size++;
    }

    public E removeFirst() {
        if (isEmpty()) {
            throw new NoSuchElementException();
        }
        Node<E> first = head.next;
        head.next = first.next;
        if (size == 1) {
            tail = head;
        }
        size--;
        return first.val;
    }

    public E removeLast() {
        if (isEmpty()) {
            throw new NoSuchElementException();
        }

        Node<E> prev = head;
        while (prev.next != tail) {
            prev = prev.next;
        }
        E val = tail.val;
        prev.next = null;
        tail = prev;
        size--;
        return val;
    }

    public E remove(int index) {
        checkElementIndex(index);

        Node<E> prev = head;
        for (int i = 0; i < index; i++) {
            prev = prev.next;
        }

        Node<E> nodeToRemove = prev.next;
        prev.next = nodeToRemove.next;
        // 删除的是最后一个元素
        if (index == size - 1) {
            tail = prev;
        }
        size--;
        return nodeToRemove.val;
    }

    // ***** 查 *****

    public E getFirst() {
        if (isEmpty()) {
            throw new NoSuchElementException();
        }
        return head.next.val;
    }

    public E getLast() {
        if (isEmpty()) {
            throw new NoSuchElementException();
        }
        return tail.val;
    }

    public E get(int index) {
        checkElementIndex(index);
        Node<E> p = getNode(index);
        return p.val;
    }

    // ***** 改 *****

    public E set(int index, E element) {
        checkElementIndex(index);
        Node<E> p = getNode(index);

        E oldVal = p.val;
        p.val = element;

        return oldVal;
    }

    // ***** 其他工具函数 *****
    public int size() {
        return size;
    }

    public boolean isEmpty() {
        return size == 0;
    }

    private boolean isElementIndex(int index) {
        return index >= 0 && index < size;
    }

    private boolean isPositionIndex(int index) {
        return index >= 0 && index <= size;
    }

    // 检查 index 索引位置是否可以存在元素
    private void checkElementIndex(int index) {
        if (!isElementIndex(index))
            throw new IndexOutOfBoundsException("Index: " + index + ", Size: " + size);
    }

    // 检查 index 索引位置是否可以添加元素
    private void checkPositionIndex(int index) {
        if (!isPositionIndex(index))
            throw new IndexOutOfBoundsException("Index: " + index + ", Size: " + size);
    }

    // 返回 index 对应的 Node
    // 注意：请保证传入的 index 是合法的
    private Node<E> getNode(int index) {
        Node<E> p = head.next;
        for (int i = 0; i < index; i++) {
            p = p.next;
        }
        return p;
    }

    public static void main(String[] args) {
        MyLinkedList2<Integer> list = new MyLinkedList2<>();
        list.addFirst(1);
        list.addFirst(2);
        list.addLast(3);
        list.addLast(4);
        list.add(2, 5);

        System.out.println(list.removeFirst()); // 2
        System.out.println(list.removeLast()); // 4
        System.out.println(list.remove(1)); // 5

        System.out.println(list.getFirst()); // 1
        System.out.println(list.getLast()); // 3
        System.out.println(list.get(1)); // 3
    }
}
```

[上一篇链表（链式存储）基本原理](https://labuladong.online/zh/algo/data-structure-basic/linkedlist-basic/)[下一篇实现贪吃蛇](https://labuladong.online/zh/algo/game/snake/)

---

## 5. 数组链表的种种变换

### 7. 环形数组技巧及实现

原文链接: <https://labuladong.online/zh/algo/data-structure-basic/cycle-array/>

前置知识

阅读本文前，你需要先学习：

- [数组（顺序存储）基础](https://labuladong.online/zh/algo/data-structure-basic/array-basic/)

一句话总结

环形数组技巧利用求模（余数）运算，将普通数组变成逻辑上的环形数组，可以让我们用 O(1)O(1)O(1) 的时间在数组头部增删元素。

## 环形数组原理

数组可能是环形的么？不可能。数组就是一块线性连续的内存空间，怎么可能有环的概念？

但是，我们可以在「逻辑上」把数组变成环形的，比如下面这段代码：

```java
// 长度为 5 的数组
int[] arr = new int[]{1, 2, 3, 4, 5};
int i = 0;
// 模拟环形数组，这个循环永远不会结束
while (i < arr.length) {
    System.out.println(arr[i]);
    i = (i + 1) % arr.length;
}
```

**这段代码的关键在于求模运算 `%`，也就是求余数**。当 `i` 到达数组末尾元素时，`i + 1` 和 `arr.length` 取余数又会变成 0，即会回到数组头部，这样就在逻辑上形成了一个环形数组，永远遍历不完。

这就是环形数组技巧。这个技巧如何帮助我们在 O(1)O(1)O(1) 的时间在数组头部增删元素呢？

是这样，假设我们现在有一个长度为 6 的数组，现在其中只装了 3 个元素，如下（未装元素的位置用 `_` 标识）：

```text
[1, 2, 3, _, _, _]
```

现在我们要在数组头部删除元素 `1`，那么我们可以把数组变成这样：

```text
[_, 2, 3, _, _, _]
```

即，我们仅仅把元素 `1` 的位置标记为空，但并不做数据搬移。

此时，如果我们要在数组头部增加元素 `4` 和元素 `5`，我们可以把数组变成这样：

```text
[4, 2, 3, _, _, 5]
```

你可以看到，当头部没有位置添加新元素时，它转了一圈，把新元素加到尾部了。

核心原理

上面只是让大家对环形数组有一个直观地印象，环形数组的关键在于，它维护了两个指针 `start` 和 `end`，`start` 指向第一个有效元素的索引，`end` 指向最后一个有效元素的下一个位置索引。

这样，当我们在数组头部添加或删除元素时，只需要移动 `start` 索引，而在数组尾部添加或删除元素时，只需要移动 `end` 索引。

当 `start, end` 移动超出数组边界（`< 0` 或 `>= arr.length`）时，我们可以通过求模运算 `%` 让它们转一圈到数组头部或尾部继续工作，这样就实现了环形数组的效果。

## 动手环节

纸上得来终觉浅，绝知此事要躬行。

我在可视化面板实现了一个简单的环形数组，你可以点击下面代码中的 `arr.addLast` 或 `arr.addFirst`，注意观察 `start, end` 指针以及 `arr` 数组中元素的变化：

算法可视化
## 代码实现

关键点、注意开闭区间

在我的代码中，环形数组的区间被定义为左闭右开的，即 `[start, end)` 区间包含数组元素。所以其他的方法都是以左闭右开区间为基础实现的。

那么肯定就会有读者问，为啥要左闭右开，我就是想两端都开，或者两端都闭，不行么？

**理论上，你可以随意设计区间的开闭，但一般设计为左闭右开区间是最方便处理的**。

因为这样初始化 `start = end = 0` 时，区间 `[0, 0)` 中没有元素，但只要让 `end` 向右移动（扩大）一位，区间 `[0, 1)` 就包含一个元素 `0` 了。

如果你设置为两端都开的区间，那么让 `end` 向右移动一位后开区间 `(0, 1)` 仍然没有元素；如果你设置为两端都闭的区间，那么初始区间 `[0, 0]` 就已经包含了一个元素。这两种情况都会给边界处理带来不必要的麻烦，如果你非要使用的话，需要在代码中做一些特殊处理。

最后，请看代码实现：

```java
public class CycleArray<T> {
    private T[] arr;
    private int start;
    private int end;
    private int count;
    private int size;

    public CycleArray() {
        this(1);
    }

    @SuppressWarnings("unchecked")
    public CycleArray(int size) {
        this.size = size;
        // 因为 Java 不支持直接创建泛型数组，所以这里使用了类型转换
        this.arr = (T[]) new Object[size];
        // start 指向第一个有效元素的索引，闭区间
        this.start = 0;
        // 切记 end 是一个开区间，
        // 即 end 指向最后一个有效元素的下一个位置索引
        this.end = 0;
        this.count = 0;
    }

    // 自动扩缩容辅助函数
    @SuppressWarnings("unchecked")
    private void resize(int newSize) {
        // 创建新的数组
        T[] newArr = (T[]) new Object[newSize];
        // 将旧数组的元素复制到新数组中
        for (int i = 0; i < count; i++) {
            newArr[i] = arr[(start + i) % size];
        }
        arr = newArr;
        // 重置 start 和 end 指针
        start = 0;
        end = count;
        size = newSize;
    }

    // 在数组头部添加元素，时间复杂度 O(1)
    public void addFirst(T val) {
        // 当数组满时，扩容为原来的两倍
        if (isFull()) {
            resize(size * 2);
        }
        // 因为 start 是闭区间，所以先左移，再赋值
        start = (start - 1 + size) % size;
        arr[start] = val;
        count++;
    }

    // 删除数组头部元素，时间复杂度 O(1)
    public void removeFirst() {
        if (isEmpty()) {
            throw new IllegalStateException("Array is empty");
        }
        // 因为 start 是闭区间，所以先赋值，再右移
        arr[start] = null;
        start = (start + 1) % size;
        count--;
        // 如果数组元素数量减少到原大小的四分之一，则减小数组大小为一半
        if (count > 0 && count == size / 4) {
            resize(size / 2);
        }
    }

    // 在数组尾部添加元素，时间复杂度 O(1)
    public void addLast(T val) {
        if (isFull()) {
            resize(size * 2);
        }
        // 因为 end 是开区间，所以是先赋值，再右移
        arr[end] = val;
        end = (end + 1) % size;
        count++;
    }

    // 删除数组尾部元素，时间复杂度 O(1)
    public void removeLast() {
        if (isEmpty()) {
            throw new IllegalStateException("Array is empty");
        }
        // 因为 end 是开区间，所以先左移，再赋值
        end = (end - 1 + size) % size;
        arr[end] = null;
        count--;
        // 缩容
        if (count > 0 && count == size / 4) {
            resize(size / 2);
        }
    }

    // 获取数组头部元素，时间复杂度 O(1)
    public T getFirst() {
        if (isEmpty()) {
            throw new IllegalStateException("Array is empty");
        }
        return arr[start];
    }

    // 获取数组尾部元素，时间复杂度 O(1)
    public T getLast() {
        if (isEmpty()) {
            throw new IllegalStateException("Array is empty");
        }
        // end 是开区间，指向的是下一个元素的位置，所以要减 1
        return arr[(end - 1 + size) % size];
    }

    public boolean isFull() {
        return count == size;
    }
    
    public int size() {
        return count;
    }

    public boolean isEmpty() {
        return count == 0;
    }
}
```

## 思考题

数组增删头部元素的效率真的只能是 O(N)O(N)O(N) 么？

我们都说，在数组增删头部元素的时间复杂度是 O(N)O(N)O(N)，因为需要搬移元素。但是，如果我们使用环形数组，其实是可以实现在 O(1)O(1)O(1) 的时间复杂度内增删头部元素的。

当然，上面实现的这个环形数组只提供了 `addFirst, removeFirst, addLast, removeLast` 这几个方法，并没有提供 [我们之前实现的动态数组](https://labuladong.online/zh/algo/data-structure-basic/array-implement/) 的某些方法，比如删除指定索引的元素，获取指定索引的元素，在指定索引插入元素等等。

但是你可以思考一下，难道环形数组实现不了这些方法么？环形数组实现这些方法，时间复杂度相比普通数组，有退化吗？

好像没有吧。

环形数组也可以删除指定索引的元素，也要做数据搬移，和普通数组一样，复杂度是 O(N)O(N)O(N)；

环形数组也可以获取指定索引的元素（随机访问），只不过不是直接访问对应索引，而是要通过 `start` 计算出真实索引，但计算和访问的时间复杂度依然是 O(1)O(1)O(1)；

环形数组也可以在指定索引插入元素，当然也要做数据搬移，和普通数组一样，复杂度是 O(N)O(N)O(N)。

你可以思考一下是不是这样。如果是这样，为什么编程语言的标准库中提供的动态数组容器底层并没有用环形数组技巧。

[上一篇实现贪吃蛇](https://labuladong.online/zh/algo/game/snake/)[下一篇跳表核心原理](https://labuladong.online/zh/algo/data-structure-basic/skip-list-basic/)

---

### 8. 双端队列（Deque）原理及实现

原文链接: <https://labuladong.online/zh/algo/data-structure-basic/deque-implement/>

前置知识

阅读本文前，你需要先学习：

- [队列/栈基本原理](https://labuladong.online/zh/algo/data-structure-basic/queue-stack-basic/)
- [环形数组技巧](https://labuladong.online/zh/algo/data-structure-basic/cycle-array/)

## 基本原理

如果你理解了前面讲解的内容，这个双端队列其实没啥可讲的了。所谓双端队列，主要是对比标准队列（FIFO 先进先出队列）多了一些操作罢了：

```java
class MyDeque<E> {
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
}
```

[标准队列](https://labuladong.online/zh/algo/data-structure-basic/queue-stack-basic/) 只能在队尾插入元素，队头删除元素，而双端队列的队头和队尾都可以插入或删除元素。

普通队列就好比排队买票，先来的先买，后来的后买；而双端队列就好比一个过街天桥，两端都可以随意进出。当然，双端队列的元素就不再满足「先进先出」了，因为它比较灵活嘛。

在做算法题的场景中，双端队列用的不算很多。感觉只有 Python 用到的多一些，因为 Python 标准库没有提供内置的栈和队列，一般会用双端队列来模拟标准队列。

## 用链表实现双端队列

很简单吧，直接复用我们之前实现的 [MyLinkedList](https://labuladong.online/zh/algo/data-structure-basic/linkedlist-implement/) 类，或者使用编程语言标准库提供的双链表结构就行了。因为双链表本就支持 O(1)O(1)O(1) 时间复杂度在链表的头尾增删元素：

```java
import java.util.LinkedList;

public class MyListDeque<E> {
    private LinkedList<E> list = new LinkedList<>();

    // 从队头插入元素，时间复杂度 O(1)
    void addFirst(E e) {
        list.addFirst(e);
    }

    // 从队尾插入元素，时间复杂度 O(1)
    void addLast(E e) {
        list.addLast(e);
    }

    // 从队头删除元素，时间复杂度 O(1)
    E removeFirst() {
        return list.removeFirst();
    }

    // 从队尾删除元素，时间复杂度 O(1)
    E removeLast() {
        return list.removeLast();
    }

    // 查看队头元素，时间复杂度 O(1)
    E peekFirst() {
        return list.getFirst();
    }

    // 查看队尾元素，时间复杂度 O(1)
    E peekLast() {
        return list.getLast();
    }

    public static void main(String[] args) {
        MyListDeque<Integer> deque = new MyListDeque<>();
        deque.addFirst(1);
        deque.addFirst(2);
        deque.addLast(3);
        deque.addLast(4);

        System.out.println(deque.removeFirst()); // 2
        System.out.println(deque.removeLast()); // 4
        System.out.println(deque.peekFirst()); // 1
        System.out.println(deque.peekLast()); // 3
    }
}
```

## 用数组实现双端队列

也很简单吧，直接复用我们在 [环形数组技巧](https://labuladong.online/zh/algo/data-structure-basic/cycle-array/) 中实现的 `CycleArray` 提供的方法就行了。环形数组头尾增删元素的复杂度都是 O(1)O(1)O(1)：

```java
class MyArrayDeque<E> {
    private CycleArray<E> arr = new CycleArray<>();

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
}
```

[上一篇用数组实现队列/栈](https://labuladong.online/zh/algo/data-structure-basic/array-queue-stack/)[下一篇哈希表核心原理](https://labuladong.online/zh/algo/data-structure-basic/hashmap-basic/)

---

## 6. 手把手带你实现队列/栈

### 9. 队列/栈基本原理

原文链接: <https://labuladong.online/zh/algo/data-structure-basic/queue-stack-basic/>

前置知识

阅读本文前，你需要先学习：

- [链表（链式存储）基础](https://labuladong.online/zh/algo/data-structure-basic/linkedlist-basic/)
- [数组（顺序存储）基础](https://labuladong.online/zh/algo/data-structure-basic/array-basic/)

计算机的两种存储方式，顺序存储（数组）和链式存储（链表）都讲完了，之后的所有数据结构都是基于这两种存储方式之上玩花活。

本文讲解队列和栈的基本原理，后面的文章会讲解如何用代码具体实现。

先说概念吧，其实队列和栈都是「操作受限」的数据结构。说它操作受限，主要是和基本的数组和链表相比，它们提供的 API 是不完整的。

比方说我们前面实现的数组和链表，增删查改的 API 都实现过了，你可以对任意一个索引元素进行增删查改，只要索引不越界，就随便你。

但是对于队列和栈，它们的操作是受限的：**队列只能在一端插入元素，另一端删除元素；栈只能在某一端插入和删除元素**。说白了就是把数组链表提供的 API 删掉了一部分，只保留头尾操作元素的 API 给你用。

形象地理解，队列只允许在队尾插入元素，在队头删除元素，栈只允许在栈顶插入元素，从栈顶删除元素。这个图中把栈竖着画，队列横着画，只是为了更形象，但实际上它们底层都是数组和链表实现的，后面会讲到：

![](https://labuladong.online/images/algo/stack-queue/1.jpg)

队列就像排队买票，先来的先离开，后来的后离开；栈就像一摞盘子，最先放的压在最下面，最后放的留在最上面，拿的时候也是最上面的先被拿走。所以我们常说，队列是一种「先进先出」的数据结构，栈是一种「先进后出」的数据结构，就是这个道理。

这两种数据结构的基本 API 如下：

```java
// 队列的基本 API
class MyQueue<E> {
    // 向队尾插入元素，时间复杂度 O(1)
    void push(E e);

    // 从队头删除元素，时间复杂度 O(1)
    E pop();

    // 查看队头元素，时间复杂度 O(1)
    E peek();

    // 返回队列中的元素个数，时间复杂度 O(1)
    int size();
}

// 栈的基本 API
class MyStack<E> {
    // 向栈顶插入元素，时间复杂度 O(1)
    void push(E e);

    // 从栈顶删除元素，时间复杂度 O(1)
    E pop();

    // 查看栈顶元素，时间复杂度 O(1)
    E peek();

    // 返回栈中的元素个数，时间复杂度 O(1)
    int size();
}
```

不同编程语言中，队列和栈提供的方法名称可能不一样，但每个方法的效果肯定是一样的。

有些语言的标准库可能没有直接提供队列和栈，你可以自己用数组或者链表模拟出队列和栈的效果。下一章我就会先带你用链表实现队列和栈。

[上一篇位图原理及实现](https://labuladong.online/zh/algo/data-structure-basic/bitmap/)[下一篇用链表实现队列/栈](https://labuladong.online/zh/algo/data-structure-basic/linked-queue-stack/)

---

### 10. 用数组实现队列/栈

原文链接: <https://labuladong.online/zh/algo/data-structure-basic/array-queue-stack/>

前置知识

阅读本文前，你需要先学习：

- [队列/栈基本原理](https://labuladong.online/zh/algo/data-structure-basic/queue-stack-basic/)

这篇文章带大家用数组作为底层数据结构实现队列和栈。

## 用数组实现栈

先用数组实现栈，这个不难，你把动态数组的尾部作为栈顶，然后调用动态数组的 API 就行了。因为数组尾部增删元素的时间复杂度都是 O(1)O(1)O(1)，符合栈的要求。

我这里直接用标准库提供的动态数组，如果你想用之前我们实现的 `MyArrayList`，也是一样的：

```java
// 用数组作为底层数据结构实现栈
public class MyArrayStack<E> {
    private ArrayList<E> arr = new ArrayList<>();

    // 向栈顶加入元素，时间复杂度 O(1)
    public void push(E e) {
        arr.add(e);
    }

    // 从栈顶弹出元素，时间复杂度 O(1)
    public E pop() {
        return arr.remove(arr.size() - 1);
    }

    // 查看栈顶元素，时间复杂度 O(1)
    public E peek() {
        return arr.get(arr.size() - 1);
    }

    // 返回栈中的元素个数，时间复杂度 O(1)
    public int size() {
        return arr.size();
    }
}
```

能否让数组的头部作为栈顶？

按照我们之前实现 `MyArrayList` 的逻辑，是不行的。因为数组头部增删元素的时间复杂度都是 O(n)O(n)O(n)，不符合要求。

但是我们可以改用前文 [环形数组技巧](https://labuladong.online/zh/algo/data-structure-basic/cycle-array/) 中实现的 `CycleArray` 类，这个数据结构在头部增删元素的时间复杂度是 O(1)O(1)O(1)，符合栈的要求。

你直接调用 `CycleArray` 的 `addFirst` 和 `removeFirst` 方法实现栈的 API 就行，我这里就不写了。

## 用数组实现队列

有了前文 [环形数组](https://labuladong.online/zh/algo/data-structure-basic/cycle-array/) 中实现的 `CycleArray` 类，用数组作为底层数据结构实现队列就不难了吧。直接复用我们实现的 `CycleArray`，就可以实现标准队列了。当然，一些编程语言也有内置的环形数组实现，你也可以自行搜索使用：

```java
public class MyArrayQueue<E> {
    private CycleArray<E> arr;

    public MyArrayQueue() {
        arr = new CycleArray<>();
    }

    public void push(E t) {
        arr.addLast(t);
    }

    public E pop() {
        return arr.removeFirst();
    }

    public E peek() {
        return arr.getFirst();
    }

    public int size() {
        return arr.size();
    }
}
```

[上一篇用链表实现队列/栈](https://labuladong.online/zh/algo/data-structure-basic/linked-queue-stack/)[下一篇双端队列（Deque）原理及实现](https://labuladong.online/zh/algo/data-structure-basic/deque-implement/)

---

### 11. 用链表实现队列/栈

原文链接: <https://labuladong.online/zh/algo/data-structure-basic/linked-queue-stack/>

前置知识

阅读本文前，你需要先学习：

- [队列/栈基本原理](https://labuladong.online/zh/algo/data-structure-basic/queue-stack-basic/)
- [数组基本原理](https://labuladong.online/zh/algo/data-structure-basic/array-basic/)

## 用链表实现栈

一些读者应该已经知道该怎么用链表作为底层数据结构实现队列和栈了。因为实在是太简单了，直接调用双链表的 API 就可以了。

注意我这里是直接用标准库的链表容器，如果你用之前我们实现的 `MyLinkedList`，也是一样的。

```java
import java.util.LinkedList;

// 用链表作为底层数据结构实现栈
public class MyLinkedStack<E> {
    private final LinkedList<E> list = new LinkedList<>();

    // 向栈顶加入元素，时间复杂度 O(1)
    public void push(E e) {
        list.addLast(e);
    }

    // 从栈顶弹出元素，时间复杂度 O(1)
    public E pop() {
        return list.removeLast();
    }

    // 查看栈顶元素，时间复杂度 O(1)
    public E peek() {
        return list.getLast();
    }

    // 返回栈中的元素个数，时间复杂度 O(1)
    public int size() {
        return list.size();
    }

    public static void main(String[] args) {
        MyLinkedStack<Integer> stack = new MyLinkedStack<>();
        stack.push(1);
        stack.push(2);
        stack.push(3);

        System.out.println(stack.peek()); // 3
        System.out.println(stack.pop()); // 3
        System.out.println(stack.peek()); // 2
    }
}
```

提示

上面这段代码相当于是把双链表的尾部作为栈顶，在双链表尾部增删元素的时间复杂度都是 O(1)，符合要求。

当然，你也可以把双链表的头部作为栈顶，因为双链表头部增删元素的时间复杂度也是 O(1)，所以这样实现也是一样的。只要做几个修改 `addLast -> addFirst`，`removeLast -> removeFirst`，`getLast -> getFirst` 就行了。

## 用链表实现队列

同理，用链表实现队列也是一样的，也直接调用双链表的 API 就可以了：

```java
import java.util.LinkedList;

// 用链表作为底层数据结构实现队列
public class MyLinkedQueue<E> {
    private final LinkedList<E> list = new LinkedList<>();

    // 向队尾插入元素，时间复杂度 O(1)
    public void push(E e) {
        list.addLast(e);
    }

    // 从队头删除元素，时间复杂度 O(1)
    public E pop() {
        return list.removeFirst();
    }

    // 查看队头元素，时间复杂度 O(1)
    public E peek() {
        return list.getFirst();
    }

    // 返回队列中的元素个数，时间复杂度 O(1)
    public int size() {
        return list.size();
    }

    public static void main(String[] args) {
        MyLinkedQueue<Integer> queue = new MyLinkedQueue<>();
        queue.push(1);
        queue.push(2);
        queue.push(3);

        System.out.println(queue.peek()); // 1
        System.out.println(queue.pop()); // 1
        System.out.println(queue.pop()); // 2
        System.out.println(queue.peek()); // 3
    }
}
```

提示

上面这段代码相当于是把双链表的尾部作为队尾，把双链表的头部作为队头，在双链表的头尾增删元素的复杂度都是 O(1)，符合队列 API 的要求。

当然，你也可以反过来，把双链表的头部作为队尾，双链表的尾部作为队头。类似栈的实现，只要改一改 list 的调用方法就行了。

[上一篇队列/栈基本原理](https://labuladong.online/zh/algo/data-structure-basic/queue-stack-basic/)[下一篇用数组实现队列/栈](https://labuladong.online/zh/algo/data-structure-basic/array-queue-stack/)

---

## 7. 哈希表的原理及实现

### 12. 用数组加强哈希表（ArrayHashMap）

原文链接: <https://labuladong.online/zh/algo/data-structure-basic/hashtable-with-array/>

前置知识

阅读本文前，你需要先学习：

- [哈希表核心原理](https://labuladong.online/zh/algo/data-structure-basic/hashmap-basic/)

上一章 [用链表加强哈希表](https://labuladong.online/zh/algo/data-structure-basic/hashtable-with-linked-list/) 我们利用 [双链表](https://labuladong.online/zh/algo/data-structure-basic/linkedlist-basic/) 对哈希表进行了加强，实现了 `LinkedHashMap` 这种数据结构，让哈希表的键保持插入顺序。

链表能加强哈希表，数组作为链表的好兄弟，其实也能加强哈希表。

## 添加 randomKey() API

现在我给你出个题，让你基于标准哈希表的 API 之上，再添加一个新的 `randomKey()` API，可以在 O(1)O(1)O(1) 的时间复杂度返回一个随机键：

```text
interface Map<K, V> {
    // 获取 key 对应的 value，时间复杂度 O(1)
    V get(K key);

    // 添加/修改 key-value 对，时间复杂度 O(1)
    void put(K key, V value);

    // 删除 key-value 对，时间复杂度 O(1)
    void remove(K key);

    // 是否包含 key，时间复杂度 O(1)
    boolean containsKey(K key);

    // 返回所有 key，时间复杂度 O(N)
    List<K> keys();

    // 新增 API：随机返回一个 key，要求时间复杂度 O(1)
    K randomKey();
}
```

均匀随机（uniform random）

注意，我们一般说的随机，都是指均匀随机，即每个元素被选中的概率相等。比如你有 `n` 个元素，你的随机算法要保证每个元素被选中的概率都是 `1/n`，才叫均匀随机。

怎么样，你会不会做？不要小看这个简单的需求，实现方法其实是比较巧妙的。

通过前面的学习，你应该知道哈希表的本质就是一个 `table` 数组，现在让你随机返回一个哈希表的键，很容易就会联想到在数组中随机获取一个元素。

在标准数组，随机获取一个元素很简单，只要用随机数生成器生成一个 `[0, size)` 的随机索引，就相当于找了一个随机元素：

```java
int randomeElement(int[] arr) {
    Random r = new Random();
    // 生成 [0, arr.length) 的随机索引
    return arr[r.nextInt(arr.length)];
}
```

这个算法是正确的，它的复杂度是 O(1)，且每个元素被选中的概率都是 `1/n`，`n` 为 `arr` 数组的总元素个数。

但你注意，上面这个函数有个前提，就是数组中的元素是紧凑存储没有空洞的，比如 `arr = [1, 2, 3, 4]`，这样才能保证任意一个随机索引都对应一个有效的元素。

如果数组中有空洞就有问题了，比如 `arr = [1, 2, null, 4]`，其中 `arr[2] = null` 代表没有存储元素的空洞，那么如果你生成的随机数恰好是 2，请问你该怎么办？

也许你想说，可以向左或者向右线性查找，找到一个非空的元素返回，类似这样：

```text
// 返回一个非空的随机元素（伪码）
int randomeElement(int[] arr) {
    Random r = new Random();
    // 生成 [0, arr.length) 的随机索引
    int i = r.nextInt(arr.length);
    while (arr[i] == null) {
        // 随机生成的索引 i 恰巧是空洞
        // 借助环形数组技巧向右进行探查
        // 直到找到一个非空元素
        i = (i + 1) % arr.length;
    }
    return arr[i];
}
```

你这样是不行的，这个算法有两个问题：

1、有个循环，最坏时间复杂度上升到了 O(N)O(N)O(N)，不符合 O(1)O(1)O(1) 的要求。

2、这个算法不是均匀随机的，因为你的查找方向是固定的，空洞右侧的元素被选中的概率会更大。比如 `arr = [1, 2, null, 4]`，元素 `1, 2, 4` 被选中的概率分别是 `1/4, 1/4, 2/4`。

那也许还有个办法，一次运气不好，就多来随机几次，直到找到一个非空元素：

```text
// 返回一个非空的随机元素（伪码）
int randomeElement(int[] arr) {
    Random r = new Random();
    // 生成 [0, arr.length) 的随机索引
    int i = r.nextInt(arr.length);
    while (arr[i] == null) {
        // 随机生成的索引 i 恰巧是空洞
        // 重新生成一个随机索引
        i = r.nextInt(arr.length);
    }
    return arr[i];
}
```

现在这个算法是均匀随机的，但问题也非常明显，它的时间复杂度竟然依赖随机数！肯定不是 O(1)O(1)O(1) 的，不符合要求。

怎么样，从一个带有空洞的数组中随机返回一个元素是不是都把你难住了？

别忘了，我们现在的目标是从哈希表中随机返回一个键，**哈希表底层的 `table` 数组不仅包含空洞，情况还会更复杂一些**：

![](https://labuladong.online/images/algo/ds-basic/hash-collision-with-key.jpeg)

如果你的哈希表用开放寻址法解决哈希冲突，那还好，就是带空洞数组的场景。

如果你的哈希表用拉链法，那可麻烦了。数组里面的每个元素是一个链表，你光随机一个索引是不够的，还要随机链表中的一个节点。

而且注意概率，这个拉链法，就算你均匀随机到一个数组索引，又均匀随机该索引存储的链表节点，得到的这个键是均匀随机的么？

其实不是，上图中 `k1, k2, k3` 被随机到的概率是 `1/2 * 1/3 = 1/6`，而 `k4, k5` 被随机到的概率是 `1/2 * 1/2 = 1/4`，这不是均匀随机。

关于概率算法

概率算法也是非常有意思的一类问题，无论算法题还是实际业务中都会用到一些经典的随机算法，我会在后文 [谈谈游戏中的随机算法](https://labuladong.online/zh/algo/frequency-interview/random-algorithm/) 和 [带权重的随机选择](https://labuladong.online/zh/algo/frequency-interview/random-pick-with-weight/) 中详细讲解，这里暂时不需要掌握。

唯一的办法就是通过 `keys` 方法遍历整个 `table` 数组，把所有的键都存储到一个数组中，然后再随机返回一个键。但这样复杂度就是 O(N)O(N)O(N) 了，还是不符合要求。

是不是感觉已经走投无路了？所以说，还是要积累一些经典数据结构设计经验，如果面试笔试的时候遇到类似的问题，你现场想恐怕是很难的。下面我就来介绍一下如何用数组加强哈希表，轻松实现 `randomKey()` API。

[上一篇用链表加强哈希表（LinkedHashMap）](https://labuladong.online/zh/algo/data-structure-basic/hashtable-with-linked-list/)[下一篇布隆过滤器原理及实现](https://labuladong.online/zh/algo/data-structure-basic/bloom-filter/)

---

### 13. 用链表加强哈希表（LinkedHashMap）

原文链接: <https://labuladong.online/zh/algo/data-structure-basic/hashtable-with-linked-list/>

前置知识

阅读本文前，你需要先学习：

- [哈希表核心原理](https://labuladong.online/zh/algo/data-structure-basic/hashmap-basic/)

前文 [哈希表原理](https://labuladong.online/zh/algo/data-structure-basic/hashmap-basic/) 从原理上分析了，不能依赖哈希表遍历 `key` 的顺序，即哈希表中的 `key` 是无序的。

但结合实际的编程经验，你可能会有些疑问。

比如熟悉 Java 的读者可能知道，Java 标准库提供的 `LinkedHashMap` 就可以**按照键的插入顺序来遍历**。例如下面这段简单的代码：

```text
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

无论你插入多少键，`keySet` 方法返回的所有键都是按照插入顺序排列，感觉就好像在向数组尾部追加元素一样。这怎么可能呢？

如果你熟悉 Golang，你会发现一个更神奇的现象。比如下面这段测试代码：

```text
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

也就是说，它每次遍历的顺序都是随机。但是按照前文 [哈希表原理](https://labuladong.online/zh/algo/data-structure-basic/hashmap-basic/) 所说，虽然哈希表的键是无序的，但是没有对哈希表做任何操作，遍历得到的结果应该不会变才对，Golang 的 map 每次遍历的顺序咋都不一样？这也太离谱了吧？

你可以先自己思考下原因，下面我给出答案。

点击查看答案

**先说 Golang 吧，每次遍历都乱序的原因就是，它故意的**。

这个原因属实是让人有些哭笑不得，Golang 为了防止开发者依赖哈希表的遍历顺序，所以每次遍历都故意返回不同的顺序，可谓用心良苦。也可以从侧面看出，确实不少开发者没了解过哈希表的基本原理。

我们不妨进一步想想，它是怎么打乱顺序的呢？真是随机打乱吗？

其实不是，你仔细看看，它这个乱序是有规律的。有没有想起前面讲过的 [环形数组](https://labuladong.online/zh/algo/data-structure-basic/cycle-array/)？

```text
| 1 2 3 4 5
5 | 1 2 3 4
2 3 4 5 | 1
| 1 2 3 4 5
```

看出来没有？如果不触发扩缩容的话，实际上它的遍历顺序应该也是固定的，只不过它不是每次都从底层 `table` 数组的头部开始，而是从一个随机的位置开始，然后利用环形数组技巧遍历整个 `table` 数组，这样就能保证多次遍历的结果具有随机性，同时又不至于为了随机性而牺牲太多性能。

再说 Java 的 `LinkedHashMap`，**它能让所有键按照插入顺序排列，是因为它把标准的哈希表和链表结合起来，组成了一种新的数据结构：哈希链表**。

这种数据结构兼具了哈希表 O(1)O(1)O(1) 的增删查改效率，同时又可以像数组链表一样保持键的插入顺序。

它是怎么做的呢？下面我会具体讲解。

[上一篇哈希集合的原理及代码实现](https://labuladong.online/zh/algo/data-structure-basic/hash-set/)[下一篇用数组加强哈希表（ArrayHashMap）](https://labuladong.online/zh/algo/data-structure-basic/hashtable-with-array/)

---

### 14. 用拉链法实现哈希表

原文链接: <https://labuladong.online/zh/algo/data-structure-basic/hashtable-chaining/>

前置知识

阅读本文前，你需要先学习：

- [哈希表核心原理](https://labuladong.online/zh/algo/data-structure-basic/hashmap-basic/)
- [链表（链式存储）基础](https://labuladong.online/zh/algo/data-structure-basic/linkedlist-basic/)

前文 [哈希表核心原理](https://labuladong.online/zh/algo/data-structure-basic/hashmap-basic/) 中我介绍了哈希表的核心原理和几个关键概念，其中提到了解决哈希冲突的方法主要有两种，分别是拉链法和开放寻址法（也常叫做线性探查法）：

![](https://labuladong.online/images/algo/ds-basic/hash-collision.jpeg)

本文就来具体介绍一下拉链法的实现原理和代码。

**首先，我会结合 [可视化面板](https://labuladong.online/zh/algo/intro/visualize/) 用拉链法实现一个简化版的哈希表，带大家直观地理解拉链法是如何实现增删查改的 API 并解决哈希冲突的，最后再给出一个比较完善的 Java 代码实现**。

## 拉链法的简化版实现

[哈希表核心原理](https://labuladong.online/zh/algo/data-structure-basic/hashmap-basic/) 已经介绍过哈希函数和 `key` 的类型的关系，其中 `hash` 函数的作用是在 O(1)O(1)O(1) 的时间把 `key` 转化成数组的索引，而 `key` 可以是任意不可变的类型。

但是这里为了方便诸位理解，我先做如下简化：

1、我们实现的哈希表只支持 `key` 类型为 `int`，`value` 类型为 `int` 的情况，如果 `key` 不存在，就返回 `-1`。

2、我们实现的 `hash` 函数就是简单地取模，即 `hash(key) = key % table.length`。这样也方便模拟出哈希冲突的情况，比如当 `table.length = 10` 时，`hash(1)` 和 `hash(11)` 的值都是 1。

3、底层的 `table` 数组的大小在创建哈希表时就固定，不考虑负载因子和动态扩缩容的问题。

这些简化能够帮助我们聚焦增删查改的核心逻辑，并且可以借助 [可视化面板](https://labuladong.online/zh/algo/intro/visualize/) 辅助大家学习理解。

[上一篇哈希表核心原理](https://labuladong.online/zh/algo/data-structure-basic/hashmap-basic/)[下一篇线性探查法的两个难点](https://labuladong.online/zh/algo/data-structure-basic/linear-probing-key-point/)

---

### 15. 线性探查法的两个难点

原文链接: <https://labuladong.online/zh/algo/data-structure-basic/linear-probing-key-point/>

前置知识

阅读本文前，你需要先学习：

- [哈希表核心原理](https://labuladong.online/zh/algo/data-structure-basic/hashmap-basic/)

前文 [哈希表核心原理](https://labuladong.online/zh/algo/data-structure-basic/hashmap-basic/) 中我介绍了哈希表的核心原理和几个关键概念，其中提到了解决哈希冲突的方法主要有两种，分别是拉链法和线性探查法（也常叫做开放寻址法）：

![](https://labuladong.online/images/algo/ds-basic/hash-collision.jpeg)

由于线性探查法稍微复杂一些，本文先讲解实现线性探查法的几个难点，下篇文章再给出具体的代码实现。

## 简化场景

之前介绍的拉链法应该是比较简单的，无非就是 `table` 中每个元素都是一个链表，出现哈希冲突的话往链表里塞元素就行了。

而线性探查法会更复杂，主要有两个难点，涉及到多种数组操作技巧。在讲清楚这两个难点之前，我们先设定一个简化的场景：

假设我们的哈希表只支持 `key` 类型为 `int`，`value` 类型为 `int` 的情况，且 `table.length` 固定为 `10`，`hash` 函数的实现是 `hash(key) = key % 10`。因为这样比较容易模拟出哈希冲突，比如 `hash(1)` 和 `hash(11)` 的值都是 1。

线性探查法的大致逻辑如下：

```java
// 线性探查法的基本逻辑，伪码实现

class MyLinearProbingHashMap {
    // 数组中每个元素都存储一个键值对
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
            // 线性探查法的逻辑
            // 向后探查，直到找到 key 或者找到空位
            while (index < table.length && table[index] != null && table[index].key != key) {
                index++;
            }
            table[index] = new KVNode(key, value);
        }
    }

    public int get(int key) {
        int index = hash(key);
        // 向后探查，直到找到 key 或者找到空位
        while (index < table.length && table[index] != null && table[index].key != key) {
            index++;
        }
        if (table[index] == null) {
            return -1;
        }
        return table[index].value;
    }

    public void remove(int key) {
        int index = hash(key);
        // 向后探查，直到找到 key 或者找到空位
        while (index < table.length && table[index] != null && table[index].key != key) {
            index++;
        }
        // 删除 table[index]
        // ...
    }
}
```

基于这个假设场景，我们来看看线性探查法的两个难点。

[上一篇用拉链法实现哈希表](https://labuladong.online/zh/algo/data-structure-basic/hashtable-chaining/)[下一篇线性探查法的两种代码实现](https://labuladong.online/zh/algo/data-structure-basic/linear-probing-code/)

---

### 16. 线性探查法的两种代码实现

原文链接: <https://labuladong.online/zh/algo/data-structure-basic/linear-probing-code/>

前置知识

阅读本文前，你需要先学习：

- [线性探查法的两个难点](https://labuladong.online/zh/algo/data-structure-basic/linear-probing-key-point/)

前文 [哈希表核心原理](https://labuladong.online/zh/algo/data-structure-basic/hashmap-basic/) 中我介绍了哈希表的核心原理和几个关键概念，[拉链法原理和实现](https://labuladong.online/zh/algo/data-structure-basic/hashtable-chaining/) 中介绍了拉链法的实现，[线性探查法的两个难点](https://labuladong.online/zh/algo/data-structure-basic/linear-probing-key-point/) 介绍了线性探查法实现哈希表的难点所在，并给出了两种方法解决删除元素时的空洞问题，本文会同时给出这两种方法的参考代码实现。

本文会先结合可视化面板给出简化的实现，方便大家理解增删查改的过程，最后给完整实现。

简化实现中，具体简化的地方如下：

1、我们实现的哈希表只支持 `key` 类型为 `int`，`value` 类型为 `int` 的情况，如果 `key` 不存在，就返回 `-1`。

2、我们实现的 `hash` 函数就是简单地取模，即 `hash(key) = key % table.length`。这样也方便模拟出哈希冲突的情况，比如当 `table.length = 10` 时，`hash(1)` 和 `hash(11)` 的值都是 1。

3、底层的 `table` 数组的大小在创建哈希表时就固定，假设 `table` 数组不会被装满，不考虑负载因子和动态扩缩容的问题。

这些简化能够帮助我们聚焦增删查改的核心逻辑，并且可以借助 [可视化面板](https://labuladong.online/zh/algo/intro/visualize/) 辅助大家学习理解。

[上一篇线性探查法的两个难点](https://labuladong.online/zh/algo/data-structure-basic/linear-probing-key-point/)[下一篇哈希集合的原理及代码实现](https://labuladong.online/zh/algo/data-structure-basic/hash-set/)

---

### 17. 哈希表核心原理

原文链接: <https://labuladong.online/zh/algo/data-structure-basic/hashmap-basic/>

前置知识

阅读本文前，你需要先学习：

- [数组（顺序存储）基础](https://labuladong.online/zh/algo/data-structure-basic/array-basic/)

首先，我需要先阐明一个初学者很容易犯的概念错误。

请问，哈希表和我们常说的 Map（键值映射）是不是同一个东西？不是。

这一点用 Java 来讲解就很清楚，`Map` 是一个 Java 接口，仅仅声明了若干个方法，并没有给出方法的具体实现：

```text
interface Map<K, V> {
    V get(K key);
    void put(K key, V value);
    V remove(K key);
    // ...
}
```

Map 接口本身只定义了键值映射的一系列操作，HashMap 这种数据结构根据自身特点实现了这些操作。还有其他数据结构也实现了这个接口，比如 `TreeMap`、`LinkedHashMap` 等等。

换句话说，你可以说 `HashMap` 的 `get, put, remove` 方法的复杂度都是 O(1)O(1)O(1) 的，但你不能说 `Map` 接口的复杂度都是 O(1)O(1)O(1)。因为如果换成其他的实现类，比如底层用二叉树结构实现的 `TreeMap`，这些方法的复杂度就变成 O(logN)O(logN)O(logN) 了。

我为什么要强调这一点呢？主要是针对使用非 Java 语言的读者。

其他编程语言可能没有 Java 这么清晰的接口定义，所以很容易让读者把哈希表和 Map 键值对混为一谈，听到键值对操作，就认为其增删查改的复杂度一定是 O(1)O(1)O(1)。这是不对的，具体要看这个底层的数据结构是如何实现键值操作的。

那么这一章节我会带大家动手实现一个哈希表，探讨哈希表为什么能做到增删查改 O(1)O(1)O(1) 复杂度，以及解决哈希冲突的两种办法。

## 哈希表的基本原理

哈希表可以理解为一个加强版的数组。

数组可以通过索引在 O(1)O(1)O(1) 的时间复杂度内查找到对应元素，索引是一个非负整数。

哈希表是类似的，可以通过 `key` 在 O(1)O(1)O(1) 的时间复杂度内查找到这个 `key` 对应的 `value`。`key` 的类型可以是数字、字符串等多种类型。

怎么做的？特别简单，哈希表的底层实现就是一个数组（我们不妨称之为 `table`）。它先把这个 `key` 通过一个哈希函数（我们不妨称之为 `hash`）转化成数组里面的索引，然后增删查改操作和数组基本相同：

```java
// 哈希表伪码逻辑
class MyHashMap {

    private Object[] table;

    // 增/改，复杂度 O(1)
    public void put(K key, V value) {
        int index = hash(key);
        table[index] = value;
    }

    // 查，复杂度 O(1)
    public V get(K key) {
        int index = hash(key);
        return table[index];
    }

    // 删，复杂度 O(1)
    public void remove(K key) {
        int index = hash(key);
        table[index] = null;
    }

    // 哈希函数，把 key 转化成 table 中的合法索引
    // 时间复杂度必须是 O(1)，才能保证上述方法的复杂度都是 O(1)
    private int hash(K key) {
        // ...
    }
}
```

具体实现上有不少细节需要处理，比如哈希函数的设计、哈希冲突的处理等等。但你只要明白了上面的核心原理，就已经成功了一半了，剩下的就是写代码了，这有何难呢？

下面我们来具体介绍一下上述增删查改过程中几个关键的概念和可能出现的问题。

## 几个关键概念及原理

### key 是唯一的，value 可以重复

哈希表中，不可能出现两个相同的 `key`，而 `value` 是可以重复的。

明白了上面讲的原理应该很好理解，你直接类比数组就行了：

**数组里面每个索引都是唯一的，不可能说你这个数组有两个索引 0。至于数组里面存什么元素，随便你，没人 care**。

所以哈希表是一样的，`key` 的值不可能出现重复，而 `value` 的值可以随意。

### 哈希函数

哈希函数的作用是把任意长度的输入（key）转化成固定长度的输出（索引）。

你也看到了，增删查改的方法中都会用到哈希函数来计算索引，如果你设计的这个哈希函数复杂度是 O(N)O(N)O(N)，那么哈希表的增删查改性能就会退化成 O(N)O(N)O(N)，**所以说这个函数的性能很关键**。

**这个函数还要保证的一点是，输入相同的 `key`，输出也必须要相同，这样才能保证哈希表的正确性**。不能说现在你计算 `hash("123") = 5`，待会儿计算 `hash("123") = 6`，这样的话哈希表就废了。

那么哈希函数是如何把非整数类型的 `key` 转化成整数索引的？又是如何保证这个索引是合法的呢？

如何把 `key` 转化成整数

这个问题可以有很多种答案，不同的哈希函数设计会有不同的方法，我这里就结合 Java 语言说一个简单的办法。其他编程语言也是类似的，可以参考这个思路，查询相关的标准库文档。

任意 Java 对象都会有一个 `int hashCode()` 方法，在实现自定义的类时，如果不重写这个方法，那么它的默认返回值可以认为是该对象的内存地址。一个对象的内存地址显然是全局唯一的一个整数。

所以我们只要调用 `key` 的 `hashCode()` 方法就相当于把 `key` 转化成了一个整数，且这个整数是全局唯一的。

当然，这个方法也有一些问题，下面会讲解，但现在至少找到了一种把任意对象转化为整数的方法。

如何保证索引合法

`hashCode` 方法返回的是 int 类型，首先一个问题就是，这个 int 值可能是负数，而数组的索引是非负整数。

那么你肯定想这样写代码，把这个值转化成非负数：

```text
int h = key.hashCode();
if (h < 0) h = -h;
```

但这样有问题，int 类型可以表示的最小值是 `-2^31`，而最大值是 `2^31 - 1`。所以如果 `h = -2^31`，那么 `-h = 2^31` 就会超出 int 类型的最大值，这叫做整型溢出，编译器会报错，甚至产生不可预知的结果。

为什么 int 的最小值是 `-2^31`，而最大值是 `2^31 - 1`？这涉及计算机补码编码的原理，简单说，int 就是 32 个二进制位，其中最高位（最左边那位）是符号位，符号位是 0 时表示正数，是 1 时表示负数。

现在的问题是，我想保证 `h` 非负，但又不能用负号直接取反。那么一个简单直接的办法是利用这种补码编码的原理，直接把最高位的符号位变成 0，就可以保证 `h` 是非负数了：

```text
int h = key.hashCode();
// 位运算，把最高位的符号位去掉
// 另外，位运算的运行速度也会比一般的算术运算快
// 所以你看标准库的源码，能用位运算的地方它都会优先使用位运算
h = h & 0x7fffffff;
// 这个 0x7fffffff 的二进制表示是 0111 1111 ... 1111
// 即除了最高位（符号位）是 0，其他位都是 1
// 把 0x7fffffff 和其他 int 进行 & 运算之后，最高位（符号位）就会被清零，即保证了 h 是非负数
```

关于补码编码的原理我这里就不详细展开了，有兴趣的话你可以自己搜索学习一下。

好的，上面解决了 `hashCode` 可能是负数的问题，但还有一个问题，就是这个 `hashCode` 一般都很大，我们需要把它映射成 `table` 数组的合法索引。

这个问题对你来说应该不难吧，我们之前在 [环形数组原理及实现](https://labuladong.online/zh/algo/data-structure-basic/cycle-array/) 里面用 `%` 求模运算来保证索引永远落在数组的合法范围内。所以这里也可以用 `%` 运算来保证索引的合法性，完整的 `hash` 函数实现如下：

```text
int hash(K key) {
    int h = key.hashCode();
    // 保证非负数
    h = h & 0x7fffffff;
    // 映射到 table 数组的合法索引
    return h % table.length;
}
```

当然，直接使用 `%` 也有问题，因为 `%` 这个求余数的运算比较消耗性能，一般在追求运行效率的标准库源码中会尽量避免使用 `%` 运算，而是使用位运算提升性能。

不过本章主要目的是带你理解实现一个简单的哈希表，就忽略这些细节优化了。有兴趣的话你可以去看一下 Java HashMap 的源码，看看它是如何实现这个 `hash` 函数的。

### 哈希冲突

上面给出了 `hash` 函数的实现，那么你肯定也会想到，如果两个不同的 `key` 通过哈希函数得到了相同的索引，怎么办呢？这种情况就叫做「哈希冲突」。

哈希冲突是否可以避免？

哈希冲突不可能避免，只能在算法层面妥善处理出现哈希冲突的情况。

哈希冲突是一定会出现的，因为这个 `hash` 函数相当于是把一个无穷大的空间映射到了一个有限的索引空间，所以必然会有不同的 `key` 映射到同一个索引上。

就好比三维物体映射到二维影子一样，这种有损压缩必然会出现信息丢失，有损信息本就无法和原信息一一对应。

出现哈希冲突的情况怎么解决？两种常见的解决方法，一种是**拉链法**，另一种是**线性探查法**（也经常被叫做**开放寻址法**）。

名字听起来高大上，说白了就是纵向延伸和横向延伸两种思路嘛：

![](https://labuladong.online/images/algo/ds-basic/hash-collision.jpeg)

拉链法相当于是哈希表的底层数组并不直接存储 `value` 类型，而是存储一个链表，当有多个不同的 `key` 映射到了同一个索引上，这些 `key -> value` 对儿就存储在这个链表中，这样就能解决哈希冲突的问题。

而线性探查法的思路是，一个 `key` 发现算出来的 `index` 值已经被别的 `key` 占了，那么它就去 `index + 1` 的位置看看，如果还是被占了，就继续往后找，直到找到一个空的位置为止。

比方说上图，key 的插入顺序是 `k2, k4, k5, k3, k1`，那么哈希表底层就会变成这样：

![](https://labuladong.online/images/algo/ds-basic/hash-collision-with-key.jpeg)

这里先讲一下原理，后面的章节我会手把手带大家分别实现这两种方法来解决哈希冲突。

### 扩容和负载因子

相信大家都听说过「负载因子」这个专业术语，现在你明白了哈希冲突的问题，就能理解负载因子的意义了。

拉链法和线性探查法虽然能解决哈希冲突的问题，但是它们会导致性能下降。

比如拉链法，你算出来 `index = hash(key)` 这个索引了，结果过去查出来的是个链表，你还得遍历一下这个链表，才能在里面找到你要的 `value`。这个过程的时间复杂度是 O(K)O(K)O(K)，`K` 是这个链表的长度。

线性探查法也是类似的，你算出来 `index = hash(key)` 这个索引了，你去这个索引位置查看，发现存储的不是要找的 `key`，但由于线性探查法解决哈希冲突的方式，你并不能确定这个 `key` 真的不存在，你必须顺着这个索引往后找，直到找到一个空的位置或者找到这个 `key` 为止，这个过程的时间复杂度也是 O(K)O(K)O(K)，`K` 为连续探查的次数。

所以说，如果频繁出现哈希冲突，那么 `K` 的值就会增大，这个哈希表的性能就会显著下降。这是我们需要避免的。

那么为什么会频繁出现哈希冲突呢？两个原因呗：

1、哈希函数设计的不好，导致 `key` 的哈希值分布不均匀，很多 `key` 映射到了同一个索引上。

2、哈希表里面已经装了太多的 `key-value` 对了，这种情况下即使哈希函数再完美，也没办法避免哈希冲突。

对于第一个问题没什么好说的，开发编程语言标准库的大佬们已经帮你设计好了哈希函数，你只要调用就行了。

对于第二个问题是我们可以控制的，即避免哈希表装太满，这就引出了「负载因子」的概念。

负载因子

负载因子是一个哈希表装满的程度的度量。一般来说，负载因子越大，说明哈希表里面存储的 `key-value` 对越多，哈希冲突的概率就越大，哈希表的操作性能就越差。

**负载因子的计算公式也很简单，就是 `size / table.length`**。其中 `size` 是哈希表里面的 `key-value` 对的数量，`table.length` 是哈希表底层数组的容量。

你不难发现，用拉链法实现的哈希表，负载因子可以无限大，因为链表可以无限延伸；用线性探查法实现的哈希表，负载因子不会超过 1。

像 Java 的 HashMap，允许我们创建哈希表时自定义负载因子，不设置的话默认是 `0.75`，这个值是经验值，一般保持默认就行了。

**当哈希表内元素达到负载因子时，哈希表会扩容**。和之前讲解 [动态数组的实现](https://labuladong.online/zh/algo/data-structure-basic/array-implement/) 是类似的，就是把哈希表底层 `table` 数组的容量扩大，把数据搬移到新的大数组中。`size` 不变，`table.length` 增加，负载因子就减小了。

### 为什么不能依赖哈希表的遍历顺序

你大概也听过一个编程常识，即哈希表中键的遍历顺序是无序的，不能依赖哈希表的遍历顺序来编写程序。这是为什么呢？

哈希表的遍历本质上就是遍历那个底层 `table` 数组：

```text
// 遍历所有 key 的伪码逻辑

// 哈希表底层的 table 数组
KVNode[] table = new KVNode[1000];

// 获取哈希表中的所有键
// 我们不能依赖这个 keys 列表的顺序
List<KeyType> keys = new ArrayList<>();

for (int i = 0; i < table.length; i++) {
    KVNode node = table[i];
    if (node != null) {
        keys.add(node.key);
    }
}
```

你如果理解了前面讲的内容，应该已经能够理解这个问题了。

首先，由于 `hash` 函数要把你的 `key` 进行映射，所以 `key` 在底层 `table` 数组中的分布是随机的，不像数组/链表结构那样有个明确的元素顺序。

其次，刚才讲了哈希表达到负载因子时会怎样？会扩容对吧，也就是 `table.length` 会变化，且会搬移元素。

那么这个搬移数据的过程，是不是要用 `hash` 函数重新计算 `key` 的哈希值，然后放到新的 `table` 数组中？

**而这个 `hash` 函数，它计算出的索引值依赖 `table.length`。也就是说，哈希表自动扩缩容后，同一个 `key` 存储在 `table` 的索引可能发生变化，所以遍历结果的顺序就和之前不一样了**。

你观察到的现象就是，这次遍历的第一个键是 `key1`，但是增删几个元素再遍历，可能发现 `key1` 跑到最后去了。

所以说，这些东西没必要背的，原理搞明白了，你稍微推理下自己都能想通。

### 为什么不建议在 for 循环中增/删哈希表的 key

注意我这里说的是不建议，并不是一定不可以。因为不同的编程语言标准库对哈希表的实现不同，有些语言针对这种情况做了优化，所以到底行不行，要查阅文档。

我们这里仅从哈希表的原理上分析，在 for 循环中增/删哈希表的 `key`，是很容易出现问题的，原因和上面相同，还是扩缩容导致的哈希值变化。

遍历哈希表的 `key`，本质就是遍历哈希表底层的 `table` 数组，如果一边遍历一边增删元素，如果遍历到一半，插入/删除操作触发了扩缩容，整个 `table` 数组都变了，那么请问，接下来应该是什么行为？还有，在遍历过程中新插入/删除的元素，是否应该被遍历到？

扩缩容导致 `key` 顺序变化是哈希表的特有行为，但即便排除这个因素，任何其他数据结构，也都不建议在遍历的过程中同时进行增删，否则很容易导致非预期的行为。

如果你非要这样做，请确保查阅了相关文档，明确这个操作的行为是什么，做到心里有数。

### key 必须是不可变的

**只有那些不可变类型，才能作为哈希表的 `key`，这一点很重要**。

所谓不可变类型，就是说这个对象一旦创建，它的值就不能再改变了。比如 Java 中的 `String, Integer` 等类型，一旦创建了这些对象，你就只能读取它的值，而不能再修改它的值了。

作为对比，Java 中的 `ArrayList`、`LinkedList` 这些对象，它们创建出来之后，可以往里面随意增删元素，所以它们是可变类型。

因此，你可以把 `String` 对象作为哈希表的 `key`，但不能把 `ArrayList` 对象作为哈希表的 `key`：

```text
// 可以把不可变类型作为 key
Map<String, AnyOtherType> map1 = new HashMap<>();
Map<Integer, AnyOtherType> map2 = new HashMap<>();

// 不应该把可变类型作为 key
// 注意，这样写并不会产生语法错误，但是代码非常容易出 bug
Map<ArrayList<Integer>, AnyOtherType> map3 = new HashMap<>();
```

为啥不建议把可变类型作为 `key` 呢？就比如这个 `ArrayList` 吧，它的 `hashCode` 方法的实现逻辑如下：

```text
public int hashCode() {
    int h = 0;
    for (int i = 0; i < elementData.length; i++) {
        h = 31 * h + elementData[i];
    }
}
```

**第一个就是效率问题**，每次计算 `hashCode` 都要遍历整个数组，复杂度是 O(N)O(N)O(N)，这样就会导致哈希表的增删查改操作的复杂度退化成 O(N)O(N)O(N)。

更严重的问题是，`ArrayList` 的 `hashCode` 是根据它里面的元素计算出来的，如果你往这个 `ArrayList` 里面增删元素，或者其中某个元素的 `hashCode` 值发生改变，那么这个 `ArrayList` 的 `hashCode` 返回值也会发生改变。

比方说，你现在用一个 `ArrayList` 类型的 `arr` 变量作为哈希表的 `key` 在哈希表中保存了对应的 `value`。但如果 `arr` 中的某个元素在程序的其他位置被修改了，那么 `arr` 的 `hashCode` 就会变化。此时你再用这个 `arr` 变量去哈希表中查询，发现找不到任何值了。

**也就是说，你存入哈希表的 `key-value` 意外丢失了，这是非常非常严重的 bug，还会带来潜在的内存泄漏问题**。

```text
public class Test {
    public static void main(String[] args) {
        // 错误示例
        // 把可变类型作为 HashMap 的 key
        Map<ArrayList<Integer>, Integer> map = new HashMap<>();

        ArrayList<Integer> arr = new ArrayList<>();
        arr.add(1);
        arr.add(2);

        map.put(arr, 999);
        System.out.println(map.containsKey(arr)); // true
        System.out.println(map.get(arr)); // 999

        arr.add(3);
        // 出现严重 bug，键值对丢失
        System.out.println(map.containsKey(arr)); // false
        System.out.println(map.get(arr)); // null

        // 此时 map 底层的 table 中，arr 的键值对数据依然存在
        // 但是由于 arr 的 hashCode 改变了，此键值对无法被查找到
        // 这也会导致内存泄漏，因为这个 arr 变量被 map 引用着，无法被垃圾回收
    }
}
```

上面就是一个简单的错误示例。你也许会说，把元素 `3` 删掉，`arr -> 999` 这个键值对不就又出现了？或者，直接遍历哈希表底层的 `table` 数组，应该也可以看到这个键值对。

拜托🙏🏻，你这是在写代码还是在写盗墓笔记呢？一会儿出现一会儿消失，你这个哈希表是幽灵附体了吗？

开个玩笑。实际上可变类型本身就是一种不确定性，在代码构成的屎山里，你怎么知道这个 `arr` 传递到哪里被修改了呢？

所以正确的做法是，使用不可变类型作为哈希表的 `key`，比方说用 `String` 类型作为 `key`。因为 Java 中的 `String` 对象一旦创建出来，它的值就不允许被改变，你就不会遇到上面的问题。

`String` 类型的 `hashCode` 方法也需要遍历所有字符，但是由于它的不可变性，这个值只要算出来一次，就可以缓存下来，不用每次都重新计算，所以 [平均时间复杂度](https://labuladong.online/zh/algo/essential-technique/complexity-analysis/) 依然是 O(1)O(1)O(1)。

我这里是用 Java 举的例子，其他语言也是类似的，你需要查询相关文档，了解标准库提供的哈希表是如何计算对象哈希值的，避免产生类似的问题。

## 总结

上面的说明应该已经吧哈希表的底层原理全部串起来了，最后模拟几个面试问题来总结一下本文的内容：

**1、为什么我们常说，哈希表的增删查改效率都是 O(1)O(1)O(1)**？

因为哈希表底层就是操作一个数组，其主要的时间复杂度来自于哈希函数计算索引和哈希冲突。只要保证哈希函数的复杂度在 O(1)O(1)O(1)，且合理解决哈希冲突的问题，那么增删查改的复杂度就都是 O(1)O(1)O(1)。

**2、哈希表的遍历顺序为什么会变化**？

因为哈希表在达到负载因子时会扩容，这个扩容过程会导致哈希表底层的数组容量变化，哈希函数计算出来的索引也会变化，所以哈希表的遍历顺序也会变化。

**3、哈希表的增删查改效率一定是 O(1)O(1)O(1) 吗**？

不一定，正如前面分析的，只有哈希函数的复杂度是 O(1)O(1)O(1)，且合理解决哈希冲突的问题，才能保证增删查改的复杂度是 O(1)O(1)O(1)。

哈希冲突好解决，都是有标准答案的。关键是哈希函数的计算复杂度。如果使用了错误的 `key` 类型，比如前面用 `ArrayList` 作为 `key` 的例子，那么哈希表的复杂度就会退化成 O(N)O(N)O(N)。

**4、为啥一定要用不可变类型作为哈希表的 `key`**？

因为哈希表的主要操作都依赖于哈希函数计算出来的索引，如果 `key` 的哈希值会变化，会导致键值对意外丢失，产生严重的 bug。

要对自己使用的编程语言标准库中的源码有一定的了解，才能保证写出高效的代码。

下面，就我将手把手带大家分别用拉链法和线性探查法来实现简单的哈希表，来加深对哈希表的理解。

[上一篇双端队列（Deque）原理及实现](https://labuladong.online/zh/algo/data-structure-basic/deque-implement/)[下一篇用拉链法实现哈希表](https://labuladong.online/zh/algo/data-structure-basic/hashtable-chaining/)

---

### 18. 哈希集合的原理及代码实现

原文链接: <https://labuladong.online/zh/algo/data-structure-basic/hash-set/>

前置知识

阅读本文前，你需要先学习：

- [哈希表核心原理](https://labuladong.online/zh/algo/data-structure-basic/hashmap-basic/)

我讲解前面每种数据结构时，都会把原理和代码实现分到两篇文章里讲解，而这里讲哈希集合时，把原理和实现同时放在本文讲解，且本章节只有本文一篇文章，你有没有觉得奇怪？

哈哈，因为哈希集合没什么好讲的，它就是把前文讲的哈希表简单封装了一下：**哈希表的键，其实就是哈希集合**。

这么一句话就可以讲完了，不过我们还是稍微具体讲一下，照顾一下哈希集合的面子。

[上一篇线性探查法的两种代码实现](https://labuladong.online/zh/algo/data-structure-basic/linear-probing-code/)[下一篇用链表加强哈希表（LinkedHashMap）](https://labuladong.online/zh/algo/data-structure-basic/hashtable-with-linked-list/)

---

## 8. 哈希表结构的种种变换

### 19. 跳表核心原理

原文链接: <https://labuladong.online/zh/algo/data-structure-basic/skip-list-basic/>

前置知识

阅读本文前，你需要先学习：

- [链表（链式存储）基础](https://labuladong.online/zh/algo/data-structure-basic/linkedlist-basic/)

在实际的面试中，几乎不会让你手写跳表的实现代码，但可能会问你跳表的基本原理及复杂度分析，所以本站需要讲解这种数据结构。

本文处在基础章节，不会具体讲解跳表的实现细节，只介绍跳表的核心原理。初学者学习本文，知道有这么一种数据结构，了解它的基本原理和时间复杂度即可。具体的代码实现将放到数据结构设计章节。

在 [链表基础](https://labuladong.online/zh/algo/data-structure-basic/linkedlist-basic/) 中我们说到，在单链表中增删查改**指定索引**的元素所需的时间复杂度是 O(N)O(N)O(N)。

其实，如果拿到了待操作的链表节点，操作几次指针就能完成删除、修改、插入操作，时间复杂度是 O(1)O(1)O(1)。

时间主要消耗在查询操作，因为通过索引查询对应的节点，只能从头结点开始，逐个遍历到目标节点，然后才做删除、修改、插入操作。

那么，我们是否可以通过一些优化方式，让链表支持快速的查找操作呢？

有一种方式是借助键值映射，用 O(1)O(1)O(1) 的时间直接拿到目标节点，避免了遍历查找的时间消耗，这个思路在后面的 [哈希链表（LinkedHashMap）](https://labuladong.online/zh/algo/data-structure-basic/hashtable-with-linked-list/) 中会详细介绍。

另一种方式，这就是本文介绍的跳表（Skip List），利用**空间换时间**的思想，用额外的空间记录额外的信息，增删查改的时间复杂度都能优化到 O(log⁡N)O(\log N)O(logN)。

## 跳表核心原理

我们就以查询指定索引的元素为例，来看看跳表是如何优化单链表的。

一条普通的单链表长这样：

```text
index  0  1  2  3  4  5  6  7  8  9
node   a->b->c->d->e->f->g->h->i->j
```

如果我们想查询索引为 7 的元素是什么，只能从索引 0 头结点开始往后遍历，直到遍历到索引 7，找到目标节点 `h`。

而跳表则是这样的：

```text
indexLevel   0-----------------------8-----10
indexLevel   0-----------4-----------8-----10
indexLevel   0-----2-----4-----6-----8-----10
indexLevel   0--1--2--3--4--5--6--7--8--9--10
nodeLevel    a->b->c->d->e->f->g->h->i->j->k
```

跳表相当于在原链表的基础上，增加了多层索引，每向上一层，索引节点的数量减少一半，索引的间隔变为 2 倍，所以索引的高度是 log⁡N\log NlogN，NNN 代表链表中元素的个数。

此时，如果我们想查询索引为 7 的元素，可以从最高层索引开始一层一层地往下找：

首先最高层的第一个索引区间是 `[0, 8]`，可以确定索引 7 在这个区间内，所以从下一层的节点 0 开始搜索；

第二层从节点 0 开始，索引区间 `[0, 4]` 不包含索引 7，继续往右移动到节点 4，索引区间 `[4, 8]` 包含索引 7，所以从下一层的节点 4 开始搜索；

第三层从节点 4 开始，索引区间 `[4, 6]` 不包含索引 7，继续往右移动到节点 6，索引区间 `[6, 8]` 包含索引 7，所以从下一层的节点 6 开始搜索；

第四层从节点 6 开始，索引区间 `[6, 7]` 包含索引 7，最终找到目标节点 `h`。

这个搜索过程中，会经过 log⁡N\log NlogN 层索引，在每层索引中移动的次数不会超过 2 次（因为上层索引区间在下一层被分为两半），所以跳表的查询时间复杂度是 O(log⁡N)O(\log N)O(logN)。

## 总结

上面这个简化的例子应该能让你对跳表的核心原理有个直观的认识，跳表是典型的**空间换时间**设计思路，额外维护多层索引，增加空间复杂度，降低增删查改的时间复杂度。

跳表的具体实现还是有一些复杂，而且和上面的简化示例有一些不同，下面补充几点：

1、上面的例子只展示了查询操作，但跳表肯定得支持插入和删除操作，这就涉及到索引层中节点的动态调整，你需要保证每一层的索引区间尽可能二分，这样才能保证索引层的高度为 log⁡N\log NlogN，否则时间复杂度就会退化。

2、不仅仅是查找索引对应的节点，跳表还可以运用到更通用的场景，比如说有序键值对的存储和查找。实际上，跳表的使用场景和后面我们会学习到的二叉搜索树非常类似，只不过跳表的代码实现相较于自平衡二叉搜索树要简单很多。

关于跳表的具体实现，我会更新到数据结构的设计章节，敬请期待。

[上一篇环形数组技巧及实现](https://labuladong.online/zh/algo/data-structure-basic/cycle-array/)[下一篇位图原理及实现](https://labuladong.online/zh/algo/data-structure-basic/bitmap/)

---

### 20. 位图原理及实现

原文链接: <https://labuladong.online/zh/algo/data-structure-basic/bitmap/>

一句话总结

位图（BitMap）是一种非常节省空间的数据结构，它用一个比特位（bit）的 0 和 1 来标记某个元素是否存在。

在后面做算法题时，我们会经常用到类似 `boolean[] visited` 这样的布尔数组，来记录数组中那些元素已经被访问过。

```text
// 假设 nums 是一个包含 1000 个整数的数组
int[] nums = {...}

// 我们在写算法时
// 可能会用一个布尔数组来记录 nums 中那些元素已经被访问过
boolean[] visited = new boolean[nums.length];
visited[10] = true;
visited[100] = true;
```

我们来仔细观察这个场景，是否存在优化空间？

布尔类型只有 `true` 和 `false` 两种状态，理论上只需要 1 个比特位（bit）的 `0` 和 `1` 就可以表示。

但在大部分编程语言中，由于内存寻址等原因，一个布尔元素通常会占用 1 字节（byte），也就是 8 个比特位的内存。

这就意味着，编程语言内置的布尔数组 `boolean[]` 实际上浪费了 7/8 的内存空间。

那么我们是否可以优化？答案是肯定的。

提示

在实际开发和求解算法题的过程中，我们使用编程语言提供的布尔数组就够了，**除非需要处理的数据规模非常大，否则没必要为了节省这一点内存空间而引入位图这种结构**。

比如后文介绍的 [布隆过滤器](https://labuladong.online/zh/algo/data-structure-basic/bloom-filter/)，专门为了处理超大规模数据而设计，才需要使用位图这种结构进行优化。

[上一篇跳表核心原理](https://labuladong.online/zh/algo/data-structure-basic/skip-list-basic/)[下一篇队列/栈基本原理](https://labuladong.online/zh/algo/data-structure-basic/queue-stack-basic/)

---

### 21. 布隆过滤器原理及实现

原文链接: <https://labuladong.online/zh/algo/data-structure-basic/bloom-filter/>

前置知识

阅读本文前，你需要先学习：

- [哈希表核心原理](https://labuladong.online/zh/algo/data-structure-basic/hashmap-basic/)
- [位图核心原理及实现](https://labuladong.online/zh/algo/data-structure-basic/bitmap/)

一句话总结

布隆过滤器的核心能力是：

- 在超大规模的数据集中，仅使用少量内存空间，即可快速判断一个元素是否存在。
- 具备数据隐私性。即，可以在不暴露具体数据的情况下，判断一个元素是否存在。

它的核心原理是，不存储具体数据，而仅仅存储数据指纹（哈希值），通过比对指纹来判断数据是否存在。

典型的超大规模数据场景有：

- 判断一个 HTTP 请求的 URL 是否在恶意 URL 列表中。这个列表的数量可以达到上亿，我们可以借助布隆过滤器，保证这个查询仅消耗少量的内存和查询时间，否则会影响用户体验。
- 在大数据存储系统中，海量的数据一般会分散存储在多个不同的文件中。查询一个数据时，需要在磁盘上遍历多个文件才能找到，效率很差。我们可以为每个文件在内存中维护一个布隆过滤器，以便快速判断目标数据是否存在于该文件中，避免无效的磁盘 IO 操作。

说到判断元素是否存在，首先应该想到前文讲的 [哈希集合](https://labuladong.online/zh/algo/data-structure-basic/hash-set/)，它可以在 O(1)O(1)O(1) 的时间增删元素，可以在 O(1)O(1)O(1) 的时间判断一个元素是否存在。

但如果数据规模特别大，那就不行了。

因为哈希集合本质上就是哈希表，而在 [哈希表的代码实现](https://labuladong.online/zh/algo/data-structure-basic/hashtable-chaining/) 中，我们必须要用一个 `KVNode` 类把键值数据存储在内存中，以便处理哈希冲突。

所以哈希集合的空间复杂度是 O(N)O(N)O(N)，随着存储元素的数量增加，占用的内存也会线性增加。在超大数据规模场景下，有限的内存肯定是无法加载所有数据的。

同时，因为哈希集合要存储实际的数据，也就不具备数据隐私性。

那么，布隆过滤器是如何实现的呢？有了布隆过滤器，是否还需要哈希集合呢？

[上一篇用数组加强哈希表（ArrayHashMap）](https://labuladong.online/zh/algo/data-structure-basic/hashtable-with-array/)[下一篇二叉树基础及常见类型](https://labuladong.online/zh/algo/data-structure-basic/binary-tree-basic/)

---

## 9. 二叉树结构及遍历

### 22. 二叉堆核心原理及可视化

原文链接: <https://labuladong.online/zh/algo/data-structure-basic/binary-heap-basic/>

前置知识

阅读本文前，你需要先学习：

- [二叉树基础及常见类型](https://labuladong.online/zh/algo/data-structure-basic/binary-tree-basic/)
- [二叉树的递归/层序遍历](https://labuladong.online/zh/algo/data-structure-basic/binary-tree-traverse-basic/)

一句话总结

二叉堆是一种能够动态排序的数据结构，是 [二叉树结构](https://labuladong.online/zh/algo/data-structure-basic/binary-tree-basic/) 的延伸。

二叉堆的主要操作就两个，`sink`（下沉）和 `swim`（上浮），用以维护二叉堆的性质。

二叉堆的主要应用有两个，首先是一种很有用的数据结构优先级队列（Priority Queue），第二是一种排序方法堆排序（Heap Sort）。

这个可视化面板直观地展示了二叉堆的基本操作，你可以点击跳转执行其中的代码，或自己修改代码玩一玩：

算法可视化

下面我就结合可视化面板来展示二叉堆的原理，最后以优先级队列为例，展示二叉堆的代码实现。

[上一篇Trie/字典树/前缀树原理及可视化](https://labuladong.online/zh/algo/data-structure-basic/trie-map-basic/)[下一篇二叉堆/优先级队列代码实现](https://labuladong.online/zh/algo/data-structure-basic/binary-heap-implement/)

---

### 23. 二叉堆/优先级队列代码实现

原文链接: <https://labuladong.online/zh/algo/data-structure-basic/binary-heap-implement/>

前置知识

阅读本文前，你需要先学习：

- [二叉堆的原理](https://labuladong.online/zh/algo/data-structure-basic/binary-heap-basic/)

前文 [二叉堆的原理](https://labuladong.online/zh/algo/data-structure-basic/binary-heap-basic/) 介绍了二叉堆的基本性质、API 和常见应用。本文将结合 [可视化面板](https://labuladong.online/zh/algo/intro/visualize/) 手把手带你实现一个优先级队列。

我们先实现一个简化版的优先级队列，用来帮你理解二叉堆的核心操作 `sink` 和 `swim`。最后我再用给出一个比较完整的代码实现。

[上一篇二叉堆核心原理及可视化](https://labuladong.online/zh/algo/data-structure-basic/binary-heap-basic/)[下一篇线段树核心原理及可视化](https://labuladong.online/zh/algo/data-structure-basic/segment-tree-basic/)

---

### 24. 二叉树基础及常见类型

原文链接: <https://labuladong.online/zh/algo/data-structure-basic/binary-tree-basic/>

前置知识

阅读本文前，你需要先学习：

- [链表（链式存储）基础](https://labuladong.online/zh/algo/data-structure-basic/linkedlist-basic/)

**我认为二叉树是最重要的基本数据结构，没有之一**。

如果你是初学者，现在这个阶段我很难给你彻底解释清楚得出这个结论的原因，你需要认真学习本站后面的内容才能逐渐理解。我暂且总结两个点：

1、二叉树本身是比较简单的基础数据结构，但是很多复杂的数据结构都是基于二叉树的，比如 [红黑树](https://labuladong.online/zh/algo/data-structure-basic/rbtree-basic/)（二叉搜索树）、[多叉树](https://labuladong.online/zh/algo/data-structure-basic/n-ary-tree-traverse-basic/)、[二叉堆](https://labuladong.online/zh/algo/data-structure-basic/binary-heap-basic/)、[图](https://labuladong.online/zh/algo/data-structure-basic/graph-basic/)、[字典树](https://labuladong.online/zh/algo/data-structure-basic/trie-map-basic/)、[并查集](https://labuladong.online/zh/algo/data-structure-basic/union-find-basic/)、[线段树](https://labuladong.online/zh/algo/data-structure-basic/segment-tree-basic/) 等等。你把二叉树玩明白了，这些数据结构都不是问题；如果你不把二叉树搞明白，这些高级数据结构你也很难驾驭。

2、二叉树不单纯是一种数据结构，更是一种常用的算法思维。一切暴力穷举算法，比如 [回溯算法](https://labuladong.online/zh/algo/essential-technique/backtrack-framework/)、[BFS 算法](https://labuladong.online/zh/algo/essential-technique/bfs-framework/)、[动态规划](https://labuladong.online/zh/algo/essential-technique/dynamic-programming-framework/) 本质上也是把具体问题抽象成树结构，你只要抽象出来了，这些问题最终都回归二叉树的问题。同样看一段算法代码，在别人眼里是一串文本，每个字都认识，但连起来就不认识了；而在你眼里的代码就是一棵树，想咋改就咋改，咋改都能改对，实在是太简单了。

后面的数据结构章节包含大量关于二叉树的讲解和习题，你按照本站的目录顺序学习，我会带你把二叉树彻底搞懂，到时候你就明白我为什么这么重视二叉树了。

## 几种常见的二叉树

二叉树的主要难点在于做算法题，它本身其实没啥难的，就是这样一种树形结构嘛：

loading...

上面就是一棵普通的二叉树，几个术语你要了解一下：

1、每个节点下方直接相连的节点称为**子节点**，上方直接相连的节点称为**父节点**。比方说节点 `3` 的父节点是 `1`，左子节点是 `5`，右子节点是 `6`；节点 `5` 的父节点是 `3`，左子节点是 `7`，没有右子节点。

2、以子节点为根的树称为**子树**。比方说节点 `3` 的左子树是节点 `5` 和 `7` 组成的树，右子树是节点 `6` 和 `8` 组成的树。

3、我们称最上方那个没有父节点的节点 `1` 为**根节点**，称最下层没有子节点的节点 `4`、`7`、`8` 为**叶子节点**。

4、我们称从根节点到最下方叶子节点经过的节点个数为二叉树的最大深度/高度，上面这棵树的最大深度是 `4`，即从根节点 `1` 到叶子节点 `7` 或 `8` 的路径上的节点个数。

没啥别的可说的了，就是这么简单。

有一些稍微特殊一些的二叉树，有他们自己的名字，你要了解一下，后面做题时见到这些专业术语，你就知道题目在说啥了。

### 满二叉树

直接看图比较直观，满二叉树就是每一层节点都是满的，整棵树像一个正三角形：

loading...

**满二叉树有个优势，就是它的节点个数很好算**。假设深度为 `h`，那么总节点数就是 `2^h - 1`，等比数列求和嘛，我们应该都学过的。

### 完全二叉树

完全二叉树是指，二叉树的每一层的节点都紧凑靠左排列，且除了最后一层，其他每层都必须是满的：

loading...

不难发现，满二叉树其实是一种特殊的完全二叉树。

**完全二叉树的特点：由于它的节点紧凑排列，如果从左到右从上到下对它的每个节点编号，那么父子节点的索引存在明显的规律**。

这个特点在讲到 [二叉堆核心原理](https://labuladong.online/zh/algo/data-structure-basic/binary-heap-basic/) 和 [线段树核心原理](https://labuladong.online/zh/algo/data-structure-basic/segment-tree-basic/) 时会用到：完全二叉树可以用数组来存储，不需要真的构建链式节点。

完全二叉树还有个比较难发觉的性质：**完全二叉树的左右子树也是完全二叉树**。

或者更准确地说应该是：**完全二叉树的左右子树中，至少有一棵是满二叉树**。

![](https://labuladong.online/images/algo/complete_tree/1.jpg)

这个性质在做算法题的时候会用到，比如 [巧算完全二叉树的节点数](https://labuladong.online/zh/algo/data-structure/count-complete-tree-nodes/)，这里就先提一下。

中英文的定义有区别

关于完全二叉树和满二叉树的定义，中文语境和英文语境似乎有点区别。

我们说的完全二叉树对应英文 Complete Binary Tree，这个没问题，说的是同一种树。

我们说的满二叉树，按理说应该翻译成 Full Binary Tree 对吧，但其实不是，满二叉树的定义对应英文的 Perfect Binary Tree。

而英文中的 Full Binary Tree 是指一棵二叉树的所有节点要么没有孩子节点，要么有两个孩子节点。

![](https://labuladong.online/images/algo/complete_tree/trees.png)

以上定义出自 wikipedia，这里就是顺便一提。其实名词叫什么都无所谓，你知道有这个区别，在看英文资料时留意一下就行了。

### 二叉搜索树

二叉搜索树（Binary Search Tree，简称 BST）是一种很常见的二叉树，它的定义是：

对于树中的每个节点，其**左子树的每个节点**的值都要小于这个节点的值，**右子树的每个节点**的值都要大于这个节点的值。你可以简单记为「左小右大」。

我把「子树的每个节点」加粗了，这是初学者常犯的错误，不要只看子节点，而要看整棵子树的所有节点。

比方说，下面这棵树就是一棵 BST：

loading...

节点 `7` 的左子树所有节点的值都小于 `7`，右子树所有节点的值都大于 `7`；节点 `4` 的左子树所有节点的值都小于 `4`，右子树所有节点的值都大于 `4`，以此类推。

相反的，下面这棵树就不是 BST：

loading...

如果你只注意每个节点的左右子节点，似乎看不出问题。你应该看整棵子树，注意看节点 `7` 的左子树中有个节点 `8`，比 `7` 大，这就不符合 BST 的定义了。

**BST 是非常常用的数据结构。因为左小右大的特性，可以让我们在 BST 中快速找到某个节点，或者找到某个范围内的所有节点，这是 BST 的优势所在**。

比方说，对于一棵普通的二叉树，其中的节点大小没有任何规律可言，那么你要找到某个值为 `x` 的节点，只能从根节点开始遍历整棵树。

而对于 BST，你可以先对比根节点和 `x` 的大小关系，如果 `x` 比根节点大，那么根节点的整棵左子树就可以直接排除了，直接从右子树开始找，这样就可以快速定位到值为 `x` 的那个节点。

关于 BST，后面会有专门的章节详细讲解，并且配有大量的习题，这里先讲些基础概念就够你用了。

### 高度平衡二叉树

高度平衡二叉树（Height-Balanced Binary Tree）是一种特殊的二叉树，**它的「每个节点」的左右子树的高度差不超过 1**。

要注意是每个节点，而不仅仅是根节点。

比如下面这棵二叉树，根节点 `1` 的左子树高度是 2，右子树高度是 3；节点 `2` 的左子树高度是 1，右子树高度是 0；节点 `3` 的左子树高度是 2，右子树高度是 1，以此类推，每个节点的左右子树高度差都不超过 1，所以这是一棵高度平衡的二叉树：

loading...

下面这棵树就不是高度平衡的二叉树，因为节点 `2` 的左子树高度是 2，右子树高度是 0，高度差超过 1，不符合条件：

loading...

**假设高度平衡二叉树中共有 NNN 个节点，那么高度平衡二叉树的高度是 O(log⁡N)O(\log N)O(logN)**。这是非常重要的性质，本站后面的章节会讲解几种基于二叉树的数据结构，如果能保证树的高度为 O(log⁡N)O(\log N)O(logN)，那么这些数据结构的增删查改效率就会很高。

反之，如果树很不平衡，比如这种极端情况：

loading...

那么这棵树其实就等同于单链表，在树中进行增删查改的效率就会大幅降低。

### 自平衡二叉树

上面介绍了高度平衡二叉树，说到它的高度为 O(log⁡N)O(\log N)O(logN)，增删查改的效率高。

如果我们可以在增删二叉树节点时对树的结构进行一些调整，那么就可以让树的高度始终是平衡的，这就是自平衡二叉树（Self-Balanced Binary Tree）。

自平衡的二叉树有很多种实现方式，最经典的就是 [红黑树](https://labuladong.online/zh/algo/data-structure-basic/rbtree-basic/)，一种自平衡的二叉搜索树。

保持树的平衡性，最关键的就是「旋转」操作，下面这个可视化面板展示了红黑树的旋转操作，你可以点击左右旋和左旋的代码，查看旋转的效果：

算法可视化
## 二叉树的实现方式

最常见的二叉树就是类似链表那样的链式存储结构，每个二叉树节点有指向左右子节点的指针，这种方式比较简单直观。

力扣/LeetCode 上给你输入的二叉树一般都是用这种方式构建的，二叉树节点类 `TreeNode` 一般长这样：

```java
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { this.val = x; }
}

// 你可以这样构建一棵二叉树：
TreeNode root = new TreeNode(1);
root.left = new TreeNode(2);
root.right = new TreeNode(3);
root.left.left = new TreeNode(4);
root.right.left = new TreeNode(5);
root.right.right = new TreeNode(6);

// 构建出来的二叉树是这样的：
//     1
//    / \
//   2   3
//  /   / \
// 4   5   6
```

既然说上面是比较常见的实现方式，那言下之意就是还有其他实现方式，对吧？

是的，在 [二叉堆原理及实现](https://labuladong.online/zh/algo/data-structure-basic/binary-heap-basic/) 和 [并查集算法详解](https://labuladong.online/zh/algo/data-structure/union-find/) 中，我们会根据具体的需求场景选择用数组来存储二叉树。

在 [可视化面板](https://labuladong.online/zh/algo/intro/visualize/) 可视化递归函数时，其实是根据函数堆栈生成的递归树，这也可以算是一种二叉树的实现方式。

另外，在一般的算法题中，我们可能会把实际问题**抽象**成二叉树结构，但我们并不需要真的用 `TreeNode` 创建一棵二叉树出来，而是直接用类似 [哈希表](https://labuladong.online/zh/algo/data-structure-basic/hashmap-basic/) 的结构来表示二叉树/多叉树。

比方说这棵二叉树：

loading...

我可以用一个哈希表，其中的键是父节点 id，值是子节点 id 的列表（每个节点的 id 是唯一的），那么一个键值对就是一个多叉树节点了，这棵多叉树就可以表示成这样：

```java
// 1 -> [2, 3]
// 2 -> [4]
// 3 -> [5, 6]

HashMap<Integer, List<Integer>> tree = new HashMap<>();
tree.put(1, Arrays.asList(2, 3));
tree.put(2, Collections.singletonList(4));
tree.put(3, Arrays.asList(5, 6));
```

这样就可以模拟和操作二叉树/多叉树结构，后文讲到图论的时候你就会知道，它有一个新的名字叫做 [邻接表](https://labuladong.online/zh/algo/data-structure-basic/graph-basic/)。

[上一篇布隆过滤器原理及实现](https://labuladong.online/zh/algo/data-structure-basic/bloom-filter/)[下一篇二叉树的递归/层序遍历](https://labuladong.online/zh/algo/data-structure-basic/binary-tree-traverse-basic/)

---

### 25. 二叉树的递归/层序遍历

原文链接: <https://labuladong.online/zh/algo/data-structure-basic/binary-tree-traverse-basic/>

读完本文，你不仅学会了算法套路，还可以顺便解决如下题目：

| LeetCode | 力扣 | 难度 |
| --- | --- | --- |
| [144. Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/) | [144. 二叉树的前序遍历](https://leetcode.cn/problems/binary-tree-preorder-traversal/) |  |
| [94. Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/) | [94. 二叉树的中序遍历](https://leetcode.cn/problems/binary-tree-inorder-traversal/) |  |
| [145. Binary Tree Postorder Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal/) | [145. 二叉树的后序遍历](https://leetcode.cn/problems/binary-tree-postorder-traversal/) |  |
| [102. Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) | [102. 二叉树的层序遍历](https://leetcode.cn/problems/binary-tree-level-order-traversal/) |  |

前置知识

阅读本文前，你需要先学习：

- [二叉树基本概念和几种特殊的二叉树](https://labuladong.online/zh/algo/data-structure-basic/binary-tree-basic/)

一句话总结

二叉树只有**递归遍历**和**层序遍历**这两种，再无其他。递归遍历可以衍生出 DFS 算法，层序遍历可以衍生出 BFS 算法。

递归遍历二叉树节点的顺序是固定的，但是有三个关键位置，在不同位置插入代码，会产生不同的效果。

层序遍历二叉树节点的顺序也是固定的，但是有三种不同的写法，对应不同的场景。

加载思维导图...
视频讲解

![Video Cover](https://labuladong.online/images/algo/vod/tree-traverse.jpg)

了解了 [二叉树基本概念和几种特殊的二叉树](https://labuladong.online/zh/algo/data-structure-basic/binary-tree-basic/)，本文来讲解如何遍历和访问二叉树的节点。

二叉树的遍历算法主要分为递归遍历和层序遍历两种，都有代码模板。递归代码模板可以延伸出后面要讲的 DFS 算法、回溯算法，层序代码模板可以延伸出后面要讲的 BFS 算法，所以我经常强调二叉树结构的重要性。

大家熟知的前序遍历、中序遍历、后序遍历，都属于二叉树的递归遍历，只不过是把自定义代码插入到了代码模板的不同位置而已，下面我会结合可视化面板来讲解。

## 递归遍历（DFS）

递归遍历二叉树的代码模板如下：

```java
// 基本的二叉树节点
class TreeNode {
    int val;
    TreeNode left, right;
}

// 二叉树的递归遍历框架
void traverse(TreeNode root) {
    if (root == null) {
        return;
    }
    traverse(root.left);
    traverse(root.right);
}
```

请问，这段短小精干的代码为什么能遍历二叉树？又是以什么顺序遍历二叉树的？

对于 `traverse` 这样的递归遍历函数，你就可以把它理解成一个在二叉树结构上游走的指针，下面用一个可视化面板直观地展现这个算法的遍历过程。

点开这个可视化面板，右侧 `root` 指针的位置就是 `traverse` 函数遍历到的位置。你可以多次点击 `console.log("enter"` 这一行代码，观察 `root` 指针在树上移动的顺序：

二叉树的递归遍历

不用着急，你可以多看几遍这个可视化面板，直到把 `traverse` 函数遍历二叉树的顺序彻底搞清楚为止。

`traverse` 函数的遍历顺序就是一直往左子节点走，直到遇到空指针不能再走了，才尝试往右子节点走一步；然后再一直尝试往左子节点走，如此循环；如果左右子树都走完了，则返回上一层父节点。

看代码也能看出来，先递归调用的 `root.left`，然后才递归调用的 `root.right`，每次进入 `traverse` 函数，都会先往左子节点递归遍历，直到遇到空指针走不动了，才轮到往右子节点走一次。

那么我们简单拓展一下，如果修改前面的 `traverse` 函数，先递归遍历 `root.right`，再递归遍历 `root.left`，会是什么效果？

```java
// 修改标准的二叉树遍历框架
void traverseFlip(TreeNode root) {
    if (root == null) {
        return;
    }
    // 反过来，先递归遍历右子树，再递归遍历左子树
    traverseFlip(root.right);
    traverseFlip(root.left);
}
```

你可以先脑补一下这个函数遍历二叉树节点的顺序，然后再点开下面的可视化面板，多次点击 `if (root === null)` 这一行代码，观察 `root` 指针在树上移动的顺序，看看和你的设想是否一致：

算法可视化

可以看到 `traverseFlip` 函数也能遍历二叉树的所有节点，只不过和标准的 `traverse` 函数遍历顺序相反。

我举这个 `traverseFlip` 的例子，是想告诉你：

递归遍历节点的顺序（即上面可视化面板中 `root` 在树上的移动顺序）**仅取决于左右子节点的递归调用顺序，与其他代码无关**。

我们说二叉树遍历时，一般不会像 `traverseFlip` 这样遍历二叉树，默认还是按照先左后右的顺序，所以当我们说二叉树遍历的代码模板时，指的是先左后右的遍历顺序：

```java
// 基本的二叉树节点
class TreeNode {
    int val;
    TreeNode left, right;
}

// 二叉树的递归遍历框架
void traverse(TreeNode root) {
    if (root == null) {
        return;
    }
    traverse(root.left);
    traverse(root.right);
}
```

只要这个先左后右的调用顺序不变，那么 `traverse` 函数访问节点的顺序就是固定的，你插入一万行代码进去，也不会变。

有一些数据结构基础的读者可能有点晕了：

不对呀，只要上过大学的数据结构课程，就知道二叉树有前/中/后序三种遍历，会得到三种不同顺序的结果。为啥你这里说递归遍历节点的顺序是固定的呢？

这个问题很好，下面来解答。

### 理解前/中/后序遍历

递归遍历的顺序，即 `traverse` 函数访问节点的顺序确实是固定的。正如可视化面板所示，`root` 指针在树上移动的顺序是固定的：

算法可视化

**但是，你在 `traverse` 函数中不同位置写代码，效果是可以不一样的。前中后序遍历的结果不同，原因是因为你把代码写在了不同位置，所以产生了不同的效果**。

比方说，刚进入一个节点的时候，你还对它的子节点一无所知，而当你要离开一个节点的时候，它的所有子节点你都遍历过了。那么在这两种情况下写的代码，肯定是可以有不同的效果的。

所谓的前中后序遍历，其实就是在二叉树遍历框架的不同位置写代码：

```java
// 二叉树的遍历框架
void traverse(TreeNode root) {
    if (root == null) {
        return;
    }
    // 前序位置
    traverse(root.left);
    // 中序位置
    traverse(root.right);
    // 后序位置
}
```

**前序位置的代码会在进入节点时立即执行；中序位置的代码会在左子树遍历完成后，遍历右子树之前执行；后序位置的代码会在左右子树遍历完成后执行**：

![](https://labuladong.online/images/algo/binary-tree-summary/2.jpeg)

下面结合可视化代码就能很直观地理解了。

请你点开下面的可视化面板，多次点击 `if (root == null)` 这一行代码，可以看到 `root` 指针在树上移动的顺序和刚才一致；节点变绿的顺序，就是前序遍历的结果，因为前序位置的代码是刚进入节点时执行的，所以前序遍历的顺序就是 `root` 指针在树上移动的顺序：

二叉树的前序遍历

中序位置的代码是左子树遍历完成后，还未遍历右子树时执行的。请你点开下面的可视化面板，多次点击 `if (root == null)` 这一行代码，可以看到 `root` 指针在树上移动的顺序和刚才一致；节点变蓝的顺序，就是中序遍历的结果，你会发现一个节点在它的左子树遍历完时才会变蓝：

二叉树的中序遍历

后序位置的代码是左右子树都遍历完，即将离开节点时执行的。请你点开下面的可视化面板，多次点击 `if (root == null)` 这一行代码，可以看到 `root` 指针在树上移动的顺序和刚才一致；节点变红的顺序，就是后序遍历的结果，你会发现一个节点在它的左右子树都遍历完时才会变红：

二叉树的后序遍历

正确理解前中后序位置非常重要，请你仔细理解上面的可视化面板，做到可以心算任意一棵二叉树的前中后序遍历结果。

划重点

特别强调，三种位置的关键区别在于执行时机不同。

实际的算法题中不会简单的让你计算前中后序的遍历结果，而是需要你把正确的代码写到正确的位置，所以你必须准确理解三个位置的代码产生的不同效果，才能写出准确的代码。

我会在 [二叉树算法思想（纲领篇）](https://labuladong.online/zh/algo/essential-technique/binary-tree-summary/) 和习题中深入探讨二叉树遍历框架的前中后序位置，以及如何运用到回溯算法、动态规划算法中，这里就不展开了。

现在，你应该可以完成力扣的 [144. 二叉树的前序遍历](https://leetcode.cn/problems/binary-tree-preorder-traversal/)、[94. 二叉树的中序遍历](https://leetcode.cn/problems/binary-tree-inorder-traversal/)、[145. 二叉树的后序遍历](https://leetcode.cn/problems/binary-tree-postorder-traversal/) 这三道题了。

最后一个知识点，[二叉搜索树（BST）](https://labuladong.online/zh/algo/data-structure-basic/binary-tree-basic/) 的中序遍历结果是有序的，这是 BST 的一个重要性质。

可以看这个可视化面板，点击其中 `res.push(root.val);` 这一行代码，就可以看到中序遍历访问节点的顺序：

BST 的中序遍历结果是有序的

在后面的 [BST 相关习题集](https://labuladong.online/zh/algo/problem-set/bst1/) 中，会有一些题目利用到这个特性。

## 层序遍历（BFS）

上面讲的递归遍历是依赖函数堆栈递归遍历二叉树的，遍历顺序是从最左侧开始，一列一列地走到最右侧。

二叉树的层序遍历，顾名思义，就是一层一层地遍历二叉树：

![](https://labuladong.online/images/algo/dijkstra/1.jpeg)

层序遍历需要借助队列来实现，而且根据不同的需求，可以有三种不同的写法，下面一一列举。

### 写法一

这是最简单的写法，代码如下：

```java
void levelOrderTraverse(TreeNode root) {
    if (root == null) {
        return;
    }
    Queue<TreeNode> q = new LinkedList<>();
    q.offer(root);
    while (!q.isEmpty()) {
        TreeNode cur = q.poll();
        // 访问 cur 节点
        System.out.println(cur.val);

        // 把 cur 的左右子节点加入队列
        if (cur.left != null) {
            q.offer(cur.left);
        }
        if (cur.right != null) {
            q.offer(cur.right);
        }
    }
}
```

你可以打开这个可视化面板，点击其中的 `while (q.length > 0)` 这一行代码，观察 `cur` 变量在树上游走的顺序，就可以看到层序遍历是一层一层，从左到右的遍历二叉树节点：

二叉树的层序遍历
这种写法的优缺点

这种写法最大的优势就是简单。每次把队头元素拿出来，然后把它的左右子节点加入队列，就完事了。

但是这种写法的缺点是，无法知道当前节点在第几层。知道节点的层数是个常见的需求，比方说让你收集每一层的节点，或者计算二叉树的最小深度等等。

所以这种写法虽然简单，但用的不多，下面介绍的写法会更常见一些。

### 写法二

对上面的解法稍加改造，就得出了下面这种写法：

```java
void levelOrderTraverse(TreeNode root) {
    if (root == null) {
        return;
    }
    Queue<TreeNode> q = new LinkedList<>();
    q.offer(root);
    // 记录当前遍历到的层数（根节点视为第 1 层）
    int depth = 1;

    while (!q.isEmpty()) {
        int sz = q.size();
        for (int i = 0; i < sz; i++) {
            TreeNode cur = q.poll();
            // 访问 cur 节点，同时知道它所在的层数
            System.out.println("depth = " + depth + ", val = " + cur.val);

            // 把 cur 的左右子节点加入队列
            if (cur.left != null) {
                q.offer(cur.left);
            }
            if (cur.right != null) {
                q.offer(cur.right);
            }
        }
        depth++;
    }
}
```

注意代码中的内层 for 循环：

```text
int sz = q.size();
for (int i = 0; i < sz; i++) {
    ...
}
```

这个变量 `i` 记录的是节点 `cur` 是当前层的第几个，大部分算法题中都不会用到这个变量，所以你完全可以改用下面的写法：

```text
int sz = q.size();
while (sz-- > 0) {
    ...
}
```

这个属于细节问题，按照自己的喜好来就行。

**但是注意队列的长度 `sz` 一定要在循环开始前保存下来**，因为在循环过程中队列的长度是会变化的，不能直接用 `q.size()` 作为循环条件。

你可以打开这个可视化面板，点击其中的 `console.log` 这一行代码，观察 `cur` 变量在树上游走的顺序，就可以看到还是一层一层，从左到右的遍历二叉树节点，但是这次还会输出节点所在的层数：

二叉树的层序遍历 2

这种写法就可以记录下来每个节点所在的层数，可以解决诸如二叉树最小深度这样的问题，是我们最常用的层序遍历写法。

### 写法三

既然写法二是最常见的，为啥还有个写法三呢？因为要给后面的进阶内容做铺垫。

现在我们只是在探讨二叉树的层序遍历，但是二叉树的层序遍历可以衍生出 [多叉树的层序遍历](https://labuladong.online/zh/algo/data-structure-basic/n-ary-tree-traverse-basic/)，[图的 BFS 遍历](https://labuladong.online/zh/algo/data-structure-basic/graph-traverse-basic/)，以及经典的 [BFS 暴力穷举算法框架](https://labuladong.online/zh/algo/essential-technique/bfs-framework/)，所以这里要拓展延伸一下。

**回顾写法二，我们每向下遍历一层，就给 `depth` 加 1，可以理解为每条树枝的权重是 1，二叉树中每个节点的深度，其实就是从根节点到这个节点的路径权重和，且同一层的所有节点，路径权重和都是相同的**。

那么假设，如果每条树枝的权重可以是任意值，现在让你层序遍历整棵树，打印每个节点的路径权重和，你会怎么做？

这样的话，同一层节点的路径权重和就不一定相同了，写法二这样只维护一个 `depth` 变量就无法满足需求了。

写法三就是为了解决这个问题，在写法一的基础上添加一个 `State` 类，让每个节点自己负责维护自己的路径权重和，代码如下：

```java
class State {
    TreeNode node;
    int depth;

    State(TreeNode node, int depth) {
        this.node = node;
        this.depth = depth;
    }
}

void levelOrderTraverse(TreeNode root) {
    if (root == null) {
        return;
    }
    Queue<State> q = new LinkedList<>();
    // 根节点的路径权重和是 1
    q.offer(new State(root, 1));

    while (!q.isEmpty()) {
        State cur = q.poll();
        // 访问 cur 节点，同时知道它的路径权重和
        System.out.println("depth = " + cur.depth + ", val = " + cur.node.val);

        // 把 cur 的左右子节点加入队列
        if (cur.node.left != null) {
            q.offer(new State(cur.node.left, cur.depth + 1));
        }
        if (cur.node.right != null) {
            q.offer(new State(cur.node.right, cur.depth + 1));
        }
    }
}
```

你可以打开这个可视化面板，点击其中的 `console.log` 这一行代码，就可以看到还是一层一层，从左到右的遍历二叉树节点，还会输出节点所在的层数：

二叉树的层序遍历 3

**这样每个节点都有了自己的 `depth` 变量，是最灵活的，可以满足所有 BFS 算法的需求**。但是由于要额外定义一个 `State` 类比较麻烦，所以非必要的话，用写法二就够了。

其实你很快就会学到，这种边带有权重的场景属于图结构算法，在之后的 [BFS 算法习题集](https://labuladong.online/zh/algo/problem-set/bfs/) 和 [dijkstra 算法](https://labuladong.online/zh/algo/data-structure/dijkstra/) 中，才会用到这种写法。

## 其他遍历？

二叉树的遍历方式只有上面两种，也许有其他的写法，但都是表现形式上的差异，本质上不可能跳出上面两种遍历方式。

比方说，你可能看到用栈来迭代遍历二叉树的代码。但这本质还是是递归遍历，只不过他手动维护栈模拟递归调用罢了。

再比如，你还可能看到递归地一层层遍历二叉树的代码。但这本质还是层序遍历，只不过他把层序遍历代码中的 for 循环用递归的形式展现了。

总之，不要被表象迷惑，二叉树的遍历方式就上面两种，结合后面的教程和习题，你把这两种遍历方式玩明白，一切暴力穷举算法都小菜一碟。

[上一篇二叉树基础及常见类型](https://labuladong.online/zh/algo/data-structure-basic/binary-tree-basic/)[下一篇DFS 和 BFS 的适用场景](https://labuladong.online/zh/algo/data-structure-basic/use-case-of-dfs-bfs/)

---

### 26. 多叉树的递归/层序遍历

原文链接: <https://labuladong.online/zh/algo/data-structure-basic/n-ary-tree-traverse-basic/>

读完本文，你不仅学会了算法套路，还可以顺便解决如下题目：

| LeetCode | 力扣 | 难度 |
| --- | --- | --- |
| [589. N-ary Tree Preorder Traversal](https://leetcode.com/problems/n-ary-tree-preorder-traversal/) | [589. N 叉树的前序遍历](https://leetcode.cn/problems/n-ary-tree-preorder-traversal/) |  |
| [590. N-ary Tree Postorder Traversal](https://leetcode.com/problems/n-ary-tree-postorder-traversal/) | [590. N 叉树的后序遍历](https://leetcode.cn/problems/n-ary-tree-postorder-traversal/) |  |
| [429. N-ary Tree Level Order Traversal](https://leetcode.com/problems/n-ary-tree-level-order-traversal/) | [429. N 叉树的层序遍历](https://leetcode.cn/problems/n-ary-tree-level-order-traversal/) |  |

前置知识

阅读本文前，你需要先学习：

- [二叉树的递归/层序遍历](https://labuladong.online/zh/algo/data-structure-basic/binary-tree-traverse-basic/)

一句话总结

多叉树结构就是 [二叉树结构](https://labuladong.online/zh/algo/data-structure-basic/binary-tree-basic/) 的延伸，二叉树是特殊的多叉树。

多叉树的遍历就是 [二叉树遍历](https://labuladong.online/zh/algo/data-structure-basic/binary-tree-traverse-basic/) 的延伸。

森林是指多个多叉树的集合，单独一棵多叉树是一个特殊的森林。

二叉树的节点长这样，每个节点有两个子节点：

```java
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
}
```

多叉树的节点长这样，每个节点有任意个子节点：

```java
class Node {
    int val;
    List<Node> children;
}
```

就这点区别，其他没了。

## 森林

这里介绍一下「森林」这个名词，后面讲到 [Union Find 并查集算法](https://labuladong.online/zh/algo/data-structure-basic/union-find-basic/) 时，会用到这个概念。

顾名思义，**森林就是多个多叉树的集合（单独一棵多叉树也是一个特殊的森林）**，用代码表示就是多个多叉树的根节点列表，类似这样：

```text
List<Node> forest;
```

只需对每个根节点分别进行 DFS/BFS 遍历，即可遍历森林的所有节点。

在并查集算法中，我们会同时持有多棵多叉树的根节点，那么这些根节点的集合就是一个森林。

接下来说下多叉树的遍历，和二叉树一样，也就递归遍历（DFS）和层序遍历（BFS）两种。

## 递归遍历（DFS）

对比二叉树的遍历框架看多叉树的遍历框架吧：

[上一篇DFS 和 BFS 的适用场景](https://labuladong.online/zh/algo/data-structure-basic/use-case-of-dfs-bfs/)[下一篇二叉搜索树的应用及可视化](https://labuladong.online/zh/algo/data-structure-basic/tree-map-basic/)

---

## 10. 二叉树结构的种种变换

### 27. 线段树核心原理及可视化

原文链接: <https://labuladong.online/zh/algo/data-structure-basic/segment-tree-basic/>

前置知识

阅读本文前，你需要先学习：

- [二叉树基础及常见类型](https://labuladong.online/zh/algo/data-structure-basic/binary-tree-basic/)
- [二叉树的递归/层序遍历](https://labuladong.online/zh/algo/data-structure-basic/binary-tree-traverse-basic/)

一句话总结

线段树是 [二叉树结构](https://labuladong.online/zh/algo/data-structure-basic/binary-tree-basic/) 的衍生，用于高效解决数组的区间查询和区间动态修改问题。

线段树可以在 O(log⁡N)O(\log N)O(logN) 的时间复杂度查询**任意长度**的区间元素聚合值，在 O(log⁡N)O(\log N)O(logN) 的时间复杂度对**任意长度**的区间元素进行动态修改，其中 NNN 为数组中的元素个数。

考虑到这是第一章，我并不准备深入讲解线段树的实现细节，具体代码会在后面的数据结构设计章节介绍。不过这里可以借助可视化面板帮你直观感受一下线段树的几种变化。

首先，[基本的线段树](https://labuladong.online/zh/algo/data-structure/segment-tree-implement/) 包含区间查询 `query` 和**单点修改** `update` 方法，你可以打开这个可视化面板，逐行点击代码，观察 `query` 和 `update` 方法的执行过程：

算法可视化

可以看到这棵二叉树的叶子节点是数组中的元素，非叶子节点就是索引区间（线段）的汇总信息，也就是「线段树」这个名字的由来。

但上面这个线段树有个问题，就是必须输入 `nums` 数组进行构建，如果我们想在一个非常长的区间上进行区间操作，比如 `[0, 10^9]`，那么上来就需要 10910^9109 的空间复杂度构建线段树，这是非常浪费的。

[动态线段树的实现](https://labuladong.online/zh/algo/data-structure/segment-tree-dynamic/) 运用「动态开点」技巧优化线段树处理稀疏数据的内存开销。你可以打开这个可视化面板，逐行点击代码，观察线段树的动态构建过程：

算法可视化

上面的实现都只支持「单点更新」，但更通用的需求是区间更新，比如把索引区间 `[i, j]` 的元素都更新为 `val`。[懒更新线段树的实现](https://labuladong.online/zh/algo/data-structure/segment-tree-lazy-update/) 运用「懒更新」技巧，给线段树新增 `rangeAdd/rangeUpdate` 方法，可以在 O(log⁡N)O(\log N)O(logN) 时间复杂度内完成**任意长度**的区间更新。

你可以打开这个可视化面板，逐行点击代码，观察懒更新线段树的运行过程。`rangeUpdate` 方法更新区间时，并不需要立即更新区间内的所有叶子节点，而是将更新的值缓存在某个非叶子节点中，当调用 `query` 方法进行区间查询时，才逐渐将更新的值向叶子节点传播：

算法可视化

下面我们来介绍线段树的使用场景和核心原理。

## 使用场景

在 [选择排序](https://labuladong.online/zh/algo/data-structure-basic/select-sort/) 中，我们会尝试解决一个需求，就是计算 `nums` 数组中从索引 `i` 开始到末尾的最小值。

我们将提出一种使用 `suffixMin` 数组的优化尝试，即提前预计算一个 `suffixMin` 数组，使得 `suffixMin[i] = min(nums[i..])`，这样就可以在 O(1)O(1)O(1) 时间内查询 `nums[i..]` 的最小值：

[上一篇二叉堆/优先级队列代码实现](https://labuladong.online/zh/algo/data-structure-basic/binary-heap-implement/)[下一篇数据压缩和霍夫曼树](https://labuladong.online/zh/algo/data-structure-basic/huffman-tree/)

---

### 28. 二叉搜索树的应用及可视化

原文链接: <https://labuladong.online/zh/algo/data-structure-basic/tree-map-basic/>

前置知识

阅读本文前，你需要先学习：

- [二叉树基础及常见类型](https://labuladong.online/zh/algo/data-structure-basic/binary-tree-basic/)
- [多叉树的递归/层序遍历](https://labuladong.online/zh/algo/data-structure-basic/n-ary-tree-traverse-basic/)

一句话总结

二叉搜索树是特殊的 [二叉树结构](https://labuladong.online/zh/algo/data-structure-basic/binary-tree-basic/)，其主要的实际应用是 `TreeMap` 和 `TreeSet`。

前文 [几种常见的二叉树类型](https://labuladong.online/zh/algo/data-structure-basic/binary-tree-basic/) 介绍二叉搜索树，接下来我会带你亲自实现一个类似 Java 标准库的 `TreeMap` 和 `TreeSet` 结构，帮助你知行合一。

**不过呢，考虑到本文还处在数据结构基础的章节，本文仅讲解 `TreeMap/TreeSet` 的原理，[动手实现TreeMap/TreeSet](https://labuladong.online/zh/algo/data-structure-basic/tree-map-implement/) 我放到了 [二叉树系列习题](https://labuladong.online/zh/algo/intro/binary-tree-practice/) 的后面**。

因为和前面的哈希表、队列这些数据结构不同，树相关的数据结构需要比较强的递归思维，难度会上一个层级。如果你对递归的理解不够深入，现在给你讲的话不仅学习曲线有些陡峭，而且意义不大，就算你费了半天劲看懂了，遇到实际的题目还是不会，这很打击信心。

所以我建议循序渐进，后面二叉树的习题章节，用 100 多道实际的算法题手把手带你培养递归思维。刷完后你就可以秒杀所有二叉树相关的算法题了，再去看树相关的数据结构实现，就会感觉非常简单。甚至你都不用看我的代码，自己凭感觉就能实现 `TreeMap/TreeSet`。

好了，废话不多说，让我们开始吧。

## 二叉搜索树的优势

前文 [几种常见的二叉树类型](https://labuladong.online/zh/algo/data-structure-basic/binary-tree-basic/) 介绍过二叉搜索树（BST）的特点，即左小右大：

对于树中的每个节点，其**左子树的每个节点**的值都要小于这个节点的值，**右子树的每个节点**的值都要大于这个节点的值。

比方说下面这棵树就是一棵 BST：

loading...

**这个左小右大的特性，可以让我们在 BST 中快速找到某个节点，或者找到某个范围内的所有节点，这是 BST 的优势所在**。

你应该已经学过前文 [二叉树的遍历](https://labuladong.online/zh/algo/data-structure-basic/binary-tree-traverse-basic/)，下面用标准的二叉树遍历函数结合可视化面板来对比展示一下 BST 和普通二叉树的操作差别。

你可以展开下面的两个面板，点击其中 `if (targetNode !== null)` 这一行代码，直观感受一下两个搜索算法的效率差别：

算法可视化
算法可视化

这里展示的是查找目标元素的场景，可以看到，利用 BST 左小右大的特性，可以迅速定位到目标节点，理想的时间复杂度是树的高度 O(logN)O(logN)O(logN)，而普通的二叉树遍历函数则需要 O(N)O(N)O(N) 的时间遍历所有节点。

至于其他增、删、改的操作，你首先查到目标节点，才能进行增删改的操作对吧？增删改的操作无非就是改一改指针，所以增删改的时间复杂度也是 O(logN)O(logN)O(logN)。

## TreeMap/TreeSet 实现原理

你看 `TreeMap` 这个名字，应该就能看出来，它和前文介绍的 [哈希表HashMap](https://labuladong.online/zh/algo/data-structure-basic/hashmap-basic/) 的结构是类似的，都是存储键值对的，`HashMap` 底层把键值对存储在一个 `table` 数组里面，而 `TreeMap` 底层把键值对存储在一棵二叉搜索树的节点里面。

至于 `TreeSet`，它和 `TreeMap` 的关系正如哈希表 `HashMap` 和哈希集合 `HashSet` 的关系一样，说白了就是 `TreeMap` 的简单封装，所以下面主要讲解 `TreeMap` 的实现原理。

力扣经典的 `TreeNode` 结构长这样：

```java
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
}
```

我们只要改一改这个经典的 `TreeNode` 结构，就可以用来实现 `TreeMap` 了：

```java
// 大写 K 为键的类型，大写 V 为值的类型
class TreeNode<K, V> {
    K key;
    V value;

    TreeNode<K, V> left;
    TreeNode<K, V> right;
    TreeNode(K key, V value) {
        this.key = key;
        this.value = value;
    }
}
```

我们将实现的 `TreeMap` 结构有如下 API：

```text
// TreeMap 主要接口
class MyTreeMap<K, V> {

    // ****** Map 键值映射的基本方法 ******

    // 增/改，复杂度 O(logN)
    public void put(K key, V value) {}

    // 查，复杂度 O(logN)
    public V get(K key) {}

    // 删，复杂度 O(logN)
    public void remove(K key) {}

    // 是否包含键 key，复杂度 O(logN)
    public boolean containsKey(K key) {}

    // 返回所有键的集合，结果有序，复杂度 O(N)
    public List<K> keys() {}

    // ****** TreeMap 提供的额外方法 ******

    // 查找最小键，复杂度 O(logN)
    public K firstKey() {}

    // 查找最大键，复杂度 O(logN)
    public K lastKey() {}

    // 查找小于等于 key 的最大键，复杂度 O(logN)
    public K floorKey(K key) {}

    // 查找大于等于 key 的最小键，复杂度 O(logN)
    public K ceilingKey(K key) {}

    // 查找排名为 k 的键，复杂度 O(logN)
    public K selectKey(int k) {}

    // 查找键 key 的排名，复杂度 O(logN)
    public int rank(K key) {}

    // 区间查找，复杂度 O(logN + M)，M 为区间大小
    public List<K> rangeKeys(K low, K high) {}
}
```

除了标准的增删查改方法 `get, put, remove, containsKey` 之外，`TreeMap` 还提供了很多额外方法，主要和 key 的大小相关。怎么样，是不是感觉很强大？

哈希表很实用，但是它确实没办法很好地处理键之间的大小关系。前文 [用链表加强哈希表](https://labuladong.online/zh/algo/data-structure-basic/hashtable-with-linked-list/) 中实现的 `LinkedHashMap` 也只是做到按「**插入顺序**」排列哈希表中的键，依然做不到按「**大小顺序**」排列。

[上一篇多叉树的递归/层序遍历](https://labuladong.online/zh/algo/data-structure-basic/n-ary-tree-traverse-basic/)[下一篇红黑树的完美平衡及可视化](https://labuladong.online/zh/algo/data-structure-basic/rbtree-basic/)

---

### 29. TreeMap/TreeSet 代码实现

原文链接: <https://labuladong.online/zh/algo/data-structure-basic/tree-map-implement/>

前置知识

阅读本文前，你需要先学习：

- [TreeMap/TreeSet 原理](https://labuladong.online/zh/algo/data-structure-basic/tree-map-basic/)

[上一篇优先级队列经典习题](https://labuladong.online/zh/algo/problem-set/binary-heap/)[下一篇基本线段树的代码实现](https://labuladong.online/zh/algo/data-structure/segment-tree-implement/)

---

### 30. Trie/字典树/前缀树原理及可视化

原文链接: <https://labuladong.online/zh/algo/data-structure-basic/trie-map-basic/>

前置知识

阅读本文前，你需要先学习：

- [二叉树基础及常见类型](https://labuladong.online/zh/algo/data-structure-basic/binary-tree-basic/)

一句话总结

Trie 树就是 [多叉树结构](https://labuladong.online/zh/algo/data-structure-basic/n-ary-tree-traverse-basic/) 的延伸，是一种针对字符串进行特殊优化的数据结构。

Trie 树在处理字符串相关操作时有诸多优势，比如节省公共字符串前缀的内存空间、方便处理前缀操作、支持通配符匹配等。

下面这个可视化面板展示了 Trie 树的结构和主要 API，你可以逐行点击代码，观察 console 输出和右侧的 Trie 树结构变化：

算法可视化

本文仅是 Trie 树（也叫做字典树、前缀树）的原理介绍，[动手实现 TrieMap/TrieSet](https://labuladong.online/zh/algo/data-structure-basic/trie-map-basic/) 我放到了[二叉树系列习题章节](https://labuladong.online/zh/algo/intro/binary-tree-practice/) 后面的数据结构设计章节。理由和上篇 [TreeMap/TreeSet 原理](https://labuladong.online/zh/algo/data-structure-basic/tree-map-basic/) 相同，在基础知识章节我不准备讲解这种复杂结构的具体实现，初学者也没必要在这个阶段理解 Trie 树的代码实现。

但是我依然把 Trie 树的原理讲解放在这里，有两个目的：

1、让你直观地感受到二叉树结构的种种幻化，你也许能理解我的教程特别强调二叉树结构的原因了。

2、在开头让你知道有这么一种数据结构，了解它的 API 以及适用的场景。未来你遇到相关的问题，也许就能想到用 Trie 树来解决，最起码有个思路，大不了回来复制代码模板嘛。这种数据结构的实现都是固定的，笔试面试也不会让你从头手搓 Trie 树，复制粘贴直接拿去用就可以了。

好了，废话不多说，让我们开始吧。

本站将会带你实现一个 `TrieMap` 和 `TrieSet`，先来梳理一下我们已经实现过的 Map/Set 类型：

- 标准的 [哈希表HashMap](https://labuladong.online/zh/algo/data-structure-basic/hashmap-basic/)，底层借助一个哈希函数把键值对存在 `table` 数组中，有两种解决哈希冲突的方法。它的特点是快，即基本的增删查改操作时间复杂度都是 O(1)O(1)O(1)。[哈希集合HashSet](https://labuladong.online/zh/algo/data-structure-basic/hash-set/) 是 `HashMap` 的简单封装。
- [哈希链表LinkedHashMap](https://labuladong.online/zh/algo/data-structure-basic/hashtable-with-linked-list/)，是 [双链表结构](https://labuladong.online/zh/algo/data-structure-basic/linkedlist-basic/) 对标准哈希表的加强。它继承了哈希表的操作复杂度，并且可以让哈希表中的所有键保持「插入顺序」。`LinkedHashSet` 是 `LinkedHashMap` 的简单封装。
- [哈希数组ArrayHashMap](https://labuladong.online/zh/algo/data-structure-basic/hashtable-with-array/)，是 [数组结构](https://labuladong.online/zh/algo/data-structure-basic/array-basic/) 对标准哈希表的加强。它继承了哈希表的操作复杂度，并且提供了一个额外的 `randomKey` 函数，可以在 O(1)O(1)O(1) 的时间返回一个随机键。`ArrayHashSet` 是 `ArrayHashMap` 的简单封装。
- [TreeMap映射](https://labuladong.online/zh/algo/data-structure-basic/tree-map-basic/)，底层是一棵二叉搜索树（编程语言标准库一般使用经过改良的自平衡 [红黑树](https://labuladong.online/zh/algo/data-structure-basic/rbtree-basic/)），基本增删查改操作复杂度是 O(logN)O(logN)O(logN)，它的特点是可以动态维护键值对的大小关系，有很多额外的 API 操作键值对。`TreeSet` 集合是 `TreeMap` 映射的简单封装。

`TrieSet` 也是 `TrieMap` 的简单封装，所以下面我们聚焦 `TrieMap` 的实现原理即可。

## Trie 树的主要应用场景

**Trie 树是一种针对字符串有特殊优化的数据结构**，这也许它又被叫做字典树的原因。Trie 树针对字符串的处理有若干优势，下面一一列举。

### 节约存储空间

用 `HashMap` 对比吧，比如说这样存储几个键值对：

```text
Map<String, Integer> map = new HashMap<>();
map.put("apple", 1);
map.put("app", 2);
map.put("appl", 3);
```

回想哈希表的实现原理，键值对会被存到 `table` 数组中，也就是说它真的创建 `"apple"`、`"app"`、`"appl"` 这三个字符串，占用了 12 个字符的内存空间。

但是注意，这三个字符串拥有共同的前缀，`"app"` 这个前缀被重复存储了三次，`"l"` 也被重复存储了两次。

如果换成 TrieMap 来存储：

```text
// Trie 树的键类型固定为 String 类型，值类型可以是泛型
TrieMap<Integer> map = new TrieMap<>();
map.put("apple", 1);
map.put("app", 2);
map.put("appl", 3);
```

Trie 树底层并不会重复存储公共前缀，所以只需要 `"apple"` 这 5 个字符的内存空间来存储键。

这个例子数据量很小，你感觉重复存储几次没啥大不了，但如果键非常多、非常长，且存在大量公共前缀（现实中确实经常有这种情况，比如证件号），那么 Trie 树就能节约大量的内存空间。

### 方便处理前缀操作

举个例子就明白了：

```text
// Trie 树的键类型固定为 String 类型，值类型可以是泛型
TrieMap<Integer> map = new TrieMap<>();
map.put("that", 1);
map.put("the", 2);
map.put("them", 3);
map.put("apple", 4);

// "the" 是 "themxyz" 的最短前缀
System.out.println(map.shortestPrefixOf("themxyz")); // "the"

// "them" 是 "themxyz" 的最长前缀
System.out.println(map.longestPrefixOf("themxyz")); // "them"

// "tha" 是 "that" 的前缀
System.out.println(map.hasKeyWithPrefix("tha")); // true

// 没有以 "thz" 为前缀的键
System.out.println(map.hasKeyWithPrefix("thz")); // false

// "that", "the", "them" 都是 "th" 的前缀
System.out.println(map.keysWithPrefix("th")); // ["that", "the", "them"]
```

除了 `keysWithPrefix` 方法的复杂度取决于返回结果的长度，其他前缀操作的复杂度都是 O(L)O(L)O(L)，其中 LLL 是前缀字符串长度。

你想想上面这几个操作，用 HashMap 或者 TreeMap 能做到吗？应该只能强行遍历所有键，然后一个个比较字符串前缀，复杂度非常高。

话说，这个 `keysWithPrefix` 方法，是不是很适合做自动补全功能呢？

[上一篇红黑树的完美平衡及可视化](https://labuladong.online/zh/algo/data-structure-basic/rbtree-basic/)[下一篇二叉堆核心原理及可视化](https://labuladong.online/zh/algo/data-structure-basic/binary-heap-basic/)

---

### 31. Union Find 并查集原理

原文链接: <https://labuladong.online/zh/algo/data-structure-basic/union-find-basic/>

前置知识

阅读本文前，你需要先学习：

- [二叉树基础及常见类型](https://labuladong.online/zh/algo/data-structure-basic/binary-tree-basic/)
- [图结构基础及通用代码实现](https://labuladong.online/zh/algo/data-structure-basic/graph-basic/)

一句话总结

并查集（Union Find）结构是 [二叉树结构](https://labuladong.online/zh/algo/data-structure-basic/binary-tree-basic/) 的衍生，用于高效解决**无向图的连通性问题**，可以在 O(1)O(1)O(1) 时间内合并两个连通分量，在 O(1)O(1)O(1) 时间内查询两个节点是否连通，在 O(1)O(1)O(1) 时间内查询连通分量的数量。

并查集算法有几种优化方法，可视化面板都做了支持。下面展示一个未经优化的并查集实现，最终多叉树几乎退化成单链表，导致算法效率降低。对于这个问题的优化思路和可视化展示，在下文中会详细介绍。

算法可视化

本文将介绍什么是图的动态连通性问题，以及为什么并查集（Union Find）算法能够高效解决动态连通性问题。

本文会结合 [可视化面板](https://labuladong.online/zh/algo/intro/visualize/) 直观展示 Union Find 算法的核心原理，以及几种优化思路的效果。

考虑到这是基础章节，本文不涉及算法代码的实现细节。具体的代码实现和算法题的运用放在后面的 [Union Find 算法实现及应用](https://labuladong.online/zh/algo/data-structure/union-find/) 和 [并查集经典习题](https://labuladong.online/zh/algo/problem-set/union-find/) 章节中，建议初学者按照目录顺序循序渐进地学习。

## 动态连通性及术语

图论算法中专业术语比较多，我就用一个简单的例子来介绍几个专业术语。

比如下面这个例子，其中有 10 个节点，分别用 0~9 标记，虽然其中没有边，但它依然是一个图结构：

![](https://labuladong.online/images/algo/unionfind/1.jpg)

我们可以说这个图结构中，有 10 个「**连通分量**」，每个节点自身都是一个连通分量，因为它们自成一派，没有和其他节点相连。

现在将其中的一些节点进行「**连接操作**」，比如连接节点 `0,1` 和 `1,2`：

![](https://labuladong.online/images/algo/unionfind/2.jpg)

此时，图结构中的节点 `0,1,2` 之间就连通了，它们三个节点共同构成了一个连通分量，我们可以说这三个节点是「**连通**」的。

同时，这个图结构中的连通分量的数量从 10 减少到了 8，因为连接操作将 `0,1,2` 三个连通分量合并成了一个。

连通关系的性质

1、自反性：节点 `p` 和 `p` 自身是连通的。

2、对称性：如果节点 `p` 和 `q` 连通，那么 `q` 和 `p` 也连通。

3、传递性：如果节点 `p` 和 `q` 连通，`q` 和 `r` 连通，那么 `p` 和 `r` 也连通。

判断这种「等价关系」非常实用，比如说编译器判断同一个内存对象的不同变量引用，比如社交网络中的朋友圈计算等等。

那么动态连通性问题就是说，给你输入一个图结构，然后进行若干次「连接操作」，同时可能会查询任意两个节点是否「连通」，或者查询当前图中有多少个「连通分量」。

我们的目标是设计一种数据结构，在尽可能小的时间复杂度下完成连接操作和查询操作。

## 为什么需要并查集算法

并查集（Union Find）结构提供如下 API：

```text
class UF {
    // 初始化并查集，包含 n 个节点，时间复杂度 O(n)
    public UF(int n);

    // 连接节点 p 和节点 q，时间复杂度 O(1)
    public void union(int p, int q);

    // 查询节点 p 和节点 q 是否连通（是否在同一个连通分量内），时间复杂度 O(1)
    public boolean connected(int p, int q);

    // 查询当前的连通分量数量，时间复杂度 O(1)
    public int count();
}
```

其中 `union` 方法用于连接两个节点，`connected` 方法用于查询两个节点是否连通，`count` 方法用于查询当前图中的连通分量数量。它们都可以在 O(1)O(1)O(1) 时间内完成。

O(1)O(1)O(1) 的时间复杂度是最牛逼的，**假设你没学过并查集算法，你应该如何实现上述几个方法呢**？

也不是完全没办法，比如 [图结构基础及通用代码实现](https://labuladong.online/zh/algo/data-structure-basic/graph-basic/) 中已经介绍了图结构邻接表/邻接矩阵的代码实现，这个 `union` 方法其实就是在图中添加一条无向边，时间复杂度可以做到 O(1)O(1)O(1)。

这个 `connected` 方法怎么实现呢？你是不是想说，去查一下邻接表/邻接矩阵，看看这两个节点是否相连就行了？

不对，别忘了上面讲的「连通」的性质，其中有有一条是「传递性」：如果节点 `p` 和 `q` 连通，`q` 和 `r` 连通，那么 `p` 和 `r` 也连通。

你单纯去查邻接表/邻接矩阵，只能判断两个节点是否**直接相连**，而无法处理这种传递的连通关系。

所以，要想实现 `connected(a, b)`，我们只能使用 [图结构的 DFS/BFS 遍历算法](https://labuladong.online/zh/algo/data-structure-basic/graph-traverse-basic/)，从 `a` 节点开始遍历所有可达的节点，看看 `b` 节点是否在其中，才能判断 `a,b` 两个节点是否连通。

这样的话，`connected` 方法的最坏时间复杂度就是图遍历的复杂度 O(V+E)O(V+E)O(V+E)，其中 VVV 是节点数量，EEE 是边数量。

接下来，`count` 方法如何实现呢？

还得依赖 [图结构的 DFS/BFS 遍历算法](https://labuladong.online/zh/algo/data-structure-basic/graph-traverse-basic/)，但是更麻烦。

你得用 BFS/DFS 遍历整幅图，将所有节点分类到不同的连通分量中，最后统计连通分量的数量。这个过程的时间复杂度是 O(V+E)O(V+E)O(V+E)。

**所以说并查集算法非常巧妙，它不仅可以在 O(1)O(1)O(1) 时间内完成上述操作，而且它根本不需要真的用邻接表/邻接矩阵构造图结构，只需要一个数组就可以了**。

下面具体介绍。

[上一篇最小生成树算法概览](https://labuladong.online/zh/algo/data-structure-basic/graph-minimum-spanning-tree/)[下一篇正在更新 ing](https://labuladong.online/zh/algo/intro/updating-2/)

---

### 32. 红黑树的完美平衡及可视化

原文链接: <https://labuladong.online/zh/algo/data-structure-basic/rbtree-basic/>

前置知识

阅读本文前，你需要先学习：

- [二叉树基础及常见类型](https://labuladong.online/zh/algo/data-structure-basic/binary-tree-basic/)
- [多叉树的递归/层序遍历](https://labuladong.online/zh/algo/data-structure-basic/n-ary-tree-traverse-basic/)
- [二叉搜索树的应用及可视化](https://labuladong.online/zh/algo/data-structure-basic/tree-map-basic/)

一句话总结

红黑树是自平衡的二叉搜索树，它的树高在任何时候都能保持在 O(log⁡N)O(\log N)O(logN)（完美平衡），这样就能保证增删查改的时间复杂度都是 O(log⁡N)O(\log N)O(logN)。

可视化面板支持创建红黑树：

算法可视化

[二叉搜索树的应用及可视化](https://labuladong.online/zh/algo/data-structure-basic/tree-map-basic/) 讲了普通的二叉搜索树存储键值对实现 `TreeMap/TreeSet` 的思路。

二叉搜索树的操作效率取决于树高，树结构越平衡，树高就接近 log⁡N\log NlogN，增删查改的效率就比较高。而普通二叉搜索树最关键的问题是它不会自动对树进行平衡，特殊的情况下会退化成链表，增删查改的时间复杂度退化为 O(N)O(N)O(N)。

下面这个可视化面板就是一个例子，如果插入若干个有序的键值对，你就能发现每次新增的键都会被插入到最右侧，导致这棵二叉搜索树退化成了链表：

[上一篇二叉搜索树的应用及可视化](https://labuladong.online/zh/algo/data-structure-basic/tree-map-basic/)[下一篇Trie/字典树/前缀树原理及可视化](https://labuladong.online/zh/algo/data-structure-basic/trie-map-basic/)

---

## 11. 图结构基础及算法概览

### 33. 图论中的基本术语

原文链接: <https://labuladong.online/zh/algo/data-structure-basic/graph-terminology/>

一幅图结构由若干 **节点 (Vertex)** 和 **边 (Edge)** 构成，其中：

- 每个节点有一个唯一 ID。
- 边可以是有向的（有向图，Directional Graph），也可以是无向的（无向图，Undirected Graph）。
- 边上可以有权重（加权图，Weighted Graph），也可以没有权重（无权图，Unweighted Graph）。

## 边的权重和方向

下图是一个有向无权图：

loading...

图中有一条从节点 `1` 指向节点 `3` 的有向边，这说明可以从节点 `1` 直接到达节点 `3`；但由于没有从节点 `3` 指向节点 `1` 的有向边，所以节点 `3` 不能直接到达节点 `1`。

下图是一个无向无权图：

loading...

图中节点 `1` 和节点 `3` 之间有一条无向边，这说明可以从节点 `1` 到达节点 `3`，也可以从节点 `3` 到达节点 `1`。

你可以把无向图理解成「双向图」，实际上我们在用代码实现图结构的时候就是这么做的。

下图是一个有向加权图：

loading...

下图是一个无向加权图：

loading...

加权图在实际场景中非常常见，比如在地图 App 中，边的权重可以是两个地点之间的距离；在物流网络中，边的权重可以是两个地点之间的运输成本等等。

围绕着加权图，又会有很多经典的图论算法，比如计算最短路径，最小生成树等等，这些都会在后面的章节逐步讲解。

## 度

对于图中的每个节点，有一个**度 (degree)** 的概念。

在无向图中，度就是每个节点相连的边的条数。

比方下面这幅无向图中，节点 `1` 的度为 2，节点 `4` 的度为 4。

loading...

由于有向图的边有方向，所以有向图中每个节点的度被细分为**入度 (indegree)**和**出度（outdegree）**。

比如下图中节点 `3` 的入度为 2（有两条边指向它），出度为 1（它有 1 条边指向别的节点）：

loading...
## 边和节点的数量关系

**我们一般讨论的图结构都是简单图（Simple Graph），即没有自环边（Self loop）和多重边（Multiple edges）的图**。

![](https://labuladong.online/images/algo/graph/simple-graph.jpg)

在简单图中，假设包含 EEE 条边，VVV 个节点，我们想一下边的条数 EEE 的取值范围是多少？

EEE 的最小值可以是 0，相当于图结构中只有若干互不相连的节点，这是可以的。

考虑 EEE 的最大值，图中的每个节点最多可以有 V−1V-1V−1 条边与其他 V−1V-1V−1 个节点相连，所以最多能有的边数为 E=V(V−1)/2≈V2E = V(V-1)/2 \approx V^2E=V(V−1)/2≈V2。

如果几乎每两个节点之间都有一条边，即 EEE 接近 V2V^2V2，我们说这幅图是 **稠密图（Dense Graph）**；如果只有很少的边，即 EEE 远小于 V2V^2V2，我们说这幅图是 **稀疏图（Sparse Graph）**。

## 子图

在图论中，子图是一个重要的基本概念。

**子图 (Subgraph)**：如果图 G′G'G′ 的所有节点和边都包含在图 GGG 中，则称 G′G'G′ 是 GGG 的一个子图。简单来说，子图是从原图中删除一些节点和边后得到的图。

loading...

假设上面这幅图为 GGG，我们举例说明子图的概念。子图有两种特殊类型：

**生成子图 (Spanning Subgraph)**：包含原图中所有节点，但只包含部分边的子图。

下图是图 GGG 的一个生成子图，它包含了所有节点，但移除了节点 `3` 和节点 `4` 之间的边。

loading...

**导出子图 (Induced Subgraph)**：选择原图的一部分节点，以及这些节点之间在原图中的所有边所构成的子图。

下图是图 GGG 的一个导出子图，它包含节点 `1,2,3,4` 及它们之间在原图中的所有边。

loading...

子图的概念在很多图算法中都有应用，比如在寻找最小生成树时，我们实际上是在寻找一个包含所有节点的带权重最小的生成子图。

## 连通性

在图论中，连通性是一个非常重要的概念，它描述了图中节点之间是否存在路径。

### 无向图的连通性

**连通图 (Connected Graph)**: 如果无向图中任意两个节点之间都存在一条路径，我们称这个图是连通的。

loading...

上图是一个连通图，从任意一个节点出发，都能到达其他所有节点。

**连通分量 (Connected Component)**：对于非连通的无向图，其中的多个连通子图被称为连通分量，一个图可以有多个连通分量。

比如下面这幅图有两个连通分量：节点 `1~5` 形成一个连通分量，节点 `6,7` 形成另一个连通分量。

loading...
### 有向图的连通性

有向图的连通性概念稍微复杂一些，因为考虑到边的方向，所以有向图的连通性分为强连通和弱连通。这块知识点有个印象就行了，实际的面试题中主要都是考察无向图的连通性。

**强连通图 (Strongly Connected Graph)**：如果有向图中任意两个节点之间都存在一条有向路径，我们称这个图是强连通的。

比如下面这幅图是一个强连通图，从任意节点出发都能到达其他所有节点。

loading...

**弱连通图 (Weakly Connected Graph)**：如果将有向图中的所有有向边都变成无向边后，该图变成连通的，那么原来的有向图就是弱连通的。

比如下面这幅图不是强连通的（无法从节点 `4` 到达节点 `1`），但它是弱连通的，因为忽略边的方向后，所有节点之间都是连通的。

loading...

**强连通分量 (Strongly Connected Component, SCC)**：有向图中的若干个最大的强连通子图称为强连通分量。

比如下面这幅图有两个强连通分量：节点 `1~3` 形成一个强连通分量，节点 `4~6` 形成另一个强连通分量。

loading...

**弱连通分量 (Weakly Connected Component, WCC)**：将有向图的所有有向边变为无向边后，形成的连通分量称为原有向图的弱连通分量。

图论中还有很多其他的复杂术语，不过对于数据结构和算法的学习，理解上面这些名词就绰绰够用了。后面我们讲到具体的图论算法时，会结合实际场景运用这些概念。

[上一篇数据压缩和霍夫曼树](https://labuladong.online/zh/algo/data-structure-basic/huffman-tree/)[下一篇图结构的通用代码实现](https://labuladong.online/zh/algo/data-structure-basic/graph-basic/)

---

### 34. 图结构的通用代码实现

原文链接: <https://labuladong.online/zh/algo/data-structure-basic/graph-basic/>

前置知识

阅读本文前，你需要先学习：

- [多叉树的递归/层序遍历](https://labuladong.online/zh/algo/data-structure-basic/n-ary-tree-traverse-basic/)

一句话总结

图结构就是 [多叉树结构](https://labuladong.online/zh/algo/data-structure-basic/n-ary-tree-traverse-basic/) 的延伸。图结构逻辑上由若干节点（`Vertex`）和边（`Edge`）构成，我们一般用邻接表、邻接矩阵等方式来存储图。

在树结构中，只允许父节点指向子节点，不存在子节点指向父节点的情况，子节点之间也不会互相链接；而图中没有那么多限制，节点之间可以相互指向，形成复杂的网络结构。

[可视化面板](https://labuladong.online/zh/algo/intro/visualize/) 支持创建图结构，你可以打开下面的可视化面板，即可看到图的逻辑结构，以及邻接表和邻接矩阵的存储方式：

算法可视化

图结构可以对很多复杂的问题进行抽象，产生了很多经典的图论算法，比如 [二分图算法](https://labuladong.online/zh/algo/data-structure/bipartite-graph/)、[拓扑排序](https://labuladong.online/zh/algo/data-structure/topological-sort/)、[最短路径算法](https://labuladong.online/zh/algo/data-structure/dijkstra/)、[最小生成树算法](https://labuladong.online/zh/algo/data-structure/kruskal/) 等，这些都会在后文介绍。

本文主要介绍图的基本概念，以及如何用代码实现图结构。

[上一篇图论中的基本术语](https://labuladong.online/zh/algo/data-structure-basic/graph-terminology/)[下一篇图结构的 DFS/BFS 遍历](https://labuladong.online/zh/algo/data-structure-basic/graph-traverse-basic/)

---

### 35. 图结构的 DFS/BFS 遍历

原文链接: <https://labuladong.online/zh/algo/data-structure-basic/graph-traverse-basic/>

前置知识

阅读本文前，你需要先学习：

- [图结构基础及通用代码实现](https://labuladong.online/zh/algo/data-structure-basic/graph-basic/)
- [多叉树的递归/层序遍历](https://labuladong.online/zh/algo/data-structure-basic/n-ary-tree-traverse-basic/)

一句话总结

图的遍历就是 [多叉树遍历](https://labuladong.online/zh/algo/data-structure-basic/n-ary-tree-traverse-basic/) 的延伸，主要遍历方式还是深度优先搜索（DFS）和广度优先搜索（BFS）。

唯一的区别是，树结构中不存在环，而图结构中可能存在环，所以我们需要标记遍历过的节点，避免遍历函数在环中死循环。

由于图结构的复杂性，可以细分为遍历图的「节点」、「边」和「路径」三种场景，每种场景的代码实现略有不同。

遍历图的「节点」和「边」时，需要 `visited` 数组在前序位置做标记，避免重复遍历；遍历图的「路径」时，需要 `onPath` 数组在前序位置标记节点，在后序位置撤销标记。

[可视化面板](https://labuladong.online/zh/algo/intro/visualize/) 支持创建图结构，同时支持可视化 DFS/BFS 遍历的路径。**你可以直观地看到，图结构看起来虽然比树结构复杂，但图的遍历本质上还是树的遍历**。

先看 DFS 算法，你可以打开下面的可视化面板，多次点击 `console.log` 这行代码，即可看到 DFS 遍历图的过程，`traverse` 函数本质上在遍历一棵多叉递归树：

算法可视化

再看 BFS 算法，你可以打开下面的可视化面板，多次点击 `console.log` 这行代码，即可看到 BFS 遍历图的过程，本质上是在层序遍历一棵多叉树：

算法可视化

下面具体讲解。

## 深度优先搜索（DFS）

前文 [图结构基础和通用实现](https://labuladong.online/zh/algo/data-structure-basic/graph-basic/) 中说了，我们一般不用 `Vertex` 这样的类来存储图，但是这里我还是先用一下这个类，以便大家把图的遍历和多叉树的遍历做对比。后面我会给出基于邻接表/邻接矩阵的遍历代码。

### 遍历所有节点（visited 数组）

对比多叉树的遍历框架看图的遍历框架吧：

```java
// 多叉树节点
class Node {
    int val;
    List<Node> children;
}

// 多叉树的遍历框架
void traverse(Node root) {
    // base case
    if (root == null) {
        return;
    }
    // 前序位置
    System.out.println("visit " + root.val);
    for (Node child : root.children) {
        traverse(child);
    }
    // 后序位置
}

// 图节点
class Vertex {
    int id;
    Vertex[] neighbors;
}

// 图的遍历框架
// 需要一个 visited 数组记录被遍历过的节点
// 避免走回头路陷入死循环
void traverse(Vertex s, boolean[] visited) {
    // base case
    if (s == null) {
        return;
    }
    if (visited[s.id]) {
        // 防止死循环
        return;
    }
    // 前序位置
    visited[s.id] = true;
    System.out.println("visit " + s.id);
    for (Vertex neighbor : s.neighbors) {
        traverse(neighbor, visited);
    }
    // 后序位置
}
```

可以看到，图的遍历比多叉树的遍历多了一个 `visited` 数组，用来记录被遍历过的节点，避免遇到环时陷入死循环。

为什么成环会导致死循环

举个最简单的成环场景，有一条 `1 -> 2` 的边，同时有一条 `2 -> 1` 的边，节点 `1, 2` 就形成了一个环：

```text
1 <=> 2
```

如果我们不标记遍历过的节点，那么从 `1` 开始遍历，会走到 `2`，再走到 `1`，再走到 `2`，再走到 `1`，如此 `1->2->1->2->...` 无限递归循环下去。

如果有了 `visited` 数组，第一次遍历到 `1` 时，会标记 `1` 为已访问，出现 `1->2->1` 这种情况时，发现 `1` 已经被访问过，就会直接返回，从而终止递归，避免了死循环。

有了上面的铺垫，就可以写出基于邻接表/邻接矩阵的图遍历代码了。虽然邻接表/邻接矩阵的底层存储方式不同，但提供了统一的 API，所以直接使用 [图结构基础和通用实现](https://labuladong.online/zh/algo/data-structure-basic/graph-basic/) 中那个 `Graph` 接口的方法即可：

```java
// 遍历图的所有节点
void traverse(Graph graph, int s, boolean[] visited) {
    // base case
    if (s < 0 || s >= graph.size()) {
        return;
    }
    if (visited[s]) {
        // 防止死循环
        return;
    }
    // 前序位置
    visited[s] = true;
    System.out.println("visit " + s);
    for (Edge e : graph.neighbors(s)) {
        traverse(graph, e.to, visited);
    }
    // 后序位置
}
```

你可以打开下面的可视化面板，多次点击 `console.log` 这行代码，即可看到 DFS 遍历图的过程：

算法可视化

由于 `visited` 数组的剪枝作用，这个遍历函数会遍历一次图中的所有节点，并尝试遍历一次所有边，所以算法的时间复杂度是 O(E+V)O(E + V)O(E+V)，其中 `E` 是边的总数，`V` 是节点的总数。

时间复杂度为什么是 $O(E + V)$？

我们之前讲解 [二叉树的遍历](https://labuladong.online/zh/algo/data-structure-basic/binary-tree-traverse-basic/) 时说，二叉树的遍历函数时间复杂度是 O(N)O(N)O(N)，其中 NNN 是节点的总数。

这里图结构既然是树结构的延伸，为什么图的遍历函数时间复杂度是 O(E+V)O(E + V)O(E+V)，要把边的数量 EEE 也算进去呢？为什么不是 O(V)O(V)O(V) 呢？

这是个非常好的问题。你可以花上两分钟想想，我把答案写在下面。

点击查看答案

其实二叉树/多叉树的遍历函数，也要算上边的数量，只不过对于树结构来说，边的数量和节点的数量是近似相等的，所以时间复杂度还是 O(N+N)=O(N)O(N + N) = O(N)O(N+N)=O(N)。

树结构中的边只能由父节点指向子节点，所以除了根节点，你可以把每个节点和它上面那条来自父节点的边配成一对儿，这样就可以比较直观地看出边的数量和节点的数量是近似相等的。

而对于图结构来说，任意两个节点之间都可以连接一条边，边的数量和节点的数量不再有特定的关系，所以我们要说图的遍历函数时间复杂度是 O(E+V)O(E + V)O(E+V)。

### 遍历所有边（二维 visited 数组）

对于图结构，遍历所有边的场景并不多见，主要是 [计算欧拉路径](https://labuladong.online/zh/algo/data-structure-basic/eulerian-graph/) 时会用到，所以这里简单提一下。

上面遍历所有节点的代码用一个一维的 `visited` 数组记录已经访问过的节点，确保每个节点只被遍历一次；那么最简单直接的实现思路就是用一个二维的 `visited` 数组来记录遍历过的边（`visited[u][v]` 表示边 `u->v` 已经被遍历过），从而确保每条边只被遍历一次。

先参考多叉树的遍历进行对比：

```java
// 多叉树节点
class Node {
    int val;
    List<Node> children;
}

// 遍历多叉树的树枝
void traverseBranch(Node root) {
    // base case
    if (root == null) {
        return;
    }
    for (Node child : root.children) {
        System.out.println("visit branch: " + root.val + " -> " + child.val);
        traverseBranch(child);
    }
}

// 图节点
class Vertex {
    int id;
    Vertex[] neighbors;
}

// 遍历图的边
// 需要一个二维 visited 数组记录被遍历过的边，visited[u][v] 表示边 u->v 已经被遍历过
void traverseEdges(Vertex s, boolean[][] visited) {
    // base case
    if (s == null) {
        return;
    }
    for (Vertex neighbor : s.neighbors) {
      // 如果边已经被遍历过，则跳过
      if (visited[s.id][neighbor.id]) {
        continue;
      }
      // 标记并访问边
      visited[s.id][neighbor.id] = true;
      System.out.println("visit edge: " + s.id + " -> " + neighbor.id);
      traverseEdges(neighbor, visited);
    }
}
```

提示

由于一条边由两个节点构成，所以我们需要把前序位置的相关代码放到 for 循环内部。

接下来，我们可以用 [图结构基础和通用实现](https://labuladong.online/zh/algo/data-structure-basic/graph-basic/) 中的 `Graph` 接口来实现：

```java
// 从起点 s 开始遍历图的所有边
void traverseEdges(Graph graph, int s, boolean[][] visited) {
    // base case
    if (s < 0 || s >= graph.size()) {
        return;
    }
    for (Edge e : graph.neighbors(s)) {
      // 如果边已经被遍历过，则跳过
      if (visited[s][e.to]) {
        continue;
      }
      // 标记并访问边
      visited[s][e.to] = true;
      System.out.println("visit edge: " + s + " -> " + e.to);
      traverseEdges(graph, e.to, visited);
    }
}
```

显然，使用二维 `visited` 数组并不是一个很高效的实现方式，因为需要创建二维 `visited` 数组，这个算法的时间复杂度是 O(E+V2)O(E + V^2)O(E+V2)，空间复杂度是 O(V2)O(V^2)O(V2)，其中 EEE 是边的数量，VVV 是节点的数量。

在讲解 [Hierholzer 算法计算欧拉路径](https://labuladong.online/zh/algo/data-structure/eulerian-graph-hierholzer/) 时，我们会介绍一种简单的优化避免使用二维 `visited` 数组，这里暂不展开。

### 遍历所有路径（onPath 数组）

为啥要把图的这几种遍历都讲清楚？因为本站开篇就讲，一切算法的本质是穷举。只要你学会了穷举一切路径，就肯定会计算最短路径，这是图论中一类经典问题。

对于树结构，遍历所有「路径」和遍历所有「节点」是没什么区别的。而对于图结构，遍历所有「路径」和遍历所有「节点」稍有不同。

因为对于树结构来说，只能由父节点指向子节点，所以从根节点 `root` 出发，到任意一个节点 `targetNode` 的路径都是唯一的。换句话说，我遍历一遍树结构的所有节点之后，必然可以找到 `root` 到 `targetNode` 的唯一路径：

[上一篇图结构的通用代码实现](https://labuladong.online/zh/algo/data-structure-basic/graph-basic/)[下一篇欧拉图和一笔画游戏](https://labuladong.online/zh/algo/data-structure-basic/eulerian-graph/)

---

### 36. DFS 和 BFS 的适用场景

原文链接: <https://labuladong.online/zh/algo/data-structure-basic/use-case-of-dfs-bfs/>

读完本文，你不仅学会了算法套路，还可以顺便解决如下题目：

| LeetCode | 力扣 | 难度 |
| --- | --- | --- |
| [111. Minimum Depth of Binary Tree](https://leetcode.com/problems/minimum-depth-of-binary-tree/) | [111. 二叉树的最小深度](https://leetcode.cn/problems/minimum-depth-of-binary-tree/) |  |

前置知识

阅读本文前，你需要先学习：

- [二叉树的递归/层序遍历](https://labuladong.online/zh/algo/data-structure-basic/binary-tree-traverse-basic/)

在实际的算法问题中，DFS 算法常用来穷举所有路径，BFS 算法常用来寻找最短路径，这是什么原因呢？

因为二叉树的递归遍历和层序遍历就是最简单的 DFS 算法和 BFS 算法，所以本文就用一道简单的二叉树例题，说明其中的道理。

[上一篇二叉树的递归/层序遍历](https://labuladong.online/zh/algo/data-structure-basic/binary-tree-traverse-basic/)[下一篇多叉树的递归/层序遍历](https://labuladong.online/zh/algo/data-structure-basic/n-ary-tree-traverse-basic/)

---

### 37. 最小生成树算法概览

原文链接: <https://labuladong.online/zh/algo/data-structure-basic/graph-minimum-spanning-tree/>

前置知识

阅读本文前，你需要先学习：

- [图结构基础及通用代码实现](https://labuladong.online/zh/algo/data-structure-basic/graph-basic/)
- [图结构术语](https://labuladong.online/zh/algo/data-structure-basic/graph-terminology/)

最小生成树是图论中的经典问题，在现实生活中有广泛的应用，比如设计最低成本的通信网络、电路布线、管道铺设等。

考虑到最小生成树的算法实现需要一些其他算法作为铺垫，且本文处在基础章节，所以不会详细讲解算法代码。

本文主要介绍最小生成树的定义及应用场景，并阐述两种经典的最小生成树算法的核心原理。具体的代码实现安排在数据结构设计章节。

## 什么是生成树

首先理解什么是生成树。给定一个无向连通图 GGG，其**生成树**是 GGG 的一个子图，它包含 GGG 中的所有顶点，并且是一棵树（即无环连通图）。

换句话说，生成树具有以下特性：

- 包含原图中的所有顶点。
- 边的数量为顶点数减一（`V-1`条边）。
- 连通且无环。

一个图可以有多个不同的生成树，例如这幅加权图：

loading...

可以有以下生成树，其中属于生成树的边被标记为了红色：

loading...

下面是一个不同的生成树：

loading...
## 什么是最小生成树

如果图是加权图，那么**最小生成树**就是边权重总和最小的生成树。

比如上面展示的例子，第二种生成树是该图的最小生成树，总权重为：2 + 3 + 5 = 10，没有其他的生成树能够得到更小的权重和了。

最小生成树在现实生活中有很多应用场景，边的权重可能代表距离、成本、时间等。

比方说想在若干城市之间修建公路，图中的节点代表城市，边代表城市之间的公路，边的权重代表修建公路的成本，我们希望找到一种方案能够连接所有城市，且总成本最小，这就是典型的最小生成树问题。

## 最小生成树算法

有两种经典的算法用于求解最小生成树问题：Kruskal 算法和 Prim 算法。它们都基于贪心思想，但实现方式不同。

Kruskal 算法相对简单一些，只需要先对图中的所有边按照权重排序，然后借助 [Union-Find 并查集算法](https://labuladong.online/zh/algo/data-structure/union-find/) 即可找到最小生成树。

Prim 算法可以由 [Dijkstra 算法](https://labuladong.online/zh/algo/data-structure/dijkstra/) 拓展而来，借助 [优先级队列](https://labuladong.online/zh/algo/data-structure-basic/binary-heap-basic/) 动态排序的特性，逐步构造最小生成树。

具体的代码实现在 [Kruskal 算法](https://labuladong.online/zh/algo/data-structure/kruskal/) 和 [Prim 算法](https://labuladong.online/zh/algo/data-structure/prim/) 中讲解。

## 随机地图构造问题

最小生成树算法经过一些巧妙的改造后，可以被用于生成游戏中的随机化迷宫、洞穴等场景。

其核心思想是利用最小生成树算法**能够连接所有顶点且无环路**的特性，来确保生成地图的连通性。通过引入随机性，可以创造出每次都不同、看起来自然且复杂的地图结构。

本站包含一个迷宫小游戏，要求你编写 `mazeGenerate` 函数生成迷宫地图，要求必须存在至少一条起点到终点的路径，且地图需要尽可能随机：

生成迷宫的随机地图

我们可以借助游戏面板直观体会一下最小生成树算法生成的地图的特点。

在游戏面板中可以选择「生成算法」和「求解算法」，你可以切换不同的生成算法，然后点击「生成」按钮，即可查看不同的算法生成地图的过程。

先来观察 Krusual 算法，地图被初始化为一个网格图结构，然后从图中的多个位置开始出现随机路径，最终连接成一个完整的迷宫地图。

再来观察 Prim 算法，地图的初始状态全部都是障碍物，然后从起点开始向周围扩展路径，最终连接成一个完整的迷宫地图。

不只是生成地图的过程不同，生成的地图特点也不同。你可以在游戏面板上切换不同的求解算法，点击「求解」按钮，即可对比查看不同的算法求解地图的过程。

我会建议观察 BFS/DFS 算法求解地图的过程，仔细体会一下不同算法生成地图的特点。在后文讲解完最小生成树算法实现之后，我们再具体讲解随机迷宫地图的生成算法。

[上一篇图结构最短路径算法概览](https://labuladong.online/zh/algo/data-structure-basic/graph-shortest-path/)[下一篇Union Find 并查集原理](https://labuladong.online/zh/algo/data-structure-basic/union-find-basic/)

---

### 38. 图结构最短路径算法概览

原文链接: <https://labuladong.online/zh/algo/data-structure-basic/graph-shortest-path/>

前置知识

阅读本文前，你需要先学习：

- [图结构基础及通用代码实现](https://labuladong.online/zh/algo/data-structure-basic/graph-basic/)
- [图结构的 DFS/BFS 遍历](https://labuladong.online/zh/algo/data-structure-basic/graph-traverse-basic/)

一句话总结

Dijkstra 算法和 A* 算法是 [图的 BFS 遍历](https://labuladong.online/zh/algo/data-structure-basic/graph-traverse-basic/) 的拓展，可以处理不包含负权重的单源最短路径问题。

SPFA 算法（基于队列的 Bellman-Ford 算法）是 [图的 BFS 遍历](https://labuladong.online/zh/algo/data-structure-basic/graph-traverse-basic/) 的拓展，可以处理包含负权重的单源最短路径问题。

Floyd 算法是 [动态规划](https://labuladong.online/zh/algo/essential-technique/dynamic-programming-framework/) 的应用，可以处理多源最短路径问题。

加载思维导图...

初学者不要觉得图论算法有多难，因为它们都是基于简单的算法思想扩展出来的。你把基本的二叉树层序遍历玩明白，自己都能发明出来这些算法，没啥了不起的。

考虑到目前处在基础知识章节，所以本文并不会详细讲解每种算法的完整代码，具体的代码实现会安排在之后的章节。

本文的重点在这些算法的关键原理、适用场景，以及这些高级算法和基础知识的联系，帮助初学者对图结构的最短路径算法有一个整体的认识。

## 最短路径问题概览

最短路径问题在生活中应用广泛，比方说计算最小成本、最短路径长度、最少时间等。

在算法中，我们一般把这类问题抽象成计算 [加权图](https://labuladong.online/zh/algo/data-structure-basic/graph-basic/) 中的最小路径权重。为了方便表述，**在本文中「最短路径」和「最小路径权重和」是等价的**。

最短路径问题大致可以分为「单源最短路径」和「多源最短路径」两类，下面会介绍几个经典的算法。

### 单源最短路径

所谓单源最短路径，就是让你计算从某个起点出发，到**其他所有顶点**的最短路径。

比方说一幅图中有 `n` 个节点，编号为 `0, 1, 2, ..., n-1`，让你计算从 `2` 号节点到其他节点的最短路径，这就是单源最短路径问题。

单源最短路径算法最终得到的输出应该是一个一维数组 `distTo`，`distTo[i]` 表示从起点到节点 `i` 的最短路径长度。

比较有代表性的单源最短路径算法有：

1、Dijkstra 算法，其本质是 BFS 算法 + 贪心思想，效率较高，但是不能处理带有负权重的图。

2、基于队列的 Bellman-Ford 算法，其本质也是 BFS 算法，可以处理带有负权重的图，但效率比 Dijkstra 算法低。

### 点对点最短路径

很多算法题中不需要我们计算起点到所有其他节点的最短路径，仅需要计算从起点 `src` 到某一个目标节点 `dst` 的最短路径。这类问题可以称为点对点最短路径问题。

**一般来说，点对点最短路径问题可以视为单源最短路径问题的特例**，你可以从 `src` 开始执行单源最短路径算法，当算出到达 `dst` 的最短路径时提前结束算法。

但是下面将介绍一种专门处理点对点问题的算法：**[A* 算法](https://labuladong.online/zh/algo/data-structure/a-star/)**（A Star Algorithm）。

我经常讲，算法的本质是穷举，你想要提高穷举的效率，就得尽可能充分地利用信息。点对点最短路径问题（已知起点和终点）比单源最短路径问题（已知起点）多了终点信息，所以完全有可能利用这个信息来提高算法的效率。

比方说，如果我们知道终点在起点的右下方，那么我们有理由猜测：应该优先向右下方搜索，可能可以更快地到达终点。

A* 算法的关键就在这里：它能够充分利用已知信息，有方向性地进行搜索，更快地找到终点。我们称这类算法为**启发式搜索算法**（Heuristic Search Algorithm）。

但是请注意，这个猜测只是经验法则，并不一定总是正确。比方说右下方可能都是死路，偏偏就得经过左上角绕个大弯才能到达终点。

所以启发式算法需要合理设置启发函数（Heuristic Function），在经验法则和实际情况中找到平衡，确保在经验法则失效时，算法的效率也不会太差。

### 多源最短路径

所谓**多源最短路径**，就是让你计算任意两节点之间的最短路径。

比方说一幅图中有 `n` 个节点，编号为 `0, 1, 2, ..., n-1`，让你计算所有节点之间的最短路径，这就是多源最短路径问题。

多源最短路径算法最终得到的输出应该是一个二维数组 `dist`，`dist[i][j]` 表示从节点 `i` 到节点 `j` 的最短路径长度。

最有代表性的是 Floyd 算法，其本质是动态规划算法。

理论上，我们对所有节点都调用一次单源最短路径算法，就可以得到多源最短路径的解。

但具体实现时，要根据图结构的特点来选择。有些场景用 Floyd 这种多源最短路径算法效率更高，有些场景多次调用 Dijkstra 这种单源最短路径算法效率更高。后面讲到这些算法的复杂度时，你就能理解了。

### 负权重边的影响

在计算最短路径时，需要着重注意的是这幅图是否包含**负权重边**；一旦包含负权重边，一定要检查是否包含**负权重环**。

为啥负权重边会影响最短路径算法呢？因为负权重边会让问题变得复杂。举个最简单的例子就能直观地理解了：

比方说我们现在站在起点 `s` 上，相邻节点有 `a` 和 `b`，`s->a` 权重为 3，`s->b` 权重为 4。

如果这幅图不存在负权重边，那么根据上述信息，我就已经可以确定 `s` 到 `a` 的最短路径是 `s->a`，权重和为 3。因为你从 `s->b` 这条路径走出去，绕一圈到达 `a` 的路径权重和肯定是大于 4 的，不可能比 3 还小。

但如果这幅图存在负权重边，那可就不一定了。因为可能出现负权重边呀，比方说 `b->a` 的权重为 -10，那么从 `s->b->a` 的路径权重和为 -6，比 `s->a` 的路径权重和 3 还小。

想让 Dijkstra 这类包含贪心思想的算法成立，需要一个前提：**它假设随着经过的边的数量增加，路径权重和一定也会增加**。但负权重边的出现打破了这一假设，导致算法失效。

如果图中存在负权重环，最短路径问题就没有意义了。比方说 `s` 到 `a` 的路径上存在负权重环，那么你可以在这个负权重环上无限转圈，使得路径权重和无限减小下去。

常见最短路径算法中，Dijkstra 算法和 A* 算法不能处理含有负权重边的图，Floyd 算法和 Bellman-Ford 算法可以处理负权重边，Bellman-Ford 算法常用来检测负权重环。

下面，我们介绍这些算法的核心原理。

[上一篇欧拉图和一笔画游戏](https://labuladong.online/zh/algo/data-structure-basic/eulerian-graph/)[下一篇最小生成树算法概览](https://labuladong.online/zh/algo/data-structure-basic/graph-minimum-spanning-tree/)

---

### 39. 欧拉图和一笔画游戏

原文链接: <https://labuladong.online/zh/algo/data-structure-basic/eulerian-graph/>

前置知识

阅读本文前，你需要先学习：

- [图结构术语](https://labuladong.online/zh/algo/data-structure-basic/graph-terminology/)
- [图结构的 DFS/BFS 遍历](https://labuladong.online/zh/algo/data-structure-basic/graph-traverse-basic/)

一句话总结

「一笔画」游戏的本质是寻找欧拉路径/欧拉回路，可以通过节点的度数判断是否存在欧拉路径/欧拉回路。

Hierholzer 算法是用于计算欧拉路径/欧拉回路的经典算法，它是 [图结构 DFS 算法](https://labuladong.online/zh/algo/data-structure-basic/graph-traverse-basic/) 的拓展。

欧拉图是图论中的经典概念，起源于著名的哥尼斯堡七桥问题。这个问题不仅在数学史上具有重要意义，在现代计算机科学中也有广泛应用，比如路径规划、电路设计等。

考虑到这是基础章节，所以不会详细讲解代码实现，具体的算法代码以及习题会安排在数据结构章节的图论部分讲解。

本文主要介绍欧拉图的定义、经典的七桥问题、欧拉路径和欧拉回路的概念，以及寻找欧拉路径的技巧，你可以在本站配套的一笔画小游戏中直观地感受到。

## 一笔画游戏

我记得小时候玩过「一笔画」小游戏，规则就是要求你一笔连接所有的点和边，其中点可以重复经过，但每条边必须恰好经过一次，不能重复经过。

网站配套的游戏面板也收录了这个小游戏：

一笔画游戏

小时候玩这种游戏就是全靠运气，随便选择起点开始乱走一通，能走完就走完，走不完就重新开始。

后来才知道这个益智小游戏其实是一个经典的图论算法，而且有套路可循。

现在就可以告诉你完成游戏的套路：

- 如果所有节点的度数都是偶数，那么可以从任何节点开始，一定可以完成一笔画，且最终会回到起点。
- 如果只有两个节点的度数为奇数，那么必须从这两个奇数度节点中的任意一个开始，才能完成一笔画。
- 如果上面两种情况都不满足，那么无法完成一笔画。

游戏面板中会显示每个节点的 [度数](https://labuladong.online/zh/algo/data-structure-basic/graph-terminology/)，你可以先试试看这个套路好不好用：）

下面我们来介绍这个小游戏背后的图论知识 - 欧拉图。

## 七桥问题

欧拉图的概念源于 18 世纪著名的哥尼斯堡七桥问题。当时的哥尼斯堡（现在的加里宁格勒）有一条河流将城市分为南北两岸，河中有东西两个小岛，有七座桥连接着北岸、南岸、东岛和西岛。

问题是：能否设计一条路线，从任意一个区域出发，经过每座桥恰好一次，最后回到起点？

我们可以将这个问题抽象成图论问题：

loading...

在这幅图中：

- 每个区域对应一个节点
- 每座桥对应一条边
- 问题转化为：是否存在一条路径，经过图中每条边恰好一次，且最终回到起点

最终，欧拉通过数学证明七桥问题无解，从而解决了这个著名问题。

## 术语定义

基于七桥问题，我们引入几个图论术语：

[上一篇图结构的 DFS/BFS 遍历](https://labuladong.online/zh/algo/data-structure-basic/graph-traverse-basic/)[下一篇图结构最短路径算法概览](https://labuladong.online/zh/algo/data-structure-basic/graph-shortest-path/)

---

## 12. 十大排序算法原理及可视化

### 40. 排序算法的关键指标

原文链接: <https://labuladong.online/zh/algo/data-structure-basic/sort-basic/>

前置知识

阅读本文前，你需要先学习：

- [数组基础](https://labuladong.online/zh/algo/data-structure-basic/array-basic/)
- [时空复杂度入门](https://labuladong.online/zh/algo/intro/complexity-basic/)

一般刷题和面试/笔试的时候不会直接让你手撕排序算法，不过考虑到知识的完整性，我这里还是开一个章节，结合 [可视化面板](https://labuladong.online/zh/algo/intro/visualize/) 讲解几种常见排序算法的原理、特点、时间复杂度和代码实现。

本文先介绍一下排序算法的几个关键指标，后面讲解到具体的排序算法时，都会根据这些指标来分析。

## 时空复杂度

首先一个指标肯定是时间复杂度和空间复杂度。

正如 [时空复杂度入门](https://labuladong.online/zh/algo/intro/complexity-basic/) 中所说，对于任意一个算法，其时间复杂度和空间复杂度都是越小越好的。

## 排序稳定性

稳定性是排序算法的一个重要性质，我们可以简单总结为：

**对于序列中的相同元素，如果排序之后它们的相对位置没有发生改变，则称该排序算法为「稳定排序」，反之则为「不稳定排序」**。

如果单单排序 int 数组，那么稳定性没有什么意义。但如果排序一些结构比较复杂的数据，那么稳定排序就会有一定的优势。

比如说现在你有若干订单数据，已经按照交易日期排好序了，现在你想对用户 ID 再进行排序，这样一来相同用户 ID 的订单就会聚集在一起，方便查看。稳定排序和不稳定排序的区别就体现在这里：

**如果你用稳定排序算法**，那么排序完成后，相同用户 ID 的订单依然会按照交易日期有序排列：

```text
   Date    UserID
2020-02-01  1001
2020-02-02  1001
2020-02-03  1001

2020-01-01  1002
2020-01-02  1002
2020-01-03  1002
...
```

因为之前已经按照日期排好序了，对用户 ID 稳定排序之后，相同用户 ID 的订单的相对位置保持不变，所以在日期上依然是有序的。

**如果你用不稳定排序算法**，相同用户 ID 的订单相对位置可能变化，所以对于相同用户 ID 的订单，交易日期的有序性会丧失，相当于你之前对日期的排序白做了。

可以看到，稳定性是个很重要的性质，所以你在使用排序算法时要特别注意，避免出现预期之外的结果。

## 是否原地排序

**原地排序就是指排序过程中不需要额外的辅助空间，只需要常数级别的额外空间，直接操作原数组进行排序**。

注意，关键是是否需要额外的空间，而不是是否返回一个新的数组。具体来说就是类似这样的区别：

```java
// 非原地排序
void sort(int[] nums) {
    // 排序过程中需要额外的辅助数组，消耗 O(N) 的空间
    int[] tmp = new int[nums.length];

    // 对 nums 进行排序
    for ...
}

// 原地排序
void sort(int[] nums) {
    // 直接操作 nums，不需要额外的辅助数组，消耗 O(1) 的空间
    for ...
}
```

:::

不难想到，对于大数据量的排序，原地排序算法是比较有优势的。

排序算法的几个关键指标就是这些，后面我会介绍几种常见的排序算法，都会根据这些指标来分析它们的优劣。

[上一篇本章导读](https://labuladong.online/zh/algo/intro/sorting/)[下一篇选择排序所面临的问题](https://labuladong.online/zh/algo/data-structure-basic/select-sort/)

---

### 41. 拥有稳定性：冒泡排序

原文链接: <https://labuladong.online/zh/algo/data-structure-basic/bubble-sort/>

读完本文，你不仅学会了算法套路，还可以顺便解决如下题目：

| LeetCode | 力扣 | 难度 |
| --- | --- | --- |
| [912. Sort an Array](https://leetcode.com/problems/sort-an-array/) | [912. 排序数组](https://leetcode.cn/problems/sort-an-array/) |  |

前置知识

阅读本文前，你需要先学习：

- [选择排序所面临的问题](https://labuladong.online/zh/algo/data-structure-basic/select-sort/)
- [数组的增删查改操作](https://labuladong.online/zh/algo/data-structure-basic/array-basic/)

一句话总结

冒泡算法是对 [选择排序](https://labuladong.online/zh/algo/data-structure-basic/select-sort/) 的一种优化，通过交换 `nums[sortedIndex]` 右侧的逆序对完成排序，是一种稳定排序算法。

你可以点开可视化面板，点击播放按钮，然后点击加速/减速按钮调节速度，即可直观感受冒泡排序的过程：

算法可视化

前文讲解了 [选择排序](https://labuladong.online/zh/algo/data-structure-basic/select-sort/) 这种最简单直接的排序算法，其中分析了选择排序的几个待优化的问题：

1、选择排序算法是个不稳定排序算法，因为每次都要交换最小元素和当前元素的位置，这样可能会改变相同元素的相对位置。

2、选择排序的时间复杂度和初始数据的有序度完全没有关系，即便输入的是一个已经有序的数组，选择排序的时间复杂度依然是 O(n2)O(n^2)O(n2)。

3、选择排序的时间复杂度是 O(n2)O(n^2)O(n2)，具体的操作次数大概是 n2/2n^2/2n2/2 次，常规的优化思路无法降低时间复杂度。

那么本文就围绕着选择排序的种种缺陷，看看能不能想办法帮它解决一下。

## 重获排序稳定性

前文分析过选择排序失去稳定性的原因，即每次都要交换最小元素（`nums[minIndex]`）和当前元素（`nums[sortedIndex]`），这样可能会改变相同元素的相对位置。

你仔细思考这个交换过程，其实它的目标是把 `nums[minIndex]` 放到到 `nums[sortedIndex]`，至于 `nums[sortedIndex]` 这个位置的元素应该去哪里，它并不关心。**之所以它用交换操作，只是因为交换操作最简单，不需要涉及数据搬移**。

在交换过程中，把 `nums[minIndex]` 放到到 `nums[sortedIndex]` 的操作是不影响相同元素的相对顺序的：

```text
[2, 2', 2'', 1, 1']
 ^           ^
[1, 2', 2'', _, 1']
 ^           ^
sortedIndex  minIndex
```

真正破坏稳定性的，是让 `nums[sortedIndex]` 去 `nums[minIndex]` 的位置这一步：

```text
[1, 2', 2'', 2, 1']
 ^           ^
```

可以看到 `2, 2', 2''` 这三个元素的相对顺序被打乱了。

**所以优化的方向就在这里，你不要图省事儿直接把 `nums[sortedIndex]` 交换到 `nums[minIndex]`，而是模仿 [在数组中部插入元素的操作](https://labuladong.online/zh/algo/data-structure-basic/array-implement/)**，将 `nums[sortedIndex..minIndex]` 的元素整体向后移动一位，把 `nums[sortedIndex + 1]` 的位置空出来让 `nums[sortedIndex]` 这个元素去那里待着。

```text
[2, 2', 2'', 1, 1']
 ^           ^
[1, 2', 2'', _, 1']
 ^           ^
[1, _, 2', 2'', 1']
 ^           ^
[1, 2, 2', 2'', 1']
 ^           ^
sortedIndex  minIndex
```

可以看到，这次 `2, 2', 2''` 和 `1, 1'` 的相对顺序都没有发生改变，选择排序就变成了稳定排序了。

具体代码如下，只需要把 [选择排序](https://labuladong.online/zh/algo/data-structure-basic/select-sort/) 代码中交换元素的部分换一下即可：

```java
// 对选择排序进行第一波优化，获得了稳定性
void sort(int[] nums) {
    int n = nums.length;
    int sortedIndex = 0;
    while (sortedIndex < n) {
        // 在未排序部分中找到最小值 nums[minIndex]
        int minIndex = sortedIndex;
        for (int i = sortedIndex + 1; i < n; i++) {
            if (nums[i] < nums[minIndex]) {
                minIndex = i;
            }
        }

        // 交换最小值和 sortedIndex 处的元素
        // int tmp = nums[sortedIndex];
        // nums[sortedIndex] = nums[minIndex];
        // nums[minIndex] = tmp;

        // 优化：将 nums[minIndex] 插入到 nums[sortedIndex] 的位置
        // 将 nums[sortedIndex..minIndex] 的元素整体向后移动一位
        int minVal = nums[minIndex];
        // 数组搬移数据的操作
        for (int i = minIndex; i > sortedIndex; i--) {
            nums[i] = nums[i - 1];
        }
        nums[sortedIndex] = minVal;

        sortedIndex++;
    }
}
```

你可以拿着这个算法去力扣第 912 题「[排序数组](https://leetcode.cn/problems/sort-an-array/)」提交一下，虽然最后会超时无法通过，但是可以证明这个算法的正确性是没有问题的。

**这个算法对比标准的选择排序，虽然拥有了稳定性，但是执行效率会下降**，虽然从 Big O 表示法的角度来看，两层嵌套循环的时间复杂度还是 O(n2)O(n^2)O(n2)，但毕竟又加了一个 for 循环，实际执行次数肯定会大于标准选择排序的 n2/2n^2/2n2/2 次。

下面我们再来看看，能不能进一步优化，避免这个额外的 for 循环。

## 优化时间复杂度

仔细观察上面的算法代码，while 循环内部主要做了两件事：

1、第一个 for 循环寻找 `nums[sortedIndex..]` 中的最小值。

2、第二个 for 循环将这个最小值插入到 `nums[sortedIndex]` 的位置。

那么我们能否将这两个步骤合在一起呢？具体来说，你在寻找 `nums[sortedIndex..]` 中的最小值的时候能不能做些力所能及的事情，能不能做到找到最小值后，它就已经被放在正确的位置上，不需要再进行数据搬移了？

答案是可以的，看我操作：

```java
// 对选择排序进行第二波优化，获得稳定性的同时避免额外的 for 循环
// 这个算法有另一个名字，叫做冒泡排序
void sort(int[] nums) {
    int n = nums.length;
    int sortedIndex = 0;
    while (sortedIndex < n) {
        // 寻找 nums[sortedIndex..] 中的最小值
        // 同时将这个最小值逐步移动到 nums[sortedIndex] 的位置
        for (int i = n - 1; i > sortedIndex; i--) {
            if (nums[i] < nums[i - 1]) {
                // swap(nums[i], nums[i - 1])
                int tmp = nums[i];
                nums[i] = nums[i - 1];
                nums[i - 1] = tmp;
            }
        }
        sortedIndex++;
    }
}
```

算法可视化

这个优化就比较巧妙了，倒序遍历 `nums[sortedIndex..]`，如果发现逆序对儿，就交换顺序，这样最小值就会逐步移动到 `nums[sortedIndex]` 的位置。

而且由于我们只交换相邻的逆序对儿，不会去碰值相同的元素，所以这个算法是稳定排序。

这个算法的时间复杂度依然是 O(n2)O(n^2)O(n2)，实际执行次数和选择排序类似，也是一个等差数列求和，大约是 n2/2n^2/2n2/2 次。

冒泡排序

这个算法的名字叫做**冒泡排序**，因为它的执行过程就像从数组尾部向头部冒出水泡，每次都会将最小值顶到正确的位置。

## 提前终止算法

上面说到选择排序的一个问题是，其时间复杂度和初始数据的有序度完全没有关系，即便输入的数组已经有序，选择排序依然会执行 O(n2)O(n^2)O(n2) 次操作。

在上面的一些列优化之后，就可以解决这个问题了，具体看代码：

```java
// 进一步优化，数组有序时提前终止算法
void sort(int[] nums) {
    int n = nums.length;
    int sortedIndex = 0;
    while (sortedIndex < n) {
        // 加一个布尔变量，记录是否进行过交换操作
        boolean swapped = false;
        for (int i = n - 1; i > sortedIndex; i--) {
            if (nums[i] < nums[i - 1]) {
                // swap(nums[i], nums[i - 1])
                int tmp = nums[i];
                nums[i] = nums[i - 1];
                nums[i - 1] = tmp;
                swapped = true;
            }
        }
        // 如果一次交换操作都没有进行，说明数组已经有序，可以提前终止算法
        if (!swapped) {
            break;
        }
        sortedIndex++;
    }
}
```

算法可视化

好了，以上就是针对选择排序的一系列优化，最终使它拥有了排序稳定性，并支持在数组有序时提前终止算法。唯一的遗憾是，时间复杂度依然是 O(n2)O(n^2)O(n2)，并没有降低。

下面我们继续探讨，看看还有什么方法能够改进选择排序。

[上一篇选择排序所面临的问题](https://labuladong.online/zh/algo/data-structure-basic/select-sort/)[下一篇运用逆向思维：插入排序](https://labuladong.online/zh/algo/data-structure-basic/insertion-sort/)

---

### 42. 运用逆向思维：插入排序

原文链接: <https://labuladong.online/zh/algo/data-structure-basic/insertion-sort/>

读完本文，你不仅学会了算法套路，还可以顺便解决如下题目：

| LeetCode | 力扣 | 难度 |
| --- | --- | --- |
| [912. Sort an Array](https://leetcode.com/problems/sort-an-array/) | [912. 排序数组](https://leetcode.cn/problems/sort-an-array/) |  |

前置知识

阅读本文前，你需要先学习：

- [选择排序所面临的问题](https://labuladong.online/zh/algo/data-structure-basic/select-sort/)
- [数组的增删查改操作](https://labuladong.online/zh/algo/data-structure-basic/array-basic/)
- [拥有稳定性：冒泡排序](https://labuladong.online/zh/algo/data-structure-basic/bubble-sort/)

一句话总结

插入排序是基于 [选择排序](https://labuladong.online/zh/algo/data-structure-basic/select-sort/) 的一种优化，将 `nums[sortedIndex]` 插入到左侧的有序数组中。对于有序度较高的数组，插入排序的效率比较高。

你可以点开可视化面板，点击播放按钮，然后点击加速/减速按钮调节速度，即可直观感受插入排序的过程：

算法可视化

前文 [选择排序所面临的问题](https://labuladong.online/zh/algo/data-structure-basic/select-sort/) 中分析了选择排序遇到的几个问题，然后逐步优化写出了 [冒泡排序](https://labuladong.online/zh/algo/data-structure-basic/bubble-sort/)，使得排序算法具有稳定性，且能够在输入数组的有序度较高时提前终止，提升效率。

回顾一下，冒泡排序的关键点在于对下面这段代码的优化：

```java
// 对选择排序进行第一波优化，获得了稳定性
void sort(int[] nums) {
    int n = nums.length;
    int sortedIndex = 0;
    while (sortedIndex < n) {
        // 在未排序部分中找到最小值 nums[minIndex]
        int minIndex = sortedIndex;
        for (int i = sortedIndex + 1; i < n; i++) {
            if (nums[i] < nums[minIndex]) {
                minIndex = i;
            }
        }

        // 交换最小值和 sortedIndex 处的元素
        // int tmp = nums[sortedIndex];
        // nums[sortedIndex] = nums[minIndex];
        // nums[minIndex] = tmp;

        // 优化：将 nums[minIndex] 插入到 nums[sortedIndex] 的位置
        // 将 nums[sortedIndex..minIndex] 的元素整体向后移动一位
        int minVal = nums[minIndex];
        // 数组搬移数据的操作
        for (int i = minIndex; i > sortedIndex; i--) {
            nums[i] = nums[i - 1];
        }
        nums[sortedIndex] = minVal;

        sortedIndex++;
    }
}
```

算法可视化

为了避免 while 内存在两个 for 循环，我们使用了一种类似冒泡的方式逐步交换 `nums[sortedIndex..]` 中的逆序对，将最小值换到 `nums[sortedIndex]` 的位置。

好的，先停在这一步，让我们忘记冒泡排序的优化方法，你来思考一下，是否还有其他方法能够优化上述代码，把 while 循环中的两个 for 循环优化成一个 for 循环？

## 反向思维

上面的算法思路是：在 `nums[sortedIndex..]` 中找到最小值，然后将其插入到 `nums[sortedIndex]` 的位置。

**那么我们能不能反过来想，在 `nums[0..sortedIndex-1]` 这个部分有序的数组中，找到 `nums[sortedIndex]` 应该插入的位置，然后进行插入呢**？

当年我思考如何对插入排序进行优化时，是想到过这个思路的，因为我想利用数组的有序性呀：既然 `nums[0..sortedIndex-1]` 这部分是已经排好序的，那么我就可以用二分搜索来寻找 `nums[sortedIndex]` 应该插入的位置。

这样一来，上述代码中的内层第一个 for 循环，我可以给他优化成对数级别的复杂度。

但是仔细想想，用二分搜索好像是多此一举的。因为就算我用二分搜索找到了 `nums[sortedIndex]` 应该插入的位置，我还是需要搬移元素进行插入，那还不如一边遍历一遍交换元素的方法简单高效呢：

```java
// 对选择排序进一步优化，向左侧有序数组中插入元素
// 这个算法有另一个名字，叫做插入排序
void sort(int[] nums) {
    int n = nums.length;
    // 维护 [0, sortedIndex) 是有序数组
    int sortedIndex = 0;
    while (sortedIndex < n) {
        // 将 nums[sortedIndex] 插入到有序数组 [0, sortedIndex) 中
        for (int i = sortedIndex; i > 0; i--) {
            if (nums[i] < nums[i - 1]) {
                // swap(nums[i], nums[i - 1])
                int tmp = nums[i];
                nums[i] = nums[i - 1];
                nums[i - 1] = tmp;
            } else {
                break;
            }
        }
        sortedIndex++;
    }
}
```

算法可视化
插入排序

这个算法的名字叫做**插入排序**，它的执行过程就像是打扑克牌时，将新抓到的牌插入到手中已经排好序的牌中。

插入排序的空间复杂度是 O(1)O(1)O(1)，是原地排序算法。时间复杂度是 O(n2)O(n^2)O(n2)，具体的操作次数和选择排序类似，是一个等差数列求和，大约是 n2/2n^2/2n2/2 次。

插入排序是一种稳定排序，因为只有在 `nums[i] < nums[i - 1]` 的情况下才会交换元素，所以相同元素的相对位置不会发生改变。

## 初始有序度越高，效率越高

显然，插入排序的效率和输入数组的有序度有很大关系，可以举极端例子来理解：

如果输入数组已经有序，或者仅有个别元素逆序，那么插入排序的内层 for 循环几乎不需要执行元素交换，所以时间复杂度接近 O(n)O(n)O(n)。

如果输入的数组是完全逆序的，那么插入排序的效率就会很低，内层 for 循环每次都要对 `nums[0..sortedIndex-1]` 的所有元素进行交换，算法的总时间复杂度就接近 O(n2)O(n^2)O(n2)。

如果对比插入排序和冒泡排序，**插入排序的综合性能应该要高于冒泡排序**。

直观地说，插入排序的内层 for 循环，只需要对 `sortedIndex` 左侧 `nums[0..sortedIndex-1]` 这部分有序数组进行遍历和元素交换，大部分非极端情况下，可能不需要遍历完 `nums[0..sortedIndex-1]` 的所有元素；而冒泡排序的内层 for 循环，每次都需要遍历`sortedIndex` 右侧 `nums[sortedIndex..]` 的所有元素。

所以冒泡排序的操作数大约是 n2/2n^2/2n2/2，而插入排序的操作数会小于 n2/2n^2/2n2/2。

你可以把插入排序的代码拿去力扣第 912 题「[排序数组](https://leetcode.cn/problems/sort-an-array/)」提交，它最终依然会超时，但可以说明算法代码的逻辑是正确的。之后的文章我们继续探讨如何对排序算法进行优化。

[上一篇拥有稳定性：冒泡排序](https://labuladong.online/zh/algo/data-structure-basic/bubble-sort/)[下一篇突破 O(N^2)：希尔排序](https://labuladong.online/zh/algo/data-structure-basic/shell-sort/)

---

### 43. 选择排序所面临的问题

原文链接: <https://labuladong.online/zh/algo/data-structure-basic/select-sort/>

读完本文，你不仅学会了算法套路，还可以顺便解决如下题目：

| LeetCode | 力扣 | 难度 |
| --- | --- | --- |
| [912. Sort an Array](https://leetcode.com/problems/sort-an-array/) | [912. 排序数组](https://leetcode.cn/problems/sort-an-array/) |  |

前置知识

阅读本文前，你需要先学习：

- [排序算法的关键指标](https://labuladong.online/zh/algo/data-structure-basic/sort-basic/)

一句话总结

选择排序是最简单朴素的排序算法，但是时间复杂度较高，且不是稳定排序。其他基础排序算法都是基于选择排序的优化。

你可以点开可视化面板，点击播放按钮，然后点击加速/减速按钮调节速度，即可直观感受选择排序的过程：

算法可视化

如果你是没接触过排序算法的初学者，那是最好的，不要急着看定义之类的东西；如果你之前了解过排序算法，现在请你忘记定义，忘记曾经背诵过的算法代码。

有了前面内容的铺垫，你已经有了一定的编程能力，能够解决一些基础的算法问题了。那么在这个前提下，我有一个学习方法分享，供你参考：

遇到一个新问题的时候，不要急着找人要一个标准答案，而应该启动自己的思考。被灌输一次标准答案，就错失一次机缘，少一分灵气。被灌得多了，人就傻了。

总有些读者，愁眉苦脸地找我诉苦，说算法题刷完了就忘怎么办啊。我还觉得这是好事呢，念念不忘的是执念，忘了才好，说明还没被塞满，这就是独立思考的机缘呀。

所以回到问题，让我们抓住这次机缘。现在就是给你输入一个数组，让你写个排序算法把所有元素从小到大排序，你来说，怎么写？如果你从来没有思考过这个问题，可以停下几分钟想一想。

```text
void sort(int[] nums) {
    // 你的代码，将 nums 中的元素从小到大排序
}
```

我第一次思考这个问题时，想到的最直接的方法是这样的：

先遍历一遍数组，找到数组中的最小值，然后把它和数组的第一个元素交换位置；接着再遍历一遍数组，找到第二小的元素，和数组的第二个元素交换位置；以此类推，直到整个数组有序。

这个算法有一个被大家熟知的名字，叫做「**选择排序**」，即每次都去遍历选择最小的元素。写成代码就是这样的：

```java
void sort(int[] nums) {
    int n = nums.length;
    // sortedIndex 是一个分割线
    // 索引 < sortedIndex 的元素都是已排序的
    // 索引 >= sortedIndex 的元素都是未排序的
    // 初始化为 0，表示整个数组都是未排序的
    int sortedIndex = 0;
    while (sortedIndex < n) {
        // 找到未排序部分 [sortedIndex, n) 中的最小值
        int minIndex = sortedIndex;
        for (int i = sortedIndex + 1; i < n; i++) {
            if (nums[i] < nums[minIndex]) {
                minIndex = i;
            }
        }
        // 交换最小值和 sortedIndex 处的元素
        int tmp = nums[sortedIndex];
        nums[sortedIndex] = nums[minIndex];
        nums[minIndex] = tmp;

        // sortedIndex 后移一位
        sortedIndex++;
    }
}
```

上述算法的可视化过程如下：

算法可视化

这个算法是正确的，稍加改动就可以作为力扣第 912 题「[排序数组](https://leetcode.cn/problems/sort-an-array/)」的解法代码。

但这个算法无法通过 912 题的所有测试用例，最后会得到一个超时的错误，这说明算法的逻辑是正确的，只是时间复杂度较高，超出了题目的限制。

暂且不管如何通过 912 题，我们先来按照 [排序算法的几个关键指标](https://labuladong.online/zh/algo/data-structure-basic/sort-basic/) 来分析一下这个排序算法。

## 是否是原地排序

是的。因为算法并没有使用额外的数组空间进行辅助，只是用了几个变量，空间复杂度是 O(1)O(1)O(1)。

## 时空复杂度分析

这个 `sort` 函数中包含一个 while 循环嵌套一个 for 循环，相当于是这样：

```text
for (int sortedIndex = 0; sortedIndex < n; sortedIndex++) {
    for (int i = sortedIndex + 1; i < n; i++) {
        // ...
    }
}
```

你看到了，这就是嵌套 for 循环，总的循环次数是 `(n - 1) + (n - 2) + (n - 3) +... + 1`，这是等差数列求和，结果近似是 `n^2 / 2`，所以这个排序算法的时间复杂度用 Big O 表示法就是 O(n2)O(n^2)O(n2)，其中 `n` 是待排序数组的元素个数。

而且你注意这个算法有个特点，即便整个数组已经是有序的，它还是会执行 `n^2 / 2` 次，即原始数据的有序度对算法的时间复杂度没有任何影响。

要关注排序算法的实际执行次数

对于一般的算法时空复杂度分析，我们只需要从 Big O 表示法的角度来分析即可，即仅关心量级（最高次项）的大小，而不关心系数和低次项。

但是在分析不同排序算法的场景下，实际的执行次数，以及一些特殊情况（比如数组本身就有序的情况），还是有必要关注的。

因为有多种排序算法从 Big O 的视角来看都是 O(n2)O(n^2)O(n2) 复杂度，那么我们要根据他们的实际执行次数以及特殊情况下的表现，来分析它们的优劣。

## 时间都去哪了？优化思路？

现在，请你观察这个算法的逻辑，仔细思考几分钟，时间复杂度是否还有优化的可能？

**不要小看这里是基础章节，我讲的都是思维方法，未来你做任何题目，优化时间复杂度的思路和这里一模一样**。

首先，如果代码没有写错，算法时间复杂度还是太高，那只有一种可能，就是**存在冗余计算**。

上述算法中出现冗余计算的地方比较容易看出来：

它首先遍历 `nums[0..]` 寻找最小值，然后遍历 `nums[1..]` 寻找最小值，然后遍历 `nums[2..]` 寻找最小值，以此类推。

那么请问，在遍历 `nums[0..]` 的时候，其实已经遍历过 `nums[1..]` 和 `nums[2..]` 的所有元素了，你为什么要再次遍历呢？

理论上，你应该可以在遍历 `nums[0..]` 的时候，顺便找到 `nums[1..]` 和 `nums[2..]` 的最小元素，对吧？如果能做到这一点，是不是就可以消掉内层的 for 循环，从把时间复杂度降低一个数量级？

好，现在我们已经找到了冗余计算的症结所在，并且有了一个优化思路。那么这个思路是否可以实现呢？你是否能够在遍历 `nums[0..]` 的时候，顺便找到 `nums[1..]` 和 `nums[2..]` 的最小元素？

**我将进行抽象，把这个优化场景转化成一个全新的问题**：

给你一个数组 `nums`，请你计算一个新数组 `suffixMin` 数组，其中 `suffixMin[i]` 表示 `nums[i..]` 中的最小值。

如果正着思考，假设现在我知道了 `nums[0..]` 中的最小元素，我是否能够推导出 `nums[1..]` 中的最小元素呢？

答案是不可能。信息不足，我实在不知道如何根据 `min(nums[0..])` 推导出 `min(nums[1..])`，只能重新遍历一遍 `nums[1..]`。

但是，我自己都不相信，就是算个最小值，咋可能这么难搞呢？我的脑子被智子锁死了吗？？？

如果反过来思考，假设现在我知道了 `nums[1..]` 中的最小元素，我是否能够推导出 `nums[0..]` 中的最小元素呢？

答案是可以的，`min(nums[0..]) = min(nums[0], min(nums[1..]))`。

有了这个思路，这个 `suffixMin` 数组就能算出来了，关键是倒着计算：

```text
int[] nums = new int[]{3, 1, 4, 2};
// suffixMin[i] 表示 nums[i..] 中的最小值
int[] suffixMin = new int[nums.length];

// 从后往前计算 suffixMin
suffixMin[nums.length - 1] = nums[nums.length - 1];
for (int i = nums.length - 2; i >= 0; i--) {
    suffixMin[i] = Math.min(nums[i], suffixMin[i + 1]);
}

// [1, 1, 2, 2]
System.out.println(suffixMin);
```

好了，这个计算 `suffixMin` 数组的问题解决了，现在回到选择排序的优化，我现在只需要花 O(n)O(n)O(n) 的时间遍历一遍 `nums` 数组算出 `suffixMin` 数组，就可以在 O(1)O(1)O(1) 的时间内得到 `nums[1..], nums[2..], ...` 任意子数组的最小值。

按理说，现在我可以把选择排序的内层 for 循环消掉，时间复杂度优化成 O(n)O(n)O(n) 了，对吗？**答案是不行**。

请你思考几分钟，为什么不行，关键的问题在哪里？

点击查看我的思考

有的读者可能会说，选择排序中需要知道最小元素的索引进行交换，而 `suffixMin` 数组里面只存储了最小元素的值，没有存储索引，所以无法优化选择排序。

但是，我完全可以建一个新数组 `minIndex`，在计算 `suffixMin` 数组的时候，同时在 `minIndex` 记录下最小元素对应的索引，所以这个问题不是关键。

**其实，问题的关键在于交换操作**。

`suffixMin` 数组正确工作有个前提，就是 `nums` 数组不可变。如果 `nums[i]` 的值发生改变，那么所有 `suffixMin[0..i]` 存储的最小值就失效了，需要重新计算一次才行。

这个应该不难理解吧，比方说你的 `suffixMin[3] = 6`，意思是 `nums[3..]` 中的最小值是 6。如果你修改了 `nums[5] = 2`，那么 `suffixMin[0..5]` 的值都应该变成 2，而不再是 6 了。

选择排序中的交换操作，会导致 `nums` 中的元素位置发生变化，进而导致 `suffixMin` 数组失效，这才是问题的本质。

综上，所有尝试都是错误的，选择排序无法进行任何优化。

那么我们花了那么多时间，尝试了种种方法，最后啥名堂也没弄出来，是不是很失败？

不，我认为这些才是有效的思考，是真正能够帮助读者掌握算法思维的。

比如上面预计算 `suffixMin` 的方法是一种经典的算法思维，后文 [前缀和技巧](https://labuladong.online/zh/algo/data-structure/prefix-sum/) 就会用到。`nums` 数组变化导致预计算数组 `suffixMin` 失效也是一类经典的算法问题，后文 [线段树基础](https://labuladong.online/zh/algo/data-structure-basic/segment-tree-basic/) 会解决这个问题。

在本站的教程中，我会经常展现这种思考过程。在后面讲到的排序算法中，你也可以思考一下，它们的本质上和选择排序有什么区别？凭什么它们就能把时间复杂度降到 O(n2)O(n^2)O(n2) 以下？

## 排序的稳定性

请你按照 [排序算法的几个关键指标](https://labuladong.online/zh/algo/data-structure-basic/sort-basic/) 中对排序稳定性的定义，分析一下这个算法是不是稳定排序？

如果这个算法不是稳定排序，那么是什么操作导致了它失去了排序稳定性呢？是否可以优化这个算法，使它成为稳定排序？请思考几分钟，然后再看我的理解。

点击查看答案

**选择排序算法不是稳定排序**。

按照稳定排序的定义，相同元素的相对位置不会发生变化才能称为稳定排序。你举个简单的例子就看出这个算法不稳定了：

```text
[2', 2''', 2'', 1]
```

这个例子中有多个重复元素 `2`，我分别用 `2'`、`2'''`、`2''` 来区别这三个元素。如果这个排序算法是稳定的，那么排序后的结果应该保持三个 `2` 的相对顺序：

```text
[1, 2', 2''', 2'']
```

但实际上，你在脑子里跑一下这个算法就能想到，它第一次寻找最小值时，肯定会把元素 `2'` 和 `1` 交换，这一下就会打乱 `2` 之间的相对顺序了：

```text
[1, 2''', 2'', 2']
```

**是交换操作，使得选择排序失去了排序的稳定性**。

有没有什么办法可以优化这个算法，使它成为稳定排序？现在时间复杂度都到 O(n2)O(n^2)O(n2) 了，属于排序算法里面最差的那一档，好歹咱也支棱起来，把自己搞成一个稳定排序，行不行？

你可以自己想一想这个问题，在后面的排序算法，我们会尝试解决这个问题。

[上一篇排序算法的关键指标](https://labuladong.online/zh/algo/data-structure-basic/sort-basic/)[下一篇拥有稳定性：冒泡排序](https://labuladong.online/zh/algo/data-structure-basic/bubble-sort/)

---

### 44. 妙用二叉树后序位置：归并排序

原文链接: <https://labuladong.online/zh/algo/data-structure-basic/merge-sort/>

前置知识

阅读本文前，你需要先学习：

- [二叉树的遍历](https://labuladong.online/zh/algo/data-structure-basic/binary-tree-traverse-basic/)
- [妙用二叉树前序位置：快速排序](https://labuladong.online/zh/algo/data-structure-basic/quick-sort/)

一句话总结

归并排序的核心思路需要结合 [二叉树的后序遍历](https://labuladong.online/zh/algo/data-structure-basic/binary-tree-traverse-basic/) 来理解：先利用递归把左右两半子数组排好序，然后在二叉树的后序位置合并两个有序数组。

你可以点开这个可视化面板，点击全屏按钮 ，然后多次点击 `merge(nums, lo, mid, hi);` 这一行代码，即可直观地看到归并排序的递归过程和排序效果：

算法可视化

**考虑到这里是基础知识章节，我只会讲一下归并排序的整体思路**，具体的代码实现和算法运用会安排在二叉树章节后面的 [归并排序详解及运用](https://labuladong.online/zh/algo/practice-in-action/merge-sort/) 里，不建议初学者现在去看。

因为归并排序算法需要熟练掌握递归思维，且需要用到 [双指针技巧](https://labuladong.online/zh/algo/essential-technique/linked-list-skills-summary/) 来合并两个有序数组，所以建议初学者按照本站目录顺序学习，到时候理解归并排序的代码会比较轻松。

## 归并排序核心思路

开头的这句总结虽然也比较抽象，但是有上一章 [快速排序核心思路](https://labuladong.online/zh/algo/data-structure-basic/quick-sort/) 的铺垫，你应该有点感觉。

我用快速排序的思路来对比一下，你就能直观感受到它俩的区别了：

前文快速排序的思路是，先把一个元素放到正确的位置（排好序），然后将这个元素左右两边剩下的元素利用递归分别排好序，最终整个数组就排好序了。代码框架如下：

[上一篇妙用二叉树前序位置：快速排序](https://labuladong.online/zh/algo/data-structure-basic/quick-sort/)[下一篇二叉堆结构的运用：堆排序](https://labuladong.online/zh/algo/data-structure-basic/heap-sort/)

---

### 45. 妙用二叉树前序位置：快速排序

原文链接: <https://labuladong.online/zh/algo/data-structure-basic/quick-sort/>

前置知识

阅读本文前，你需要先学习：

- [选择排序所面临的问题](https://labuladong.online/zh/algo/data-structure-basic/select-sort/)
- [二叉树的遍历](https://labuladong.online/zh/algo/data-structure-basic/binary-tree-traverse-basic/)

一句话总结

快速排序的核心思路需要结合 [二叉树的前序遍历](https://labuladong.online/zh/algo/data-structure-basic/binary-tree-traverse-basic/) 来理解：在二叉树遍历的前序位置将一个元素排好位置，然后递归地将剩下的元素排好位置。

你可以点开这个可视化面板，点击全屏按钮 ，然后多次点击 `let p = partition(nums, lo, hi)` 这部分代码，即可直观地看到快排的递归过程和排序效果：

算法可视化

上来这一句总结是不是就把初学者听懵了？数组排序算法怎么扯到二叉树上了？

所以说，计算机思维和人类思维是不一样的。

正常人要排序数组，一般就是维护一个 `sortedIndex`，保持 `[0, sortedIndex)` 有序，逐步右移 `sortedIndex`，直到整个数组有序。这中间历经种种坎坷，逢山开路遇水搭桥，正如我们前面讲的 [选择排序](https://labuladong.online/zh/algo/data-structure-basic/select-sort/)、[冒泡排序](https://labuladong.online/zh/algo/data-structure-basic/bubble-sort/)、[插入排序](https://labuladong.online/zh/algo/data-structure-basic/insertion-sort/)、[希尔排序](https://labuladong.online/zh/algo/data-structure-basic/shell-sort/)。

**但是越是效率高的算法，离计算机思维越近，未经训练的人就越难理解**。学过前面几种基础排序算法，现在你应该可以感觉到这一点了，容易理解和推导的排序算法复杂度全都是 O(N2)O(N^2)O(N2)，而突破 O(N2)O(N^2)O(N2) 的排序算法，都感觉不是人类能想出来的。

哪个人要是张嘴就说：排序数组简单啊，只要把一个元素排好序，然后把剩下元素排好序，就能把整个数组排好序了。那只能说这个人可能是三体人潜伏在地球的特务：）

[上一篇突破 O(N^2)：希尔排序](https://labuladong.online/zh/algo/data-structure-basic/shell-sort/)[下一篇妙用二叉树后序位置：归并排序](https://labuladong.online/zh/algo/data-structure-basic/merge-sort/)

---

### 46. 二叉堆结构的运用：堆排序

原文链接: <https://labuladong.online/zh/algo/data-structure-basic/heap-sort/>

读完本文，你不仅学会了算法套路，还可以顺便解决如下题目：

| LeetCode | 力扣 | 难度 |
| --- | --- | --- |
| [912. Sort an Array](https://leetcode.com/problems/sort-an-array/) | [912. 排序数组](https://leetcode.cn/problems/sort-an-array/) |  |

前置知识

阅读本文前，你需要先学习：

- [二叉堆基础](https://labuladong.online/zh/algo/data-structure-basic/binary-heap-basic/)
- [二叉堆实现优先级队列](https://labuladong.online/zh/algo/data-structure-basic/binary-heap-implement/)

一句话总结

堆排序是从 [二叉堆结构](https://labuladong.online/zh/algo/data-structure-basic/binary-heap-basic/) 衍生出来的排序算法，复杂度为 O(Nlog⁡N)O(N \log N)O(NlogN)。堆排序主要分两步，第一步是在待排序数组上原地创建二叉堆（Heapify），然后进行原地排序（Sort）。

你可以打开下方可视化面板，点击跳转到 `let heap = ...` 这部分代码可以看到数组被抽象成完全二叉树；不断点击 `Heap.swim` 这部分代码，可以看到原地建堆的过程；点击 `Heap.sink` 这部分代码，可以看到原地排序的过程。

学习堆排序算法**必须**掌握二叉堆结构原理，否则可能完全无法理解排序过程。

算法可视化

前文 [二叉堆基础](https://labuladong.online/zh/algo/data-structure-basic/binary-heap-basic/) 介绍过二叉堆结构，[二叉堆实现优先级队列](https://labuladong.online/zh/algo/data-structure-basic/binary-heap-implement/) 利用二叉堆结构实现了一个 `SimpleMinPQ` 优先级队列，插入队列的元素会按照从小到大的顺序取出。

本文将介绍堆排序算法，它是基于二叉堆性质衍生出来的一种全新排序算法，非常优雅和高效。

首先，我要复述一下二叉堆实现优先级队列的几个关键原理，**如果你有任何不理解的地方，务必回去复习前文，否则无法理解堆排序**。

1、二叉堆（优先级队列）底层是用数组实现的，但是逻辑上是一棵完全二叉树，主要依靠 `swim, sink` 方法来维护堆的性质。

2、优先级队列可以分为小顶堆和大顶堆，小顶堆会将整个堆中最小的元素维护在堆顶，大顶堆会将整个堆中最大的元素维护在堆顶。

3、优先级队列插入元素时，首先把元素追加到二叉堆底部，然后调用 `swim` 方法把该元素上浮到合适的位置，时间复杂度是 O(log⁡N)O(\log N)O(logN)。

4、优先级队列删除堆顶元素时，首先把堆底的最后一个元素交换到堆顶作为新的堆顶元素，然后调用 `sink` 方法把这个新的堆顶元素下沉到合适的位置，时间复杂度是 O(log⁡N)O(\log N)O(logN)。

那么最简单的堆排序算法思路就是直接利用优先级队列，把所有元素塞到优先级队列里面，然后再取出来，不就完成排序了吗？

```java
// 直接利用优先级队列对数组从小到大排序
void sort(int[] nums) {
    // 创建一个从小到大排序元素的小顶堆
    SimpleMinPQ pq = new SimpleMinPQ(nums.length);
    // 先把所有元素插入到优先级队列中
    for (int num : nums) {
        // push 操作会自动构建二叉堆，时间复杂度为 O(logN)
        pq.push(num);
    }
    // 再把所有元素取出来，就是从小到大排序的结果
    for (int i = 0; i < nums.length; i++) {
        // pop 操作从堆顶弹出二叉堆堆中最小的元素，时间复杂度为 O(logN)
        nums[i] = pq.pop();
    }
}
```

因为优先级队列的 `push, pop` 方法的复杂度都是 O(log⁡N)O(\log N)O(logN)，所以整个排序的时间复杂度是 O(Nlog⁡N)O(N \log N)O(NlogN)，其中 `N` 是输入数组的长度。

这个思路可以得到正确的排序结果，但空间复杂度是 O(N)O(N)O(N)，因为我们创建的这个优先级队列是一个额外的数据结构，它的底层使用了一个数组来存储元素。

所以，堆排序要解决的问题是，**不要使用额外的辅助空间，直接在原数组上进行 `sink, swim` 操作**，在 O(Nlog⁡N)O(N \log N)O(NlogN) 的时间内完成排序。

堆排序的两个关键步骤

1、原地建堆（Heapify）：直接把待排序数组原地变成一个二叉堆。

2、排序（Sort）：将元素不断地从堆中取出，最终得到有序的结果。

你不妨自己思考几分钟，对比一下优先级队列增删元素的过程，其实利用 `swim, sink` 方法原地实现这两步并不难，应该可以独立思考出来。

在具体讲解堆排序代码实现之前，我先把二叉堆的 `swim, sink` 方法和配套的工具函数写出来，因为后文我会带你逐步优化堆排序的代码，就不重复实现这些函数了。

这些函数就是从 [二叉堆实现优先级队列](https://labuladong.online/zh/algo/data-structure-basic/binary-heap-implement/) 中的优先级队列实现里抠出来的，把数组作为函数参数传入，其他的逻辑完全一样：

[上一篇妙用二叉树后序位置：归并排序](https://labuladong.online/zh/algo/data-structure-basic/merge-sort/)[下一篇全新的排序原理：计数排序](https://labuladong.online/zh/algo/data-structure-basic/counting-sort/)

---

### 47. 突破 O(N^2)：希尔排序

原文链接: <https://labuladong.online/zh/algo/data-structure-basic/shell-sort/>

读完本文，你不仅学会了算法套路，还可以顺便解决如下题目：

| LeetCode | 力扣 | 难度 |
| --- | --- | --- |
| [912. Sort an Array](https://leetcode.com/problems/sort-an-array/) | [912. 排序数组](https://leetcode.cn/problems/sort-an-array/) |  |

前置知识

阅读本文前，你需要先学习：

- [选择排序所面临的问题](https://labuladong.online/zh/algo/data-structure-basic/select-sort/)
- [运用逆向思维：插入排序](https://labuladong.online/zh/algo/data-structure-basic/insertion-sort/)

一句话总结

希尔排序是基于 [插入排序](https://labuladong.online/zh/algo/data-structure-basic/insertion-sort/) 的简单改进，通过预处理增加数组的局部有序性，突破了插入排序的 O(N2)O(N^2)O(N2) 时间复杂度。

你可以点开可视化面板，点击播放按钮，然后点击加速/减速按钮调节速度，即可直观感受希尔排序的过程：

算法可视化

必须承认，希尔排序的思路很难想到，我是在《算法 4》第一次了解到这个算法，然后惊叹于这个算法的简单优化竟然能给插入排序带来如此大的提升。

首先我们要明确一个 **`h` 有序数组** 的概念。

## h 有序数组

一个数组是 `h` 有序的，是指这个数组中任意间隔为 `h`（或者说间隔元素的个数为 `h-1`）的元素都是有序的。

这个概念用文字不好描述清楚，直接看个例子吧。比方说 `h=3` 时，一个 `3` 有序数组是这样的：

[上一篇运用逆向思维：插入排序](https://labuladong.online/zh/algo/data-structure-basic/insertion-sort/)[下一篇妙用二叉树前序位置：快速排序](https://labuladong.online/zh/algo/data-structure-basic/quick-sort/)

---

### 48. 全新的排序原理：计数排序

原文链接: <https://labuladong.online/zh/algo/data-structure-basic/counting-sort/>

读完本文，你不仅学会了算法套路，还可以顺便解决如下题目：

| LeetCode | 力扣 | 难度 |
| --- | --- | --- |
| [75. Sort Colors](https://leetcode.com/problems/sort-colors/) | [75. 颜色分类](https://leetcode.cn/problems/sort-colors/) |  |
| [912. Sort an Array](https://leetcode.com/problems/sort-an-array/) | [912. 排序数组](https://leetcode.cn/problems/sort-an-array/) |  |

前置知识

阅读本文前，你需要先学习：

- [排序算法的关键指标](https://labuladong.online/zh/algo/data-structure-basic/sort-basic/)
- [选择排序所面临的问题](https://labuladong.online/zh/algo/data-structure-basic/select-sort/)

一句话总结

计数排序的原理比较简单：统计每种元素出现的次数，进而推算出每个元素在排序后数组中的索引位置，最终完成排序。

计数排序的时间和空间复杂度都是 O(n+max−min)O(n + max - min)O(n+max−min)，其中 nnn 是待排序数组长度，max−minmax - minmax−min 是待排序数组的元素范围。

这是计数排序的可视化面板，你可以点击 `sorted[count[index] - 1] = nums[i]` 这部分代码，即可看到有序数组形成的过程：

算法可视化

比方说，输入一个 `nums` 数组，我统计出其中有 2 个元素 `1`，1 个元素 `3`，3 个元素 `6`，那么只要我在数组中依次填入 2 个 `1`，1 个 `3`，3 个 `6`，就能得到排序结果 `[1, 1, 3, 6, 6, 6]`。

我们做一道简单的题目就能明白了，来看力扣第 75 题「[颜色分类](https://leetcode.cn/problems/sort-colors/)」：

**75. 颜色分类**|[力扣](https://leetcode.cn/problems/sort-colors/)|[LeetCode](https://leetcode.com/problems/sort-colors/)

给定一个包含红色、白色和蓝色、共 `n`* *个元素的数组 `nums` ，**[原地](https://baike.baidu.com/item/%E5%8E%9F%E5%9C%B0%E7%AE%97%E6%B3%95) **对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

我们使用整数 `0`、 `1` 和 `2` 分别表示红色、白色和蓝色。

必须在不使用库内置的 sort 函数的情况下解决这个问题。

**示例 1：**

```text

输入：nums = [2,0,2,1,1,0]
输出：[0,0,1,1,2,2]
```

**示例 2：**

```text

输入：nums = [2,0,1]
输出：[0,1,2]
```

**提示：**

- `n == nums.length`
- `1 <= n <= 300`
- `nums[i]` 为 `0`、`1` 或 `2`

**进阶：**

- 你能想出一个仅使用常数空间的一趟扫描算法吗？

题目来源：[力扣 75. 颜色分类](https://leetcode.cn/problems/sort-colors/)。

这道题有多种思路，最优解法是用双指针技巧仅遍历一次数组完成排序，我会在 [数组双指针技巧习题](https://labuladong.online/zh/algo/problem-set/array-two-pointers/) 中介绍。这里我们用计数排序的思路来解决这个问题，说白了就是让你对数组排序，且这个数组里只有 0、1、2 三种元素。

我们可以创建一个大小为 3 的 `count` 数组，`count[0], count[1], count[2]` 分别表示数组中 0、1、2 出现的次数。然后我们按照 `count` 数组的统计结果，依次填充原数组即可。

```java
class Solution {
    public void sortColors(int[] nums) {
        // 统计 0, 1, 2 出现的次数
        int[] count = new int[3];
        for (int element : nums) {
            count[element]++;
        }

        // 按照 count 数组的统计结果，依次填充原数组
        int index = 0;
        for (int element = 0; element < 3; element++) {
            for (int i = 0; i < count[element]; i++) {
                nums[index] = element;
                index++;
            }
        }
    }
}
```

这就是一个简单的计数排序算法，不过这个题目给的场景比较简单，只有 `0, 1, 2` 三种元素，下面我们给出一个更通用的计数排序算法。

## 通用的计数排序

虽然计数排序的原理简单，但是在通用的计数排序代码中，还是有一些编码技巧的。

我们从提出问题开始。计数排序需要把数组中的元素作为 `count` 数组的索引才能计数，那么我们可以提出如下疑问：

1、是不是说只有当 `nums` 数组中的元素都是非负整数的时候才能用计数排序呢？包含负数时如何排序？对自定义的类型如何排序？

2、根据计数排序的原理，我们仅关心某一个元素出现了多少次，而并不关心相同元素的相对位置，那么看起来计数排序是一个不稳定排序，对吗？

3、因为计数排序需要将元素的值作为 `count` 数组的索引，那么如果数组中的最大元素的值很大时，会不会导致 `count` 数组太大，空间复杂度过高？

下面我们来一步一步思考这些问题，尝试给出解法。

[上一篇二叉堆结构的运用：堆排序](https://labuladong.online/zh/algo/data-structure-basic/heap-sort/)[下一篇博采众长：桶排序](https://labuladong.online/zh/algo/data-structure-basic/bucket-sort/)

---

### 49. 博采众长：桶排序

原文链接: <https://labuladong.online/zh/algo/data-structure-basic/bucket-sort/>

读完本文，你不仅学会了算法套路，还可以顺便解决如下题目：

| LeetCode | 力扣 | 难度 |
| --- | --- | --- |
| [912. Sort an Array](https://leetcode.com/problems/sort-an-array/) | [912. 排序数组](https://leetcode.cn/problems/sort-an-array/) |  |

前置知识

阅读本文前，你需要先学习：

- [计数排序](https://labuladong.online/zh/algo/data-structure-basic/counting-sort/)

一句话总结

桶排序算法的核心思想分三步：

1、将待排序数组中的元素使用映射函数分配到若干个「桶」中。

2、对每个桶中的元素进行排序。

3、最后将这些排好序的桶进行合并，得到排序结果。

打开下面的可视化面板，多次点击 `buckets[index].push(num)` 这行代码，即可看到元素分配到不同桶中的过程；多次点击 `insertSort(curBucket)` 这一行代码，即可看到对每个桶进行排序的过程；多次点击 `nums[index++] = num` 这行代码，即可看到合并有序桶的过程。

算法可视化

桶排序算法可能并不常见，但我个人感觉它的思想非常有意思，因为你可以在它的算法思想中同时看到前面讲的 [归并排序](https://labuladong.online/zh/algo/data-structure-basic/merge-sort/) 和 [计数排序](https://labuladong.online/zh/algo/data-structure-basic/counting-sort/) 的影子。

如果你按顺序学习了前面的所有算法，就会感慨这些算法之间千丝万缕的联系。看看这一代代计算机大佬，就为了「排序」这一个需求，真所谓八仙过海各显神通，精妙的想法层出不穷，我们作为后辈，何不好好品味一下呢？

## 桶排序的关键点

言归正传，桶排序的思路真的很简单，就是先把待排序数组中的元素分配到若干个桶中，对每个桶中的元素分别进行排序，最后再把这些桶中的元素按顺序合并起来。

这个思路是不是有点像 [归并排序](https://labuladong.online/zh/algo/data-structure-basic/merge-sort/)？都是把大的数组分成小的数组进行排序，最后再合并起来。不过桶排序更加灵活，三个核心步骤中每一步都可以变化：

1、如何将待排序元素分配到桶中？你需要决定桶的数量，并提供一个映射函数。

2、如何对每个桶中的元素进行排序？理论上可以使用任意排序算法，或者模拟 [归并排序](https://labuladong.online/zh/algo/data-structure-basic/merge-sort/) 的思路，对每个桶递归地运行桶排序。

3、如何将排好序的桶合并起来？后面的章节会讲 [合并多个有序链表/数组](https://labuladong.online/zh/algo/essential-technique/array-two-pointers-summary/) 的通用算法，但那个算法会用到 [二叉堆结构](https://labuladong.online/zh/algo/data-structure-basic/binary-heap-basic/)，且复杂度为 O(n∗logk)O(n*logk)O(n∗logk)，这里显然不适用：

如果我都用上二叉堆了，还搞什么桶排序，直接上 [堆排序](https://labuladong.online/zh/algo/data-structure-basic/heap-sort/) 不就完事了，是吧？所以这一步合并操作的时间复杂度不能超过 O(n)O(n)O(n)，要做到这一点，就要合理设计分配元素的映射函数。

关于这三个问题，我想首先探讨其中第二个问题。不知道你有没有想过，**为什么要把待排序数组分成若干个桶，然后再对每个桶进行排序？这样排序，和直接对整个待排序数组排序相比，真的有区别吗**？

答案是，如果暂时不考虑合并有序桶的算法复杂度，那么分开排序当然要比整体排序效率高。

分开排序 vs 整体排序

以最简单的 [选择排序](https://labuladong.online/zh/algo/data-structure-basic/select-sort/) 为例，如果我直接对大小为 nnn 的数组进行选择排序，那么时间复杂度是 O(n2)O(n^2)O(n2)。

假设我们将待排序数组分成 kkk 个桶，对于每个桶使用选择排序，那么总的时间复杂度是大于 O(n2)O(n^2)O(n2)，还是小于 O(n2)O(n^2)O(n2)？

这其实是一个简单的数学题，假设有个正整数 nnn，且它可以分解为 n=n1+n2+⋯+nkn = n_1 + n_2 + \cdots + n_kn=n1​+n2​+⋯+nk​，那么 n2n^2n2 和 n12+n22+⋯+nk2n_1^2 + n_2^2 + \cdots + n_k^2n12​+n22​+⋯+nk2​ 哪个更大？

有多种思路可以得到答案，我们来看这种几何的思路：

把这个 n2n^2n2 想象成一个正方形的面积，而 n12+n22+⋯+nk2n_1^2 + n_2^2 + \cdots + n_k^2n12​+n22​+⋯+nk2​ 是这个大正方形的一条边上的若干小正方形的面积之和，这样就能直观的理解了，显然这些小正方形的面积没有整个正方形的面积大，所以 n2>=n12+n22+⋯+nk2n^2 >= n_1^2 + n_2^2 + \cdots + n_k^2n2>=n12​+n22​+⋯+nk2​。

**由此可知，分开排序的时间复杂度总和是小于整体排序的**，这就是保证桶排序算法的数学基础。

基于正方形面积的这个抽象，我们还可以更进一步。当 kkk 无限大，n1,n2,⋯ ,nkn_1, n_2, \cdots, n_kn1​,n2​,⋯,nk​ 无限小时会怎样？

正方形那条边上的小正方形面值之和越来越小，最终会和那条边融为一体，也就是说 n12+n22+⋯+nk2n_1^2 + n_2^2 + \cdots + n_k^2n12​+n22​+⋯+nk2​ 的值会无限接近 nnn。

**以此观之，如果桶排序将待排序元素分配到尽可能多的桶中（kkk 尽可能大），即每个桶至多只有一个元素时，桶排序就转化成了 [计数排序](https://labuladong.online/zh/algo/data-structure-basic/counting-sort/)，其复杂度也将降低到 O(n)O(n)O(n)**。

即便不能做到每个桶只有一个元素，只要 k>1k > 1k>1，桶排序的时间复杂度也会小于 O(n2)O(n^2)O(n2)，kkk 越大，时间复杂度越接近 O(n)O(n)O(n)。

反过来，如果取最小值 k=1k = 1k=1，那桶排序就完全退化成了选择排序，时间复杂度是 O(n2)O(n^2)O(n2)。

当然，上述分析都没有考虑合并有序桶的时间复杂度，不过只要能在 O(n)O(n)O(n) 的时间内进行合并，那么桶排序的总时间复杂度依然是小于 O(n2)O(n^2)O(n2) 的。

下面我将来探讨如何把待排序元素分配到桶中，以及如何合并有序桶，最后给出桶排序的几种代码实现。

[上一篇全新的排序原理：计数排序](https://labuladong.online/zh/algo/data-structure-basic/counting-sort/)[下一篇基数排序（Radix Sort）](https://labuladong.online/zh/algo/data-structure-basic/radix-sort/)

---

### 50. 基数排序（Radix Sort）

原文链接: <https://labuladong.online/zh/algo/data-structure-basic/radix-sort/>

读完本文，你不仅学会了算法套路，还可以顺便解决如下题目：

| LeetCode | 力扣 | 难度 |
| --- | --- | --- |
| [912. Sort an Array](https://leetcode.com/problems/sort-an-array/) | [912. 排序数组](https://leetcode.cn/problems/sort-an-array/) |  |

前置知识

阅读本文前，你需要先学习：

- [排序算法的关键指标](https://labuladong.online/zh/algo/data-structure-basic/sort-basic/)
- [计数排序](https://labuladong.online/zh/algo/data-structure-basic/counting-sort/)

一句话总结

基数排序是 [计数排序](https://labuladong.online/zh/algo/data-structure-basic/counting-sort/) 算法的扩展，它的主要思路是对待排序元素的每一位依次进行计数排序。由于计数排序是稳定的，所以对每一位完成计数排序后，所有元素就完成了排序。

点击 `let maxLen = 0` 这一行代码，可以看到算法将数组元素都转化为了非负数；多次点击 `countSort(nums, k)` 这一行代码，对每一位执行计数排序；最后点击 `nums[i] -= offset` 这一行代码，将数组元素转化回原来的值，完成排序：

算法可视化

首先解释一下基数排序（Radix Sort）这个名词。

基数（Radix）其实就是进制的意思，比如十进制数的基数就是 10，二进制数的基数就是 2。看这个名字就知道这个排序算法肯定和数字的进制有关，进而可以推断，这个算法不是通用排序算法，待排序数据必须是整数，或者能够通过某种规则转化成整数，才能使用基数排序。

我发现网上的很多资料会把基数排序和桶排序放在一起，认为基数排序是桶排序的应用。

但我不认同这种看法，我认为基数排序是计数排序的扩展，可以用来解决计数排序空间复杂度过高的问题，和桶排序关系不大。

现在你已经学习过 [计数排序](https://labuladong.online/zh/algo/data-structure-basic/counting-sort/) 和 [桶排序](https://labuladong.online/zh/algo/data-structure-basic/bucket-sort/) 了，在我介绍了基数排序的原理后，你也可以自己思考一下，它是到底是计数排序的扩展还是桶排序的扩展。

## 基数排序的原理

基数排序的原理很简单，比方说输入的数组都是三位数 `nums = [329, 457, 839, 439, 720, 355, 350]`，我们先按照个位数排序，然后按照十位数排序，然后按照百位数排序，最终就完成了整个数组的排序。

**这里面的关键在于，对每一位的排序都必须是稳定排序，否则最终结果就不对了**。

用这个 `nums` 数组为例，演示一下基数排序的过程，我把每个数字竖着写，方便查看每一位的排序效果。

首先是初始状态：

```text
329
457
839
439
720
355
350
```

按照个位数进行稳定排序，得到：

```text
720
350
355
457
329
839
439
  ^
```

再按照十位数进行稳定排序，得到：

```text
720
329
839
439
350
355
457
 ^
```

最后按照百位数进行稳定排序，得到：

```text
329
350
355
439
457
720
839
^
```

上面就是基数排序的过程，在给出解法代码之前，先解答一些关于基数排序的问题：

1、为什么对每一位必须使用稳定排序？

2、使用什么稳定排序比较好，为什么？

3、如果待排序数组中的数字不全是三位数，怎么办？有负数怎么办？

4、必须按照从个位数到高位数的顺序进行排序吗？是否可以反过来，从高位数到个位数进行排序？

### 为什么对每一位必须使用稳定排序

举个很简单的例子：

```text
56
57
```

个位数已经排好序了，现在要对十位数排序。

十位数都是 5，稳定排序可以保证这两个 5 的顺序不变，最终的结果就是正确的；而如果使用不稳定排序，这两个 5 的顺序就可能被打乱，最终的结果就不对了。

[上一篇博采众长：桶排序](https://labuladong.online/zh/algo/data-structure-basic/bucket-sort/)[下一篇正在更新 ing](https://labuladong.online/zh/algo/intro/updating-3/)

---

## 13. 补充:哈夫曼树

### 51. 数据压缩和霍夫曼树

原文链接: <https://labuladong.online/zh/algo/data-structure-basic/huffman-tree/>

前置知识

阅读本文前，你需要先学习：

- [二叉树基础及常见类型](https://labuladong.online/zh/algo/data-structure-basic/binary-tree-basic/)

一句话总结

霍夫曼树是二叉树结构的经典应用，它是一种最优前缀编码树，常用于数据压缩。

本文会介绍霍夫曼编码的原理，并对比几种常见的数据压缩思路。

具体的代码实现会放到数据结构设计章节中，带你基于霍夫曼编码实现一个压缩程序。

## 浅谈数据压缩

我们可以把数据压缩算法分为两大类，分别是 **无损压缩** 和 **有损压缩**。

**无损压缩** 是指压缩后的数据可以完全还原，不会丢失任何信息。

比如我们把若干文件打包成一个 zip 压缩包，这个 zip 所需的磁盘空间会更小，且解压后可以完全还原原始文件，这就叫无损压缩。

**有损压缩** 是指压缩后的数据会丢失一些信息，但是压缩率更高（即压缩后的数据占用空间更小）。

比如我们经常会有图片压缩的需求，有些图像处理工具能够在不明显影响图片质量的前提下，显著降低图片的磁盘占用空间，这就是有损压缩。

那么我们来思考几个问题。

1、有损压缩是怎么做到在丢失信息的前提下，依然保证图片质量的呢？

2、有损压缩会丢失一些信息，换取空间的减少，这个可以理解。但无损压缩是怎么做到不丢失任何信息的前提下，压缩数据的呢？

首先，有损压缩肯定是会降低图片质量的，只不过这个降低的程度在我们的可接受范围内。

还是以图片压缩为例，人眼对「亮度」比较敏感，对「色度」不敏感。那么我们就可以用低精度的数据类型来表示「色度」，这样即便丢失了一些「色度」的信息，也几乎看不出区别。

但无损压缩不能这么搞，因为它要保证压缩后的数据可以再完全还原，所以**无损压缩的本质就是编码和解码**。

举个简单的例子，`hahahahahahaha` 这个字符串，我可以编码为 `ha*7`，解码时只需要把 `ha` 重复 7 次，就可以还原出原始字符串。

**无损压缩的效果取决于压缩算法是否能够充分挖掘出原始数据中的冗余信息**。

越是通用的压缩算法，能够挖掘出的冗余信息就越少，压缩率就越低；越是专用的压缩算法，能够挖掘出的冗余信息就越多，压缩率就越高。

比方说音频文件包含声波信息，专业的音频压缩算法能够找到声波信息中的冗余进行压缩，效果就好；而通用的 zip 压缩算法将音频文件也视为普通的字节流，无法挖掘声波信息的冗余，压缩效果自然就差。

所以没有全能的压缩算法，只能在通用性、压缩率和性能之间进行权衡。

本文讲解的霍夫曼编码，就是一种通用无损压缩算法，将原始数据输入霍夫曼算法，会得到压缩后的数据和一个码表，解码时需要根据码表还原出原始数据。

## 定长编码 vs 变长编码

既然说到了编码和解码，就不得不聊一聊定长编码（fixed-length encoding）和变长编码（variable-length encoding）。

ASCII 编码是一种定长编码，它将每个字符编码为 8 位二进制数，即一个字节。

UTF-8 编码是一种变长编码，它将每个字符编码为 1 到 4 个字节。

**定长编码最大的优势是可以「随机访问」**，因为每个字符的编码长度都是固定的，所以可以很容易地根据索引计算出字符的位置。

**变长编码的优势是存储效率高**，比如 UTF-8 编码就是一种变长编码，存储英文字符时占用一个字节，存储中文时占用三个字节，通用性和存储效率都比 ASCII 编码强。但由于每个字符的编码长度不固定，无法通过索引进行「随机访问」。

到这里不妨思考一下，现代编辑器基本都是用 UTF-8 编码了，而对字符串进行随机访问又是编辑器的基本功能，如果每次访问都要线性扫描，显然效率很差，那么编辑器是怎么解决这个问题的呢？

回到数据压缩的场景，比方说 `aaabacc` 这个字符串有 7 个小写字母，用 ASCII 编码需要 7x8=56 bit，我现在想对它进一步压缩，应该怎么做？

因为现在只有 `a,b,c` 三种字符，所以其实不需要用 8 比特来表示每个字符，用 2 比特就够了。

比方说这样编码：

- `a` 编码为 `00`
- `b` 编码为 `01`
- `c` 编码为 `10`

那么 `aaabacc` 就可以编码为二进制的 `00000001001010`，长度为 14 比特。

这种编码方式就叫 **定长编码**，因为每个字符的编码长度都固定为 2 比特。

定长编码的好处是简单，只需要知道所有可能的字符种类，就可以确定编码了。不过定长编码的压缩效果并不是很好，因为没有充分利用字符出现的频率信息。

比方说还以 `aaabacc` 为例，既然字符 `a` 出现的频率较高，`b,c` 出现的频率低，那么能否使用更短的编码来表示 `a`，让 `b,c` 使用更长的编码呢？

其实是可以的，这就叫 **变长编码**。比如这样编码：

- `a` 编码为 `0`
- `b` 编码为 `10`
- `c` 编码为 `11`

那么 `aaabacc` 就可以编码为二进制的 `0001001111`，长度为 10 比特，比定长编码的压缩效果更好。

## 变长编码的难点

两个难点

1、如何设计编码才能保证解码的唯一性？

2、如何保证压缩率（编码数据尽可能短）？

3、如何保证解码的效率？

我们仔细分析一下上面 `aaabacc` 的例子。

这种编码方案是没有歧义的：

- `a` 编码为 `0`
- `b` 编码为 `10`
- `c` 编码为 `11`

如果把 `a` 编码为 `1`，那么编码方案中 `a` 和 `c` 的编码存在歧义：

- `a` 编码为 `1`
- `b` 编码为 `10`
- `c` 编码为 `11`

`aaabacc` 会被编码为二进制的 `11111011111`，但是 `a` 和 `c` 的编码存在歧义，`11` 既可以解码为 `c`，也可以解码为 `aa`，所以无法解码出原始数据。

对比上面两个例子可以发现一些规律：**任意一个编码，都不能是另一个编码的前缀**。

比如第二个例子中， `a` 编码为 `1`，而 `b, c` 编码的前缀都是 `1`，所以编码方案有歧义。

那么可能有读者会反驳，比如下面这个编码方案：

- `a` 编码为 `1`
- `b` 编码为 `10`
- `c` 编码为 `100`

虽然出现了相同的前缀，但是我们可以在解码时添加额外的比较逻辑：

读取到 `1` 时，继续向后探测两位，看看是否可能凑出 `10` 或 `100`，进而决定如何解码。

这样确实可以保证解码唯一性，**但是压缩率低，且解码效率差**。向后匹配的逻辑相当于嵌套 for 循环：

```text
for (int i = 0; i < N; i++) {
    for (int j = 1; j <= K; j++) {
        ...
    }
}
```

假设最长的编码长度为 KKK，编码后的数据长度为 NNN，那么解码的时间复杂度 O(NK)O(NK)O(NK)。

如果你能保证任意一个编码都不是另一个编码的前缀，那么就不需要尝试向后匹配了。这样一来，解码的复杂度就降到了 O(N)O(N)O(N)。

在实际的编解码场景中 NNN 往往很大，即便 KKK 较小，解码速度慢几倍也是非常糟糕的，所以我们需要保证编解码算法的时间复杂度为 O(N)O(N)O(N)，且压缩率尽可能高。

[上一篇线段树核心原理及可视化](https://labuladong.online/zh/algo/data-structure-basic/segment-tree-basic/)[下一篇图论中的基本术语](https://labuladong.online/zh/algo/data-structure-basic/graph-terminology/)

---
