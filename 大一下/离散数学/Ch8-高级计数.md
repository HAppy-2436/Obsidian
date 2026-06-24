# 第八章 高级计数技术

> **考试分值**：6 题 / 45 分（与 Ch6 共出 6 题，本章约 3 题）
> **考纲 section**：8.1, 8.2, 8.3, 8.4, 8.5, 8.6（**全考**）
> **作业覆盖**：8.1, 8.2, 8.4, 8.5, 8.6（无 8.3 作业），共 33 道必做题

## 反复出现的考点

| 排名 | 考点 | 频次 |
|---|---|---|
| ★★★ | **8.2 特征方程解线性递推** | 10+ |
| ★★★ | **8.5/8.6 容斥原理** | 7+ |
| ★★★ | **8.4 生成函数解递推** | 13 |
| ★★☆ | **8.1 递推建模** | 5 |
| ★★☆ | **8.3 主定理** | 0（**但必考**） |

> [!warning] **8.2 特征方程** 和 **8.5/8.6 容斥** 是必考核心
> **8.3 主定理** 虽然没作业但必考

---

## 8.1 递推关系初步

### 反复考的：递推建模

```
作业 2 典型：银行存款（每年存 1 万，年利率 r%）
Bₙ = Bₙ₋₁ + 10000 + r%·Bₙ₋₁ = (1+r)Bₙ₋₁ + 10000

作业 8 典型：Hanoi 塔
Hₙ = 2Hₙ₋₁ + 1, H₁ = 1

作业 12 典型：集合大小
Sₙ = 2Sₙ₋₁ - 1
```

### 配套作业

**必做题（5 题）：**

**2** 

```
2. a) Find a recurrence relation for the number of permu-
tations of a set with n elements.
b) Use this recurrence relation to ﬁnd the number of per-
mutations of a set with n elements using iteration.
```

**4** 

```
4. A country uses as currency coins with values of 1 peso,
2 pesos, 5 pesos, and 10 pesos and bills with values of
5 pesos, 10 pesos, 20 pesos, 50 pesos, and 100 pesos.
Find a recurrence relation for the number of ways to pay
a bill of n pesos if the order in which the coins and bills
are paid matters.
```

**8** 

```
8. a) Find a recurrence relation for the number of bit strings
of length n that contain three consecutive 0s.
b) What are the initial conditions?
c) How many bit strings of length seven contain three
consecutive 0s?
```

**10**（精选版未找到，请查 PDF）

**12** 

```
12. a) Find a recurrence relation for the number of ways to
climb n stairs if the person climbing the stairs can take
one, two, or three stairs at a time.
b) What are the initial conditions?
c) In how many ways can this person climb a ﬂight of
eight stairs?
A string that contains only 0s, 1s, and 2s is called a ternary
string.
```


**仅需读（1 题）：**

**11(read)**  **[仅读]**

```
11. a) Find a recurrence relation for the number of ways to
climb n stairs if the person climbing the stairs can take
one stair or two stairs at a time.
b) What are the initial conditions?
c) In how many ways can this person climb a ﬂight of
eight stairs?
```


---

## 8.2 特征方程解线性递推（**核心必考**）

### 二阶齐次线性递推

**形式**：aₙ = c₁aₙ₋₁ + c₂aₙ₋₂

**解法**：

1. 写**特征方程**：x² = c₁x + c₂ → x² - c₁x - c₂ = 0
2. 求**特征根** r₁, r₂
3. **通解**：

| 根的情况 | 通解 |
|---|---|
| 两个不同实根 r₁, r₂ | aₙ = αr₁ⁿ + βr₂ⁿ |
| 两个相同实根 r | aₙ = (α + βn)rⁿ |

4. 用初始条件 a₀, a₁ 求 α, β

### 反复考的题型 1：典型题目（作业 22-36 反复出）

**作业 22 典型**：aₙ = 6aₙ₋₁ - 11aₙ₋₂ + 6aₙ₋₃

```
特征方程：x³ - 6x² + 11x - 6 = 0
         (x-1)(x-2)(x-3) = 0
         根：r=1, 2, 3
通解：aₙ = α·1ⁿ + β·2ⁿ + γ·3ⁿ
```

**作业 28 典型**：Fibonacci

```
Fₙ = Fₙ₋₁ + Fₙ₋₂, F₁=F₂=1
特征方程：x² = x + 1
         x = (1±√5)/2
通解：Fₙ = α[(1+√5)/2]ⁿ + β[(1-√5)/2]ⁿ
```

### 非齐次线性递推

**形式**：aₙ = c₁aₙ₋₁ + c₂aₙ₋₂ + F(n)

**解法**：

1. 先解对应齐次方程
2. 找**特解** aₙ⁽ᵖ⁾（形式由 F(n) 决定）
3. 通解 = 齐次通解 + 特解

**特解形式表**（必背）：

| F(n) 形式 | 特解 aₙ⁽ᵖ⁾ 形式 |
|---|---|
| C（常数） | A（常数） |
| Cn | An + B |
| Cn² | An² + Bn + C |
| dⁿ (d 不是特征根) | Adⁿ |
| dⁿ (d 是特征根) | Andⁿ |

### 配套作业

**必做题（6 题）：**

**2(g)** （小问：g）

```
2. Determine which of these are linear homogeneous recur-
rence relations with constant coeﬃcients. Also, ﬁnd the
degree of those that are.
a) a
n = 3an−2 b) an = 3
c) an = a2
n−1 d) an = an−1+ 2an−3
e) an = an−1∕n
f) an = an−1+ an−2 + n+ 3
g) an = 4an−2+ 5an−4+ 9an−7
```

**4(g)** （小问：g）

```
4. Solve these recurrence relations together with the initial
conditions given.
a) an = an−1+ 6an−2for n ≥ 2, a0 = 3, a1 = 6
b) an = 7an−1−10an−2for n ≥ 2, a0 = 2, a1 = 1
c) an = 6an−1−8an−2for n ≥ 2, a0 = 4, a1 = 10
d) an = 2an−1−an−2for n ≥ 2, a0 = 4, a1 = 1
e) an = an−2for n ≥ 2, a0 = 5, a1 =−1
f) an =−6an−1−9an−2for n ≥ 2, a0 = 3, a1 =−3
g) an+2 =−4an+1 + 5an for n ≥ 0, a0 = 2, a1 = 8
```

**12** 

```
12. Find the solution to an = 2an−1+ an−2−2an−3
for n = 3, 4, 5,… , with a0 = 3, a1 = 6, and a2 = 0.
```

**14** 

```
14. Find the solution to an = 5an−2−4an−4 with a0 = 3,
a1 = 2, a2 = 6, and a3 = 8.
```

**18** 

```
18. Solve the recurrence relation a
n = 6an−1−12an−2+
8an−3with a0 =−5,a 1 = 4, and a2 = 88.
```

**20** 

```
20. Find the general form of the solutions of the recurrence
relation an = 8an−2−16an−4.
```


---

## 8.3 主定理（**Master Theorem**）

> [!warning] **8.3 没有作业但必考**！

### 主定理形式

T(n) = aT(n/b) + f(n)，设 f(n) = Θ(n^c log^k n)

| 情况 | 条件 | 结论 |
|---|---|---|
| **1** | f(n) = O(n^c log^k n) 且 c < log_b a | T(n) = Θ(n^(log_b a)) |
| **2** | f(n) = Θ(n^c log^k n) 且 c = log_b a | T(n) = Θ(n^c log^(k+1) n) |
| **3** | f(n) = Ω(n^c log^k n) 且 c > log_b a 且正则条件 | T(n) = Θ(f(n)) |

### 反复考的判定（必考）

**例子**：T(n) = 4T(n/2) + n²

```
a=4, b=2, f(n)=n²
log_b a = log₂ 4 = 2
c = 2
f(n) = Θ(n²·log⁰n)
c = log_b a → 情况 2
T(n) = Θ(n² log n)
```

**例子**：T(n) = 2T(n/2) + n

```
a=2, b=2, f(n)=n
log_b a = 1
c = 1
c = log_b a → 情况 2
T(n) = Θ(n log n)
```

> [!tip] 速记
> - c < log_b a：**分治占主导** → Θ(n^(log_b a))
> - c = log_b a：**两项均衡** → Θ(n^c log^(k+1) n)
> - c > log_b a：**归并步骤占主导** → Θ(f(n))

### 配套练习（无作业，自练）

```
T(n) = 2T(n/2) + n³        → 情况 3，Θ(n³)
T(n) = 8T(n/2) + n²        → 情况 1，Θ(n³)
T(n) = 9T(n/3) + n²        → 情况 2，Θ(n² log n)
```

---

## 8.4 生成函数（**必考**）

### 反复考的：用生成函数解递推

**形式**：

$$
G(x) = a_0 + a_1 x + a_2 x^2 + \cdots = \sum_{n=0}^{\infty} a_n x^n
$$

**步骤**：

1. 用递推关系把 G(x) 写成封闭形式（通常是分式）
2. **部分分式分解**
3. 展开成幂级数，读出 aₙ 系数

### 反复考的题型 1：简单递推 aₙ = 2aₙ₋₁, a₀ = 1

```
G(x) = 1 + 2x + 4x² + 8x³ + ... = 1/(1-2x)
aₙ = 2ⁿ
```

### 反复考的题型 2：Fibonacci（作业 14 反复考）

```
递推：Fₙ = Fₙ₋₁ + Fₙ₋₂, F₀=0, F₁=1
G(x) = x/(1-x-x²)
部分分式分解 → Fₙ = (1/√5)[φⁿ - (1-φ)ⁿ]
```

### 反复考的题型 3：组合计数（作业 20, 22, 24）

```
用生成函数求"放球入盒"的方案数
例：n 个不可区分的球放 4 个可区分盒，每盒 0+ 个 → 系数 = C(n+3, 3)
```

### 配套作业

**必做题（13 题）：**

**32(e)** （小问：e）

```
32. If G(x) is the generating function for the sequence {a
k},
what is the generating function for each of these se-
quences?
a) 2a
0,2 a1,2 a2,2 a3,…
b) 0, a0, a1, a2, a3, … (assuming that terms follow the
pattern of all but the ﬁrst term)
c) 0, 0, 0, 0, a2, a3, … (assuming that terms follow the
pattern of all but the ﬁrst four terms)
d) a2, a3, a4,…
e) a1,2 a2,3 a3,4 a4,… [Hint: Calculus required here.]
f) a2
0,2 a0a1, a2
1
+ 2a0a2,2 a0a3 + 2a1a2,2 a0a4 +
2a1a3 + a2
2
,…
```

**38** 

```
38. Use generating functions to solve the recurrence relation
ak = ak−1+ 2ak−2+ 2k with initial conditionsa0 = 4a n d
a1 = 12.
```

**40** 

```
40. Use generating functions to solve the recurrence rela-
tion a
k = 2ak−1+ 3ak−2+ 4k + 6 with initial conditions
a0 = 20, a1 = 60.
```

**2** 

```
2. Find the generating function for the ﬁnite sequence 1, 4,
16, 64, 256.
In Exercises 3–8, by a closed form we mean an algebraic ex-
pression not involving a summation over a range of values or
the use of ellipses.
```

**4(e)** （小问：e）

```
4. Find a closed form for the generating function for each of
these sequences. (Assume a general form for the terms of
the sequence, using the most obvious choice of such a se-
quence.)
a) −1,−1,−1,−1,−1,−1,−1, 0, 0, 0, 0, 0, 0,…
b) 1, 3, 9, 27, 81, 243, 729,…
c) 0, 0, 3,−3, 3,−3, 3,−3,…
d) 1, 2, 1, 1, 1, 1, 1, 1, 1, …
e)
(
7
0
)
,2
(
7
1
)
,2
2
(
7
2
)
,… , 2
7
(
7
7
)
,0 ,0 ,0 ,0 , …
f) −3, 3,−3, 3,−3, 3,…
g) 0, 1, −2, 4,−8, 16,−32, 64,…
h) 1, 0, 1, 0, 1, 0, 1, 0, …
```

**6(f)** （小问：f）

```
6. Find a closed form for the generating function for the se-
quence{an},w h e r e
a) an =−1f o ra l ln= 0, 1, 2,… .
b) an = 2n for n = 1, 2, 3, 4,… and a0 = 0.
c) an = n−1f o rn = 0, 1, 2,… .
d) an = 1∕(n+ 1)! for n = 0, 1, 2,… .
e) an =
(
n
2
)
for n = 0, 1, 2,… .
f) an =
(
10
n+ 1
)
for n = 0, 1, 2,… .
```

**8(f)(g)** （小问：f, g）

```
8. For each of these generating functions, provide a closed
formula for the sequence it determines.
a) (x2 + 1)3 b) (3x−1)3
c) 1∕(1−2x2) d) x2∕(1−x)3
e) x−1+ (1∕(1−3x)) f) (1+ x3)∕(1+ x)3
∗g) x∕(1+ x+ x2) h) e3x2
−1
```

**10(c)(d)(e)** （小问：c, d, e）

```
10. Find the coeﬃcient of x9 in the power series of each of
these functions.
a) (1+ x
3 + x6 + x9 + ⋯) 3
b) (x2 + x3 + x4 + x5 + x6 + ⋯) 3
c) (x3 + x5 + x6)(x3 + x4)(x+ x2 + x3 + x4 + ⋯)
d) (x+ x4 + x7 + x10 + ⋯)(x 2 + x4 + x6 + x8 + ⋯)
e) (1+ x+ x2)3
```

**12(d)** （小问：d）

```
12. Find the coeﬃcient of x12 in the power series of each of
these functions.
a) 1∕(1+ 3x) b) 1∕(1−2x)2
c) 1∕(1+ x)8 d) 1∕(1−4x)3
e) x3∕(1+ 4x)2
```

**14** 

```
14. Use generating functions to determine the number of dif-
ferent ways 12 identical action ﬁgures can be given to ﬁve
children so that each child receives at most three action
ﬁgures.
```

**20** 

```
20. What is the generating function for the sequence {ck},
where ck represents the number of ways to make change
for k pesos using bills worth 10 pesos, 20 pesos, 50 pesos,
and 100 pesos?
```

**22** 

```
22. Give a combinatorial interpretation of the coeﬃcient
of x6 in the expansion (1 + x+ x2 + x3 + ⋯) n.U s et h i s
interpretation to ﬁnd this number.
```

**24** 

```
24. a) What is the generating function for {ak},w h e r eak
is the number of solutions of x1 + x2 + x3 + x4 = k
when x1, x2, x3,a n dx4 are integers with x1 ≥ 3, 1 ≤
x2 ≤ 5, 0 ≤ x3 ≤ 4, and x4 ≥ 1?
b) Use your answer to part (a) to ﬁnd a7.
```


**仅需读（1 题）：**

**5(f)(read)** （小问：f） **[仅读]**

```
5. Find a closed form for the generating function for the se-
quence{a
n},w h e r e
a) an = 5f o ra l ln= 0, 1, 2,… .
b) an = 3n for all n = 0, 1, 2,… .
c) an = 2f o rn = 3, 4, 5,… and a0 = a1 = a2 = 0.
d) an = 2n+ 3f o ra l ln= 0, 1, 2,… .
e) an =
(
8
n
)
for all n = 0, 1, 2,… .
f) an =
(
n+ 4
n
)
for all n = 0, 1, 2,… .
```


---

## 8.5 容斥原理（PIE）（**核心必考大题**）

### 公式

| 集合数 | 公式 |
|---|---|
| 2 个 | |A∪B| = |A| + |B| - |A∩B| |
| 3 个 | |A∪B∪C| = |A|+|B|+|C| - |A∩B|-|A∩C|-|B∩C| + |A∩B∩C| |
| n 个 | 加单项（奇数个+），减两项交集（偶数个-），加三项交集，... |

### 反复考的题型 1：3 集合容斥

```
已知：
  |A|=1232, |B|=879, |C|=114
  |A∩B|=103, |A∩C|=23, |B∩C|=14
  |A∪B∪C|=2092
求：|A∩B∩C|

|A∪B∪C| = |A|+|B|+|C| - |A∩B|-|A∩C|-|B∩C| + |A∩B∩C|
2092 = 1232+879+114-103-23-14 + |A∩B∩C|
2092 = 2085 + |A∩B∩C|
|A∩B∩C| = 7
```

### 反复考的题型 2：错位排列（8.6 反复考，必考）

**公式**：

$$
D_n = n! \sum_{k=0}^{n} \frac{(-1)^k}{k!}
$$

**递推**：Dₙ = n Dₙ₋₁ + (-1)ⁿ, D₁ = 0

**前几项**：

| n | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| Dₙ | 0 | 1 | 2 | 9 | 44 | 265 |

> [!tip] 错位排列 = 没有任何元素在原位

### 反复考的题型 3：满射计数（8.6 反复考）

**公式**：n 元集到 k 元集的满射个数

$$
k! \, S(n, k)
$$

其中 S(n, k) 是**第二类 Stirling 数**

**第二类 Stirling 数递推**：

$$
S(n, k) = k \cdot S(n-1, k) + S(n-1, k-1)
$$

> [!warning] 满射数 = k! · S(n, k)，不是 kⁿ

### 配套作业

**必做题（5 题）：**

**2** 

```
2. There are 345 students at a college who have taken a
course in calculus, 212 who have taken a course in dis-
crete mathematics, and 188 who have taken courses in
both calculus and discrete mathematics. How many stu-
dents have taken a course in either calculus or discrete
mathematics?
```

**8** 

```
8. In a survey of 270 college students, it is found that 64 like
Brussels sprouts, 94 like broccoli, 58 like cauliﬂower,
26 like both Brussels sprouts and broccoli, 28 like both
Brussels sprouts and cauliﬂower, 22 like both broccoli
and cauliﬂower, and 14 like all three vegetables. How
many of the 270 students do not like any of these
vegetables?
```

**18** 

```
18. How many elements are in the union of four sets if
each of the sets has 100 elements, each pair of the sets
shares 50 elements, each three of the sets share 25 ele-
ments, and there are 5 elements in all four sets?
```

**20** 

```
20. How many terms are there in the formula for the number
of elements in the union of 10 sets given by the principle
of inclusion–exclusion?
```

**22** 

```
22. How many elements are in the union of ﬁve sets if the
sets contain 10,000 elements each, each pair of sets has
1000 common elements, each triple of sets has 100 com-
mon elements, every four of the sets have 10 common
elements, and there is 1 element in all ﬁve sets?
```


**必做题（4 题）：**

**2** 

```
2. Explain how the Fibonacci numbers arise in a variety of
applications, such as in phyllotaxis, the study of arrange-
ment of leaves in plants, in the study of reﬂections by
mirrors, and so on.
```

**3** 

```
3. Describe diﬀerent variations of the Tower of Hanoi
puzzle, including those with more than three pegs (in-
cluding the Reve’s puzzle discussed in the text and
exercises), those where disk moves are restricted, and
those where disks may have the same size. Include what
is known about the number of moves required to solve
each variation.
```

**4** 

```
4. Discuss as many diﬀerent problems as possible where the
Catalan numbers arise.
```

**5** 

```
5. Discuss some of the problems in which Richard Bellman
ﬁrst used dynamic programming.
```


---

## 章末自检清单

- [ ] 递推建模
- [ ] **特征方程解二阶/三阶齐次递推**（**必考**）
- [ ] 非齐次递推的特解形式
- [ ] **主定理三种情况判定**（**必考**）
- [ ] **生成函数解递推**（**必考**）
- [ ] **PIE 容斥公式**（**必考大题**）
- [ ] **错位排列 Dₙ 公式**（**必考**）
- [ ] **满射数 = k! S(n, k)**（**必考**）
