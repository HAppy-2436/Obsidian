# 第一章 逻辑与证明（知识点精讲版）

> **考试分值**：4 题 / 30 分（与 Ch2、Ch9 合并）
> **考纲范围**：1.1, 1.3, 1.4, 1.5, 1.6（**不考** 1.2 应用、1.7/1.8 证明方法）
> **必考大题**：**1.6 推理规则**（每年必出，需熟练到能闭卷写证明）
> **学习方式**：通读每个知识点的"深入讲解"部分，看懂后再做 2-3 道典型例题，最后用配套作业自测

---

## 知识点地图

| 知识点 | 出处 | 频次 | 难度 | 重要性 |
|---|---|---|---|---|
| K1 命题与联结词 | 1.1 | ★★★ | 易 | 基础 |
| K2 真值表 + 条件句变形 | 1.1 | ★★★ | 易 | 基础 |
| K3 命题等价 + De Morgan | 1.3 | ★★★ | 中 | 核心 |
| K4 谓词与量词 | 1.4 | ★★★ | 中 | 核心 |
| K5 嵌套量词 | 1.5 | ★★☆ | 中 | 重点 |
| K6 **推理规则** | 1.6 | ★★★ | 难 | **必考大题** |

---

# K1 命题与联结词

## 核心概念

- **命题（proposition）**：有**唯一真值**（T 或 F）的陈述句
- **5 个联结词**：¬（非）、∧（与）、∨（或）、→（蕴含）、↔（当且仅当）
- **优先级**：¬ > ∧ > ∨ > → > ↔

## 深入讲解

### 什么是命题、什么不是

**是命题的**：陈述句 + 真值确定。
- "2 + 3 = 5" → 命题（T）
- "波士顿是麻州首府" → 命题（T）

**不是命题的**：
- **疑问句**："现在几点？"（没有真值）
- **命令句**："请关门。"（不是判断）
- **悖论**："这句话是假的"（自指，无一致真值）
- **含变量的等式**："x + 2 = 11"（不是命题，是谓词——x 不确定）
- **依赖时间的**："今天下雨"（真值随时间变，但考试一般不计较）

### 5 个联结词的本质理解

**¬p**：取反，一对一映射
- 唯一需要记的是"否定量词时也用"（后面 K4）

**p ∧ q**：合取，**两者都真才真**
- 记忆：AND 是"狭窄"门，两边都得过

**p ∨ q**：析取，**至少一个真就真**（inclusive or）
- 日常"或"在英语中常是 exclusive（异或），但**逻辑上是 inclusive**
- 异或 ⊕：恰好一个真才真

**p → q**：**最反直觉的一个**
- 真值表：

| p | q | p→q |
|---|---|------|
| T | T | **T** |
| T | F | **F** |
| F | T | **T** |
| F | F | **T** |

- **关键**：p 假时 p→q 永远为真（"vacuous truth"）
- 例子："如果雪是黑的，那么我是皇帝"——雪不是黑的，所以这整句**是真的**（虽然结论荒谬）
- 考试**最爱考这个**：给你一个假前件，问 p→q 真不真——永远真

**p ↔ q**：双条件，**真值相同就真**
- "相同"包括两者都假！1+1=3 iff 猴会飞——都假，所以**真**

### 命题联结词的英文表达（必背）

**核心规律**：
- "p **only if** q" → p→q（q 是 p 的必要条件）
- "p **if** q" → q→p
- "p **is sufficient for** q" → p→q
- "q **is necessary for** p" → p→q
- "p **whenever** q" → q→p
- "p **unless** q" → ¬q→p（除非 q，即"如果不 q 那么 p"）
- "p **if and only if** q"（p iff q）→ p↔q

**死规律**：
- "only if" 在后 → → 方向是指**向前件**（p→q）
- "if" 在前 → → 方向是指**向后件**（q→p）

### 自然语言 ↔ 符号化的实战技巧

**技巧 1：先找主语谓语，再选联结词**
- "Linda 比 Sanjay 年轻" → L < S（不是命题，先跳过）

**技巧 2：用 → 处理"如果"，用 ∧ 处理"且"**
- "It is hot **and** humid" → p ∧ q
- "If **hot**, **then** humid" → p → q

**技巧 3："but" = "and"**
- "hot but not humid" → p ∧ ¬q

**技巧 4："or (or both)" 明确强调 inclusive**
- 普通 "or" 一般按 inclusive 处理，除非题目明确"but not both"

## 典型例题

### 例 1.1：自然语言 ↔ 符号（高频）

**题**：Let p = "I bought a lottery ticket this week." q = "I won the million dollar jackpot." Express:
- a) ¬p → ¬q
- b) ¬p ∧ ¬q
- c) ¬p ∨ (p ∧ q)

**解**：
- a) "If I didn't buy a lottery ticket this week, then I didn't win the million dollar jackpot."
- b) "I didn't buy a lottery ticket this week, and I didn't win the million dollar jackpot."
- c) "I didn't buy a lottery ticket this week, or (I bought a lottery ticket this week and I won the million dollar jackpot)."
  - 注意：c 比较绕，关键是按符号逐字翻译

### 例 1.2：双条件真值（反直觉点）

**题**：Determine if true or false: "1 + 1 = 3 if and only if monkeys can fly."

**解**：1+1=3 是 F，monkeys can fly 是 F。两边相同 → **真**。

> ⚠️ **易错**：很多学生看到"假命题"就选假。p↔q 在两边都假时为真。

### 例 1.3：复杂英文转符号（必考）

**题**：Let p = "It is below freezing.", q = "It is snowing." Write: "Either it is below freezing or it is snowing, but it is not snowing if it is below freezing."

**解**：
- "Either A or B" → A ∨ B = (p ∨ q)
- "but" = "and"
- "it is not snowing if it is below freezing" → p → ¬q
- 整体：(p ∨ q) ∧ (p → ¬q)

## 易错点总结

- ❌ "only if q" 写成 q→p（应该是 p→q）
- ❌ p↔q 看到假命题就判假（要查真值是否相同）
- ❌ p→q 中 p 假时以为假（p 假时 p→q 永远真）
- ❌ 复合命题漏看否定（"not A and not B" ≠ "not (A and B)"，前者 ¬A ∧ ¬B，后者 ¬(A∧B) = ¬A ∨ ¬B）

## 配套作业（精选）

- 1.1.3, 1.1.5（求否定）
- 1.1.10, 1.1.13（符号化 / 自然语言化）
- 1.1.18, 1.1.19, 1.1.20（双条件 / 条件句真值）
- 1.1.21, 1.1.22（inclusive vs exclusive or）
- 1.1.24, 1.1.25, 1.1.26（写 "if p, then q"）
- 1.1.27, 1.1.28（写 "p iff q"）

---

# K2 真值表 + 条件句变形

## 核心概念

- **真值表行数**：n 个不同命题变量 → **2ⁿ 行**
- **条件句四种变形**（设原 p→q）：

| 名称 | 形式 | 与原命题关系 |
|---|---|---|
| converse（逆） | q→p | **不等价** |
| inverse（否） | ¬p→¬q | **不等价**（但等价于 converse）|
| contrapositive（逆否） | ¬q→¬p | **等价**（必背）|

## 深入讲解

### 为什么 contrapositive 等价

看真值表：

| p | q | p→q | ¬q | ¬p | ¬q→¬p |
|---|---|-----|----|----|-------|
| T | T | T   | F  | F  | T     |
| T | F | F   | T  | F  | F     |
| F | T | T   | F  | T  | T     |
| F | F | T   | T  | T  | T     |

p→q 列和 ¬q→¬p 列完全一致 → 等价。

**为什么 converse / inverse 不等价**：
- converse q→p：原 p→q 假时（如 T/F），converse 可以真（F/T 是真）
- 例子："如果下雨，地湿" → converse "如果地湿，下雨"（地湿不一定是下雨）

**考试陷阱**：
- 题目问"下列哪些等价"——只要看 contrapositive
- 题目让"用逆否证明"——就是证明 contrapositive

### 真值表行数计算

**关键**：数**不同变量**的个数，不是联结词个数。

| 命题 | 不同变量 | 行数 |
|---|---|---|
| p → ¬p | {p} | 2¹ = 2 |
| (p∨¬r)∧(q∨¬s) | {p,q,r,s} | 2⁴ = 16 |
| q∨p∨¬s∨¬r∨¬t∨u | {p,q,r,s,t,u} | 2⁶ = 64 |
| (p∧r∧t)↔(q∧t) | {p,q,r,t} | 2⁴ = 16 |

### 永真 / 永假 / 偶然

- **Tautology（永真）**：所有行都为 T
- **Contradiction（永假）**：所有行都为 F
- **Contingency（偶然）**：有时真有时假

**判定方法**：
- 永真：所有行 T
- 永假：所有行 F
- 否则：偶然

### 用真值表判定条件句（反直觉训练）

**实战**：判断 "If 1+1=3, then 2+2=4" 真值
- 前件 1+1=3：F
- 后件 2+2=4：T
- p=F, q=T → p→q = **真**

> 训练：每看到 p→q，**先判前件真值**——若 F，无论后件是什么，p→q 都真。

## 典型例题

### 例 2.1：contrapositive 求法

**题**：State converse, contrapositive, inverse of "If it snows today, I will ski tomorrow."

**解**（设 p=下雪, q=明天滑雪）：
- 原 p→q: If it snows today, I will ski tomorrow.
- converse q→p: If I ski tomorrow, then it snows today.
- inverse ¬p→¬q: If it doesn't snow today, then I won't ski tomorrow.
- contrapositive ¬q→¬p: If I don't ski tomorrow, then it didn't snow today.

> **注意**：contrapositive 是唯一等价的。

### 例 2.2：永真判定（真值表法）

**题**：Show (p∧q)→p is a tautology by truth table.

**解**：

| p | q | p∧q | (p∧q)→p |
|---|---|-----|---------|
| T | T | T   | T       |
| T | F | F   | T       |
| F | T | F   | T       |
| F | F | F   | T       |

全 T → **永真** ✓

> 速记：第二行 (T,F)：前件 F，蕴含 T
> 第三、四行：前件 F，蕴含 T

### 例 2.3：真值表行数

**题**：How many rows in truth table of (p∧r∧t) ↔ (q∧t)?

**解**：不同变量 {p, q, r, t} = 4 个 → 2⁴ = **16** 行

> t 出现两次只算 1 个变量。

## 易错点总结

- ❌ 算行数时数联结词或重复变量
- ❌ 以为 converse 等价于原命题
- ❌ 永真证明时漏行
- ❌ p→q 中前件假时判定为假

## 配套作业（精选）

- 1.1.29, 1.1.30（条件句变形）
- 1.1.31, 1.1.32（真值表行数）
- 1.1.33, 1.1.34, 1.1.35, 1.1.36, 1.1.37（构造真值表）
- 1.1.40, 1.1.41（多变量真值表）

---

# K3 命题等价 + De Morgan（核心）

## 核心概念

- **等价定义**：p ≡ q 当且仅当 p ↔ q 是永真
- **De Morgan 定律**：

$$\neg(p \wedge q) \equiv \neg p \vee \neg q$$
$$\neg(p \vee q) \equiv \neg p \wedge \neg q$$

- **条件等价**：

$$p \to q \equiv \neg p \vee q \equiv \neg q \to \neg p$$
$$\neg(p \to q) \equiv p \wedge \neg q$$

## 深入讲解

### 等价证明的三种方法

**方法 1：真值表法**
- 列出所有 2ⁿ 种赋值
- 比较两个命题的列是否完全一致
- 一致即等价
- **缺点**：变量多时（如 n≥4）真值表行数爆炸

**方法 2：等价律链式证明（最常考）**
- 从一边开始
- 每步标"≡ ...（等价律名）"
- 逐步变形直到另一边

**方法 3：互推法（用于条件句等价）**
- 证 p→q ⇒ (其他形式)
- 证 (其他形式) ⇒ p→q

### De Morgan 定律的深入理解

**核心规则**：否定要**穿透**联结词，并**翻转**联结词
- ¬(P ∧ Q) = ¬P ∨ ¬Q（与变或）
- ¬(P ∨ Q) = ¬P ∧ ¬Q（或变与）

**推广到 n 元**：
- ¬(P₁ ∧ P₂ ∧ ... ∧ Pₙ) = ¬P₁ ∨ ¬P₂ ∨ ... ∨ ¬Pₙ
- ¬(P₁ ∨ P₂ ∨ ... ∨ Pₙ) = ¬P₁ ∧ ¬P₂ ∧ ... ∧ ¬Pₙ

**实战例**：¬(p→q) 的 De Morgan 化简
- p→q ≡ ¬p∨q
- ¬(¬p∨q) ≡ ¬(¬p) ∧ ¬q ≡ p ∧ ¬q（用 De Morgan + 双重否定）

**死规律**：De Morgan 与 集合版本完全平行，只是把 ∧ 换 ∩、∨ 换 ∪。

### 核心等价律（表 6，11 条）

| 类别 | 等价律 |
|---|---|
| Identity | p∧T≡p, p∨F≡p |
| Domination | p∨T≡T, p∧F≡F |
| Idempotent | p∨p≡p, p∧p≡p |
| Double negation | ¬(¬p)≡p |
| Commutative | p∨q≡q∨p, p∧q≡q∧p |
| Associative | (p∨q)∨r≡p∨(q∨r) |
| Distributive | p∨(q∧r)≡(p∨q)∧(p∨r) |
| De Morgan | 见上 |
| Absorption | p∨(p∧q)≡p, p∧(p∨q)≡p |
| Negation | p∨¬p≡T, p∧¬p≡F |

> **背法**：Identity、Domination、Idempotent 容易混，要背口诀：
> - Identity: p 跟自己（∧T 或 ∨F）
> - Domination: p 被吞掉（∨T 直接 T，∧F 直接 F）
> - Idempotent: p 跟 p 重复

### 条件句相关等价（表 7，必背）

$$p \to q \equiv \neg p \vee q$$
$$p \to q \equiv \neg q \to \neg p \text{ (contrapositive)}$$
$$p \vee q \equiv \neg p \to q$$
$$p \wedge q \equiv \neg(p \to \neg q)$$
$$\neg(p \to q) \equiv p \wedge \neg q$$
$$(p \to q) \wedge (p \to r) \equiv p \to (q \wedge r)$$
$$(p \to r) \wedge (q \to r) \equiv (p \vee q) \to r$$
$$(p \to q) \vee (p \to r) \equiv p \to (q \vee r)$$
$$(p \to r) \vee (q \to r) \equiv (p \wedge q) \to r$$

> **速记**：分配律的"条件版"——
> - (p→q) ∧ (p→r) → p 在前，要 ∧ 一起 → (q∧r)
> - (p→r) ∧ (q→r) → r 在后，∧ → (p∨q)→r

### 双条件相关等价（表 8）

$$p \leftrightarrow q \equiv (p \to q) \wedge (q \to p)$$
$$p \leftrightarrow q \equiv \neg p \leftrightarrow \neg q$$
$$p \leftrightarrow q \equiv (p \wedge q) \vee (\neg p \wedge \neg q)$$
$$\neg(p \leftrightarrow q) \equiv p \leftrightarrow \neg q$$

### 对偶（Dual）

**定义**：把 ∨ ↔ ∧, T ↔ F 互换得到的命题。

**性质**：
- 对偶的对偶 = 自身
- 两个等价命题的对偶也等价
- Table 6 的等价律（除双重否定外）都是"对偶配对"

**实战步骤**（当原命题含 → 时）：
1. 先把 → 换成 ¬p∨q
2. 整个替换 ∨↔∧, T↔F
3. 如需要再转回 → 形式

**例**：求 (p∨q)→r 的对偶
1. → 替换：¬(p∨q) ∨ r
2. 对偶：¬(p∧q) ∧ r
3. 还原为 →：(p∧q)→r ← **注意要再换一次**

### 永真证明的非真值表法

**核心思想**：条件句假 ⟺ 前件真且后件假。所以要证 p→q 是永真，等价于证明"无法同时 p 真和 q 假"。

**两种非真值表法**：

**方法 A**：设结论假，推出矛盾
- 要证 (p∧q)→p 永真
- 设结论假：p∧q 真 且 p 假
- 但 p∧q 真要求 p 真 → 矛盾 ✓

**方法 B**：等价律链式证明 ≡ T
- 要证 p→(p∨q) 永真
- p→(p∨q) ≡ ¬p∨(p∨q) （条件等价）
- ≡ (¬p∨p)∨q （结合律 + 交换律）
- ≡ T∨q （否定律）
- ≡ T （支配律）
- ✓ 永真

## 典型例题

### 例 3.1：De Morgan 求否定

**题**：Negate "Jan is rich and happy."

**解**：
- P = "Jan is rich", Q = "Jan is happy"
- 原命题 = P ∧ Q
- 否定 = ¬(P ∧ Q) ≡ ¬P ∨ ¬Q
- = "Jan is not rich, or Jan is not happy."

> ⚠️ 常见错：写成 "Jan is not rich, and Jan is not happy."（错用 ∧，应该用 ∨）

### 例 3.2：等价律证明（必考大题套路）

**题**：Show ¬(p ∨ (¬p ∧ q)) ≡ ¬p ∧ ¬q

**解**（链式证明）：

```
¬(p ∨ (¬p ∧ q))
≡ ¬p ∧ ¬(¬p ∧ q)             (De Morgan 第二律)
≡ ¬p ∧ (¬(¬p) ∨ ¬q)          (De Morgan 第一律)
≡ ¬p ∧ (p ∨ ¬q)              (双重否定)
≡ (¬p ∧ p) ∨ (¬p ∧ ¬q)       (分配律)
≡ F ∨ (¬p ∧ ¬q)              (否定律 p∧¬p=F)
≡ (¬p ∧ ¬q) ∨ F              (交换律)
≡ ¬p ∧ ¬q                    (Identity)
```

✓ 证毕

> **实战模板**：每行写"≡ ...（等价律名）"，从左到右。

### 例 3.3：永真证明（不用真值表）

**题**：Show (p → q) ∧ (q → r) → (p → r) is a tautology.

**解**（设结论假，导出矛盾）：

```
(p → q) ∧ (q → r) → (p → r) 假
⟺ (p → q) ∧ (q → r) 真 且 (p → r) 假
⟺ p → q 真, q → r 真, p → r 假

p → r 假 ⟺ p 真 且 r 假

但 p 真 且 q → r 真 ⟺ p 真 且 (q 假 或 r 真)
∵ r 假 ⟹ q 假

但 p 真 且 p → q 真 ⟹ q 真
∴ q 真 且 q 假 → 矛盾 ✓
```

> **实战模板**：设结论假 → 推到矛盾。

### 例 3.4：永真证明（等价律链）

**题**：Show [p ∧ (p → q)] → q is a tautology.

**解**：

```
[p ∧ (p → q)] → q
≡ ¬[p ∧ (p → q)] ∨ q         (条件等价)
≡ ¬p ∨ ¬(p → q) ∨ q          (De Morgan)
≡ ¬p ∨ (p ∧ ¬q) ∨ q          (条件否定等价)
≡ ¬p ∨ (p ∧ ¬q) ∨ q          (重排)
≡ ¬p ∨ [p ∧ (¬q ∨ q)]        (... 复杂路径)
```

用更聪明的等价律：

```
[p ∧ (p → q)] → q
≡ [p ∧ (¬p ∨ q)] → q         (条件等价)
≡ [(p ∧ ¬p) ∨ (p ∧ q)] → q   (分配律)
≡ [F ∨ (p ∧ q)] → q          (否定律)
≡ (p ∧ q) → q                (Identity)
≡ ¬(p ∧ q) ∨ q               (条件等价)
≡ (¬p ∨ ¬q) ∨ q              (De Morgan)
≡ ¬p ∨ (¬q ∨ q)              (结合)
≡ ¬p ∨ T                     (否定律)
≡ T                          (支配)
```

✓ 永真

### 例 3.5：求对偶

**题**：Find the dual of (p∨q) → r

**解**：
1. 消 →：¬(p∨q) ∨ r
2. 对偶（∨↔∧, T↔F）：¬(p∧q) ∧ r
3. 如要转回 →：(p∧q) → r

## 易错点总结

- ❌ De Morgan 翻转联结词时漏否定
- ❌ 等价证明跳步骤
- ❌ 永真证明用真值表时漏行
- ❌ 条件句 ¬(p→q) 写成 ¬p→¬q（应该是 p∧¬q）
- ❌ 对偶时漏 T/F 互换

## 配套作业（精选）

- 1.3.5, 1.3.7（De Morgan 否定）
- 1.3.9（条件等价）
- 1.3.11, 1.3.12（永真证明）
- 1.3.13, 1.3.14（永真证明 - 不用真值表）
- 1.3.15, 1.3.16（永真证明 - 链式）
- 1.3.20, 1.3.22, 1.3.26, 1.3.28（等价证明）
- 1.3.33（求对偶）

---

# K4 谓词与量词

## 核心概念

- **谓词 P(x)**：含变量 x 的命题函数。P(5) 才是命题
- **全称量词 ∀x P(x)**："对所有 x，P(x) 成立"
- **存在量词 ∃x P(x)**："存在 x 使 P(x) 成立"
- **量词否定**（必背）：

$$\neg \forall x \, P(x) \equiv \exists x \, \neg P(x)$$
$$\neg \exists x \, P(x) \equiv \forall x \, \neg P(x)$$

## 深入讲解

### 量词的逻辑本质

**∀ 等价于合取**：
- ∀x P(x) ≡ P(x₁) ∧ P(x₂) ∧ ... ∧ P(xₙ)
- 域是有限集时
- 域为空时（空集上的全称）→ **永真**

**∃ 等价于析取**：
- ∃x P(x) ≡ P(x₁) ∨ P(x₂) ∨ ... ∨ P(xₙ)
- 域是有限集时
- 域为空时（空集上的存在）→ **永假**

### 自然语言 ↔ 量词符号化（核心难点）

**核心规则**（死记）：

| 自然语言 | 符号化 |
|---|---|
| All A are B | ∀x (A(x) → B(x)) |
| Some A are B | ∃x (A(x) ∧ B(x)) |
| No A are B | ∀x (A(x) → ¬B(x)) |
| Some A are not B | ∃x (A(x) ∧ ¬B(x)) |
| Every A is B | ∀x (A(x) → B(x)) |
| There is an A such that B | ∃x (A(x) ∧ B(x)) |
| Only A are B | ∀x (B(x) → A(x)) |
| Every A has property B | ∀x (A(x) → B(x)) |
| At least one A is B | ∃x (A(x) ∧ B(x)) |

> ⚠️ **死规律**：
> - 全称（all/every/no/only）：**用 →**
> - 存在（some/there is/at least）：**用 ∧**
>
> 为什么？考虑 "All A are B"：
> - 对 x ∉ A：x 不在范围内，A(x) 为假
> - "A(x)→B(x)"：当 A(x) 假，蕴含自动真（vacuous truth）
> - 所以全称用 → 是合理的

**反例训练**：为什么 "All A are B" 错写为 ∀x (A(x) ∧ B(x)) 是错的？
- 若 x ∉ A：A(x) 为假，A(x)∧B(x) 为假
- 全称要求所有 x 命题为真，但 x ∉ A 时假 → 矛盾
- 例："All dogs are mammals" 错写成 ∀x(D(x) ∧ M(x)) → 对 x = cat，D(x)∧M(x) = F∧T = F → 命题假
- 但 ∀x(D(x) → M(x)) 对 x = cat：D(x)=F → F→M(x) = T → 命题真 ✓

### 量词否定：4 步法

**步骤**（针对 ∀x∃y∀z P(x,y,z) 这种多量词）：
1. 从最外层开始否定
2. 量词翻转（∀↔∃）
3. 谓词取反
4. 重复直到没有量词

**实战**：¬(∀x ∃y P(x, y))
1. ¬∀ → ∃¬ : ∃x ¬∃y P(x, y)
2. ¬∃ → ∀¬ : ∃x ∀y ¬P(x, y)
- 完成

### 求量词真值（针对有限域）

**∀x P(x) 真**：所有元素都满足 P
**∀x P(x) 假**：至少一个元素不满足（找反例）
**∃x P(x) 真**：至少一个元素满足
**∃x P(x) 假**：所有元素都不满足

**针对无限域**：
- ∀x P(x)：要证明对所有 x 成立（一般证）
- ∀x P(x) 假：找**一个反例**
- ∃x P(x)：找**一个真例**
- ∃x P(x) 假：证明对所有 x 都不成立

### 量词与联结词的优先级

**优先级**：∀ 和 ∃ **高于**所有联结词

所以 ∀x P(x) ∨ Q 中，∀x P(x) 是一个整体。

## 典型例题

### 例 4.1：符号化（最常考）

**题**：Let L(x, y) = "x loves y". Symbolize:
a) Everybody loves Jerry.
b) Everybody loves somebody.
c) There is somebody whom everybody loves.
d) Nobody loves everybody.

**解**（设 J = Jerry）：
- a) ∀x L(x, J)
- b) ∀x ∃y L(x, y)
- c) ∃y ∀x L(x, y)
- d) ∀x ¬L(x, every-body)... 让我换种说法：
  - "Nobody loves everybody" = "For every person x, x does not love everybody"
  - = ∀x ∀y ¬L(x, y)
  - 或 ¬∃x ∀y L(x, y)
  - 或 ∀x ∃y ¬L(x, y)（每人都有不爱的人）

### 例 4.2：量词次序的实质差异

**题**：Truth value of these on reals:
- A: ∀x ∃y (x + y = 0)
- B: ∃y ∀x (x + y = 0)

**解**：
- A：对每个 x，存在 y = -x 使 x + y = 0 → **真**
- B：存在单一 y，使所有 x 满足 x + y = 0。但不同 x 需要不同 y（如 x=1 要 y=-1，x=2 要 y=-2）→ 单一 y 不可能 → **假**

> **核心**：∀x∃y 中 y 可随 x 变；∃y∀x 中 y 固定，要应付所有 x。

### 例 4.3：量词否定

**题**：Negate ∀x ∃y (x + y = 0)

**解**：
- ¬∀x ∃y(x+y=0)
- ≡ ∃x ∀y ¬(x+y=0)
- ≡ ∃x ∀y (x+y ≠ 0)

### 例 4.4：求真值（整数域）

**题**：∀n(n² ≥ n) on integers.

**解**：检查每个整数
- n=0: 0² = 0 ≥ 0 ✓
- n=1: 1 ≥ 1 ✓
- n=2: 4 ≥ 2 ✓
- n=-1: 1 ≥ -1 ✓
- **证明**：n² - n = n(n-1)，整数 n(n-1) 永远 ≥ 0（除了... 实际 n=0,1 时为 0，其他非负）
- **真** ✓

## 易错点总结

- ❌ "All A are B" 写成 ∀x(A∧B)，错！应该是 ∀x(A→B)
- ❌ 量词次序颠倒（∀∃ vs ∃∀）
- ❌ 量词否定时漏翻量词或漏否谓词
- ❌ 求 ∀ 真值时举例（举例只能证假）
- ❌ 求 ∃ 真值时试图证所有（证所有只能证假）

## 配套作业（精选）

- 1.4.5, 1.4.10（量词符号化）
- 1.4.15（量词求真值）
- 1.4.20, 1.4.40（量词翻译）
- 1.4.30, 1.4.35（量词否定）
- 1.4.48（谓词逻辑等价证明）

---

# K5 嵌套量词

## 核心概念

**量词次序的不可交换性**：
- ∀x∀y P ≡ ∀y∀x P（**同量词可换**）
- ∃x∃y P ≡ ∃y∃x P
- **∀x∃y P ≠ ∃x∀y P**（**不同量词不可换**）

**多量词否定**：从左到右逐个 ∀↔∃，谓词取反。

## 深入讲解

### ∀x∃y vs ∃x∀y 的本质区别

**∀x∃y P(x, y)**：
- "对每个 x，存在 y 使 P 成立"
- y **可以随 x 变**
- 类比：每个学生都有某个朋友（不同学生可以有不同朋友）

**∃x∀y P(x, y)**：
- "存在一个 x，使 P 对所有 y 成立"
- y **固定为全体**，x 是固定的
- 类比：存在一个所有人都喜欢的朋友（同一个人）

**实战例子**：
- ∀x∃y(x = y²)：每个 x 都是某个 y 的平方。**假**（x = -1 不是平方）
- ∃y∀x(x = y²)：存在一个 y 使所有 x 是 y²。**假**（不可能所有 x 都等于同一个 y²）
- ∀x∃y(x ≤ y)：每个 x 都有 ≥ 它的 y。**真**（y = x）
- ∃y∀x(x ≤ y)：存在最大 y。**假**（实数无最大）

### 嵌套量词翻译为英文

**技巧**：从内到外，逐层翻译

**例**：∀x ∃y (x < y²)
- 内层 ∃y (x < y²)：x 小于某个 y²
- 外层 ∀x：对每个 x，x 小于某个 y²
- 英文：For every real number x, there is a real number y such that x < y².

### 多量词否定（递归）

**规则**：每个量词都要翻转 + 谓词取反

**例**：∀x ∃y ∀z P(x, y, z)
- ¬∀x ∃y ∀z P
- ≡ ∃x ¬∃y ∀z P
- ≡ ∃x ∀y ¬∀z P
- ≡ ∃x ∀y ∃z ¬P

> **速记**：每个量词都翻，每翻一个把谓词取反一次。

## 典型例题

### 例 5.1：量词次序真值（必考）

**题**：Real domain, true or false:
- ∀x ∃y (x² = y)
- ∀x ∃y (x = y²)
- ∃x ∀y (xy = 0)
- ∃x ∀y (xy ≠ 0)

**解**：
- ∀x∃y(x²=y)：y = x² 永远存在 → **真**
- ∀x∃y(x=y²)：x < 0 时无实数 y → **假**
- ∃x∀y(xy=0)：x=0 时 xy=0 对所有 y → **真**
- ∃x∀y(xy≠0)：含 y=0 时 xy=0 → **假**（任何 x，y=0 时 xy=0）

### 例 5.2：嵌套量词否定

**题**：Negate ∀x ∀y ∃z (xz + yz = 0)

**解**：
- ¬∀x∀y∃z(xz+yz=0)
- ≡ ∃x¬∀y∃z(xz+yz=0)
- ≡ ∃x∃y¬∃z(xz+yz=0)
- ≡ ∃x∃y∀z¬(xz+yz=0)
- ≡ ∃x∃y∀z(xz+yz ≠ 0)

### 例 5.3：翻译成英文

**题**：∀x ∃y (x² < y) 翻译成英文。

**解**：For every real number x, there is a real number y such that x² < y.

> 即："每个实数 x，都存在实数 y，使 x² < y"（每个平方数都小于某个数，显然真）。

## 易错点总结

- ❌ 把 ∀x∃y 当作 ∃x∀y
- ❌ 多量词否定时漏翻某个量词
- ❌ 翻译成英文时丢失量词

## 配套作业（精选）

- 1.5.5, 1.5.11, 1.5.15（多种翻译）
- 1.5.20（量词次序真值 - **重点**）
- 1.5.25（翻译成英文）
- 1.5.30, 1.5.35（嵌套量词否定 - **重点**）
- 1.5.42（应用）

---

# K6 推理规则（**必考大题**）

## 核心概念

**8 个命题逻辑规则**（必背）：

| 名称 | 规则 | 缩写 |
|---|---|---|
| Modus Ponens | p, p→q ⊢ q | MP |
| Modus Tollens | ¬q, p→q ⊢ ¬p | MT |
| Hypothetical Syllogism | p→q, q→r ⊢ p→r | HS |
| Disjunctive Syllogism | p∨q, ¬p ⊢ q | DS |
| Addition | p ⊢ p∨q | Add |
| Simplification | p∧q ⊢ p | Simp |
| Conjunction | p, q ⊢ p∧q | Con |
| Resolution | p∨q, ¬p∨r ⊢ q∨r | Res |

**4 个谓词规则**：

| 名称 | 规则 | 注意 |
|---|---|---|
| Universal Instantiation | ∀x P(x) ⊢ P(c) | c 是任意元素 |
| Universal Generalization | P(c) ⊢ ∀x P(x) | **c 必须任意** |
| Existential Instantiation | ∃x P(x) ⊢ P(c) | c 是使 P 成立的那个 |
| Existential Generalization | P(c) ⊢ ∃x P(x) | c 是某个具体元素 |

## 深入讲解

### 8 条规则的"长相"识别

看到前提时，对照规则模板：

```
MP:    [p→q]  + [p]      → 结论 [q]
MT:    [p→q]  + [¬q]     → 结论 [¬p]
HS:    [p→q]  + [q→r]    → 结论 [p→r]
DS:    [p∨q]  + [¬p]     → 结论 [q]   (或 [¬q] + [p])
Add:   [p]                → 结论 [p∨q]
Simp:  [p∧q]              → 结论 [p]   (或 [q])
Con:   [p] + [q]          → 结论 [p∧q]
Res:   [p∨q] + [¬p∨r]    → 结论 [q∨r]
```

### 推理题的标准解题流程

**第 1 步：符号化**
- 把所有自然语言翻译成 p, q, r 形式的命题
- 写明每个符号的含义

**第 2 步：列出前提**
- 每条前提写一行
- 标号 1, 2, 3, ...

**第 3 步：找推导路径**
- 看结论形式，反推需要什么前件
- 一条条对照规则找匹配

**第 4 步：写证明**
- 每行写一个公式
- 右边标注：行号 + 规则名

**第 5 步：验证**
- 检查每步引用的前提是否真存在
- 检查规则名是否正确
- 检查结论是否就是目标

### 复合推理的常用套路

**套路 1：MT 收尾**
- 看到结论是 ¬p，找前提里有 p→q 和 ¬q（MT 反向）
- 或找 p→q 和 ¬q 的等价物

**套路 2：HS 串联**
- 多个 p→q, q→r, r→s 链接 → HS 一次得到 p→r → 再 HS 得到 p→s
- 谓词推理常这样做

**套路 3：De Morgan + 简化**
- ¬(A∧B) → ¬A ∨ ¬B → 配合 DS 或 简化 + Add

**套路 4：Addition 收尾**
- 结论是 p∨q，已证 p，加 Add 即可
- 或已证 q 也可

### 谓词推理的陷阱：EI 后不能再 UG

**规则冲突**：
- EI 把 ∃x P(x) 引入一个**特定的 c**（满足 P(c)）
- UG 要求 c 是**任意**的（对任意 c 都成立）
- 因此 EI 后**不能**用 UG

**实战**：
- ∃x P(x) → P(c) [EI] → Q(c) [其他推导] → ∃x Q(x) [EG]  ✓
- ∃x P(x) → P(c) [EI] → ∀x Q(x) [UG] ✗ （c 不再任意）

### 论证有效性的两种判定方法

**方法 1：找推理链**
- 能用规则推出来 → 有效
- 推不出来 → 无效

**方法 2：找反例（更可靠）**
- 找一组赋值使所有前提真但结论假
- 找到 → 无效
- 找不到（穷举）→ 有效

**实战**：判定 "p, p→q ⊢ q" 有效性
- 用 MP：p + p→q → q ✓
- 有效

**实战**：判定 "p→q, q ⊢ p" 有效性
- 找反例：p=F, q=T：p→q=T, q=T，但 p=F
- 前提真但结论假 → 无效

### 谓词证明的"重用 c"技巧

谓词证明的标准做法是把多个 ∃ 引入的 c **合并为一个**（虽然严格逻辑不严谨，但教材接受这种"重用"）。

**实战**：

```
前提: ∃x P(x), ∃x Q(x)
证明: ∃x (P(x) ∧ Q(x))

证:
1. ∃x P(x)            Premise
2. P(c)                1, EI
3. ∃x Q(x)            Premise
4. Q(c)                3, EI  ← 重用 c
5. P(c) ∧ Q(c)         2, 4, Conj
6. ∃x (P(x) ∧ Q(x))   5, EG
```

> **考试标准写法**：就是这种重用 EI。

## 典型例题

### 例 6.1：识别推理规则

**题**：识别每条论证使用的规则：
a) Alice 是数学专业。所以 Alice 是数学专业或计算机专业。
b) 天下雨，地就湿。下雨了。所以地湿了。
c) 若明天下雨，运动会取消。明天下雨。所以运动会取消。

**解**：
- a) p, ∴ p∨q → **Addition**
- b) p→q, p, ∴ q → **Modus Ponens**
- c) 同 b → **MP**

### 例 6.2：基础推理证明

**题**：从前提 "If I don't sleep well, then I don't have strange dreams." 和 "I have strange dreams." 推出 "I sleep well."

**解**（设 r = 睡不好, q = 做怪梦）：

```
1. r → ¬q            Premise
2. q                 Premise
3. ¬¬q               2, DN
4. ¬r                1, 3, MT
5. ∴ 我睡得好        ¬r = "我睡得好"
```

### 例 6.3：复合推理（典型必考）

**题**：从前提
- p → q
- ¬q → r
- ¬r
推 p → ¬s（任何 s）

**解**：

```
1. p → q              Premise
2. ¬q → r             Premise
3. ¬r                 Premise
4. ¬¬q                ?, 错误，让我重新推导
```

实际推导：

```
1. p → q              Premise
2. ¬q → r             Premise
3. ¬r                 Premise
4. ¬q                 2, 3, MT  (¬q→r 和 ¬r → ¬q)
5. ¬p                 1, 4, MT
```

但要证明 p → ¬s：p 真时 ¬p 假。所以这组前提**不能**推出 p → ¬s。

> **实战提示**：先看结论形式，反推需要的步骤。如果某前提无法用上，可能说明论证无效。

### 例 6.4：多步谓词证明（必考大题）

**题**：从前提
- ∀x (R(x) → S(x))       "所有人读书就服务人民"
- ∀x (S(x) → D(x))       "所有服务人民的人应受表扬"
- ∀x (D(x) → P(x))       "所有应受表扬的人会升职"
- ¬P(Harry)               "Harry 不会升职"
证 ¬R(Harry)               "Harry 没读书"

**解**：

```
1. ∀x (R(x) → S(x))        Premise
2. ∀x (S(x) → D(x))        Premise
3. ∀x (D(x) → P(x))        Premise
4. ¬P(Harry)               Premise
5. R(Harry) → S(Harry)     1, UI
6. S(Harry) → D(Harry)     2, UI
7. D(Harry) → P(Harry)     3, UI
8. R(Harry) → P(Harry)     5, 6, 7, HS（连续）
9. ¬R(Harry)               8, 4, MT
```

✓ 证毕

> **实战模板**：
> 1. 多个 ∀ 前提 → 一律 UI
> 2. UI 结果用 HS 链接
> 3. 用 MT 收尾（已知 ¬结论的反面）

### 例 6.5：复合条件句证明（必考）

**题**：从前提
- (¬p ∨ ¬q) → (r ∧ s)
- ¬s
证 p ∨ q

**解**：

```
1. (¬p ∨ ¬q) → (r ∧ s)    Premise
2. ¬s                      Premise
3. ¬(r ∧ s)                ?, 不能从 2 直接得 ¬(r∧s)
   实际: s 假时，r ∧ s 假 → ¬(r∧s) 真 ✓
   但要从 ¬s 推 ¬(r∧s) 需要：(r∧s)→s 是公理，所以 ¬s → ¬(r∧s)
   这个推理我们承认。
4. ¬(r ∧ s)                2, 反向推理（从 ¬s 推出 ¬(r∧s)）
5. ¬(¬p ∨ ¬q)              1, 4, MT（取逆否）
6. p ∧ q                   5, De Morgan
7. p                       6, Simp
8. p ∨ q                   7, Addition
```

✓ 证毕

> **实战模板**：
> 1. 复合条件句用 MT 时要取逆否
> 2. De Morgan 处理双重否定
> 3. 结尾用 Add 或 DS

### 例 6.6：谓词推理（中等难度）

**题**：从前提
- ∀x (L(x) → F(x))           "所有狮子凶猛"
- ∃x (L(x) ∧ ¬C(x))         "有些狮子不喝咖啡"
- ∃x (F(x) ∧ ¬C(x) ∧ M(x))  "有些不喝咖啡的凶猛动物吃人"
证 ∃x (M(x) ∧ L(x) ∧ ¬C(x))  "有些不喝咖啡的狮子吃人"

**解**：

```
1. ∀x (L(x) → F(x))           Premise
2. ∃x (L(x) ∧ ¬C(x))         Premise
3. ∃x (F(x) ∧ ¬C(x) ∧ M(x))  Premise
4. L(c) ∧ ¬C(c)               2, EI
5. L(c) → F(c)                1, UI
6. F(c)                       4, 5, MP
7. L(c) ∧ ¬C(c) ∧ F(c)        4, 6, Conj
8. F(c) ∧ ¬C(c) ∧ M(c)        3, EI（重用 c）
9. M(c) ∧ L(c) ∧ ¬C(c)        7, 8, Conj
10. ∃x (M(x) ∧ L(x) ∧ ¬C(x)) 9, EG
```

> **实战提示**：谓词证明每步右边标"行号, 规则名"，让评分老师看得清楚。

## 易错点总结

- ❌ MT 用反（p→q + ¬p 推不出 ¬q）
- ❌ EI 后用 UG（c 已不任意）
- ❌ UI 把所有变量都用同一个 c（应该用 a, b, c 等不同名）
- ❌ 谓词证明不标行号和规则
- ❌ De Morgan 在否定时漏联结词翻转
- ❌ 推理链中间卡住不知如何继续（提示：看结论形式反推）

## 配套作业（精选）

- 1.6.1（识别规则 - 必做）
- 1.6.5, 1.6.10（基础推理）
- 1.6.15（论证有效性）
- 1.6.20, 1.6.28（用规则证明 - 必考）
- 1.6.25, 1.6.32（谓词推理 - 必考）

---

## 总复习清单

- [ ] 5 个联结词真值表闭卷能写
- [ ] "only if" / "unless" / "whenever" 等英文短语对应 → 方向
- [ ] contrapositive 等价于原条件（converse / inverse 不等价）
- [ ] De Morgan 双公式倒背如流
- [ ] 条件等价 p→q ≡ ¬p∨q ≡ ¬q→¬p
- [ ] ¬(p→q) ≡ p∧¬q（不是 ¬p→¬q）
- [ ] Table 6 等价律（11 条）
- [ ] Table 7 条件等价（9 条）
- [ ] Table 8 双条件等价（4 条）
- [ ] 量词否定 ∀↔∃
- [ ] "All A are B" → ∀x(A→B)，"Some A are B" → ∃x(A∧B)
- [ ] ∀x∃y vs ∃x∀y 量词次序不可换
- [ ] 永真证明两种方法：设结论假推矛盾 / 等价律链 ≡ T
- [ ] 8 条命题规则能识别 + 写出
- [ ] 4 条谓词规则：UI/UG/EI/EG
- [ ] EI 后**不能**用 UG
- [ ] 谓词证明模板：UI + HS + MT 收尾
- [ ] 复合条件句：取逆否 + De Morgan + Add/DS 收尾