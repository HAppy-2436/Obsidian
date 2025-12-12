# JavaScript 闭包

## 定义
闭包（Closure）是指函数能够记住并访问其词法作用域，即使函数在其词法作用域之外执行。闭包使内部函数可以访问外部函数的变量，常用于数据封装、回调函数和模块化。

## 核心内容
**1. 基本概念**
```javascript
function outer() {
    let count = 0;  // 外部变量
    
    function inner() {
        count++;  // 访问外部变量
        console.log(count);
    }
    
    return inner;  // 返回内部函数
}

const counter = outer();
counter();  // 1
counter();  // 2
counter();  // 3
// inner函数记住了outer的count变量
```

**2. 数据封装（私有变量）**
```javascript
function createPerson(name) {
    let age = 0;  // 私有变量
    
    return {
        getName() {
            return name;
        },
        getAge() {
            return age;
        },
        setAge(newAge) {
            if (newAge >= 0) {
                age = newAge;
            }
        }
    };
}

const person = createPerson('Alice');
console.log(person.getName());  // 'Alice'
person.setAge(25);
console.log(person.getAge());   // 25
// 无法直接访问name和age
```

**3. 循环中的闭包陷阱**
```javascript
// 错误示例（var）
for (var i = 0; i < 3; i++) {
    setTimeout(function() {
        console.log(i);  // 输出 3, 3, 3
    }, 100);
}
// 闭包捕获的是i的引用，循环结束i=3

// 解决方法1：使用let
for (let i = 0; i < 3; i++) {
    setTimeout(function() {
        console.log(i);  // 输出 0, 1, 2
    }, 100);
}
// let是块级作用域，每次循环有独立的i

// 解决方法2：IIFE
for (var i = 0; i < 3; i++) {
    (function(j) {
        setTimeout(function() {
            console.log(j);  // 输出 0, 1, 2
        }, 100);
    })(i);
}
```

**4. 模块模式**
```javascript
const calculator = (function() {
    let result = 0;  // 私有状态
    
    return {
        add(n) {
            result += n;
            return this;
        },
        subtract(n) {
            result -= n;
            return this;
        },
        getResult() {
            return result;
        }
    };
})();

calculator.add(10).subtract(3);
console.log(calculator.getResult());  // 7
// result无法从外部访问
```

**5. 函数工厂**
```javascript
function makeMultiplier(factor) {
    return function(number) {
        return number * factor;
    };
}

const double = makeMultiplier(2);
const triple = makeMultiplier(3);

console.log(double(5));  // 10
console.log(triple(5));  // 15
// 每个函数保持独立的factor
```

**6. 事件处理与回调**
```javascript
function setupButton(buttonId) {
    let clickCount = 0;
    
    document.getElementById(buttonId).addEventListener('click', function() {
        clickCount++;
        console.log(`Button clicked ${clickCount} times`);
    });
}

setupButton('myButton');
// 回调函数记住了clickCount
```

**7. 防抖和节流**
```javascript
// 防抖（debounce）
function debounce(fn, delay) {
    let timer = null;
    
    return function(...args) {
        clearTimeout(timer);
        timer = setTimeout(() => {
            fn.apply(this, args);
        }, delay);
    };
}

// 节流（throttle）
function throttle(fn, delay) {
    let lastTime = 0;
    
    return function(...args) {
        const now = Date.now();
        if (now - lastTime >= delay) {
            fn.apply(this, args);
            lastTime = now;
        }
    };
}

// 使用
const handleScroll = debounce(() => {
    console.log('Scroll handled');
}, 300);

window.addEventListener('scroll', handleScroll);
```

**8. 内存泄漏风险**
```javascript
// 可能导致内存泄漏
function createLeak() {
    const largeData = new Array(1000000).fill('data');
    
    return function() {
        console.log(largeData[0]);
        // largeData一直被闭包引用，无法释放
    };
}

// 避免泄漏：及时清理
function better() {
    let data = getLargeData();
    
    return {
        getData() {
            return data;
        },
        cleanup() {
            data = null;  // 手动释放
        }
    };
}
```

## 应用场景
- 数据封装：创建私有变量和方法
- 回调函数：事件监听器、定时器
- 函数柯里化：部分应用参数
- 模块化：IIFE模块模式
- React Hooks：useState、useEffect等
- 防抖节流：性能优化

## 注意事项
- 闭包会持有外部变量引用，可能导致内存泄漏
- 循环中使用var时注意闭包陷阱（用let或IIFE）
- 过度使用闭包会增加内存消耗
- 调试时闭包变量可能不直观
- 性能敏感场景谨慎使用
- 及时清理不需要的闭包引用

## 关联知识
与 [[JavaScript_原型链]]、[[JavaScript_事件循环]]、[[函数传参]] 相关。
