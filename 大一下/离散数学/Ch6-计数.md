# 第六章 计数

> **考试分值**：6 题 / 45 分（与 Ch8 共出 6 题，本章约 3 题）
> **考纲 section**：6.1, 6.2, 6.3, 6.4, 6.5, 6.6（**全考**）
> **作业覆盖**：6 个 section，共 32 道必做题

## 反复出现的考点

| 排名 | 考点 | 频次 |
|---|---|---|
| ★★★ | **6.5 广义组合（可重/不可区分）** | 7 |
| ★★★ | **6.1 加法/乘法/减法原理** | 8 |
| ★★☆ | **6.3 排列组合 P(n,r), C(n,r)** | 3 |
| ★★☆ | **6.4 二项式定理 + Pascal** | 6 |
| ★★☆ | **6.2 鸽巢原理** | 4 |
| ★☆☆ | **6.6 排列生成** | 4 |

> [!warning] **6.5 广义组合** 和 **6.1 计数原理** 是必考核心

---

## 6.1 计数基础（**必考**）

### 4 大原理

| 原理 | 判定关键字 | 公式 |
|---|---|---|
| **加法** | "或"（互斥） | |A∪B| = |A|+|B| |
| **乘法** | "和""又"（独立） | |A×B| = |A|·|B| |
| **减法** | "不超过" "非" | |A| = |U| - |Ā| |
| **除法** | "等价类" | 计数 = 总数 / 每类大小 |

### 反复考的题型 1：加法 + 乘法原理

```
作业 24 典型：3 男 5 女，选 1 男 1 女
总选法 = 3 × 5 = 15（乘法：先选男再选女）
```

### 反复考的题型 2：减法原理（"至少"题）

```
作业 36 典型：1000 以内可被 7 或 11 整除的正整数
|A∪B| = |A| + |B| - |A∩B|
     = ⌊1000/7⌋ + ⌊1000/11⌋ - ⌊1000/77⌋
     = 142 + 90 - 12 = 220
```

> [!tip] "或"用加法，"和"用乘法，"至少"用减法

### 配套作业

**必做题（8 题）：**

**16** 

```
16. How many strings are there of four lowercase letters that
have the letter x in them?
```

**24** 

```
24. How many positive integers between 1000 and 9999 in-
clusive
a) are divisible by 9?
b) are even?
c) have distinct digits?
d) are not divisible by 3?
e) are divisible by 5 or 7?
f) are not divisible by either 5 or 7?
g) are divisible by 5 but not by 7?
h) are divisible by 5 and 7?
```

**26** 

```
26. How many strings of four decimal digits
a) do not contain the same digit twice?
b) end with an even digit?
c) have exactly three digits that are 9s?
```

**30** 

```
30. How many license plates can be made using either three
uppercase English letters followed by three digits or four
uppercase English letters followed by two digits?
```

**36** 

```
36. How many functions are there from the set {1, 2,… ,n},
where n is a positive integer, to the set{0, 1}?
```

**38** 

```
38. How many partial functions (see Section 2.3) are there
from a set with ﬁve elements to sets with each of these
number of elements?
a) 1 b) 2 c) 5 d) 9
```

**40** 

```
40. How many subsets of a set with 100 elements have more
than one element?
```

**48** 

```
48. In how many ways can a photographer at a wedding ar-
range 6 people in a row from a group of 10 people, where
the bride and the groom are among these 10 people, if
a) the bride must be in the picture?
b) both the bride and groom must be in the picture?
c) exactly one of the bride and the groom is in the pic-
ture?
```


---

## 6.2 鸽巢原理

### 两个版本

| 版本 | 公式 | 含义 |
|---|---|---|
| **基本** | n 物体放 k 盒，n > k → 必有一盒 ≥ 2 | 物体比盒子多 |
| **广义** | n 物体放 k 盒 → 必有一盒 ≥ ⌈n/k⌉ | 平均分配最均匀 |

### 配套作业

**必做题（4 题）：**

**2** 

```
2. Show that if there are 30 students in a class, then at least
two have last names that begin with the same letter.
```

**4** 

```
4. A bowl contains 10 red balls and 10 blue balls. A woman
selects balls at random without looking at them.
a) How many balls must she select to be sure of having
at least three balls of the same color?
b) How many balls must she select to be sure of having
at least three blue balls?
```

**8** 

```
8. Let d be a positive integer. Show that among any group of
d+ 1 (not necessarily consecutive) integers there are two
with exactly the same remainder when they are divided
by d.
```

**18** 

```
18. How many numbers must be selected from the set
{1, 3, 5, 7, 9, 11, 13, 15} to guarantee that at least one pair
of these numbers add up to 16?
```


---

## 6.3 排列与组合

### 必背公式

$$
P(n, r) = n(n-1)(n-2)\cdots(n-r+1) = \frac{n!}{(n-r)!}
$$

$$
\binom{n}{r} = \frac{n!}{r!(n-r)!}
$$

### 反复考判定

| 题型 | 选 P 还是 C |
|---|---|
| 排队、座位、密码（有顺序） | **P(n,r)** |
| 选人、选菜、选委员（无顺序） | **C(n,r)** |

### 配套作业

**必做题（3 题）：**

**20** 

```
20. How many bit strings of length 10 have
a) exactly three 0s?
b) more 0s than 1s?
c) at least seven 1s?
d) at least three 1s?
```

**22** 

```
22. How many permutations of the letters ABCDEFGHcon-
tain
a) the string ED?
b) the string CDE?
c) the strings BA and FGH?
d) the strings AB, DE,a n dGH?
e) the strings CABand BED?
f) the strings BC Aand AB F?
```

**28** 

```
28. Thirteen people on a softball team show up for a game.
a) How many ways are there to choose 10 players to take
the ﬁeld?
b) How many ways are there to assign the 10 positions
by selecting players from the 13 people who show up?
c) Of the 13 people who show up, three are women. How
many ways are there to choose 10 players to take the
ﬁeld if at least one of these players must be a woman?
```


---

## 6.4 二项式系数

### 必背

#### Pascal 恒等式

$$
\binom{n}{k} = \binom{n-1}{k-1} + \binom{n-1}{k}
$$

#### 二项式定理

$$
(x+y)^n = \sum_{k=0}^{n} \binom{n}{k} x^{n-k} y^k
$$

> [!warning] x 的指数是 n-k（不是 k）

#### 常用求和

$$
\sum_{k=0}^{n} \binom{n}{k} = 2^n
$$

### 配套作业

**必做题（6 题）：**

**8** 

```
8. What is the coeﬃcient of x8y9 in the expansion of
(3x+ 2y)17?
```

**14**（精选版未找到，请查 PDF）

**24** 

```
24. Suppose that k and n are integers with 1 ≤ k < n.P r o v e
the hexagon identity
(
n−1
k−1
)(
n
k+ 1
)(
n+ 1
k
)
=
(
n−1
k
)(
n
k−1
)(
n+ 1
k+ 1
)
,
which relates terms in Pascal’s triangle that form a
hexagon.
```

**26** 

```
26. Prove the identity (n
r
)(r
k
)= (n
k
)(n−k
r−k
), whenever n, r,a n d
k are nonnegative integers with r ≤ n and k ≤ r,
a) using a combinatorial argument.
b) using an argument based on the formula for the num-
ber of r-combinations of a set with n elements.
```

**28** 

```
28. Show that if p is a prime and k is an integer such that
1 ≤ k ≤ p−1, then p divides (
p
k
).
```

**32** 

```
32. Show that if n is a positive integer, then(2n
2
)= 2(n
2
)+ n2
a) using a combinatorial argument.
b) by algebraic manipulation.
∗33. Give a combinatorial proof that ∑ n
k= 1 k(n
k
)= n2n−1.
[Hint: Count in two ways the number of ways to select
a committee and to then select a leader of the commit-
tee.]
∗34. Give a combinatorial proof that ∑ n
k= 1 k(n
k
)2
= n(2n−1
n−1
).
[Hint: Count in two ways the number of ways to select a
committee, with n members from a group ofn mathemat-
ics professors and n computer science professors, such
that the chairperson of the committee is a mathematics
professor.]
```


---

## 6.5 广义排列与组合（**核心必考**）

### 3 个核心公式

| 类型 | 公式 | 关键判别 |
|---|---|---|
| **可重排列** | n^r | 元素可重复，**有序** |
| **可重组合** | $$ \binom{n+r-1}{r} $$ | 元素可重复，**无序** |
| **不可区分对象** | $$ \frac{n!}{n_1!\, n_2!\, \cdots\, n_k!} $$ | n 个对象分 k 类，nᵢ 不可区分 |

### 反复考的题型 1：可重组合（**必考大题**）

**公式**：从 n 类元素中**无序**取 r 个（每类可重复）

$$
\binom{n+r-1}{r}
$$

**典型**：从 4 种水果买 6 个，有多少种买法（数量不限）？

```
= C(4+6-1, 6) = C(9, 6) = 84
```

> [!tip] "**星星-竖线**"法：6 个星星 + 3 条竖线 = 9 个位置选 3 条放竖线 = C(9,3)

### 反复考的题型 2：不可区分对象排列（**必考大题**）

**公式**：n 个对象分成 k 类（nᵢ 个不可区分）：

$$
\frac{n!}{n_1!\, n_2!\, \cdots\, n_k!}
$$

**典型**：单词 MISSISSIPPI 的排列数

```
M:1, I:4, S:4, P:2 → 11!/(1!4!4!2!) = 11!/(1×24×24×2) = 34650
```

> [!warning] 字母重复 = 不可区分；分母是各类阶乘的乘积

### 反复考的题型 3：可重排列

**公式**：n^r

**典型**：3 位二进制字符串（每位可 0 或 1）数量

```
= 2³ = 8
```

### 配套作业

**必做题（7 题）：**

**6** 

```
6. How many ways are there to select ﬁve unordered ele-
ments from a set with three elements when repetition is
allowed?
```

**8** 

```
8. How many diﬀerent ways are there to choose a dozen
donuts from the 21 varieties at a donut shop?
```

**14** 

```
14. How many solutions are there to the equation
x
1 + x2 + x3 + x4 = 17,
where x1,x 2,x 3,a n dx4 are nonnegative integers?
```

**16** 

```
16. How many solutions are there to the equation
x1 + x2 + x3 + x4 + x5 + x6 = 29,
where xi, i = 1, 2, 3, 4, 5, 6, is a nonnegative integer such
that
a) x
i > 1f o ri = 1, 2, 3, 4, 5, 6?
b) x1 ≥ 1, x2 ≥ 2, x3 ≥ 3, x4 ≥ 4, x5 > 5, and x6 ≥ 6?
c) x1 ≤ 5?
d) x1 < 8a n dx2 > 8?
```

**32** 

```
32. How many diﬀerent strings can be made from the letters
in MISSISSIPPI, using all the letters?
```

**34** 

```
34. How many diﬀerent strings can be made from the letters
in AARDVARK, using all the letters, if all three Asm u s t
be consecutive?
```

**40** 

```
40. A professor packs her collection of 40 issues of a mathe-
matics journal in four boxes with 10 issues per box. How
many ways can she distribute the journals if
a) each box is numbered, so that they are distinguish-
able?
b) the boxes are identical, so that they cannot be distin-
guished?
```


**仅需读（1 题）：**

**15(read)**  **[仅读]**

```
15. How many solutions are there to the equation
x1 + x2 + x3 + x4 + x5 = 21,
where xi, i = 1, 2, 3, 4, 5, is a nonnegative integer such
that
a) x1 ≥ 1?
b) xi ≥ 2f o ri = 1, 2, 3, 4, 5?
c) 0 ≤ x1 ≤ 10?
d) 0 ≤ x1 ≤ 3, 1 ≤ x2 < 4, and x3 ≥ 15?
```


---

## 6.6 排列与组合的生成

### 反复考的算法

#### 字典序生成排列

从小到大生成所有 n! 个排列：
- 找最右的 aᵢ < aᵢ₊₁ 位置
- 找 aᵢ 右边的最小比 aᵢ 大的元素
- 交换，反转右半

### 配套作业

**必做题（4 题）：**

**2** 

```
2. Discuss ways in which the current telephone numbering
plan can be extended to accommodate the rapid demand
for more telephone numbers. (See if you can ﬁnd some
of the proposals coming from the telecommunications in-
dustry.) For each new numbering plan you discuss, show
how to ﬁnd the number of diﬀerent telephone numbers it
supports.
```

**5** 

```
5. Describe the diﬀerent models used to model the dis-
tribution of particles in statistical mechanics, including
Maxwell–Boltzmann, Bose–Einstein, and Fermi–Dirac
statistics. In each case, describe the counting techniques
used in the model.
```

**8** 

```
8. Describe the latest discoveries of values and bounds for
Ramsey numbers.
```

**9** 

```
9. Describe additional ways to generate all the permutations
of a set with n elements besides those found in Section
6.6. Compare these algorithms and the algorithms de-
scribed in the text and exercises of Section 6.6 in terms
of their computational complexity.
```


---

## 章末自检清单

- [ ] 4 大计数原理的判定
- [ ] 鸽巢原理（基本 + 广义）
- [ ] **P(n,r) 和 C(n,r)** 公式
- [ ] **Pascal 恒等式**（必考）
- [ ] **二项式定理**（必考）
- [ ] **可重组合**（**必考大题**）
- [ ] **不可区分对象**（**必考大题**）
- [ ] 可重排列 n^r
