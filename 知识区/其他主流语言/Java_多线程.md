# Java 多线程

## 定义
Java多线程是指在同一程序中同时执行多个线程，每个线程独立执行不同任务。通过Thread类、Runnable接口、线程池等机制实现并发编程，需要处理线程同步、通信和安全问题。

## 核心内容
**1. 创建线程**
```java
// 方法1：继承Thread类
class MyThread extends Thread {
    public void run() {
        System.out.println("Thread running");
    }
}
MyThread t = new MyThread();
t.start();

// 方法2：实现Runnable接口（推荐）
class MyRunnable implements Runnable {
    public void run() {
        System.out.println("Runnable running");
    }
}
Thread t = new Thread(new MyRunnable());
t.start();

// 方法3：Lambda表达式（Java 8）
Thread t = new Thread(() -> {
    System.out.println("Lambda running");
});
t.start();
```

**2. 线程同步（synchronized）**
```java
class Counter {
    private int count = 0;
    
    // 同步方法
    public synchronized void increment() {
        count++;
    }
    
    // 同步代码块
    public void decrement() {
        synchronized(this) {
            count--;
        }
    }
    
    // 静态同步方法（锁类对象）
    public static synchronized void staticMethod() {
        // ...
    }
}
```

**3. volatile关键字**
```java
class SharedFlag {
    private volatile boolean flag = false;  // 保证可见性
    
    public void setFlag() {
        flag = true;  // 立即写回主内存
    }
    
    public boolean getFlag() {
        return flag;  // 从主内存读取
    }
}
```

**4. wait/notify机制**
```java
class Producer {
    private Queue<Integer> queue;
    private int maxSize;
    
    public synchronized void produce() throws InterruptedException {
        while (queue.size() == maxSize) {
            wait();  // 队列满，等待
        }
        queue.add(1);
        notify();  // 唤醒消费者
    }
}

class Consumer {
    public synchronized void consume() throws InterruptedException {
        while (queue.isEmpty()) {
            wait();  // 队列空，等待
        }
        queue.poll();
        notify();  // 唤醒生产者
    }
}
```

**5. 线程池（ExecutorService）**
```java
import java.util.concurrent.*;

// 固定大小线程池
ExecutorService executor = Executors.newFixedThreadPool(5);

// 提交任务
executor.submit(() -> {
    System.out.println("Task running");
});

// 关闭线程池
executor.shutdown();

// 单线程池
ExecutorService single = Executors.newSingleThreadExecutor();

// 缓存线程池
ExecutorService cached = Executors.newCachedThreadPool();

// 自定义线程池
ThreadPoolExecutor pool = new ThreadPoolExecutor(
    5,     // 核心线程数
    10,    // 最大线程数
    60L,   // 空闲线程存活时间
    TimeUnit.SECONDS,
    new LinkedBlockingQueue<>()
);
```

**6. Lock接口（更灵活的锁）**
```java
import java.util.concurrent.locks.*;

class BankAccount {
    private Lock lock = new ReentrantLock();
    private int balance = 0;
    
    public void deposit(int amount) {
        lock.lock();
        try {
            balance += amount;
        } finally {
            lock.unlock();  // 必须在finally中释放
        }
    }
    
    // 读写锁
    private ReadWriteLock rwLock = new ReentrantReadWriteLock();
    
    public void read() {
        rwLock.readLock().lock();
        try {
            // 多个线程可同时读
        } finally {
            rwLock.readLock().unlock();
        }
    }
    
    public void write() {
        rwLock.writeLock().lock();
        try {
            // 只有一个线程可写
        } finally {
            rwLock.writeLock().unlock();
        }
    }
}
```

**7. 线程状态**
```
NEW → RUNNABLE ↔ RUNNING
         ↓         ↓
      BLOCKED   WAITING
         ↓         ↓
      TIMED_WAITING
         ↓
    TERMINATED
```

**8. 线程安全集合**
```java
// 同步集合
List<Integer> syncList = Collections.synchronizedList(new ArrayList<>());
Map<String, Integer> syncMap = Collections.synchronizedMap(new HashMap<>());

// 并发集合（性能更好）
ConcurrentHashMap<String, Integer> map = new ConcurrentHashMap<>();
CopyOnWriteArrayList<Integer> list = new CopyOnWriteArrayList<>();
BlockingQueue<Integer> queue = new LinkedBlockingQueue<>();
```

## 应用场景
- Web服务器：处理多个客户端请求
- GUI应用：主线程处理UI，工作线程执行耗时操作
- 并发下载：多线程同时下载文件
- 数据处理：并行处理大量数据
- 定时任务：ScheduledExecutorService执行定时任务

## 注意事项
- 避免死锁：多个线程互相等待对方释放锁
- synchronized开销较大，优先考虑无锁方案
- volatile不保证原子性（count++不安全）
- 线程池用完要shutdown，避免资源泄漏
- 不要在synchronized块中调用外部方法
- 优先使用concurrent包下的工具类

## 关联知识
与 [[Java_异常处理]]、[[Java_集合框架]]、[[volatile关键字]] 相关。
