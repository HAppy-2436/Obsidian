# 第一章 逻辑与证明（按知识点组织）

> **考试分值**：4 题 / 30 分（与 Ch2、Ch9 合并）
> **考纲范围**：1.1, 1.3, 1.4, 1.5, 1.6（**不考** 1.2 应用、1.7/1.8 证明方法）
> **必考大题**：1.6 推理规则（每年必出）
> **总题数**：约 209 道

---

## 知识点地图

| 知识点 | 出处 | 频次 | 难度 |
|---|---|---|---|
| K1 命题与联结词 | 1.1 | ★★★ | 易 |
| K2 真值表 + 条件句变形 | 1.1 | ★★★ | 易 |
| K3 命题等价 + De Morgan | 1.3 | ★★★ | 中 |
| K4 谓词与量词 | 1.4 | ★★★ | 中 |
| K5 嵌套量词 + 量词否定 | 1.5 | ★★☆ | 中 |
| K6 推理规则（必考大题）| 1.6 | ★★★ | 难 |

---

# K1 命题与联结词

## 核心概念

**命题（proposition）**：有唯一真值的陈述句。命令、疑问、悖论不算。

**5 个联结词（按优先级从高到低）**：

| 符号 | 名称 | 含义 |
|---|---|---|
| ¬p | 否定（非） | 反转 |
| p ∧ q | 合取（与） | **都**真才真 |
| p ∨ q | 析取（或） | **有**真就真（含"或"是 inclusive）|
| p → q | 条件（蕴含） | p 真 q 假才**假**（p 假永远真）|
| p ↔ q | 双条件 | p、q 真值**相同**才真 |

## 反复考的题型

### 题型 1：自然语言 ↔ 符号化（高频）

**符号化技巧**：
- "p 但 q" → p ∧ q
- "p 或 q（含两者）" → p ∨ q
- "如果 p 那么 q" / "p 仅当 q" / "p 是 q 的充分条件" → p → q
- "p 仅当 q" = "p → q"（注意是 p → q 不是 q → p）
- "p 当且仅当 q" → p ↔ q
- "除非 q 否则 p" = "如果非 q 那么 p" = ¬q → p

### 题型 2：复合命题求真值（p, q 给具体值时）

直接按真值表逐个求。

### 题型 3：in / exclusive or 判定

- **inclusive or** = ∨（"或两者"）
- **exclusive or** = ⊕（"或其一，但不同时"）

## 配套作业（题号 + 完整题目）

**Section 1.1**

**3.** What is the negation of each of these propositions?
a) Linda is younger than Sanjay.
b) Mei makes more money than Isabella.
c) Moshe is taller than Monica.
d) Abby is richer than Ricardo.

**5.** What is the negation of each of these propositions?
a) Mei has an MP3 player.
b) There is no pollution in New Jersey.
c) 2+1 = 3.
d) The summer in Maine is hot and sunny.

**10.** Let p and q be the propositions
p: I bought a lottery ticket this week.
q: I won the million dollar jackpot.
Express each of these propositions as an English sentence.
a) ¬p　b) p∨q　c) p→q　d) p∧q　e) p↔q　f) ¬p→¬q　g) ¬p∧¬q　h) ¬p∨(p∧q)

**13.** Let p and q be the propositions
p: It is below freezing.　q: It is snowing.
Write these propositions using p, q, and logical connectives (including negations).
a) It is below freezing and snowing.
b) It is below freezing but not snowing.
c) It is not below freezing and it is not snowing.
d) It is either snowing or below freezing (or both).
e) If it is below freezing, it is also snowing.
f) Either it is below freezing or it is snowing, but it is not snowing if it is below freezing.
g) That it is below freezing is necessary and sufficient for it to be snowing.

**18.** Determine whether these biconditionals are true or false.
a) 2+2 = 4 if and only if 1+1 = 2.
b) 1+1 = 2 if and only if 2+3 = 4.
c) 1+1 = 3 if and only if monkeys can fly.
d) 0 > 1 if and only if 2 > 1.

**19.** Determine whether each of these conditional statements is true or false.
a) If 1+1 = 2, then 2+2 = 5.
b) If 1+1 = 3, then 2+2 = 4.
c) If 1+1 = 3, then 2+2 = 5.
d) If monkeys can fly, then 1+1 = 3.

**21.** For each of these sentences, determine whether an inclusive or, or an exclusive or, is intended.
a) Coffee or tea comes with dinner.
b) A password must have at least three digits or be at least eight characters long.
c) The prerequisite for the course is a course in number theory or a course in cryptography.
d) You can pay using U.S. dollars or euros.

---

# K2 真值表 + 条件句变形

## 核心概念

**真值表行数**：n 个命题变量 → **2^n 行**。

**条件句 p → q 的"反直觉"真值**：

| p | q | p→q |
|---|---|---|
| T | T | **T** |
| T | F | **F** |
| F | T | **T** |
| F | F | **T** |

> 关键：**p 假时 p→q 永远为真**（"vacuous truth"）。
> 例子："如果雪是黑的，那么我是皇帝"——雪不是黑的，所以这句是真的。

**条件句四种形式**（设原条件句 p→q）：

| 名称 | 形式 | 与 p→q 的关系 |
|---|---|---|
| **converse**（逆） | q → p | 不等价 |
| **inverse**（否） | ¬p → ¬q | 不等价，但等价于 converse |
| **contrapositive**（逆否） | ¬q → ¬p | **等价**（必背）|

> **contrapositive ≡ 原条件**：证明时常用逆否命题代替原命题。

**条件句的英文等价**（必背）：

| 表达 | 等价形式 |
|---|---|
| "p implies q" | p→q |
| "if p, then q" | p→q |
| "p is sufficient for q" | p→q |
| "q is necessary for p" | p→q |
| "p only if q"（p 仅当 q）| p→q |
| "q if p" | p→q |
| "p whenever q" | q→p（**注意次序**）|
| "p unless q" | ¬q → p |

## 反复考的题型

### 题型 1：求真值表行数
n 个不同变量 → 2^n 行。

### 题型 2：构造真值表
列出所有 2^n 种赋值 → 逐列计算 → 看是否全 T（永真）、全 F（永假）、或两者都不是（偶然式 contingency）。

### 题型 3：converse / inverse / contrapositive
设原命题 → 写三种变形 → **只有 contrapositive 等价于原命题**。

### 题型 4：自然语言转 "if p, then q"
看清主语谓语，注意 "only if" / "unless" / "whenever" 等关键英文短语。

## 配套作业

**Section 1.1（续）**

**24.** Write each of these statements in the form "if p, then q" in English.
a) It is necessary to wash the boss's car to get promoted.
b) Winds from the south imply a spring thaw.
c) A sufficient condition for the warranty to be good is that you bought the computer less than a year ago.
d) Willy gets caught whenever he cheats.
e) You can access the website only if you pay a subscription fee.
f) Getting elected follows from knowing the right people.
g) Carol gets seasick whenever she is on a boat.

**27.** Write each of these propositions in the form "p if and only if q" in English.
a) If it is hot outside you buy an ice cream cone, and if you buy an ice cream cone it is hot outside.
b) For you to win the contest it is necessary and sufficient that you have the only winning ticket.
c) You get promoted only if you have connections, and you have connections only if you get promoted.
d) If you watch television your mind will decay, and conversely.
e) The trains run late on exactly those days when I take it.

**29.** State the converse, contrapositive, and inverse of each of these conditional statements.
a) If it snows today, I will ski tomorrow.
b) I come to class whenever there is going to be a quiz.
c) A positive integer is a prime only if it has no divisors other than 1 and itself.

**31.** How many rows appear in a truth table for each of these compound propositions?
a) p → ¬p
b) (p∨¬r)∧(q∨¬s)
c) q∨p∨¬s∨¬r∨¬t∨u
d) (p∧r∧t) ↔ (q∧t)

**33.** Construct a truth table for each of these compound propositions.
a) p∧¬p　b) p∨¬p　c) (p∨¬q) → q　d) (p∨q) → (p∧q)
e) (p → q) ↔ (¬q → ¬p)　f) (p → q) → (q → p)

**35.** Construct a truth table for each of these compound propositions.
a) (p∨q) → (p⊕q)　b) (p⊕q) → (p∧q)
c) (p∨q)⊕(p∧q)　d) (p ↔ q)⊕(¬p ↔ q)

---

# K3 命题等价 + De Morgan（核心）

## 核心概念

**等价（logically equivalent）**：p ≡ q 当且仅当 p ↔ q 是永真式（tautology）。

**De Morgan 定律**（必背）：

$$\neg(p \wedge q) \equiv \neg p \vee \neg q$$
$$\neg(p \vee q) \equiv \neg p \wedge \neg q$$

**推广到 n 个变量**：
$$\neg(p_1 \vee p_2 \vee \cdots \vee p_n) \equiv \neg p_1 \wedge \neg p_2 \wedge \cdots \wedge \neg p_n$$

**条件等价**（必背）：

$$p \to q \equiv \neg p \vee q \equiv \neg q \to \neg p$$

**条件句否定**（必背）：

$$\neg(p \to q) \equiv p \wedge \neg q$$

**永真 / 永假 / 偶然**：
- **tautology**：永远真（如 p∨¬p）
- **contradiction**：永远假（如 p∧¬p）
- **contingency**：有时真有时假

**核心等价表（Table 6）**：

| 等价律 | 公式 |
|---|---|
| Identity | p∧T≡p, p∨F≡p |
| Domination | p∨T≡T, p∧F≡F |
| Idempotent | p∨p≡p, p∧p≡p |
| Double negation | ¬(¬p)≡p |
| Commutative | p∨q≡q∨p, p∧q≡q∧p |
| Associative | (p∨q)∨r≡p∨(q∨r) |
| Distributive | p∨(q∧r)≡(p∨q)∧(p∨r) |
| De Morgan | 见上 |
| Absorption | p∨(p∧q)≡p |
| Negation | p∨¬p≡T, p∧¬p≡F |

**对偶（dual）**：把所有 ∨ ↔ ∧, T ↔ F 互换。

**满意性（satisfiability）**：至少存在一种赋值使命题为真。否则是 unsatisfiable。

## 反复考的题型

### 题型 1：用真值表证明等价
构造两个命题的真值表 → 比较所有行 → 一致即等价。

### 题型 2：用等价律证明等价（"链式证明"）
从一边开始，每步写出用的等价律，直到变形为另一边。

### 题型 3：De Morgan 求否定
1. 找最外层联结词（∧ 或 ∨）
2. 替换成另一个（∧→∨，∨→∧）
3. 每个子命题取否定

### 题型 4：永真性判断
- 用真值表（n 小时）
- 或用等价律证明 ≡ T（n 大时）

### 题型 5：判断满意性
找一种赋值使命题为真即可，不必找全。

## 配套作业

**Section 1.3**

**5.** Use truth tables to verify these equivalences.
a) p∧T≡p　b) p∨F≡p　c) p∧F≡F　d) p∨T≡T
e) p∨p≡p　f) p∧p≡p

**7.** Use De Morgan's laws to find the negation of each of the following statements.
a) Jan is rich and happy.
b) Carlos will bicycle or run tomorrow.
c) Mei walks or takes the bus to class.
d) Ibrahim is smart and hard working.

**9.** For each of these compound propositions, use the conditional-disjunction equivalence to find an equivalent compound proposition that does not involve conditionals.
a) p → ¬q
b) (p → q) → r
c) (¬q → p) → (p → ¬q)

**11.** Show that each of these conditional statements is a tautology by using truth tables.
a) (p∧q) → p　b) p → (p∨q)　c) ¬p → (p → q)
d) (p∧q) → (p → q)　e) ¬(p → q) → p　f) ¬(p → q) → ¬q

**13.** Show that each conditional statement in Exercise 11 is a tautology using the fact that a conditional statement is false exactly when the hypothesis is true and the conclusion is false. (Do not use truth tables.)

**17.** Use truth tables to verify the absorption laws.
a) p∨(p∧q)≡p　b) p∧(p∨q)≡p

**20.** Show that p↔q and (p∧q)∨(¬p∧¬q) are logically equivalent.

**22.** Show that p→q and ¬q→¬p are logically equivalent.

**26.** Show that (p→q)∧(p→r) and p→(q∧r) are logically equivalent.

**28.** Show that (p→q)∨(p→r) and p→(q∨r) are logically equivalent.

**33.** Find the dual of each of these compound propositions.
a) p∨q　b) (p∧¬q)∨(¬p∧q)　c) (p∧q∧r)∨s

**42.** Show that the logical equivalences in Table 6, except for the double negation law, come in pairs, where each pair contains compound propositions that are duals of each other.

---

# K4 谓词与量词

## 核心概念

**谓词 P(x)**：含变量 x 的命题函数。P(5) 是一个命题（可能有真值）。

**全称量词（∀）**：
- ∀x P(x)：**对所有** x，P(x) 都成立
- "Everyone"、"Everything"、"All" 对应 ∀
- 等价：∀x P(x) ≡ P(x₁) ∧ P(x₂) ∧ ... ∧ P(xₙ)

**存在量词（∃）**：
- ∃x P(x)：**存在**一个 x 使 P(x) 成立
- "Some"、"There exists"、"At least one" 对应 ∃
- 等价：∃x P(x) ≡ P(x₁) ∨ P(x₂) ∨ ... ∨ P(xₙ)

**量词否定（必背）**：

$$\neg \forall x \, P(x) \equiv \exists x \, \neg P(x)$$
$$\neg \exists x \, P(x) \equiv \forall x \, \neg P(x)$$

> **记忆法**：否定量词时，∀ ↔ ∃，谓词也取否定。

**多个量词的优先级**：∀ 和 ∃ 优先级高于所有联结词。

## 反复考的题型

### 题型 1：自然语言 ↔ 量词符号化

**常见模式**：
- "All A are B" → ∀x (A(x) → B(x))
- "Some A are B" → ∃x (A(x) ∧ B(x))
- "No A are B" → ∀x (A(x) → ¬B(x)) 或 ¬∃x (A(x) ∧ B(x))
- "Some A are not B" → ∃x (A(x) ∧ ¬B(x))

> ⚠️ **关键区别**：全称用 →，存在用 ∧。
> 错误示例："All A are B" 错写成 ∀x (A(x) ∧ B(x))。

### 题型 2：量词否定

一步一步：先否定最外层量词（∀↔∃），再否定谓词，重复直到没有量词。

### 题型 3：求真值
对有限域，列所有 x 验证；对无限域，找反例或证明。

## 配套作业

**Section 1.4**

**5.** Let L(x, y) be the statement "x loves y." Write the following in terms of L(x, y), quantifiers, and logical connectives.
a) Everybody loves Jerry.
b) Everybody loves somebody.
c) There is somebody whom everybody loves.
d) Nobody loves everybody.
e) There is somebody whom Lydia does not love.

**10.** Express the statement "No one has more than three grandmothers" using predicates, quantifiers, and logical connectives.

**15.** Determine the truth value of each of these statements if the domain consists of all integers.
a) ∀n(n² ≥ n)
b) ∃n(n² = 2)
c) ∃n(n² < 0)
d) ∀n(n² ≠ n)

**20.** Translate each of these statements into logical expressions using predicates, quantifiers, and logical connectives.
a) No one can fool everyone all of the time.
b) At least one person can fool exactly one person at all times.
c) There is someone in this class who can fool exactly one person in this class.
d) No one in this class can fool exactly two different people in this class.

**30.** Negate each of the following statements.
a) ∀x(x² > x)
b) ∃x(x² = 2)
c) ∀x ∃y(x + y = 0)
d) ∃x ∃y(x + y ≠ 0)
e) ∀x ∀y ∃z(xz = y)

**35.** Find a counterexample, if possible, to these universally quantified statements, where the domain for all variables consists of all integers.
a) ∀x ∃y(x = 1/y)
b) ∀x ∃y(y² − x < 100)
c) ∀x ∀y(x² ≠ y³)
d) ∀x ∃y(xy = x)

**40.** Translate the following sentences into logical expressions.
a) Some student in this class has visited Mexico.
b) Every student in this class has visited either Mexico or Canada.
c) There is a student in this class who has visited both Mexico and Canada.
d) Every student in this class has visited neither Mexico nor Canada.

---

# K5 嵌套量词

## 核心概念

**量词次序很关键**：
- ∀x ∀y P(x, y) ≡ ∀y ∀x P(x, y)（同量词可交换）
- ∃x ∃y P(x, y) ≡ ∃y ∃x P(x, y)
- **∀x ∃y ≠ ∃y ∀x**（不同量词不可交换！）

**典型例子**（理解 ∀x ∃y 与 ∃x ∀y 的区别）：
- ∀x ∃y (x + y = 0)：对任意 x，存在 y 使 x+y=0。**真**（y=-x）
- ∃y ∀x (x + y = 0)：存在 y，使所有 x 都满足 x+y=0。**假**（不同 x 需要不同 y）

**多量词否定**（递推用 K4 规则）：
¬∀x ∃y P(x,y) ≡ ∃x ∀y ¬P(x,y)
¬∃x ∀y P(x,y) ≡ ∀x ∃y ¬P(x,y)

## 反复考的题型

### 题型 1：符号化（最常考）
- "Every x has some y such that..." → ∀x ∃y
- "There is an x such that every y..." → ∃x ∀y
- "For every x and y..." → ∀x ∀y
- "There exists x and y such that..." → ∃x ∃y

### 题型 2：嵌套量词否定
从左到右一个一个否定：∀↔∃，谓词取反。

### 题型 3：嵌套量词翻译为英文
反过来。

## 配套作业

**Section 1.5**

**5.** Translate each of these statements into logical expressions in two different ways.
a) There is a student in this class who can speak Hindi.
b) Every student in this class is friendly.
c) There is a person in this class such that not every person is his or her friend.
d) Every student in this class has studied calculus.
e) Not all students in this class can swim.

**11.** Let L(x, y) be the statement "x loves y." Write the following using logical expressions, quantifiers, and L.
a) Everyone loves himself or herself.
b) There is someone who loves no one.
c) There is someone who is loved by everyone.
d) Everyone is loved by someone.

**15.** Let F(x, y) be the statement "x can fool y." Write the following in terms of F, quantifiers, and logical connectives.
a) Everyone can fool exactly one person other than himself/herself.
b) No one can fool exactly two different people.
c) Everyone can fool at least one other person.
d) There is someone whom everyone can fool.

**20.** Determine the truth value of each of these statements if the domain consists of all real numbers.
a) ∀x ∃y(x² = y)
b) ∀x ∃y(x = y²)
c) ∃x ∀y(xy = 0)
d) ∃x ∀y(xy ≠ 0)
e) ∀x ∃y(x + y > 0)
f) ∃x ∀y(x + y > 0)

**25.** Translate each of these statements into English.
a) ∀x ∃y(x² < y)
b) ∃x ∀y(x < y²)
c) ∀x ∀y ∃z(x + y = z²)
d) ∃x ∃y ∀z(xz = y)
e) ∀x ∀y ∃z(xz + yz = 0)

**30.** Negate each of the following statements.
a) ∃x ∃y P(x, y)
b) ∀x ∃y P(x, y)
c) ∃x ∀y P(x, y)
d) ∀x ∀y P(x, y)
e) ∃x ∃y ¬P(x, y)
f) ¬∃x ∀y P(x, y)

**35.** Express the negations of each of these statements using quantifiers.
a) Every student in this class knows Java.
b) There is a student in this class who has not seen a computer.
c) There is a student in this class who has taken every math course offered.
d) Every student in this class has taken at least one computer science course.

---

# K6 推理规则（**必考大题**）

## 核心概念

**8 个基本推理规则**（必背，能默写）：

| 名称 | 规则 | 缩写 |
|---|---|---|
| **Modus Ponens（假言推理）** | p, p→q ⊢ q | MP |
| **Modus Tollens（拒取式）** | ¬q, p→q ⊢ ¬p | MT |
| **Hypothetical Syllogism（假言三段论）** | p→q, q→r ⊢ p→r | HS |
| **Disjunctive Syllogism（析取三段论）** | p∨q, ¬p ⊢ q | DS |
| **Addition（附加）** | p ⊢ p∨q | Add |
| **Simplification（化简）** | p∧q ⊢ p | Simp |
| **Conjunction（合取）** | p, q ⊢ p∧q | Con |
| **Resolution（消解）** | p∨q, ¬p∨r ⊢ q∨r | Res |

**谓词逻辑规则**：

| 名称 | 规则 | 注意 |
|---|---|---|
| **Universal Instantiation（全称例化）** | ∀x P(x) ⊢ P(c) | c 是任意元素 |
| **Universal Generalization（全称推广）** | P(c) ⊢ ∀x P(x) | **c 必须是任意元素**，不能是具体某个 |
| **Existential Instantiation（存在例化）** | ∃x P(x) ⊢ P(c) | c 是使 P 成立的那个**特定**元素，不能再用于 UG |
| **Existential Generalization（存在推广）** | P(c) ⊢ ∃x P(x) | c 是某个具体元素 |

> ⚠️ **关键陷阱**：
> - UI/EG 可直接用
> - **EI 后不能用 UG**（c 不再是"任意"）
> - UG 前提必须是关于"任意 c"（不能在 ∀ 内部用某个特定 c）

**论证有效性**：前提全部为真时结论必真。

## 反复考的题型

### 题型 1：识别推理规则（最常考）
看前提的形式 → 对照 8 条规则 → 写出规则名。

### 题型 2：用规则证明结论（**必考大题**）

**标准步骤**：
1. 列出所有前提（每行一条）
2. 找到能推出下一步的规则
3. 每行右边标注引用的前提编号 + 规则名
4. 一直推到目标

**模板**：

```
1. p→q            Premise
2. ¬q             Premise
3. ¬p             MT (1, 2)
4. ∴ ...
```

### 题型 3：论证有效性判断（必考）

方法：
1. 用真值表：所有前提为 T 时，结论必为 T → 有效
2. 反证：找一组赋值使所有前提 T 但结论 F → 无效

### 题型 4：谓词逻辑证明（涉及 EI/UG 时易错）

例：证明"Some A are B" from "All A are B"：
1. ∃x A(x)           Premise
2. A(c)              EI (1)        ← c 是某个特定元素
3. ∀x (A(x) → B(x))  Premise
4. A(c) → B(c)       UI (3)
5. B(c)              MP (2, 4)
6. ∃x B(x)           EG (5)

⚠️ 第 2 步 EI 之后**不能再**用 UG，因为 c 不再任意。

## 配套作业

**Section 1.6**

**1.** What rule of inference is used in each of these arguments?
a) Alice is a mathematics major. Therefore, Alice is either a mathematics major or a computer science major.
b) Jerry is a mathematics major and a computer science major. Therefore, Jerry is a mathematics major.
c) If it is rainy, then the pool will be closed. It is rainy. Therefore, the pool will be closed.
d) If it snows today, the university will close. The university is not closed today. Therefore, it did not snow today.
e) If I go swimming, then I will stay in the sun too long. If I stay in the sun too long, then I will get sunburned. If I get sunburned, then I will be in pain tomorrow. Therefore, if I go swimming, I will be in pain tomorrow.

**5.** What are the rules of inference used in the famous Lewis Carroll argument?
"No ducks waltz. No officers ever decline to waltz. All my poultry are ducks. Therefore, none of my poultry are officers."

**10.** For each of these sets of premises, what relevant conclusion or conclusions can be drawn? Explain the rules of inference used to obtain each conclusion.
a) "If I eat spicy foods, then I have strange dreams." "I have strange dreams." "If I don't sleep well, then I don't have strange dreams."
b) "Either the congressman is corrupt or he is a fool." "The congressman is not a fool."
c) "If I go to the movies, I don't finish my homework." "I don't go to the movies." "If I don't finish my homework, I won't do well on the exam."

**15.** For each of these sets of premises, determine whether the argument is valid.
a) If it snows today, I will ski tomorrow. I will not ski tomorrow if there is less than two feet of snow. Therefore, if it snows today, then there is at least two feet of snow.
b) If I work out, I feel good. If I feel good, I play well. I don't play well. Therefore, I didn't work out.

**20.** Show that the premises "If it does not rain or if it is not foggy, then the sailing race will be held and the lifesaving demonstration will go on" and "The lifesaving demonstration will not go on" imply the conclusion "It will rain or it will be foggy."

**25.** Use rules of inference to show that if premises "All lions are fierce," "Some lions do not drink coffee," and "Some fierce creatures that do not drink coffee are man-eating" are true, then the conclusion "Some man-eating creatures are not coffee-drinking lions" is true.

**28.** For each of the following arguments, determine whether the argument is valid. If valid, name the rule of inference that validates it.
a) Kangaroos are mammals. I am studying mammals. Therefore, I am studying kangaroos.
b) It is either hotter than 100 degrees today or it is less than 100 degrees today. It is not hotter than 100 degrees today. Therefore, it is less than 100 degrees today.

**32.** Show that the premises (a) "Everyone who reads serves the people better," (b) "Everyone who serves the people better deserves to be praised," (c) "Everyone who deserves to be praised will be promoted," and (d) "Harry will not be promoted" imply that Harry did not read.

---

## 复习清单

- [ ] 能区分 "only if" / "if" / "unless" / "whenever" 的条件句方向
- [ ] contrapositive ≡ 原条件（converse / inverse 不等价）
- [ ] De Morgan 双公式倒背如流
- [ ] 条件等价 p→q ≡ ¬p∨q ≡ ¬q→¬p
- [ ] 量词否定：∀↔∃
- [ ] ∀ 谓词用 →，∃ 谓词用 ∧
- [ ] ∀x∃y ≠ ∃x∀y（量词次序）
- [ ] 8 条推理规则能识别 + 写出
- [ ] EI 后**不能**用 UG
- [ ] 谓词证明每步右边标注：引用的行号 + 规则名