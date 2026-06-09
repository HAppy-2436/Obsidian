# Chapter 09 — 表与数据访问 (Hash) — 数据结构与程序设计(23)Hash函数

- 章节编号: Chapter09 (#23)
- 来源路径: `C:\Users\Li\OneDrive\Backup\1\大一下\2024数据结构与算法wlp\历年\王丽i萍 数据结构与算法\王丽i萍 数据结构与算法\chapter09-02\数据结构与程序设计(23)Hash函数.ppt`
- 提取的页面组数: 36
- 核心数据结构/算法: 线性表, 哈希表, 类, 链地址法, 开放定址法, 探测, 链表, 数组, 查找, 哈希, 表
- 时间复杂度: (无显式标注)
- 代码示例: 有 (匹配度=7)
- 关键例题: (未识别)

---

## 提取的原始内容

> 自动从 MS-PPT 二进制格式 (`TextCharsAtom` / `TextBytesAtom`) 提取，共 36 个文本组。

### Slide 1

```
单击此处编辑母版标题样式

单击此处编辑母版文本样式
第二级
第三级
第四级
第五级
```

### Slide 2

```
数据结构与程序设计
```

### Slide 4

```
数据结构与程序设计(23)Chapter09 9.6 Hashing函数

王丽苹
lipingwang@sei.ecnu.edu.cn
```

### Slide 5

```
哈希函数

顺序查找和二分查找都是建立在“比较”的基础上，所要查找的关键字与存贮地址之间无确定的关系，故查找的效率决定于查找中比较的次数。
如果能找到一种函数，对应于每个关键字，都能唯一确定一个存贮地址，那么在查找时，只要根据给定的关键字用该函数进行计算后即可直接取得该关键字所在记录的存贮地址，从而获得待查记录。这个思想就是哈希查找的思想，相应地称这种函数为哈希函数。
Hash函数输入为：关键字
Hash函数输出为：存储位置
满足上述存储关系的表为Hash表。关键字在整个Hash表中必须要唯一。
```

### Slide 6

```
建立哈希函数带有极强的技术性和经验性，下面简单介绍几种常用方法。
1．直接哈希函数
直接哈希函数是直接取关键字或关键字的某个线性函数作为哈希函数，其特点是关键字与哈希地址之间是一对一的关系，因此不会发生冲突，但它的空间浪费严重，因为在大多数情况下，由哈希函数计算出来的地址不是连续的。
例如，对参加某一活动的同学进行登记，关键字为学生的学号，哈希函数为H(key) = key 。
```

### Slide 7

```
2．除数取余法
这种方法是先找出一个合适的正整数m，取关键字对m的余数作为哈希函数的值，即H（key）= key mod m。为了尽可能避免冲突，一般m取小于存贮区长度的尽可能大的素数。
```

### Slide 8

```
3．随机法
当关键字的长度不等时，通常采用随机函数法，先选择一个随机函数作为哈希函数，关键字对应的随机函数值即为哈希地址，即H（key）=ran (key)。
```

### Slide 9

```
在哈希表的建表过程中，若对于某个哈希函数H（k），若有两个或两个以上的关键字映射的哈希地址相同，即H（key1）= H（key2）（key1≠key2），则发生冲突。在前一节提到过，选择哈希函数时应选择均匀的，冲突较少的。但在大多数情况下，冲突是不可避免的，因此选择哈希函数和解决冲突是哈希查找中两个主要研究内容。
常用的处理冲突的方法有开放地址法和链地址法。
```

### Slide 10

```
9.6.3 开放地址法

开放地址法解决哈希冲突的思想是，将整个哈希地址区看成一个环形表，当冲突发生时，根据某种解决冲突的方法，为发生冲突的关键字找出一个“空”的地址单元作为该关键字的哈希地址。
若插入元素，则碰到空的地址单元就存放要插入的同义词。若检索元素，则需要碰到空的地址单元后，才能说明表中没有待查的元素(检索失败)。
```

### Slide 11

```
用开地址法解决冲突的方法讨论：
（1）用线性探测法：
即将基本存储区看作一个循环表。若在地址为d=h(key)的单元发生碰撞，则依次探查下述地址单元∶d+1,d+2,…,m-1,0,1,…,d-1 (m为基本存储区的长度)直到找到一个空单元或查找到关键码为key的元素为止。如果从单元d开始探查，查找一遍后，又回到地址d，则表示基本存储区已经溢出。
可能会造成 “堆积”。
```

### Slide 12

```
例子：已知关键码集合K={18，73，10，5，68，99，27，41，51，32，25}，设散列表基本区域用数组element表示，大小为m(m=13)，散列函数为h(key)=key%13，用线性探查法解决碰撞。
按散列函数d=key%13计算每个元素的散列地址如下：
h(18)=5,	h(73)=8,	h(10)=10,	h(5)=5,
h(68)=3,	h(99)=8           h(27)=1,	h(41)=2,
h(51)=12,	h(32)=6,	h(25)=12
最后的散列表为：
```

### Slide 13

```
用开地址法解决冲突的方法讨论：
（2）平方探测法
我们可以改变增量的形式，如发生冲突时，检测H(key)±1，H(key函数)±4, H(key函数)±9 ……这种方法就称为平方探测法。
（3）增量函数法
选择两个散列函数h1和h2他们均以关健字为自变量，h1产生0到m-1之间的数作为地址，如果有冲突，则计算h2的值，h2产生一个1到m-1之间的并和m互素的数作为地址的增量。
例如两个散列函数可以为h1(key)=key%m和h2(key)=key%(m-2)+1。
如果d=h1(key)发生碰撞，则再计算h2(key)，得到探查序列为∶(d+h2(key))%m,  (d+2h2(key))%m,  (d+3h2(key))%m, …
```

### Slide 14

```
开放地址法实现讨论
```

### Slide 15

```
开放地址法
```

### Slide 16

```
//以下是Hash函数的设计

int hash(const Record &new_entry){
	return new_entry.the_key()%hash_size;
}

int hash(const Key &new_entry){
	return new_entry.the_key()%hash_size;
}

Error_code insert(const Record &new_entry);
创建Hash表的方法：
(1) 计算当前待插入元素new_entry在Hash表中的位置。
(2) 判断该关键字是否唯一。不唯一则报错。
(2) 判断当前位置是否空闲：
如果空闲直接将元素放入当前位置
如果不空闲，选用冲突检测方法，计算下一个可放置的位置。
(3) 重复（2），直到找到位置，或者判断出当前表格已满。
约定：
0，表示当前位置空闲。
-1，表示当前位置的元素被删除。
```

### Slide 17

```
Error_code Hash_table :: insert(const Record &new_entry)
{
	Error_code result = success;
	int probe_count, // Counter to be sure that table is not full.
	increment, // Increment used for quadratic probing.
	probe; // Position currently probed in the hash table.
	probe = hash(new_entry);
	probe_count = 0; increment = 1;
	if(retrieve((Record)new_entry, (Record)new_entry)==success) return； duplicate_error;
	while (table[probe] != 0 // Is the location empty?
		&& table[probe] != -1 // empty because delete
		&& probe_count < (hash_size + 1)/2) { // Has overflow occurred?
		probe_count++;
		probe = (probe + increment)%hash_size;
		increment += 2; // Prepare increment for next iteration.每次递增2。
	}
	if (table[probe] == 0) table[probe] = new_entry;
	if (table[probe] == -1) table[probe] = new_entry;
	// Insert new entry.
	else result = overflow; // The table is full.
	return result;
}
```

### Slide 18

```
Error_code retrieve(const Key &target, Record &found) const;
访问Hash表：
(1) 通过Hash函数计算得到target的位置prob。
(2) 判断prob位置的值是否与target相等：
如果相等，则找到该关键字。将其内容存储于found中。
如果不相等，则根据冲突解决的方法，计算下一个地址prob。
(3) 重复步骤2，
直到找到，
或者确定target不存在于hash表中：a, 碰到Prob位置为空闲，b，计算了所有可能的位置。
```

### Slide 19

```
Error_code Hash_table :: remove(const Key &target, Record &found)
删除Hash表的一个元素。
(1) 通过Hash函数计算得到target的位置prob。
(2) 判断prob位置的值是否与target相等：
如果相等，则找到该关键字。将其内容存储于found中,将该位置置为-1。
如果不相等，则根据冲突解决的方法，计算下一个地址prob。
(3) 重复步骤2，
直到找到，则删除成功。
或者确定target不存在于hash表中：a, 碰到Prob位置为空闲，b，计算了所有可能的位置。此时删除失败。
```

### Slide 20

```
9.6.4 链地址法

拉链法解决哈希冲突的思想是将所有具有相同哈希地址的关键字连接成一个单链表。
设基本区域长度为m，使用拉链法需要建立m条链表，所有散列地址相同的元素存放在同一条链表中。
设给定元素的关键码为key，首先根据散列函数h计算出h(key)，即确定是在第h(key)条链表中，然后在该链表中进行插入、删除及检索操作。
已知关键码集合K={18，73，10，5，68，99，27，41，51，32，25}，m取13，设散列函数为h(key)=key%13，用拉链法得到的散列表如下图所示。
```

### Slide 21

```
链地址法

#include "Record.h"
#include "LinkList.cpp "

const int hash_size = 97;
class Hash_table {
public:
	void clear( );
	Error_code insert(const Record &new_entry);
	Error_code retrieve(const Key &target, Record &found) const;
	Error_code remove(const Key &target, Record &found);
private:
	List<Record> table[hash_size];//table的每一个元素为一个列表
};

int hash(const Record &new_entry);
int hash(const Key &new_entry);
```

### Slide 22

```
//仍然选用与开地址法相同的Hash函数
int hash(const Record &new_entry){
	return new_entry.the_key()%hash_size;
}

int hash(const Key &new_entry){
	return new_entry.the_key()%hash_size;
}

Error_code Hash_table :: insert(const Record &new_entry)
创建Hash表：
(1) 通过Hash函数计算得到new_entry的位置prob。
(2) 判断new_entry是否在下表为prob的List中存在。
如果存在则插入失败。
如果不存在，插入new_entry
```

### Slide 23

```
Error_code Hash_table :: retrieve(const Key &target, Record &found) const
访问关键字target：
(1) 通过Hash函数计算得到new_entry的位置prob。
(2) 判断target是否在下标为prob的List中存在。
即：逐一访问table[prob]中的每一个元素，判断是否与target相等。
```

### Slide 24

```
Error_code Hash_table :: remove(const Key &target, Record &found){
	int probe;
	probe = hash(target);
	for(int i=0; i<table[probe].size(); i++){
		Record tmp;
		table[probe].retrieve(i,tmp);
		if(target==tmp){//存在的话直接删除。
			table[probe].remove(i,found);
			return success;
		}
	}
	return not_present;//不存在的话，删除失败。
}

P411
书本9.7节
装填因子（Load factor）
For open addressing, load factor can never exceed 1;
For chaining, there is no limit on the size of load factor.

课后作业

作业：完成P409 E6（a）
请用线性探测解决冲突，写出hash表存储的内容。
上机实现链地址法哈希散列表。
```

### Slide 25

```
用平方探测来解决冲突。

增量次数需要满足的条件：2*count<size+1

湥浵䔠牲牯损摯筥潮彴牰獥湥ⱴ漠敶晲潬ⱷ搠灵楬慣整敟牲牯‬畳捣獥絳഻潣獮⁴湩⁴慨桳獟穩⁥‽㜹※挍慬獳䠠獡彨慴汢⁥ൻ異汢捩ഺ瘉楯⁤汣慥⡲⤠഻䔉牲牯损摯⁥湩敳瑲挨湯瑳删捥牯⁤渦睥敟瑮祲㬩ऍ牅潲彲潣敤爠瑥楲癥⡥潣獮⁴敋⁹琦牡敧ⱴ删捥牯⁤昦畯摮 潣獮㭴ऍ牅潲彲潣敤爠浥癯⡥潣獮⁴敋⁹琦牡敧ⱴ删捥牯⁤昦畯摮㬩瀍楲慶整ഺ刉捥牯⁤慴汢孥慨桳獟穩嵥഻㭽഍湩⁴慨桳挨湯瑳删捥牯⁤渦睥敟瑮祲㬩഍湩⁴慨桳挨湯瑳䬠祥☠敮彷湥牴⥹഻
```

### Slide 26

```
汣獡⁳敋⁹ൻ椉瑮欠祥഻異汢捩ഺ䬉祥⠠湩⁴⁸‽⤰഻椉瑮琠敨歟祥  潣獮㭴納഻戍潯⁬灯牥瑡牯㴠‽挨湯瑳䬠祥☠ⱸ挠湯瑳䬠祥☠⥹�
```

### Slide 27

```
汣獡⁳敒潣摲ൻ異汢捩ഺ漉数慲潴⁲敋⡹⤠※⼯椠灭楬楣⁴潣癮牥楳湯映潲⁭敒潣摲琠⁯敋⁹മ刉捥牯⡤湩⁴㵸ⰰ椠瑮礠〽㬩ऍ湩⁴桴彥敫⡹⤠挠湯瑳഻椉瑮琠敨潟桴牥⤨挠湯瑳഻瀍楲慶整ഺ椉瑮欠祥഻椉瑮漠桴牥഻㭽഍潢汯漠数慲潴⁲㴡⠠潣獮⁴敒潣摲☠ⱸ挠湯瑳删捥牯⁤礦㬩戍潯⁬灯牥瑡牯㴠‽挨湯瑳删捥牯⁤砦‬潣獮⁴敒潣摲☠⥹�
```

### Slide 28

```
潶摩䠠獡彨慴汢⁥㨺挠敬牡⤨ൻ昉牯椨瑮椠〽※㱩慨桳獟穩㭥椠⬫笩ऍ刉捥牯⁤浴㭰ऍ琉扡敬楛㵝浴㭰ഠ紉納
```

### Slide 29

```
牅潲彲潣敤䠠獡彨慴汢⁥㨺爠瑥楲癥⡥潣獮⁴敋⁹琦牡敧ⱴ删捥牯⁤昦畯摮 潣獮筴ऍ湩⁴牰扯彥潣湵ⱴ⼠ 潃湵整⁲潴戠⁥畳敲琠慨⁴慴汢⁥獩渠瑯映汵⹬ऍ湩牣浥湥ⱴ⼠ 湉牣浥湥⁴獵摥映牯焠慵牤瑡捩瀠潲楢杮മ瀉潲敢※⼯倠獯瑩潩⁮畣牲湥汴⁹牰扯摥椠⁮桴⁥慨桳琠扡敬മ瀉潲敢㴠栠獡⡨慴杲瑥㬩ऍ牰扯彥潣湵⁴‽㬰ऍ湩牣浥湥⁴‽㬱ऍ桷汩⁥琨扡敬灛潲敢⁝㴡〠⼠ 獉琠敨氠捯瑡潩⁮浥瑰㽹ऍ☉…慴汢孥牰扯嵥琮敨歟祥⤨℠‽慴杲瑥琮敨歟祥⤨⼠ 潮⁴潦湵൤उ☦瀠潲敢损畯瑮㰠⠠慨桳獟穩⁥‫⤱㈯ ⁻⼯䠠獡漠敶晲潬⁷捯畣牲摥ിउ牰扯彥潣湵⭴㬫ऍ瀉潲敢㴠⠠牰扯⁥‫湩牣浥湥⥴栥獡彨楳敺഻उ湩牣浥湥⁴㴫㈠※⼯倠敲慰敲椠据敲敭瑮映牯渠硥⁴瑩牥瑡潩⹮ऍൽ††††晩⠠慴汢孥牰扯嵥琮敨歟祥⤨㴠‽慴杲瑥琮敨歟祥⤨笩ऍ昉畯摮㴠琠扡敬灛潲敢㭝ऍ爉瑥牵⁮畳捣獥㭳ऍൽ攉獬⁥敲畴湲渠瑯灟敲敳瑮഻�
```

### Slide 30

```
牅潲彲潣敤䠠獡彨慴汢⁥㨺爠浥癯⡥潣獮⁴敋⁹琦牡敧ⱴ删捥牯⁤昦畯摮笩ऍ‍†††椠瑮瀠潲敢损畯瑮‬⼯䌠畯瑮牥琠⁯敢猠牵⁥桴瑡琠扡敬椠⁳潮⁴畦汬മ椉据敲敭瑮‬⼯䤠据敲敭瑮甠敳⁤潦⁲畱摡慲楴⁣牰扯湩⹧ऍ牰扯㭥⼠ 潐楳楴湯挠牵敲瑮祬瀠潲敢⁤湩琠敨栠獡⁨慴汢⹥ऍ牰扯⁥‽慨桳琨牡敧⥴഻瀉潲敢损畯瑮㴠〠഻椉据敲敭瑮㴠ㄠ഻眉楨敬⠠慴汢孥牰扯嵥℠‽‰⼯䤠⁳桴⁥潬慣楴湯攠灭祴ിउ☦琠扡敬灛潲敢⹝桴彥敫⡹ 㴡琠牡敧⹴桴彥敫⡹ ⼯渠瑯映畯摮ऍ☉…牰扯彥潣湵⁴‼栨獡彨楳敺⬠ㄠ⼩⤲笠⼠ 慈⁳癯牥汦睯漠捣牵敲㽤ऍ瀉潲敢损畯瑮⬫഻उ牰扯⁥‽瀨潲敢⬠椠据敲敭瑮┩慨桳獟穩㭥ऍ椉据敲敭瑮⬠‽㬲⼠ 牐灥牡⁥湩牣浥湥⁴潦⁲敮瑸椠整慲楴湯മ紉‍†††椠⁦琨扡敬灛潲敢⹝桴彥敫⡹ 㴽琠牡敧⹴桴彥敫⡹⤩ൻउ潦湵㵤慴汢孥牰扯嵥഻उ慴汢孥牰扯嵥ⴽ㬱†⼯瑡整瑮潩൮उ敲畴湲猠捵散獳഻紉ऍ汥敳爠瑥牵⁮潮彴牰獥湥㭴納
```

### Slide 31

```
潶摩洠楡⡮笩ऍ慈桳瑟扡敬洠桹獡㭨ऍ祭慨桳椮獮牥⡴敒潣摲㌨㈬⤰㬩ऍ祭慨桳椮獮牥⡴敒潣摲㔨㌬⤰㬩ऍ祭慨桳椮獮牥⡴敒潣摲㤨㔬⤰㬩഍刉捥牯⁤慴杲瑥഻洉桹獡⹨敲牴敩敶䬨祥㔨Ⱙ慴杲瑥㬩ऍ潣瑵㰼䬢祥›㰢琼牡敧⹴桴彥敫⡹㰩∼†桔⁥瑯敨㩲∠㰼慴杲瑥琮敨潟桴牥⤨㰼湥汤഻ഉ琉牡敧㵴敒潣摲〨〬㬩ऍ祭慨桳爮瑥楲癥⡥敋⡹⤳琬牡敧⥴഻按畯㱴∼敋㩹∠㰼慴杲瑥琮敨歟祥⤨㰼•吠敨漠桴牥›㰢琼牡敧⹴桴彥瑯敨⡲㰩攼摮㭬
```

### Slide 32

```
敒畳瑬

敋㩹㔠†桔⁥瑯敨㩲㌠ര敋㩹㌠†桔⁥瑯敨㩲㈠�
```

### Slide 33

```
琉牡敧㵴敒潣摲〨〬㬩ऍ祭慨桳爮浥癯⡥敋⡹⤳琬牡敧⥴഻按畯㱴∼敋㩹∠㰼慴杲瑥琮敨歟祥⤨㰼•吠敨漠桴牥›㰢琼牡敧⹴桴彥瑯敨⡲㰩攼摮㭬഍琉牡敧㵴敒潣摲〨〬㬩ऍ祭慨桳爮瑥楲癥⡥敋⡹⤳琬牡敧⥴഻按畯㱴∼敋㩹∠㰼慴杲瑥琮敨歟祥⤨㰼•吠敨漠桴牥›㰢琼牡敧⹴桴彥瑯敨⡲㰩攼摮㭬ऍ楣⹮敧⡴㬩഍�
```

### Slide 34

```
䬍祥›″吠敨漠桴牥›〲䬍祥›‰吠敨漠桴牥›�
```

### Slide 35

```
潶摩䠠獡彨慴汢⁥㨺挠敬牡⤨ൻ昉牯椨瑮椠〽※㱩慨桳獟穩㭥椠⬫笩ऍ琉扡敬楛⹝汣慥⡲㬩ऍൽ�
```

### Slide 36

```
牅潲彲潣敤䠠獡彨慴汢⁥㨺椠獮牥⡴潣獮⁴敒潣摲☠敮彷湥牴⥹഍ൻ椉瑮瀠潲敢഻瀉潲敢㴠栠獡⡨敮彷湥牴⥹഻昉牯椨瑮椠〽※㱩慴汢孥牰扯嵥献穩⡥㬩椠⬫笩ऍ刉捥牯⁤浴㭰ऍ琉扡敬灛潲敢⹝敲牴敩敶椨琬灭㬩ऍ椉⡦浴㵰渽睥敟瑮祲 敲畴湲搠灵楬慣整敟牲牯഻紉഍琉扡敬灛潲敢⹝湩敳瑲〨‬敮彷湥牴⥹഻爉瑥牵⁮畳捣獥㭳納
```

### Slide 37

```
牅潲彲潣敤䠠獡彨慴汢⁥㨺爠瑥楲癥⡥潣獮⁴敋⁹琦牡敧ⱴ删捥牯⁤昦畯摮 潣獮筴ऍ湩⁴牰扯㭥ऍ牰扯⁥‽慨桳琨牡敧⥴഻昉牯椨瑮椠〽※㱩慴汢孥牰扯嵥献穩⡥㬩椠⬫笩ऍ刉捥牯⁤浴㭰ऍ琉扡敬灛潲敢⹝敲牴敩敶椨琬灭㬩ऍ椉⡦慴杲瑥㴽浴⥰ൻउ昉畯摮琽灭഻उ爉瑥牵⁮畳捣獥㭳ऍ紉ऍൽ爉瑥牵⁮潮彴牰獥湥㭴納
```
