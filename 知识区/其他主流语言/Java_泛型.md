# Java 泛型

## 定义
Java泛型（Generics）是JDK 5引入的特性，允许在类、接口和方法中使用类型参数，实现类型参数化，提供编译时类型安全检查，避免类型转换，增强代码复用性。

## 核心内容
**1. 泛型类**
```java
// 定义泛型类
public class Box<T> {
    private T value;
    
    public void set(T value) {
        this.value = value;
    }
    
    public T get() {
        return value;
    }
}

// 使用
Box<Integer> intBox = new Box<>();
intBox.set(10);
Integer val = intBox.get();  // 无需类型转换

Box<String> strBox = new Box<>();
strBox.set("Hello");
```

**2. 泛型接口**
```java
public interface Comparable<T> {
    int compareTo(T other);
}

public class Student implements Comparable<Student> {
    private int score;
    
    @Override
    public int compareTo(Student other) {
        return this.score - other.score;
    }
}
```

**3. 泛型方法**
```java
public class Utils {
    // 泛型方法
    public static <T> void printArray(T[] array) {
        for (T element : array) {
            System.out.println(element);
        }
    }
    
    // 多类型参数
    public static <K, V> void printPair(K key, V value) {
        System.out.println(key + " = " + value);
    }
}

// 使用
Integer[] arr = {1, 2, 3};
Utils.printArray(arr);
Utils.<Integer>printArray(arr);  // 显式指定类型
```

**4. 类型边界（Bounded Type Parameters）**
```java
// 上界：T必须是Number或其子类
public class Calculator<T extends Number> {
    public double sum(T a, T b) {
        return a.doubleValue() + b.doubleValue();
    }
}

Calculator<Integer> intCalc = new Calculator<>();
Calculator<Double> doubleCalc = new Calculator<>();
// Calculator<String> strCalc = new Calculator<>();  // 错误

// 多重边界
public <T extends Comparable<T> & Serializable> void process(T item) {
    // T必须实现Comparable和Serializable
}
```

**5. 通配符（Wildcards）**
```java
// 无界通配符 ?
public void printList(List<?> list) {
    for (Object obj : list) {
        System.out.println(obj);
    }
}

// 上界通配符 ? extends
public double sum(List<? extends Number> list) {
    double total = 0;
    for (Number num : list) {
        total += num.doubleValue();
    }
    return total;
}
// 可以读取（作为Number），不能写入

// 下界通配符 ? super
public void addNumbers(List<? super Integer> list) {
    list.add(1);
    list.add(2);
}
// 可以写入Integer，读取为Object
```

**6. PECS原则（Producer Extends, Consumer Super）**
```java
// Producer（生产者）：只读取，用extends
public void copy(List<? extends T> src, List<T> dest) {
    for (T item : src) {  // 读取
        dest.add(item);
    }
}

// Consumer（消费者）：只写入，用super
public void fill(List<? super T> list, T value) {
    list.add(value);  // 写入
}
```

**7. 类型擦除（Type Erasure）**
```java
// 编译前
List<Integer> intList = new ArrayList<>();
List<String> strList = new ArrayList<>();

// 编译后（类型擦除）
List intList = new ArrayList();
List strList = new ArrayList();

// 无法获取泛型类型
// T t = new T();  // 错误
// T[] arr = new T[10];  // 错误

// 运行时类型相同
System.out.println(intList.getClass() == strList.getClass());  // true
```

**8. 泛型与数组**
```java
// 不能创建泛型数组
// List<String>[] array = new List<String>[10];  // 错误

// 可以使用ArrayList
List<List<String>> listOfLists = new ArrayList<>();

// 或类型擦除
List<String>[] array = (List<String>[]) new List[10];  // 未检查警告
```

## 应用场景
- 集合框架：ArrayList<T>、HashMap<K,V>
- 自定义容器类：栈、队列、树等数据结构
- 工具类：Collections、Arrays等通用方法
- DAO层：通用数据访问对象
- 框架开发：Spring、Hibernate等

## 注意事项
- 泛型信息在运行时被擦除（无法用instanceof检查）
- 不能创建泛型数组
- 静态方法不能使用类的类型参数
- 基本类型不能作为类型参数（用包装类）
- 泛型不支持协变（List<String>不是List<Object>的子类）
- 注意通配符的读写限制

## 关联知识
与 [[Java_集合框架]]、[[Java_接口]]、[[C++_模板]] 相关。
