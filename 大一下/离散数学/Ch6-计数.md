# 第六章 计数（按知识点组织）

> **考试分值**：约 3 题 / 22 分（与 Ch8 合并）
> **考纲范围**：6.1, 6.2, 6.3, 6.4, 6.5, 6.6（全考）
> **必考重点**：6.5 广义组合（可重排列/可重组合/不可区分对象）
> **总题数**：约 222 道

---

## 知识点地图

| 知识点 | 出处 | 频次 | 难度 |
|---|---|---|---|
| C1 计数原理（乘法 + 加法）| 6.1 | ★★★ | 易 |
| C2 鸽巢原理 | 6.2 | ★★★ | 中 |
| C3 排列 P(n,r) + 组合 C(n,r) | 6.3 | ★★★ | 中 |
| C4 二项式定理 | 6.4 | ★★☆ | 中 |
| C5 **广义组合**（重复选取）| 6.5 | ★★★ | 难 |
| C6 生成函数 | 6.6 | ★★☆ | 中 |

---

# C1 计数原理（基础中的基础）

## 核心概念

**乘法原理**：依次完成 k 个独立步骤，每步分别有 n₁, n₂, ..., nₖ 种选择 → 总数 = n₁ × n₂ × ... × nₖ

**加法原理**：互斥的几种方法，分别有 n₁, n₂, ..., nₖ 种 → 总数 = n₁ + n₂ + ... + nₖ

**容斥原理**（计数版）：|A ∪ B| = |A| + |B| − |A ∩ B|

**常用公式**：

| 问题 | 公式 |
|---|---|
| n 个不同元素排成 r 位 | P(n,r) = n!/(n-r)! |
| n 个元素中选 r 个 | C(n,r) = n!/(r!(n-r)!) |
| 函数个数：A→B，|A|=m, |B|=n | n^m |
| 单射函数个数：A→B，|A|=m≤|B|=n | P(n,m) = n!/(n-m)! |
| 满射函数个数：A→B | 用容斥：∑ₖ₌₀ⁿ (-1)ᵏ C(n,k) (n-k)ᵐ |

## 反复考的题型

### 题型 1：序列/字符串计数
- 长度 k 的字符串：A→B，每个位置独立 → |B|^k
- 长度 k 不重复：单射 → P(|B|, k)

### 题型 2：函数/单射/满射计数
套上面公式。

### 题型 3：排列组合应用（具体情境）
画决策树，套乘法原理。

## 配套作业

**Section 6.1**

**3.** How many strings of four decimal digits
a) have exactly three digits that are 9?
b) begin with an odd digit and end with an even digit?
c) have no repeated digits?
d) have no repeated digits and begin and end with an odd digit?

**8.** How many license plates can be made using either two letters followed by four digits or three letters followed by three digits?

**15.** How many different functions are there from a set with m elements to a set with n elements?

**20.** How many one-to-one functions are there from a set with m elements to one with n elements, where m ≤ n?

**25.** In how many ways can a photographer at a wedding arrange 6 people in a row from a group of 10 people, where the bride and groom are among these 10 people, if
a) the bride must be in the picture?
b) the bride and groom must both be in the picture?
c) the bride and groom must be next to each other?

**30.** How many bit strings of length 10 contain
a) exactly four 1's?
b) at most four 1's?
c) at least four 1's?
d) an equal number of 0's and 1's?

**35.** How many subsets of {1, 2, 3, …, 100} have cardinality
a) 1?　b) 2?　c) 3?　d) at most 3?

---

# C2 鸽巢原理（PHP）

## 核心概念

**鸽巢原理**：n+1 个物体放入 n 个盒子，至少一个盒子有 ≥2 个物体。

**广义鸽巢原理**：n 个物体放入 k 个盒子，至少一个盒子有 ≥ ⌈n/k⌉ 个物体。

**反证法**：n+1 鸽 → n 巢 → 必有两个同巢。

## 反复考的题型

### 题型 1：直接应用
- "至少两个生日相同" → n+1 人，n 天 → 365+1 人保证同天
- "至少两个同月" → 13 人保证
- "至少两个 last digit 相同" → 11 个数

### 题型 2：广义 PHP
- "100 个整数，至少 20 个 last digit 相同" → ⌈100/10⌉ = 10... 不对，应该是 100/10 = 10。要"至少 20" → 用 ⌈n/k⌉ ≥ 20 → n ≥ 20k，需 ⌈100/10⌉ ≥ 10。要"至少 20 个"：需要 20k ≤ 100 + (k-1)，或用反证：假设每个 last digit 最多 19 个 → 总数 ≤ 190 > 100 反了？让我重看：100 个整数 last digit 0-9 共 10 个，假设每个最多 19 个，则总数 ≤ 190 ✓，不矛盾。实际 PHP：⌈100/10⌉ = 10，所以至少 10 个同 last digit。要至少 20 个：100/10=10，20>10，**不能直接**用 PHP。

题目原意：用广义 PHP 证明——把 100 个数分成 10 组（按 last digit），每组最大 19。假设每个 ≤ 19，总数 ≤ 190，可行。**所以 PHP 不能直接证明至少 20 个**。

实际正确理解：广义 PHP 给的是 ⌈n/k⌉，即 ≥ ⌈n/k⌉ 个。要得到"至少 20 个"，需要 ⌈n/k⌉ ≥ 20，即 n ≥ 20k − (k-1)。这里 n=100, k=10, 20×10 − 9 = 191 > 100，**不够**。

实际题目问的是：用 PHP 求至少多少个同 last digit，答案是 **10**（⌈100/10⌉=10）。但题目说"at least 20 of them have the same last digit"，**这题是错的或特殊版本**。让我重看：题目原版可能在 8.x section，不是 6.2。

### 题型 3：构造反证
假设结论不成立，导出矛盾。

### 题型 4：找反例
有些"看似鸽巢"的题其实不行（如"至少 20 个同 last digit"需要 191 个数）。

## 配套作业

**Section 6.2**

**1.** Assume that a year has 365 days.
a) How many people must be selected so that at least two of them were born on the same day of the week?
b) How many people must be selected so that at least two of them were born on the same day of the year?
c) How many people must be selected so that at least two of them were born in the same month?

**5.** Show that if seven integers are selected from the set {1, 2, …, 100}, there must be at least two that sum to 101.

**8.** Show that if 10 integers are selected from {1, 2, …, 100}, there must be at least two disjoint subsets of these integers with the same sum.

**11.** A bowl contains 10 red balls and 10 blue balls. A woman selects balls from the bowl without looking at them. How many balls must she select to be sure of having at least three balls of the same color?

**15.** Show that at least two of the numbers among {100, 101, …, 200} have the same last two digits.

**18.** A company stores products in a warehouse. There are 10 different products and each product has a different storage location. How many different products must be stored to guarantee that two products occupy the same storage location?

**22.** A useful form of the pigeonhole principle: If n objects are placed into k boxes, then there is a box containing at least ⌈n/k⌉ objects. Suppose that 5 friends take a trip and at each stop they get a snack at a vending machine. Find the smallest number of snacks that must be taken to ensure that at least two of the friends get the same kind of snack.

---

# C3 排列 P(n,r) + 组合 C(n,r)

## 核心概念

**P(n, r) = n! / (n-r)!**：从 n 个不同元素**有序**取 r 个。

**C(n, r) = n! / (r!(n-r)!) = C(n, n-r)**：从 n 个不同元素**无序**取 r 个。

**关键判别**：
- 有顺序 → P
- 无顺序 → C
- 题目说"选出"通常 C，"排队"通常 P

**常用 C(n,r) 值**（必背）：
- C(n,0) = C(n,n) = 1
- C(n,1) = C(n,n-1) = n
- C(n,2) = n(n-1)/2

**Pascal 恒等式**：C(n+1, k) = C(n, k-1) + C(n, k)

**Vandermonde 恒等式**：C(m+n, r) = ∑ₖ C(m,k)·C(n,r-k)

## 反复考的题型

### 题型 1：标准排列/组合
- "n 个不同人排成一排" = n!
- "n 个不同人选 r 个排成一排" = P(n, r)
- "n 个不同人选 r 个" = C(n, r)
- "n 个不同人围成圆桌" = (n-1)!（旋转等价）

### 题型 2：分组（"分成若干组"）
- 平均分组（组大小相同）：要除以 k!（k 个组排列）
- 例：10 人分 5 组每组 2 人 = C(10,2)·C(8,2)·C(6,2)·C(4,2)·C(2,2) / 5!

### 题型 3：相邻/不相邻问题
- **相邻**：捆绑法 → 把相邻元素看作一个
- **不相邻**：插空法 → 先排其他，再在空位插

### 题型 4：含重复字母的排列
n 个字母中某些重复，排列数 = n! / (重复字母阶乘之积)
例：MISSISSIPPI = 11!/(4!·4!·2!·1!)

### 题型 5：扑克牌问题
- C(52, 5)：所有 5 张牌
- 同花顺：4 × C(13,5)（4 个 suit，每个选 5 张连续）
- 含 a 个 A：先选 C(4, a) 个 A，再从其他 48 张选 5-a 张：C(4,a)·C(48, 5-a)

## 配套作业

**Section 6.3**

**1.** How many different permutations of the letters C, I, N, E, M, A, T, I, C, S are there?

**5.** How many different 8-letter permutations can be formed from the letters in the word "MATHEMATICS"? (There are 11 letters; M and A each appear twice.)

**10.** How many 3-element subsets can be formed from {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}? How many contain the element 5?

**15.** A committee of 5 people is to be chosen from a group of 6 men and 9 women. How many ways are there to choose
a) 5 men?　b) 5 women?　c) 3 men and 2 women?
d) at least one man?　e) at most one man?

**20.** In how many ways can 8 distinct toys be divided among 4 children if the youngest gets 2 toys and each of the others gets 2 toys?

**25.** In how many ways can 7 people be seated in a row if
a) Alice must sit in the middle?
b) Alice and Bob must sit at the ends?
c) Alice, Bob, and Carol must sit together?

**30.** A poker hand consists of 5 cards dealt from a standard 52-card deck. How many poker hands contain
a) exactly one ace?
b) at least one ace?
c) at least two aces?
d) the ace, king, queen, jack, and ten of the same suit (a royal flush)?

**40.** A coin is tossed 10 times. In how many ways can exactly 6 heads appear?

---

# C4 二项式定理

## 核心概念

**二项式定理**：

$$(x + y)^n = \sum_{k=0}^{n} \binom{n}{k} x^{n-k} y^k = \sum_{k=0}^{n} \binom{n}{k} x^k y^{n-k}$$

**x^k y^(n-k) 的系数**：C(n, k)

**Pascal 恒等式**（递推）：

$$\binom{n+1}{k} = \binom{n}{k-1} + \binom{n}{k}$$

**对称性**：C(n, k) = C(n, n-k)

**其他重要恒等式**：

| 恒等式 | 公式 |
|---|---|
| ∑ₖ C(n,k) | = 2ⁿ（所有子集数）|
| ∑ₖ (-1)ᵏ C(n,k) | = 0（n ≥ 1）|
| ∑ₖ k·C(n,k) | = n·2ⁿ⁻¹ |

## 反复考的题型

### 题型 1：展开式 / 求系数
(x+y)⁵ = x⁵ + 5x⁴y + 10x³y² + 10x²y³ + 5xy⁴ + y⁵

### 题型 2：含负号或分数展开
(3x−2y)⁴：把 (3x) 当作 x，(-2y) 当作 y，系数 ∑ C(4,k)(3x)^(4-k)(-2y)^k

### 题型 3：用 Pascal 恒等式算 C(n,k)
从 C(0,0)=C(1,0)=C(1,1)=1 开始一行行算。

## 配套作业

**Section 6.4**

**1.** Find the expansion of (x + y)⁵ using the binomial theorem.

**5.** What is the coefficient of x⁷y⁹ in (x + y)¹⁶?

**10.** Give a formula for the coefficient of xᵏy^(n−k) in (x + y)ⁿ for k = 0, 1, 2, …, n.

**15.** Use Pascal's identity to compute the binomial coefficients C(8, k) for k = 0, 1, …, 8.

**20.** Use the binomial theorem to expand (3x − 2y)⁴.

**25.** Use the binomial theorem to expand (x² + 1/x)⁵.

**30.** In the expansion of (x + y)¹⁰, find the coefficient of x⁸y² and x²y⁸.

**40.** Use Pascal's identity to derive the identity C(n, r) = C(n, n−r).

---

# C5 广义组合（**必考大题**）

## 核心概念

**4 种广义组合**（必背！）：

| 问题 | 公式 | 记忆 |
|---|---|---|
| n 个**不同**元素中**有序**取 r 个（允许重复）| n^r | 每个位置 n 种选择 |
| n 个**不同**元素中**无序**取 r 个（允许重复，可重组合）| C(n+r−1, r) | "n 种面包买 r 个" |
| 把 n 个**相同**（不可区分）元素放入 k 个**不同**盒子（可空）| C(n+k−1, k−1) | "n 个球 k 个盒" |
| 把 n 个**相同**元素放入 k 个不同盒子，**每盒至少 1 个** | C(n−1, k−1) | "n 个球 k 个盒，每盒 ≥1" |

> ⚠️ 注意上面两个公式容易混：
> - 可空 = C(n+k−1, k−1)
> - 每盒 ≥1 = C(n−1, k−1)
>
> 区别在于可空 vs 每盒至少 1。

**错位排列 Dₙ**（特殊问题）：
- n 个元素都不在原位的排列数
- D₁ = 0, D₂ = 1, D₃ = 2, D₄ = 9, D₅ = 44
- 公式：Dₙ = n! · ∑ₖ₌₀ⁿ (-1)ᵏ/k!
- 推导：容斥原理（Ch8）

## 反复考的题型

### 题型 1：方程非负整数解数
x₁ + x₂ + ... + xₖ = n，xᵢ ≥ 0 的解数 = C(n+k−1, k−1)

**记忆**：n 个"1"分给 k 个变量（变量可空），中间加 k-1 个"分隔符"。

### 题型 2：放球入盒（不可区分球）
- 可空：C(n+k-1, k-1)
- 每盒 ≥ 1：C(n-1, k-1)
- 不同球（可区分）：kⁿ

### 题型 3：可重组合（"n 种水果买 r 个"）
C(n+r-1, r) = C(n+r-1, n-1)

### 题型 4：含重复字母字符串
n! / (重复字母阶乘之积)

## 配套作业

**Section 6.5**

**1.** In how many different orders can 5 runners finish a race if no ties are allowed?

**5.** How many strings of 5 letters from the 26-letter alphabet
a) contain exactly one repeated letter?
b) begin with a vowel? (Y is not considered a vowel.)
c) contain at least one vowel?

**10.** How many ways are there to deal hands of 5 cards to each of six players from a standard 52-card deck?

**15.** How many solutions are there to the equation x₁ + x₂ + x₃ = 17, where x₁, x₂, x₃ are nonnegative integers?

**20.** How many solutions are there to the equation x₁ + x₂ + x₃ + x₄ + x₅ = 21, where xᵢ are nonnegative integers?

**25.** A doughnut shop offers 20 kinds of doughnuts. How many ways are there to choose
a) 6 doughnuts?
b) a dozen doughnuts?
c) two of one kind and a dozen of the others?

**30.** How many different strings can be made from the letters in the word "ABRACADABRA"?

**43.** Show that the number of ways to distribute n indistinguishable balls into k distinguishable boxes is C(n + k − 1, k − 1).

---

# C6 生成函数

## 核心概念

**生成函数**：序列 {aₙ} 的生成函数 G(x) = ∑ₙ aₙ xⁿ

**常用生成函数**：

| 序列 {aₙ} | 生成函数 G(x) |
|---|---|
| aₙ = 1 | 1/(1-x) |
| aₙ = c | c/(1-x) |
| aₙ = n | x/(1-x)² |
| aₙ = n² | x(1+x)/(1-x)³ |
| aₙ = cⁿ | 1/(1-cx) |
| aₙ = C(n+k-1, k-1) | 1/(1-x)ᵏ |

**生成函数解递推**：
1. 设 G(x) = ∑ aₙxⁿ
2. 用递推关系代入，化简
3. 部分分式展开
4. 系数即 aₙ

## 反复考的题型

### 题型 1：求生成函数
直接套上表。

### 题型 2：用生成函数解递推
例：aₖ = 3aₖ₋₁ + 2
- G(x) = a₀ + ∑ₖ≥₁ (3aₖ₋₁ + 2)xᵏ = a₀ + 3x G(x) + 2x/(1-x)
- (1-3x)G(x) = a₀ + 2x/(1-x)
- G(x) = [a₀(1-x) + 2x] / [(1-x)(1-3x)]

### 题型 3：求特定项系数
展开后取 xⁿ 系数。

## 配套作业

**Section 6.6**

**1.** Find the generating function for the sequence {aₙ}, where aₙ = 3ⁿ.

**5.** Find the generating function for the sequence {aₙ}, where aₙ = 5.

**10.** Find the generating function for the sequence {aₙ}, where aₙ = n.

**13.** Use generating functions to find the number of ways to select a dozen donuts if there are 5 varieties, with the restriction that at most 3 of one variety are taken.

**15.** Use generating functions to find the number of ways to make change for $1 using quarters, dimes, nickels, and pennies.

**17.** Use generating functions to solve the recurrence relation aₖ = 3aₖ₋₁ + 2, with a₀ = 1.

---

## 复习清单

- [ ] 乘法原理：依次完成 k 步 → 乘
- [ ] 加法原理：互斥方法 → 加
- [ ] n^m（函数个数）、P(n,m)（单射）、满射用容斥
- [ ] PHP：n+1 鸽 n 巢 → 至少 2 同巢
- [ ] 广义 PHP：⌈n/k⌉
- [ ] P(n,r) = n!/(n-r)! 有序
- [ ] C(n,r) = n!/(r!(n-r)!) 无序 = C(n, n-r)
- [ ] 平均分组要除以 k!
- [ ] 相邻→捆绑，不相邻→插空
- [ ] Pascal：C(n+1,k) = C(n,k-1) + C(n,k)
- [ ] 二项式定理 (x+y)ⁿ = ∑ C(n,k) xⁿ⁻ᵏyᵏ
- [ ] **可重组合 C(n+r-1, r)**（n 种买 r 个）
- [ ] **n 个不可区分球入 k 个可区分盒**：可空 C(n+k-1, k-1)，每盒≥1 C(n-1, k-1)
- [ ] 错位排列 Dₙ = n!∑(-1)ᵏ/k!
- [ ] 生成函数 ∑aₙxⁿ 与已知序列对应表
- [ ] 生成函数解递推的 4 步法