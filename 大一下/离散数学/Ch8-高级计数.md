# 第八章 高级计数技术（按知识点组织）

> **考试分值**：约 3 题 / 23 分（与 Ch6 合并）
> **考纲范围**：8.1, 8.2, 8.3, 8.4, 8.5, 8.6（全考）
> **必考三大块**：**8.2 特征方程** + **8.3 主定理** + **8.5/8.6 容斥**
> **总题数**：约 154 道

---

## 知识点地图

| 知识点 | 出处 | 频次 | 难度 |
|---|---|---|---|
| A1 递推关系建模 | 8.1 | ★★☆ | 中 |
| A2 **线性递推求解**（特征方程）| 8.2 | ★★★ | 难 |
| A3 **Master Theorem**（主定理）| 8.3 | ★★★ | 中 |
| A4 生成函数解递推 | 8.3, 8.4 | ★★☆ | 中 |
| A5 **容斥原理** | 8.4, 8.5 | ★★★ | 中 |
| A6 **容斥应用**（满射/错位/原函数）| 8.5, 8.6 | ★★★ | 难 |

---

# A1 递推关系建模

## 核心概念

**递推关系（recurrence relation）**：用 aₙ 与前面项的关系定义序列。

**初始条件**：a₀ 或 a₁ 的具体值。

**建模步骤**：
1. 定义 aₙ：明确含义
2. 找递推：第 n 步 = f(前面步骤)
3. 给初始条件

## 反复考的题型

### 题型 1：储蓄复利
aₙ = (1 + r) · aₙ₋₁，a₀ = 本金
解：aₙ = (1+r)ⁿ · 本金

### 题型 2：Tower of Hanoi
aₙ = 2aₙ₋₁ + 1，a₁ = 1
解：aₙ = 2ⁿ − 1

### 题型 3：含连续 0 的位串
aₙ = aₙ₋₁ + aₙ₋₂ + 2ⁿ⁻²（分最后一位是 1 还是 0 后面跟 1）

### 题型 4：找零钱数
aₙ = aₙ₋₁ + aₙ₋₅ + aₙ₋₁₀ + aₙ₋₂₅

## 配套作业

**Section 8.1**

**1.** A sequence is defined recursively by a₁ = 1, aₙ = aₙ₋₁ + 2 for n ≥ 2. Find a₃ and a₅.

**5.** A sequence is defined recursively by a₁ = 1, aₙ = 3aₙ₋₁ for n ≥ 2. Find a₃, a₅, and a₈.

**10.** A sequence is defined recursively by a₁ = 1, a₂ = 2, aₙ = aₙ₋₁ + 2aₙ₋₂ for n ≥ 3. Find a₃, a₄, and a₅.

**15.** Suppose that a person deposits $10,000 in a savings account at an annual interest rate of 5%, compounded yearly. Define a sequence that gives the amount of money in the account after n years. Find a formula for aₙ.

**20.** Find a closed formula for the sequence defined recursively by a₁ = 1, a₂ = 2, aₙ = aₙ₋₁ + 2aₙ₋₂ for n ≥ 3.

**25.** The Tower of Hanoi problem consists of n disks and three pegs. Find a recurrence relation for the number of moves required to solve the Tower of Hanoi problem.

**28.** A country uses coins of 1, 5, 10, and 25 cents. Find a recurrence relation for the number of ways to make change for n cents.

**34.** Find a recurrence relation for the number of bit strings of length n that contain a pair of consecutive 0's.

---

# A2 线性递推求解（特征方程）（**必考**）

## 核心概念

**齐次线性递推**：aₙ = c₁aₙ₋₁ + c₂aₙ₋₂ + ... + cₖaₙ₋ₖ

**特征方程**：xᵏ − c₁xᵏ⁻¹ − c₂xᵏ⁻² − ... − cₖ = 0

**求根**：解出特征根 r₁, r₂, ..., rₖ

**通解形式**（按根的情况）：

| 根的情况 | 通解 |
|---|---|
| k 个**不同**实根 | aₙ = α₁r₁ⁿ + α₂r₂ⁿ + ... + αₖrₖⁿ |
| 重根（r 重 t 次）| 加项 (α + βn + γn² + ... + δnᵗ⁻¹) rⁿ |
| 复数根 r = ρ(cos θ + i sin θ) | ρⁿ (α cos nθ + β sin nθ) |

**非齐次线性递推**：aₙ = c₁aₙ₋₁ + ... + cₖaₙ₋ₖ + F(n)

通解 = 齐次通解 + 非齐次特解

**特解猜测表**（必背）：

| F(n) 形式 | 特解尝试 |
|---|---|
| 常数 C | 常数 A（若 1 不是特征根）；否则 An |
| 多项式 Pₘ(n) | 同次多项式 Qₘ(n)；若 1 是重根则乘 n |
| αⁿ（α 非特征根）| Cαⁿ |
| αⁿ（α 是 t 重特征根）| (C₀ + C₁n + ... + Cₜ₋₁nᵗ⁻¹)αⁿ |
| (αⁿ)·Pₘ(n) | 复杂情况：综合上面规则 |

## 反复考的题型

### 题型 1：求齐次通解（最常考）

**模板**：

```
aₙ = 4aₙ₋₁ − 4aₙ₋₂，a₀=1, a₁=1

特征方程：x² − 4x + 4 = 0
          (x − 2)² = 0
          x = 2（重根 2 次）

通解：aₙ = (α + βn) · 2ⁿ

代入 a₀=1：α = 1
代入 a₁=1：(1 + β)·2 = 1 → β = −1/2

∴ aₙ = (1 − n/2) · 2ⁿ
```

### 题型 2：解非齐次递推

```
aₙ = 2aₙ₋₁ + 3·2ⁿ，a₀ = 1

特征方程：x − 2 = 0 → x = 2
齐次通解：α · 2ⁿ
F(n) = 3·2ⁿ，2 是单特征根
特解尝试：C·n·2ⁿ
代入：C·n·2ⁿ = 2·C(n−1)·2ⁿ⁻¹ + 3·2ⁿ
       C·n·2ⁿ = C(n−1)·2ⁿ + 3·2ⁿ
       Cn = Cn − C + 3
       C = 3
∴ aₙ = α·2ⁿ + 3n·2ⁿ
代入 a₀=1：α = 1
∴ aₙ = (1 + 3n) · 2ⁿ
```

### 题型 3：判断给定序列是否为解
逐项验证。

## 配套作业

**Section 8.2**

**1.** Determine whether the sequence {aₙ} is a solution of the recurrence relation aₙ = 2aₙ₋₁ − aₙ₋₂ for n ≥ 2 if
a) aₙ = 3n　b) aₙ = 2ⁿ　c) aₙ = 3　d) aₙ = n² + n　e) aₙ = 2ⁿ − 1

**5.** Find a recurrence relation for the number aₙ of n-bit strings with no two consecutive 0's.

**10.** Find the solution of the recurrence relation aₙ = 2aₙ₋₁ + 3·2ⁿ with initial condition a₀ = 1.

**15.** Solve the recurrence relation aₙ = aₙ₋₁ + 6aₙ₋₂ with initial conditions a₀ = 3, a₁ = 4.

**20.** Solve the recurrence relation aₙ = 4aₙ₋₁ − 4aₙ₋₂ with initial conditions a₀ = 1, a₁ = 1.

**25.** Solve the recurrence relation aₙ = 6aₙ₋₁ − 9aₙ₋₂ with initial conditions a₀ = 1, a₁ = 3.

**30.** Find a closed formula for the sequence defined by the recurrence relation aₙ = aₙ₋₁ + aₙ₋₂ + aₙ₋₃ with a₀ = 1, a₁ = 2, a₂ = 3.

**32.** Find the general form of the particular solution of aₙ = 6aₙ₋₁ − 9aₙ₋₂ + 3ⁿ² + n·3ⁿ.

---

# A3 Master Theorem（主定理）（**必考**）

## 核心概念

**分治递推形式**：

$$T(n) = aT(n/b) + f(n)$$

其中 a ≥ 1, b > 1 是常数，f(n) 是渐近正的函数。

**Master Theorem 三种情况**：

设临界指数 $c^* = \log_b a$。

| 情况 | 条件 | 结论 |
|---|---|---|
| **情况 1** | f(n) = O(n^(c*−ε)) 对某 ε > 0 | T(n) = Θ(n^c*) |
| **情况 2** | f(n) = Θ(n^c* · logᵏn) 对 k ≥ 0 | T(n) = Θ(n^c* · logᵏ⁺¹n) |
| **情况 3** | f(n) = Ω(n^(c*+ε)) 且 a·f(n/b) ≤ c·f(n) | T(n) = Θ(f(n)) |

**简化记忆法**：把 f(n) 与 n^(log_b a) 比较：
- f(n) **小得多**（多项式级别小）→ T(n) = Θ(n^(log_b a))
- f(n) **同级别** → T(n) = Θ(f(n) · log n)
- f(n) **大得多**（多项式级别大）+ **规则性条件** → T(n) = Θ(f(n))

## 反复考的题型

### 题型 1：套 Master Theorem

**模板**：

```
T(n) = 7T(n/2) + n²

a = 7, b = 2
n^(log_b a) = n^(log₂7) ≈ n^2.807

f(n) = n² = O(n^(2.807−ε)) → 情况 1

∴ T(n) = Θ(n^log₂7) ≈ Θ(n^2.807)
```

### 题型 2：判断 Master Theorem 是否适用
当 f(n) 不是多项式（如 n² log n）时，看是否能匹配三种情况之一。

**经典不可用情况**：T(n) = 4T(n/2) + n² log n
- n^(log₂4) = n²
- f(n) = n² log n：与 n² 差一个 log n 因子
- 情况 2 要求 f(n) = Θ(n^c* · logᵏn)，这里 k=1 ✓
- 所以 **可以用** → T(n) = Θ(n² log² n)

### 题型 3：递推求解（验证）

迭代法：T(n) = aT(n/b) + f(n) = a²T(n/b²) + af(n/b) + f(n) = ... → 几何级数求和

## 配套作业

**Section 8.3**

**1.** Use the iteration method to find an upper bound for the recurrence relation T(n) = 3T(n/2) + n, where T(1) = 1.

**5.** Use the master theorem to find a big-O estimate for T(n) = 7T(n/2) + n².

**10.** Can the master theorem be applied to the recurrence T(n) = 4T(n/2) + n² log n?

**15.** Use the master theorem to find a big-O estimate for T(n) = 4T(n/2) + n³.

**20.** Show that the solution of the recurrence T(n) = T(n/3) + 1 is O(log n).

---

# A4 生成函数解递推

## 核心概念

**步骤**：
1. 设 G(x) = ∑ₙ₌₀^∞ aₙxⁿ
2. 用递推关系两边乘 xⁿ，对 n 求和
3. 整理成 G(x) 的方程
4. 部分分式展开 G(x)
5. 系数即 aₙ

**常用展开**：

| G(x) | 系数 |
|---|---|
| 1/(1-x) | 1（n≥0）|
| 1/(1-αx) | αⁿ |
| x/(1-x)² | n（n≥1）|
| x/(1-x)³ | n²/2 |
| 1/(1-x)ᵏ | C(n+k-1, k-1) |

## 反复考的题型

### 题型 1：求序列生成函数
套公式表。

### 题型 2：解递推（与 A2 互补）

```
aₖ = 3aₖ₋₁ + 2，a₀ = 1

G(x) = a₀ + ∑ₖ≥1 (3aₖ₋₁ + 2)xᵏ
     = 1 + 3x·G(x) + 2x/(1-x)

(1-3x)G(x) = 1 + 2x/(1-x) = (1-x+2x)/(1-x) = (1+x)/(1-x)
G(x) = (1+x) / [(1-x)(1-3x)]
```

部分分式展开后求系数。

## 配套作业

**Section 8.3（续）**

**23.** Find the generating function for the sequence {aₙ}, where aₙ = 2ⁿ + 3, n ≥ 0.

**26.** Use generating functions to solve the recurrence relation aₖ = 3aₖ₋₁ + 2 for k ≥ 1 with a₀ = 1.

**30.** Use generating functions to solve the recurrence relation aₖ = 2aₖ₋₁ + 3ᵏ for k ≥ 1 with a₀ = 1.

---

# A5 容斥原理（**必考**）

## 核心概念

**容斥原理**（n 个集合）：

$$|A_1 \cup A_2 \cup \cdots \cup A_n| = \sum_i |A_i| - \sum_{i<j} |A_i \cap A_j| + \sum_{i<j<k} |A_i \cap A_j \cap A_k| - \cdots + (-1)^{n+1} |A_1 \cap \cdots \cap A_n|$$

**直观理解**：
- 加：每个 Aᵢ 算一次
- 减：重复算了两次的减去一次
- 加：被减多了的再加回
- ...

**n = 2** 情况：|A ∪ B| = |A| + |B| − |A ∩ B|

**n = 3 情况**（最常考）：

$$|A \cup B \cup C| = |A| + |B| + |C| - |A \cap B| - |A \cap C| - |B \cap C| + |A \cap B \cap C|$$

## 反复考的题型

### 题型 1：求不在集合中的元素数

```
1-1000 中不被 2、3、5 整除的数
= 1000 − |A₂ ∪ A₃ ∪ A₅|
A₂: 500, A₃: 333, A₅: 200
A₂∩A₃: 166, A₂∩A₅: 100, A₃∩A₅: 66
A₂∩A₃∩A₅: 33
|A₂ ∪ A₃ ∪ A₅| = 500+333+200−166−100−66+33 = 734
∴ 不被整除 = 1000 − 734 = 266
```

### 题型 2：满足多重限制的解数（带上限 xᵢ ≤ cᵢ）

**技巧**：先求总非负解数，再减去违反一个上限的解，再加回违反两个上限的解（容斥）。

### 题型 3：特定性质元素数

例：≤ 1000 中非完全平方也非完全立方 = 1000 − |A ∪ B|

## 配套作业

**Section 8.4**

**5.** Suppose that 100 college freshmen are surveyed about their course enrollments: 60 take English, 40 take Math, 30 take History, 20 take both English and Math, 15 take both English and History, 10 take both Math and History, and 5 take all three. How many take none of these courses?

**10.** Find the number of integers between 1 and 1000 that are not divisible by 2, 3, or 5.

**13.** How many bit strings of length 8 contain either three consecutive 0's or four consecutive 1's?

**16.** A professor asks her class to write a paper on a topic of interest. She lists 15 topics; 8 are in literature and 7 are in science. How many ways can a student choose a topic if the student must select a topic in either literature or science but not both?

**18.** How many solutions are there to the equation x₁ + x₂ + x₃ = 17 where each xᵢ is a positive integer and where x₁ ≤ 5, x₂ ≤ 6, and x₃ ≤ 7?

**19.** Find the number of positive integers less than 1000 that are not perfect squares or perfect cubes.

---

# A6 容斥应用（满射 / 错位排列）（**必考**）

## 核心概念

### 应用 1：满射计数

从 |A|=m 到 |B|=n 的满射数 = ∑ₖ₌₀ⁿ (-1)ᵏ C(n,k)(n−k)ᵐ

**记忆**：先选 k 个 B 元素被排除（让 f 不到），再算剩下 (n−k) 个像的函数个数 (n−k)ᵐ。

**特殊值**：
- m < n → 0（不可能满射）
- m = n → n!（排列）
- m = n+1 → C(n+1, 2) · n!

### 应用 2：错位排列（derangement）

n 个元素都不在原位的排列数：

$$D_n = n! \sum_{k=0}^{n} \frac{(-1)^k}{k!}$$

**递推**：Dₙ = (n−1)(Dₙ₋₁ + Dₙ₋₂)，D₁=0, D₂=1

**常用值**：

| n | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| Dₙ | 0 | 1 | 2 | 9 | 44 | 265 |

### 应用 3：欧拉 φ 函数

φ(n) = 1 到 n 中与 n 互素的整数个数

**公式**：n = p₁^a₁ · p₂^a₂ · ... · pₖ^aₖ，则

$$\varphi(n) = n \prod_{i=1}^{k} \left(1 - \frac{1}{p_i}\right)$$

## 反复考的题型

### 题型 1：满射数计算

```
6 个元素到 4 个元素的满射数
= ∑ₖ₌₀⁴ (-1)ᵏ C(4,k)(4−k)⁶
= C(4,0)·4⁶ − C(4,1)·3⁶ + C(4,2)·2⁶ − C(4,3)·1⁶ + C(4,4)·0⁶
= 4096 − 4·729 + 6·64 − 4·1 + 0
= 4096 − 2916 + 384 − 4
= 1560
```

### 题型 2：错位排列

```
n 个人帽子都放错位置 = Dₙ
D₅ = 5!(1 − 1 + 1/2 − 1/6 + 1/24 − 1/120)
    = 120 × (1 − 1 + 0.5 − 0.1667 + 0.0417 − 0.0083)
    = 120 × 0.3667 = 44
```

### 题型 3：环上座位（不相邻）

n 人围圆桌，Alice 不与 Bob 相邻：
- 总：(n−1)!
- Alice 在某位置，Bob 在 Alice 相邻：2 × (n−2)!（两方向）
- 相邻：2(n−2)!
- 不相邻：(n−1)! − 2(n−2)!

### 应用 4：分配问题（每员工至少一个工作）

5 个不同工作分给 4 个不同员工，每人至少一个：
- 满射数（员工是像，工作是源）
- = ∑ₖ₌₀⁴ (-1)ᵏ C(4,k)(4−k)⁵

## 配套作业

**Section 8.5**

**1.** How many onto functions are there from a set with six elements to a set with four elements?

**5.** How many ways are there to deal hands of 5 cards to each of four players from a standard 52-card deck?

**10.** How many solutions are there to the equation x₁ + x₂ + x₃ + x₄ = 17, where xᵢ are nonnegative integers with x₁ ≤ 2, x₂ ≤ 3, x₃ ≤ 4, x₄ ≤ 5?

**13.** How many ways are there to seat 8 people around a circular table if Alice and Bob must not sit next to each other?

**15.** How many ways are there to assign 5 different jobs to 4 different employees if every employee is assigned at least one job?

**17.** Find the number of onto functions from a set of 6 elements to a set of 3 elements.

**20.** Use the principle of inclusion–exclusion to derive a formula for the Euler phi function φ(n).

**22.** Find the number of primes less than 200 using the principle of inclusion–exclusion.

---

## 复习清单

- [ ] 建模 5 类：复利、Hanoi、位串、找零、兔子
- [ ] 齐次递推：特征方程 → 求根 → 通解（含重根、复根）
- [ ] 非齐次：齐次通解 + 特解（特解尝试表）
- [ ] 特解尝试：αⁿ 型（F(n) 含 αⁿ 时，若 α 是特征根要乘 n）
- [ ] Master Theorem 三情况：n^(log_b a) 与 f(n) 比较
- [ ] 情况 2：f(n) = Θ(n^(c*)·logᵏn) → Θ(n^(c*)·logᵏ⁺¹n)
- [ ] 情况 3：必须满足正则条件 a·f(n/b) ≤ c·f(n)
- [ ] 生成函数：(1-αx)⁻¹ ↔ αⁿ
- [ ] 容斥公式（n=2, n=3 必背）
- [ ] 满射数 = ∑(-1)ᵏ C(n,k)(n−k)ᵐ
- [ ] 错位 Dₙ = n!∑(-1)ᵏ/k!
- [ ] Dₙ 递推：Dₙ = (n−1)(Dₙ₋₁ + Dₙ₋₂)
- [ ] φ(n) = n·∏(1 − 1/pᵢ)