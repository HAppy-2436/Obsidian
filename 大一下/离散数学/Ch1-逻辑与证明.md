# 第一章 逻辑与证明

> **考试分值**：4 题 / 30 分（与 Ch2、Ch9 共出 4 题，本章约 1-2 题）
> **考纲 section**：1.1, 1.3, 1.4, 1.5, 1.6（**不考** 1.2 / 1.7 / 1.8）
> **作业覆盖**：5 个 section，共 31 道必做题

## 反复出现的考点

| 排名 | 考点 | 出现频次 |
|---|---|---|
| ★★★ | **1.6 用规则证明论证有效** | 4+ |
| ★★★ | **1.6 找论证形式 + 判断有效性** | 4 |
| ★★★ | **1.6 指出论证错误 / 找反例** | 5 |
| ★★☆ | **1.6 谓词规则证明** | 3 |
| ★★☆ | **1.1 真值表判断命题等价** | 8+ |
| ★☆☆ | **1.3 条件 ↔ 析取转换** | 3 |
| ★☆☆ | **1.4-1.5 量词翻译 + 否定** | 8+ |

> [!warning] 重点
> **1.6 推理规则是 Ch1 核心**——8 条命题规则 + 4 条谓词规则必须会默写

---

## 1.1 命题逻辑

### 真值表（必背）

| 符号 | 名称 | 真值规则 |
|---|---|---|
| ¬p | 否定 | 0→1, 1→0 |
| p ∧ q | 合取 | 都 1 才 1 |
| p ∨ q | 析取 | 都 0 才 0 |
| p ⊕ q | 异或 | 相异为 1 |
| **p → q** | 条件 | **p=1, q=0 时为 0；其他都为 1** |
| p ↔ q | 双条件 | 真值相同才 1 |

> [!tip] 速记
> 条件 p→q：**只有 p 真 q 假才假**（"承诺"逻辑）

### 反复考的题型

1. **翻译自然语言为符号**：用 p, q 表示原命题
2. **画真值表**：列出所有 2ⁿ 行赋值
3. **判断等价**：两列真值相同则等价
4. **位运算求值**：把命题当 bit string 计算

### 配套作业（必做题全文）

**必做题（9 题）：**

**2** 

```
2. Which of these are propositions? What are the truth
values of those that are propositions?
a) Do not pass go.
b) What time is it?
c) There are no black ﬂies in Maine.
d) 4+ x = 5.
e) The moon is made of green cheese.
f) 2n ≥ 100.
```

**10** 

```
10. Let p and q be the propositions
p: I bought a lottery ticket this week.
q: I won the million dollar jackpot.
Express each of these propositions as an English sen-
tence.
a) ¬p b) p∨q c) p → q
d) p∧q e) p ↔ q f) ¬p → ¬q
g) ¬p∧¬q h) ¬p∨(p∧q)
```

**12** 

```
12. Let p and q be the propositions “The election is decided”
and “The votes have been counted,” respectively. Express
each of these compound propositions as an English sen-
tence.
a) ¬p b) p∨q
c) ¬p∧q d) q → p
e) ¬q → ¬p f) ¬p → ¬q
g) p ↔ q h) ¬q∨(¬p∧q)
```

**14** 

```
14. Let p, q,a n dr be the propositions
p: You have the ﬂu.
q: You miss the ﬁnal examination.
r: You pass the course.
Express each of these propositions as an English sen-
tence.
a) p → q b) ¬q ↔ r
c) q → ¬r d) p∨q∨r
e) (p → ¬r)∨(q → ¬r) f) (p∧q)∨(¬q∧r)
```

**18** 

```
18. Determine whether these biconditionals are true or
false.
a) 2+ 2 = 4 if and only if 1+ 1 = 2.
b) 1+ 1 = 2 if and only if 2+ 3 = 4.
c) 1+ 1 = 3 if and only if monkeys can ﬂy.
d) 0 > 1 if and only if 2 > 1.
```

**32** 

```
32. How many rows appear in a truth table for each of these
compound propositions?
a) (q → ¬p)∨(¬p → ¬q)
b) (p∨¬t)∧(p∨¬s)
c) (p → r)∨(¬s → ¬t)∨(¬u → v)
d) (p∧r∧s)∨(q∧t)∨(r∧¬t)
```

**34** 

```
34. Construct a truth table for each of these compound propo-
sitions.
a) p → ¬p b) p ↔ ¬p
c) p⊕(p∨q) d) (p∧q) → (p∨q)
e) (q → ¬p) ↔ (p ↔ q)
f) (p ↔ q)⊕(p ↔ ¬q)
```

**36** 

```
36. Construct a truth table for each of these compound propo-
sitions.
a) p⊕p b) p⊕¬p
c) p⊕¬q d) ¬p⊕¬q
e) (p⊕q)∨(p⊕¬q) f) (p⊕q)∧(p⊕¬q)
```

**38** 

```
38. Construct a truth table for each of these compound propo-
sitions.
a) (p∨q)∨r b) (p∨q)∧r
c) (p∧q)∨r d) (p∧q)∧r
e) (p∨q)∧¬r f) (p∧q)∨¬r
```


---

## 1.3 命题等价

### 必背等价律

| 名称 | 公式 |
|---|---|
| 同一律 | p∧T ≡ p, p∨F ≡ p |
| 支配律 | p∨T ≡ T, p∧F ≡ F |
| 幂等律 | p∨p ≡ p, p∧p ≡ p |
| 双重否定 | ¬¬p ≡ p |
| 交换/结合 | p∨q ≡ q∨p, (p∨q)∨r ≡ p∨(q∨r) |
| 分配律 | p∨(q∧r) ≡ (p∨q)∧(p∨r) |
| 德摩根律 | ¬(p∧q) ≡ ¬p∨¬q |
| 吸收律 | p∨(p∧q) ≡ p |
| 否定律 | p∨¬p ≡ T, p∧¬p ≡ F |

### 必背转换（反复考）

| 转换 | 公式 |
|---|---|
| **条件 → 析取** | p → q ≡ **¬p ∨ q** |
| **条件否定** | ¬(p → q) ≡ **p ∧ ¬q** |
| **双条件 → 复合** | p ↔ q ≡ (p∧q)∨(¬p∧¬q) |
| **双条件否定** | ¬(p ↔ q) ≡ **p ⊕ q** |
| **异或** | p ⊕ q ≡ (p∧¬q)∨(¬p∧q) |

> [!warning] 易错
> - ¬(p→q) ≡ p∧¬q（**不是** ¬p→¬q）
> - 逆否等价：p→q ≡ ¬q→¬p（**正确**），但 p→q ≡ q→p（**错**）

### 配套作业

**必做题（6 题）：**

**4** 

```
4. Use truth tables to verify the associative laws
a) (p∨q)∨r ≡ p∨(q∨r).
b) (p∧q)∧r ≡ p∧(q∧r).
```

**12** 

```
12. Show that each of these conditional statements is a tau-
tology by using truth tables.
a) [¬p∧(p∨q)] → q
b) [(p → q)∧(q → r)] → (p → r)
c) [p∧(p → q)] → q
d) [(p∨q)∧(p → r)∧(q → r)] → r
```

**18** 

```
18. Determine whether (¬p∧(p → q)) → ¬q is a tautology.
```

**32** 

```
32. Show that p ↔ q and ¬p ↔ ¬q are logically equivalent.
```

**34** 

```
34. Show that (p∨q)∧(¬p∨r) → (q∨r) is a tautology.
```

**66(a)(b)** （小问：a, b）

```
66. Determine whether each of these compound propositions
is satisﬁable.
a) (p∨q∨¬r)∧(p∨¬q∨¬s)∧(p∨¬r∨¬s)∧
(¬p∨¬q∨¬s)∧(p∨q∨¬s)
b) (¬p∨¬q∨r)∧(¬p∨q∨¬s)∧(p∨¬q∨¬s)∧
(¬p∨¬r∨¬s)∧(p∨q∨¬r)∧(p∨¬r∨¬s)
c) (p∨q∨r)∧(p∨¬q∨¬s)∧(q∨¬r∨s) ∧(¬p∨
r∨s)∧(¬p∨q∨¬s)∧(p∨¬q∨¬r) ∧(¬p∨
¬q∨s)∧(¬p∨¬r∨¬s)
```


---

## 1.4 谓词与量词

### 核心

$$\neg \forall x\, P(x) \equiv \exists x\, \neg P(x)$$
$$\neg \exists x\, P(x) \equiv \forall x\, \neg P(x)$$

### 限制论域

- ∀x ∈ S P(x) ≡ ∀x (x ∈ S **→** P(x))
- ∃x ∈ S P(x) ≡ ∃x (x ∈ S **∧** P(x))

> **∀ 用 →，∃ 用 ∧**——反复错点

### 空论域

- 空论域时 ∀x P(x) 为真（**空真**）
- 空论域时 ∃x P(x) 为假

### 配套作业

**必做题（7 题）：**

**12** 

```
12. Let Q(x) be the statement “ x+ 1 > 2x.” If the domain
consists of all integers, what are these truth values?
a) Q(0) b) Q(−1) c) Q(1)
d) ∃xQ(x) e) ∀xQ(x) f) ∃x¬Q(x)
g) ∀x¬Q(x)
```

**14** 

```
14. Determine the truth value of each of these statements if
the domain consists of all real numbers.
a) ∃x(x
3 =−1) b) ∃x(x4 < x2)
c) ∀x((−x)2 = x2) d) ∀x(2x > x)
```

**16** 

```
16. Determine the truth value of each of these statements
if the domain of each variable consists of all real num-
bers.
a) ∃x(x2 = 2) b) ∃x(x2 =−1)
c) ∀x(x2 + 2 ≥ 1) d) ∀x(x2 ≠ x)
```

**18** 

```
18. Suppose that the domain of the propositional function
P(x) consists of the integers −2,−1, 0, 1, and 2. Write
out each of these propositions using disjunctions, con-
junctions, and negations.
a) ∃xP(x) b) ∀xP(x) c) ∃x¬P(x)
d) ∀x¬P(x) e) ¬∃xP(x) f) ¬∀xP(x)
```

**20** 

```
20. Suppose that the domain of the propositional function
P(x) consists of −5,−3,−1, 1, 3, and 5. Express these
statements without using quantiﬁers, instead using only
negations, disjunctions, and conjunctions.
a) ∃xP(x) b) ∀xP(x)
c) ∀x((x ≠ 1) → P(x))
d) ∃x((x ≥ 0)∧P(x))
e) ∃x(¬P(x))∧∀x((x < 0) → P(x))
```

**30** 

```
30. Suppose the domain of the propositional function P(x, y)
consists of pairsx and y,w h e r ex is 1, 2, or 3 andy is 1, 2,
or 3. Write out these propositions using disjunctions and
conjunctions.
a) ∃xP(x, 3) b) ∀yP(1,y )
c) ∃y¬P(2,y) d) ∀x¬P(x, 2)
```

**38** 

```
38. Find a counterexample, if possible, to these universally
quantiﬁed statements, where the domain for all variables
consists of all real numbers.
a) ∀x(x2 ≠ x) b) ∀x(x2 ≠ 2)
c) ∀x(|x|> 0)
```


---

## 1.5 嵌套量词

### 核心：量词顺序

| 同类 | 可交换？ |
|---|---|
| ∀x∀y P(x,y) ≡ ∀y∀x P(x,y) | ✅ |
| ∃x∃y P(x,y) ≡ ∃y∃x P(x,y) | ✅ |
| **∀x∃y P(x,y) ≡ ∃y∀x P(x,y)** | ❌ |

> [!warning] ∀∃ 与 ∃∀ 含义不同：
> - ∀x ∃y (x < y)：每个数都有比自己大的数（**真**）
> - ∃y ∀x (x < y)：存在最大数（**假**）

### 嵌套量词的否定

逐层取反：

$$\neg \forall x \exists y\, P(x,y) \equiv \exists x \forall y\, \neg P(x,y)$$

### 配套作业

**必做题（4 题）：**

**26** 

```
26. Let Q(x, y) be the statement “ x+ y = x−y.” If the do-
main for both variables consists of all integers, what are
the truth values?
a) Q(1, 1) b) Q(2, 0)
c) ∀yQ(1,y) d) ∃xQ(x,2)
e) ∃x∃yQ(x, y) f) ∀x∃yQ(x, y)
g) ∃y∀xQ(x, y) h) ∀y∃xQ(x, y)
i) ∀x∀yQ(x, y)
```

**28** 

```
28. Determine the truth value of each of these statements
if the domain of each variable consists of all real num-
bers.
a) ∀x∃y(x2 = y) b) ∀x∃y(x= y2)
c) ∃x∀y(xy= 0) d) ∃x∃y(x+ y ≠ y + x)
e) ∀x(x ≠ 0 → ∃y(xy= 1))
f) ∃x∀y(y≠ 0 → xy = 1)
g) ∀x∃y(x+ y = 1)
h) ∃x∃y(x+ 2y = 2∧2x+ 4y = 5)
i) ∀x∃y(x+ y = 2∧2x−y = 1)
j) ∀x∀y∃z(z= (x+ y)∕2)
```

**30** 

```
30. Rewrite each of these statements so that negations ap-
pear only within predicates (that is, so that no negation
is outside a quantiﬁer or an expression involving logical
connectives).
a) ¬∃y∃xP(x, y) b) ¬∀x∃yP(x, y)
c) ¬∃y(Q(y)∧∀x¬R(x, y))
d) ¬∃y(∃xR(x, y)∨∀xS(x, y))
e) ¬∃y(∀x∃zT(x, y, z)∨∃x∀zU(x, y, z))
```

**40** 

```
40. Find a counterexample, if possible, to these universally
quantiﬁed statements, where the domain for all variables
consists of all integers.
a) ∀x∃y(x= 1∕y)
b) ∀x∃y(y2 −x < 100)
c) ∀x∀y(x2 ≠ y3)
```


---

## 1.6 推理规则（**核心必考大题**）

### 8 条命题规则（必背）

| 规则名 | 形式 |
|---|---|
| **MP** (Modus Ponens) | p→q, p ⊢ q |
| **MT** (Modus Tollens) | p→q, ¬q ⊢ ¬p |
| **HS** (Hypothetical Syllogism) | p→q, q→r ⊢ p→r |
| **DS** (Disjunctive Syllogism) | p∨q, ¬p ⊢ q |
| **Add** (Addition) | p ⊢ p∨q |
| **Simp** (Simplification) | p∧q ⊢ p |
| **Conj** (Conjunction) | p, q ⊢ p∧q |
| **Res** (Resolution) | p∨q, ¬p∨r ⊢ q∨r |

### 4 条谓词规则

| 规则名 | 形式 | 关键限制 |
|---|---|---|
| **UI** | ∀x P(x) ⊢ P(c) | c 是**任意**元素（可复用） |
| **UG** | P(c) ⊢ ∀x P(x) | c 必须**真的任意** |
| **EI** | ∃x P(x) ⊢ P(c) | c 是**某个特定**元素（**不能用于 UG**） |
| **EG** | P(c) ⊢ ∃x P(x) | c 是某个元素 |

> [!warning] 易错
> - EI 推出的 c **不能用于 UG**（c 是"某个特定"而不是"任意"）

### 反复出现的题型 1：用规则证明论证有效（**必考大题**）

**典型题目（作业 12）**：

```
12. Show that the argument form with premises (p ∧t) →
(r∨s), q → (u∧t), u → p,a n d¬s and conclusion q → r
is valid by ﬁrst using Exercise 11 and then using rules of
inference from Table 1.
```

**标准解法步骤**：

1. 把条件命题转换：p→q ≡ ¬p∨q
2. 从结论反推：结论需要什么前件？
3. 从已知前件开始：能用 MP/MT/HS 的就先用
4. 每步标注规则名 + 行号

**作业 12 完整解法参考**：

```
1. (p∧t)→(r∨s)              前提
2. q→(u∧t)                   前提
3. u→p                       前提
4. ¬s                        前提
5. 假设 q                    条件证明
6. u∧t                       2,5,MP
7. u                         6,Simp
8. t                         6,Simp
9. p                         3,7,MP
10. p∧t                      8,9,Conj
11. r∨s                      1,10,MP
12. r                        11,4,DS    ← 关键：s 排除掉，留 r
13. ∴ q→r                    5-12 条件证明
```

### 反复出现的题型 2：找论证形式 + 判断有效性

**典型 valid 论证**（必背）：

- 假言推理：p→q, p, ∴ q
- 拒取式：p→q, ¬q, ∴ ¬p
- 假言三段论：p→q, q→r, ∴ p→r
- 析取三段论：p∨q, ¬p, ∴ q

**典型 invalid 论证**：

- 肯定后件：p→q, q, ∴ p（**谬误**）
- 否定前件：p→q, ¬p, ∴ ¬q（**谬误**）

### 反复出现的题型 3：指出论证错误 / 找反例

**典型错误**（作业 17）：

```

```

**错误分析**：

```
前提: ∃x H(x)
结论: H(Lola)

错误: ∃x H(x) 只能推出 ∃x H(x) → H(c) (某个 c)，不能推出 H(Lola)
     "某个快乐的人存在" ≠ "Lola 快乐"
```

### 反复出现的题型 4：用消解证

**典型题目（作业 30）**：

```
30. Use resolution to show the hypotheses “Allen is a bad
boy or Hillary is a good girl” and “Allen is a good boy or
David is happy” imply the conclusion “Hillary is a good
girl or David is happy.”
```

**解法**：

```
1. A∨H                      前提
2. ¬A∨D                     前提
3. H∨D                      1,2, Res  ← 消解
```

### 配套作业

**必做题（5 题）：**

**12** 

```
12. Show that the argument form with premises (p ∧t) →
(r∨s), q → (u∧t), u → p,a n d¬s and conclusion q → r
is valid by ﬁrst using Exercise 11 and then using rules of
inference from Table 1.
```

**24** 

```
24. Identify the error or errors in this argument that sup-
posedly shows that if ∀x(P(x)∨Q(x)) is true then
∀xP(x)∨∀xQ(x)i st r u e .
```

**26** 

```
26. Justify the rule of universal transitivity, which states
that if ∀x(P(x) → Q(x)) and ∀x(Q(x) → R(x)) are true,
then ∀x(P(x) → R(x)) is true, where the domains of all
quantiﬁers are the same.
```

**28** 

```
28. Use rules of inference to show that if∀x(P(x)∨Q(x)) and
∀x((¬P(x)∧Q(x)) → R(x)) are true, then ∀x(¬R(x) →
P(x)) is also true, where the domains of all quantiﬁers
are the same.
```

**30** 

```
30. Use resolution to show the hypotheses “Allen is a bad
boy or Hillary is a good girl” and “Allen is a good boy or
David is happy” imply the conclusion “Hillary is a good
girl or David is happy.”
```


---

## 章末自检清单

- [ ] 5 个联结词真值表（条件 p→q 是核心）
- [ ] 10 条等价律
- [ ] **p→q ↔ ¬p∨q** 和 **p↔q ↔ (p∧q)∨(¬p∧¬q)**
- [ ] 量词德摩根律
- [ ] ∀ 用 →、∃ 用 ∧（限制论域）
- [ ] ∀∃ 与 ∃∀ 不可交换
- [ ] **8 条命题规则全默写**（必考）
- [ ] **4 条谓词规则** UI/UG/EI/EG 区别
- [ ] **EI 不能接 UG**（必考易错）
- [ ] 用规则写完整证明（标注规则名 + 行号）
- [ ] 区分 MP/MT vs 肯定后件/否定前件谬误
- [ ] 会用消解（Resolution）
