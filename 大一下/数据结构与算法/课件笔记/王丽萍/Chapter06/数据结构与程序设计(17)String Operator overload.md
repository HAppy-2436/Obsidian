# Chapter 06 — 抽象数据类型与运算符重载 — 数据结构与程序设计(17)String Operator overload

- 章节编号: Chapter06 (#17)
- 来源路径: `C:\Users\Li\OneDrive\Backup\1\大一下\2024数据结构与算法wlp\历年\王丽i萍 数据结构与算法\王丽i萍 数据结构与算法\chapter06-03\数据结构与程序设计(17)String Operator overload.ppt`
- 提取的页面组数: 32
- 核心数据结构/算法: 数组, 指针, 类, 运算符重载, 运算符, 字符串
- 时间复杂度: (无显式标注)
- 代码示例: 有 (匹配度=7)
- 关键例题: (未识别)

---

## 提取的原始内容

> 自动从 MS-PPT 二进制格式 (`TextCharsAtom` / `TextBytesAtom`) 提取，共 32 个文本组。

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
数据结构与程序设计(17)

王丽苹
lipingwang@sei.ecnu.edu.cn

课程内容安排

C String 与 String的比较。
讨论C++中String Class的实现方法。

C String 与 String Class

string class: string class in the standard library accessed by #include <string>

C strings: can be accessed by #include <cstring>
    A String constant is stored as a char array. 即一个常量的string被认为是cstring
   e.g.: “Hello everyone” // cstring
      string s = “Hello everyone” //String object
```

### Slide 5

```
A C string is a char array terminated by the null character ‘\0’  ( with ASCII value 0 ).
A C string variable can be initialized in its declaration in following ways.

char  message [ 8 ]  =  { ‘H’, ‘e’, ‘l’, ‘l’, ‘o’, ‘\0’ };

char  message [ 8 ]  =  “Hello” ;

Char *message = “hello”;
```

### Slide 6

```
‘H’      ‘e’       ‘l’        ‘l’       ‘o’       ‘\0’
```

### Slide 7

```
字符串 (String)
```

### Slide 8

```
字符串是n (  0 ) 个字符的有限序列，记作
S : “c1c2c3…cn”
其中，S 是串名字
           “c1c2c3…cn” 是串值
           ci 是串中字符
            n 是串的长度。
```

### Slide 9

```
//字符串的拷贝操作。
char *strcpy(char *to, char *from);
Pre: The string from has been initialized.
Post: The function copies string from to string to, including ‘\0’; it returns a pointer to the beginning of the string to.
//将from指向的内容链接在to的内容之后
char *strcat(char *to, char *from);
Pre: The strings from and to have been initialized.
Post: The function copies string from to the end of string to,including ‘\0’; it returns a pointer to the beginning of the string to.
```

### Slide 10

```
//求字符串的长度
int strlen(char *s);
Pre: The string s has been initialized.
Post: The function returns the length of the string s, not including the null byte ‘\0’ at the end of the string s.
//字符串的比较操作。
int strcmp(char *s1, char *s2);
Pre: The strings s1 and s2 have been initialized.
Post: The function compares string s1 to string s2; it returns< 0 if s1 < s2, 0 if s1 == s2, or > 0 if s1 > s2.
```

### Slide 11

```
//返回s2第一次在s1中出现的位置。
char *strstr(char *s1, char *s2);
Pre: The strings s1 and s2 have been initialized.
Post: The function returns a pointer to the first occurrence of the string s2 in the string s1, or it returns NULL if the string s2 is not present in s1.
```

### Slide 12

```
“ Important string”

“ acquires an alias”
```

### Slide 13

```
// ******************************************************
//  PrintName program
//  This program prints a name in two different formats
// ******************************************************

#include <iostream>		// for cout and endl
#include <string>		// for data type string

using namespace std;

const  string  FIRST = “Herman”;  // Person’s first name
const  string  LAST =  “Smith”;   // Person’s last name
const  char    MIDDLE = ‘G’;      // Person’s middle initial
```

### Slide 14

```
int  main( )
{
     string    firstLast;    //  Name in first-last format
     string    lastFirst;	  //  Name in last-first format

     firstLast = FIRST + “ “ + LAST ;
     cout  << “Name in first-last format is “  << endl
	    << firstLast  <<  endl;

     lastFirst = LAST + “, “ + FIRST + ’ ’ ;
     cout  << “Name in first-last format is “  << endl
	    << lastFirst  <<  MIDDLE  <<  ’.’  <<  endl;

     return  0;
}
```

### Slide 15

```
运算符重载，全局方法
```

### Slide 16

```
全局函数的实现Operator Overload
```

### Slide 17

```
void write(String &s)
/* Post: The String parameters is written to cout . */
{
cout << s.c_str( ) << endl;
}

注意：
Char *p = “hello”;
Cout<<p;//将输出字符串hello的值。
```

### Slide 18

```
目录String下例程
上机完成String

课后作业
```

### Slide 19

```
第一次实例化时，调用相应构造函数。
	String s1="s1 string";  //调用String (const char * copy)
	String s2=s1;  //调用String (const String &copy)

无操作符重载
	s1=“s1 string2”;  //“s1 string2”采用String (const char * copy)构造临时String tmp,缺省赋值后，调用析构函数释放tmp，s1无意义。
	s2=s1；
//缺省赋值后，s2无意义。

有void operator = (const String &copy)操作符重载，无void operator = (const char * copy)操作符重载。
	s1=“s1 string2”;
//“s1 string2”采用String (const char * copy)构造临时String tmp,采用void operator = (const String &copy)操作符重载赋值后，调用析构函数释放tmp ，s1有内容“s1 string2”。

有void operator = (const String &copy)操作符重载，有void operator = (const char * copy)操作符重载。
	s1=“s1 string2”;
//采用void operator = (const char * copy)操作符重载赋值，s1有内容“s1 string2”。
```

### Slide 20

```
1. 编译器将根据类型调用，cstring的标准函数。
strcpy(copy, cfirst);
strcat(copy, csecond);

2. 需要对=进行重载才能够使得以下语句成立。
add_to = copy;

桗瑡椠⁳⁡⁃瑓楲杮‿桃牡愠牲祡
```

### Slide 21

```
敭獳条⁥せ⁝††嬠崱††††㉛⁝†††嬠崳††††嬠崴††††嬠崵††††㙛⁝†††嬠崷
```

### Slide 22

```
畦据楴湯⁳桴瑡洠湡灩汵瑡⁥ⵃ瑳楲杮�
```

### Slide 23

```
瑓楲杮⁳湩䌠

按慨⁲‪㵰栢汥潬眠牯摬㬢†⼯慣❮⁴敢眠楲瑴湥ऍ档牡⨠焠渽睥挠慨孲瑳汲湥瀨⬩崱഻猉牴灣⡹ⱱ⥰഻按畯㱴焼㰼湥汤഻⼉焯瀽഻瀉焽഻⨉㵰䠧㬧‍†挠畯㱴焼㰼湥汤഻按畯㱴瀼㰼湥汤഻�

档牡⨠瑳捲祰挨慨⁲琪Ɐ挠慨⁲昪潲⥭ൻ†椉瑮椠഻†昉牯椨〽昻潲孭嵩㴡尧✰椻⬫琩孯嵩昽潲孭嵩഻†琉孯嵩✽ぜ㬧‍ठ敲畴湲琠㭯納

湩⁴猠牴敬⡮档牡⨠猠ഩൻ††湩⁴㭩‍†映牯椨〽猻楛⅝✽ぜ㬧⭩⤫഻††敲畴湲⠠⥩഻�

潃灭牡獩湯

佂䭏倠㌲‴楆畧敲㘠㔮�
```

### Slide 24

```
㉓㴠猠�
```

### Slide 25

```
ⵃ瑳楲杮⁳牡⁥楷敤祬愠慶汩扡敬മⵃ瑳楲杮⁳牡⁥敶祲攠晦捩敩瑮മⵃ瑳楲杮漠橢捥獴愠敲渠瑯攠据灡畳慬整⹤䌍猭牴湩獧愠敲攠獡⁹潴洠獩獵ⱥ眠瑩⁨潣獮煥敵据獥琠慨⁴慣⁮敢搠獩獡牴畯⹳䤍⁴獩攠獡⁹潦⁲⁡汣敩瑮琠⁯牣慥整攠瑩敨⁲慧扲条⁥牯愠楬獡獥映牯䌠猭牴湩⁧慤慴�
```

### Slide 26

```
⭃‫牐杯慲⵭匭䱔匠剔义�

⭃‫潃敤䌠湯楴畮摥
```

### Slide 27

```
畏灴瑵漠⁦牐杯慲�

†慎敭椠⁮楦獲⵴慬瑳映牯慭⁴獩䠠牥慭⁮浓瑩൨†慎敭椠⁮慬瑳昭物瑳椭楮楴污映牯慭⁴獩匠業桴‬效浲湡䜠�

浉汰浥湥慴楴湯漠⁦瑓楲杮䌠慬獳

汣獡⁳瑓楲杮笠瀍扵楬㩣⼠ 敭桴摯⁳景琠敨猠牴湩⁧䑁ൔ匉牴湩⡧⤠഻縉瑓楲杮 㬩ऍ瑓楲杮⠠潣獮⁴瑓楲杮☠潣祰㬩⼠ 潣祰挠湯瑳畲瑣牯ऍ瑓楲杮⠠潣獮⁴档牡⨠挠灯⥹※⼯挠湯敶獲潩⁮牦浯䌠猭牴湩൧匉牴湩⁧䰨獩㱴档牡‾挦灯⥹※⼯挠湯敶獲潩⁮牦浯䰠獩൴瘉楯⁤灯牥瑡牯㴠⠠潣獮⁴瑓楲杮☠潣祰㬩ऍ潣獮⁴档牡⨠彣瑳⡲⤠挠湯瑳※⼯挠湯敶獲潩⁮潴䌠猭祴敬猠牴湩൧牰瑯捥整㩤ऍ档牡⨠湥牴敩㭳ऍ湩⁴敬杮桴഻㭽
```

### Slide 28

```
潢汯漠数慲潴⁲㴽⠠潣獮⁴瑓楲杮☠獲ⱴ挠湯瑳匠牴湩⁧猦捥湯⥤഻潢汯漠数慲潴⁲‾挨湯瑳匠牴湩⁧爦瑳‬潣獮⁴瑓楲杮☠敳潣摮㬩戍潯⁬灯牥瑡牯㰠⠠潣獮⁴瑓楲杮☠獲ⱴ挠湯瑳匠牴湩⁧猦捥湯⥤഻潢汯漠数慲潴⁲㴾⠠潣獮⁴瑓楲杮☠獲ⱴ挠湯瑳匠牴湩⁧猦捥湯⥤഻潢汯漠数慲潴⁲㴼⠠潣獮⁴瑓楲杮☠獲ⱴ挠湯瑳匠牴湩⁧猦捥湯⥤഻潢汯漠数慲潴⁲㴡⠠潣獮⁴瑓楲杮☠獲ⱴ挠湯瑳匠牴湩⁧猦捥湯⥤഻
```

### Slide 29

```
瑓楲杮挠湯瑳畲瑣牯

瑓楲杮㨠›瑓楲杮⠠ഩൻ攉瑮楲獥㴠渠睥挠慨孲崱഻攉瑮楲獥せ⁝‽尧✰഻氉湥瑧⁨‽㬰納

瑓楲杮㨠›瑓楲杮⠠楌瑳挼慨㹲☠湩江獩⥴⼍‪潐瑳›桔⁥瑓楲杮椠⁳湩瑩慩楬敺⁤祢琠敨挠慨慲瑣牥䰠獩⁴湩江獩⁴‮⼪笍ऍ敬杮桴㴠椠彮楬瑳献穩⡥⤠഻攉瑮楲獥㴠渠睥挠慨孲敬杮桴⬠ㄠ㭝ऍ潦⁲椨瑮椠㴠〠※⁩‼敬杮桴※⭩⤫椠彮楬瑳爮瑥楲癥⡥Ⱪ攠瑮楲獥楛⥝഻攉瑮楲獥汛湥瑧嵨㴠✠ぜ㬧納
```

### Slide 30

```
潣獮⁴档牡匪牴湩⁧㨺挠獟牴  潣獮൴⨯倠獯㩴䄠瀠楯瑮牥琠⁯⁡敬慧⁬ⵃ瑳楲杮漠橢捥⁴慭捴楨杮琠敨匠牴湩⁧獩爠瑥牵敮⹤⨠യൻ爉瑥牵⁮挨湯瑳挠慨⁲⤪攠瑮楲獥഻�

潢汯漠数慲潴⁲㴽⠠潣獮⁴瑓楲杮☠楦獲ⱴ挠湯瑳匠牴湩⁧猦捥湯⥤⼍‪潐瑳›敒畴湲琠畲⁥晩琠敨匠牴湩⁧楦獲⁴条敲獥眠瑩⁨瑓楲杮猠捥湯⁤‮汅敳›敒畴湲映污敳⸠⨠യൻ爉瑥牵⁮瑳捲灭昨物瑳挮獟牴 Ⱙ猠捥湯⹤彣瑳⡲⤠ 㴽〠഻ൽ

畆据楴湯传敶汲慯�

潶摩猠牴慣⡴瑓楲杮☠摡彤潴‬潣獮⁴瑓楲杮☠摡彤湯ഩ⨯倠獯㩴吠敨映湵瑣潩⁮潣据瑡湥瑡獥匠牴湩⁧摡彤湯漠瑮⁯桴⁥湥⁤景匠牴湩⁧摡彤潴⸠⨍യൻ潣獮⁴档牡⨠晣物瑳㴠愠摤瑟⹯彣瑳⡲⤠഻潣獮⁴档牡⨠獣捥湯⁤‽摡彤湯挮獟牴 㬩挍慨⁲挪灯⁹‽敮⁷档牡獛牴敬⡮晣物瑳 ‫瑳汲湥挨敳潣摮 ‫崱഻瑳捲祰挨灯ⱹ挠楦獲⥴഻瑳捲瑡挨灯ⱹ挠敳潣摮㬩愍摤瑟⁯‽潣祰※⼯ി敤敬整嬠⁝潣祰഻�

慍湩倠潲牧浡

瑓楲杮爠慥彤湩椨瑳敲浡☠湩異⥴⼍‪潐瑳›敒畴湲愠匠牴湩⁧敲摡⠠獡挠慨慲瑣牥⁳整浲湩瑡摥戠⁹⁡敮⁷楬敮漠⁲湡攠摮漭ⵦ楦敬挠慨慲瑣牥 牦浯愠⁮獩牴慥⁭慰慲敭整⹲⨠യൻ楌瑳挼慨㹲琠浥㭰植瑮猠穩⁥‽㬰挍慨⁲㭣眍楨敬⠠挨㴠椠灮瑵瀮敥⡫⤠ 㴡䔠䙏☠…挨㴠椠灮瑵朮瑥 ⤩℠‽尧❮ഩ整灭椮獮牥⡴楳敺⬫‬⥣഻瑓楲杮愠獮敷⡲整灭㬩爍瑥牵⁮湡睳牥഻�
```

### Slide 31

```
獯牴慥⁭…灯牥瑡牯㰠‼漨瑳敲浡☠漠瑵異ⱴ匠牴湩⁧ㅳ笩ऍ畯灴瑵㰠‼ㅳ挮獟牴  㰼攠摮㭬ऍ敲畴湲漠瑵異㭴納

潶摩洠楡⡮笩ഉ††††瑓楲杮猠㴱猢‱瑳楲杮㬢ऍ潣瑵㰼ㅳ挮獟牴⤨㰼湥汤഻按畯㱴猼牴敬⡮ㅳ挮獟牴⤨㰩攼摮㭬ऍ瑓楲杮猠⠲猢′瑳楲杮⤢഻按畯㱴猼⸲彣瑳⡲㰩攼摮㭬ऍ潣瑵㰼瑳汲湥猨⸲彣瑳⡲⤩㰼湥汤�

敒畳瑬

ㅳ猠牴湩൧ഹ㉳猠牴湩൧�

ऍ晩猨㸱猽⤲挠畯㱴∼ㅳ㴾㉳㰢攼摮㭬ऍ汥敳挠畯㱴∼ㅳ猼∲㰼湥汤഻猉㴲ㅳ഻椉⡦ㅳ㴽㉳ 潣瑵㰼猢㴱㉳㰢攼摮㭬ऍ汥敳挠畯㱴∼ㅳ㴡㉳㰢攼摮㭬

ㅳ猼ലㅳ猽�

匉牴湩⁧㍳爽慥彤湩挨湩㬩ऍ瑳捲瑡猨ⰳㅳ㬩ऍ牷瑩⡥㍳㬩納

敨摡栍慥獤‱瑳楲杮�
```

### Slide 32

```
䈍住⁋㉐ㄴ䔠�

潃祰挠湯瑳畲瑣牯愠摮漠数慲潴⁲�
```

### Slide 33

```
桔⁥畦据楴湯瀠敥⡫ 獩甠敳⁤楷桴椠灮瑵猠牴慥獭‬湡⁤敲畴湲⁳桴⁥敮瑸挠慨慲瑣牥椠⁮桴⁥瑳敲浡漠⁲佅⁆晩琠敨攠摮漠⁦楦敬椠⁳敲摡‮数步⤨搠敯⁳潮⁴敲潭敶琠敨挠慨慲瑣牥映潲⁭桴⁥瑳敲浡‮
```
