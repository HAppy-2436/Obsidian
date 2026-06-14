# Chapter 07 — 查找 — 数据结构与程序设计(18) searching

- 章节编号: Chapter07 (#18)
- 来源路径: `C:\Users\Li\OneDrive\Backup\1\大一下\2024数据结构与算法wlp\历年\王丽i萍 数据结构与算法\王丽i萍 数据结构与算法\chapter07-01\数据结构与程序设计(18) searching.ppt`
- 提取的页面组数: 26
- 核心数据结构/算法: 线性表, 查找, 运算符, 构造函数, 顺序, 二分查找, 类, 表
- 时间复杂度: (无显式标注)
- 代码示例: 有 (匹配度=6)
- 关键例题: (未识别)

---

## 提取的原始内容

> 自动从 MS-PPT 二进制格式 (`TextCharsAtom` / `TextBytesAtom`) 提取，共 26 个文本组。

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
数据结构与程序设计(18)

王丽苹
lipingwang@sei.ecnu.edu.cn

Information retrieval is one of the important applications of computers.
We are given a list of records, where each record is associated with one piece of information, which we shall call a key(关键字). (BOOK P269 FIGURE 7.1)
本章讨论顺序存储列表的查找操作，链接存储在第10章讨论。
```

### Slide 5

```
The searching problem falls naturally into two cases.
Internal searching（内部查找） means that all the records are kept in high-speed memory.
In external searching（外部查找）, most of the records are kept in disk files.
We study only internal searching.
```

### Slide 6

```
void main(){
	Key target(5);
	Record myrecord(5,9);
	if (target==myrecord)  cout<<"yes"<<endl;
	else cout<<"no"<<endl;

}

调用operator Key( )构造临时Key tmp,采用void operator == (const Key &x, const Key &y)操作符比较。

Output:
yes
```

### Slide 7

```
目录SeqSearch下例程

Recorder中的成员operator Key( );主要完成从Recorder对象到Key对象的自动转换。可以用其他方法完成该功能。

Use constructor to conversion from Record to Key .
```

### Slide 8

```
void main(){
	Key target(5);
	Record myrecord(5,9);
	if (target==myrecord)  cout<<"yes"<<endl;
	else cout<<"no"<<endl;
}

调用Key(const Record &r)构造临时Key tmp,采用void operator == (const Key &x, const Key &y)操作符比较后，调用析构函数释放tmp。

Output:
yes
```

### Slide 9

```
目录SeqSearch2下例程

Sequential Search 顺序查找 P272
```

### Slide 10

```
Sequential search is easy to write and efficient for short lists, but a disaster for long ones.
One of the best methods for a list with keys in order is binary search.

首先讨论如何构建一个有序的列表。
然后讨论针对顺序列表的二分查找。
```

### Slide 11

```
有序列表的定义：
DEFINITION
An ordered list is a list in which each entry contains a key, such that the keys are in order. That is, if entry i comes before entry j in the list, then the key of entry i is less than or equal to the key of entry j .
```

### Slide 12

```
Error_code Ordered_list :: insert(const Record &data)
/* Post: If the Ordered_list is not full, the function succeeds: The Record data is inserted into the list, following the last entry of the list with a strictly lesser key (or in the first list position if no list element has a lesser key).
Else: the function fails with the diagnostic Error_code overflow. */
{
	int s = size( );
	int position;
	for (position = 0; position < s; position++) {
		Record list_data;
		retrieve(position, list_data);
		if (data < list_data) break;  //book p279 wrong
	}
	return List<Record> :: insert(position, data);
      //调用父类的方法。
}
```

### Slide 13

```
目录Ordered_list下例程

课后阅读

关于顺序查找的效率测试。
课后阅读P274 3.testing
理解函数test_search//统计查找成功和查找不成功时的比较次数。

桃灡整⁲‷䕓剁䡃义େ
```

### Slide 14

```
桃灡整⁲‷䕓剁䡃义�

敗愠敲朠癩湥漠敮欠祥‬慣汬摥琠敨琠牡敧ⱴ愠摮愠敲愠歳摥琠⁯敳牡档琠敨氠獩⁴潴映湩⁤桴⁥敲潣摲猨 椨⁦湡⥹眠潨敳欠祥椠⁳桴⁥慳敭愠⁳桴⁥慴杲瑥മ敗漠瑦湥愠歳栠睯琠浩獥漠敮欠祥椠⁳潣灭牡摥眠瑩⁨湡瑯敨⁲畤楲杮愠猠慥捲⹨吠楨⁳楧敶⁳獵愠朠潯⁤敭獡牵⁥景琠敨琠瑯污愠潭湵⁴景眠牯⁫桴瑡琠敨愠杬牯瑩浨眠汩⁬潤മ
```

### Slide 15

```
浉汰浥湥慴楴湯漠⁦敋⁹汃獡�

挍慬獳䬠祥笠ऍ湩⁴敫㭹瀍扵楬㩣ऍ敋⁹椨瑮砠㴠〠㬩ऍ湩⁴桴彥敫⡹⤠挠湯瑳഻㭽഍潢汯漠数慲潴⁲㴽⠠潣獮⁴敋⁹砦‬潣獮⁴敋⁹礦㬩

敋㩹䬺祥椨瑮砠笩ऍ敫㵹㭸納഍湩⁴敋㩹琺敨歟祥⤨挠湯瑳ൻ爉瑥牵⁮敫㭹納഍潢汯漠数慲潴⁲㴽⠠潣獮⁴敋⁹砦‬潣獮⁴敋⁹礦ഩൻ爉瑥牵⁮⹸桴彥敫⡹⤠㴠‽⹹桴彥敫⡹⤠഻�

浉汰浥湥慴楴湯漠⁦敒潣摲䌠慬獳

汣獡⁳敒潣摲ൻ異汢捩ഺ漉数慲潴⁲敋⡹⤠※⼯椠灭楬楣⁴潣癮牥楳湯映潲⁭उउ†敒潣摲琠⁯敋⁹മ刉捥牯⡤湩⁴㵸ⰰ椠瑮礠〽㬩瀍楲慶整ഺ椉瑮欠祥഻椉瑮漠桴牥഻㭽

敒潣摲㨺敒潣摲椨瑮砠‬湩⁴⥹ൻ欉祥砽഻漉桴牥礽഻ൽ刍捥牯㩤漺数慲潴⁲敋⡹⤠ൻ䬉祥琠灭欨祥㬩納

敔瑳䴠楡�
```

### Slide 16

```
浉汰浥湥慴楴湯漠⁦敓牡档

湁瑯敨⁲敍桴摯
```

### Slide 17

```
汣獡⁳敋⁹ൻ椉瑮欠祥഻異汢捩ഺ䬉祥⠠湩⁴⁸‽⤰഻䬉祥⠠潣獮⁴敒潣摲☠⥲഻椉瑮琠敨歟祥  潣獮㭴納഻戍潯⁬灯牥瑡牯㴠‽挨湯瑳䬠祥☠ⱸ挠湯瑳䬠祥☠⥹�

敋㩹䬺祥椨瑮砠笩ऍ敫㵹㭸納഍敋㩹䬺祥挨湯瑳删捥牯⁤爦笩ऍ敫㵹⹲桴彥敫⡹㬩納഍湩⁴敋㩹琺敨歟祥⤨挠湯瑳ൻ爉瑥牵⁮敫㭹納഍潢汯漠数慲潴⁲㴽⠠潣獮⁴敋⁹砦‬潣獮⁴敋⁹礦ഩൻ爉瑥牵⁮⹸桴彥敫⡹⤠㴠‽⹹桴彥敫⡹⤠഻�

汣獡⁳敒潣摲ൻ異汢捩ഺ刉捥牯⡤湩⁴㵸ⰰ椠瑮礠〽㬩ऍ湩⁴桴彥敫⡹ 潣獮㭴瀍楲慶整ഺ椉瑮欠祥഻椉瑮漠桴牥഻㭽

敒潣摲㨺敒潣摲椨瑮砠‬湩⁴⥹ൻ欉祥砽഻漉桴牥礽഻ൽ植瑮删捥牯㩤琺敨歟祥⤨挠湯瑳ൻ爉瑥牵⁮敫㭹納
```

### Slide 18

```
䔍牲牯损摯⁥敳畱湥楴污獟慥捲⡨潣獮⁴楌瑳刼捥牯㹤☠桴彥楬瑳ബ潣獮⁴敋⁹琦牡敧ⱴ椠瑮☠潰楳楴湯ഩ⨯倠獯㩴䤠⁦湡攠瑮祲椠⁮桴⁥楬瑳栠獡欠祥攠畱污琠⁯慴杲瑥Ⱐ琠敨⁮敲畴湲猠捵散獳愠摮琠敨漍瑵異⁴慰慲敭整⁲潰楳楴湯氠捯瑡獥猠捵⁨湡攠瑮祲眠瑩楨⁮桴⁥楬瑳മ瑏敨睲獩⁥敲畴湲渠瑯灟敲敳瑮愠摮瀠獯瑩潩⁮敢潣敭⁳湩慶楬⹤⨠യൻ湩⁴⁳‽桴彥楬瑳献穩⡥⤠഻潦⁲瀨獯瑩潩⁮‽㬰瀠獯瑩潩⁮‼㭳瀠獯瑩潩⭮⤫笠‍†删捥牯⁤慤慴഻††桴彥楬瑳爮瑥楲癥⡥潰楳楴湯‬慤慴㬩‍†椠⁦琨牡敧⁴㴽搠瑡⥡爠瑥牵⁮畳捣獥㭳納爍瑥牵⁮潮彴牰獥湥㭴納
```

### Slide 19

```
湁污獹獩

䈍住⁋㉐㌷名敨渠浵敢⁲景挠浯慰楲潳獮漠⁦敫獹搠湯⁥湩猠煥敵瑮慩⁬敳牡档漠⁦⁡楬瑳漠⁦敬杮桴渠椠㩳唍獮捵散獳畦⁬敳牡档›⁮潣灭牡獩湯⹳匍捵散獳畦⁬敳牡档‬敢瑳挠獡㩥ㄠ挠浯慰楲潳⹮匍捵散獳畦⁬敳牡档‬潷獲⁴慣敳›⁮潣灭牡獩湯⹳匍捵散獳畦⁬敳牡档‬癡牥条⁥慣敳›渨⬠ㄠ⼩㈠挠浯慰楲潳獮മ

楂慮祲匠慥捲�
```

### Slide 20

```
牏敤敲⁤楌瑳�
```

### Slide 21

```
挍慬獳传摲牥摥江獩㩴瀠扵楬⁣楌瑳刼捥牯㹤ൻ異汢捩ഺ䔉牲牯损摯⁥湩敳瑲挨湯瑳删捥牯⁤搦瑡⥡഻䔉牲牯损摯⁥湩敳瑲椨瑮瀠獯瑩潩Ɱ挠湯瑳删捥牯⁤搦瑡⥡഻䔉牲牯损摯⁥敲汰捡⡥湩⁴潰楳楴湯‬潣獮⁴敒潣摲☠慤慴㬩納�
```

### Slide 22

```
牅潲彲潣敤传摲牥摥江獩⁴㨺椠獮牥⡴潣獮⁴敒潣摲☠慤慴ഩ⨯倠獯㩴䤠⁦桴⁥牏敤敲彤楬瑳椠⁳潮⁴畦汬‬桴⁥畦据楴湯猠捵散摥㩳吠敨删捥牯⁤慤慴椠⁳湩敳瑲摥椠瑮⁯桴⁥楬瑳‬潦汬睯湩⁧桴⁥慬瑳攠瑮祲漠⁦桴⁥楬瑳眠瑩⁨⁡瑳楲瑣祬氠獥敳⁲敫⁹漨⁲湩琠敨映物瑳氠獩⁴潰楳楴湯椠⁦潮氠獩⁴汥浥湥⁴慨⁳⁡敬獳牥欠祥⸩䔍獬㩥琠敨映湵瑣潩⁮慦汩⁳楷桴琠敨搠慩湧獯楴⁣牅潲彲潣敤漠敶晲潬⹷⨠�
```

### Slide 23

```
牅潲彲潣敤传摲牥摥江獩⁴㨺椠獮牥⡴湩⁴潰楳楴湯‬潣獮⁴敒潣摲☠慤慴ഩ⨯倠獯㩴䤠⁦桴⁥牏敤敲⁤楬瑳椠⁳潮⁴畦汬‬‰㴼瀠獯瑩潩⁮㴼渠Ⱐ眠敨敲渠椠⁳桴⁥畮扭牥漠⁦湥牴敩⁳湩琠敨氠獩ⱴ愠摮琠敨删捥牯⁤慤慴挠湡戠⁥湩敳瑲摥愠⁴潰楳楴湯椠⁮桴⁥楬瑳‬楷桴畯⁴楤瑳牵楢杮琠敨氠獩⁴牯敤Ⱳ琠敨⁮桴⁥畦据楴湯猍捵散摥㩳䄠祮攠瑮祲映牯敭汲⁹湩瀠獯瑩潩⁮湡⁤污⁬慬整⁲湥牴敩⁳慨敶琠敨物瀠獯瑩潩⁮畮扭牥⁳湩牣慥敳⁤祢ㄠ愠摮搠瑡⁡獩椠獮牥整⁤瑡潰楳楴湯漠⁦桴൥楌瑳⸠ഠ汅敳›桴⁥畦据楴湯映楡獬眠瑩⁨⁡楤条潮瑳捩䔠牲牯损摯⁥‮⼪
```

### Slide 24

```
牅潲彲潣敤传摲牥摥江獩⁴㨺椠獮牥⡴湩⁴潰楳楴湯‬潣獮⁴敒潣摲☠慤慴ഩ⨯倠獯㩴††猠捵散摥㩳䄠祮攠瑮祲映牯敭汲⁹湩瀠獯瑩潩⁮湡⁤污⁬慬整⁲湥牴敩⁳慨敶琠敨物‍†䔠獬㩥琠敨映湵瑣潩⁮慦汩⁳楷桴愠搠慩湧獯楴⁣牅潲彲潣敤⸠⨠യൻ刉捥牯⁤楬瑳摟瑡㭡ऍ晩⠠潰楳楴湯㸠〠 ⽻琯敨氠晥⁴景琠敨椠獮牥⁴慤慴ऍ爉瑥楲癥⡥潰楳楴湯ⴠㄠ‬楬瑳摟瑡⥡഻उ晩⠠慤慴㰠氠獩彴慤慴ഩउ爉瑥牵⁮慦汩഻紉ഉ椉⁦瀨獯瑩潩⁮‼楳敺 ⤩笠⼯桴⁥楲桧⁴景琠敨椠獮牥⁴慤慴ऍ爉瑥楲癥⡥潰楳楴湯‬楬瑳摟瑡⥡഻उ晩⠠慤慴㸠氠獩彴慤慴ഩउ爉瑥牵⁮慦汩഻紉ऍ敲畴湲䰠獩㱴敒潣摲‾㨺椠獮牥⡴潰楳楴湯‬慤慴㬩納
```

### Slide 25

```
牅潲彲潣敤传摲牥摥江獩⁴㨺爠灥慬散椨瑮瀠獯瑩潩Ɱ挠湯瑳删捥牯⁤搦瑡⥡笍ऍ晩⠠潰楳楴湯㰠〠簠⁼潰楳楴湯㸠‽潣湵⥴敲畴湲爠湡敧敟牲牯഻刉捥牯⁤楬瑳摟瑡㭡ऍ晩⠠潰楳楴湯㸠〠 ⽻琯敨氠晥⁴景琠敨椠獮牥⁴慤慴ऍ爉瑥楲癥⡥潰楳楴湯ⴠㄠ‬楬瑳摟瑡⥡഻उ晩⠠慤慴㰠氠獩彴慤慴ഩउ爉瑥牵⁮慦汩഻紉ഉ椉⁦瀨獯瑩潩⁮‼楳敺 ⴩⤱笠⼯桴⁥楲桧⁴景琠敨椠獮牥⁴慤慴ऍ爉瑥楲癥⡥潰楳楴湯‫ⰱ氠獩彴慤慴㬩ऍ椉⁦搨瑡⁡‾楬瑳摟瑡⥡ऍउ敲畴湲映楡㭬ऍൽ攉瑮祲灛獯瑩潩嵮㴠搠瑡㭡ऍ敲畴湲猠捵散獳഻�
```

### Slide 26

```
汣獡⁳敒潣摲ൻ異汢捩ഺ刉捥牯⡤㬩ऍ敒潣摲椨瑮砠‬湩⁴㵹⤰഻椉瑮琠敨歟祥⤨挠湯瑳഻牰癩瑡㩥ऍ湩⁴敫㭹ऍ湩⁴瑯敨㭲納഻഍潢汯漠数慲潴⁲‾挨湯瑳删捥牯⁤砦‬潣獮⁴敒潣摲☠⥹഻戍潯⁬灯牥瑡牯㰠⠠潣獮⁴敒潣摲☠ⱸ挠湯瑳删捥牯⁤礦㬩഍獯牴慥⁭…灯牥瑡牯㰠‼漨瑳敲浡☠畯灴瑵‬敒潣摲☠⥸�
```

### Slide 27

```
敒潣摲㨺敒潣摲⤨ൻ欉祥〽഻漉桴牥〽഻ൽ刍捥牯㩤刺捥牯⡤湩⁴ⱸ椠瑮礠笩ऍ敫㵹㭸ऍ瑯敨㵲㭹納഍湩⁴敒潣摲㨺桴彥敫⡹ 潣獮筴ऍ敲畴湲欠祥഻�

潢汯漠数慲潴⁲‾挨湯瑳删捥牯⁤砦‬潣獮⁴敒潣摲☠⥹笍ऍ敲畴湲砠琮敨歟祥  ‾⹹桴彥敫⡹⤠഻ൽ戍潯⁬灯牥瑡牯㰠⠠潣獮⁴敒潣摲☠ⱸ挠湯瑳删捥牯⁤礦ഩൻ爉瑥牵⁮⹸桴彥敫⡹⤠㰠礠琮敨歟祥 㬩納഍獯牴慥⁭…灯牥瑡牯㰠‼漨瑳敲浡☠畯灴瑵‬敒潣摲☠⥸笍ऍ畯灴瑵㰼⹸桴彥敫⡹㬩ऍ畯灴瑵㰼湥汤഻爉瑥牵⁮畯灴瑵഻�

牏敤敲⁤楌瑳⵳䴭楡�

整灭慬整㰠汣獡⁳楌瑳敟瑮祲ാ潶摩瀠楲瑮䰨獩彴湥牴⁹砦笩ऍ潣瑵㰼㭸ഉൽ瘍楯⁤慭湩⤨ൻ伉摲牥摥江獩⁴祭楬瑳഻昉牯椨瑮椠〽椻㔼椻⬫洩汹獩⹴湩敳瑲刨捥牯⡤⩩⤲㬩ऍ祭楬瑳椮獮牥⡴敒潣摲㌨⤩഻洉汹獩⹴湩敳瑲〨刬捥牯⡤〳⤩഻按畯㱴∼潙牵氠獩⁴慨敶∠㰼祭楬瑳献穩⡥㰩∼攠敬敭瑮㩳㰢攼摮㭬ऍ祭楬瑳琮慲敶獲⡥牰湩⥴�

敒畳瑬

潙牵氠獩⁴慨敶㘠攠敬敭瑮㩳」㈍㌍㐍㘍㠍

洉汹獩⹴敲潭敶〨‬敒潣摲椨⤩഻按畯㱴∼晁整⁲敲潭敶〨㨩㰢攼摮㭬ऍ祭楬瑳琮慲敶獲⡥牰湩⥴഻�

晁整⁲敲潭敶〨㨩㈍㌍㐍㘍㠍

ऍ祭楬瑳爮灥慬散〨‬敒潣摲⴨⤱㬩ऍ潣瑵㰼䄢瑦牥爠灥慬散〨‬敒潣摲⴨⤱㨩㰢攼摮㭬ऍ祭楬瑳琮慲敶獲⡥牰湩⥴഻�

晁整⁲敲汰捡⡥ⰰ删捥牯⡤ㄭ⤩ഺㄭ㌍㐍㘍㠍
```
