# 图的广度优先遍历 BFS
- 来源：`C:\Users\Li\OneDrive\Backup\1\大一下\2024数据结构与算法wlp\历年\王丽i萍 数据结构与算法\王丽i萍 数据结构与算法\lzl大一下 数据结构与算法\7.3.2图的广度优先遍历.ppt.pdf`
- 课件（PDF）页数：51
- 提取文本段：0
- 字符数：6653

## 核心概念
- 图 (Graph)
- 邻接表 (Adjacency List)
- 广度优先搜索 (BFS)
- 数组 (Array)
- 队列 (Queue)

## 代码片段
```cpp
{
Visited[100]={False}；//假设图中顶点数没有超过100个
Visited[x]=True；cout<<x;Queue.push(x);
{
V= Queue.front();
Queue.pop();
{
Visited[w]=True;cout<<w;Queue.push（w）；
}
}
}
void BFS (ALGraph mg,int x)
{
bool visited[100]={false};
queue<int> q;
cout<<mg.vexs[x].data <<" ";visited[x]=true;q.push(x);
while(q.empty()==false){
int v=q.front();
q.pop();
for(int w=::FirstAdjVex(mg,v);w>0;w=::NextAdjVex(mg,v,w)){
```

## 提取的原始内容

```text
算法演示
2.

0
例图及其邻接表表示
1 v1
v2 v3
v1
2 v2
v1 v4 v5
3 V3
v1 v6 v7
v2
v3
4 V4
v2 v8
v4
v5 v6 v7
5 v5
v2 v8
6 v6
v3 v7
v8
7 v7
v3 v6
8 v8
v4 v5

演示开始，以 为遍历的起点
v1

0
队列
1 v1
v2 v3
2 v2
v1 v4 v5
3 V3
v1 v6 v7
4 V4
v2 v8
5 v5
v2 v8
v1
访问v1
6 v6
v3 v7
7 v7
v3 v6
8 v8
v4 v5

0
队列
1 v1
v2 v3
v1
2 v2
v1 v4 v5
3 V3 V1入队列
v1 v6 v7
4 V4
v2 v8
5 v5
v2 v8
v1
6 v6
v3 v7
7 v7
v3 v6
8 v8
v4 v5

0
队列
1 v1
v2 v3
2 v2
v1 v4 v5
3 V3
v1 v6 v7
取队头元素
v1
4 V4
v2 v8
5 v5
v2 v8
v1
6 v6
v3 v7
7 v7
v3 v6
8 v8
v4 v5

0
队列
1 v1
v2 v3
2 v2
v1 v4 v5
3 V3
v1 v6 v7
v1
4 V4
v2 v8
V1的邻接点v2没
有被访问过，访
问之，且入队列
5 v5
v2 v8
v1 v2
6 v6
v3 v7
7 v7
v3 v6
8 v8
v4 v5

0
队列
1 v1
v2 v3
2 v2 v2
v1 v4 v5
3 V3
v1 v6 v7
v1
4 V4
v2 v8
5 v5
v2 v8
v1 v2
6 v6
v3 v7
7 v7
v3 v6
8 v8
v4 v5

0
队列
1 v1
v2 v3
2 v2 v2
v1 v4 v5
3 V3
v1 v6 v7
v1
4 V4
v2 v8
V1的邻接点v3没
有被访问过，访
问之，且入队列
5 v5
v2 v8
v1 v2 v3
6 v6
v3 v7
7 v7
v3 v6
8 v8
v4 v5

0
队列
1 v1
v2 v3
2 v2 v2 v3
v1 v4 v5
3 V3
v1 v6 v7
v1
4 V4
v2 v8
5 v5
v2 v8
v1 v2 v3
6 v6
v3 v7
7 v7
v3 v6
8 v8
v4 v5

0
队列
1 v1
v2 v3
2 v2 v2 v3
v1 v4 v5
3 V3
v1 v6 v7
4 V4
v2 v8
5 v5
v2 v8
v1 v2 v3
6 v6
v3 v7
7 v7
v3 v6
8 v8
v4 v5

0
队列
1 v1
v2 v3
2 v2 v3
v1 v4 v5
3 V3
v1 v6 v7
v2
4 V4
v2 v8
5 v5
v2 v8
v1 v2 v3
6 v6
v3 v7
7 v7
v3 v6
8 v8
v4 v5

0
队列
1 v1
v2 v3
2 v2 v3
v1 v4 v5
3 V3
v1 v6 v7
v2
4 V4
v2 v8
5 v5
v2 v8
v1 v2 v3
6 v6
v3 v7
7 v7
v3 v6
8 v8
v4 v5

0
队列
1 v1
v2 v3
2 v2 v3
v1 v4 v5
3 V3
v1 v6 v7
v2
4 V4
v2 v8
V2的邻接点v1已
经被访问过不再
访问
5 v5
v2 v8
v1 v2 v3
6 v6
v3 v7
7 v7
v3 v6
8 v8
v4 v5

0
队列
1 v1
v2 v3
2 v2 v3
v1 v4 v5
3 V3
v1 v6 v7
v2
4 V4
v2 v8
5 v5
v2 v8
v1 v2 v3 v4
6 v6
v3 v7
V2的邻接点v4没
有被访问过，访
7 v7
v3 v6
问之，且入队列
8 v8
v4 v5

0
队列
1 v1
v2 v3
2 v2 v3 v4
v1 v4 v5
3 V3
v1 v6 v7
v2
4 V4
v2 v8
5 v5
v2 v8
v1 v2 v3 v4
6 v6
v3 v7
7 v7
v3 v6
8 v8
v4 v5

0
队列
1 v1
v2 v3
2 v2 v3 v4
v1 v4 v5
3 V3
v1 v6 v7
v2
4 V4
v2 v8
5 v5
v2 v8
v1 v2 v3 v4 v5
6 v6
v3 v7
V2的邻接点v5没
有被访问过，访
7 v7
v3 v6
问之，且入队列
8 v8
v4 v5

0
队列
1 v1
v2 v3
2 v2 v3 v4 v5
v1 v4 v5
3 V3
v1 v6 v7
v2
4 V4
v2 v8
5 v5
v2 v8
v1 v2 v3 v4 v5
6 v6
v3 v7
7 v7
v3 v6
8 v8
v4 v5

0
队列
1 v1
v2 v3
2 v2 v3 v4 v5
v1 v4 v5
3 V3
v1 v6 v7
4 V4
v2 v8
5 v5
v2 v8
v1 v2 v3 v4 v5
6 v6
v3 v7
7 v7
v3 v6
8 v8
v4 v5

0
队列
1 v1
v2 v3
2 v2 v4 v5
v1 v4 v5
3 V3
v1 v6 v7
v3
4 V4
v2 v8
5 v5
v2 v8
v1 v2 v3 v4 v5
6 v6
v3 v7
7 v7
v3 v6
8 v8
v4 v5

0
队列
1 v1
v2 v3
2 v2 v4 v5
v1 v4 v5
3 V3
v1 v6 v7
v3
4 V4
v2 v8
5 v5
v2 v8
v1 v2 v3 v4 v5
6 v6
v3 v7
7 v7
v3 v6
8 v8
v4 v5

0
队列
1 v1
v2 v3
2 v2 v4 v5
v1 v4 v5
3 V3
v1 v6 v7
v3
4 V4
v2 v8
5 v5
v2 v8
v1 v2 v3 v4 v5
6 v6
v3 v7
V3的邻接点v1已
7 v7 经被访问过不再
v3 v6
访问
8 v8
v4 v5

0
队列
1 v1
v2 v3
2 v2 v4 v5
v1 v4 v5
3 V3
v1 v6 v7
v3
4 V4
v2 v8
5 v5
v2 v8
v1 v2 v3 v4 v5 v6
6 v6
v3 v7
V3的邻接点v6没
有被访问过，访
7 v7
v3 v6
问之，且入队列
8 v8
v4 v5

0
队列
1 v1
v2 v3
2 v2 v4 v5 v6
v1 v4 v5
3 V3
v1 v6 v7
v3
4 V4
v2 v8
5 v5
v2 v8
v1 v2 v3 v4 v5 v6
6 v6
v3 v7
7 v7
v3 v6
8 v8
v4 v5

0
队列
1 v1
v2 v3
2 v2 v4 v5 v6
v1 v4 v5
3 V3
v1 v6 v7
v3
4 V4
v2 v8
5 v5
v2 v8
v1 v2 v3 v4 v5 v6 v7
6 v6
v3 v7
V3的邻接点v7没
有被访问过，访
7 v7
v3 v6
问之，且入队列
8 v8
v4 v5

0
队列
1 v1
v2 v3
2 v2 v4 v5 v6 v7
v1 v4 v5
3 V3
v1 v6 v7
v3
4 V4
v2 v8
5 v5
v2 v8
v1 v2 v3 v4 v5 v6 v7
6 v6
v3 v7
7 v7
v3 v6
8 v8
v4 v5

0
队列
1 v1
v2 v3
2 v2 v4 v5 v6 v7
v1 v4 v5
3 V3
v1 v6 v7
4 V4
v2 v8
5 v5
v2 v8
v1 v2 v3 v4 v5 v6 v7
6 v6
v3 v7
7 v7
v3 v6
8 v8
v4 v5

0
队列
1 v1
v2 v3
2 v2 v5 v6 v7
v1 v4 v5
3 V3
v1 v6 v7
v4
4 V4
v2 v8
5 v5
v2 v8
v1 v2 v3 v4 v5 v6 v7
6 v6
v3 v7
7 v7
v3 v6
8 v8
v4 v5

0
队列
1 v1
v2 v3
2 v2 v5 v6 v7
v1 v4 v5
3 V3
v1 v6 v7
v4
4 V4
v2 v8
5 v5
v2 v8
v1 v2 v3 v4 v5 v6 v7
6 v6
v3 v7
7 v7
v3 v6
8 v8
v4 v5

0
队列
1 v1
v2 v3
2 v2 v5 v6 v7
v1 v4 v5
3 V3
v1 v6 v7
v4
4 V4
v2 v8
5 v5
v2 v8
v1 v2 v3 v4 v5 v6 v7
6 v6
v3 v7
V4的邻接点v2已
7 v7
v3 v6
经被访问过不再
访问
8 v8
v4 v5

0
队列
1 v1
v2 v3
2 v2 v5 v6 v7
v1 v4 v5
3 V3
v1 v6 v7
v4
4 V4
v2 v8
5 v5
v2 v8
v1 v2 v3 v4 v5 v6 v7 v8
6 v6
v3 v7
V4的邻接点v8没
有被访问过，访
7 v7
v3 v6
问之，且入队列
8 v8
v4 v5

0
队列
1 v1
v2 v3
2 v2 v5 v6 v7 v8
v1 v4 v5
3 V3
v1 v6 v7
v4
4 V4
v2 v8
5 v5
v2 v8
v1 v2 v3 v4 v5 v6 v7 v8
6 v6
v3 v7
7 v7
v3 v6
8 v8
v4 v5

0
队列
1 v1
v2 v3
2 v2 v5 v6 v7 v8
v1 v4 v5
3 V3
v1 v6 v7
4 V4
v2 v8
5 v5
v2 v8
v1 v2 v3 v4 v5 v6 v7 v8
6 v6
v3 v7
7 v7
v3 v6
8 v8
v4 v5

0
队列
1 v1
v2 v3
2 v2 v6 v7 v8
v1 v4 v5
3 V3
v1 v6 v7
v5
4 V4
v2 v8
5 v5
v2 v8
v1 v2 v3 v4 v5 v6 v7 v8
6 v6
v3 v7
7 v7
v3 v6
8 v8
v4 v5

0
队列
1 v1
v2 v3
2 v2 v6 v7 v8
v1 v4 v5
3 V3
v1 v6 v7
v5
4 V4
v2 v8
5 v5
v2 v8
v1 v2 v3 v4 v5 v6 v7 v8
6 v6
v3 v7
7 v7 V5的邻接点v2、
v3 v6
v8已经被访问过
不再访问
8 v8
v4 v5

0
队列
1 v1
v2 v3
2 v2 v6 v7 v8
v1 v4 v5
3 V3
v1 v6 v7
4 V4
v2 v8
5 v5
v2 v8
v1 v2 v3 v4 v5 v6 v7 v8
6 v6
v3 v7
7 v7
v3 v6
8 v8
v4 v5

0
队列
1 v1
v2 v3
2 v2 v7 v8
v1 v4 v5
3 V3
v1 v6 v7
v6
4 V4
v2 v8
5 v5
v2 v8
v1 v2 v3 v4 v5 v6 v7 v8
6 v6
v3 v7
7 v7
v3 v6
8 v8
v4 v5

0
队列
1 v1
v2 v3
2 v2 v7 v8
v1 v4 v5
3 V3
v1 v6 v7
v6
4 V4
v2 v8
5 v5
v2 v8
v1 v2 v3 v4 v5 v6 v7 v8
6 v6
v3 v7
7 v7 V6的邻接点v3、
v3 v6
v7已经被访问过
不再访问
8 v8
v4 v5

0
队列
1 v1
v2 v3
2 v2 v7 v8
v1 v4 v5
3 V3
v1 v6 v7
4 V4
v2 v8
5 v5
v2 v8
v1 v2 v3 v4 v5 v6 v7 v8
6 v6
v3 v7
7 v7
v3 v6
8 v8
v4 v5

0
队列
1 v1
v2 v3
2 v2 v8
v1 v4 v5
3 V3
v1 v6 v7
v7
4 V4
v2 v8
5 v5
v2 v8
v1 v2 v3 v4 v5 v6 v7 v8
6 v6
v3 v7
7 v7
v3 v6
8 v8
v4 v5

0
队列
1 v1
v2 v3
2 v2 v8
v1 v4 v5
3 V3
v1 v6 v7
v7
4 V4
v2 v8
5 v5
v2 v8
v1 v2 v3 v4 v5 v6 v7 v8
6 v6
v3 v7
7 v7 V7的邻接点v3、
v3 v6
v6已经被访问过
不再访问
8 v8
v4 v5

0
队列
1 v1
v2 v3
2 v2 v8
v1 v4 v5
3 V3
v1 v6 v7
4 V4
v2 v8
5 v5
v2 v8
v1 v2 v3 v4 v5 v6 v7 v8
6 v6
v3 v7
7 v7
v3 v6
8 v8
v4 v5

0
队列
1 v1
v2 v3
2 v2
v1 v4 v5
3 V3
v1 v6 v7
v8
4 V4
v2 v8
5 v5
v2 v8
v1 v2 v3 v4 v5 v6 v7 v8
6 v6
v3 v7
7 v7 V8的邻接点v4、
v3 v6
v5已经被访问过
不再访问
8 v8
v4 v5

0
队列
1 v1
v2 v3
2 v2
v1 v4 v5
队列为空，算法结束
3 V3
v1 v6 v7
4 V4
v2 v8
5 v5
v2 v8
v1 v2 v3 v4 v5 v6 v7 v8
6 v6
v3 v7
7 v7
v3 v6
8 v8
v4 v5

算法实现
3.
从演示过程可以看出，我们必须知道顶点
是否已经被访问过。在具体实现时，我们
用一个数组visited[]来记录顶点是否被访问
过。如果visited[i]的值为True，则顶点vi已
经被访问，否则没有被访问。

算法实现
3.
Void BFS（Graph G，int x）
{
Visited[100]={False}；//假设图中顶点数没有超过100个
Visited[x]=True；cout<<x;Queue.push(x);
While(!Q.empty())
{
V= Queue.front();
Queue.pop();
For(v的每个邻接点w）
If（visited[w]==false)
{
Visited[w]=True;cout<<w;Queue.push（w）；
}
}
}

当图的存储结构为邻接表时，广度优先算法可以表示如下：
void BFS (ALGraph mg,int x)
{
bool visited[100]={false};
queue<int> q;
cout<<mg.vexs[x].data <<" ";visited[x]=true;q.push(x);
while(q.empty()==false){
int v=q.front();
q.pop();
for(int w=::FirstAdjVex(mg,v);w>0;w=::NextAdjVex(mg,v,w)){
if(visited[w]==false){
cout<<mg.vexs[w].data<<" ";
visited[w]=true;
q.push(w);
}
}
}
}

练习题：
对于下面一个图及其存储结构，写出以
v2、v8为起始点的广度优先遍历序列。

0
例图及其邻接表表示
1 v1
v2 v3
v1
2 v2
v1 v4 v5
3 V3
v1 v6 v7
v2
v3
4 V4
v2 v8
v4
v5 v6 v7
5 v5
v2 v8
6 v6
v3 v7
v8
7 v7
v3 v6
8 v8
v4 v5

答案如下：
以v2为起始点：v2-v1-v4-v5-v3-v8-v6-v7
以v8为起始点：v8-v4-v5-v2-v1-v3-v6-v7

思考题：
若图不是连通图，如何进行广度优先遍历？
v1 v2
v6 v7
v3
v4 v5
```
