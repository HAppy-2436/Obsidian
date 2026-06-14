# ch4归并算法案例-逆序对
- 来源路径：`C:\Users\Li\OneDrive\Backup\1\大一下\2024数据结构与算法wlp\数据结构\数据结构与算法\课件\第一部分\ch4归并算法案例-逆序对.pdf`
- 页数：2 页
- 提取字符数：1429

## 核心概念
- 归并排序 (Merge Sort)
- 逆序对 (Inversion Count)
## 关键定义
- 序列中的一个逆序对，是指存在两个数𝒂_𝒊和𝒂_𝒋  ，有𝒂_𝒊>𝒂_𝒋且𝟏≤𝒊<𝒋≤𝒏。也就是说，大
- ll mid = left+ (right-left)/2;//即mid =(left+ right)/2 平分成两个子序列,避免left+
## 时间复杂度 / 复杂度要点
- （无）
## 典型例题
- 输入一个序列{𝒂_𝟏,𝒂_𝟐, …,𝒂_𝒏} ，交换任意两个相邻元素，不超过k 次。交换之后，问最少
- 输入：输入包含多个测试。对于每个测试：
- 输出：最少的逆序对数量。
- Sample Input：
- Sample Output：
## 代码片段
- #include <bits/stdc++.h>
- void Merge(ll a[], ll left, ll mid, ll right){
- void Mergesort(ll a[], ll left, ll right){
- int main(){

## 提取的原始内容

```text
归并算法案例-逆序对问题 
输入一个序列{𝒂_𝟏,𝒂_𝟐, …,𝒂_𝒏} ，交换任意两个相邻元素，不超过k 次。交换之后，问最少
的逆序对有多少个。 
序列中的一个逆序对，是指存在两个数𝒂_𝒊和𝒂_𝒋  ，有𝒂_𝒊>𝒂_𝒋且𝟏≤𝒊<𝒋≤𝒏。也就是说，大
的数排在小的数前面。 
输入：输入包含多个测试。对于每个测试： 
第一行是n和k，𝟏 ≤ 𝒏 ≤ 〖𝟏𝟎〗^𝟓，𝟎 ≤ 𝒌 ≤ 〖𝟏𝟎〗^𝟗；第二行包括n个整数{𝒂_𝟏,𝒂_𝟐, …,𝒂_𝒏}，
𝟎≤ 𝒂_𝒊  ≤〖𝟏𝟎〗^𝟗。 
输出：最少的逆序对数量。 
Sample Input： 
3 1 
2 2 1 
3 0 
2 2 1 
Sample Output： 
1 
2 
 
参考代码： 
#include <bits/stdc++.h> 
const int MAXN = 100005; 
typedef long long ll; 
ll a[MAXN],cnt; 
 
void Merge(ll a[], ll left, ll mid, ll right){ 
    ll b[MAXN], i=left, j = mid+ 1, t=left; 
    while(i <= mid && j<=right){ 
        if(a[i]> a[j]){ 
            b[t++] = a[j++]; 
            cnt+=mid-i+1;//记录逆序对数量 
        } 
        else b[t++]=a[i++]; 
    } 
    //一个子序列中的数都处理完了，另一个还没有，把剩下的直接复制过来 
    while(i <= mid) b[t++]=a[i++]; 
    while(j <= right) b[t++]=a[j++]; 
    for(i=left; i<=right; i++) a[ i] = b[i];//把排好序的b[]复制回a[] 
} 
 
void Mergesort(ll a[], ll left, ll right){ 
    if(left<right){ 
        ll mid = left+ (right-left)/2;//即mid =(left+ right)/2 平分成两个子序列,避免left+ 
right 和溢出 
        Mergesort(a, left, mid); 

        Mergesort(a, mid+ 1, right); 
        Merge(a, left, mid, right);//合并 
    } 
} 
 
int main(){ 
    ll n,k; 
    while(scanf("%lld%lld", &n, &k)==2){ 
        cnt = 0; 
        for(ll i=0;i<n;i++) scanf("%lld", &a[i]); 
        Mergesort(a,0,n- 1);//归并排序 
        if(cnt<=k) printf("0\n"); 
        else       printf("%I64d\n", cnt - k); 
    } 
    return 0; 
} 

```
