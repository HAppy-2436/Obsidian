# 第二章 基本结构（按知识点组织）

> **考试分值**：4 题 / 30 分（与 Ch1、Ch9 合并）
> **考纲范围**：2.1, 2.2, 2.3, 2.4, 2.5, 2.6（全考）
> **必考重点**：2.3 函数（单/满/双射）、2.5 可数性
> **总题数**：约 218 道

---

## 知识点地图

| 知识点 | 出处 | 频次 | 难度 |
|---|---|---|---|
| L1 集合与子集 | 2.1 | ★★☆ | 易 |
| L2 集合运算 + De Morgan | 2.1, 2.2 | ★★★ | 易 |
| L3 对称差 + 幂集 + Venn | 2.2 | ★★☆ | 易 |
| L4 函数基础 | 2.3 | ★★☆ | 易 |
| L5 单射/满射/双射 + 反函数 + 复合 | 2.3 | ★★★ | 中 |
| L6 序列 + 求和 + 大 O | 2.4 | ★★☆ | 中 |
| L7 可数集与不可数集 | 2.5 | ★★★ | 中 |
| L8 矩阵 + 转置 + 逆矩阵 + 布尔矩阵 | 2.6 | ★★☆ | 中 |

---

# L1 集合与子集

## 核心概念

**集合**：无序、互不相同元素的聚集。元素 a ∈ 集合 A 写作 a ∈ A。

**集合表示法**：
- 列举：{1, 2, 3}
- 构造：{x | x 是偶数}
- 常用集合：ℕ 自然数、ℤ 整数、ℚ 有理数、ℝ 实数、ℂ 复数

**子集**：A ⊆ B 当且仅当 ∀x (x ∈ A → x ∈ B)

**真子集**：A ⊊ B 当且仅当 A ⊆ B 且 A ≠ B

**空集**：∅，任何集合的子集。

**幂集**：P(A) = {S | S ⊆ A}，|P(A)| = 2^|A|

## 反复考的题型

### 题型 1：列出子集
n 元集合 → 2^n 个子集。

### 题型 2：子集关系证明
- A ⊆ B：任取 x ∈ A，证明 x ∈ B
- A = B：A ⊆ B 且 B ⊆ A

### 题型 3：集合表达式化简
用集合恒等式（见 L3）。

## 配套作业

**Section 2.1**

**1.** Can two sets be equal if they share no elements in common? Explain.

**5.** List all the subsets of {0, 1, 2}.

**10.** Let A = {1, 2, 3, 4, 5} and B = {0, 3, 6}. Find:
a) A ∪ B　b) A ∩ B　c) A − B　d) B − A　e) A ⊕ B

**37.** Show that if A ⊆ B and B ⊆ C then A ⊆ C.

---

# L2 集合运算 + De Morgan

## 核心概念

**5 种基本运算**：

| 运算 | 符号 | 定义 |
|---|---|---|
| 并（union） | A ∪ B | {x | x ∈ A ∨ x ∈ B} |
| 交（intersection） | A ∩ B | {x | x ∈ A ∧ x ∈ B} |
| 差（difference） | A − B | {x | x ∈ A ∧ x ∉ B} |
| 对称差（symmetric difference） | A ⊕ B | (A − B) ∪ (B − A) |
| 补（complement） | Ā | {x ∈ U | x ∉ A} |

**集合 De Morgan 定律**（必背，与命题版一一对应）：

$$A \cap B 的补 = \overline{A} \cup \overline{B}$$
$$A \cup B 的补 = \overline{A} \cap \overline{B}$$

> **记忆**：与命题 De Morgan 完全一样，只是把 ∧ 改成 ∩、∨ 改成 ∪。

## 反复考的题型

### 题型 1：给定有限集合求运算结果
列元素，按定义逐个判断。

### 题型 2：证明集合等式
- 任取 x 在左边，证明 x 在右边
- 再任取 x 在右边，证明 x 在左边

**模板**：

```
证：A − (B ∪ C) = (A − B) ∩ (A − C)

(⊆) 任取 x ∈ A − (B ∪ C)
    → x ∈ A 且 x ∉ B ∪ C
    → x ∈ A 且 ¬(x ∈ B ∨ x ∈ C)
    → x ∈ A 且 x ∉ B 且 x ∉ C
    → (x ∈ A 且 x ∉ B) 且 (x ∈ A 且 x ∉ C)
    → x ∈ (A − B) ∩ (A − C)

(⊇) 反向同理。
```

### 题型 3：找满足条件的集合
利用已知条件（A ∪ B, A ∩ B, B − A 等）反推 A 和 B。

## 配套作业

**Section 2.1**

**15.** Let A = {a, b, c, d, e}, B = {a, b, c}, C = {c, d, e, f}. Find:
a) A ∩ (B ∪ C)　b) (A ∩ B) ∪ C　c) (A − B) − C　d) (A − C) − (B − C)

**20.** Prove that A − (B ∪ C) = (A − B) ∩ (A − C).

**25.** Find all sets A and B that satisfy A ∪ B = {1, 2, 3, 4, 5, 6}, A ∩ B = {1, 2, 3, 4}, and B − A = {6}.

**30.** Prove or disprove that (A ∪ B) − C = (A − C) ∪ (B − C).

**Section 2.2**

**1.** Let A = {1, 2, 3, 4, 5}, B = {0, 1, 2, 3}. Find:
a) A ∪ B　b) A ∩ B　c) A − B　d) B − A　e) A ⊕ B

**5.** Use set notation to write each of the following.
a) The set of all integers that are greater than 2 and less than 7.
b) The set of all integers whose square is less than 20.
c) The set of all integers that are perfect cubes and perfect squares.

**15.** Let A = {a, b, c, d}, B = {c, d, e, f}, C = {b, d, e}. Find:
a) A ∪ (B ∩ C)　b) (A ∪ B) ∩ C　c) A ∩ (B ∪ C)　d) (A ∩ B) ∪ C　e) A ⊕ (B ∩ C)

**25.** Show that A ∪ B = A ∩ B if and only if A = B.

**37.** Let A, B, and C be sets. Show that A ∪ (B − C) = (A ∪ B) − (C − A).

---

# L3 对称差 + 幂集 + Venn

## 核心概念

**对称差性质**（必背）：
- A ⊕ B = (A ∪ B) − (A ∩ B)
- A ⊕ B = (A − B) ∪ (B − A)
- 交换律：A ⊕ B = B ⊕ A
- 结合律：A ⊕ (B ⊕ C) = (A ⊕ B) ⊕ C
- A ⊕ ∅ = A
- A ⊕ A = ∅

**幂集**：P(A) = 所有子集的集合。
- |P(A)| = 2^|A|
- P(∅) = {∅}（∅ 的子集只有 ∅ 自己）

**Venn 图**：用重叠圆表示集合，阴影部分表示运算结果。

## 反复考的题型

### 题型 1：求幂集
列所有子集（包括 ∅ 和 A 自身）。

### 题型 2：证明对称差性质
用集合等式证明（双包含）。

### 题型 3：Venn 图绘制
- A ∪ (B ∩ C)：A 的全部，加上 B、C 重叠部分（在 A 外的部分）
- A ∩ (B ∪ C)：B ∪ C 的全部，与 A 重叠的部分

## 配套作业

**Section 2.2**

**10.** Find the power set of {∅, {∅}, {∅, {∅}}}.

**20.** Draw the Venn diagrams for each of these combinations of the sets A, B, and C.
a) A ∩ (B ∪ C)　b) A ∪ (B ∩ C)　c) (A ∪ B) ∩ C　d) (A ∩ B) ∪ C

**30.** Prove that the symmetric difference is associative: A ⊕ (B ⊕ C) = (A ⊕ B) ⊕ C.

---

# L4 函数基础

## 核心概念

**函数 f: A → B** 是从 A 到 B 的二元关系，每个 a ∈ A 有**唯一一个** b ∈ B 对应。

- **domain（定义域）**：A
- **codomain（值域）**：B
- **image（像）**：f(A) = {f(a) | a ∈ A} ⊆ B
- **preimage（原像）**：f⁻¹(b) = {a ∈ A | f(a) = b}

**多对一**：不同 a 可能映到同一个 b。一对多**不是函数**。

## 反复考的题型

### 题型 1：判断是否构成函数
检查每个输入是否有唯一输出。
- f(x) = 1/x：当 x=0 时无定义，**不是** ℝ → ℝ 的函数
- f(x) = ±√(x²+1)：每个 x 对应两个值，**不是**函数

### 题型 2：求像与原像
像 = 所有输出值的集合；原像 = 使 f(x)=b 的所有 x。

## 配套作业

**Section 2.3**

**1.** Why is f not a function from ℝ to ℝ if
a) f(x) = 1/x?
b) f(x) = √x?
c) f(x) = ±√(x²+1)?

**5.** Determine whether f is a function from ℤ to ℤ where f(n) = ⌊n/2⌋.

---

# L5 单射/满射/双射 + 反函数 + 复合（**核心**）

## 核心概念

| 性质 | 定义 | 等价说法 |
|---|---|---|
| **单射（injective / one-to-one）** | a₁ ≠ a₂ ⇒ f(a₁) ≠ f(a₂) | f(a₁)=f(a₂) ⇒ a₁=a₂ |
| **满射（surjective / onto）** | ∀b ∈ B, ∃a ∈ A, f(a)=b | 像 = codomain |
| **双射（bijective）** | 既单射又满射 | 一一对应 |

**复合函数**：f ∘ g (x) = f(g(x))。注意 (f ∘ g)(x) ≠ (g ∘ f)(x)，一般**不交换**。

**反函数**：f 存在反函数 f⁻¹ **当且仅当 f 是双射**。
- 反函数满足：f(f⁻¹(y)) = y，f⁻¹(f(x)) = x

**求反函数步骤**：
1. 写 y = f(x)
2. 解出 x = ?(y)
3. 互换 x 和 y

## 反复考的题型

### 题型 1：判断单射
方法：
- 看 f(a₁)=f(a₂) 时 a₁=a₂ 是否成立
- 严格单调函数必单射
- 例：f(x)=x² 在 ℝ 上**不**单射（f(1)=f(-1)），但在 [0,∞) 上单射

### 题型 2：判断满射
检查 B 中每个元素是否有原像。

### 题型 3：求反函数
按步骤解。

### 题型 4：复合函数计算
(f ∘ g)(x) = f(g(x))：先算 g(x)，再代入 f。

### 题型 5：双射 ↔ 反函数存在
存在反函数 ⟺ 双射。

## 配套作业

**Section 2.3**

**10.** Determine whether f is one-to-one for each of the following.
a) f(x) = x + 1
b) f(x) = 2x³ + 1
c) f(x) = |x|
d) f(x) = x² + 1
e) f(x) = −x²
f) f(x) = x / (x² + 1)

**15.** Find f ∘ g and g ∘ f, where f(x) = x² + 1 and g(x) = x + 2, are functions from ℝ to ℝ.

**20.** Suppose g is a function from A to B and f is a function from B to C where A = {a, b, c}, B = {1, 2}, C = {x, y, z}. If g(a) = 2, g(b) = 1, g(c) = 2, and f(1) = x, f(2) = y, find (a) f ∘ g and (b) g⁻¹ if it exists.

**25.** Let f be a function from {a, b, c, d} to {1, 2, 3} with f(a) = 2, f(b) = 1, f(c) = 3, f(d) = 1. Is f one-to-one? Is f onto?

**30.** Find the inverse function of f(x) = 2x³ + 1.

**37.** Show that the function f(x) = ax + b from ℝ to ℝ is one-to-one if and only if a ≠ 0. Show that f has an inverse if a ≠ 0.

---

# L6 序列 + 求和 + 大 O

## 核心概念

**序列**：aₙ 是从正整数（或非负整数）到某集合的函数。

**常用求和公式**（必背）：

$$\sum_{k=1}^{n} k = \frac{n(n+1)}{2}$$

$$\sum_{k=1}^{n} k^2 = \frac{n(n+1)(2n+1)}{6}$$

$$\sum_{k=1}^{n} k^3 = \left[\frac{n(n+1)}{2}\right]^2$$

$$\sum_{k=0}^{n-1} 2^k = 2^n - 1 \quad (几何级数)$$

$$\sum_{k=0}^{\infty} x^k = \frac{1}{1-x} \quad (|x|<1)$$

**大 O 符号**：f(x) = O(g(x)) 表示存在常数 C, k 使 |f(x)| ≤ C·|g(x)| 对所有 x > k 成立。

**常见大小关系**（重要）：
$$\log\log n < \log n < \sqrt{n} < n < n\log n < n^2 < 2^n < n!$$

## 反复考的题型

### 题型 1：求序列指定项
直接代入 n。

### 题型 2：求和
套公式，或展开。

### 题型 3：判断大 O 关系
看 f 和 g 的增长率。

## 配套作业

**Section 2.4**

**1.** Find the first four terms and the 100th term of the sequence defined by:
a) aₙ = 2n + 1
b) aₙ = (−2)ⁿ
c) aₙ = 3ⁿ + 3^(−n)
d) aₙ = 2 + (−1)ⁿ

**5.** Find the first four terms and the 50th term of the sequence whose nth term is given.
a) aₙ = n²/(n+1)
b) aₙ = (−1)ⁿ⁺¹/n
c) aₙ = 10ⁿ/3ⁿ
d) aₙ = 2ⁿ⁺¹/2ⁿ⁻¹

**15.** What are the terms a₀, a₁, a₂, a₃ of the sequence {aₙ} where aₙ satisfies the recurrence aₙ = 2aₙ₋₁ + aₙ₋₂ − 2aₙ₋₃, with a₀ = 3, a₁ = −1, a₂ = 4?

**20.** Use a summation formula to evaluate each of the following sums.
a) ∑_{k=1}^{10} k
b) ∑_{k=1}^{10} k²
c) ∑_{k=1}^{10} k³
d) ∑_{k=1}^{10} (−2)ᵏ

**25.** Compute each of these double sums.
a) ∑_{i=1}^{2} ∑_{j=1}^{3} (i + j)
b) ∑_{i=0}^{3} ∑_{j=0}^{2} (2i + j)
c) ∑_{i=1}^{3} ∑_{j=0}^{2} (3i − 2j)

**35.** Find ∑_{k=100}^{200} k.

**48.** Find ∑_{j=0}^{n} (2j + 1)/(n+1)².

---

# L7 可数集与不可数集（**必考**）

## 核心概念

**三类集合**：
- **有限集**：元素个数有限
- **可数无限（countably infinite）**：与正整数集 ℕ 等势（双射）
- **不可数（uncountable）**：与 ℝ 等势，不是可数无限

**可数无限集的判定**：
- 能与 ℕ 建立双射
- 元素可"枚举"（列出第 1 个、第 2 个...）
- 例子：ℕ、ℤ、ℚ、所有整数序列、所有 0/1 有限序列、所有有限子集

**不可数集**：
- 实数集 ℝ
- (0, 1) 区间
- 任何区间
- 所有无穷 0/1 序列

**Cantor 对角线法**：证明 (0,1) 实数不可数。
- 假设可数，列出所有实数
- 构造一个新实数，与每个对角线位置不同
- 与列表每项至少一位不同 → 不在列表中 → 矛盾

**Schröder–Bernstein 定理**：若 |A| ≤ |B| 且 |B| ≤ |A|，则 |A| = |B|（存在双射）。

## 反复考的题型

### 题型 1：判断可数性

| 集合类型 | 可数性 |
|---|---|
| 整数 < N | 有限 |
| 偶数 / 奇数 / 整数倍 | 可数无限 |
| 整数对 (m, n) | 可数无限（用对角枚举）|
| 有理数 ℚ | 可数无限 |
| 实数 ℝ、(a,b) 区间 | **不可数** |
| 所有整数序列 | 可数无限 |
| 所有 0/1 有限序列 | 可数无限 |
| 所有 0/1 无穷序列 | **不可数** |
| 整数集 P(ℕ) | **不可数** |

### 题型 2：构造双射
- 奇数 ↔ 整数：f(n) = (n-1)/2（奇数 → 整数）；g(m) = 2m+1（整数 → 奇数）
- 正整数 ↔ 整数：f(n) = (n-1)/2（n 奇）；f(n) = -n/2（n 偶）

### 题型 3：证明不可数
用 Cantor 对角线法（必考大题）。

**模板**：

```
设 S = {无穷 0/1 序列} 可数。
则可枚举为 s₁, s₂, s₃, ...，每个 sᵢ = bᵢ₁bᵢ₂bᵢ₃...
构造序列 t：t 的第 i 位 = 1 − bᵢᵢ（与 sᵢ 第 i 位相反）
则 t 与每个 sᵢ 至少一位不同 → t ∉ 列表 → 矛盾。
∴ S 不可数。
```

## 配套作业

**Section 2.5**

**1.** Determine whether each of these sets is finite, countably infinite, or uncountable.
a) the integers less than 10
b) the odd negative integers
c) the real numbers between 0 and 2
d) the integers with absolute value less than 100,000
e) the real numbers with decimal representations consisting of all 1's

**5.** Show that if A and B are countably infinite sets, then A ∪ B is countably infinite.

**10.** Determine whether the set {a, b, c, d, …, z} is countably infinite or uncountable.

**15.** Use the Schröder–Bernstein theorem to prove that if |A| = |B| and |B| ≤ |C| then |A| ≤ |C|.

**20.** Show that the set of all finite sequences of integers is countably infinite.

**23.** Show that the set of all finite sequences of 0's and 1's is countably infinite.

**27.** Show that the set of all finite subsets of ℕ is countably infinite.

---

# L8 矩阵 + 转置 + 逆矩阵 + 布尔矩阵

## 核心概念

**矩阵乘法**：A(m×n) × B(n×p) = C(m×p)。**C[i][j] = ∑ₖ A[i][k]·B[k][j]**

注意：
- AB 有意义**不一定** BA 有意义（维度问题）
- 即使维度匹配，**AB ≠ BA**（一般不交换）

**转置**：Aᵀ 的 (i, j) 元素 = A 的 (j, i) 元素。

**逆矩阵**：A⁻¹ 存在当且仅当 det(A) ≠ 0（2×2 情况）。
- 2×2 公式：A⁻¹ = (1/det(A)) · [[d, -b], [-c, a]]（当 A = [[a,b],[c,d]]）

**布尔矩阵**：元素为 0/1，加法用 ∨、乘法用 ∧。
- 用于表示关系（见 Ch9）
- join（R₁ ∨ R₂）= 元素级 OR
- meet（R₁ ∧ R₂）= 元素级 AND
- 复合 R₁R₂ = 布尔矩阵乘法

## 反复考的题型

### 题型 1：矩阵乘法
按定义一行行算。

### 题型 2：判断哪些积可定义
m×n 矩阵只能与 n×p 矩阵相乘，结果是 m×p。

### 题型 3：转置
行列互换。

### 题型 4：求 2×2 逆矩阵
套公式。

### 题型 5：布尔矩阵运算
0/1 当真假，∨=OR, ∧=AND。

## 配套作业

**Section 2.6**

**1.** Let A = [[1, 1], [0, 1]] and B = [[−1, 0], [1, 1]]. Find:
a) A + B　b) AB　c) BA　d) A² + B²

**5.** Let A = [[2, 1, −1], [0, 1, 3]] and B = [[1, 2], [3, 1], [−1, 4]]. Find:
a) AB　b) BA　(if defined)

**10.** Let A be a 3×4 matrix, B be a 4×5 matrix, and C be a 4×4 matrix. Determine which of the following products are defined and find the size of those that are: A², AB, BA, ACB, CA, BC, CB, BCC, A³.

**15.** Find the transpose of each matrix in Exercise 1.

**20.** Let A = [[1, 2], [3, 4]]. Show that A is invertible and find A⁻¹.

**25.** Let A = [[1, 0], [2, 3]]. Find A⁻¹.

**28.** Use Boolean matrices to find the join and meet of the relations R₁ = {(1,1), (1,2), (2,1), (3,2)} and R₂ = {(1,1), (1,2), (2,2), (3,1), (3,2)}.

**30.** Use Boolean matrices to find the join and meet of the relations R₁ = {(1,1), (1,2), (2,3), (3,3)} and R₂ = {(1,1), (2,2), (3,1), (3,3)}.

---

## 复习清单

- [ ] 集合 De Morgan 双公式
- [ ] 对称差性质（交换、结合、A⊕A=∅）
- [ ] |P(A)| = 2^|A|
- [ ] 单射/满射/双射判定技巧
- [ ] 求反函数：解 y=f(x) → 互换
- [ ] 复合函数：(f∘g)(x) = f(g(x))，一般不交换
- [ ] 求和公式 4 个（k, k², k³, 几何）
- [ ] 大 O：log n < √n < n < n log n < n² < 2ⁿ
- [ ] 可数无限 vs 不可数（哪些可数哪些不可数）
- [ ] Cantor 对角线法证明不可数
- [ ] 矩阵乘法维度匹配
- [ ] 2×2 逆矩阵公式