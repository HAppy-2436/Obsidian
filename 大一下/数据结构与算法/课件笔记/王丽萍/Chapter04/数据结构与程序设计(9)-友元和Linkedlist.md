# Chapter 04 — 链表与多项式 — 数据结构与程序设计(9)-友元和Linkedlist

- 章节编号: Chapter04 (#9)
- 来源路径: `C:\Users\Li\OneDrive\Backup\1\大一下\2024数据结构与算法wlp\历年\王丽i萍 数据结构与算法\王丽i萍 数据结构与算法\Chapter04-03\数据结构与程序设计(9)-友元和Linkedlist.ppt`
- 提取的页面组数: 21
- 核心数据结构/算法: 数组, 线性表, 栈, 查找, 类, 模板, 构造函数, 友元, 链表, 搜索, 指针, 表
- 时间复杂度: (无显式标注)
- 代码示例: 有 (匹配度=12)
- 关键例题: (未识别)

---

## 提取的原始内容

> 自动从 MS-PPT 二进制格式 (`TextCharsAtom` / `TextBytesAtom`) 提取，共 21 个文本组。

### Slide 1

```
单击此处编辑母版标题样式

单击此处编辑母版文本样式
第二级
第三级
第四级
第五级
```

### Slide 3

```
数据结构与程序设计
```

### Slide 4

```
数据结构与程序设计(9)

王丽苹
lipingwang@sei.ecnu.edu.cn

Example：编程中的问题

void printMyclass(Myclass m){
	cout<<m.a1<<“   ”<<m.a2;
 //希望在函数中访问私有成员a1和a2，怎么办？
} //为全局的函数

void main(){
	Myclass m2;

   cout<<endl<<"Here is printMyclass(m2):"<<endl;
	printMyclass(m2);
	cout<<endl;
}
```

### Slide 5

```
C++ 基础知识—例程AboutClass3

友元函数：
      是在某类中说明的一个函数，它不是该类的成员，但允许访问该类的所有对象的私有成员和保护成员。
```

### Slide 6

```
class Myclass{
protected:
	int a1;
private:
	int a2;
public:
	Myclass();
	//friend void printMyclass();
   //友元函数的声明
	friend void printMyclass(Myclass m);
};
```

### Slide 7

```
Myclass::Myclass(){
	a1=1;
	a2=2;
}

//void Myclass::printMyclass(){
//	cout<<a1<<"   "<<a2;
//}//error, printMyclass为Myclass的友元，不是成员函数

void printMyclass(){
//	cout<<a1<<"   "<<a2;
}
```

### Slide 8

```
void printMyclass(Myclass m){
	cout<<m.a1<<"   "<<m.a2;
} //为全局的函数

void main(){
	Myclass m1,m2;
	//cout<<endl<<"Here is m1.printMyclass(m2):"<<endl;
	//m1.printMyclass(m2);
	cout<<endl<<"Here is printMyclass(m2):"<<endl;
	printMyclass(m2);
	cout<<endl;
}
```

### Slide 9

```
C++ 基础知识--例程AboutClass3

目录AboutClass3下例程
```

### Slide 10

```
友元虽然出现在类的说明中，但它不是类的成员函数，所以没有this指针。
友元说明可以出现在类的私有或公有部分，没有区别。
友元可直接访问对象的私有成员，省去调用类成员函数的开销，但破坏了类的封装和数据隐藏，因此不能滥用友元。
可以将一个类说明为另一个类的友元。
友元关系不具有传递性和交换性。

C++ 基础知识—友元类

class Stack;
class Node{
   friend Stack;
   private int entry; //私有成员
   private Node *next;//私有成员
};
```

### Slide 11

```
友元为扩充类的接口提供了一种灵活的方法。

C++ 基础知识—引用

C++中使用引用建立变量或对象的别名。
引用分为：引用参数、返回引用以及独立引用。
```

### Slide 12

```
目录AboutClass4下例程
#include<iostream.h>
void swap(int &x, int &y){
	int tmp;
	tmp=x;
	x=y;
	y=tmp;
}

void main(){
	int a=1,b=2;
	cout<<endl<<"old a: "<<a<<" old b: "<<b;
	swap(a,b);
	cout<<endl<<"new a: "<<a<<" new b: "<<b;
	cout<<endl;
}

引用参数
```

### Slide 13

```
目录AboutClass4下例程
#include<iostream.h>
char s[]="Hello world";
char &replace(int i){
	return s[i];
}

void main(){
	replace(5)='X';
	cout<<s<<endl;
}

返回引用
```

### Slide 14

```
目录AboutClass4下例程
#include<iostream.h>
void main(){
	int a=1,b=2;
	int &ref=a;
	ref=10;
	cout<<"new a: "<<a<<endl;
}

独立引用
```

### Slide 15

```
说明引用时，独立引用必须初始化。
一旦初始化，引用就不能重新赋值。
```

### Slide 16

```
不能引用数组
char s[]="Hello world";
//void setArray(char  & s2[]){
//	s2[0]='h';
//}
void setArray(char  s2[]){
	s2[0]='h';
}

void main(){
	setArray(s);
	cout<<s<<endl;
}
```

### Slide 17

```
不能建立引用指针, 但可以建立指针的引用。
void main(){
   int a=1;
   int &ref=a;
   int &ref2=ref;
   //int & *p=&a;
   int  *p=&ref2;
   int * &p2=p; //p2为指针p的别名。
   cout<<&p<<" "<<&p2;
}
```

### Slide 18

```
上机题10

设有一个表头指针为h的单链表。试设计一个算法，通过遍历一趟链表，将链表中所有结点的链接方向逆转。要求逆转结果链表的表头指针h指向原链表的最后一个结点。
template<class Node_entry>
struct Node {
//  data members
   Node_entry entry;
   Node *next;
//  constructors
   Node();
   Node(const Node_entry item, Node *add_on = 0);
};
template<class Node_entry>
void Inverse (Node<Node_entry> * &first )
```

### Slide 19

```
上机题10-不带模板

设有一个表头指针为h的单链表。试设计一个算法，通过遍历一趟链表，将链表中所有结点的链接方向逆转。要求逆转结果链表的表头指针h指向原链表的最后一个结点。
Typedef int Node_entry;
struct Node {
//  data members
   Node_entry entry;
   Node *next;
//  constructors
   Node();
   Node(const Node_entry item, Node *add_on = 0);
};

void Inverse (Node * &first )
```

### Slide 20

```
上机题18

用双向链表来实现一个有序表，使得能在这个表中进行正向和反向搜索。指针p总是指向最后成功搜索到的结点，搜索可以从p指示的结点出发沿任一方向进行。试根据这种情况编写一个函数search(head, p, key)，检索具有关键码key的结点，当搜索成功时函数返回被检索的结点地址，相应地修改p。若搜索不成功则函数返回空指针0，p保持不变。。
Template <class Type>
DblListNode<Type> * Search ( DblListNode<Type> * head,  DblListNode<Type> *& p, Type key )
```

### Slide 21

```
上机题18-不带模板

用双向链表来实现一个有序表，使得能在这个表中进行正向和反向搜索。指针p总是指向最后成功搜索到的结点，搜索可以从p指示的结点出发沿任一方向进行。试根据这种情况编写一个函数search(head, p, key)，检索具有关键码key的结点，当搜索成功时函数返回被检索的结点地址，相应地修改p。若搜索不成功则函数返回空指针0，p保持不变。。
DblListNode * Search ( DblListNode * head,  DblListNode *& p, Type key )
```

### Slide 22

```
如果期望在类A的外部，函数f中访问类A的私有成员，可以用友元的形式来解决这个问题。
方法：
在类的声明中，说明f为友元函数。

通过Node的定义，说明Node具有一个友元类 Stack。
这样，发生的变化是：
Node的私有成员不仅可以在Node成员函数中访问，
而且在Stack的实现中也可以通过Node的对象访问他的私有成员。

指针的引用：是指为一个指针变量建议一个别名，这个是允许的。 Int* &p2 =p; //p2为指针p的别名。
引用的指针：是指希望将引用的地址存放在指针变量中起来，但是引用没有内存地址，它只是一个变量的别名，所以不能够建立它的指针。

#include <iostream.h>
void main(){
   int a=23;
   int &ref=a;
   int &ref2=ref;
   //int& *p=&a;
   int  *p=&ref2;
   int * &p2=p;
   cout<<&p<<" "<<&p2<<endl;
   cout<<&a<<" "<<&ref<<" "<<&ref2<<endl;
}
输出为：
0x0012FF70 0x0012FF70
0x0012FF7C 0x0012FF7C 0x0012FF7C

注意：此时的形参为指向指针的引用。经过这样，Inverse函数结束后，实参的值才会改变

敒畳瑬

效敲椠⁳牰湩䵴捹慬獳洨⤲ഺ‱†�
```
