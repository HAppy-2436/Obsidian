# 第九章 关系

> **考试分值**：4 题 / 30 分（与 Ch1、Ch2 共出 4 题，本章约 1-2 题）
> **考纲 section**：9.1, 9.3, 9.4, 9.5, 9.6（**不考** 9.2）
> **作业覆盖**：9.1, 9.3, 9.4, 9.5, 9.6，共 67 道必做题（题数最多）

## 反复出现的考点

| 排名 | 考点 | 频次 |
|---|---|---|
| ★★★ | **9.4 关系的闭包 + Warshall 算法** | 10+ |
| ★★★ | **9.5 证明等价关系 + 求等价类** | 12 |
| ★★★ | **9.6 Hasse 图 + 极大/极小/最大/最小** | 17 |
| ★★★ | **9.1 自反/对称/反对称/传递判定** | 15+ |
| ★★☆ | **9.3 关系矩阵 + 关系图** | 11 |

> [!warning] **9.5 等价类** 和 **9.6 偏序 + Hasse 图** 是 Ch9 必考核心

---

## 9.1 关系与其性质（**基础**）

### 4 大性质（必背）

| 性质 | 定义 | 判定方法 |
|---|---|---|
| **自反** (reflexive) | ∀a∈A, (a,a) ∈ R | 矩阵对角线全是 1 |
| **对称** (symmetric) | (a,b)∈R → (b,a)∈R | 矩阵关于对角线对称 |
| **反对称** (antisymmetric) | (a,b)∈R ∧ (b,a)∈R → a=b | 对称位置不能同时为 1（除非 a=b） |
| **传递** (transitive) | (a,b)∈R ∧ (b,c)∈R → (a,c)∈R | 复合 R² ⊆ R |

> [!warning] 对称 vs 反对称：一个关系可以既对称又反对称（如恒等关系）

### 反复考的题型

1. **判断 4 大性质**（作业 6, 10, 14, 26）：数对角线、矩阵对称、复合
2. **复合关系 R∘S**（作业 30, 32, 34）：R∘S = { (a,c) : ∃b: (a,b)∈S ∧ (b,c)∈R }
3. **用关系图判断**（作业 42, 44, 46）

### 配套作业

**必做题（16 题）：**

**2(a)** （小问：a）

```
2. h) x ≥ y2.
```

**6** 

```
6. Determine whether the relation R on the set of all real
numbers is reﬂexive, symmetric, antisymmetric, and/or
transitive, where (x, y)∈R if and only if
a) x+ y = 0. b) x =± y.
c) x−y is a rational number.
d) x = 2y. e) xy ≥ 0.
f) xy = 0. g) x = 1.
h) x = 1o ry = 1.
```

**10** 

```
10. Give an example of a relation on a set that is
a) both symmetric and antisymmetric.
b) neither symmetric nor antisymmetric.
A relation R on the set A is irreﬂexive if for every
a ∈A, (a, a)∉R.T h a ti s ,R is irreﬂexive if no element
in A is related to itself.
```

**14** 

```
14. Which relations in Exercise 6 are irreﬂexive?
```

**26** 

```
26. Let R be the relation R ={ (a, b)∣a < b} on the set of
integers. Find
a) R−1. b) R.
```

**30** 

```
30. Let R1 ={ (1, 2), (2, 3), (3, 4)} and R2 ={ (1, 1), (1, 2),
(2, 1), (2,2), (2,3), (3,1), (3,2), (3,3), (3,4)} be relations
from{1, 2, 3} to{1, 2, 3, 4}.F i n d
a) R1 ∪R2. b) R1 ∩R2.
c) R1 −R2. d) R2 −R1.
```

**32** 

```
32. Let R be the relation {(1, 2), (1, 3), (2, 3), (2, 4), (3, 1)},
and let S be the relation{(2, 1), (3, 1), (3, 2), (4, 2)}.F i n d
S ◦R.
```

**34** 

```
34. Find
a) R1 ∪R3. b) R1 ∪R5.
c) R2 ∩R4. d) R3 ∩R5.
e) R1 −R2. f) R2 −R1.
g) R1 ⊕R3. h) R2 ⊕R4.
```

**42** 

```
42. Let R1 and R2 be the “divides” and “is a multiple of”
relations on the set of all positive integers, respectively.
That is, R1 ={ (a, b)∣a divides b} and R2 ={ (a, b)∣a
is a multiple of b}.F i n d
a) R1 ∪R2. b) R1 ∩R2.
c) R1 −R2. d) R2 −R1.
e) R1 ⊕R2.
```

**44** 

```
44. List the 16 diﬀerent relations on the set {0, 1}.
```

**46** 

```
46. Which of the 16 relations on {0, 1}, which you listed in
Exercise 44, are
a) reﬂexive? b) irreﬂexive?
c) symmetric? d) antisymmetric?
e) asymmetric? f) transitive?
```

**52** 

```
52. Suppose that R and S are reﬂexive relations on a set A.
Prove or disprove each of these statements.
a) R∪S is reﬂexive.
b) R∩S is reﬂexive.
c) R⊕S is irreﬂexive.
d) R−S is irreﬂexive.
e) S ◦R is reﬂexive.
```

**54** 

```
54. Show that the relation R on a set A is antisymmetric if
and only if R ∩R−1 is a subset of the diagonal relation
Δ={ (a, a)∣a ∈A}.
```

**56** 

```
56. Show that the relationR on a set A is reﬂexive if and only
if the complementary relation R is irreﬂexive.
```

**58** 

```
58. Let R be the relation on the set {1, 2, 3, 4, 5} containing
the ordered pairs (1, 1), (1, 2), (1, 3), (2, 3), (2, 4), (3, 1),
(3, 4), (3,5), (4,2), (4,5), (5,1), (5,2), and (5,4). Find
a) R2. b) R3. c) R4. d) R5.
```

**60**（精选版未找到，请查 PDF）


**仅需读（4 题）：**

**3(read)**  **[仅读]**

```
3. For each of these relations on the set {1, 2, 3, 4}, decide
whether it is reﬂexive, whether it is symmetric, whether
it is antisymmetric, and whether it is transitive.
a) {(2, 2), (2, 3), (2, 4), (3, 2), (3, 3), (3, 4)}
b) {(1, 1), (1, 2), (2, 1), (2, 2), (3, 3), (4, 4)}
c) {(2, 4), (4, 2)}
d) {(1, 2), (2, 3), (3, 4)}
e) {(1, 1), (2, 2), (3, 3), (4, 4)}
f) {(1, 3), (1, 4), (2, 3), (2, 4), (3, 1), (3, 4)}
```

**21(read)**  **[仅读]**

```
21. Which relations in Exercise 6 are asymmetric?
```

**27(read)**  **[仅读]**

```
27. Let R be the relation R ={ (a, b)∣a divides b} on the set
of positive integers. Find
a) R
−1. b) R.
```

**49(read)**（精选版未找到，请查 PDF）


---

## 9.3 关系表示

### 三种表示

| 表示 | 适用 |
|---|---|
| **集合** (有序对列表) | 小集合 |
| **0-1 矩阵** | 中等规模 |
| **有向图** | 中等规模，可视化 |

### 矩阵运算 ↔ 关系运算

| 关系运算 | 矩阵运算 |
|---|---|
| R ∪ S | M_R ∨ M_S |
| R ∩ S | M_R ∧ M_S |
| **R ∘ S**（复合） | **M_S × M_R**（注意顺序） |
| R⁻¹（逆） | M_R 转置 |
| R̄（补） | ~M_R |

> [!warning] 复合 R∘S 对应矩阵 M_S × M_R（**S 的矩阵在左边**）

### 配套作业

**必做题（11 题）：**

**2(c)** （小问：c）

```
2. b) R3. c) R4.
```

**4** 

```
4. List the ordered pairs in the relations on{1, 2, 3, 4} corre-
sponding to these matrices (where the rows and columns
correspond to the integers listed in increasing order).
a)
⎡
⎢
⎢
⎢⎣
1101
1010
0111
1011
⎤
⎥
⎥
⎥⎦
b)
⎡
⎢
⎢
⎢⎣
1110
0100
0011
1001
⎤
⎥
⎥
⎥⎦
c)
⎡
⎢
⎢
⎢⎣
0101
1010
0101
1010
⎤
⎥
⎥
⎥⎦
```

**8** 

```
8. Determine whether the relations represented by the ma-
trices in Exercise 4 are reﬂexive, irreﬂexive, symmetric,
antisymmetric, and/or transitive.
```

**10** 

```
10. How many nonzero entries does the matrix representing
the relation R on A ={ 1, 2, 3,… , 1000} consisting of the
ﬁrst 1000 positive integers have if R is
a) {(a, b)∣a ≤ b}?
b) {(a, b)∣a = b± 1}?
c) {(a, b)∣a+ b = 1000}?
d) {(a, b)∣a+ b ≤ 1001}?
e) {(a, b)∣a ≠ 0}?
```

**12** 

```
12. How can the matrix for R−1,t h ei n v e r s eo ft h e
relation R, be found from the matrix representing R,
when R is a relation on a ﬁnite set A?
```

**14** 

```
14. Let R1 and R2 be relations on a set A represented by the
matrices
MR1
=
⎡
⎢
⎢⎣
010
111
100
⎤
⎥
⎥⎦
and MR2
=
⎡
⎢
⎢⎣
010
011
111
⎤
⎥
⎥⎦
.
Find the matrices that represent
a) R1 ∪R2. b) R1 ∩R2. c) R2 ◦R1.
d) R1 ◦R1. e) R1 ⊕R2.
```

**16** 

```
16. Let R b ear e l a t i o no nas e tA with n elements. If there
are k nonzero entries in MR, the matrix representing R,
how many nonzero entries are there in MR−1, the matrix
representing R−1,t h ei n v e r s eo fR?
```

**22** 

```
22. Draw the directed graph that represents the relation
{(a, a), (a, b), (b, c), (c, b), (c, d), (d, a), (d, b)}.
In Exercises 23–28 list the ordered pairs in the relations rep-
resented by the directed graphs.
```

**30** 

```
30. How can the directed graph of a relation R on a ﬁnite
set A be used to determine whether a relation is irreﬂex-
ive?
```

**32** 

```
32. Determine whether the relations represented by the di-
rected graphs shown in Exercises 26–28 are reﬂexive, ir-
reﬂexive, symmetric, antisymmetric, asymmetric, and/or
transitive.
```

**34** 

```
34. Let R b ear e l a t i o no nas e tA. Explain how to use the di-
rected graph representing R to obtain the directed graph
representing the complementary relation R.
```


**仅需读（2 题）：**

**15(read)**  **[仅读]**

```
15. Let R be the relation represented by the matrix
MR =
⎡
⎢
⎢⎣
010
001
110
⎤
⎥
⎥⎦
.
Find the matrices that represent
a) R
```

**17(read)**  **[仅读]**

```
17. Let R b ear e l a t i o no nas e tA with n elements. If there
are k nonzero entries in MR, the matrix representing R,
how many nonzero entries are there in MR, the matrix
representing R, the complement of R?
```


---

## 9.4 关系的闭包（**必考**）

### 三大闭包

| 闭包 | 记号 | 构造方法 |
|---|---|---|
| **自反闭包** | r(R) | 矩阵对角线全置 1 |
| **对称闭包** | s(R) | 矩阵关于对角线求并（M ∨ Mᵀ） |
| **传递闭包** | t(R) | **Warshall 算法**（反复 M ∨ M²） |

### 反复考的：Warshall 算法（**必考大题**）

**算法步骤**：

设 M 是关系 R 的 0-1 矩阵

```
W₀ = M
For k = 1 to n:
    Wₖ[i][j] = 1 iff (Wₖ₋₁[i][j] = 1) OR (Wₖ₋₁[i][k] = 1 AND Wₖ₋₁[k][j] = 1)
Wₙ = 传递闭包 t(R)
```

**关键**：在第 k 步，把 i 经 k 到 j 的路径标为 1

> [!tip] Wₖ 含义：考虑中间节点 ∈ {1, 2, ..., k} 时 i 到 j 的可达性

### 反复考的：自反闭包 + 对称闭包

**自反闭包**：r(R) = R ∪ I_A，其中 I_A = { (a,a) : a ∈ A }

**对称闭包**：对每条 (a,b) 边加反向 (b,a)

### 配套作业

**必做题（10 题）：**

**26(c)(d)** （小问：c, d）

```
26. Use Algorithm 1 to ﬁnd the transitive closures of these
relations on{a, b, c, d, e}.
a) {(a, c), (b, d), (c, a), (d, b), (e, d)}
b) {(b, c), (b, e), (c, e), (d, a), (e, b), (e, c)}
c) {(a, b), (a, c), (a, e), (b, a),(b, c),(c, a),(c, b),(d, a),
(e, d)}
d) {(a, e), (b, a), (b, d),(c, d),(d, a),(d, c),(e, a),(e, b),
(e, c), (e, e)}
```

**35** 

```
35. Show that the closure with respect to the property P of
the relation R ={ (0, 0), (0, 1), (1, 1), (2, 2)} on the set
{0, 1, 2} does not exist if P is the property
a) “is not reﬂexive.”
b) “has an odd number of elements.”
```

**2** 

```
2. Let R be the relation {(a, b)∣a ≠ b} on the set of inte-
gers. What is the reﬂexive closure of R?
```

**4** 

```
4. How can the directed graph representing the reﬂexive
closure of a relation on a ﬁnite set be constructed from
the directed graph of the relation?
In Exercises 5–7 draw the directed graph of the reﬂexive clo-
sure of the relations with the directed graph shown.
```

**6** 

```
6.
ba
c d
```

**8** 

```
8. How can the directed graph representing the symmetric
closure of a relation on a ﬁnite set be constructed from
the directed graph for this relation?
```

**10** 

```
10. Find the smallest relation containing the relation in Ex-
ample 2 that is both reﬂexive and symmetric.
```

**16(f)** （小问：f）

```
16. Determine whether these sequences of vertices are paths
in this directed graph.
a) a, b, c, e
b) b, e, c, b, e
c) a, a, b, e, d, e
d) b, c, e, d, a, a, b
e) b, c, c, b, e, d, e, d
f) a, a, b, b, c, c, b, e, d
ba c
e
d
```

**18** 

```
18. Determine whether there is a path in the directed graph
in Exercise 16 beginning at the ﬁrst vertex given and
ending at the second vertex given.
a) a, b b) b, a c) b, b
d) a, e e) b, d f) c, d
g) d, d h) e, a i) e, c
```

**22** 

```
22. Suppose that the relation R is reﬂexive. Show that R∗is
reﬂexive.
```


**仅需读（2 题）：**

**29(read)**  **[仅读]**

```
29. Find the smallest relation containing the relation
{(1, 2), (1, 4), (3, 3), (4, 1)} that is
a) reﬂexive and transitive.
b) symmetric and transitive.
c) reﬂexive, symmetric, and transitive.
```

**23(read)**  **[仅读]**

```
23. Suppose that the relation R is symmetric. Show that R∗
is symmetric.
```


---

## 9.5 等价关系（**核心必考**）

### 反复考的核心

#### 题型 1：判断等价关系

```
必须三性质都满足：
  ✓ 自反：∀a, (a,a)∈R
  ✓ 对称：(a,b)∈R → (b,a)∈R
  ✓ 传递：(a,b)∈R ∧ (b,c)∈R → (a,c)∈R
```

#### 题型 2：证明 R 是等价关系

**作业 15 典型**：R = {((a,b),(c,d)) | a+d = b+c}

```
自反：(a,b) → (a,b)：a+b = b+a ✓
对称：(a,b)R(c,d) → a+d=b+c → c+b=d+a → (c,d)R(a,b) ✓
传递：(a,b)R(c,d) ∧ (c,d)R(e,f) → a+d=b+c ∧ c+f=d+e
       → a+d=b+c 和 c+f=d+e → a+d+d+e = b+c+c+f → a+e = b+f → (a,b)R(e,f) ✓
```

#### 题型 3：求等价类

**模 m 同余的等价类**：

```
[a]_m = {x ∈ ℤ | x ≡ a (mod m)}
     = {a + km | k ∈ ℤ}
```

#### 题型 4：等价类 ↔ 划分（**必考**）

**核心定理**：

> 集合 A 上的等价关系 R 与 A 的划分一一对应

**作业 55-66 反复考**：给定划分，找对应等价关系；反之亦然

### 配套作业

**必做题（12 题）：**

**12** 

```
12. Show that the relation R consisting of all pairs (x, y)s u c h
that x and y are bit strings of length three or more that
agree except perhaps in their ﬁrst three bits is an equiva-
lence relation on the set of all bit strings of length three
or more.
```

**15** 

```
15. Let R be the relation on the set of ordered pairs
of positive integers such that (( a, b), (c, d)) ∈R if and
only if a+ d = b+ c. Show that R is an equivalence
relation.
```

**16** 

```
16. Let R be the relation on the set of ordered pairs of pos-
itive integers such that (( a, b), (c, d)) ∈R if and only if
ad = bc. Show that R is an equivalence relation.
```

**22** 

```
22.
a b
d c
```

**24(c)** （小问：c）

```
24. Determine whether the relations represented by these
zero–one matrices are equivalence relations.
a)
⎡
⎢
⎢⎣
111
011
111
⎤
⎥
⎥⎦
b)
⎡
⎢
⎢
⎢⎣
1010
0101
1010
0101
⎤
⎥
⎥
⎥⎦
c)
⎡
⎢
⎢
⎢⎣
1110
1110
1110
0001
⎤
⎥
⎥
⎥⎦
```

**36** 

```
36. What is the congruence class [4]m when m is
a) 2? b) 3? c) 6? d) 8?
```

**40** 

```
40. a) What is the equivalence class of (1, 2) with respect
to the equivalence relation in Exercise 16?
b) Give an interpretation of the equivalence classes for
the equivalence relationR in Exercise 16. [Hint: Look
at the ratio a∕bcorresponding to (a, b).]
```

**42** 

```
42. Which of these collections of subsets are partitions of
{−3,−2,−1,0, 1, 2, 3}?
a) {−3,−1,1, 3}, {−2, 0, 2}
b) {−3,−2,−1,0}, {0, 1, 2, 3}
c) {−3, 3}, {−2, 2}, {−1, 1}, {0}
d) {−3,−2,2, 3}, {−1, 1}
```

**48** 

```
48. List the ordered pairs in the equivalence relations pro-
duced by these partitions of {a, b, c, d, e, f, g}.
a) {a, b},{c, d},{e, f, g}
b) {a}, {b}, {c, d},{e, f},{g}
c) {a, b, c, d},{e, f, g}
d) {a, c, e, g},{b, d},{f}
A partition P1 is called a reﬁnement of the partition P2 if
every set in P1 is a subset of one of the sets in P2.
```

**56** 

```
56. Suppose that R1 and R2 are equivalence relations on the
set S. Determine whether each of these combinations
of R1 and R2 must be an equivalence relation.
a) R1 ∪R2 b) R1 ∩R2 c) R1 ⊕R2
```

**62** 

```
62. Determine the number of diﬀerent equivalence relations
on a set with four elements by listing them.
∗63. Do we necessarily get an equivalence relation when we
form the transitive closure of the symmetric closure of
the reﬂexive closure of a relation?
∗64. Do we necessarily get an equivalence relation when we
form the symmetric closure of the reﬂexive closure of the
transitive closure of a relation?
```

**66** 

```
66. Suppose we use Theorem 2 to form an equivalence rela-
tion R from a partition P. What is the partition P
′that
results if we use Theorem 2 again to form a partition
from R?
```


**仅需读（6 题）：**

**1(read)**  **[仅读]**

```
1. Which of these relations on {0, 1, 2, 3} are equivalence
relations? Determine the properties of an equivalence re-
lation that the others lack.
a) {(0, 0), (1, 1), (2, 2), (3, 3)}
b) {(0, 0), (0, 2), (2, 0), (2, 2), (2, 3), (3, 2), (3, 3)}
c) {(0, 0), (1, 1), (1, 2), (2, 1), (2, 2), (3, 3)}
d) {(0, 0), (1, 1), (1, 3), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)}
e) {(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0),
(2, 2), (3, 3)}
```

**11(read)**  **[仅读]**

```
11. Show that the relation R consisting of all pairs (x, y)s u c h
that x and y are bit strings of length three or more that
agree in their ﬁrst three bits is an equivalence relation on
the set of all bit strings of length three or more.
```

**25(read)**  **[仅读]**

```
25. Show that the relation R on the set of all bit strings such
that sRt if and only if s and t contain the same number
of 1s is an equivalence relation.
```

**55(read)**  **[仅读]**

```
55. Find the smallest equivalence relation on the set
{a, b, c, d, e}containing the relation{(a, b), (a, c), (d, e)}.
```

**57(read)**  **[仅读]**

```
57. Consider the equivalence relation from Example 2,
namely, R ={ (x, y)∣x−y is an integer}.
a) What is the equivalence class of 1 for this equivalence
relation?
b) What is the equivalence class of 1/2 for this equiva-
lence relation?
∗58. Each bead on a bracelet with three beads is either red,
white, or blue, as illustrated in the ﬁgure shown.
Bead 1
Red
Bead 3
Blue
Bead 2
White
Deﬁne the relation R between bracelets as: ( B1,B 2),
where B1 and B2 are bracelets, belongs to R if and only
if B2 can be obtained from B1 by rotating it or rotating it
and then reﬂecting it.
a) Show that R is an equivalence relation.
b) What are the equivalence classes of R?
∗59. Let R be the relation on the set of all colorings of the
2× 2 checkerboard where each of the four squares is col-
ored either red or blue so that (C1,C 2), where C1 and C2
are 2 × 2 checkerboards with each of their four squares
colored blue or red, belongs to R if and only if C2 can be
obtained from C1 either by rotating the checkerboard or
by rotating it and then reﬂecting it.
a) Show that R is an equivalence relation.
b) What are the equivalence classes of R?
```

**65(read)**  **[仅读]**

```
65. Suppose we use Theorem 2 to form a partition P from
an equivalence relation R. What is the equivalence rela-
tion R
′that results if we use Theorem 2 again to form an
equivalence relation from P?
```


---

## 9.6 偏序（**必考**）

### 反复考的核心

#### 题型 1：判断偏序（自反 + 反对称 + 传递）

#### 题型 2：画 Hasse 图（**必考大题**）

**步骤**：

1. 列出所有元素作为顶点
2. 画覆盖关系（无中间元素的 aRb 关系）
3. 按层次排列：最小元在底部，最大元在顶部
4. 不画自环、不画传递边、不画箭头

**作业 2 典型**：(P({1,2}), ⊆) 的 Hasse 图

```
P({1,2}) = {∅, {1}, {2}, {1,2}}
⊆ 关系：
  ∅ ⊆ {1}, ∅ ⊆ {2}, ∅ ⊆ {1,2}
  {1} ⊆ {1,2}, {2} ⊆ {1,2}

Hasse 图：
  {1,2}
   / \
  {1} {2}
   \ /
    ∅
```

#### 题型 3：找极大/极小/最大/最小元素

| 概念 | 定义 |
|---|---|
| **最大元素** | ∀a∈A, a ≤ M |
| **最小元素** | ∀a∈A, m ≤ a |
| **极大元素** | 没有比它**更大**的元素 |
| **极小元素** | 没有比它**更小**的元素 |

> [!warning] 反复错点
> - **最大 ↔ 极大**：最大就是极大，但极大不一定是最大
> - 一个偏序集**最大可能不存在**

#### 题型 4：格（lattice）

**定义**：每对元素都有最小上界（LUB）和最大下界（GLB）的偏序集

**判断方法**：每对 a, b 都有 a∨b（LUB）和 a∧b（GLB）

### 配套作业

**必做题（18 题）：**

**16** 

```
16. a) Let S be the set of subroutines of a computer program.
Deﬁne the relation R by P R Q if subroutine P calls
subroutine Q during its execution. Describe the tran-
sitive closure of R.
b) For which subroutines P does ( P, P) belong to the
transitive closure of R?
c) Describe the reﬂexive closure of the transitive closure
of R.
```

**20** 

```
20. Which of these are equivalence relations on the set of all
people?
a) {(x, y) ∣x and y have the same sign of the zodiac}
b) {(x, y) ∣x and y were born in the same year}
c) {(x, y) ∣x and y have been in the same city}
∗21. How many diﬀerent equivalence relations with exactly
three diﬀerent equivalence classes are there on a set with
ﬁve elements?
```

**22** 

```
22. Show that {(x, y) ∣x−y ∈Q} is an equivalence relation
on the set of real numbers, where Q denotes the set of
rational numbers. What are [1], [1
2 ], and [𝜋]?
Courtesy of George Csicsery
PAUL ERD˝OS (1913–1996) Paul Erd˝os, born in Budapest, Hungary, was the son of two high school mathe-
Links
matics teachers. He was a child prodigy; at age 3 he could multiply three-digit numbers in his head, and at 4 he
discovered negative numbers on his own. Because his mother did not want to expose him to contagious diseases,
he was mostly home-schooled. At 17 Erd˝os entered E˝otv˝os University, graduating four years later with a Ph.D.
in mathematics. After graduating he spent four years at Manchester, England, on a postdoctoral fellowship. In
1938 he went to the United States because of the diﬃcult political situation in Hungary, especially for Jews.
He spent much of his time in the United States, except for 1954 to 1962, when he was banned as part of the
paranoia of the McCarthy era. He also spent considerable time in Israel.
Erd˝os made many signiﬁcant contributions to combinatorics and to number theory. One of the discoveries
of which he was most proud is his elementary proof (in the sense that it does not use any complex analysis)
of the prime number theorem, which provides an estimate for the number of primes not exceeding a ﬁxed positive integer. He also
participated in the modern development of the Ramsey theory.
Erd˝os traveled extensively throughout the world to work with other mathematicians, visiting conferences, universities, and
research laboratories. He had no permanent home. He devoted himself almost entirely to mathematics, traveling from one mathe-
matician to the next, proclaiming “My brain is open.” Erd ˝os was the author or coauthor of more than 1500 papers and had more
than 500 coauthors. Copies of his articles are kept by Ron Graham, a famous discrete mathematician with whom he collaborated
extensively and who took care of many of his worldly needs.
Erd˝os oﬀered rewards, ranging from $10 to $10,000, for the solution of problems that he found particularly interesting, with the
size of the reward depending on the diﬃculty of the problem. He paid out close to $4000. Erd˝os had his own special language, using
such terms as “epsilon” (child), “boss” (woman), “slave” (man), “captured” (married), “liberated” (divorced), “Supreme Fascist”
(God), “Sam” (United States), and “Joe” (Soviet Union). Although he was curious about many things, he concentrated almost all
his energy on mathematical research. He had no hobbies and no full-time job. He never married and apparently remained celibate.
Erd˝os was extremely generous, donating much of the money he collected from prizes, awards, and stipends for scholarships and to
worthwhile causes. He traveled extremely lightly and did not like having many material possessions.

Supplementary Exercises 669
```

**24** 

```
24. Draw the Hasse diagram for inclusion on the set P(S),
where S ={ a, b, c, d}.
In Exercises 25–27 list all ordered pairs in the partial ordering
with the accompanying Hasse diagram.
```

**32** 

```
32. Answer these questions for the partial order represented
by this Hasse diagram.
b
fd
gi
j
a c
e
h
k
ml
a) Find the maximal elements.
b) Find the minimal elements.
c) Is there a greatest element?
d) Is there a least element?
e) Find all upper bounds of{a, b, c}.
f) Find the least upper bound of{a, b, c},i fi te x i s t s .
g) Find all lower bounds of{f, g, h}.
h) Find the greatest lower bound of{f, g, h},i fi te x i s t s .
```

**34** 

```
34. Show that no separate basis case is needed for the princi-
ple of well-founded induction. That is,P(u)i st r u ef o ra l l
minimal elements u in S if∀x(∀y(y≺x → P(y)) → P(x)).
∗35. Show that the principle of well-founded induction is
valid.
A relation R on a set A is a quasi-ordering on A if R is reﬂex-
ive and transitive.
```

**36** 

```
36. Let R be the relation on the set of all functions from
Z
+ to Z+ such that ( f, g) belongs to R if and only if f
is O(g). Show that R is a quasi-ordering.
```

**40** 

```
40. Show that if x and y are elements of a lattice L,t h e n
x∨y = y if and only if x∧y = x.
A lattice L is bounded if it has both an upper bound,d e -
noted by 1, such that x ≼ 1f o ra l lx∈L and a lower bound,
denoted by 0, such that 0 ≼ x for all x ∈L.
```

**42** 

```
42. Show that every ﬁnite lattice is bounded.
A lattice is calleddistributive if x∨(y∧z) = (x∨y)∧(x∨z)
and x∧(y∨z) = (x∧y)∨(x∧z)f o ra l lx, y,a n dz in L.
∗43. Give an example of a lattice that is not distributive.
```

**44** 

```
44. Show that the lattice ( P(S),⊆)w h e r eP(S) is the power
set of a ﬁnite set S is distributive.
```

**46** 

```
46. Give an example of a ﬁnite lattice where at least one el-
ement has more than one complement and at least one
element has no complement.
```

**50** 

```
50. Show that if (S, ⪯) has a greatest element b,t h e naw i n -
ning strategy for Chomp on this poset exists. [Hint: Gen-
eralize the argument in Example 12 in Section 1.8.]
Computer Projects
Write programs with these input and output.
```

**52** 

```
52. Give an example of an inﬁnite lattice with
a) neither a least nor a greatest element.
b) a least but not a greatest element.
c) a greatest but not a least element.
d) both a least and a greatest element.
```

**2** 

```
2. Describe the basic principles of relational databases, go-
ing beyond what was covered in Section 9.2. How widely
used are relational databases as compared with other
types of databases?
```

**6** 

```
6. Describe how equivalence classes can be used to deﬁne
the rational numbers as classes of pairs of integers and
how the basic arithmetic operations on rational numbers
can be deﬁned following this approach. (See Exercise 40
in Section 9.5.)
```

**8(a)** （小问：a）

```
8. Describe some of the mechanisms used to enforce infor-
mation ﬂow policies in computer operating systems.
```

**12** 

```
12. Explain what is meant by a modular lattice. Describe
some of the properties of modular lattices and describe
how modular lattices arise in the study of projective
geometry.
```

**14** 

```
14. Given the matrix representing a relation on a ﬁnite set,
ﬁnd the matrix representing the smallest equivalence re-
lation containing this relation.
```


**仅需读（4 题）：**

**39(read)**  **[仅读]**

```
39. Show that the following properties hold for all elements
x, y,a n dz of a lattice L.
a) x∧y = y∧x and x∨y = y∨x (commutative laws)
b) (x∧y)∧z = x∧(y∧z)a n d( x∨y)∨z = x∨(y∨z)
(associative laws)
c) x∧(x∨y) = x and x∨(x∧y) = x (absorption laws)
d) x∧x = x and x∨x = x (idempotent laws)
```

**41(read)**  **[仅读]**

```
41. Show that if L is a bounded lattice with upper bound
1 and lower bound 0 then these properties hold for all
elements x ∈L.
a) x∨1 = 1 b) x∧1 = x
c) x∨0 = x d) x∧0 = 0
```

**43(read)**  **[仅读]**

```
43. Determine whether the posets with these Hasse diagrams
are lattices.
a)
a
b
d
c
e
f
g
b)
a
b
d
c
e
f g
h
c)
a
b
d
c
e
fg
h
i
```

**45(read)**  **[仅读]**

```
45. Is the lattice (Z+,∣) distributive?
The complement of an element a of a bounded lattice L with
upper bound 1 and lower bound 0 is an element b such that
a∨b = 1a n da ∧b = 0. Such a lattice is complemented if
every element of the lattice has a complement.
```


---

## 章末自检清单

- [ ] 4 大关系性质判定（自反/对称/反对称/传递）
- [ ] 关系矩阵 + 关系有向图
- [ ] 矩阵运算 ↔ 关系运算（特别是 R∘S = M_S × M_R）
- [ ] **自反/对称/传递闭包的构造**
- [ ] **Warshall 算法**（**必考大题**）
- [ ] **证明等价关系**（三性质都证）
- [ ] **求等价类**（特别是模 m 同余）
- [ ] **等价类 ↔ 划分的一一对应**（**必考**）
- [ ] **画 Hasse 图**（**必考大题**）
- [ ] **找极大/极小/最大/最小元素**（**必考**）
- [ ] 判断格
