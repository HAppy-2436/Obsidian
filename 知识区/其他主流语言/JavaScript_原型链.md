# JavaScript 原型链

## 定义
原型链（Prototype Chain）是JavaScript实现对象继承的机制，每个对象都有一个内部属性`[[Prototype]]`（通过`__proto__`访问）指向其原型对象，形成链式结构，用于属性和方法的查找和共享。

## 核心内容
**1. 原型基础**
```javascript
// 构造函数
function Person(name) {
    this.name = name;
}

// 原型对象
Person.prototype.sayHello = function() {
    console.log('Hello, ' + this.name);
};

// 创建实例
const p1 = new Person('Alice');
const p2 = new Person('Bob');

p1.sayHello();  // 'Hello, Alice'
p2.sayHello();  // 'Hello, Bob'

// p1和p2共享Person.prototype上的方法
console.log(p1.sayHello === p2.sayHello);  // true
```

**2. 原型关系**
```javascript
function Person(name) {
    this.name = name;
}

const p = new Person('Alice');

// 原型关系
p.__proto__ === Person.prototype  // true
Person.prototype.constructor === Person  // true
Person.__proto__ === Function.prototype  // true
Person.prototype.__proto__ === Object.prototype  // true
Object.prototype.__proto__ === null  // 原型链终点
```

**3. 原型链查找**
```javascript
function Animal(name) {
    this.name = name;
}
Animal.prototype.eat = function() {
    console.log(this.name + ' is eating');
};

function Dog(name, breed) {
    Animal.call(this, name);  // 继承属性
    this.breed = breed;
}

// 继承原型
Dog.prototype = Object.create(Animal.prototype);
Dog.prototype.constructor = Dog;

Dog.prototype.bark = function() {
    console.log('Woof!');
};

const dog = new Dog('Buddy', 'Golden');

// 原型链查找顺序
dog.bark();  // 1. 在dog自身找 → 2. 在Dog.prototype找 → 找到
dog.eat();   // 1. 在dog自身找 → 2. 在Dog.prototype找 → 3. 在Animal.prototype找 → 找到
dog.toString();  // 继续向上找到Object.prototype
```

**4. 原型链图示**
```
dog对象
  ↓ __proto__
Dog.prototype
  ↓ __proto__
Animal.prototype
  ↓ __proto__
Object.prototype
  ↓ __proto__
null
```

**5. 属性遮蔽（Property Shadowing）**
```javascript
function Person() {}
Person.prototype.name = 'Default';

const p = new Person();
console.log(p.name);  // 'Default'（来自原型）

p.name = 'Alice';  // 在实例上添加属性
console.log(p.name);  // 'Alice'（实例属性遮蔽原型属性）

delete p.name;
console.log(p.name);  // 'Default'（删除实例属性后显示原型属性）
```

**6. 检测属性位置**
```javascript
function Person(name) {
    this.name = name;
}
Person.prototype.age = 20;

const p = new Person('Alice');

// 检查自身属性
p.hasOwnProperty('name');  // true
p.hasOwnProperty('age');   // false

// 检查属性是否存在（包括原型链）
'name' in p;  // true
'age' in p;   // true
'toString' in p;  // true

// 获取自身属性
Object.keys(p);  // ['name']
Object.getOwnPropertyNames(p);  // ['name']
```

**7. 现代继承（ES6 class）**
```javascript
class Animal {
    constructor(name) {
        this.name = name;
    }
    
    eat() {
        console.log(this.name + ' is eating');
    }
}

class Dog extends Animal {
    constructor(name, breed) {
        super(name);  // 调用父类构造函数
        this.breed = breed;
    }
    
    bark() {
        console.log('Woof!');
    }
}

const dog = new Dog('Buddy', 'Golden');
dog.eat();   // 继承自Animal
dog.bark();  // Dog自己的方法

// 底层仍是原型链
dog.__proto__ === Dog.prototype  // true
Dog.prototype.__proto__ === Animal.prototype  // true
```

**8. 原型方法 vs 实例方法**
```javascript
function Person(name) {
    this.name = name;
    
    // 实例方法（每个实例独立）
    this.sayHi = function() {
        console.log('Hi');
    };
}

// 原型方法（所有实例共享）
Person.prototype.sayHello = function() {
    console.log('Hello');
};

const p1 = new Person('Alice');
const p2 = new Person('Bob');

console.log(p1.sayHi === p2.sayHi);  // false（不同实例）
console.log(p1.sayHello === p2.sayHello);  // true（共享）
```

**9. Object.create()**
```javascript
const parent = {
    greet() {
        console.log('Hello');
    }
};

const child = Object.create(parent);
child.name = 'Alice';

child.greet();  // 'Hello'（继承自parent）
child.__proto__ === parent  // true

// 创建无原型对象
const obj = Object.create(null);
obj.toString();  // 报错：toString不存在
```

## 应用场景
- 对象继承：类继承体系
- 方法共享：节省内存（原型方法）
- 属性查找：原型链查找机制
- 多态：子类重写父类方法
- 工具函数：Array.prototype.map等
- 框架设计：Vue、React的组件继承

## 注意事项
- 修改原型会影响所有实例
- 不要修改内置对象原型（Array.prototype等）
- 原型链过长会影响性能
- 使用hasOwnProperty检查自身属性
- `__proto__`已废弃，用Object.getPrototypeOf()
- 优先使用ES6 class语法

## 关联知识
与 [[JavaScript_闭包]]、[[Java_面向对象]]、[[C++_虚函数]] 相关。
