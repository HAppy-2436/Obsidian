# 数据结构与算法 — 全部 Lab 题汇总（客观版）
> 🤖 自动生成于 2026-06-24 22:56（纯客观统计，不含完成状态）  
> 📚 来源：CStudyasst (mynereus.com)  
> 🏫 班级：**数据结构与算法** (ID: `o389JgRM`)  
> 👩‍🏫 教师：王丽苹  
> 📅 学期：2025-2026 学年第 2学期

## 总体概览
| 指标 | 数值 |
|------|------|
| Lab 总数 | 25 |
| 题目总数 | 51 |
| 满分总和 | 2500 |
| 平均每题满分 | 49.0 |

## 按知识点分布
| 知识点 | Lab 数 | 题数 | 满分小计 |
|---|---:|---:|---:|
| 排序 | 3 | 9 | 300 |
| 单链表 | 2 | 6 | 200 |
| 栈 | 3 | 5 | 300 |
| 队列 | 2 | 4 | 200 |
| 递归 | 2 | 4 | 200 |
| 查找 | 2 | 4 | 200 |
| 二叉树 | 2 | 4 | 200 |
| 数组与游戏 | 2 | 3 | 200 |
| 链式结构（栈/队列） | 2 | 3 | 200 |
| 线性表（链式） | 1 | 3 | 100 |
| 哈希表 | 2 | 3 | 200 |
| 线性表（顺序） | 1 | 2 | 100 |
| 线性表应用（字符串） | 1 | 1 | 100 |

## 按难度分布
| 难度 | 题数 | 满分小计 |
|---|---:|---:|
| 简单 | 2 | 134 |
| 中等 | 38 | 1760 |
| 困难 | 11 | 606 |

## Lab 速查表
| # | Lab 名 | 知识点 | 截止时间 | 题目数 |
|---|---|---|---|---:|
| 01 | Lab01-第一章上机 | 数组与游戏 | 2026-03-09 22:00:00 | 2 |
| 02 | Lab02-栈及应用 | 栈 | 2026-03-16 22:00:00 | 3 |
| 03 | Lab03-队列 | 队列 | 2026-03-23 23:00:00 | 3 |
| 04 | Lab04-单链表基础 | 单链表 | 2026-05-21 00:00:00 | 5 |
| 05 | Lab05-课堂 | 链式结构（栈/队列） | 2026-04-24 12:00:00 | 1 |
| 06 | Lab05-链式结构及应用 | 链式结构（栈/队列） | 2026-04-24 12:00:00 | 2 |
| 07 | Lab06-递归 | 递归 | 2026-04-18 00:00:00 | 2 |
| 08 | Lab07-List上机练习1 | 线性表（顺序） | 2026-05-12 23:59:00 | 2 |
| 09 | Lab08-List上机2 | 线性表（链式） | 2026-04-27 23:00:00 | 3 |
| 10 | Lab09-List应用（字符串类） | 线性表应用（字符串） | 2026-05-12 23:59:00 | 1 |
| 11 | Lab10-查找 | 查找 | 2026-05-12 23:00:00 | 3 |
| 12 | Lab10-课堂二分查找的实现 | 查找 | 2026-05-12 23:59:00 | 1 |
| 13 | Lab11-排序算法1 | 排序 | 2026-05-19 21:00:00 | 3 |
| 14 | Lab11-课堂上机 | 排序 | 2026-05-19 21:00:00 | 1 |
| 15 | Lab12-排序算法2 | 排序 | 2026-05-26 23:00:00 | 5 |
| 16 | Lab13-Hash表上机实践 | 哈希表 | 2026-06-01 23:00:00 | 2 |
| 17 | Lab13-课堂作业 | 哈希表 | 2026-05-28 12:00:00 | 1 |
| 18 | Lab14-课后上机 | 二叉树 | 2026-06-10 12:00:00 | 3 |
| 19 | Lab14-课堂-二叉树的遍历 | 二叉树 | 2026-06-04 00:00:00 | 1 |
| 20 | 中序波兰式求解 | 栈 | 2026-05-21 00:00:00 | 1 |
| 21 | 二维Life Game | 数组与游戏 | 2026-03-05 12:00:00 | 1 |
| 22 | 单链表课堂练习 | 单链表 | 2026-03-26 23:00:00 | 1 |
| 23 | 栈课堂练习 | 栈 | 2026-03-12 12:00:00 | 1 |
| 24 | 课堂练习3-环形队列 | 队列 | 2026-03-19 12:00:00 | 1 |
| 25 | 递归课堂练习 | 递归 | 2026-04-18 00:00:00 | 2 |

---

## 题目详情（按 Lab）
## Lab01：Lab01-第一章上机

- **知识点**：数组与游戏
- **截止时间**：2026-03-09 22:00:00
- **题目数**：2

### 题目 1：One-Dimensional Life

- **难度**：中等　|　**满分**：50
- **questionId**：`136`
- **时间限制**：1000 ms　|　**内存限制**：128 MB

**题目描述：**

```
One-Dimensional Life takes place on a straight line instead of a rectangular grid. Each cell has four neighboring positions: those at distance one or two from it on each side. The rules are similar to those of two-dimensional Life except (1) a dead cell with either two or three living neighbors will become alive in the next generation, and (2) a living cell dies if it has zero, one, or three living neighbors. (Hence a dead cell with zero, one, or four living neighbors stays dead; a living cell with two or four living neighbors stays alive.) The progress of sample communities is shown in Figure 1.6(Textbook page44）. Design, write, and test a program for one-dimensional Life.
The total count of the cells is less than 60.

Input: the position of living cells (1<=postion<=60. Terminate the list with the special number -1). 
      The number (n) of generation. (n=0 means the initial Grid)
Output: the n-th generation of the grid.（仅需要输出第n代的结果）

For example：
【输入】
5 7 -1
1
【输出】
```
-----*------------------------------------------------------
```
```

---

### 题目 2：Magic Square

- **难度**：中等　|　**满分**：50
- **questionId**：`135`
- **时间限制**：1000 ms　|　**内存限制**：128 MB

**题目描述：**

```
A magic square is a square array or integers such that the sum of every row, the sum of every column, and sum of each of the two diagonals are all equal. 
Write a program that generates a magic square by the following method. This method works only when the size of the square is an odd number. Start by placing 1 in the middle of the top row. Write down successive integers 2, 3, … along a diagonal going upward and to the right. When you reach the top row(as you do immediately since 1 is in the top now), continue to the bottom row as though the bottom row were immediately above the top row. When you reach the rightmost column, continue to the leftmost column as though it were immediately to the right of the rightmost one. When you reach a position that is already occupied, instead drop straight down one position from the previous number to insert the new one. The 5*5 magic square constructed by this method is shown as follows.
17 24 1 8 15
23 5 7 14 16
4 6 13 20 22
10 12 19 21 3
11 18 25 2 9

【输入】奇数n，1<=n<=101.
【输出】$$n\times n$$的magic square.<font color=red>**(数字之间为两个空格，每行最后一个数字后面无空格。)**</font>

For example,
【输入】 5
【输出】
17&nbsp;&nbsp;24&nbsp;&nbsp;1&nbsp;&nbsp;8&nbsp;&nbsp;15
23&nbsp;&nbsp;5&nbsp;&nbsp;7&nbsp;&nbsp;14&nbsp;&nbsp;16
4&nbsp;&nbsp;6&nbsp;&nbsp;13&nbsp;&nbsp;20&nbsp;&nbsp;22
10&nbsp;&nbsp;12&nbsp;&nbsp;19&nbsp;&nbsp;21&nbsp;&nbsp;3
11&nbsp;&nbsp;18&nbsp;&nbsp;25&nbsp;&nbsp;2&nbsp;&nbsp;9
```

---

## Lab02：Lab02-栈及应用

- **知识点**：栈
- **截止时间**：2026-03-16 22:00:00
- **题目数**：3

### 题目 1：10以内的后序波兰式求解

- **难度**：中等　|　**满分**：33
- **questionId**：`139`
- **时间限制**：1000 ms　|　**内存限制**：128 MB

**题目描述：**

```
(10以内的后序波兰式求解) 请编写程序求解10以内的后序波兰式的值。
【输入】合法的10以内的后序波兰式
【输出】后序波兰式的值（按照整型计算的结果）
例如：
【输入】23+6\*
【输出】30
【输入】23+\* //非法的后序表达式
【输出】none //表示无对应结果
```

---

### 题目 2：出入栈序列判断

- **难度**：中等　|　**满分**：33
- **questionId**：`141`
- **时间限制**：1000 ms　|　**内存限制**：128 MB

**题目描述：**

```
假设以I和O分别表示入栈和出栈操作。栈的初态和终态均为空，入栈和出栈的操作序列可表示为仅由I和O组成的序列，可以操作的序列称为称为合法序列，否则称为非法序列。

例如：

A.IOIIOIOO 合法 B.IOOIOIIO 不合法 

C.IIIOIOIO 合法 D.IIIOOIOO 合法

请写出一个算法，判断所给的操作序列是否合法。若合法，返回true，否则返回false

【输入】n n条I和O组成的序列(序列长度<=80)

【输出】n条序列的判断结果（true或者false）

例如：

【输入】

3

IOIIOIOO

IOOIOIIO

IIIOIOIO



【输出】

true

false

true
```

---

### 题目 3：程序代码中的括号匹配

- **难度**：中等　|　**满分**：34
- **questionId**：`142`
- **时间限制**：1000 ms　|　**内存限制**：128 MB

**题目描述：**

```
（程序代码中的括号匹配）请编写程序对一段程序代码中的括号匹配情况进行判断。括号类型有(),[],{}三类，程序代码中可能包含注释,如多行注释/\* \*/和单行注释//，且注释内容不参与括号匹配情况的分析。
【输入】 若干行程序代码，代码长度小于1500个字符
【输出】 除去注释后的括号数量 括号是否匹配（yes/no）
例如：
【输入】
int Collatz(unsigned int n) {
    if(n==1) return 0;
    else if(n%2) return Collatz(n*3+1)+1;
    else return Collatz(n/2)+1;
}
【输出】12 yes

【输入】
float CalcPay( /\* [in] \*/  float  payRate,     // Employee's pay rate
              /\* [in] \*/  float  hours      // Hours worked
               ){     //return Wages earned（）
【输出】 3 no

【输入】"//" ()
【输出】2 yes
```

---

## Lab03：Lab03-队列

- **知识点**：队列
- **截止时间**：2026-03-23 23:00:00
- **题目数**：3

### 题目 1：字符串的平衡性分析

- **难度**：中等　|　**满分**：33
- **questionId**：`148`
- **时间限制**：1000 ms　|　**内存限制**：128 MB

**题目描述：**

```
（字符串的平衡性分析）P92 Programming Project 3.3

Write a program that will read one line of input from the terminal. The input is supposed to consist of two parts separated by a colon :. As its result, your program should produce a single character as follows:

N No colon on the line.

L The left part (before the colon) is longer than the right.

R The right part (after the colon) is longer than the left.

D The left and right parts have the same length but are different.

S The left and right parts are exactly the same.

Examples: 

Input            Output

Sample Sample      N

Left:Right         R

Sample:Sample      S

Dog:Cat            D

Rabbit:Dog         L

【输入】

字符串的数量n

第2到n+1行分别输入需要分析的字符串

【输出】

N条字符串的判断结果

例如：

【输入】

3

Sample Sample

Dog:Cat

Rabbit:Dog

【输出】

N

D

L
```

---

### 题目 2：双端队列

- **难度**：中等　|　**满分**：33
- **questionId**：`147`
- **时间限制**：1000 ms　|　**内存限制**：128 MB

**题目描述：**

```
（双端队列）The word deque (pronounced either “deck” or “DQ”) is a shortened form of double-ended queue and denotes a list in which entries can be added or removed from either the first or the last position of the list, but no changes can be made elsewhere in the list. Thus a deque is a generalization of both a stack and a queue. The fundamental operations on a deque are append_front, append_rear, serve_front, serve_rear, retrieve_front, and retrieve_rear.

参考：https://en.wikipedia.org/wiki/Double-ended_queue

请实现deque，并解决如下问题：

在许多应用类软件的开发中都需要有保存用户历史操作的功能，例如word需要存储用户的编辑操作历史，浏览器需要存储用户浏览网页的历史，搜索栏需要保存最近的搜索记录等。请编写程序存储用户最近的n条操作记录，并将其按照时间顺序（由近到远）输出。

【输入】

设置软件需要最大保留的历史操作条数n（1<=n<=50）

用户的历史操作序列（数值可能大于n）且操作序列用大写字母来表示。

【输出】最近的n条操作序列（若操作序列长度小于n，则全部输出）

例如：

【输入】

5

A B C D

【输出】

D C B A

【输入】

5

A B C D E F G

【输出】

G F E D C
```

---

### 题目 3：团队队列

- **难度**：中等　|　**满分**：34
- **questionId**：`150`
- **时间限制**：1000 ms　|　**内存限制**：128 MB

**题目描述：**

```
（团队队列）有t个团队的人正在排一个长队。每次新来一个人时，如果他有队友在排队，那么这个新人会插队到最后一个队友的身后。如果没有任何一个队友排队，则他会排到长队的队尾。输入要求支持如下指令：

ENQUEUE x y：x团队编号为y的人进入长队。

DEQUEUE：长队的队首出队。

STOP：停止模拟

对于每个DEQUEUE指令，输出出队的人的编号。

【输入】输入数据包含多个测试样例，输入的每个样例第一行为团队数t（1<=t<=10），团队编号为1…t，接着的每行输入操作指令。当输入指令为STOP时，结束该样例的模拟。当输入样例的团队数t为0时，结束输入，无需担心指令出错。

【输出】对于每一个测试样例，输出“Scenario #k”。接着，对每一条DEQUEUE指令，输出出队的人的编号。每个测试样例以一个空白行隔开（包括最后一个测试样例）

例如：

【输入】

2

ENQUEUE 1 101

ENQUEUE 2 201

ENQUEUE 1 102

ENQUEUE 2 202

ENQUEUE 1 103

ENQUEUE 2 203

DEQUEUE

DEQUEUE

DEQUEUE

DEQUEUE

DEQUEUE

DEQUEUE

STOP

2

ENQUEUE 1 101

ENQUEUE 2 201

ENQUEUE 1 102

ENQUEUE 1 103

ENQUEUE 1 104

ENQUEUE 1 105

DEQUEUE

DEQUEUE

ENQUEUE 2 202

ENQUEUE 2 203

DEQUEUE

DEQUEUE

DEQUEUE

DEQUEUE

STOP

0

【输出】

Scenario #1

101

102

103

201

202

203



Scenario #2

101

102

103

104

105

201
```

---

## Lab04：Lab04-单链表基础

- **知识点**：单链表
- **截止时间**：2026-05-21 00:00:00
- **题目数**：5

### 题目 1：单链表的指定值插入

- **难度**：困难　|　**满分**：20
- **questionId**：`153`
- **时间限制**：1000 ms　|　**内存限制**：128 MB

**题目描述：**

```
（单链表的指定值插入）请编写程序在单链表的值为x的元素之后均插入值为y的元素，并输出所有的插入位置。

【输入】第一行整数n(1<=n)

第二行为单链表中的n个整数

第三行 x（x在单链表中存在）y要插入的整数，x和y均为int类型，且不相等

【输出】y插入在单链表中的下标位置

例如：

【输入】

5

3 6 9 10 1

6 7   //在所有的数字6后面插入数字7

【输出】

2     //7插入后的位置

【输入】

5

3 6 9 6 1

6 7   //在所有的数字6后面插入数字7

【输出】

2 5   //7插入后的位置
```

---

### 题目 2：删除单链表的指定值

- **难度**：困难　|　**满分**：20
- **questionId**：`154`
- **时间限制**：1000 ms　|　**内存限制**：128 MB

**题目描述：**

```
（删除单链表的指定值）请编写程序删除单链表中所有值为x的元素。并输出删除x后的链表信息。

【输入】第一行整数n(1<=n)

第二行为单链表中的n个整数

第三行 x，x为int类型

【输出】删除x后的单链表信息

例如：

【输入】

6

3 6 9 10 6 1

6

【输出】

3 9 10 1
```

---

### 题目 3：约瑟夫问题

- **难度**：中等　|　**满分**：20
- **questionId**：`155`
- **时间限制**：1000 ms　|　**内存限制**：128 MB

**题目描述：**

```
（约瑟夫问题）n 个人围成一个圆圈，首先第1个人从1开始一个人一个人顺时针报数,  报到第m个人，令其出列。然后再从下一个人开始，从1顺时针报数，报到第m个人，再令其出列，…，如此下去,  直到圆圈中只剩一个人为止。此人即为优胜者。请用环形链表实现约瑟夫问题。

【输入】n(2<=n<=60) m(1<=m)

【输出】最后的胜利者编号（编号范围是1至n）

例如：

【输入】

8 3

【输出】

7
```

---

### 题目 4：链表置逆

- **难度**：中等　|　**满分**：20
- **questionId**：`156`
- **时间限制**：1000 ms　|　**内存限制**：128 MB

**题目描述：**

```
（链表置逆）设有一个表头指针为h的单链表。试设计一个算法，通过遍历一趟链表，将链表中所有结点的链接方向逆转。要求逆转结果链表的表头指针h指向原链表的最后一个结点。

【输入】第一行整数n(1<=n)

第二行为单链表中的n个整数

【输出】置逆后的单链表信息

例如：

【输入】

6

3 6 9 10 6 1

【输出】

1 6 10 9 6 3
```

---

### 题目 5：删除链表中的重复元素

- **难度**：中等　|　**满分**：20
- **questionId**：`157`
- **时间限制**：1000 ms　|　**内存限制**：128 MB

**题目描述：**

```
（删除链表中的重复元素）请编写程序删除链表中的多余节点，即：若链表中有多个节点具有相同的值，则只保留其中的一个节点即可，使得处理后的链表中的值各不相同。

【输入】第一行整数n(1<=n)

第二行为单链表中的n个整数

【输出】删除链表中的重复元素后的单链表信息

例如：

【输入】

9

3 6 9 10 6 1 3 10 6

【输出】

3 6 9 10 1
```

---

## Lab05：Lab05-课堂

- **知识点**：链式结构（栈/队列）
- **截止时间**：2026-04-24 12:00:00
- **题目数**：1

### 题目 1：链式存储的栈

- **难度**：困难　|　**满分**：100
- **questionId**：`158`
- **时间限制**：1000 ms　|　**内存限制**：128 MB

**题目描述：**

```
（链式存储的栈）请用链式存储实现栈的数据结构MLinkedStack。你所实现的栈应包括：pop，push，top，size，clear，full等功能。利用你实现的Stack实现输入数字的逆序输出。

【输入】整数序列以-1结束，序列长度小于100

【输出】输入整数序列的逆序序列

例如：

【输入】3 9 8 2 5 -1 

【输出】5 2 8 9 3
```

---

## Lab06：Lab05-链式结构及应用

- **知识点**：链式结构（栈/队列）
- **截止时间**：2026-04-24 12:00:00
- **题目数**：2

### 题目 1：链式存储的队列

- **难度**：困难　|　**满分**：50
- **questionId**：`159`
- **时间限制**：1000 ms　|　**内存限制**：128 MB

**题目描述：**

```
（链式存储的队列）请用链式存储实现队列的数据结构MyLinkedQueue。你所实现的队列应包括：出队、入队、访问队首、判断队列是否已满，判断队列是否为空等功能。利用你实现的MyLinkedQueue实现输入整数序列的顺序输出。

【输入】整数序列以-1结束，序列长度小于100

【输出】输入整数序列的顺序序列

例如：

【输入】3 9 8 2 5 -1 

【输出】3 9 8 2 5
```

---

### 题目 2：多项式的运算

- **难度**：中等　|　**满分**：50
- **questionId**：`160`
- **时间限制**：1000 ms　|　**内存限制**：128 MB

**题目描述：**

```
（多项式的运算）请编写程序实现多项式的加法、减法、乘法（选做）的运算。

【输入】第一行运算符c（c可能为+，-， *）

第二行，运算符c的第一个多项式。多项式每一项的系数和指数，且按照指数的降序排列，输入0 0表示结束。

第三行，运算符c的第二个多项式。多项式每一项的系数和指数，且按照指数的降序排列，输入0 0表示结束。

其中，输入多项式每一项的系数与指数均为整数，指数非负且系数不为0。

【输出】多项式运算后的结果。用^表示指数项，例如5X2的正确输出为5X^2。

例如：

【输入】

+

3 5 6 2 12 0 0 0  //表示：3X^5+6X^2+12

7 2 1 1 0 0       //表示：7X^2+X

【输出】

3X^5+13X^2+X+12



【输入】

+

7 14 2 8 -10 6 1 0 0 0  //表示：7X^14+2X^8-10X^6+1

4 18 8 14 -3 10 10 6 -1 4 0 0  //表示：4X^18+8X^14-3X^10+10X^6-X^4

【输出】

4X^18+15X^14-3X^10+2X^8-X^4+1



注意：乘法运算为选做功能，测试用例中包含有1/3的乘法运算符，若不支持乘法运算则将会有6个用例不能通过测试。
```

---

## Lab07：Lab06-递归

- **知识点**：递归
- **截止时间**：2026-04-18 00:00:00
- **题目数**：2

### 题目 1：n个数的全排列

- **难度**：中等　|　**满分**：50
- **questionId**：`163`
- **时间限制**：1000 ms　|　**内存限制**：128 MB

**题目描述：**

```
给定整数n，n<=10，请求出n的全排列。

N=3时，1-3的排列可以为：

1:1 2 3

2:1 3 2

3:2 1 3

4:2 3 1

5:3 1 2

6:3 2 1

一共有6种情况

【输入】 整数n，n<=20

【输出】 

1-n的排列 （排列数大于10的，仅输出前10组即可）

总的全排列数

例如：

【输入】 4

【输出】 

1:1 2 3 4

2:1 2 4 3

3:1 3 2 4

4:1 3 4 2

5:1 4 2 3

6:1 4 3 2

7:2 1 3 4

8:2 1 4 3

9:2 3 1 4

10:2 3 4 1

24
```

---

### 题目 2：A Maze Problem

- **难度**：中等　|　**满分**：50
- **questionId**：`164`
- **时间限制**：1000 ms　|　**内存限制**：128 MB

**题目描述：**

```
A maze is to be represented by a 12*12 array composed of three values: Open, Wall, or Exit. There is one exit from the maze. Write a program to determine whether it is possible to exit the maze from the starting point (any open square can be a starting point). You may move vertically and horizontally to any adjacent open square(左右上下四个方向). You may not move to a square containing a wall. The input consists of a series of 12 lines of 12 characters each, representing the contents of each square in the maze. The characters are O, W, or E.

【输入】 12×12的迷宫方阵，每个格子的可能取值有：O, W, or E，输入数据能够确保迷宫只有一个出口。

任意3个起点的坐标,格式如下(x,y)。其中x为纵坐标，y为横坐标，起始坐标从左上角的格子开始，坐标起始值为0.

【输出】 

起点到出口的最短路径长度（经过多少个方格），若起点无法到达出口则输出-1。起始节点和结束节点都算入路径长度的计算。



例如：

【输入】 

O	W	O	W	O	W	O	O	W	O	W	O

O	W	O	W	W	W	W	O	W	O	O	E

O	W	W	W	O	O	O	O	O	O	O	O

W	W	W	O	O	O	O	W	W	W	O	W

O	O	O	O	W	W	W	O	O	O	O	O

O	O	W	O	W	O	W	O	W	O	W	W

O	W	W	O	O	O	W	W	O	O	O	W

O	O	W	O	O	W	W	W	O	O	O	O

O	O	O	W	O	O	O	O	W	W	W	W

W	W	W	O	O	O	O	W	W	W	O	O

O	W	W	W	W	O	O	O	O	O	W	W

W	W	W	O	O	O	O	O	W	W	W	W

(0,0) (5,7) (7,8)

【输出】 

-1 9 10

【解释】

输出表示第一个点（0，0）无法到达出口；

第二个点（5，7）到达出口的最短路径是9；

第三个点（7，8）到达出口的最短路径是10；
```

---

## Lab08：Lab07-List上机练习1

- **知识点**：线性表（顺序）
- **截止时间**：2026-05-12 23:59:00
- **题目数**：2

### 题目 1：List的顺序实现

- **难度**：困难　|　**满分**：50
- **questionId**：`165`
- **时间限制**：1000 ms　|　**内存限制**：128 MB

**题目描述：**

```
（List的顺序实现）请用顺序存储实现通用线性表的数据结构MyList。你所实现的List应包括：Intsert，Remove，Retrieve，Replace, Traverse，Size，Full等功能。利用你实现的MyList实现对所输入的整数序列的顺序输出。

【输入】整数序列以-1结束，序列长度小于100

【输出】输入整数序列的顺序序列

例如：

【输入】3 9 8 2 5 -1 

【输出】3 9 8 2 5
```

---

### 题目 2：List的单链表实现

- **难度**：困难　|　**满分**：50
- **questionId**：`168`
- **时间限制**：1000 ms　|　**内存限制**：128 MB

**题目描述：**

```
（List的单链表实现）请用单链表（需要记录最后一次访问的位置）实现通用线性表的数据结构MyList。你所实现的List应包括：Insert，Remove，Retrieve，Replace, Traverse，Size，Full等功能。利用你实现的MyList实现输入序列的增删及修改。

【输入】输入数据共4行，操作过程中序列长度始终小于100；

第1行为输入的整数序列，以-1结束；

第2行为N（N>=0）对数a b（0<=a<=length），表示在第a个位置前插入数b，以-1 -1结束；

第3行为M（M>=0）个数c（0<=c<=length-1），表示删除第c个位置的元素，以-1结束；

第4行为P（P>=0）对数d e（0<=d<=length-1），表示修改第d个位置的元素，以-1 -1结束。

**注意：插入，删除，修改操作均按照顺序在同一个序列中进行。

【输出】操作后的新序列。

例如：

【输入】 

3 7 8 4 6 -1

1 2 -1 -1  //在第1个位置的元素7前插入数2，此时序列为3 2 7 8 4 6

3 -1  // 删除序列3 2 7 8 4 6第3个位置的元素8，此时序列为3 2 7 4 6

4 9 -1 -1//将现有序列第4个位置的元素6修改为9，此时序列为3 2 7 4 9

【输出】

3 2 7 4 9  // 输出操作后的新序列
```

---

## Lab09：Lab08-List上机2

- **知识点**：线性表（链式）
- **截止时间**：2026-04-27 23:00:00
- **题目数**：3

### 题目 1：List的双链表实现

- **难度**：困难　|　**满分**：33
- **questionId**：`169`
- **时间限制**：1000 ms　|　**内存限制**：128 MB

**题目描述：**

```
（List的双链表实现）请用双链表（需要记录最后一次访问的位置）实现通用线性表的数据结构MyList。你所实现的List应包括：Insert，Remove，Retrieve，Replace, Traverse，Size，Full等功能。利用你实现的MyList实现输入序列的增删、修改及正逆序输出。

【输入】输入数据共4行，操作过程中序列长度始终小于100；

第1行为输入的整数序列，以-1结束；

第2行为N（N>=0）对数a b（0<=a<=length），表示在第a个位置前插入数b，以-1 -1结束；

第3行为M（M>=0）个数c（0<=c<=length-1），表示删除第c个位置的元素，以-1结束；

第4行为P（P>=0）对数d e（0<=d<=length-1），表示修改第d个位置的元素，以-1 -1结束。

**注意：插入，删除，修改操作均按照顺序在同一个序列中进行。

【输出】操作后新序列的正逆序输出，第1行为正序，第2行为逆序。

例如：

【输入】 

3 7 8 4 6 -1

1 2 -1 -1// 在第1个位置的元素7前插入数2，此时序列为3 2 7 8 4 6

3 -1// 删除序列3 2 7 8 4 6第3个位置的元素8，此时序列为3 2 7 4 6

4 9 -1 -1//将现有序列第4个位置的元素6修改为9，此时序列为3 2 7 4 9

【输出】

3 2 7 4 9  // 新序列的正序输出

9 4 7 2 3  // 新序列的逆序输出
```

---

### 题目 2：页面的相关系数

- **难度**：中等　|　**满分**：33
- **questionId**：`167`
- **时间限制**：1000 ms　|　**内存限制**：128 MB

**题目描述：**

```
（页面的相关系数）有N个 Web 页面，给每个Web页面分配一个相关系数 Vi（Vi为正整数），请输出具有最大相关系数的页面，如果具有最大相关系数的页面有多个，那么将这些页面全部输出。

*请尝试用自己编写的MyList来辅助完成该题。

【输入】

第 1 行：一个正整数 N (0<N<=150)

第 2 行 ~ N+1 行：每行包含一个字符串和一个整数 Vi，两者之间用一个空格分隔。字符串表示Web页面的URL（字符串长度不超过 100 个字符,且不含有空格）,整数 Vi(1<=Vi<=100)为页面的相关系数。

【输出】

输出具有最大相关系数的页面的URL，如果具有最大相关系数的页面有多个，则按照输入的顺序依次将它们都输出。每行的最后有一个换行符。

例如：

【输入】 

10

www.youtube.com 1

www.google.com 13

www.google.com.hk 3

www.alibaba.com 13

www.taobao.com 5

www.bad.com 10

www.good.com 7

www.baidu.com 8

www.university.edu.cn 9

www.ecnu.edu.cn 13

【输出】

www.google.com

www.alibaba.com

www.ecnu.edu.cn
```

---

### 题目 3：大数运算

- **难度**：简单　|　**满分**：34
- **questionId**：`166`
- **时间限制**：1000 ms　|　**内存限制**：128 MB

**题目描述：**

```
（大数运算）long long类型一般占8个字节是C/C++中的精度最高的整数类型，其取值范围是： -9223372036854775808～+9223372036854775807。在很多场景中，整数范围超出了long long的最值，例如在非对称加密中密钥长度一般为1024bit，转换为十进制数将超过300位，因此不能直接用内置的整数类型来运算。请编写大数运算类型MyBigInteger，使其支持大数据的加法，减法，乘法的运算。（除法为选做功能，除法运算符合C/C++中的整数除法运算的规则，有20%的测试用例包含除法运算，）

【输入】 

大整数n，n的位数<=200

大整数m，m的位数<=200

运算符（+，-，*, /）

【输出】n和m的运算结果

例如：

【输入】

56891237265

32156789215

-

【输出】

24734448050
```

---

## Lab10：Lab09-List应用（字符串类）

- **知识点**：线性表应用（字符串）
- **截止时间**：2026-05-12 23:59:00
- **题目数**：1

### 题目 1：String的实现

- **难度**：中等　|　**满分**：100
- **questionId**：`170`
- **时间限制**：1000 ms　|　**内存限制**：128 MB

**题目描述：**

```
（String的实现）请实现字符串数据结构String。String类型支持的操作有：
比较：==,>,<,>=,<=；
输入/输出；
字符串的操作：连接，求长度，子串查找，取子串等。
利用你实现的String类实现查找及字典序排序等功能。
以下为String的一种实现参考：
```
class String {
public: // methods of the string ADT
	String( );
	~String( );
	String (const String &copy); // copy constructor
	String (const char *copy); // conversion from C-string
	String (List<char> &copy); // conversion from List
	void operator = (const String &copy);
	const char *c_str( ) const; // conversion to C-style string
protected:
	char *entries;
	int length;
};

bool operator == (const String &rst, const String &second);
bool operator > (const String &rst, const String &second);
bool operator < (const String &rst, const String &second);
bool operator >= (const String &rst, const String &second);
bool operator <= (const String &rst, const String &second);
bool operator != (const String &rst, const String &second);

void strncpy(String &to, const String &from, int n);
void strcat(String &add_to, const String &add_on);
int strstr(const String &text, const String &target); 

String read_in(istream &input);
void write(String &s);
```
【输入】输入数据共3行；
第1行为字符串个数N（1<=N<=1000）；
第2行为输入的字符串序列，以空格隔开；
第3行为N（N>=0）对数a b（0<=a，b<=length-1），以-1 -1结束，判断第a个字符串是否是第b个字符串的子串，若是则输出第b个字符串中第一次出现第a个字符串的位置（以0开始），若不是则输出-1。
【输出】输出数据共2行；
第1行为输入数据第二行的结果，以空格隔开；
第2行为字符串序列的字典序输出。
例如：
【输入】
3
abc abcd cba
0 1 0 2 -1 -1
【输出】
0 -1  // abc在abcd中首次出现的位置是0，abc不是cba的子串
abc abcd cba  // 字典序输出
```

---

## Lab11：Lab10-查找

- **知识点**：查找
- **截止时间**：2026-05-12 23:00:00
- **题目数**：3

### 题目 1：前向和后向的最近邻值

- **难度**：中等　|　**满分**：33
- **questionId**：`172`
- **时间限制**：1000 ms　|　**内存限制**：128 MB

**题目描述：**

```
（前向和后向的最近邻值）给定一个包含有m个节点的双链表，链表每个节点的值均为正整数：
（1）节点i的前向最近邻值需要满足j小于i,且节点j的值小于节点i的值，j为满足条件的最大位置点。节点j的值即为节点i的前向最近邻值。若j不存在，节点i的前向最近邻值为0。
（2）节点i的后向最近邻值需要满足j大于i,且节点j的值大于节点i的值，j为满足条件的最小位置点。节点j的值即为节点i的后向最近邻值。若j不存在，节点i的后向最近邻值为0。
【输入】双链表中的m个值以-1结束
【输出】
按顺序输出每个节点的前向最近邻值；
按顺序输出每个节点的后向最近邻值；
例如：
【输入】 2 1 5 -1
【输出】
0 0 1
5 5 0
【输入】 2 7 3 4 5 -1
【输出】
0 2 2 3 4
7 0 4 5 0
```

---

### 题目 2：求开方值

- **难度**：中等　|　**满分**：33
- **questionId**：`176`
- **时间限制**：1000 ms　|　**内存限制**：128 MB

**题目描述：**

```
（Sqrt function）Implement int sqrt(int x).Compute and return the square root of x, where x is guaranteed to be a non-negative integer. Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

【输入】x的值，x为整数

【输出】x的平方根（整数）

例如：

【输入】 4

【输出】 2

【输入】 8

【输出】 2 //8的开方为2.82842，结果只需要输出整数，故输出2即可。
```

---

### 题目 3：Start and End Position

- **难度**：中等　|　**满分**：34
- **questionId**：`175`
- **时间限制**：1000 ms　|　**内存限制**：128 MB

**题目描述：**

```
（Start and end position）Given an array of integers numbers sorted in ascending order, find the starting and ending position of a given target value. Your algorithm's runtime complexity must be in the order of O(log n). If the target is not found in the array, return [-1, -1].

【输入】 

第一行，要查找的目标值

第二行，值按升序排列的整数数组，数组以-1结束（数组长度小于2000）

【输出】 目标值在数组里，第一次以及最后一次出现的下标

例如：

【输入】 

8

5 7 7 8 8 10 -1

【输出】

[3,4]

【输入】 

6

5 7 7 8 8 10 -1 

【输出】

[-1,-1]
```

---

## Lab12：Lab10-课堂二分查找的实现

- **知识点**：查找
- **截止时间**：2026-05-12 23:59:00
- **题目数**：1

### 题目 1：二分查找的实现

- **难度**：中等　|　**满分**：100
- **questionId**：`178`
- **时间限制**：1000 ms　|　**内存限制**：128 MB

**题目描述：**

```
（二分查找的实现）请尝试用你实现的顺序存储List实现二分查找。List中的Record包含key和other部分。其中key为英文单词，other为单词的中文解释。

【输入】

第一行，查询目标target（英文单词）

第二行，若干条包含key（string）和other（string）的序列，序列按照key的升序排列；（单词数量小于2000）

【输出】查询目标所在的下标，查询目标的内容（key和other），若单词不存在则输出-1即可。

例如

【输入】

wait

computer 电脑 eye 眼睛 hello 你好 train 火车 wait 等待 zebra 斑马

【输出】

4

wait 等待

【输入】

apple

computer 电脑 eye 眼睛 hello 你好 train 火车 wait 等待 zebra 斑马

【输出】

-1 //不存在
```

---

## Lab13：Lab11-排序算法1

- **知识点**：排序
- **截止时间**：2026-05-19 21:00:00
- **题目数**：3

### 题目 1：插入排序的顺序实现

- **难度**：中等　|　**满分**：33
- **questionId**：`180`
- **时间限制**：1000 ms　|　**内存限制**：128 MB

**题目描述：**

```
请在你实现的顺序存储的List基础上实现插入排序。

【输入】

第一行，待排序序列个数n，序列长度小于1000；

第二行，n个整数序列；

【输出】

插入排序的中间结果，即当有序序列长度为n/2时的中间结果；

插入排序的最终结果；

例如：

【输入】

5

9 3 8 2 5

【输出】

3 9 8 2 5//输出有序序列长度为2（5/2）时的结果

2 3 5 8 9
```

---

### 题目 2：插入排序的链式实现

- **难度**：中等　|　**满分**：33
- **questionId**：`188`
- **时间限制**：1000 ms　|　**内存限制**：128 MB

**题目描述：**

```
请在你实现的链式存储的List基础上实现插入排序。

【输入】

第一行，待排序序列个数n，序列长度小于1000；

第二行，n个整数序列；

【输出】

插入排序的中间结果，即当有序序列长度为n/2时的中间结果；

插入排序的最终结果；

例如：

【输入】

5

9 3 8 2 5

【输出】

3 9 8 2 5//输出有序序列长度为2（5/2）时的结果

2 3 5 8 9
```

---

### 题目 3：Largest Number

- **难度**：中等　|　**满分**：34
- **questionId**：`184`
- **时间限制**：1000 ms　|　**内存限制**：128 MB

**题目描述：**

```
Given a list of non negative integers, arrange them such that they form the largest number.

Example 1:

Input: [10,2]

Output: "210"

Example 2:

Input: [3,30,34,5,9]

Output: "9534330"

【输入】n个非负数，n大于1小于1000，序列n长度小于1000；

【输出】n个非负数组成的最大值。

例如：

【输入】

3 30 34 5 9

【输出】

9534330
```

---

## Lab14：Lab11-课堂上机

- **知识点**：排序
- **截止时间**：2026-05-19 21:00:00
- **题目数**：1

### 题目 1：选择排序

- **难度**：中等　|　**满分**：100
- **questionId**：`183`
- **时间限制**：1000 ms　|　**内存限制**：128 MB

**题目描述：**

```
请在你实现的顺序存储的List基础上实现选择排序（按照找最小值的方法来实现选择排序）。

【输入】

第一行，待排序序列个数n，序列长度小于1000；

第二行，n个整数序列；

【输出】

选择排序的中间结果，即当有序序列长度为n/2时的中间结果；

选择排序的最终结果；

例如：

【输入】

5

9 3 8 2 5

【输出】

2 3 8 9 5//输出有序序列长度为2（5/2）时的结果

2 3 5 8 9
```

---

## Lab15：Lab12-排序算法2

- **知识点**：排序
- **截止时间**：2026-05-26 23:00:00
- **题目数**：5

### 题目 1：归并排序的链式实现

- **难度**：中等　|　**满分**：20
- **questionId**：`189`
- **时间限制**：1000 ms　|　**内存限制**：128 MB

**题目描述：**

```
请在你实现的链式存储的List基础上实现归并排序。

【输入】

第一行，待排序序列个数n，序列长度小于1000；

第二行，n个整数序列；

【输出】

归并排序的中间结果，即归并前的子序列1和子序列2；

归并排序的最终结果；

例如：

【输入】

5

9 3 8 2 5

【输出】

3 8 9//归并前的子序列1

2 5//归并前的子序列2

2 3 5 8 9
```

---

### 题目 2：快速排序的顺序实现

- **难度**：中等　|　**满分**：20
- **questionId**：`190`
- **时间限制**：1000 ms　|　**内存限制**：128 MB

**题目描述：**

```
请在你实现的顺序存储的List基础上实现快速排序。（假设序列中的最后一个元素为轴点），此题需要按照课本的方法进行序列划分。

【输入】

第一行，待排序序列个数n，序列长度小于1000；

第二行，n个整数序列；

【输出】

快速排序的中间结果，即第一轮排序后序列的排列情况；

快速排序的最终结果；

例如：

【输入】

5

6 3 8 2 5

【输出】

2 3 5 8 6

2 3 5 6 8
```

---

### 题目 3：颜色排序sort colors

- **难度**：中等　|　**满分**：20
- **questionId**：`186`
- **时间限制**：1000 ms　|　**内存限制**：128 MB

**题目描述：**

```
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue. Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

请尝试编写适合该问题的排序算法。

最合适该问题的算法复杂度可控制在O(n)，辅助空间为常数。

【输入】0，1，2组成的任意整数序列，序列长度小于10000。

【输出】输出整数序列的顺序序列

例如：

【输入】2 0 2 1 1 0

【输出】0 0 1 1 2 2
```

---

### 题目 4：优先级队列的实现

- **难度**：中等　|　**满分**：20
- **questionId**：`192`
- **时间限制**：1000 ms　|　**内存限制**：128 MB

**题目描述：**

```
优先级队列（priority queue） 是0个或多个元素的集合，每个元素都有一个优先权（在此假设数字越大优先权越高，一样大的数字优先权一样大）。对优先级队列执行的操作有（1）查找（2）插入一个新元素 （3）删除 一般情况下，查找操作用来搜索优先权最大的元素，删除操作用来删除该元素 。对于优先权相同的元素，可按先进先出次序处理或按任意优先权进行。请借助于堆实现优先级队列的数据结构。

要求：（1）采用顺序存储；（2）支持的操作有：删除元素操作（即取出最大优先级的元素）；插入元素操作；

【输入】

第一行，n个初始元素（元素大于0，顺序随机），以-1结束；n小于1000；

第二行，删除的元素个数m，m小于n

第三行，需要插入到优先级队列的元素序列，以-1结束；

【输出】

第一行，初始优先级队列的信息；（ 书本build_heap算法建堆）

第二行，删除m个元素后的优先级队列信息；

第三行，插入了若干元素后的优先级队列信息；（需要采用自下而上的算法插入堆）

【输入】

6 3 8 2 5 -1//初始序列

2//从优先级队列中删除2个元素

12 7 9 -1//依次插入3个新的值，插入12时，先把12追加到堆的尾部，然后再自下而上的调整堆。

【输出】

8 5 6 2 3

5 2 3//删除了2个元素8，6后的优先级队列

12 7 9 2 5 3//依次插入12，7，9后的堆
```

---

### 题目 5：堆排序的顺序实现

- **难度**：中等　|　**满分**：20
- **questionId**：`191`
- **时间限制**：1000 ms　|　**内存限制**：128 MB

**题目描述：**

```
请在你实现的顺序存储的List基础上实现堆排序。

【输入】

第一行，待排序序列个数n，序列长度小于1000；

第二行，n个整数序列；

【输出】

初始的堆；（大根堆）

堆排序后的结果；

例如：

【输入】

5

6 3 8 2 5

【输出】

8 5 6 2 3//输入序列构造的初始大根堆

2 3 5 6 8
```

---

## Lab16：Lab13-Hash表上机实践

- **知识点**：哈希表
- **截止时间**：2026-06-01 23:00:00
- **题目数**：2

### 题目 1：Hash Map的实现

- **难度**：中等　|　**满分**：50
- **questionId**：`203`
- **时间限制**：1000 ms　|　**内存限制**：128 MB

**题目描述：**

```
Design a HashMap without using any built-in hash table libraries.

Note:请用链地址法解决冲突；



To be specific, your design should include these functions:

put(key, value) : Insert a (key, value) pair into the HashMap. If the value already exists in the HashMap, update the value. Note:新值插入链表头部，如果已经存在值，则更新这个值

get(key): Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.

remove(key) : Remove the mapping for the value key if this map contains the mapping for the key.



Example:

MyHashMap hashMap;

hashMap.put(“abc”, “abc”);          

hashMap.put(“abcd”, “abcd”);         

hashMap.get(“abc”);            // returns 1

hashMap.get(“cat”);            // returns -1 (not found)

hashMap.put(“abcd”, “ABCD”);          // update the existing value

hashMap.get(“abcd”);            // returns 1 

hashMap.remove(“abcd”);          // remove the mapping for 2

hashMap.get(“abcd”);            // returns -1 (not found)



Key字符串类型的转换借助于BKDR Hash Function

// BKDR Hash Function

unsigned int BKDRHash(char *str)

{

    unsigned int seed = 31; // 31 131 1313 13131 131313 etc..

    unsigned int hash = 0;

 

    while (*str)

    {

        hash = (hash * seed + (*str++))% Hash_Size;

    }

 

    return (hash% Hash_Size); //使hash函数返回值在hash表的有效地址范围

}





【输入】

第一行，整数n和m，n表示hash表的大小，m代表插入hash表的元素个数。n小于1000的素数，m小于n。注意n可理解为BKDRHash中Hash_Size的值。

第二行，m对<key value>的值

第三行，1组<key value>//insert<key value>到Hash Map

第四行，任意的Key1//删除Key

第五行，任意查询的key2

【输出】

第一行，对应于输入第三行<key value>插入到Hash Map的地址信息；

第二行，对应于输入第四行删除key1的过程；

第三行，对应于输入第五行探测的key2的过程；

注意若key在hash表中不存在，则输出NULL。

例如：

【输入】

7 6

computer 电脑 eye 眼睛 hello 你好 train 火车 wait 等待 zebra 斑马

train 火车，训练

dog

hello



注意：此时Key的位置信息为computer:1; eye:1; hello:0; train:3; wait:2; zebra:0



【输出】

3//输出train对应的地址码；

6 dog NULL//dog的地址码为6，删除dog失败；

0 zebra hello 你好//hello的地址码为0，先访问到zebra然后访问到hello。
```

---

### 题目 2：Longest Substring Without Repeating Characters

- **难度**：中等　|　**满分**：50
- **questionId**：`205`
- **时间限制**：1000 ms　|　**内存限制**：128 MB

**题目描述：**

```
Given a string, find the length of the longest substring without repeating characters.



Example 1:

Input: "abcabcbb"

Output: 3 

Explanation: The answer is "abc", with the length of 3. 



Example 2:

Input: "bbbbb"

Output: 1

Explanation: The answer is "b", with the length of 1.



Example 3:

Input: "pwwkew"

Output: 3

Explanation: The answer is "wke", with the length of 3. 

Note that the answer must be a substring, "pwke" is a subsequence and not a substring.



【输入】

第一行，长度为n的字符串，字符串中不包含空格，n小于2000。

【输出】

最大非重复子串的长度；



例如：

【输入】

pwwkew

【输出】

3

【输入】

bbbbb

【输出】

1
```

---

## Lab17：Lab13-课堂作业

- **知识点**：哈希表
- **截止时间**：2026-05-28 12:00:00
- **题目数**：1

### 题目 1：Hash Table的顺序实现

- **难度**：中等　|　**满分**：100
- **questionId**：`202`
- **时间限制**：1000 ms　|　**内存限制**：128 MB

**题目描述：**

```
请实现顺序存储的Hash Table。Hash函数用取余法（Modular Arithmetic，除数为小于Hash表大小），冲突检测算法为平方探测，考虑overflow的情况，探测ci'sh次数的上限和课本定义相同。
【输入】
第一行，整数n和m，n表示hash表的大小，m代表插入hash表的元素个数。n为小于2000的素数，m小于n。
第二行，m对<key value>的值
第三行，任意查询的key1
第四行，任意查询的key2
【输出】
第一行，探测到key1的过程及key1对应的value；
第二行，探测到key2的过程及key2对应的value；
注意若key在hash表中不存在，则输出NULL。
例如：
【输入】
13 6//hash函数为 key%13
16 16 3 3 29 29 26 26 39 39 52 52//6对<key value>的值,若出现重复的key，hash表只存放第一次的key value对
52
20
【输出】
0 1 4 9 52 52//先后探测了0，1，4，9等位置，且探测成功；
7 8 NULL//先后探测了位置7和8，探测失败；
```

---

## Lab18：Lab14-课后上机

- **知识点**：二叉树
- **截止时间**：2026-06-10 12:00:00
- **题目数**：3

### 题目 1：Binary Search Tree

- **难度**：中等　|　**满分**：33
- **questionId**：`209`
- **时间限制**：1000 ms　|　**内存限制**：128 MB

**题目描述：**

```
请用链式存储的二叉查找树实现单词信息的查找。包含的操作有：插入元素、删除元素、查找元素等。

注意：Record包含key和other部分。其中key为英文单词，other为单词的中文解释。

【输入】

第1行，插入的单词数量，插入二叉查找树的单词信息，若干条包含key（string）和other（string）的序列；（单词数量小于2000）

第2行，删除的单词数量，从二叉查找树中删除的单词清单；（若为多个单词，会用空格隔开）（请用其前驱节点代替删除节点）

第3行，查询目标target1（英文单词）

第4行，查询目标target2（英文单词）



【输出】

第1行，查询目标1所在的路径信息和查询目标的内容（key和other），若单词不存在则输出NULL即可。

第2行，查询目标2所在的路径信息和查询目标的内容（key和other），若单词不存在则输出NULL即可。



例如

【输入】

6 train 火车  eye 眼睛 hello 你好 computer 电脑 wait 等待 zebra 斑马//插入

1 eye//删除

hello//查询目标1

eye//查询目标2

【输出】

train computer hello 你好//从根节点train开始，经过左孩子computer，然后右孩子，查找成功

train computer hello NULL//不存在

【说明】：

6个单词（train 火车  eye 眼睛 hello 你好 computer 电脑 wait 等待 zebra 斑马）生成的二叉查找树为：

      t

    /    \

  e      w

/    \      \

c    h      z



删除eye之后的查找树：

      t

    /    \

  c      w

    \      \

    h      z

在此基础上查找hello：访问路径为 t，c，h；成功

在此基础上查找eye，访问路径为：t，c，h，null；失败（h->left为空）
```

---

### 题目 2：The Sum of Path

- **难度**：困难　|　**满分**：33
- **questionId**：`215`
- **时间限制**：1000 ms　|　**内存限制**：128 MB

**题目描述：**

```
给定一棵二叉树和一个整数k，判断该二叉树中是否存在一条根节点至叶节点的路径，该路径上所有节点的值的和等于k。

【输入】
第一行 插入的元素个数，空格隔开的若干整数，数量小于2000；
第二行 整数k
【输出】
生成的二叉树的高度（仅有一个node的二叉树高度为0），是否存在这样一条路径，true或者false

例如：
【输入】
7 1 2 2 3 4 4 3
7
  
 &ensp; &ensp;1
 &ensp;  / \
&ensp;2 &ensp;2
&ensp;/ \  / \
3  4 4  3

【输出】
2 true

【输入】
6 1 3 2 3 4 7
10

 &ensp;&ensp;1
   &ensp; / \
  &ensp;3  &ensp;  2
 &ensp;/ \  /
&ensp;3  4 7

【输出】
2 true
```

---

### 题目 3：二分查找树的最矮公共祖先

- **难度**：中等　|　**满分**：34
- **questionId**：`216`
- **时间限制**：1000 ms　|　**内存限制**：128 MB

**题目描述：**

```
给定一个二分查找树和两个树中的节点，请找出这两个节点在这棵二分查找树中最矮(离叶子节点最接近)的公共祖先。

【输入】
第一行，插入的整数数量，空格隔开的若干不重复的整数，数量小于2000
第二行，两个整数p和q，空格隔开。（p和q是树中的节点值）
【输出】
最矮的公共祖先

例如：【输入】
8 6 2 8 4 3 5 7 9
2 8
【输出】
6

【输入】
8 6 2 8 4 3 5 7 9
2 4
【输出】
2

【解释】
二叉查找树为：
 &ensp;  &ensp; 6
 &ensp;&ensp;  /&ensp;\
  &ensp; 2 &ensp; 8
   &ensp;&ensp;\ &ensp;&ensp;/&ensp;\
  &ensp;&ensp;4 &ensp;7&ensp;&ensp;9
   &ensp;&ensp;/&ensp;\
   &ensp;3&ensp;&ensp;5
2和8的最矮公共祖先是6；
2和4的最矮公共祖先为2；
```

---

## Lab19：Lab14-课堂-二叉树的遍历

- **知识点**：二叉树
- **截止时间**：2026-06-04 00:00:00
- **题目数**：1

### 题目 1：Traverse of Binary Tree

- **难度**：中等　|　**满分**：100
- **questionId**：`27`
- **时间限制**：1000 ms　|　**内存限制**：128 MB

**题目描述：**

```
（二叉树遍历）请实现链式存储的二叉树结构。包含的操作有：插入元素（生成完全二叉树）、计算二叉树高度、前序、中序、后序遍历等。

【输入】

第一行，插入的元素个数，空格隔开的若干整数，整数数量小于2000；



【输出】

第一行，生成的完全二叉树的高度； （仅有一个node的二叉树高度为0）

第二行，二叉树前序遍历结果；

第三行，二叉树中序遍历结果；

第四行，二叉树后序遍历结果；



例如：

【输入】

10 0 1 2 3 4 5 6 7 8 9



【输出】

3

0  1  3  7  8  4  9  2  5  6

7  3  8  1  9  4  0  5  2  6

7  8  3  9  4  1  5  6  2  0
```

---

## Lab20：中序波兰式求解

- **知识点**：其他
- **截止时间**：2026-05-21 00:00:00
- **题目数**：1

### 题目 1：中序波兰式求解

- **难度**：简单　|　**满分**：100
- **questionId**：`143`
- **时间限制**：1000 ms　|　**内存限制**：128 MB

**题目描述：**

```
(中序波兰式求解) 请编写程序求解中序波兰式的值。表达式中可能的运算符有+，-，\*，/，（）。
【输入】中序波兰式
【输出】波兰式的值 //输出的数据类型符合C/C++对表达式求值的定义，即表达式的输出类型由高精度的运算数来决定。

浮点型保留小数点后的3位小数
例如：
【输入】2\*(4+5)-12
【输出】6
【输入】2*2.5
【输出】5.000
备注：
（1）对于80%的测试数据运算数中仅仅包含正整数；
（2）对于10%的测试数据运算数中包含有浮点数；
（3）对于10%的测试数据运算数中包含有负数；
```

---

## Lab21：二维Life Game

- **知识点**：其他
- **截止时间**：2026-03-05 12:00:00
- **题目数**：1

### 题目 1：Life Game(二维)

- **难度**：中等　|　**满分**：100
- **questionId**：`134`
- **时间限制**：1000 ms　|　**内存限制**：128 MB

**题目描述：**

```
Definitions：
Life is really a simulation, not a game with players. It takes place on unbounded rectangular grid in which each cell can either be occupied by an organism or not. Occupied cells are called alived; unoccupied cells are called dead. Which cells are alive changes from generation to generation according to the number of neighboring cells that are alive, as follows transition rules:
(1)	The neighbors of a given cell are the eight cells that touch it vertically, horizontally, or diagonally.
(2)	If a cell is alive but either has no neighboring cells alive or only one alive, then in the next generation the cell dies of loneliness.
(3)	If a cell is alive and has four or more neighboring cells also alive, then in the next generation the cell dies of overcrowding.
(4)	A living cell with either two or three living neighbors remains alive in the next generation.
(5)	If a cell is dead, then in the next generation it will become alive if it has exactly three neighboring cells, no more or fewer, that are already alive. All other dead cells remain dead in the next generation.
(6)	All births and deaths take place at exactly the same time.
(7)	The size of grid is 20*60（棋盘有20行输入范围1-20，有60列输入范围1-60）

Input: the coordinates of living cells (Terminate the list with the special pair -1 -1). 
      The number (n) of generation. (n=0 means the initial Grid)
Output: the next n generations of the grid.

For example：
【输入】
5 3
5 4
5 5
5 6
-1 -1 //输入结束
3 //输出第3代的结果
【输出】
```
------------------------------------------------------------
------------------------------------------------------------
------------------------------------------------------------
---**-------------------------------------------------------
--*--*------------------------------------------------------
---**-------------------------------------------------------
------------------------------------------------------------
------------------------------------------------------------
------------------------------------------------------------
------------------------------------------------------------
------------------------------------------------------------
------------------------------------------------------------
------------------------------------------------------------
------------------------------------------------------------
------------------------------------------------------------
------------------------------------------------------------
------------------------------------------------------------
------------------------------------------------------------
------------------------------------------------------------
------------------------------------------------------------
```
```

---

## Lab22：单链表课堂练习

- **知识点**：其他
- **截止时间**：2026-03-26 23:00:00
- **题目数**：1

### 题目 1：单链表的创建与输出

- **难度**：困难　|　**满分**：100
- **questionId**：`151`
- **时间限制**：1000 ms　|　**内存限制**：128 MB

**题目描述：**

```
（单链表的创建与输出）请用链表的形式存储用户输入的n个整数。要求使用堆内存，注意内存的分配和释放。
【输入】第一行整数n，第二行n个整数
【输出】n个整数之和（n>=0）
例如：
【输入】
5
3 6 9 10 1
【输出】
29
```

---

## Lab23：栈课堂练习

- **知识点**：其他
- **截止时间**：2026-03-12 12:00:00
- **题目数**：1

### 题目 1：栈的顺序实现

- **难度**：困难　|　**满分**：100
- **questionId**：`137`
- **时间限制**：1000 ms　|　**内存限制**：128 MB

**题目描述：**

```
请用顺序存储实现栈的数据结构Stack。你所实现的栈应包括：pop，push，top，size，clear，full等功能。利用你实现的Stack实现输入数字的逆序输出。

【输入】整数序列以-1结束，序列长度小于100

【输出】输入整数序列的逆序序列

例如：

【输入】3 9 8 2 5 -1 

【输出】5 2 8 9 3
```

---

## Lab24：课堂练习3-环形队列

- **知识点**：其他
- **截止时间**：2026-03-19 12:00:00
- **题目数**：1

### 题目 1：环形队列

- **难度**：中等　|　**满分**：100
- **questionId**：`146`
- **时间限制**：1000 ms　|　**内存限制**：128 MB

**题目描述：**

```
（环形队列）请用顺序存储实现环形的数据结构CirQueue。你所实现的环形队列应包括：出队、入队、访问队首、判断队列是否已满，判断队列是否为空等功能。利用你实现的CirQueue实现输入整数序列的顺序输出。

【输入】整数序列以-1结束，序列长度小于100

【输出】输入整数序列的顺序序列

例如：

【输入】3 9 8 2 5 -1 

【输出】3 9 8 2 5
```

---

## Lab25：递归课堂练习

- **知识点**：其他
- **截止时间**：2026-04-18 00:00:00
- **题目数**：2

### 题目 1：递归求最小求和

- **难度**：困难　|　**满分**：50
- **questionId**：`103`
- **时间限制**：1000 ms　|　**内存限制**：128 MB

**题目描述：**

```
（指针）99. 有数组int array[ ]，

用递归方法实现求最小值、求和。

递归函数原型：

int Min (int arr[ ], int n); int Sum (int arr [ ], int n);

【输入】

第1行：一个正整数 n，为数组 array 中的元素个数，不超过100。

第2行，由空格分隔的n个整数，每个整数在 int 范围内。

【输出】

一行，由空格分隔的2个整数，分别表示数组 array 中各元素的最小值与和。

保证中间与最终答案在 int 范围内。

【样例输入】

10

0 1 2 3 4 5 6 7 8 9

【样例输出】 

0 45
```

---

### 题目 2：二进制转换为十进制

- **难度**：中等　|　**满分**：50
- **questionId**：`161`
- **时间限制**：1000 ms　|　**内存限制**：128 MB

**题目描述：**

```
请用递归的方式实现二进制向十进制转换。

【输入】 二进制序列，长度小于20

【输出】 二进制对应的10进制数

例如：

【输入】111001 

【输出】57
```

---
