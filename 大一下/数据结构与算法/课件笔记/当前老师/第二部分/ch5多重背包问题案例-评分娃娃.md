# ch5多重背包问题案例-评分娃娃
- 来源路径：`C:\Users\Li\OneDrive\Backup\1\大一下\2024数据结构与算法wlp\数据结构\数据结构与算法\课件\第二部分\ch5多重背包问题案例-评分娃娃.pdf`
- 页数：2 页
- 提取字符数：1156

## 核心概念
- 背包问题 (Knapsack)
- 多重背包 (Multiple Knapsack)
- vector
- set / unordered_set
## 关键定义
- （无）
## 时间复杂度 / 复杂度要点
- （无）
## 典型例题
-  输入格式
-  输入一行，输入 6 个整数，代表每种娃娃的数量 mi（0≤mi≤20,000）。
-  输出格式
-  输出一行。如果能把所有娃娃分成萌值之和相同的两组，请输出Can be divided.，
- 否则输出Can’t be divided.。
## 代码片段
- #include <cstdio>
- #include <cstring>
- #include <iostream>
- #include <vector>

## 提取的原始内容

```text
ch5 多重背包问题案例-评分娃娃 
 小明酷爱收集萌萌的娃娃。小明收集了 6 种不同的娃娃，第 i 种娃娃的萌值为 i（1
≤i≤6）。现在已知每种娃娃的数量 mi，小明想知道，能不能把娃娃分成两组，使得
每组的娃娃萌值之和相同。  
 输入格式  
 输入一行，输入 6 个整数，代表每种娃娃的数量 mi（0≤mi≤20,000）。  
 输出格式  
 输出一行。如果能把所有娃娃分成萌值之和相同的两组，请输出Can be divided.，
否则输出Can’t be divided.。  
 样例输入  
 2 0 1 1 2 1  
 样例输出  
 Can’t be divided. 
 
参考代码： 
#include <cstdio> 
#include <cstring> 
#include <iostream> 
#include <vector> 
using namespace std; 
vector<int>v; 
int a[10]; 
int dp[200000]; 
int cnt=0; 
int main() 
{ 
    memset(dp,0,sizeof(dp)); 
    int goal=0; 
    for(int i=1;i<=6;i++) 
    { 
        cin>>a[i]; 
        goal+=i*a[i]; 
    } 
    for(int i=1;i<=6;i++) 
    {   int j=0; 
        for(;a[i]>=(1<<j);j++) 
        { 
            v.push_back(i*(1<<j)); 
            a[i]-=v[j]; 
        } 
        v.push_back(i*(a[i])); 
    } 
    if(goal%2==1){ 
        cout<<"Can't be divided."; 

        return 0; 
    } 
    goal=goal/2; 
    for(int i=0;i<v.size();i++) 
    { 
        for(int j=v[i];j<=goal;j++) 
        dp[j]=max(dp[j],dp[j-v[i]]+v[i]); 
    } 
    if(dp[goal]==goal)cout<<"Can be divided."; 
    else cout<<"Can't be divided."; 
    return 0; 
    } 

```
