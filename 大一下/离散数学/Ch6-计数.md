# 第六章 计数

> **考试分值**：$score
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

$hw_61

---

## 6.2 鸽巢原理

### 两个版本

| 版本 | 公式 | 含义 |
|---|---|---|
| **基本** | n 物体放 k 盒，n > k → 必有一盒 ≥ 2 | 物体比盒子多 |
| **广义** | n 物体放 k 盒 → 必有一盒 ≥ ⌈n/k⌉ | 平均分配最均匀 |

### 配套作业

$hw_62

---

## 6.3 排列与组合

### 必背公式

$$P(n, r) = n(n-1)(n-2)\cdots(n-r+1) = \frac{n!}{(n-r)!}$$

$$\binom{n}{r} = \frac{n!}{r!(n-r)!}$$

### 反复考判定

| 题型 | 选 P 还是 C |
|---|---|
| 排队、座位、密码（有顺序） | **P(n,r)** |
| 选人、选菜、选委员（无顺序） | **C(n,r)** |

### 配套作业

$hw_63

---

## 6.4 二项式系数

### 必背

#### Pascal 恒等式

$$\binom{n}{k} = \binom{n-1}{k-1} + \binom{n-1}{k}$$

#### 二项式定理

$$(x+y)^n = \sum_{k=0}^{n} \binom{n}{k} x^{n-k} y^k$$

> [!warning] x 的指数是 n-k（不是 k）

#### 常用求和

$$\sum_{k=0}^{n} \binom{n}{k} = 2^n$$

### 配套作业

$hw_64

---

## 6.5 广义排列与组合（**核心必考**）

### 3 个核心公式

| 类型 | 公式 | 关键判别 |
|---|---|---|
| **可重排列** | n^r | 元素可重复，**有序** |
| **可重组合** | $\binom{n+r-1}{r}$ | 元素可重复，**无序** |
| **不可区分对象** | $\frac{n!}{n_1!\, n_2!\, \cdots\, n_k!}$ | n 个对象分 k 类，nᵢ 不可区分 |

### 反复考的题型 1：可重组合（**必考大题**）

**公式**：从 n 类元素中**无序**取 r 个（每类可重复）

$$\binom{n+r-1}{r}$$

**典型**：从 4 种水果买 6 个，有多少种买法（数量不限）？

```
= C(4+6-1, 6) = C(9, 6) = 84
```

> [!tip] "**星星-竖线**"法：6 个星星 + 3 条竖线 = 9 个位置选 3 条放竖线 = C(9,3)

### 反复考的题型 2：不可区分对象排列（**必考大题**）

**公式**：n 个对象分成 k 类（nᵢ 个不可区分）：

$$\frac{n!}{n_1!\, n_2!\, \cdots\, n_k!}$$

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

$hw_65

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
