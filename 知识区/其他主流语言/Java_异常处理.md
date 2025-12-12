# Java 异常处理

## 定义
Java异常处理是一种处理程序运行时错误的机制，通过try-catch-finally、throw、throws等关键字捕获和处理异常，分为检查型异常（Checked）和非检查型异常（Unchecked），保证程序健壮性。

## 核心内容
**1. 异常体系**
```
Throwable
├── Error（严重错误，不应捕获）
│   ├── OutOfMemoryError
│   ├── StackOverflowError
│   └── VirtualMachineError
└── Exception
    ├── RuntimeException（非检查型异常）
    │   ├── NullPointerException
    │   ├── ArrayIndexOutOfBoundsException
    │   ├── ArithmeticException
    │   └── ClassCastException
    └── IOException（检查型异常）
        ├── FileNotFoundException
        ├── SQLException
        └── ...
```

**2. try-catch-finally**
```java
try {
    int result = 10 / 0;  // 可能抛异常的代码
    String s = null;
    s.length();
} catch (ArithmeticException e) {
    System.out.println("算术异常：" + e.getMessage());
} catch (NullPointerException e) {
    System.out.println("空指针异常");
} finally {
    // 总是执行（即使有return）
    System.out.println("清理资源");
}

// 多异常捕获（Java 7）
try {
    // ...
} catch (IOException | SQLException e) {
    System.out.println("IO或SQL异常");
}
```

**3. throw 和 throws**
```java
// throw：手动抛出异常
public void withdraw(double amount) {
    if (amount <= 0) {
        throw new IllegalArgumentException("金额必须大于0");
    }
    if (amount > balance) {
        throw new RuntimeException("余额不足");
    }
    balance -= amount;
}

// throws：声明方法可能抛出的异常
public void readFile(String path) throws IOException {
    FileReader fr = new FileReader(path);  // 可能抛IOException
    // ...
    fr.close();
}

// 调用时必须处理
try {
    readFile("test.txt");
} catch (IOException e) {
    e.printStackTrace();
}
```

**4. 自定义异常**
```java
// 检查型异常（继承Exception）
public class InsufficientFundsException extends Exception {
    private double amount;
    
    public InsufficientFundsException(double amount) {
        super("余额不足，需要：" + amount);
        this.amount = amount;
    }
    
    public double getAmount() {
        return amount;
    }
}

// 非检查型异常（继承RuntimeException）
public class InvalidAgeException extends RuntimeException {
    public InvalidAgeException(String message) {
        super(message);
    }
}

// 使用
public void withdraw(double amount) throws InsufficientFundsException {
    if (amount > balance) {
        throw new InsufficientFundsException(amount - balance);
    }
    balance -= amount;
}
```

**5. try-with-resources（Java 7）**
```java
// 自动关闭资源（实现AutoCloseable接口）
try (FileReader fr = new FileReader("test.txt");
     BufferedReader br = new BufferedReader(fr)) {
    String line = br.readLine();
} catch (IOException e) {
    e.printStackTrace();
}
// 自动调用close()，无需finally

// 自定义资源类
class MyResource implements AutoCloseable {
    public void doWork() {
        System.out.println("Working...");
    }
    
    @Override
    public void close() {
        System.out.println("Resource closed");
    }
}

try (MyResource res = new MyResource()) {
    res.doWork();
}
```

**6. 异常链**
```java
try {
    // 底层操作
    throw new SQLException("数据库连接失败");
} catch (SQLException e) {
    // 包装为业务异常
    throw new RuntimeException("操作失败", e);  // 保留原始异常
}

// 获取原因
catch (RuntimeException e) {
    Throwable cause = e.getCause();  // SQLException
    System.out.println(cause.getMessage());
}
```

**7. 常见异常处理模式**
```java
// 记录日志并重新抛出
try {
    // ...
} catch (Exception e) {
    logger.error("操作失败", e);
    throw e;
}

// 转换异常类型
try {
    // ...
} catch (IOException e) {
    throw new RuntimeException("文件操作失败", e);
}

// 默认值处理
public int parse(String str) {
    try {
        return Integer.parseInt(str);
    } catch (NumberFormatException e) {
        return 0;  // 返回默认值
    }
}

// 清理资源
Connection conn = null;
try {
    conn = getConnection();
    // 使用连接
} catch (SQLException e) {
    // 处理异常
} finally {
    if (conn != null) {
        try {
            conn.close();
        } catch (SQLException e) {
            // 记录关闭失败
        }
    }
}
```

**8. 检查型 vs 非检查型**
| 类型 | 继承自 | 编译检查 | 处理方式 | 示例 |
|------|--------|----------|----------|------|
| 检查型 | Exception | 必须处理 | try-catch或throws | IOException |
| 非检查型 | RuntimeException | 不强制 | 可选处理 | NullPointerException |

## 应用场景
- 文件操作：IOException处理
- 网络通信：超时、连接失败
- 数据库操作：SQLException
- 业务逻辑：自定义业务异常
- 参数校验：IllegalArgumentException
- 资源管理：try-with-resources

## 注意事项
- 不要捕获Error（如OutOfMemoryError）
- 不要使用空catch块（至少记录日志）
- 不要过度使用异常（正常流程不应抛异常）
- finally中避免return（会覆盖try/catch的return）
- 优先使用标准异常（IllegalArgumentException等）
- 异常信息要清晰明确

## 关联知识
与 [[Java_面向对象]]、[[Java_接口]]、[[文件操作]] 相关。
