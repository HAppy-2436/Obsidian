# JavaScript 事件循环

## 定义
事件循环（Event Loop）是JavaScript处理异步操作的核心机制，通过调用栈（Call Stack）、任务队列（Task Queue）、微任务队列（Microtask Queue）协调同步和异步代码的执行顺序，实现单线程非阻塞。

## 核心内容
**1. 执行模型**
```
┌───────────────────────┐
│   Call Stack          │ 同步代码执行
│   (调用栈)            │
└───────────────────────┘
           ↓
┌───────────────────────┐
│   Microtask Queue     │ Promise、MutationObserver
│   (微任务队列)         │ 优先级高
└───────────────────────┘
           ↓
┌───────────────────────┐
│   Macrotask Queue     │ setTimeout、setInterval
│   (宏任务队列)         │ I/O、UI渲染
└───────────────────────┘
```

**2. 执行顺序示例**
```javascript
console.log('1');  // 同步

setTimeout(() => {
    console.log('2');  // 宏任务
}, 0);

Promise.resolve().then(() => {
    console.log('3');  // 微任务
});

console.log('4');  // 同步

// 输出顺序：1, 4, 3, 2
// 执行顺序：同步代码 → 微任务 → 宏任务
```

**3. 详细执行流程**
```javascript
console.log('Start');

setTimeout(() => {
    console.log('Timeout 1');
    Promise.resolve().then(() => {
        console.log('Promise in Timeout 1');
    });
}, 0);

Promise.resolve()
    .then(() => {
        console.log('Promise 1');
        setTimeout(() => {
            console.log('Timeout in Promise 1');
        }, 0);
    })
    .then(() => {
        console.log('Promise 2');
    });

setTimeout(() => {
    console.log('Timeout 2');
}, 0);

console.log('End');

/* 输出：
Start
End
Promise 1
Promise 2
Timeout 1
Promise in Timeout 1
Timeout 2
Timeout in Promise 1
*/
```

**4. 宏任务（Macrotask）**
```javascript
// setTimeout
setTimeout(() => {
    console.log('setTimeout');
}, 0);

// setInterval
const timer = setInterval(() => {
    console.log('setInterval');
}, 1000);

// setImmediate（Node.js）
setImmediate(() => {
    console.log('setImmediate');
});

// I/O操作
fs.readFile('file.txt', (err, data) => {
    console.log('File read');
});

// UI渲染
requestAnimationFrame(() => {
    console.log('Animation frame');
});
```

**5. 微任务（Microtask）**
```javascript
// Promise
Promise.resolve().then(() => {
    console.log('Promise microtask');
});

// async/await
async function test() {
    console.log('1');
    await Promise.resolve();
    console.log('2');  // 微任务
}

// MutationObserver
const observer = new MutationObserver(() => {
    console.log('DOM changed');
});

// queueMicrotask（现代浏览器）
queueMicrotask(() => {
    console.log('Microtask');
});

// process.nextTick（Node.js，优先级最高）
process.nextTick(() => {
    console.log('nextTick');
});
```

**6. async/await与事件循环**
```javascript
async function async1() {
    console.log('async1 start');
    await async2();
    console.log('async1 end');  // 微任务
}

async function async2() {
    console.log('async2');
}

console.log('script start');

setTimeout(() => {
    console.log('setTimeout');
}, 0);

async1();

new Promise(resolve => {
    console.log('promise1');
    resolve();
}).then(() => {
    console.log('promise2');
});

console.log('script end');

/* 输出：
script start
async1 start
async2
promise1
script end
async1 end
promise2
setTimeout
*/
```

**7. 经典面试题**
```javascript
setTimeout(() => console.log('1'), 0);
Promise.resolve().then(() => console.log('2'));
Promise.resolve().then(() => {
    console.log('3');
    setTimeout(() => console.log('4'), 0);
});
Promise.resolve().then(() => console.log('5'));
setTimeout(() => console.log('6'), 0);
console.log('7');

// 输出：7, 2, 3, 5, 1, 6, 4
```

**8. Node.js事件循环（6个阶段）**
```
   ┌───────────────────────┐
┌─>│        timers         │ setTimeout/setInterval
│  └───────────┬───────────┘
│  ┌───────────┴───────────┐
│  │   pending callbacks   │ I/O回调
│  └───────────┬───────────┘
│  ┌───────────┴───────────┐
│  │       idle, prepare   │ 内部使用
│  └───────────┬───────────┘
│  ┌───────────┴───────────┐
│  │         poll          │ 获取新I/O事件
│  └───────────┬───────────┘
│  ┌───────────┴───────────┐
│  │         check         │ setImmediate
│  └───────────┬───────────┘
│  ┌───────────┴───────────┐
└──│    close callbacks    │ socket.on('close')
   └───────────────────────┘
```

## 应用场景
- 异步请求：Ajax、Fetch API
- 定时器：setTimeout、setInterval
- 事件处理：点击、滚动等DOM事件
- Promise链：异步流程控制
- 动画：requestAnimationFrame
- I/O操作：文件读写、网络通信

## 注意事项
- 微任务优先级高于宏任务
- 每个宏任务执行完后，清空所有微任务
- setTimeout(fn, 0)不是立即执行，最小延迟4ms
- 长时间同步代码会阻塞事件循环
- Promise的executor是同步执行的
- await后面的代码相当于then回调

## 关联知识
与 [[JavaScript_Promise]]、[[JavaScript_闭包]]、[[Java_多线程]] 相关。
