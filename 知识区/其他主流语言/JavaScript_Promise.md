# JavaScript Promise

## 定义
Promise是JavaScript处理异步操作的对象，代表一个尚未完成但预期将来会完成的操作，有pending（进行中）、fulfilled（成功）、rejected（失败）三种状态，通过then、catch、finally方法处理结果，配合async/await使用更简洁。

## 核心内容
**1. Promise基础**
```javascript
// 创建Promise
const promise = new Promise((resolve, reject) => {
    // 异步操作
    setTimeout(() => {
        const success = true;
        if (success) {
            resolve('成功');  // 状态变为fulfilled
        } else {
            reject('失败');   // 状态变为rejected
        }
    }, 1000);
});

// 处理结果
promise
    .then(result => {
        console.log(result);  // '成功'
    })
    .catch(error => {
        console.error(error);  // '失败'
    })
    .finally(() => {
        console.log('完成');  // 无论成功失败都执行
    });
```

**2. 三种状态**
```javascript
// pending（进行中）
const p1 = new Promise((resolve, reject) => {
    // 尚未调用resolve或reject
});

// fulfilled（已成功）
const p2 = Promise.resolve('成功');
const p3 = new Promise(resolve => resolve('成功'));

// rejected（已失败）
const p4 = Promise.reject('失败');
const p5 = new Promise((resolve, reject) => reject('失败'));

// 状态一旦改变，不可逆
```

**3. 链式调用**
```javascript
fetch('/api/user')
    .then(response => response.json())
    .then(data => {
        console.log(data);
        return fetch(`/api/posts/${data.id}`);
    })
    .then(response => response.json())
    .then(posts => {
        console.log(posts);
    })
    .catch(error => {
        console.error('错误:', error);
    });

// 返回值会传递给下一个then
Promise.resolve(1)
    .then(x => x + 1)  // 2
    .then(x => x * 2)  // 4
    .then(x => console.log(x));  // 4
```

**4. Promise静态方法**
```javascript
// Promise.all（全部成功才成功）
Promise.all([
    fetch('/api/user'),
    fetch('/api/posts'),
    fetch('/api/comments')
]).then(([user, posts, comments]) => {
    console.log('全部完成');
}).catch(error => {
    console.log('有一个失败');
});

// Promise.race（第一个完成的结果）
Promise.race([
    fetch('/api/fast'),
    fetch('/api/slow')
]).then(result => {
    console.log('第一个完成:', result);
});

// Promise.allSettled（等待全部完成，不管成功失败）
Promise.allSettled([
    Promise.resolve(1),
    Promise.reject('error'),
    Promise.resolve(3)
]).then(results => {
    results.forEach(result => {
        console.log(result.status);  // 'fulfilled' 或 'rejected'
    });
});

// Promise.any（第一个成功的结果）
Promise.any([
    Promise.reject('error1'),
    Promise.resolve(2),
    Promise.resolve(3)
]).then(result => {
    console.log(result);  // 2
});
```

**5. async/await**
```javascript
// async函数返回Promise
async function fetchData() {
    return '数据';  // 自动包装为Promise.resolve('数据')
}

fetchData().then(data => console.log(data));

// await等待Promise完成
async function getData() {
    try {
        const response = await fetch('/api/user');
        const data = await response.json();
        console.log(data);
        return data;
    } catch (error) {
        console.error('错误:', error);
    }
}

// 并行执行
async function parallel() {
    const [user, posts] = await Promise.all([
        fetch('/api/user'),
        fetch('/api/posts')
    ]);
    // 同时发起请求
}

// 串行执行
async function serial() {
    const user = await fetch('/api/user');
    const posts = await fetch('/api/posts');
    // 依次执行
}
```

**6. 错误处理**
```javascript
// then的第二个参数
promise.then(
    result => console.log(result),
    error => console.error(error)
);

// catch捕获错误
promise
    .then(result => {
        throw new Error('出错了');
    })
    .catch(error => {
        console.error(error);
        return '默认值';  // 返回值传递给下一个then
    })
    .then(value => {
        console.log(value);  // '默认值'
    });

// async/await错误处理
async function handleError() {
    try {
        const data = await fetch('/api/data');
        return data;
    } catch (error) {
        console.error(error);
        return null;
    }
}
```

**7. Promise封装**
```javascript
// 封装setTimeout
function delay(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

await delay(1000);
console.log('1秒后执行');

// 封装回调函数
function readFilePromise(path) {
    return new Promise((resolve, reject) => {
        fs.readFile(path, 'utf8', (err, data) => {
            if (err) reject(err);
            else resolve(data);
        });
    });
}

// 重试机制
async function retry(fn, times) {
    for (let i = 0; i < times; i++) {
        try {
            return await fn();
        } catch (error) {
            if (i === times - 1) throw error;
        }
    }
}

await retry(() => fetch('/api/data'), 3);
```

**8. 常见模式**
```javascript
// 超时控制
function timeout(promise, ms) {
    return Promise.race([
        promise,
        new Promise((_, reject) => 
            setTimeout(() => reject('超时'), ms)
        )
    ]);
}

// 顺序执行数组
async function sequence(tasks) {
    for (const task of tasks) {
        await task();
    }
}

// 限制并发数
async function limit(tasks, concurrency) {
    const results = [];
    const executing = [];
    
    for (const task of tasks) {
        const p = task().then(result => {
            executing.splice(executing.indexOf(p), 1);
            return result;
        });
        results.push(p);
        executing.push(p);
        
        if (executing.length >= concurrency) {
            await Promise.race(executing);
        }
    }
    
    return Promise.all(results);
}
```

## 应用场景
- 网络请求：Fetch API、Ajax
- 文件操作：读写文件（Node.js）
- 定时器：延迟执行
- 动画：等待动画完成
- 数据库操作：异步查询
- 多个异步操作：Promise.all并行处理

## 注意事项
- Promise状态一旦改变不可逆
- then返回新Promise（支持链式调用）
- catch能捕获之前所有then的错误
- async函数自动返回Promise
- await只能在async函数中使用
- Promise构造函数的executor是同步执行的

## 关联知识
与 [[JavaScript_事件循环]]、[[JavaScript_闭包]]、[[Java_异常处理]] 相关。
