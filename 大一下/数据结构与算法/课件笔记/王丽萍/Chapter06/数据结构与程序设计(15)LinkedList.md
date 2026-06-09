# Chapter 06 — 抽象数据类型与运算符重载 — 数据结构与程序设计(15)LinkedList

- 章节编号: Chapter06 (#15)
- 来源路径: `C:\Users\Li\OneDrive\Backup\1\大一下\2024数据结构与算法wlp\历年\王丽i萍 数据结构与算法\王丽i萍 数据结构与算法\chapter06-02\数据结构与程序设计(15)LinkedList.ppt`
- 提取的页面组数: 42
- 核心数据结构/算法: 线性表, 链表, 指针, 类, 运算符, 构造函数, 表
- 时间复杂度: (无显式标注)
- 代码示例: 有 (匹配度=9)
- 关键例题: (未识别)

---

## 提取的原始内容

> 自动从 MS-PPT 二进制格式 (`TextCharsAtom` / `TextBytesAtom`) 提取，共 42 个文本组。

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
数据结构与程序设计(15)

王丽苹
lipingwang@sei.ecnu.edu.cn
```

### Slide 5

```
本章主要讨论链表的实现。
即用链接存储形式来实现列表。
```

### Slide 6

```
链表中节点的类型定义：
struct Node {
// data members
	Node_entry entry;
	Node *next;
// constructors
	Node( );
	Node(Node_entry item, Node *link = NULL);
};
```

### Slide 7

```
列表的链接实现方式，请参考：
目录LinkList下例程
```

### Slide 8

```
//结构体类型Node的定义。
struct Node {
// data members
	Node_entry entry;
	Node *next;
// constructors
	Node( );
	Node(Node_entry item, Node * add_on = NULL);
};
```

### Slide 9

```
//构造函数的实现
Node::Node( )
{
	next = NULL;
}

Node::Node(Node_entry item, Node *add_on)
{
	entry = item;
	next = add_on;
}
```

### Slide 10

```
enum Error_code{underflow, overflow, range_error, success};
typedef int List_entry;
class List {
public:
	~List( );
	List( );
	List(const List &copy);
	void operator = (const List &copy);
	int size( ) const;
	bool full( ) const;
	bool empty( ) const;
	void clear( );
	void traverse(void (*visit)(List_entry &));
	Error_code retrieve(int position, List_entry &x) const;
	Error_code replace(int position, const List_entry &x);
	Error_code remove(int position, List_entry &x);
	Error_code insert(int position, const List_entry &x);
protected:
// Data members for the linked list implementation now follow.
	int count; //表示链表中元素的个数
	Node *head; //存放链表的头结点地址
// The following auxiliary function is used to locate list positions
	Node *set_position(int position) const; //返回指定位置的节点的地址

};
```

### Slide 11

```
Node *List :: set_position(int position) const
/* Pre: position is a valid position in the List ; 0 <= position < count .
Post: Returns a pointer to the Node inposition . */
{
	Node *q = head; //引入临时的指针q
       //通过q来周游链表
	for (int i = 0; i < position; i++)
               q = q->next;
	return q;
}
```

### Slide 12

```
Insert操作
```

### Slide 13

```
Error_code List :: insert(int position, const List_entry &x)
/* Post: If the List is not full and 0 <= position <= n , where n is the number of
entries in the List , the function succeeds: Any entry formerly at position and
all later entries have their position numbers increased by 1, and x is inserted at
position of the List .
Else: The function fails with a diagnostic error code. */
{
	if (position < 0 || position > count)
		return range_error;
	Node *new_node, *previous, *following;
	if (position > 0) {
		//定位previous和following的位置。
                       previous = set_position(position - 1);
		following = previous->next;
	}
	else following = head;
```

### Slide 14

```
//产生新的节点空间。
        new_node = new Node(x, following);
	if (new_node == NULL)
		return overflow;
	//将新产生的节点加入到链表中。
         if (position == 0)
		head = new_node;
	else
		previous->next = new_node;
	count++;
	return success;
}
```

### Slide 15

```
Implementation of Linked Insert的两种情况：
```

### Slide 16

```
Implementation of Linked Listremove的两种情况：
```

### Slide 17

```
这里存在一点小问题：当 List x，y;
x = y //ok
x= x //将出现问题。
```

### Slide 18

```
实现效率分析

在处理n个元素的链表时：
Clear, insert, remove, retrieve和replace的时间与n近似。
List，empty，full和size在常量时间内操作。
这种实现还有没有改进的余地呢？

楌歮摥䰠獩⁴浉汰浥湥慴楴湯�
```

### Slide 19

```
楌歮摥䰠獩⁴浉汰浥湥慴楴湯
```

### Slide 20

```
捁楴湯⁳湯愠䰠湩敫⁤楌瑳

潂歯倠㈲′䘠杩牵⁥⸶റ
```

### Slide 21

```
浉汰浥湥慴楴湯漠⁦楌歮摥䰠獩�
```

### Slide 22

```
䰍獩⁴㨺䰠獩⡴ഩൻ按畯瑮㴠〠഻栉慥⁤‽啎䱌഻�
```

### Slide 23

```
†ठ††潰楳楴湯ㄭ ††††††††††††††††††††瀠獯瑩潩�

牰癥潩獵

潦汬睯湩�

潐楳楴湯〾

潐楳楴湯〽

敮彷潮敤
```

### Slide 24

```
䔍牲牯损摯⁥楌瑳㨠›敲潭敶椨瑮瀠獯瑩潩Ɱ䰠獩彴湥牴⁹砦ഩൻ椉⁦瀨獯瑩潩⁮‼‰籼瀠獯瑩潩⁮㴾挠畯瑮ഩउ敲畴湲爠湡敧敟牲牯഻三摯⁥瀪敲楶畯ⱳ⨠潦汬睯湩㭧ऍ晩⠠潰楳楴湯㸠〠 ൻउ牰癥潩獵㴠猠瑥灟獯瑩潩⡮潰楳楴湯ⴠㄠ㬩ऍ昉汯潬楷杮㴠瀠敲楶畯⵳渾硥㭴ऍ瀉敲楶畯⵳渾硥㵴潦汬睯湩ⵧ渾硥㭴ऍൽ攉獬筥ऍ昉汯潬楷杮㴠栠慥㭤ऍ栉慥⁤‽敨摡㸭敮瑸഻紉‍††††砠昽汯潬楷杮㸭湥牴㭹ऍ敤敬整映汯潬楷杮഻††按畯瑮ⴭ഻爉瑥牵⁮畳捣獥㭳納
```

### Slide 25

```
†ठ††潰楳楴湯ㄭ †††††潰楳楴湯
```

### Slide 26

```
植瑮䰠獩⁴㨺猠穩⡥ 潣獮൴ൻ爉瑥牵⁮潣湵㭴納
```

### Slide 27

```
戍潯⁬楌瑳㨠›畦汬⤨挠湯瑳笍ऍ潎敤⨠敮彷潮敤഻渉睥湟摯⁥‽敮⁷潎敤഻椉⁦渨睥湟摯⁥㴽丠䱕⥌敲畴湲琠畲㭥ऍ汥敳笠ऍ搉汥瑥⁥敮彷潮敤഻उ敲畴湲映污敳഻紉納
```

### Slide 28

```
戍潯⁬楌瑳㨠›浥瑰⡹ 潣獮൴ൻ爉瑥牵⁮潣湵㵴〽഻�
```

### Slide 29

```
瘍楯⁤楌瑳㨠›汣慥⡲ഩൻ䰉獩彴湥牴⁹㭸ऍ桷汩⡥攡灭祴⤨爩浥癯⡥ⰰ⥸഻�
```

### Slide 30

```
瘍楯⁤楌瑳㨠›牴癡牥敳瘨楯⁤⨨楶楳⥴䰨獩彴湥牴⁹⤦ഩൻ三摯⁥瀪湟摯㵥敨摡഻眉楨敬瀨湟摯⥥ൻउ⨨楶楳⥴瀨湟摯ⵥ放瑮祲㬩ऍ瀉湟摯㵥彰潮敤㸭敮瑸഻紉納
```

### Slide 31

```
䔍牲牯损摯⁥楌瑳㨠›敲牴敩敶椨瑮瀠獯瑩潩Ɱ䰠獩彴湥牴⁹砦 潣獮൴ൻ椉⁦瀨獯瑩潩⁮‼‰籼瀠獯瑩潩⁮㴾挠畯瑮ഩउ敲畴湲爠湡敧敟牲牯഻三摯⁥瀪湟摯㭥ऍ彰潮敤猽瑥灟獯瑩潩⡮潰楳楴湯㬩ऍ㵸彰潮敤㸭湥牴㭹ऍ敲畴湲猠捵散獳഻�
```

### Slide 32

```
䔍牲牯损摯⁥楌瑳㨠›敲汰捡⡥湩⁴潰楳楴湯‬潣獮⁴楌瑳敟瑮祲☠⥸笍ऍ晩⠠潰楳楴湯㰠〠簠⁼潰楳楴湯㸠‽潣湵⥴ऍ爉瑥牵⁮慲杮彥牥潲㭲ऍ潎敤⨠彰潮敤഻瀉湟摯㵥敳彴潰楳楴湯瀨獯瑩潩⥮഻瀉湟摯ⵥ放瑮祲砽഻爉瑥牵⁮畳捣獥㭳納�
```

### Slide 33

```
䰍獩⁴㨺䰠獩⡴潣獮⁴楌瑳☠潣祰ഩൻ按畯瑮㴠〠഻栉慥⁤‽啎䱌഻三摯⁥焪㴠挠灯⹹敨摡഻椉瑮椠〽഻眉楨敬焨笩ऍ椉獮牥⡴Ⱪ⵱放瑮祲㬩ऍ焉焽㸭敮瑸഻उ⭩㬫ऍൽ�
```

### Slide 34

```
†⼯湁瑯敨⁲敭桴摯䰍獩⁴㨺䰠獩⡴潣獮⁴楌瑳☠潣祰ഩൻ††潣湵⁴‽㬰‍†丠摯⁥渪睥损灯ⱹ⨠彰潣祰㴠挠灯⹹敨摡഻††晩⠠彰潣祰㴠‽啎䱌 敨摡㴠丠䱕㭌‍†攠獬⁥⁻††††††††††††⼯†畄汰捩瑡⁥桴⁥楬歮摥渠摯獥甠楳杮戠獡⁥敭桴摯മ†††栉慥⁤‽敮彷潣祰㴠渠睥丠摯⡥彰潣祰㸭湥牴⥹഻按畯瑮⬫഻†††眉楨敬⠠彰潣祰㸭敮瑸 ൻ††††ठ††瀠损灯⁹‽彰潣祰㸭敮瑸഻†††††††渠睥损灯⵹渾硥⁴‽敮⁷潎敤瀨损灯⵹放瑮祲㬩ऍ††挠畯瑮⬫഻†††††††渠睥损灯⁹‽敮彷潣祰㸭敮瑸഻ ൽ††素‍�
```

### Slide 35

```
潃祰䌠湯瑳畲瑣牯

†瀠损灯⁹†††††††栠慥⁤††††渠睥损灯⁹
```

### Slide 36

```
瘍楯⁤楌瑳㨠›灯牥瑡牯㴠⠠潣獮⁴楌瑳☠潣祰ഩൻ䰉獩彴湥牴⁹㭸ऍ桷汩⡥攡灭祴⤨爩浥癯⡥ⰰ⥸഻三摯⁥焪㴠挠灯⹹敨摡഻椉瑮椠〽഻眉楨敬焨笩ऍ椉獮牥⡴Ⱪ⵱放瑮祲㬩ऍ焉焽㸭敮瑸഻उ⭩㬫ऍൽ納⼍㼯㼿䤠⁳瑩传�
```

### Slide 37

```
瘍楯⁤楌瑳㨠›灯牥瑡牯㴠⠠潣獮⁴楌瑳☠潣祰ഩൻ䰉獩彴湥牴⁹㭸ऍ晩琨楨㵳☽潣祰 敲畴湲഻眉楨敬ℨ浥瑰⡹⤩敲潭敶〨砬㬩ऍ潎敤⨠ⁱ‽潣祰栮慥㭤ऍ湩⁴㵩㬰ऍ桷汩⡥⥱ൻउ湩敳瑲椨焬㸭湥牴⥹഻उ㵱⵱渾硥㭴ऍ椉⬫഻紉納
```

### Slide 38

```
䰍獩⁴㨺縠楌瑳 ഩൻ䰉獩彴湥牴⁹㭸ऍ桷汩⡥攡灭祴⤨爩浥癯⡥ⰰ⥸഻�
```

### Slide 39

```
瘍楯⁤灵慤整䰨獩彴湥牴⁹砦笩ऍ⩸㈽ऻ納഍瘍楯⁤牰湩⡴楌瑳敟瑮祲☠⥸ൻ按畯㱴砼㰼湥汤ऻ納
```

### Slide 40

```
潶摩洠楡⡮笩ऍ楌瑳椼瑮‾祭楬瑳഻昉牯椨瑮椠〽椻㔼椻⬫洩汹獩⹴湩敳瑲椨椬㬩ऍ潣瑵㰼夢畯⁲楬瑳栠癡⁥㰢洼汹獩⹴楳敺⤨㰼•汥浥湥獴∺㰼湥汤഻洉汹獩⹴牴癡牥敳瀨楲瑮㬩ऍ祭楬瑳爮浥癯⡥ⰱ椠㬩ऍ潣瑵㰼䄢瑦牥爠浥癯⡥⤱∺㰼湥汤഻洉汹獩⹴牴癡牥敳瀨楲瑮㬩ऍ祭楬瑳爮浥癯⡥ⰰ椠㬩ऍ潣瑵㰼䄢瑦牥爠浥癯⡥⤰∺㰼湥汤഻洉汹獩⹴牴癡牥敳瀨楲瑮㬩�
```

### Slide 41

```
敒畳瑬

潙牵氠獩⁴慨敶㔠攠敬敭瑮㩳」ㄍ㈍㌍㐍䄍瑦牥爠浥癯⡥⤱ഺരലളഴ晁整⁲敲潭敶〨㨩㈍㌍㐍
```

### Slide 42

```
䰉獩㱴湩㹴洠汹獩㉴洨汹獩⥴഻ठ潣瑵㰼䄢瑦牥洠汹獩㉴洨汹獩⥴∺㰼湥汤഻洉汹獩㉴琮慲敶獲⡥牰湩⥴഻ऍ潣瑵㰼䄢瑦牥甠摰瑡㩥㰢攼摮㭬ऍ祭楬瑳琮慲敶獲⡥灵慤整㬩ऍ祭楬瑳琮慲敶獲⡥牰湩⥴ऻऍऍ楌瑳椼瑮‾祭楬瑳㬳ऍ祭楬瑳㴳祭楬瑳഻ठ潣瑵㰼䄢瑦牥洠汹獩㍴洽汹獩㩴㰢攼摮㭬ऍ祭楬瑳⸳牴癡牥敳瀨楲瑮㬩納
```

### Slide 43

```
晁整⁲祭楬瑳⠲祭楬瑳㨩㈍㌍㐍䄍瑦牥甠摰瑡㩥㐍㘍㠍䄍瑦牥洠汹獩㍴洽汹獩㩴㐍㘍㠍
```
