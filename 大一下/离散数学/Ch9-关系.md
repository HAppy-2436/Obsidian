# 第九章 关系（按知识点组织）

> **考试分值**：4 题 / 30 分（与 Ch1、Ch2 合并）
> **考纲范围**：9.1, 9.3, 9.4, 9.5, 9.6（**不考** 9.2 n-元关系）
> **必考三大块**：**9.4 Warshall** + **9.5 等价类 ↔ 划分** + **9.6 Hasse 图**
> **总题数**：约 162 道

---

## 知识点地图

| 知识点 | 出处 | 频次 | 难度 |
|---|---|---|---|
| R1 关系基础 + 表示 | 9.1, 9.3 | ★★☆ | 易 |
| R2 关系性质（4 性）| 9.1 | ★★★ | 中 |
| R3 关系闭包 + Warshall | 9.4 | ★★★ | 难 |
| R4 等价关系 + 等价类 + 划分 | 9.5 | ★★★ | 中 |
| R5 偏序 + Hasse 图 | 9.6 | ★★★ | 中 |
| R6 拓扑排序 + Dilworth | 9.6 | ★★☆ | 中 |

---

# R1 关系基础 + 表示

## 核心概念

**关系**：从 A 到 B 的二元关系 R ⊆ A × B。
- A 到 A 的关系称为 A 上的关系。

**表示法**：
1. **集合表示**：列出有序对 {(a₁,b₁), (a₂,b₂), ...}
2. **关系矩阵**：A × B，元素 (i,j) = 1 iff (aᵢ,bⱼ) ∈ R
3. **关系图**：顶点 = 元素，边 = 关系
4. **逆关系**：R⁻¹ = {(b,a) | (a,b) ∈ R}

**关系上的运算**（设 S, T 是 A 上的关系）：

| 运算 | 定义 |
|---|---|
| 并 S ∪ T | (a,b) ∈ S 或 T |
| 交 S ∩ T | 都在 |
| 复合 S ∘ T | ∃c 使 (a,c) ∈ T 且 (c,b) ∈ S |
| 幂 Rⁿ | R 自复合 n 次 |

**复合的矩阵表示**：M_S∘T = M_S ⊙ M_T（布尔矩阵乘法）

## 反复考的题型

### 题型 1：列有序对
看清定义"a R b 当且仅当 ..."

### 题型 2：画关系矩阵
按关系是否存在填 0/1。

### 题型 3：求复合关系
(a,b) ∈ R₁ ∘ R₂ 当且仅当 ∃c 使 (a,c) ∈ R₁ 且 (c,b) ∈ R₂。

## 配套作业

**Section 9.1**

**1.** List the ordered pairs in the relation R from A = {0, 1, 2, 3, 4} to B = {0, 1, 2, 3} where (a, b) ∈ R if a > b.

**Section 9.3**

**1.** Represent each of these relations on {1, 2, 3} with a matrix (with the elements of this set listed in increasing order).
a) {(1,1), (1,2), (1,3)}
b) {(1,2), (2,1), (2,2), (2,3), (3,1), (3,3)}
c) {(1,1), (1,2), (2,1), (3,2)}
d) {(1,1), (1,2), (2,2), (3,3), (3,1), (3,2)}

---

# R2 关系性质（核心）

## 核心概念

设 R 是集合 A 上的关系。

| 性质 | 定义 | 矩阵判别 | 图判别 |
|---|---|---|---|
| **自反（reflexive）** | ∀a ∈ A, (a,a) ∈ R | 主对角线全 1 | 每点有自环 |
| **非自反** | ∀a, (a,a) ∉ R | 主对角线全 0 | 无自环 |
| **对称（symmetric）** | (a,b) ∈ R → (b,a) ∈ R | 矩阵对称 | 边无方向 |
| **反对称（antisymmetric）** | (a,b)∈R ∧ (b,a)∈R → a=b | aᵢⱼ = 1 且 i≠j → aⱼᵢ = 0 | 无双向不同边 |
| **非对称（asymmetric）** | (a,b) ∈ R → (b,a) ∉ R（除非 a=b）| — | 仅单向 |
| **传递（transitive）** | (a,b)∈R ∧ (b,c)∈R → (a,c)∈R | M² ≤ M（按位）| 若 a→b→c 存在则 a→c 必存在 |

## 反复考的题型

### 题型 1：判断 4 性质
看有序对，逐条检查 4 个性质。

### 题型 2：证明关系性质
- 自反：∀a, (a,a) ∈ R
- 对称：(a,b) ∈ R ⇒ (b,a) ∈ R
- 反对称：(a,b) ∈ R ∧ (b,a) ∈ R ⇒ a = b
- 传递：(a,b), (b,c) ∈ R ⇒ (a,c) ∈ R

### 题型 3：关系计数
- A 上关系总数：2^(n²)
- 自反关系数：2^(n²−n)
- 对称关系数：2^(n(n+1)/2)
- 反对称关系数：2ⁿ · 3^(n(n−1)/2)（对角线 n 个，每个 0/1；非对角 (n(n-1)/2) 个对，每个 3 种：00/01/10）

## 配套作业

**Section 9.1**

**5.** For each of these relations on the set {1, 2, 3, 4}, decide whether it is reflexive, symmetric, antisymmetric, transitive, or none of these.
a) {(2,2), (2,3), (2,4), (3,2), (3,3), (3,4)}
b) {(1,1), (1,2), (2,1), (2,2), (3,3), (4,4)}
c) {(2,4), (4,2)}
d) {(1,2), (1,4), (2,3), (3,4)}
e) {(1,1), (2,2), (3,3)}
f) {(1,3), (3,1)}

**10.** Let R be the relation on the set of people consisting of pairs (a, b) where a and b are siblings. Is R reflexive, symmetric, antisymmetric, transitive?

**15.** Let A = {a, b, c}. How many relations on A are there? How many are reflexive? Symmetric? Antisymmetric?

**25.** Determine whether the relation R on the set of all integers is reflexive, symmetric, antisymmetric, and/or transitive, where (x, y) ∈ R if and only if x ≡ y (mod 7).

**30.** How many symmetric relations are there on a set with n elements?

---

# R3 关系闭包 + Warshall 算法（**必考**）

## 核心概念

**闭包**：包含 R 且满足某性质的最小关系。

| 闭包 | 定义 |
|---|---|
| **自反闭包 R∪△** | R ∪ {(a,a) | a ∈ A}（△ 是恒等关系）|
| **对称闭包 R∪R⁻¹** | R ∪ R⁻¹ |
| **传递闭包 R\*** | R ∪ R² ∪ R³ ∪ ... |

**传递闭包 = 关系图中的"可达性"**：(a,b) ∈ R\* 当且仅当能从 a 走到 b（含 0 步）。

### Warshall 算法（求传递闭包）

**输入**：关系 R 的 0/1 矩阵 Mᵣ
**输出**：传递闭包的矩阵 W

**算法**（按列 k = 1 到 n 处理）：

```
W[0] = Mᵣ
for k = 1 to n:
    for i = 1 to n:
        for j = 1 to n:
            W[k][i][j] = W[k-1][i][j] OR (W[k-1][i][k] AND W[k-1][k][j])
W = W[n]
```

**直观理解**：W[i][j] = 1 当 i → k 走得到 **且** k → j 走得到。

**简化记法**（不用三维数组）：每列用中间点 k 更新 i 行 j 列。

## 反复考的题型

### 题型 1：求自反闭包
直接加 (a,a) 对。

### 题型 2：求对称闭包
加 (a,b) 的逆 (b,a)。

### 题型 3：求传递闭包（手算）
迭代 R² = R ∘ R，检查是否新增；不停直到稳定。

### 题型 4：Warshall 算法（**必考大题**）

**模板**：

```
原矩阵（顶点 1-4）：
      1  2  3  4
  1 [ 0  1  0  0 ]
  2 [ 0  0  1  0 ]
  3 [ 0  0  0  1 ]
  4 [ 1  0  0  0 ]

k=1：用顶点 1 作中间
  - 哪些 i→1→j 可达？
  1 行：1→1 没有（保留）；1→2 保留
  2→1? 否
  4→1 是 1，4→j 看哪些 j 让 1→j 走得到：1→2，所以 4→2 = 1
  更新矩阵...

k=2：用顶点 2 作中间
  ...

k=3：用顶点 3
k=4：用顶点 4

最终矩阵：每个 [i][j] 表示 i 到 j 是否可达
```

## 配套作业

**Section 9.4**

Warshall 算法配套作业（请参考教材 PDF p637–645 对应题目，常见形式为给定矩阵逐步计算）：
- 求给定矩阵的传递闭包（Warshall 算法）
- 求给定矩阵的自反闭包、对称闭包
- 判断给定关系是否已是某闭包

> ⚠️ 注：本题大量依赖图示或具体矩阵，建议直接从教材 PDF 中刷该 section 的前 10 题练习。

---

# R4 等价关系 + 等价类 + 划分（**必考**）

## 核心概念

**等价关系**：自反 + 对称 + 传递。
- 例：模 n 同余 x ≡ y (mod n)；同姓；同血型

**等价类**：[a]_R = {x | (a,x) ∈ R}（所有与 a 等价的元素）

**重要性质**：
1. 等价类是 A 的子集
2. a ∈ [a]_R
3. [a]_R = [b]_R 当且仅当 (a,b) ∈ R
4. [a]_R ≠ [b]_R 当且仅当 [a]_R ∩ [b]_R = ∅
5. **等价类的并 = A**（覆盖）

**划分（partition）**：A 的一族子集 {A₁, A₂, ...} 满足：
- 互不相交：Aᵢ ∩ Aⱼ = ∅（i ≠ j）
- 覆盖：A = A₁ ∪ A₂ ∪ ...

**核心定理（必背）**：

> 集合 A 上的每个等价关系 R 唯一对应 A 的一个划分（= 等价类集合）。
> 反之，A 的每个划分唯一确定 A 上的一个等价关系。

## 反复考的题型

### 题型 1：证明等价关系
证自反 + 对称 + 传递。

### 题型 2：求等价类

```
R = "模 3 同余"，A = {0,1,2,3,4,5}
[0] = {0, 3}
[1] = {1, 4}
[2] = {2, 5}
```

### 题型 3：划分 ↔ 等价类互转

给定划分 {{1,4,5}, {2,6}, {3}} → 等价类就是这些块
给定等价类 [a]={a,...} → 划分就是这些类

### 题型 4：判断是否为划分
- 互不相交？✓
- 覆盖全集？✓
- 都是非空？✓

## 配套作业

**Section 9.5**

**5.** List the ordered pairs in the equivalence relation on {1, 2, 3, 4, 5, 6} produced by the partition {{1, 4, 5}, {2, 6}, {3}}.

**10.** Let R be the relation on the set of integers where x R y if and only if x + y is even. Show that R is an equivalence relation.

**15.** Which of the following collections of subsets are partitions of {1, 2, 3, 4, 5, 6}?
a) {{1, 2}, {3, 4}, {5, 6}}
b) {{1}, {2, 3, 4}, {5, 6}}
c) {{1, 5}, {2}, {3, 4}, {6}}

**18.** Suppose that R is an equivalence relation on a finite set A. Show that the equivalence classes of R form a partition of A.

**20.** Let R be the relation on the set of all bit strings such that s R t if and only if s and t contain the same number of 1's. Show that R is an equivalence relation.

**22.** Find the equivalence class of 3 modulo 7 (i.e., [3]₇) and [5]₇.

---

# R5 偏序 + Hasse 图（**必考**）

## 核心概念

**偏序（partial order）**：自反 + 反对称 + 传递。
- 例子：集合上的 ⊆；正整数上的整除 |；数上的 ≤

**偏序集（poset）**：(S, ≼) 是偏序 + 集合 S。

### Hasse 图（核心必考）

**画法**（**严格按步骤**）：
1. 列出所有有序对
2. 去掉自环（(a,a)）
3. 去掉传递边：若 a ≼ c 且存在 b 使 a ≼ b ≼ c，去掉 (a,c)
4. **去掉反向边**：每对只保留"小→大"一个方向
5. 画法：小的在下面，大的在上面

> ⚠️ **关键**：Hasse 图只看**直接覆盖关系**（不存在中间元素的覆盖关系）。

### 极值元素

| 元素 | 定义 |
|---|---|
| **最大元（maximum）** | ∀s, s ≤ a（一个或没有） |
| **最小元（minimum）** | ∀s, a ≤ s（一个或没有） |
| **极大元（maximal）** | ¬∃s: a ≤ s ∧ a ≠ s（可能有多个）|
| **极小元（minimal）** | ¬∃s: s ≤ a ∧ s ≠ a |
| **上界（upper bound）** | a ≤ u 且 b ≤ u 的 u |
| **下界（lower bound）** | l ≤ a 且 l ≤ b 的 l |
| **最小上界 LUB / join** | 所有上界中最小的 |
| **最大下界 GLB / meet** | 所有下界中最大的 |

> **最大元 vs 极大元**：
> - 最大元：什么都比它小（唯一）
> - 极大元：没有比它大的（可多个，不一定唯一）
> - 例：{1,2,3} 中 3 是最大元也是极大元；但 {1,2} 偏序集 {1,2} 全序，1 是最小也是极小，2 是最大也是极大

**格（lattice）**：每个二元子集都有 LUB 和 GLB 的偏序集。

## 反复考的题型

### 题型 1：画 Hasse 图

```
({1,2,3,4,6,12}, |)
关系：1|2,1|3,1|4,1|6,1|12, 2|4,2|6,2|12, 3|6,3|12, 4|12, 6|12

Hasse 图（直接覆盖）：
    12
   / \
  6   4
 / \   \
3   2   (没有)
 \ /  
  1
```

### 题型 2：找极大/极小/最大/最小

```
读 Hasse 图：
- 顶部（无上边）：极大元（可能有多个）
- 底部（无下边）：极小元
- 唯一顶部：最大元
- 唯一底部：最小元
```

### 题型 3：找 LUB / GLB

```
两个元素的最小上界 = 它们的"公共祖先中最低的"
两个元素的最大下界 = 它们的"公共后代中最高的"
```

### 题型 4：判断偏序

3 性质：自反 + 反对称 + 传递

### 题型 5：判断格

每个二元子集都有 LUB 和 GLB。

## 配套作业

**Section 9.6**

**5.** Draw the Hasse diagram for the partial order {(a, b) | a divides b} on {1, 2, 3, 4, 6, 8, 12, 24}.

**10.** For the poset ({1, 3, 5, 9, 15, 45}, |), find the maximum, minimum, greatest lower bound, and least upper bound if they exist.

**15.** Use the Hasse diagram of the divisibility relation on {1, 2, 3, 4, 6, 8, 12, 24} to find all maximal and minimal elements.

**18.** Show that the relation "x ≤ y if and only if x divides y" on the set of positive integers is a partial order.

**20.** Determine whether each of these posets is a lattice.
a) ({1, 2, 3, 4, 6, 12}, |)
b) ({1, 2, 4, 8, 16}, |)

**25.** Let (S, ≤) be a poset. Show that (S, ≥) is also a poset, where x ≥ y iff y ≤ x.

**30.** Find all antichains in the poset ({2, 3, 4, 6, 8, 12, 24}, |).

**38.** Show that every finite poset has at least one minimal element.

---

# R6 拓扑排序 + Dilworth 定理

## 核心概念

**拓扑排序**：DAG（有向无环图）上把所有顶点排成线性序列，使每条边 (a,b) 中 a 在 b 之前。

**算法**：
1. 找入度为 0 的顶点 v
2. 输出 v，删 v 的所有出边
3. 重复直到所有顶点输出

**反链（antichain）**：偏序集中两两不可比的元素集合。

**Dilworth 定理（重要）**：

> 有限偏序集的最大反链大小 = 覆盖该偏序集的最小链数

## 反复考的题型

### 题型 1：拓扑排序
持续找入度 0 顶点。

### 题型 2：找最大反链
选两两不可比的最大子集。

### 题型 3：Dilworth 定理应用
互相对应关系。

## 配套作业

**Section 9.6（续）**

**1.** Scheduling tasks: Given tasks with precedence constraints, find a topological sort.

**5.** Find a linear extension (topological sort) of the poset ({1, 2, 3, 4, 5, 6}, |) where 1|2, 1|3, 2|4, 2|5, 3|6.

**15.** Dilworth's theorem: Show that the minimum number of chains needed to cover a finite poset equals the size of a maximum antichain.

**20.** Use Dilworth's theorem to find the minimum number of chains needed to cover the poset ({1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, |).

---

## 复习清单

- [ ] 4 性质判定：自反、对称、传递、反对称
- [ ] 关系矩阵判别 4 性质
- [ ] 关系计数：总 2^(n²)，对称 2^(n(n+1)/2)，反对称 2ⁿ·3^(n(n-1)/2)
- [ ] **Warshall 算法**：k=1..n 逐步更新（必考）
- [ ] 等价关系：自反+对称+传递
- [ ] 等价类 ↔ 划分 一一对应
- [ ] 偏序：自反+**反对称**+传递（不是对称）
- [ ] Hasse 图：去自环 + 去传递边 + 去反向边
- [ ] 极大 vs 最大：可多个 vs 唯一
- [ ] LUB/GLB 在 Hasse 图上的判读
- [ ] 拓扑排序：找入度 0 → 输出 → 删边
- [ ] Dilworth：最大反链 = 最小链覆盖