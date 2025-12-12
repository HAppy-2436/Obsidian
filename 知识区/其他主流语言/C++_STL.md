# C++ STL

## 定义
STL（Standard Template Library）是C++标准模板库，提供通用的容器、算法、迭代器和函数对象，基于模板实现，是C++高效编程的核心工具。

## 核心内容
**1. 容器（Containers）**

**顺序容器**
```cpp
#include <vector>
vector<int> vec = {1, 2, 3};
vec.push_back(4);
vec[0] = 10;

#include <list>
list<int> lst = {1, 2, 3};
lst.push_front(0);  // 双向链表

#include <deque>
deque<int> dq;
dq.push_front(1);
dq.push_back(2);
```

**关联容器**
```cpp
#include <map>
map<string, int> m;
m["apple"] = 1;
m["banana"] = 2;

#include <set>
set<int> s = {3, 1, 4, 1, 5};  // 自动排序去重
s.insert(2);

#include <unordered_map>
unordered_map<string, int> um;  // 哈希表，O(1)查找

#include <unordered_set>
unordered_set<int> us;
```

**容器适配器**
```cpp
#include <stack>
stack<int> stk;
stk.push(1);
stk.pop();

#include <queue>
queue<int> q;
q.push(1);
q.pop();

#include <priority_queue>
priority_queue<int> pq;  // 大顶堆
```

**2. 迭代器（Iterators）**
```cpp
vector<int> vec = {1, 2, 3, 4, 5};

// 遍历
for (auto it = vec.begin(); it != vec.end(); ++it) {
    cout << *it << " ";
}

// range-based for（C++11）
for (const auto& val : vec) {
    cout << val << " ";
}

// 反向迭代器
for (auto it = vec.rbegin(); it != vec.rend(); ++it) {
    cout << *it << " ";
}
```

**3. 算法（Algorithms）**
```cpp
#include <algorithm>

vector<int> vec = {3, 1, 4, 1, 5};

// 排序
sort(vec.begin(), vec.end());
sort(vec.begin(), vec.end(), greater<int>());  // 降序

// 查找
auto it = find(vec.begin(), vec.end(), 4);
bool found = binary_search(vec.begin(), vec.end(), 3);

// 计数
int cnt = count(vec.begin(), vec.end(), 1);

// 修改
reverse(vec.begin(), vec.end());
fill(vec.begin(), vec.end(), 0);
transform(vec.begin(), vec.end(), vec.begin(), [](int x) { return x * 2; });

// 最值
auto max_it = max_element(vec.begin(), vec.end());
auto min_it = min_element(vec.begin(), vec.end());

// 去重
sort(vec.begin(), vec.end());
vec.erase(unique(vec.begin(), vec.end()), vec.end());
```

**4. 函数对象与Lambda**
```cpp
// 函数对象
struct Compare {
    bool operator()(int a, int b) {
        return a > b;
    }
};
sort(vec.begin(), vec.end(), Compare());

// Lambda表达式（C++11）
sort(vec.begin(), vec.end(), [](int a, int b) { return a > b; });

// 谓词
auto it = find_if(vec.begin(), vec.end(), [](int x) { return x > 3; });
```

**5. 常用操作示例**
```cpp
// vector操作
vector<int> v;
v.push_back(1);
v.pop_back();
v.insert(v.begin(), 0);
v.erase(v.begin());
v.clear();
int size = v.size();
bool empty = v.empty();

// map操作
map<string, int> m;
m["key"] = 10;
if (m.count("key")) { /* 存在 */ }
m.erase("key");
for (const auto& [key, val] : m) {  // C++17
    cout << key << ": " << val << endl;
}

// set操作
set<int> s;
s.insert(5);
s.erase(5);
auto it = s.find(3);
```

**6. 容器选择指南**
| 需求 | 推荐容器 |
|------|----------|
| 动态数组 | vector |
| 频繁头部插入删除 | deque, list |
| 键值映射 | map(有序), unordered_map(无序) |
| 去重集合 | set(有序), unordered_set(无序) |
| 先进后出 | stack |
| 先进先出 | queue |
| 优先级队列 | priority_queue |

## 应用场景
- 数据结构：用vector替代数组，map存储映射关系
- 算法竞赛：STL算法提高编码效率
- 排序搜索：sort、binary_search等
- 图算法：用vector<vector<int>>表示邻接表
- 字符串处理：配合string类

## 注意事项
- vector的push_back可能触发扩容（预留空间用reserve）
- map/set基于红黑树，O(log n)；unordered基于哈希，O(1)
- 迭代器失效：插入删除可能导致迭代器失效
- 不要对空容器使用front()、back()
- algorithm头文件的函数都需要迭代器范围
- 使用const引用避免拷贝：`const auto&`

## 关联知识
与 [[C++_模板]]、[[C++_智能指针]]、[[C++_引用]] 相关。
