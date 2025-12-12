# Java 面向对象

## 定义
Java面向对象编程（OOP）是一种以对象为中心的编程范式，通过类、对象、封装、继承、多态三大特性，将现实世界抽象为程序模型，提高代码复用性和可维护性。

## 核心内容
**1. 类与对象**
```java
// 类定义
public class Person {
    // 成员变量（属性）
    private String name;
    private int age;
    
    // 构造器
    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }
    
    // 方法
    public void sayHello() {
        System.out.println("Hello, I'm " + name);
    }
    
    // getter/setter
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
}

// 创建对象
Person p = new Person("Alice", 20);
p.sayHello();
```

**2. 封装（Encapsulation）**
```java
public class BankAccount {
    // 私有变量，外部不可直接访问
    private double balance;
    
    // 公有方法控制访问
    public void deposit(double amount) {
        if (amount > 0) {
            balance += amount;
        }
    }
    
    public boolean withdraw(double amount) {
        if (amount > 0 && amount <= balance) {
            balance -= amount;
            return true;
        }
        return false;
    }
    
    public double getBalance() {
        return balance;
    }
}
```

**3. 继承（Inheritance）**
```java
// 父类
public class Animal {
    protected String name;
    
    public void eat() {
        System.out.println(name + " is eating");
    }
}

// 子类继承父类
public class Dog extends Animal {
    private String breed;
    
    // 重写父类方法
    @Override
    public void eat() {
        System.out.println(name + " (dog) is eating");
    }
    
    // 子类特有方法
    public void bark() {
        System.out.println("Woof!");
    }
}

// 使用
Dog dog = new Dog();
dog.name = "Buddy";
dog.eat();   // 调用重写的方法
dog.bark();  // 调用子类方法
```

**4. 多态（Polymorphism）**
```java
// 编译时多态（方法重载）
public class Calculator {
    public int add(int a, int b) {
        return a + b;
    }
    
    public double add(double a, double b) {
        return a + b;
    }
    
    public int add(int a, int b, int c) {
        return a + b + c;
    }
}

// 运行时多态（方法重写）
Animal animal1 = new Dog();    // 向上转型
Animal animal2 = new Cat();
animal1.eat();  // 调用Dog的eat()
animal2.eat();  // 调用Cat的eat()

// 多态数组
Animal[] animals = {new Dog(), new Cat(), new Bird()};
for (Animal a : animals) {
    a.eat();  // 各自调用重写的方法
}
```

**5. 访问修饰符**
| 修饰符 | 类内部 | 同包 | 子类 | 其他 |
|--------|--------|------|------|------|
| private | ✓ | ✗ | ✗ | ✗ |
| default | ✓ | ✓ | ✗ | ✗ |
| protected | ✓ | ✓ | ✓ | ✗ |
| public | ✓ | ✓ | ✓ | ✓ |

**6. static与final**
```java
public class MathUtils {
    // 静态变量（类变量）
    public static final double PI = 3.14159;
    private static int count = 0;
    
    // 静态方法
    public static int add(int a, int b) {
        return a + b;
    }
    
    // 静态代码块
    static {
        System.out.println("Class loaded");
    }
}

// 使用
double pi = MathUtils.PI;
int sum = MathUtils.add(3, 5);

// final类（不可继承）
public final class ImmutableClass { }

// final方法（不可重写）
public final void finalMethod() { }

// final变量（常量）
public final int MAX_SIZE = 100;
```

**7. 抽象类**
```java
public abstract class Shape {
    protected String color;
    
    // 抽象方法（无实现）
    public abstract double area();
    
    // 具体方法（有实现）
    public void setColor(String color) {
        this.color = color;
    }
}

public class Circle extends Shape {
    private double radius;
    
    @Override
    public double area() {
        return Math.PI * radius * radius;
    }
}

// 不能实例化抽象类
// Shape s = new Shape();  // 错误
Shape s = new Circle();    // 正确
```

**8. 内部类**
```java
public class Outer {
    private int data = 10;
    
    // 成员内部类
    class Inner {
        void display() {
            System.out.println(data);  // 访问外部类成员
        }
    }
    
    // 静态内部类
    static class StaticInner {
        void show() {
            System.out.println("Static inner");
        }
    }
    
    // 局部内部类
    void method() {
        class LocalInner {
            void print() { }
        }
    }
    
    // 匿名内部类
    Runnable r = new Runnable() {
        public void run() {
            System.out.println("Anonymous");
        }
    };
}
```

## 应用场景
- 软件建模：将现实对象抽象为类
- 代码复用：通过继承复用父类代码
- 框架设计：使用多态实现可扩展架构
- 设计模式：工厂、单例、观察者等
- 大型项目：模块化、分层设计

## 注意事项
- Java不支持多继承（但可实现多接口）
- 重写方法不能降低访问权限
- 构造器不能被继承和重写
- 静态方法不能被重写（可以被隐藏）
- 优先使用组合而非继承
- 遵循单一职责原则

## 关联知识
与 [[Java_接口]]、[[Java_泛型]]、[[Java_异常处理]] 相关。
