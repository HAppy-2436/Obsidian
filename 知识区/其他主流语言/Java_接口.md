# Java 接口

## 定义
接口（Interface）是Java中定义行为规范的抽象类型，包含抽象方法（Java 8后可有默认方法）、常量定义，类通过implements实现接口必须重写所有抽象方法，支持多继承，实现解耦和多态。

## 核心内容
**1. 接口定义**
```java
public interface Animal {
    // 抽象方法（默认public abstract）
    void eat();
    void sleep();
    
    // 常量（默认public static final）
    int MAX_AGE = 100;
    String TYPE = "Mammal";
}

// 实现接口
public class Dog implements Animal {
    @Override
    public void eat() {
        System.out.println("Dog eats");
    }
    
    @Override
    public void sleep() {
        System.out.println("Dog sleeps");
    }
}
```

**2. 多接口实现**
```java
interface Flyable {
    void fly();
}

interface Swimmable {
    void swim();
}

// 实现多个接口
class Duck implements Flyable, Swimmable {
    public void fly() {
        System.out.println("Duck flies");
    }
    
    public void swim() {
        System.out.println("Duck swims");
    }
}
```

**3. 接口继承**
```java
interface Vehicle {
    void move();
}

interface Car extends Vehicle {
    void drive();
}

interface ElectricCar extends Car {
    void charge();
}

// 实现时需重写所有方法
class Tesla implements ElectricCar {
    public void move() { }
    public void drive() { }
    public void charge() { }
}
```

**4. 默认方法（Java 8）**
```java
interface MyInterface {
    // 抽象方法
    void abstractMethod();
    
    // 默认方法（有实现）
    default void defaultMethod() {
        System.out.println("Default implementation");
    }
    
    // 静态方法
    static void staticMethod() {
        System.out.println("Static method");
    }
}

class MyClass implements MyInterface {
    public void abstractMethod() {
        // 必须实现
    }
    // defaultMethod可选择性重写
}

// 使用
MyInterface.staticMethod();  // 直接调用静态方法
```

**5. 函数式接口（Java 8）**
```java
// 只有一个抽象方法的接口
@FunctionalInterface
interface Calculator {
    int calculate(int a, int b);
}

// Lambda表达式实现
Calculator add = (a, b) -> a + b;
Calculator multiply = (a, b) -> a * b;

System.out.println(add.calculate(5, 3));  // 8

// 常用函数式接口
Runnable r = () -> System.out.println("Run");
Comparator<Integer> cmp = (a, b) -> a - b;
Predicate<String> isEmpty = s -> s.isEmpty();
Function<String, Integer> length = s -> s.length();
```

**6. 接口 vs 抽象类**
| 特性 | 接口 | 抽象类 |
|------|------|--------|
| 继承 | 多继承 | 单继承 |
| 方法 | 抽象+默认+静态 | 抽象+具体 |
| 变量 | 只能常量 | 任意变量 |
| 构造器 | 无 | 有 |
| 访问修饰符 | public | 任意 |
| 用途 | 定义规范 | 代码复用 |

**7. 标记接口（Marker Interface）**
```java
// 无方法的接口，仅作标记
interface Serializable {
    // 空接口
}

class User implements Serializable {
    // 表明User可序列化
}

// JVM识别标记接口
if (obj instanceof Serializable) {
    // 执行序列化
}
```

**8. 常见接口应用**
```java
// Comparable接口
class Student implements Comparable<Student> {
    int score;
    
    public int compareTo(Student other) {
        return this.score - other.score;
    }
}

// Comparator接口
Comparator<Student> byName = new Comparator<Student>() {
    public int compare(Student s1, Student s2) {
        return s1.name.compareTo(s2.name);
    }
};

// Iterable接口
class MyCollection implements Iterable<Integer> {
    public Iterator<Integer> iterator() {
        return new MyIterator();
    }
}
```

## 应用场景
- 定义规范：DAO接口、Service接口
- 回调机制：事件监听器接口
- 策略模式：定义不同算法接口
- 适配器模式：统一不同类的接口
- 依赖注入：Spring框架中的接口注入
- 多态：面向接口编程

## 注意事项
- 接口中的方法默认是public abstract
- 接口中的变量默认是public static final
- Java 8前接口只能有抽象方法和常量
- 实现类必须实现所有抽象方法（除非也是抽象类）
- 接口不能实例化
- 优先使用接口而非抽象类（组合优于继承）

## 关联知识
与 [[Java_面向对象]]、[[Java_泛型]]、[[Java_集合框架]] 相关。
