# KMP算法

## 定义
KMP（Knuth-Morris-Pratt）算法是高效的字符串匹配算法，通过预处理模式串构建next数组（失配指针），避免重复比较，时间复杂度O(n+m)，优于暴力匹配的O(nm)。

## 核心内容
**1. next数组（最长公共前后缀）**
```cpp
// next[i]：模式串s[0..i]的最长公共前后缀长度
void build_next(string pattern, vector<int>& next) {
    int m = pattern.length();
    next.resize(m);
    next[0] = 0;
    
    int j = 0;  // 前缀末尾
    for (int i = 1; i < m; i++) {
        // 失配时回退
        while (j > 0 && pattern[i] != pattern[j]) {
            j = next[j - 1];
        }
        
        if (pattern[i] == pattern[j]) {
            j++;
        }
        next[i] = j;
    }
}

// 示例：pattern = "ABABC"
// next = [0, 0, 1, 2, 0]
```

**2. KMP匹配**
```cpp
vector<int> kmp_search(string text, string pattern) {
    int n = text.length(), m = pattern.length();
    if (m == 0) return {};
    
    vector<int> next;
    build_next(pattern, next);
    
    vector<int> matches;  // 所有匹配位置
    int j = 0;  // 模式串指针
    
    for (int i = 0; i < n; i++) {
        // 失配时根据next数组跳转
        while (j > 0 && text[i] != pattern[j]) {
            j = next[j - 1];
        }
        
        if (text[i] == pattern[j]) {
            j++;
        }
        
        if (j == m) {  // 完全匹配
            matches.push_back(i - m + 1);
            j = next[j - 1];  // 继续查找下一个
        }
    }
    
    return matches;
}

// 时间复杂度：O(n + m)
// 空间复杂度：O(m)
```

**3. 查找第一个匹配**
```cpp
int kmp_find(string text, string pattern) {
    int n = text.length(), m = pattern.length();
    if (m == 0) return 0;
    
    vector<int> next;
    build_next(pattern, next);
    
    int j = 0;
    for (int i = 0; i < n; i++) {
        while (j > 0 && text[i] != pattern[j]) {
            j = next[j - 1];
        }
        if (text[i] == pattern[j]) {
            j++;
        }
        if (j == m) {
            return i - m + 1;  // 返回起始位置
        }
    }
    
    return -1;  // 未找到
}
```

**4. 计数匹配次数**
```cpp
int kmp_count(string text, string pattern) {
    vector<int> matches = kmp_search(text, pattern);
    return matches.size();
}
```

**5. next数组优化版（nextval）**
```cpp
// 优化：当失配时，如果next[j]位置字符与当前相同，继续跳转
void build_nextval(string pattern, vector<int>& nextval) {
    int m = pattern.length();
    nextval.resize(m);
    nextval[0] = -1;  // 不同定义
    
    int j = -1;
    for (int i = 0; i < m - 1; i++) {
        while (j >= 0 && pattern[i] != pattern[j]) {
            j = nextval[j];
        }
        j++;
        
        // 优化：跳过相同字符
        if (pattern[i + 1] == pattern[j]) {
            nextval[i + 1] = nextval[j];
        } else {
            nextval[i + 1] = j;
        }
    }
}
```

**6. 最小循环节**
```cpp
// 如果len % (len - next[len-1]) == 0，则有循环节
int min_period(string s) {
    int n = s.length();
    vector<int> next;
    build_next(s, next);
    
    int len = n - next[n - 1];
    if (n % len == 0) {
        return len;  // 最小循环节长度
    }
    return n;  // 无循环节
}

// 示例："abcabcabc" -> 循环节 "abc"，长度3
```

**7. 最长回文前缀**
```cpp
int longest_palindrome_prefix(string s) {
    string rev = s;
    reverse(rev.begin(), rev.end());
    string combined = s + "#" + rev;
    
    vector<int> next;
    build_next(combined, next);
    
    return next.back();  // 最长公共前后缀
}
```

**8. 应用：重复子串**
```cpp
// LeetCode 459：判断是否由子串重复构成
bool repeatedSubstringPattern(string s) {
    int n = s.length();
    vector<int> next;
    build_next(s, next);
    
    int len = n - next[n - 1];
    return next[n - 1] > 0 && n % len == 0;
}
```

**9. KMP vs 暴力匹配**
```cpp
// 暴力匹配（O(nm)）
int brute_force(string text, string pattern) {
    int n = text.length(), m = pattern.length();
    for (int i = 0; i <= n - m; i++) {
        int j = 0;
        while (j < m && text[i + j] == pattern[j]) {
            j++;
        }
        if (j == m) return i;
    }
    return -1;
}
```

**10. next数组图解**
```
pattern: A B A B C
index:   0 1 2 3 4
next:    0 0 1 2 0

解释：
- next[0] = 0：空串无前后缀
- next[1] = 0："A"无公共前后缀
- next[2] = 1："AB"无，"ABA"有公共"A"
- next[3] = 2："ABAB"有公共"AB"
- next[4] = 0："ABABC"无公共前后缀
```

## 应用场景
- 字符串匹配：文本编辑器的查找功能
- 模式识别：DNA序列匹配
- 数据压缩：检测重复模式
- 网络入侵检测：特征码匹配
- 文本处理：查找替换
- 循环节判断：周期字符串

## 注意事项
- next数组定义有多种（0-based, -1-based）
- next[i]表示s[0..i]的最长公共前后缀
- 失配时跳转到next[j-1]位置
- KMP不回溯文本串指针
- 预处理时间O(m)，匹配时间O(n)
- 空模式串返回0（约定）

## 关联知识
与 [[字符串哈希]]、[[字符串]]、[[动态规划]] 相关。
