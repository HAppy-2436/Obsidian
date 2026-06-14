# ch4Huffman编码案例-Entropy
- 来源路径：`C:\Users\Li\OneDrive\Backup\1\大一下\2024数据结构与算法wlp\数据结构\数据结构与算法\课件\第一部分\ch4Huffman编码案例-Entropy.pdf`
- 页数：2 页
- 提取字符数：1062

## 核心概念
- 哈夫曼编码 (Huffman)
- 字符串 (String)
- vector
- algorithm 头文件
## 关键定义
- （无）
## 时间复杂度 / 复杂度要点
- （无）
## 典型例题
- 输入一个字符串，分别用普通ASCII 编码（每个字符8bit）和huffman 编码，输出编码后
- 的长度，并输出压缩比。
- Sample Input：
- Sample Output：
## 代码片段
- #include <cstdio>
- #include <cstring>
- #include <string>
- #include <iostream>

## 提取的原始内容

```text
Huffman 编码案例-Entropy 
输入一个字符串，分别用普通ASCII 编码（每个字符8bit）和huffman 编码，输出编码后
的长度，并输出压缩比。 
Sample Input： 
AAAAABCD 
THE_CAT_IN_THE_HAT 
END 
Sample Output： 
64 13 4.9 
144 51 2.8 
 
参考代码： 
#include <cstdio> 
#include <cstring> 
#include <string> 
#include <iostream> 
#include <algorithm> 
#include <queue> 
using namespace std; 
 
string s; 
priority_queue <int, vector<int>, greater<int> > q; 
//priority_queue <int> q; 
int main() 
{ 
 
while(getline(cin, s) && s != "END"){ 
 
 
int t = 1; 
 
 
sort(s.begin(), s.end()); 
 
 
for(int i = 1; i < s.length(); i++){ 
 
 
 
if(s[i] != s[i-1]){ 
 
 
 
 
q.push(t); 
 
 
 
 
t = 1; 
 
 
 
} 
 
 
 
else t++; 
 
 
} 
 
 
q.push(t); 
 
 
 
if(q.size() == 1) { 
 
 
 
printf("%d %d 8.0\n", s.length()*8, s.length()); 
 
 
 
q.pop(); 
 
 
 
continue; 
 
 
} 
 
 
 
int ans = 0; 

 
 
while(q.size() > 1){ 
 
 
 
int a = q.top(); q.pop(); 
 
 
 
int b = q.top(); q.pop(); 
 
 
 
q.push(a+b); 
 
 
 
ans += a+b; 
 
 
} 
 
 
q.pop(); 
 
 
printf("%d %d %.1lf\n", s.length()*8, ans, (double)s.length()*8.0/(double)ans); 
 
} 
} 

```
