# 第二章 基本结构（集合、函数、序列、矩阵）

> **考试分值**：4 题 / 30 分（与 Ch1、Ch9 共出 4 题，本章约 1-2 题）
> **考纲 section**：2.1, 2.2, 2.3, 2.4, 2.5, 2.6（**全考**）
> **作业覆盖**：2.1/2.3/2.4/2.5/2.6（无 2.2 作业），共 37 道必做题

## 反复出现的考点

| 排名 | 考点 | 频次 |
|---|---|---|
| ★★★ | **2.3 单/满/双射判定** | 4 |
| ★★★ | **2.3 构造单/满/双射例子** | 1（必考） |
| ★★☆ | **2.5 证明可数（构造双射）** | 3 |
| ★★☆ | **2.5 证明不可数** | 2 |
| ★★☆ | **2.1 集合运算** | 6 |
| ★☆☆ | **2.4 求和公式** | 5 |

> [!warning] 重点
> **2.3 函数判定** 和 **2.5 可数性** 是 Ch2 必考核心

---

## 2.1 集合

### 核心

- **子集**：A ⊆ B 当且仅当 ∀x(x ∈ A → x ∈ B)
- **真子集**：A ⊂ B 当且仅当 A ⊆ B 且 A ≠ B
- **幂集**：P(S) = 所有 A ⊆ S 的集合，**|P(S)| = 2^|S|**

### 反复错的点（作业 12 反复考）

```
∅ ∈ {∅}         ✓
∅ ⊂ {∅}         ✓
{∅} ⊆ {∅}       ✓
{∅} ∈ {∅}       ✗
```

> [!tip] ∈ 是"是...的元素"，⊆ 是"是...的子集"

### 配套作业

**必做题（7 题）：**

**8** 

```
8. Suppose that A ={ 2, 4, 6}, B ={ 2, 6}, C ={ 4, 6},a n d
D ={ 4, 6, 8}. Determine which of these sets are subsets
of which other of these sets.
```

**12** 

```
12. Determine whether these statements are true or false.
a) ∅∈{ ∅ } b) ∅∈{ ∅,{∅}}
c) {∅} ∈ {∅} d) {∅} ∈ {{∅}}
e) {∅}⊂ {∅,{∅}} f) {{∅}}⊂ {∅,{∅}}
g) {{∅}}⊂ {{∅},{∅}}
```

**22** 

```
22. What is the cardinality of each of these sets?
a) ∅ b) {∅}
c) {∅,{∅}} d) {∅,{∅},{∅,{∅}}}
```

**24** 

```
24. Can you conclude that A = B if A and B are two sets with
t h es a m ep o w e rs e t ?
```

**26** 

```
26. Determine whether each of these sets is the power set of
as e t ,w h e r ea and b are distinct elements.
a) ∅ b) {∅,{a}}
c) {∅,{a},{∅,a}} d) {∅,{a},{b},{a, b}}
```

**34** 

```
34. Let A ={ a, b, c}, B ={ x, y},a n dC ={ 0, 1}.F i n d
a) A× B× C. b) C× B× A.
c) C× A× B. d) B× B× B.
```

**46** 

```
46. Translate each of these quantiﬁcations into English and
determine its truth value.
a) ∃x∈R (x3 =−1) b) ∃x∈Z (x+ 1 > x)
c) ∀x∈Z (x−1 ∈Z) d) ∀x∈Z (x2 ∈Z)
```


---

## 2.2 集合运算

> **本章未布置 2.2 作业**。集合运算是 Ch6 计数的前置，必须掌握

### 5 种运算

| 运算 | 记号 | 定义 |
|---|---|---|
| 交集 | A ∩ B | {x : x ∈ A 且 x ∈ B} |
| 并集 | A ∪ B | {x : x ∈ A 或 x ∈ B} |
| 差集 | A - B | {x : x ∈ A 且 x ∉ B} |
| 补集 | Ā | {x : x ∉ A} |
| 对称差 | A ⊕ B | (A - B) ∪ (B - A) |

### 必背恒等式

| 名称 | 公式 |
|---|---|
| 交换律 | A ∪ B = B ∪ A |
| 结合律 | (A∪B)∪C = A∪(B∪C) |
| 分配律 | A∪(B∩C) = (A∪B)∩(A∪C) |
| 德摩根律 | A∩B 的补 = Ā∪B̄ |
| 吸收律 | A∪(A∩B) = A |

---

## 2.3 函数（**必考重点**）

### 三大类型判定

| 类型 | 条件 | 判定 |
|---|---|---|
| **单射** | f(a)=f(b) → a=b | 不同输入 → 不同输出 |
| **满射** | ∀y∈B ∃x∈A: f(x)=y | B 每个元素都有原像 |
| **双射** | 单射 + 满射 | 都满足 |

> [!warning] 有限集 A, B：**|A| = |B|** 且 f 单射 ↔ f 是双射

### 反复考的题型 1：判断 Z→Z 函数是否单射

```
a) f(n) = n-1          单射 ✓（f(a)=f(b) → a-1=b-1 → a=b）
b) f(n) = n²+1         不是单射 ✗（f(1)=f(-1)=2）
c) f(n) = n³           单射 ✓
d) f(n) = ⌈n/2⌉        不是单射 ✗（f(0)=f(1)=1）
```

> [!tip] 单射判定
> - 一次函数：单射
> - 二次函数：不是单射
> - 奇数次幂：单射
> - 取整函数：不是单射

### 反复考的题型 2：判断 Z×Z→Z 函数是否满射

```
a) f(m,n) = 2m-n       满射 ✓（任意 z = 2·0 - (-z) = z）
b) f(m,n) = m²-n²      不是满射 ✗（奇数无法表示）
c) f(m,n) = m+n+1      满射 ✓
d) f(m,n) = |m|-|n|     不是满射 ✗（值域 ≥ 0）
e) f(m,n) = m²-4       不是满射 ✗（值域 ≥ -4）
```

### 反复考的题型 3：构造单/满/双射例子（**必考**）

```
a) 单射不满射（N→N）：f(n) = 2n（值域只有偶数）
b) 满射不单射（N→N）：f(1)=1, f(n)=n-1 for n>1
c) 双射（N→N）：f(n) = n+1（不是恒等）
d) 既不单也不满（N→N）：f(n) = ⌊n/2⌋
```

> [!tip]
> - 单射不满射：值域比定义域小（如 f(n)=2n）
> - 满射不单射：多个输入映到同一输出

### 反复考的题型 4：判断双射 R→R

```
a) f(x) = -3x+4       双射 ✓（一次函数）
b) f(x) = -3x²+7      不是双射 ✗（二次函数）
c) f(x) = (x+1)/(x+2) 不是双射 ✗（x=-2 无定义）
d) f(x) = x⁵+1        双射 ✓（奇数次幂严格单调）
```

### 配套作业

**必做题（13 题）：**

**10** 

```
10. Determine whether each of these functions from
{a, b, c, d} to itself is one-to-one.
a) f (a) = b, f (b) = a, f (c) = c, f (d) = d
b) f (a) = b, f (b) = b, f (c) = d, f (d) = c
c) f (a) = d, f (b) = b, f (c) = c, f (d) = d
```

**12** 

```
12. Determine whether each of these functions from Z to Z
is one-to-one.
a) f (n) = n−1 b) f (n) = n2 + 1
c) f (n) = n3 d) f (n) = ⌈n∕2⌉
```

**14** 

```
14. Determine whether f : Z× Z → Z is onto if
a) f (m, n)= 2m−n.
b) f (m, n)= m2 −n2.
c) f (m, n)= m+ n+ 1.
d) f (m, n)= |m|−|n|.
e) f (m, n)= m2 −4.
```

**20** 

```
20. Give an example of a function from N to N that is
a) one-to-one but not onto.
b) onto but not one-to-one.
c) both onto and one-to-one (but diﬀerent from the iden-
tity function).
d) neither one-to-one nor onto.
```

**22** 

```
22. Determine whether each of these functions is a bijection
from R to R.
a) f (x) =−3x+ 4
b) f (x) =−3x
2 + 7
c) f (x) = (x+ 1)∕(x+ 2)
d) f (x) = x5 + 1
```

**24** 

```
24. Let f : R → R and let f (x) > 0f o ra l lx ∈R. Show that
f (x) is strictly increasing if and only if the functiong(x) =
1∕f(x) is strictly decreasing.
```

**30** 

```
30. Let S ={ −1, 0, 2, 4, 7}.F i n df (S)i f
a) f (x) = 1. b) f (x) = 2x+ 1.
c) f (x) = ⌈x∕5⌉. d) f (x)=⌊(x
2 + 1)∕3⌋.
```

**36**（精选版未找到，请查 PDF）

**37**（精选版未找到，请查 PDF）

**38** 

```
38. Find f ◦gand g◦f,w h e r ef (x) = x2 + 1a n dg(x) = x+ 2,
are functions from R to R.
```

**44** 

```
44. Let f be the function from R to R deﬁned by
f (x) = x2.F i n d
a) f−1({1}). b) f−1({x ∣0 < x < 1}).
c) f−1({x ∣x > 4}).
```

**46** 

```
46. Let f be a function fromA to B.L e tS and T be subsets of
B. Show that
a) f−1(S∪T) = f−1(S)∪f−1(T).
b) f−1(S∩T) = f−1(S)∩f−1(T).
```

**72** 

```
72. Suppose that f is an invertible function from Y to Z and
g is an invertible function from X to Y. Show that the
inverse of the composition f ◦g i sg i v e nb y(f ◦g)−1=
g−1◦f−1.
```


---

## 2.4 序列与求和

### 必背求和公式

$\sum_{i=1}^{n} i = \frac{n(n+1)}{2}$

$\sum_{i=1}^{n} i^2 = \frac{n(n+1)(2n+1)}{6}$

$\sum_{i=1}^{n} i^3 = \left(\frac{n(n+1)}{2}\right)^2$

### 配套作业

**必做题（5 题）：**

**10(d)(e)** （小问：d, e）

```
10. Find the ﬁrst six terms of the sequence deﬁned by each
of these recurrence relations and initial conditions.
a) an =−2an−1, a0 =−1
b) an = an−1−an−2, a0 = 2, a1 =−1
c) an = 3a2
n−1,a 0 = 1
d) an = nan−1+ a2
n−2
,a 0 =−1,a 1 = 0
e) an = an−1−an−2+ an−3,a 0 = 1,a 1 = 1,a 2 = 2
```

**12(d)** （小问：d）

```
12. Show that the sequence {an} is a solution of the recur-
rence relation an =−3an−1+ 4an−2if
a) an = 0. b) an = 1.
c) an = (−4)n. d) an = 2(−4)n + 3.
```

**16(f)(g)** （小问：f, g）

```
16. Find the solution to each of these recurrence relations
with the given initial conditions. Use an iterative ap-
proach such as that used in Example 10.
a) a
n =−an−1,a 0 = 5
b) an = an−1+ 3,a 0 = 1
c) an = an−1−n, a0 = 4
d) an = 2an−1−3,a 0 =−1
e) an = (n+ 1)an−1,a 0 = 2
f) an = 2nan−1,a 0 = 3
g) an =−an−1+ n−1,a 0 = 7
```

**18** 

```
18. A person deposits $1000 in an account that yields 9% in-
terest compounded annually.
a) Set up a recurrence relation for the amount in the ac-
count at the end of n years.
b) Find an explicit formula for the amount in the account
at the end of n years.
c) How much money will the account contain after 100
years?
```

**20** 

```
20. Assume that the population of the world in 2017 was 7.6
billion and is growing at the rate of 1.12% a year.
a) Set up a recurrence relation for the population of theLinks world n years after 2017.
b) Find an explicit formula for the population of the
world n years after 2017.
c) What will the population of the world be in 2050?
```


**仅需读（1 题）：**

**11(read)**  **[仅读]**

```
11. Let an = 2n + 5 ⋅3n for n = 0, 1, 2,… .
a) Find a0,a 1,a 2,a 3, and a4.
b) Show that a2 = 5a1 −6a0,a 3 = 5a2 −6a1,a n da4 =
5a3 −6a2.
c) Show that an = 5an−1−6an−2 for all integers n with
n ≥ 2.
```


---

## 2.5 基数（**必考**）

### 反复考的核心 1：证明集合可数（构造双射）

**方法**：构造显式双射 f: ℕ → S

**典型例子**：

- 奇正整数 {1, 3, 5, ...}：f(n) = 2n-1
- 负整数 {-1, -2, -3, ...}：f(n) = -n
- 所有整数 ℤ：奇偶交错

### 反复考的核心 2：证明集合不可数（Cantor 对角线法）

```
假设 [0,1] 中所有实数可数：r₁, r₂, r₃, ...
每个 rᵢ 写为十进制 0.d₁d₂d₃...
构造 s = 0.d'₁d'₂d'₃... 其中 d'ᵢ = 5 if dᵢ≠5 else 4
则 s ≠ rᵢ（因为第 i 位不同）→ s 不在列表中 → 矛盾
```

> [!warning] 不能用"5"，因为 0.5555... = 0.5556，要用"5 或 4"交替

### 配套作业

**必做题（5 题）：**

**15** 

```
15. Show that if A and B are sets, A is uncountable, and
A ⊆B,t h e nB is uncountable.
```

**16** 

```
16. Show that a subset of a countable set is also countable.
```

**17** 

```
17. If A is an uncountable set and B is a countable set, must
A−B be uncountable?
```

**27**（精选版未找到，请查 PDF）

**28** 

```
28. Show that the set Z+ × Z+ is countable.
∗ 29. Show that the set of all ﬁnite bit strings is countable.
∗ 30. Show that the set of real numbers that are solutions of
quadratic equations ax2 + bx+ c = 0, where a, b,a n dc
are integers, is countable.
∗ 31. Show that Z+ × Z+ is countable by showing that the
polynomial function f : Z+ × Z+ → Z+ with f (m, n)=
(m+ n−2)(m+ n−1)∕2+ m is one-to-one and onto.
∗ 32. Show that when you substitute (3n+ 1)2 for each occur-
rence of n and (3m+ 1)2 for each occurrence of m in the
right-hand side of the formula for the function f (m, n)i n
Exercise 31, you obtain a one-to-one polynomial func-
tion Z× Z → Z. It is an open question whether there is a
one-to-one polynomial function Q× Q → Q.
```


---

## 2.6 矩阵

### 矩阵乘法（必考）

C = AB，其中 cᵢⱼ = Σₖ aᵢₖ bₖⱼ

> [!warning] 矩阵乘法**不交换**：AB ≠ BA

### 布尔矩阵

- 元素 ∈ {0,1}，用 ∨ 和 ∧
- **布尔积** A⊙B：(A⊙B)ᵢⱼ = ∨ₖ(aᵢₖ ∧ bₖⱼ)

### 配套作业

**必做题（7 题）：**

**2(b)** （小问：b）

```
2. Research where the concept of a function ﬁrst arose, and
describe how this concept was ﬁrst used.
```

**3(c)** （小问：c）

```
3. Explain the diﬀerent ways in which the Encyclopedia of
Integer Sequences has been found useful. Also, describe
a few of the more unusual sequences in this encyclopedia
and how they arise.
```

**4(b)(c)** （小问：b, c）

```
4. Deﬁne the recently invented EKG sequence and describe
some of its properties and open questions about it.
```

**6** 

```
6. Expand the discussion of the continuum hypothesis in the
text.
```

**18** 

```
18. Show that if n is an integer, then n = ⌈n∕2⌉+⌊n∕2⌋.
```

**26** 

```
26. Prove that if m and n are positive integers and x is a real
number, then
⌊⌊x⌋+ n
m
⌋
=
⌊x+ n
m
⌋
.
∗27. Prove that ifm is a positive integer andx is a real number,
then
⌊mx⌋= ⌊x⌋+
⌊
x+ 1
m
⌋
+
⌊
x+ 2
m
⌋
+ ⋯
+
⌊
x+ m−1
m
⌋
.
∗28. We deﬁne the Ulam numbers by setting u1 = 1a n du2 =
```

**28** 

```
28. Find the Boolean product of A and B,w h e r e
A =
⎡
⎢
⎢⎣
1001
0101
1111
⎤
⎥
⎥⎦
and B =
⎡
⎢
⎢
⎢⎣
10
01
11
10
⎤
⎥
⎥
⎥⎦
.
```


---

## 章末自检清单

- [ ] ∅ vs {∅} 区别
- [ ] 单/满/双射判定
- [ ] 构造单/满/双射例子
- [ ] 3 个 Σ 公式
- [ ] **构造双射证可数**（必考）
- [ ] **Cantor 对角线法证不可数**（必考）
- [ ] 矩阵乘法
