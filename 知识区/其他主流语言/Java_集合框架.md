# Java 集合框架

## 定义
Java集合框架（Java Collections Framework）是一套用于存储和操作对象的标准接口和实现类，提供List、Set、Map等数据结构，统一的操作接口和高效的算法实现。

## 核心内容
**1. 集合框架体系**
```
Collection
├── List（有序，可重复）
│   ├── ArrayList（动态数组）
│   ├── LinkedList（双向链表）
│   └── Vector（线程安全）
├── Set（无序，不重复）
│   ├── HashSet（哈希表）
│   ├── LinkedHashSet（保持插入顺序）
│   └── TreeSet（红黑树，有序）
└── Queue（队列）
    ├── PriorityQueue（优先队列）
    └── Deque（双端队列）

Map（键值对）
├── HashMap（哈希表）
├── LinkedHashMap（保持插入顺序）
├── TreeMap（红黑树，有序）
└── Hashtable（线程安全，过时）
```

**2. List接口**
```java
// ArrayList（最常用）
List<String> list = new ArrayList<>();
list.add("apple");
list.add(0, "banana");  // 指定位置插入
list.get(0);
list.set(0, "orange");
list.remove(0);
list.size();
list.contains("apple");

// LinkedList（频繁插入删除）
LinkedList<Integer> linked = new LinkedList<>();
linked.addFirst(1);
linked.addLast(3);
linked.removeFirst();

// 遍历
for (String item : list) {
    System.out.println(item);
}

// 迭代器
Iterator<String> it = list.iterator();
while (it.hasNext()) {
    System.out.println(it.next());
}
```

**3. Set接口**
```java
// HashSet（无序，O(1)）
Set<Integer> set = new HashSet<>();
set.add(1);
set.add(2);
set.add(1);  // 重复元素不会添加
System.out.println(set.size());  // 2

// TreeSet（有序，O(log n)）
TreeSet<String> treeSet = new TreeSet<>();
treeSet.add("c");
treeSet.add("a");
treeSet.add("b");
// 输出：a, b, c（自动排序）

// LinkedHashSet（保持插入顺序）
Set<String> linkedSet = new LinkedHashSet<>();
```

**4. Map接口**
```java
// HashMap（最常用）
Map<String, Integer> map = new HashMap<>();
map.put("apple", 1);
map.put("banana", 2);
map.get("apple");  // 1
map.containsKey("apple");  // true
map.remove("banana");
map.size();

// 遍历
for (Map.Entry<String, Integer> entry : map.entrySet()) {
    System.out.println(entry.getKey() + " = " + entry.getValue());
}

// 只遍历键
for (String key : map.keySet()) {
    System.out.println(key);
}

// 只遍历值
for (Integer value : map.values()) {
    System.out.println(value);
}

// TreeMap（有序）
TreeMap<Integer, String> treeMap = new TreeMap<>();

// LinkedHashMap（保持插入顺序）
Map<String, Integer> linkedMap = new LinkedHashMap<>();
```

**5. Queue接口**
```java
// 普通队列
Queue<Integer> queue = new LinkedList<>();
queue.offer(1);  // 入队
queue.poll();    // 出队
queue.peek();    // 查看队首

// 优先队列（小顶堆）
PriorityQueue<Integer> pq = new PriorityQueue<>();
pq.offer(3);
pq.offer(1);
pq.offer(2);
pq.poll();  // 1（最小值）

// 大顶堆
PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());

// Deque（双端队列）
Deque<Integer> deque = new ArrayDeque<>();
deque.addFirst(1);
deque.addLast(2);
deque.removeFirst();
```

**6. Collections工具类**
```java
List<Integer> list = new ArrayList<>();

// 排序
Collections.sort(list);
Collections.sort(list, Collections.reverseOrder());

// 查找
int index = Collections.binarySearch(list, 5);
int max = Collections.max(list);
int min = Collections.min(list);

// 反转
Collections.reverse(list);

// 打乱
Collections.shuffle(list);

// 填充
Collections.fill(list, 0);

// 不可修改集合
List<Integer> unmodifiable = Collections.unmodifiableList(list);

// 同步集合
List<Integer> syncList = Collections.synchronizedList(list);
```

**7. 性能对比**
| 操作 | ArrayList | LinkedList | HashSet | TreeSet | HashMap | TreeMap |
|------|-----------|------------|---------|---------|---------|---------|
| 添加 | O(1) | O(1) | O(1) | O(log n) | O(1) | O(log n) |
| 删除 | O(n) | O(1)* | O(1) | O(log n) | O(1) | O(log n) |
| 查找 | O(1)索引 | O(n) | O(1) | O(log n) | O(1) | O(log n) |
| 遍历 | 快 | 慢 | 快 | 中 | 快 | 中 |

## 应用场景
- ArrayList：动态数组，随机访问
- LinkedList：频繁插入删除
- HashSet：去重、快速查找
- TreeSet：有序集合、范围查询
- HashMap：键值映射、缓存
- PriorityQueue：优先级调度、Dijkstra算法

## 注意事项
- ArrayList扩容时会拷贝数组（预分配用ensureCapacity）
- HashMap非线程安全（多线程用ConcurrentHashMap）
- 遍历时不要用add/remove（用Iterator.remove()）
- TreeSet/TreeMap的元素必须实现Comparable或提供Comparator
- HashMap的key要正确重写hashCode和equals
- 优先使用接口类型声明：`List<> list = new ArrayList<>()`

## 关联知识
与 [[Java_泛型]]、[[Java_接口]]、[[Java_多线程]] 相关。
