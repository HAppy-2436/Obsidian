# volatile关键字

## 定义
volatile是类型限定符，告知编译器该变量可能被程序外部因素（硬件、中断、其他线程）随时改变，禁止编译器对该变量进行优化，每次访问必须从内存重新读取。

## 核心内容
**1. 基本用法**
```c
volatile int flag = 0; // 声明易变变量
volatile unsigned int *port = (unsigned int *)0x40000000; // 硬件寄存器映射
```

**2. volatile作用示例**
```c
// 无volatile - 编译器优化
int flag = 0;
while (flag == 0) {
    // 编译器可能优化为：if (flag == 0) while(1);
}

// 有volatile - 每次从内存读取
volatile int flag = 0;
while (flag == 0) {
    // 每次循环都重新读取flag的值
}
```

**3. volatile指针**
```c
volatile int *p;           // 指向volatile变量的指针
int volatile *p;           // 同上
int *volatile p;           // volatile指针（指针本身是volatile）
volatile int *volatile p;  // 都是volatile
```

**4. 典型应用场景**
- **硬件寄存器**：GPIO、UART、定时器等外设寄存器
- **中断服务程序**：ISR中修改的全局变量
- **多线程共享变量**：防止编译器缓存优化
- **内存映射IO**：MMIO地址空间

**5. volatile vs const**
```c
volatile const int status_reg; // 只读但会变化的硬件寄存器
```

## 应用场景
- 嵌入式系统：操作外设寄存器（ADC、GPIO、DMA控制器）
- 中断编程：主函数与ISR之间的标志变量
- 多线程同步：轻量级标志位（不保证原子性）
- 调试：防止优化导致观察不到变量变化

## 注意事项
- volatile不保证原子性，多线程需额外同步机制
- volatile不能防止指令重排序
- 过度使用会降低性能（禁止优化）
- volatile不能替代互斥锁或原子操作
- 读-改-写操作（i++）不是原子的

## 关联知识
与 [[指针]]、[[内存布局]]、[[静态变量]] 相关。
