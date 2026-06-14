# ch5状压动态规划案例-消除字符串
- 来源路径：`C:\Users\Li\OneDrive\Backup\1\大一下\2024数据结构与算法wlp\数据结构\数据结构与算法\课件\第二部分\ch5状压动态规划案例-消除字符串.pdf`
- 页数：2 页
- 提取字符数：872

## 核心概念
- 字符串 (String)
- 动态规划 (DP)
- 状态压缩 DP
## 关键定义
- 小明喜欢中心对称的字符串，即回文字符串。现在小明手里有一个字符串 S，小明每次都会
## 时间复杂度 / 复杂度要点
- （无）
## 典型例题
- 输入格式：输入一行。输入一个字符串 S（1≤length(S)≤16），字符串均由小写字母组成。
- 输出格式：输出一行，输出一个整数，表示消除整个字符串需要的最少操作次数。
- 样例输入
- 样例输出
## 代码片段
- #include<bits/stdc++.h>
- int main(){
- cin>>s;
- cout<<dp[(1<<t)-1]<<endl;

## 提取的原始内容

```text
ch5 状压动态规划案例-消除字符串 
小明喜欢中心对称的字符串，即回文字符串。现在小明手里有一个字符串 S，小明每次都会
进行这样的操作：从 S 中挑选一个回文的子序列，将其从字符串 S 中去除，剩下的字符重
组成新的字符串 S。  小明想知道，最少可以进行多少次操作，可以消除整个字符串。   
输入格式：输入一行。输入一个字符串 S（1≤length(S)≤16），字符串均由小写字母组成。   
输出格式：输出一行，输出一个整数，表示消除整个字符串需要的最少操作次数。   
样例输入   
abaccba  
样例输出   
2 
 
参考代码： 
#include<bits/stdc++.h> 
using namespace std; 
int dp[(1<<16)+10]={0}; 
string s; 
const int inf =0x3f3f3f3f; 
int check(int j){ 
 
string s1="",s2=""; 
 
int pos=0; 
 
while(j){ 
 
 
if(j&1){ 
 
 
 
s1+=s[pos]; 
 
 
} 
 
 
pos++; 
 
 
j>>=1; 
 
} 
 
s2=s1; 
 
reverse(s2.begin(),s2.end()); 
 
return s1==s2; 
} 
int main(){ 
 
cin>>s; 
 
int t=s.size(); 
 
for(int i=1;i<(1<<t);i++){ 
 
 
if(check(i)){ 
 
 
 
dp[i]=1; 
 
 
}else{ 
 
 
 
dp[i]=inf; 
 
 
 
for(int j=i;j;j=(j-1)&i){ 
 
 
 
 
dp[i]=min(dp[i],dp[j]+dp[j^i]); 
 
 
 
} 
 
 
} 
 
} 

 
cout<<dp[(1<<t)-1]<<endl; 
 
return 0; 
} 

```
