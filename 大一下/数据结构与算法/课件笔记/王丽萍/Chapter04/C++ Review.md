# Chapter 04 — 链表与多项式 — C++ Review

- 章节编号: Chapter04 (#?)
- 来源路径: `C:\Users\Li\OneDrive\Backup\1\大一下\2024数据结构与算法wlp\历年\王丽i萍 数据结构与算法\王丽i萍 数据结构与算法\Chapter04-01\C++ Review.ppt`
- 提取的页面组数: 51
- 核心数据结构/算法: 数组, 线性表, 栈, 指针, 类, 继承, 多态, 模板, 运算符重载, 运算符, 构造函数, 析构函数, 字符串, 虚函数, 泛型
- 时间复杂度: (无显式标注)
- 代码示例: 有 (匹配度=16)
- 关键例题: (未识别)

---

## 提取的原始内容

> 自动从 MS-PPT 二进制格式 (`TextCharsAtom` / `TextBytesAtom`) 提取，共 51 个文本组。

### Slide 2

```
ANSI C++
Microsoft C++ (MS Visual C++ 6.0)
Other vendors:  Borland, Symantec, Turbo, …
Many older versions (almost annual) including different version of C too
Many vendor specific versions
Many platform specific versions
For this class: Unix / Linux based versions
g++
```

### Slide 3

```
^
|
&& (booleans only)
|| (booleans only)
?:
= += -= *= ….

C++ allows operator overloading
```

### Slide 4

```
Applied automatically provided there is no loss of precision
float  double
int  double
Example
int iresult, i=3;
double dresult, d=3.2;
dresult = i/d   => implicit casting dresult=0.9375
iresult = i/d    => error! Why? Loss in precision, 				     needs explicit casting

if (boolean)
		statement;
	else if(boolean)
		statement2;
	else
		statement3;

Booleans only, not integers!
if (i > 0)    correct
if (i = 2)    correct / incorrect ?
```

### Slide 5

```
C++ allows for three different ways of passing parameters:
Pass “by value”
E.g. foo (int n)
Appropriate for small objects (usually primitive types) that should not be altered by the function call
Pass “by constant reference”
E.g. foo(const T& myT)
Appropriate for large objects that should not be altered by the function call
Pass “by reference”
E.g. foo(bool & errFlag)
Appropriate for small objects that can be altered by the function call
Array types are always passed “by reference”
```

### Slide 6

```
An alias – another name for an object.
    int x = 5;
    int &y = x; // y is a
                // reference to x
    y = 10;

What happened to x?
What happened to y?  –  y is x.
```

### Slide 7

```
class Change //找零
{
private:
	int quarters;
	int dimes;
public:
	int getQuarters() {return quarters;}
	int getDimes() {return dimes;}
	void setQuarters(int aQuarters) {quarters = aQuarters;}
		…...
	void printChange()
	{cout << "\nQuarters: " << quarters
	             << "     Dimes: " << dimes << endl;
	}
};
```

### Slide 8

```
// first we define the variables.
int height = 72;
int result = 0;
human hank;

//set our human’s height
hank.setHeight(height);

//get his height
result = hank.getHeight();

cout << “Hank is = “ << result << “inches tall” << endl;
```

### Slide 9

```
Inheritance (cont’d)

class classname: public parentname {
	private:
		….;
	public:
		….;
	//access to parent methods through
	// parentname::methodname …
}
```

### Slide 10

```
#include “Segment.H”

#include <iostream>
```

### Slide 11

```
If this variable is
not defined…
```

### Slide 12

```
#include<iostream>
	Tell compiler that we are doing I/O
cout
	Object to which we can send data.
<<
	operator for sending data.
endl  `\n’ `\t’
	Special symbols that we can send.
```

### Slide 13

```
#include <iostream.h>

main ()
{
	int userInput;
	cout << “Enter number:”;
	cin >> userInput;
	cout << “You entered ” <<
		userInput << endl;
}
```

### Slide 14

```
#include <iostream.h>
#include <fstream.h>
main()
{
	int inputNumber;

	ofstream myOutputFile(“outfile”);
	ifstream myInputFile(“infile”);
	myOutputFile << “text to file.” << endl;
	myInputFile >> inputNumber;
	myOutputFile.close();
	myInputFile.close();
}
```

### Slide 15

```
int main(){
	int i, j;
	int *pi, *pj;

	i   = 5;
	j   = i;
	pi  = &i;
	pj  = pi;
	*pj = 4;

	cout << i << “ “;
	cout << j << “ “;
	cout << *pi << “ “;
	cout << *pj << endl;

	return 0;
}

Point *p = new Point(5, 5);
Point is a class already defined
new can be thought of a function with slightly strange syntax
new allocates space to hold the object.
new calls the object’s constructor.
new returns a pointer to that object.

new returns a pointer to the dynamically created object.

#include “Cow.h”
#include <iostream>
using namespace std;

int main(){
	int *i = new int(12);
	Cow *c = new Cow;
	...
	delete i;
	delete c;

	return 0;
}
```

### Slide 16

```
int* badFunction(){
	int num = 10;
	return &num;
}
int* stillBad(int n){
	n += 12;
	return &n;
}
int main(){
	int num = 12;
	int *myNum = badFunction();
	int *myOtherNum = 	stillBad(num);

	cout << *myNum << “, “;
	cout << *myOtherNum << endl;

	return 0;
}

int evilFunction(){
	int *i = new int(9);
	return *i;
}

int main(){
	int num = evilFunction();

	// I’m loosing my memory!!

	return 0;
}
```

### Slide 17

```
If a class dynamically allocates memory, we need a way to deallocate it when it’s destroyed.
Distructors called upon distruction of an object

delete calls the object’s destructor.
delete frees space occupied by the object.

A destructor cleans up after the object.
Releases resources such as memory.

Destructors – an Example
```

### Slide 18

```
Won’t compile.

void Math::printSquares(const int& j, int& k)
{
	  k = k*k;  // Does this compile?
    cout << j*j << “, “ << k << endl;
}
int main()
{
    int i = 5;
    Math::printSquares(i, i);
}
```

### Slide 19

```
#include <iostream>
...
std::string question =
			  “How do I prevent RSI?”;
std::cout << question << std::endl;

using namespace std;

string answer = “Type less.”;
cout << answer << endl;

But, not in header files!
```

### Slide 20

```
Limited Generic Programming (polymorphism)
	Some functions have the same semantic meaning for some (if not all) data 	types.  For instance, a function print() should display a sensible 	representation of anything passed in.  Ideally, it shouldn’t need to be 	rewritten for each possible type.

 Less repetitive code
	Code that only differs in the data type it handles does not have to be
	rewritten for each and every data type you want to handle.  It’s easier to
	read and maintain since one piece of code is used for everything
```

### Slide 21

```
Naive method – write an overloaded function for each type
```

### Slide 22

```
Problem: Oftentimes, it is nice to be able to swap the values of two  	variables.  This function’s behavior is similar for all data types. Templated 	functions let you do that – in most cases without any syntax changes.

Template method – write one templated function

The template<…>  line states that everything in the following declaration or definition is under the subject of the template. (In this case, the definition is the function swap)

In here goes a list of “placeholders variables.” In almost all cases, they will be specified with either the typename or class keywords.  These two keywords are equivalent.

“Placeholder variables” have one value within each template declaration.  Think of them as being replaced by whatever type you specify the template to be.
```

### Slide 23

```
template<class Stack_entry>
Error_code MyStack<Stack_entry>::pop()
/*
Pre:  None.
Post: If the Stack is not empty, the top of
      the Stack is removed.  If the Stack
      is empty, an Error_code of underflow is returned.
*/

{
   Error_code outcome = success;
   if (count == 0)
      outcome = underflow;
   else --count;
   return outcome;
}

……

Class Templates: Example cont’d

#include "MyStack.h"

template<class Stack_entry>
Error_code MyStack<Stack_entry>::push(const Stack_entry &item)
/*
Pre:  None.
Post: If the Stack is not full, item is added to the top of the Stack.  If the Stack is full,
an Error_code of overflow is returned and the Stack is left unchanged.
*/
{
   Error_code outcome = success;
   if (count >= maxstack)
      outcome = overflow;
   else
      entry[count++] = item;
   return outcome;
}
……
```

### Slide 24

```
What’s the output? 5, i was copied.

What’s the output now? 25, i was changed.
```

### Slide 25

```
What happened to x? – it is now 10
What happened to y? – silly question?   y is x.   eg: professor Black is Michael.

avoid copying big objects.
makes syntax work out better.
won’t slice

Can’t have a reference to nothing.
can’t reseat/reassign reference.
```

### Slide 26

```
Much like a java reference (but more explicit)
A pointer is a variable that contains the address of an object in memory.

Line 1 – x is an integer, give it value 10
Line 3 – p gets the address of x
```

### Slide 27

```
Ask about virtual. (what’s wrong here…)
```

### Slide 28

```
If you can, you should make this guarantee.
const extends the type to allow you to specify which data is read-only
Why is this good?  --- gets the compiler to help make sure certain values don’t change.

Just because there’s a reference to something const, doesn’t mean that it won’t change.
it simply won’t be changed through that reference.

汃捩⁫潴攠楤⁴慍瑳牥琠瑩敬猠祴敬

汃捩⁫潴攠楤⁴慍瑳牥琠硥⁴瑳汹獥匍捥湯⁤敬敶൬桔物⁤敬敶൬潆牵桴氠癥汥䘍晩桴氠癥汥
```

### Slide 29

```
⭃‫敒楶睥

䌍⬫眠牡⵭灵

畯汴湩�

楈瑳牯⁹湡⁤癯牥楶睥䈍獡捩映慥畴敲൳慐慲敭整⁲慰獳湩൧汃獡敳൳湉敨楲慴据⁥湡⁤楶瑲慵൬效摡牥映汩൥佉䴍浥牯⁹慍慮敧敭瑮䈍杩琠牨敥›敤瑳畲瑣牯‬潣祰挠湯瑳畲瑣牯‬湡⁤獡楳湧敭瑮漠数慲潴൲潃獮൴敔灭慬整

楈瑳牯⁹景䌠⬫

㤱㈷›䌠氠湡畧条⁥敤敶潬数⁤瑡䈠汥⁬慌獢䐍湥楮⁳楒捴楨⁥牷瑯⁥⁃潦⁲湕硩传൓敎摥摥䌠映牯眠牯⁫楷桴唠楮൸慬整㜠猰›䌠戠捥浯獥瀠灯汵牡映牯传⁓敤敶潬浰湥⁴祢洠湡⁹敶摮牯൳慍祮瘠牡慩瑮⁳景琠敨氠湡畧条⁥敤敶潬数൤乁䥓猠慴摮牡⁤⁃湩ㄠ㠹ⴷ㤸഍

楈瑳牯⁹景䌠⬫⠠潣瑮湩敵⥤

慥汲⁹〸㩳†橂牡敮匠牴畯瑳畲⁰摡獤传⁏敦瑡牵獥琠⁯⁃牣慥楴杮䌠⬫㤍猰›挠湯楴畮摥攠潶畬楴湯漠⁦桴⁥慬杮慵敧愠摮椠獴愠灰楬慣楴湯൳牰晥牥敲⁤慬杮慵敧映牯传⁓湡⁤潬⁷敬敶⁬牰杯慲浭湩൧潰異慬⁲慬杮慵敧映牯愠灰楬慣楴湯搠癥汥灯敭瑮氍睯氠癥汥挠湯牴汯愠摮栠杩⁨敬敶⁬潰敷൲�

潃据灥畴污祬眠慨⁴獩䌠⬫

汁整湲瑡癩獥ഺ獩椠⁴ⱃ眠瑩⁨潬獴洠牯⁥灯楴湯⁳湡⁤敦瑡牵獥ി獩椠⁴湡传⁏牰杯慲浭湩⁧慬杮慵敧眠瑩⁨⁃獡椠獴挠牯㽥植⁳瑩愠搠癥汥灯敭瑮攠癮物湯敭瑮ി湏洠獯⁴祳瑳浥⁳瑩椠⁳⁡敤敶潬浰湥⁴湥楶潲浮湥ⱴ氠湡畧条ⱥ愠摮氠扩慲祲‬獵摥映牯戠瑯⁨牰捯摥牵污愠摮漠橢捥⁴牯敩瑮摥瀠潲牧浡業杮‬桴瑡挠湡戠⁥畣瑳浯穩摥愠摮攠瑸湥敤⁤獡搠獥物摥�

敖獲潩獮漠⁦⭃�

桃牡捡整楲瑳捩⁳景䌠⬫愠⁳⁡潃灭瑵牥䰠湡畧条�

牐捯摥牵污伍橢捥⁴牏敩瑮摥䔍瑸湥楳汢൥⸮�

瑏敨⁲住䰠湡畧条獥

浓污瑬污൫異敲传⁏慬杮慵敧搠癥汥灯摥愠⁴䅐䍒䨍癡⁡戍極瑬漠⁮⽃⭃ഫ扯敪瑣⁳湡⁤慤慴琠灹獥䔍晩汥愠摮漠桴牥�
```

### Slide 30

```
桗瑡礠畯挠湡搠⁯楷桴䌠⬫

灁獰⠠瑳湡慤潬敮‬敗⁢灡獰‬潣灭湯湥獴ഩ捁楴敶搠獥瑫灯⠠祄慮業⁣呈䱍‬湩汣圠扥ഩ牃慥整朠慲桰捩污愠灰൳慄慴愠捣獥⁳攨洭楡ⱬ映汩獥‬䑏䍂ഩ湉整牧瑡⁥潣灭湯湥獴眠 瑯敨⁲慬杮慵敧�

楄慳癤湡慴敧⁳景䌠⬫

敔摮⁳潴戠⁥湯⁥景琠敨氠獥⁳潰瑲扡敬氠湡畧条獥䌍浯汰捩瑡摥‿㐍‰灯牥瑡牯ⱳ椠瑮楲慣整瀠敲散敤据ⱥ瀠楯瑮牥ⱳ攠捴മ慣⁮潣瑮潲⁬癥牥瑹楨杮洍湡⁹硥散瑰潩獮愠摮猠数楣污挠獡獥琍敲敭摮畯⁳楬牢牡敩⁳潢桴猠慴摮牡Ɽ瘠湥潤⁲灳捥晩捩‬湡⁤癡楡慬汢⁥潦⁲異捲慨敳‬畢⁴污⁬牡⁥湩牴捩瑡൥獁数瑣⁳扡癯⁥慣⁮敲畳瑬椠⁮楨桧洠楡瑮湥湡散挠獯獴

摁慶瑮条獥漠⁦⭃�

癁楡慬汢⁥湯洠獯⁴慭档湩獥䌍湡朠瑥朠潯⁤数晲牯慭据൥慃⁮敧⁴浳污⁬楳敺䌍湡洠湡条⁥敭潭祲攠晦捥楴敶祬䌍湡挠湯牴汯攠敶祲桴湩൧潇摯猠灵汰⁹景瀠潲牧浡敭獲匍極慴汢⁥潦⁲污潭瑳愠祮琠灹⁥景瀠潲牧浡⠠牦浯猠獹整獭瀠潲牧浡⁳潴愠灰楬慣楴湯⥳

楈瑳牯⁹湡⁤癯牥楶睥䈍獡捩映慥畴敲൳慐慲敭整⁲慰獳湩൧汃獡敳൳湉敨楲慴据⁥湡⁤楶瑲慵൬效摡牥映汩൥佉䴍浥牯⁹慍慮敧敭瑮䈍杩琠牨敥›敤瑳畲瑣牯ⱥ挠灯⁹潣獮牴捵潴Ⱳ愠摮愠獳杩浮湥⁴灯牥瑡牯䌍湯瑳名浥汰瑡�

牐浩瑩癩⁥祔数�

潢汯उ牴敵漠⁲慦獬⁥漨汮⁹⭃⤫挍慨ॲ㠉ㄯⴶ楢⁴猍潨瑲†उ㘱戭瑩猠杩敮⁤湩整敧൲湩ॴउ㈳戭瑩猠杩敮⁤湩整敧൲湵楳湧摥उ㈳戭瑩甠獮杩敮⁤湩整敧൲潬杮उ㈳⼠㘠ⴴ楢⁴楳湧摥椠瑮来牥昍潬瑡उ㈳戭瑩映潬瑡湩⁧潰湩൴潤扵敬उ㐶戭瑩映潬瑡湩⁧潰湩�

灏牥瑡牯⁳湡⁤牐捥摥湥散

嵛†‮††††††ഠ潴愠捣獥⁳牡慲獹攠敬敭瑮⁳⼠琠⁯捡散獳漠橢捥⁴敭桴摯⁳湡⁤楦汥獤攍灸⭲‫硥牰ⴭ⬠攫灸⁲ⴠ攭灸⁲℠ഠ敮⁷⠠祴数攩灸൲‪ ഥ‫ⴠഠ㰼†㸾†椨瑮来牥⁳湯祬ഩ‼‾㴾†㴼㴍‽℠ഽ�

牐捥摥湥散䔠慸灭敬

桗瑡椠㩳㔠⬠㈠‱ ‴‥ള‽‵‫㈨‱ ⤴┠㌠㴍㔠⬠⠠㔠┠㌠ഩ‽‵‫ല‽�

硅汰捩瑩䌠獡楴杮

琨灹⥥攠灸敲獳潩൮潐獳扩敬愠潭杮愠汬椠瑮来牥愠摮映潬瑡琠灹獥倍獯楳汢⁥浡湯⁧潳敭挠慬獳爠晥牥湥散൳䔍朮‮湩⁴⁩‽椨瑮  搨畯汢⥥‵ 搨畯汢⥥″�

浉汰捩瑩䌠獡楴杮

潃瑮潲⁬汆睯

睓瑩档⼠挠獡�

睳瑩档⠠潣瑮潲噬牡ഩ笉ഉ 挠獡⁥愧‧ഺउ瑳瑡浥湥⵴റउ牢慥㭫ऍ†慣敳✠❢㨠ऍ猉慴整敭瑮㈭ऍ戉敲歡഻ 搠晥畡瑬㨠ऍ猉慴整敭瑮㌭ऍ戉敲歡഻ ൽ潄渠瑯映牯敧⁴桴⁥牢慥⁫潣浭湡⁤潴愠潶摩猠牵牰獩⁥敲畳瑬�

潌灯�

桷汩⡥戼潯敬湡⤾‍†猠慴整敭瑮഻損൯††瑳瑡浥湥㭴眍楨敬㰨潢汯慥㹮ഩउഉ昍牯椨楮⵴硥牰※戼潯敬湡㬾椠据⵲硥牰ഩ††瑳瑡浥湥㭴�

潌灯删晥敲桳牥

桗捩⁨潬灯⁳畭瑳攠數畣整琠敨物猠慴整敭瑮⁳瑡氠慥瑳漠据㽥圍楨档氠潯獰挠湡挠潨獯⁥潴渠癥牥攠數畣整琠敨物猠慴整敭瑮㽳圍楨档瘠污敵漠⁦桴⁥潢汯慥⁮湩楤慣整⁳潴搠⁯桴⁥瑳瑡浥湥獴愠慧湩�

潓敭䌠湯敶瑮潩獮映牯嘠牡慩汢⁥慎敭⁳

獕⁥敬瑴牥⁳湡⁤畮扭牥൳潄渠瑯甠敳猠数楣污挠慨慲瑣牥⁳湩汣摵湩⁧灳捡獥‬潤獴‬湵敤汲湩獥‬潰湵⁤楳湧ⱳ攠捴മ桔⁥楦獲⁴敬瑴牥眠汩⁬敢氠睯牥挠獡൥獕⁥慶楲扡敬渠浡獥琠慨⁴牡⁥敭湡湩晧汵⠠硥散瑰映牯漠捣獡潩慮⁬潣湵整獲琠慨⁴敷洠杩瑨挠污⁬Ⱪ樠‬ⱸ攠捴⤮复畯挠湡挠湯慣整慮整眠牯獤‬湡⁤慣楰慴楬敺攠捡⁨晡整⁲桴⁥楦獲ⱴ攠朮Ⱞ戠湡䉫污‬桴獩捁瑣畎Ɑ琠瑯流൴晉礠畯愠扢敲楶瑡ⱥ戠⁥潣獮獩整瑮‮䘠牯攠慸灭敬搠⁯潮⁴獵⁥潢桴戠湡䉫污†湡⁤潴慴䉬污湡散愠⁳慶楲扡敬渠浡獥�

潓敭䌠湯敶瑮潩獮映牯匠牴捵⁴湡⁤䌋慬獳丠浡獥

湉挠敲瑡湩⁧慮敭⁳景猠牴捵獴愠摮挠慬獳獥‬灡汰⁹桴⁥慳敭爠汵獥愠⁳潦⁲慶楲扡敬渠浡獥‬硥散瑰琠敨映物瑳挠慨慲瑣牥眠汩⁬敢甠灰牥挠獡൥硅浡汰㩥愍⁮扯敪瑣猧渠浡㩥†祭慃൲桴⁥瑳畲瑣漠⁲汣獡⁳慮敭›†慃൲湁瑯敨⁲硅浡汰㩥†偡牥潳⁮†湡⁤†敐獲湯

癏牥楶睥

個獡楳杮倠牡浡瑥牥�
```

### Slide 31

```
慐獳湩⁧祢瘠污敵

潶摩猠畱牡⡥湩⁴⥩笍‍†椠㴠椠椪഻ൽ湩⁴慭湩⤨笍‍†椠瑮椠㴠㔠഻††煳慵敲椨㬩‍†挠畯⁴㰼椠㰠‼湥汤഻�

慐獳湩⁧祢爠晥牥湥散

潶摩猠畱牡⡥湩♴椠ഩൻ††⁩‽⩩㭩納植瑮洠楡⡮ഩൻ††湩⁴⁩‽㬵‍†猠畱牡⡥⥩഻††潣瑵㰠‼⁩㰼攠摮㭬納

慐獳湩⁧祢挠湯瑳湡⁴敲敦敲据�

潶摩猠畱牡⡥潣獮⁴湩♴椠ഩൻ††⁩‽⩩㭩納植瑮洠楡⡮ഩൻ††湩⁴⁩‽㬵‍†猠畱牡⡥⥩഻††潣瑵㰠‼⁩㰼攠摮㭬納

潗瑮眠牯Ⱬ眠票�

湩⁴煳慵敲挨湯瑳椠瑮…⥩笍‍†爠瑥牵⁮⩩㭩納植瑮洠楡⡮ഩൻ††湩⁴⁩‽㬵‍†挠畯⁴㰼猠畱牡⡥⥩㰠‼湥汤഻�

楗汬琠栠獩眠牯㽫

桗瑡椠⁳⁡敲敦敲据㽥

桗⁹牡⁥桴祥甠敳畦㽬

桗湥瀠獡楳杮愠杲浵湥⁴景氠牡敧猠穩⁥挨慬獳琠灹⥥‬慣⁮慳敶猠慰散匍浯瑥浩獥渠敥⁤潴挠慨杮⁥⁡慶畬⁥景愠⁮牡畧敭瑮䌍湡戠⁥獵摥琠⁯敲畴湲洠牯⁥桴湡漠敮瘠污敵⠠慰獳洠汵楴汰⁥慰慲敭整獲戠⁹敲敦敲据⥥�

潈⁷牡⁥敲敦敲据獥ଠ楤晦牥湥⁴牦浯倠楯瑮牥㽳
```

### Slide 32

```
删晥牥湥散

倠楯瑮牥

椠瑮愠㴠ㄠ㬰‍湩⁴⁢‽〲഻椠瑮☠⁣‽㭡‍⁣‽㭢ഠ圍慨⁴獩琠敨瘠污敵漠⁦㽡

椠瑮愠㴠ㄠ㬰‍湩⁴⁢‽〲഻椠瑮⨠⁣‽愦഻挠㴠☠㭢
```

### Slide 33

```
畏汴湩�

汃獡敳�

牐癯摩⁥⁡敭档湡獩⁭潦⁲敤楦楮杮挠慬獳獥漠⁦扯敪瑣⹳圍⁥慣⁮敤楦敮琠敨挠慬獳漠⁦污⁬潣灭瑵牥⁳潴栠癡⁥散瑲楡⁮档牡捡整楲瑳捩⹳䄍⁮湩瑳湡散漠⁦⁡潣灭瑵牥椠⁳潹牵栠浯⁥䍐മ汃獡敳⁳潣瑮楡⁮敭扭牥瘠牡慩汢獥愠摮洠浥敢⁲畦据楴湯⹳

汃獡敳⁳湩䌠⬫଺桗⁹牃慥整䌠慬獳獥⼠传橢捥獴�

敋灥⁳污⁬敲慬整⁤湩潦⠠⹩⹥‬慤慴 潴敧桴牥刍晥牥琠⁯污⁬桴⁥敲慬整⁤湩潦戠⁹湯⁥慮敭倍潲整瑣琠敨椠普牯慭楴湯䠍摩⁥敭桴摯⁳桴瑡甠敳漠⁲档湡敧琠敨椠普൯敋灥洠瑥潨獤琠杯瑥敨⁲楷桴琠敨物爠汥瑡摥椠普�

硅浡汰⁥景䈠湥晥瑩⁳景䌠敲瑡湩⁧湡传橢捥�

敋灥⁳污⁬敲慬整⁤湩潦⠠⹩⹥‬慤慴 潴敧桴牥倍牥潳⁮桴獩敐獲湯ऻഉ敐獲湯琠楨偳牥潳⁮‽敮⁷敐獲湯⠠䈢汩≬‬䌢楬瑮湯Ⱒ㔠⤲഻敒敦⁲潴愠汬琠敨爠汥瑡摥椠普⁯祢漠敮渠浡൥琉楨偳牥潳൮牐瑯捥⁴桴⁥湩潦浲瑡潩൮उ慬瑳慎敭㴠∠潄敬㬢†⼠港牯慭汬⁹慤慴洠浥敢獲ठउ牡⁥牰癩瑡ⱥ愠摮洠浥敢⁲畦据楴湯⁳牡⁥異汢捩�

汃獡敳⁳湡⁤扏敪瑣�

慍浭污�

畈慭獮

楔敧獲

敐杧�

汣獡�

湩敨楲獴

湩瑳湡散漭�

硅浡汰⁥景愠匠浩汰⁥汃獡�

潍敲䌠慬獳䔠慸灭敬

汣獡⁳畨慭൮ൻ⼉ 桴獩搠瑡⁡獩瀠楲慶整琠⁯湩瑳湡散⁳景琠敨挠慬獳ऍ湩⁴敨杩瑨഻按慨⁲慮敭嵛഻椉瑮眠楥桧㭴഍異汢捩ഺ瘉楯।猠瑥效杩瑨椨瑮栠楥桧噴污敵㬩ऍ湩ॴ朠瑥效杩瑨⤨഻㭽�

畆据楴湯䐠晥湩瑩潩獮

潶摩栠浵湡㨺敳䡴楥桧⡴湩⁴敨杩瑨慖畬⥥笍ऍ晩⠠敨杩瑨慖畬⁥‾⤰ऍ栉楥桧⁴‽敨杩瑨慖畬㭥ऍ汥敳ऍ栉楥桧⁴‽㬰納഍湩⁴畨慭㩮机瑥效杩瑨⤨笍ऍ敲畴湲栨楥桧⥴഻�

硅浡汰�

慈歮椠⁳㈷椠据敨⁳慴汬

畏灴瑵

湉瑳湡楴瑡湩⁧湡传橢捥�

桔⁥汣獡⁳敤楦楮楴湯搠敯⁳潮⁴牣慥整愠祮漠橢捥獴䤍獮慴瑮慩楴杮愠摮挠湯瑳畲瑣湩⁧牡⁥煥極慶敬瑮眠牯獤映牯戠極摬湩⁧⁡敮⁷扯敪瑣戠獡摥漠⁮桴⁥潭敤⁬椨攮Ⱞ琠浥汰瑡⥥漠⁦桴⁥汣獡൳湉瑳湡楴瑡湩⁧獩搠湯⁥番瑳氠歩⁥敤汣牡湩⁧⁡慶楲扡敬漠⁦⁡畢汩⁴湩搠瑡⁡祴数䤍獮慴瑮慩楴杮椠⁳潤敮戠⁹⁡潣獮牴捵潴⁲猨浯瑥浩獥挠污敬⁤⁡潣獮牴捵潴⁲敭桴摯ഩ晉琠敨∠汣獡⁳牰癯摩牥•潤獥渠瑯瀠潲楶敤愠挠湯瑳畲瑣牯‬桴湥琠敨䌠⬫挠浯楰敬⁲牰癯摩獥愠搠晥畡瑬漠敮愠瑵浯瑡捩污祬名敨搠晥畡瑬挠湯瑳畲瑣牯搠敯⁳潮⁴牰癯摩⁥慶畬獥琠⁯桴⁥慤慴洠浥敢獲⠠⹩⹥琠敨椠獮慴据⁥慶楲扡敬⥳

湉瑳湡楴瑡湩⁧湡传橢捥⁴洨牯⥥

桗湥琠敨漠橢捥⁴獩椠獮慴瑮慩整Ɽ洠浥牯⁹獩愠汬捯瑡摥䔍慸灭敬漠⁦湩瑳湡楴瑡潩⁮椨灭楬楣⁴慣汬漠⁦潣獮牴捵潴⥲ऍ䌉牡洠䍹牡഻उ汅灥慨瑮漠敮汅灥慨瑮‬睴䕯敬桰湡㭴不⁯湩瑩慩楬慺楴湯琠歡獥瀠慬散䔍捡⁨扯敪瑣栠獡椠獴漠湷洠浥牯⁹污潬慣楴湯漍敮汅灥慨瑮愠摮琠潷汅灥慨瑮愠敲猠灥牡瑡⁥扯敪瑣⁳湩搠晩敦敲瑮氠捯瑡潩獮椠⁮敭潭祲䔍捡⁨獩愠摤敲獳摥椠摮癩摩慵汬⁹祢渠浡⁥牯氠捯瑡潩൮慅档搠瑡⁡敭扭牥椠⁳摡牤獥敳⁤湩楤楶畤污祬甠楳杮琠敨漠橢捥⁴慮敭愠摮琠敨搠瑡⁡敭扭牥渠浡ⱥ映牯攠慸灭敬›†ऍउ湯䕥敬桰湡⹴条൥उ琉潷汅灥慨瑮渮浡�

敒敦敲据湩⁧湡传橢捥�

慅档漠橢捥⁴慨⁳⁡慮敭⠠牯愠氠捯瑡潩⥮眠楨档椠⁳獡楳湧摥眠敨⁮桴⁥扯敪瑣椠⁳湩瑳湡楴瑡摥瀍楲慶整搠瑡⁡敭扭牥⁳牡⁥捡散獳扩敬漠汮⁹楷桴湩琠敨挠慬獳猍湩散洠獯⁴慤慴洠浥敢獲愠敲瀠楲慶整‬桴瑡洠慥獮琠慨⁴桴獥⁥慤慴椠整獭愠敲愠捣獥敳⁤敧敮慲汬⁹祢洠慥獮漠⁦敭扭牥映湵瑣潩獮洍䕹敬桰湡⹴条⁥‽㈷※⼯潷❮⁴潷歲‬獡畳業杮愠敧ठउ ⼯獩搠捥慬敲⁤獡瀠楲慶整洍䕹敬桰湡⹴敳䅴敧㜨⤲※⼯眠汩⁬潷歲
```

### Slide 34

```
湉敨楲慴据�

桔⁥潰敷⁲景漠橢捥⵴牯敩瑮摥氠湡畧条獥䔍慮汢獥爠略敳漠⁦楦汥獤洯瑥潨獤䄍汬瀠牡湥⁴楦汥獤椠据畬敤⁤湩挠楨摬椠獮慴瑮慩楴湯倍潲整瑣摥愠摮瀠扵楬⁣楦汥獤愠摮洠瑥潨獤搠物捥汴⁹捡散獳扩敬琠⁯档汩൤慐敲瑮洠瑥潨獤洠祡戠⁥癯牥楲摤湥不睥映敩摬⁳湡⁤敭桴摯⁳慭⁹敢愠摤摥琠⁯桴⁥档汩൤畍瑬灩敬椠桮牥瑩湡散
```

### Slide 35

```
效摡牥映汩�

潆⁲潣灭敬⁸汣獡敳ⱳ琠敨洠浥敢⁲畦据楴湯⁳牡⁥敤汣牡摥椠⁮⁡敨摡牥映汩⁥湡⁤桴⁥敭扭牥映湵瑣潩獮愠敲椠灭敬敭瑮摥椠⁮⁡敳慰慲整映汩⹥名楨⁳污潬獷瀠潥汰⁥潴氠潯⁫瑡琠敨挠慬獳搠晥湩瑩潩獮‬湡⁤桴楥⁲敭扭牥映湵瑣潩獮猠灥牡瑡汥൹桔⁥敨摡牥映汩⁥敮摥⁳潴戠⁥湩汣摵摥椠⁮潹牵瀠潲牧浡眠敨⁮潹⁵獵⁥桴⁥汣獡敳⁳敤楦敮⁤湩琠敨栠慥⁤楦敬
```

### Slide 36

```
椣据畬敤

湉敳瑲栠慥敤⁲楦敬愠⁴桴獩瀠楯瑮�

獕⁥楬牢牡⁹敨摡牥�

效摡牥䜠慵摲�

椣湦敤⁦彟䕓䵇久彔䕈䑁剅彟⌍敤楦敮张卟䝅䕍呎䡟䅅䕄归ൟ⼍ 潣瑮湥獴漠⁦敓浧湥⹴ൈ⼯⸮മ⌍湥楤൦名⁯湥畳敲椠⁴獩猠晡⁥潴椠据畬敤愠映汩⁥潭敲琠慨⁮湯散�
```

### Slide 37

```
椣湦敤⁦彟䕓䵇久彔䕈䑁剅彟⌍敤楦敮张卟䝅䕍呎䡟䅅䕄归ൟ⼍ 潣瑮湥獴漠⁦敳浧湥⹴ൈ⼯⸮മ⌍湥楤൦名⁯湥畳敲椠⁴獩猠晡⁥潴椠据畬敤愠映汩⁥潭敲琠慨⁮湯散�

敄楦敮椠⹴

湅⁤景朠慵摲摥愠敲⹡
```

### Slide 38

```
湉異�

椣据畬敤㰠潩瑳敲浡栮ാ吉汥⁬桴⁥楬歮牥眠⁥牡⁥潤湩⁧慢楳⁣⽉൏楣൮吉敨椠灮瑵漠橢捥⹴䤠⁴敲牴敩敶⁳湩異⁴牦浯琠敨欠祥潢牡൤㸾ऍ桔⁥硥牴捡潴⁲灯牥瑡牯�

湅整⁲畮扭牥ㄺ㌲㔴复畯攠瑮牥摥ㄠ㌲㔴

⽉⁏牆浯愠䘠汩�

⽉⁏牦浯愠映汩⁥獩搠湯⁥湩愠猠浩汩牡眠祡�
```

### Slide 39

```
桗瑡椠⁳⁡潰湩整㽲
```

### Slide 40

```
湩⁴⁸‽〱഻湩⁴瀪഻瀍㴠☠㭸഍഍瀍朠瑥⁳桴⁥摡牤獥⁳景砠椠⁮敭潭祲�
```

### Slide 41

```
湩⁴⁸‽〱഻湩⁴瀪഻瀍㴠☠㭸഍瀪㴠㈠㬰഍⨍⁰獩琠敨瘠污敵愠⁴桴⁥摡牤獥⁳⹰
```

### Slide 42

```
湩⁴⁸‽〱഻湩⁴瀪഻瀍㴠☠㭸഍瀪㴠㈠㬰഍�

敄汣牡獥愠瀠楯瑮牥ഠ潴愠⁮湩整敧�

…椠⁳摡牤獥⁳灯牥瑡牯‍†朠瑥⁳摡牤獥⁳景砠�

‪搠牥晥牥湥散漠数慲潴൲††敧獴瘠污敵愠⁴�
```

### Slide 43

```
⁁潐湩整⁲硅浡汰�

‾ⰴ㔠‬ⰴ㐠

汁潬慣楴杮洠浥牯⁹獵湩⁧敮�

敍潭祲䄠汬捯瑡潩⁮硅浡汰獥

牐扯敬獭

慄杮楬杮瀠楯瑮牥൳潐湩整獲琠⁯敭潭祲琠慨⁴慨⁳污敲摡⁹敢湥搠慥汬捯瑡摥猍来敭瑮瑡潩⁮慦汵⁴挨牯⁥畤灭⸩⸮漠⁲潷獲⹥⸮മ敍潭祲氠慥൫潌獯湩⁧潰湩整獲琠⁯祤慮業慣汬⁹污潬慣整⁤敭潭祲匍扵瑳湡楴污瀠潲汢浥椠⁮慭祮挠浯敭捲慩⁬牰摯捵獴匍敥圠湩潤獷㤠സ⭃‫䅈⁓低䜠剁䅂䕇䌠䱏䕌呃佉ⅎ

慄杮楬杮瀠楯瑮牥攠慸灭敬�

湩⁴慭湩⤨ൻ椉瑮⨠祭畎⁭‽敮⁷湩⡴㈱㬩ऍ湩⁴洪佹桴牥畎⁭‽祭畎㭭഍搉汥瑥⁥祭畎㭭ऍऍ潣瑵㰠‼洪佹桴牥畎⁭㰼攠摮㭬഍爉瑥牵⁮㬰納�

敍潭祲䰠慥⁫硅浡汰獥

湩⁴慭湩⤨ൻ椉瑮⨠祭畎⁭‽敮⁷湩⡴㈱㬩ऍ祭畎⁭‽敮⁷湩⡴〱㬩ऍ⼯传灯⹳⸮഍搉汥瑥⁥祭畎㭭ऍऍ敲畴湲〠഻ൽ

敄污潬慣楴杮洠浥牯⁹獵湩⁧敤敬整�

⼯愠汬捯瑡⁥敭潭祲倍楯瑮⨠⁰‽敮⁷潐湩⡴ⰵ㔠㬩഍⸮മ⼯映敲⁥桴⁥敭潭祲損汥瑥⁥㭰†഍潆⁲癥牥⁹慣汬琠⁯敮ⱷ琠敨敲洠獵⁴敢攍慸瑣祬漠敮挠污⁬潴搠汥瑥⹥�

獕湩⁧敮⁷楷桴愠牲祡�

湩⁴⁸‽〱഻湩⩴渠浵ㅳ㴠渠睥椠瑮ㅛ崰※⼠ 歯植瑮‪畮獭′‽敮⁷湩孴嵸※†⼯漠൫䤍楮楴污穩獥愠⁮牡慲⁹景ㄠ‰湩整敧獲漠⁮桴⁥敨灡മ⭃‫煥極慶敬瑮漠⁦ൃ椉瑮‪畮獭㴠⠠湩⩴洩污潬⡣⁸‪楳敺景椨瑮⤩഻

獕湩⁧敮⁷楷桴洠汵楴楤敭獮潩慮⁬牡慲獹

湩⁴⁸‽ⰳ礠㴠㐠഻湩⩴渠浵㍳㴠渠睥椠瑮硛孝崴㕛㭝⼯漠൫湩⩴渠浵㑳㴠渠睥椠瑮硛孝嵹㕛㭝⼯䈠䑁ഡ䤍楮楴污穩獥愠洠汵楴楤敭獮潩慮⁬牡慲൹湏祬琠敨映物瑳搠浩湥楳湯挠湡戠⁥⁡慶楲扡敬‮桔⁥敲瑳洠獵⁴敢挠湯瑳湡獴മ獕⁥楳杮敬搠浩湥楳湯愠牲祡⁳潴映歡⁥畭瑬摩浩湥楳湯污漠敮�

獕湩⁧敤敬整漠⁮牡慲獹

⼯愠汬捯瑡⁥敭潭祲植瑮‪畮獭‱‽敮⁷湩孴〱㭝植瑮‪畮獭″‽敮⁷湩孴嵸㑛孝崵഻⸍⸮⼍ 牦敥琠敨洠浥牯൹敤敬整嵛渠浵ㅳ഻敤敬整嵛渠浵㍳഻䠍癡⁥潴甠敳搠汥瑥孥⹝

汃獡⁳敄瑳畲瑣牯�

汣獡⁳祍汃獡筳瀍扵楬㩣ऍ祍汃獡⡳笩ऍ⼉ 潃獮牴捵潴൲紉ऍ䵾䍹慬獳⤨୻⼉ 敄瑳畲瑣牯ऍൽഉ⸉⸮納�

敄瑳畲瑣牯�

汣獡⁳敓浧湥൴ൻ異汢捩ഺ††敓浧湥⡴㬩‍†瘠物畴污縠敓浧湥⡴㬩瀍楲慶整ഺ††潐湩⁴洪灟ⰰ⨠彭ㅰ഻㭽

敓浧湥㩴区来敭瑮⤨笍‍†洠灟‰‽敮⁷潐湩⡴ⰰ〠㬩‍†洠灟‱‽敮⁷潐湩⡴ⰱㄠ㬩納匍来敭瑮㨺卾来敭瑮⤨笍‍†搠汥瑥⁥彭ば഻††敤敬整洠灟㬱納�

潃祰䌠湯瑳畲瑣牯愠摮䄠獳杩浮湥⁴灏牥瑡牯

潃祰䌠湯瑳畲瑣牯›ऍ汣獡⁳潒獯整筲ऍ異汢捩ഺउ⸮മउ潒獯整⡲潣獮⁴潒獯整⁲爦獨笩ऍउ⼯䐠⁯潹牵搠敥⁰潣祰ऍ紉ऍ⸉⸮ऍ㭽ऍ⸮മ⼉ 獕条൥刉潯瑳牥爠ㄨ⤲഻刉潯瑳牥猠爨㬩

獁楳湧敭瑮传数慲潴㩲ऍऍ汣獡⁳潒獯整筲ऍ異汢捩ഺउ⸮മउ潒獯整♲ഠउ灯牥瑡牯⠽潣獮⁴潒獯整⁲爦獨笩‍उ⼉ 潃祰猠畴晦ऍ紉ऍ⸉⸮ऍ㭽ऍ⸮മ⼉ 獕条൥刉潯瑳牥爠ㄨ⤲‬⡳〱㬩ऍ⁲‽㭳

慃潮楮慣⁬潆浲

汁⁬汣獡敳⁳桳畯摬栠癡⁥慥档漠⁦桴⁥潦汬睯湩㩧䐍晥畡瑬挠湯瑳畲瑣牯䌍灯⁹潣獮牴捵潴൲獁楳湧敭瑮漠数慲潴൲敄瑳畲瑣牯

⼯䌠湡湯捩污䌠睯挍慬獳䌠睯ൻ異汢捩ഺ䌉睯⤨⹻⸮ൽ䌉睯挨湯瑳䌠睯☠桲⥳⹻⸮ൽ䌉睯…灯牥瑡牯⠽潣獮⁴潃⁷挦ഩउ⹻⸮ൽ縉潃⡷笩⸮紮഍⸉⸮納�

湉牴摯捵湩㩧†潣獮�

潶摩䴠瑡㩨瀺楲瑮煓慵敲挨湯瑳椠瑮…⥩笍‍†椠㴠椠椪഻††潣瑵㰠‼⁩㰼攠摮㭬納植瑮洠楡⡮ഩൻ††湩⁴⁩‽㬵‍†䴠瑡㩨瀺楲瑮煓慵敲椨㬩‍†䴠瑡㩨瀺楲瑮畃敢椨㬩納

潈⁷潤獥挠湯瑳眠牯⁫敨敲�

敒畴湲湩⁧潣獮⁴敲敦敲据獥椠⁳䭏

汣獡⁳潐湩൴ൻ潰湩㩴‍†挠湯瑳搠畯汢♥朠瑥⡘ 潣獮㭴‍†挠湯瑳搠畯汢♥朠瑥⡙ 潣獮㭴‍†瘠楯⁤潭敶搨畯汢⁥硤‬潤扵敬搠⥹഻牰癩瑡㩥‍†搠畯汢⁥彭ⱸ洠祟഻�

潣獮⁴潤扵敬…潐湩㩴机瑥⡘ 潣獮൴ൻ††敲畴湲洠硟഻�

潃獮慴瑮映湵瑣潩Ɱഠ污潳挠污敬⁤捡散獳牯

敒畴湲愠爠晥牥湥散琠⁯⁡潣獮慴瑮搠畯汢�

慎敭灳捡獥

慎敭灳捡獥愠敲欠湩⁤景氠歩⁥慰正条獥椠⁮慊慶刍摥捵獥渠浡湩⁧潣普楬瑣൳潍瑳猠慴摮牡獤䌠⬫爠畯楴敮⁳湡⁤汣獡敳⁳湡⁤湵敤⁲桴⁥瑳⁤慮敭灳捡�

獵湩⁧慮敭灳捡�
```

### Slide 44

```
敔灭慬整

桗瑡攠慸瑣祬愠敲琠浥汰瑡獥映牯‬湡⁤桷⁹敬牡⁮桴浥�
```

### Slide 45

```
硅浡汰㩥愠猠慷⁰畦据楴湯

潶摩猠慷⡰湩⁴愦‬湩⁴戦 ൻ†湩⁴⁣‽㭡‍愠㴠戠഻†⁢‽㭣納

潶摩猠慷⡰⁔愦‬⁔戦 ൻ†⁔⁣‽㭡‍愠㴠戠഻†⁢‽㭣納

睓灡映牯椠瑮来牥�

睓灡映牯愠⁮牡楢牴牡⁹祴数吠

整灭慬整㰠祴数慮敭吠ാ潶摩猠慷⡰⁔愦‬⁔戦 ൻ†⁔⁣‽㭡‍愠㴠戠഻†⁢‽㭣納

桔獩映湵瑣潩⁮慣⁮敢甠敳⁤楷桴愠祮琠灹⁥桴瑡猠灵潰瑲⁳獡楳湧敭瑮愠摮挠湡戠⁥慰獳摥椠⁮獡愠渠湯挭湯瑳爠晥牥湥散‮�
```

### Slide 46

```
敔灭慬整匠湹慴㩸猠慷⁰楤獳捥整�
```

### Slide 47

```
敔灭慬整匠湹慴㩸唠楳杮椠�

硅浡汰㩥‍ठ潤扵敬搠‱‽⸴ⰵ搠′‽⸶㬷ऍ睳灡搨ⰱ搠⤲�

祓瑮硡

汃獡⁳敔灭慬整㩳䔠慸灭敬

硅浡汰㩥吠浥汰瑡獥猠慴正

椣湦敤⁦䅍剔塉䡟⌍敤楦敮䴠呁䥒彘ൈ湥浵䔠牲牯损摯筥湵敤晲潬ⱷ漠敶晲潬ⱷ猠捵散獳㭽挍湯瑳椠瑮洠硡瑳捡⁫‽〱഻整灭慬整挼慬獳匠慴正敟瑮祲ാ汣獡⁳祍瑓捡⁫ൻ異汢捩ഺ†䴠卹慴正⤨഻†戠潯⁬浥瑰⡹ 潣獮㭴‍†牅潲彲潣敤瀠灯⤨഻‍†‍†牅潲彲潣敤琠灯匨慴正敟瑮祲☠瑩浥 潣獮㭴‍†牅潲彲潣敤瀠獵⡨潣獮⁴瑓捡彫湥牴⁹椦整⥭഻瀍楲慶整ഺ†椠瑮挠畯瑮഻†匠慴正敟瑮祲攠瑮祲浛硡瑳捡嵫഻㭽഍攣摮晩⼠‪䅍剔塉䡟⨠�

楆敬›慍牴硩栮

潎楴散琠敨漠汮⁹摡楤楴湯琠⁯桴⁥汣獡⁳敤楦楮楴湯椠⁳桴⁥楬敮ഺ†整灭慬整㰠祴数慮敭吠�

楗桴湩琠敨琠敨搠晥湩瑩潩⁮汢捯Ⱬ琠敨瀠慬散潨摬牥栠獡挠湡戠⁥獵摥愠⁳⁡慤慴琠灹⹥†桗湥琠敨琠浥汰瑡⁥獩猠数楣污穩摥‬瑩琠歡獥漠⁮桴⁥慶畬⁥景琠敨猠数楣污穩瑡潩⹮
```

### Slide 48

```
楆敬›慍牴硩挮灰

汃獡⁳敔灭慬整㩳甠慳敧

敔灭慬整⁤汣獡敳⁳畭瑳戠⁥硥汰捩瑩祬猠数楣污穩摥‮吠畨ⱳ琠⁯牣慥整愠猠慴正漠⁦潤扵敬⁳獵湩⁧桴⁥慬瑳攠慸灭敬‬桴⁥祳瑮硡眠畯摬戠㩥‍䴉卹慴正搼畯汢㹥洠㌨㌬㬩

汁潬獷礠畯琠⁯慥楳祬猠潴敲愠祮桴湩⁧楷桴畯⁴牷瑩湩⁧⁡潣瑮楡敮⁲潹牵敳晬圍汩⁬楧敶礠畯琠敨洠獯⁴楨敤畯⁳潣灭汩⁥牥潲獲攠敶⁲晩礠畯甠敳琠敨⁭湩潣牲捥汴⹹�

呓⁌硥浡汰�

獵湩⁧慮敭灳捡⁥瑳㭤琍灹摥晥氠獩㱴湩㹴椠瑮楬瑳഻祴数敤⁦湩汴獩㩴椺整慲潴⁲湩汴獩䥴整㭲഍湩汴獩⁴㭶瘍瀮獵彨慢正㐨㬩植瑮楬瑳瑉牥愠഻潦⡲⁡‽⹶敢楧⡮㬩愠℠‽⹶湥⡤㬩⬠愫ഩൻ椉瑮挠㴠⠠愪㬩納�

潎⁷潣灭汩⁥湡⁤畲⁮⁡楳灭敬挠⬫瀠潲牧浡

潃灭汩瑡潩⁮潍敤�

牐灥潲散獳牯刍獥汯敶⁳污⁬牰灥潲散獳牯搠物捥楴敶൳椣据畬敤‬搣晥湩⁥慭牣獯‬椣摦晥‬瑥⹣䌍浯楰敬൲潃癮牥獴琠硥⁴湩潴漠橢捥⁴楦敬൳慍⁹慨敶甠牮獥汯敶⁤湩整潲橢捥⁴敲敦敲据獥䰍湩敫൲敒潳癬獥愠汬椠瑮牥扯敪瑣爠晥牥湥散⁳漨⁲楧敶⁳潹⁵⁡楬歮牥攠牲牯ഩ牃慥整⁳桴⁥楢慮祲攠數畣慴汢൥潌摡牥䰍慯獤琠敨瀠潲牧浡椠瑮⁯䅒⁍湡⁤畲獮琠敨洠楡⡮ 畦据楴湯

桔⁥䔠摮吋慨歮礠畯�
```

### Slide 49

```
畊瑳氠歩⁥慪慶മ畂⁴潹⁵慨敶琠⁯桴湩⁫扡畯⁴潰湩整獲�
```

### Slide 50

```
潎朠牡慢敧挠汯敬瑣潩⹮�
```

### Slide 51

```
潮整挠湯瑳椠⁳慰瑲漠⁦桴⁥敲畴湲琠灹ⱥ愠摮猠⁯獩椠⁮潢桴搠捥慬慲楴湯愠摮搠晥湩瑩潩�
```

### Slide 52

```
潄獥琠楨⁳潧栠牥㽥㼿
```
