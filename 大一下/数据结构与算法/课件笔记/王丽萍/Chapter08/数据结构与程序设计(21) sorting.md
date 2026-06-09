# Chapter 08 — 排序 — 数据结构与程序设计(21) sorting

- 章节编号: Chapter08 (#21)
- 来源路径: `C:\Users\Li\OneDrive\Backup\1\大一下\2024数据结构与算法wlp\历年\王丽i萍 数据结构与算法\王丽i萍 数据结构与算法\Chapter08-02\数据结构与程序设计(21) sorting.ppt`
- 提取的页面组数: 39
- 核心数据结构/算法: 线性表, 堆, 排序, 类, 插入排序, 归并排序, 快速排序, 指针, 表
- 时间复杂度: (无显式标注)
- 代码示例: 有 (匹配度=5)
- 关键例题: (未识别)

---

## 提取的原始内容

> 自动从 MS-PPT 二进制格式 (`TextCharsAtom` / `TextBytesAtom`) 提取，共 39 个文本组。

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
数据结构与程序设计(21)

王丽苹
lipingwang@sei.ecnu.edu.cn

Chapter 08 排序

插入排序
选择排序
希尔排序
快速排序
合并排序
堆排序

Sortable_list新增排序

class Sortable_list: public List<Record> {
public: // Add prototypes for sorting methods here.
……
	//for quick_sort.
	void quick_sort( );
	void recursive_quick_sort(int low, int high);
	int partition(int low, int high);

	//for heap_sort.
	void heap_sort( );
	void build_heap( );
	void insert_heap(const Record &current, int low, int high);
};
//for Mergesort
void divide_from(Sortable_list & mylist, Sortable_list & secondlist);
void combine(Sortable_list & firstsortlist, const Sortable_list & secondsortlist);
void Mergesort(Sortable_list & mylist);
```

### Slide 5

```
合并排序思想:
We chop the list into two sublists of sizes as nearly equal as possible and then sort them separately. Afterward, we carefully merge the two sorted sublists into a single sorted list.
把待排序的列表划分为分成近似相等的两部分，分别将两个子列表排序，然后再合并成一个完整的列表。
```

### Slide 6

```
Mergesort:
BOOK P341 FIGURE 8.9
Example
对26 33 35 29 19 12 22进行合并排序的过程
(1)划分为：26 33 35 29 and 19 12 22
(2) 对子序列1：26 33 35 29 进行合并排序
(3) 对子序列2：19 12 22进行合并排序
(4) 合并两个子序列
```

### Slide 7

```
void divide_from(Sortable_list & mylist, Sortable_list & secondlist){
	int mid=(mylist.size()-1)/2; //分割点的坐标
	int secondsize=mylist.size()-(mid+1); //子序列二的长度
	for (int i=0; i<secondsize; i++){
		Record x;
		if(mylist.retrieve(mid+1, x)==success){
			secondlist.insert(i, x);
			mylist.remove(mid+1, x);//在原序列中删除该节点
		}
	}
}
```

### Slide 8

```
void combine(Sortable_list & firstsortlist, const Sortable_list & secondsortlist){
	Sortable_list tmp;
	int m=0, n=0, i=0;//m为第一个列表的下标，n为第二个列表的下标
	while(m<firstsortlist.size() && n<secondsortlist.size()){
		Record x, y;
		firstsortlist.retrieve(m, x);
		secondsortlist.retrieve(n, y);
		if(x<=y){
			tmp.insert(i++, x);//i为合并后列表的下标
			m++;
		}
		else{
			tmp.insert(i++, y);
			n++;
		}
	}
```

### Slide 9

```
class Sortable_list: public List<Record> {
public: // Add prototypes for sorting methods here.
	void insertion_sort( );

private: // Add prototypes for auxiliary functions here.

};
//对sub_list进行合并排序
void recursive_merge_sort(Node<Record> * &sub_list);
//将sub_list划分为两部分，函数返回后半部分的指针
Node<Record> * divide_from(Node<Record> *sub_list);
//将first和Second合并
Node<Record> * merge(Node<Record> *first,			                                			Node<Record> *second);
```

### Slide 10

```
Quicksort思想:
We first choose some key from the list for which, we hope, about half the keys will come before and half after. Call this key the pivot（轴点）. Then we partition the items so that all those with keys less than the pivot come in one sublist, and all those with greater keys come in another. Then we sort the two reduced lists separately, put the sublists together, and the whole list will be in order.
```

### Slide 11

```
int Sortable_list :: partition(int low, int high)
{
	Record pivot;
	int i, // used to scan through the list
	last_small; // position of the last key less than pivot，记录小于抽点的数值下标
	swap(low, (low + high)/2);//将抽点与最小位置的值交换，并放置于最小的位置
	pivot = entry[low]; // First entry is now pivot .
	last_small = low; //初始化为最小的位置
	for (i = low + 1; i <= high; i++)
		if (entry[i] < pivot) {
			last_small ++; //从low+1开始放置。
			swap(last_small, i); // Move large entry to right and small to left.
		}
	swap(low, last_small); // Put the pivot into its proper position.
	return last_small;
}
```

### Slide 12

```
Quicksort P354 分析
```

### Slide 13

```
代码走读： 16 33 15 29 49 25 32
low=0；high=6
```

### Slide 14

```
课后作业，请用作业本完成
BOOK P343 E1, E2
```

### Slide 15

```
BOOK P364
DEFINITION A heap is a list in which each entry contains a key, and, for all positions k in the list, the key at position k is at least as large as the keys in positions 2k+1 and 2k + 2, provided these positions exist in the list.
这样的堆也称为大根堆。
```

### Slide 16

```
void Sortable_list :: insert_heap(const Record &current, int low, int high)
/* Pre: The entries of the Sortable list between indices low + 1 and high ,
inclusive, form a heap. The entry in position low will be discarded.
Post: The entry current has been inserted into the Sortable list and the
entries rearranged so that the entries between indices low and high ,
inclusive, form a heap.
Uses: The class Record , and the contiguous List implementation of Chapter 6.*/

Low+1到High满足堆的结构。插入Current。
经过插入后，最终使得从下标low到下标high形成一个新堆
```

### Slide 17

```
void Sortable_list :: build_heap( )
/* Post: The entries of the Sortable list have been rearranged so that it becomes a heap.
Uses: The contiguous List implementation of Chapter 6, and insert heap . */
{
	int low; // All entries beyond the position low form a heap.
        //非叶子结点K的满足的条件是：2K+1<=COUNT-1
        //K<=1/2*COUNT-1
	for (low = count/2 - 1; low >= 0; low--) {
		Record current = entry[low];
		insert_heap(current, low, count - 1);
	}
}
```

### Slide 18

```
走读代码，build_heap( )
说明以下数据建堆的过程：
26 5 77 1 61 11 59 15 48 19

结果为：
77 61 59 48 19 11 26 15 1 5
```

### Slide 19

```
堆属于完全二叉树，即（1）只有最下面两层的结点度数小于2，其余各层结点度数都等于2。（2）并且在最下面一层的结点都集中于该层左边的若干位置上。
J.Willioms and Floyd 在1964年提出了对排序的方法。
快速排序和堆排序都是不稳定的
```

### Slide 20

```
在建堆时对于叶子结点不需要再关心是否符合堆序，只需要建立非叶子结点的堆序即可。

敍杲獥牯�
```

### Slide 21

```
潶摩䴠牥敧潳瑲匨牯慴汢彥楬瑳☠洠汹獩⥴笍ऍ潓瑲扡敬江獩⁴敳潣摮楬瑳഻椉⁦洨汹獩⹴楳敺⤨ㄾ ൻउ楤楶敤晟潲⡭祭楬瑳‬敳潣摮楬瑳㬩ऍ䴉牥敧潳瑲洨汹獩⥴഻उ敍杲獥牯⡴敳潣摮楬瑳㬩ऍ按浯楢敮洨汹獩ⱴ猠捥湯汤獩⥴഻紉ഠ⁽
```

### Slide 22

```
眉楨敬洨昼物瑳潳瑲楬瑳献穩⡥⤩ൻउ敒潣摲砠഻उ楦獲獴牯汴獩⹴敲牴敩敶洨‬⥸഻उ浴⹰湩敳瑲椨⬫‬⥸഻उ⭭㬫ऍൽ眉楨敬渨猼捥湯獤牯汴獩⹴楳敺⤨笩ऍ刉捥牯⁤㭹ऍ猉捥湯獤牯汴獩⹴敲牴敩敶渨‬⥹഻उ浴⹰湩敳瑲椨⬫‬⥹഻उ⭮㬫ऍൽ昉物瑳潳瑲楬瑳琽灭഻�

敍杲獥牯⁴潆⁲楌歮摥䰠獩獴
```

### Slide 23

```
潶摩爠捥牵楳敶浟牥敧獟牯⡴潎敤刼捥牯㹤⨠☠畳形楬瑳笩ऍ晩⠠畳形楬瑳℠‽啎䱌☠…畳形楬瑳㸭敮瑸℠‽啎䱌 ൻउ潎敤刼捥牯㹤⨠敳潣摮桟污⁦‽楤楶敤晟潲⡭畳形楬瑳㬩ऍ爉捥牵楳敶浟牥敧獟牯⡴畳形楬瑳㬩ऍ爉捥牵楳敶浟牥敧獟牯⡴敳潣摮桟污⥦഻उ畳形楬瑳㴠洠牥敧猨扵江獩ⱴ猠捥湯彤慨晬㬩ऍ⁽納�
```

### Slide 24

```
潎敤刼捥牯㹤⨠搠癩摩彥牦浯丨摯㱥敒潣摲‾猪扵江獩⥴⼯㍐㘴⼍‪潐瑳›桔⁥楬瑳漠⁦潮敤⁳敲敦敲据摥戠⁹畳形楬瑳栠獡戠敥⁮敲畤散⁤潴椠獴映物瑳栠污ⱦ愠摮愠瀠楯瑮牥琠⁯桴⁥楦獲⁴潮敤椠⁮桴⁥敳潣摮栠污⁦景琠敨猠扵楬瑳椠⁳敲畴湲摥‮晉琠敨猍扵楬瑳栠獡愠⁮摯⁤畮扭牥漠⁦湥牴敩ⱳ琠敨⁮瑩⁳楦獲⁴慨晬眠汩⁬敢漠敮攠瑮祲氠牡敧൲桴湡椠獴猠捥湯⹤⼪笍ऍ潎敤刼捥牯㹤⨠潰楳楴湯‬⼯琠慲敶獲獥琠敨攠瑮物⁥楬瑳ऍ洪摩潰湩ⱴ⼠ 潭敶⁳瑡栠污⁦灳敥⁤景瀠獯瑩潩⁮潴洠摩潰湩൴⨉敳潣摮桟污㭦ऍ晩⠠洨摩潰湩⁴‽畳形楬瑳 㴽丠䱕⥌爠瑥牵⁮啎䱌※⼯䰠獩⁴獩攠灭祴മ瀉獯瑩潩⁮‽業灤楯瑮㸭敮瑸഻眉楨敬⠠潰楳楴湯℠‽啎䱌 ⁻⼯䴠癯⁥潰楳楴湯琠楷散映牯洠摩潰湩❴⁳湯⁥潭敶മउ潰楳楴湯㴠瀠獯瑩潩⵮渾硥㭴ऍ椉⁦瀨獯瑩潩⁮㴡丠䱕⥌笠ऍउ業灤楯瑮㴠洠摩潰湩⵴渾硥㭴ऍउ潰楳楴湯㴠瀠獯瑩潩⵮渾硥㭴ऍ紉ഠ紉ഠ猉捥湯彤慨晬㴠洠摩潰湩⵴渾硥㭴ऍ業灤楯瑮㸭敮瑸㴠丠䱕㭌ऍ敲畴湲猠捥湯彤慨晬഻�
```

### Slide 25

```
業灤楯瑮

潰楳楴湯
```

### Slide 26

```
潎敤刼捥牯㹤⨠洠牥敧丨摯㱥敒潣摲‾昪物瑳‬潎敤刼捥牯㹤⨠敳潣摮ഩൻ三摯㱥敒潣摲‾氪獡彴潳瑲摥※⼯瀠楯瑮⁳潴琠敨氠獡⁴潮敤漠⁦潳瑲摥氠獩൴三摯㱥敒潣摲‾潣扭湩摥※⼯搠浵祭映物瑳渠摯ⱥ瀠楯瑮⁳潴洠牥敧⁤楬瑳ऍ慬瑳獟牯整⁤‽挦浯楢敮㭤ऍ桷汩⁥昨物瑳℠‽啎䱌☠…敳潣摮℠‽啎䱌 ⁻⼯䄠瑴捡⁨潮敤眠瑩⁨浳污敬⁲敫൹उ晩⠠楦獲⵴放瑮祲㰠‽敳潣摮㸭湥牴⥹笠ऍउ慬瑳獟牯整ⵤ渾硥⁴‽楦獲㭴ऍउ慬瑳獟牯整⁤‽楦獲㭴ऍउ楦獲⁴‽楦獲⵴渾硥㭴⼠ 摁慶据⁥潴琠敨渠硥⁴湵敭杲摥渠摯⹥ऍ紉ഠउ汥敳笠ऍउ慬瑳獟牯整ⵤ渾硥⁴‽敳潣摮഻उ氉獡彴潳瑲摥㴠猠捥湯㭤ऍउ敳潣摮㴠猠捥湯ⵤ渾硥㭴ऍ紉†ऍ⁽ഠ⼯䄠瑦牥漠敮氠獩⁴湥獤‬瑡慴档琠敨爠浥楡摮牥漠⁦桴⁥瑯敨⹲ऍ晩⠠楦獲⁴㴽丠䱕⥌ऍ氉獡彴潳瑲摥㸭敮瑸㴠猠捥湯㭤ऍ汥敳ऍ氉獡彴潳瑲摥㸭敮瑸㴠映物瑳഻爉瑥牵⁮潣扭湩摥渮硥㭴納ഠ
```

### Slide 27

```
潣扭湩摥

慬瑳獟牯整�

楦獲�
```

### Slide 28

```
潶摩洠楡⡮笩ऍ潓瑲扡敬江獩⁴祭楬瑳഻昉牯椨瑮椠〽※㱩〱※⭩⤫洠汹獩⹴湩敳瑲椨刬捥牯⡤〱椭ㄬ⤰㬩ऍ潣瑵㰼吢敨氠獩⁴獩›㰢攼摮㭬ऍ祭楬瑳琮慲敶獲⡥牰湩⥴഻ऍ潣瑵㰼湥汤㰼唢敳爠捥牵楳敶浟牥敧獟牯⁴敍桴摯∺㰼湥汤഻爉捥牵楳敶浟牥敧獟牯⡴祭楬瑳䜮瑥桟慥⡤⤩഻洉汹獩⹴牴癡牥敳瀨楲瑮㬩ऍऍ潣瑵㰼湥汤㰼唢敳椠獮牥楴湯獟牯⁴敍桴摯∺㰼湥汤഻洉汹獩⹴湩敳瑲潩彮潳瑲⤨഻洉汹獩⹴牴癡牥敳瀨楲瑮㬩഍按湩朮瑥⤨഻納
```

### Slide 29

```
整灭慬整㰠汣獡⁳楌瑳敟瑮祲ാ潎敤䰼獩彴湥牴㹹⨠☠楌瑳䰼獩彴湥牴㹹㨠›敇彴敨摡⤨ൻ爉瑥牵⁮敨摡഻�

畑捩彫潳瑲
```

### Slide 30

```
畑捩獫牯㩴䈍住⁋㍐㌴䘠䝉剕⁅⸸〱

畑捩獫牯�

㘶†〳†㔳†㤲†㤱†㈳†㔳

㤲†〳†㔳†㘶†㤱†㈳†㔳

楐潶㵴㤲

㤲†㤱†㔳†㘶†〳†㈳†㔳

㤱†㤲†㔳†㘶†〳†㈳†㔳

†††††㌠‵㘠‶㌠‰㌠′㌠व†楐潶㵴〳

†††††㌠‰㘠‶㌠‵㌠′㌠व†

††††††††㘠‶㌠‵㌠′㌠व†楐潶㵴㔳

††㔳†㘶†㈳†㔳 �

††㔳†㈳†㘶†㔳 �

††㈳†㔳†㘶†㔳 �

††उ††㘠‶㌠व†倠癩瑯㘽‶�

††उ††㘠‶㌠व

††उ††㌠‵㘠श
```

### Slide 31

```
潶摩匠牯慴汢彥楬瑳㨠›畱捩彫潳瑲 ഩ⨯倠獯㩴吠敨攠瑮楲獥漠⁦桴⁥潓瑲扡敬氠獩⁴慨敶戠敥⁮敲牡慲杮摥猠⁯桴瑡琠敨物欠祥⁳牡⁥潳瑲摥椠瑮⁯潮摮捥敲獡湩⁧牯敤⹲唍敳㩳䌠湯楴畧畯⁳楌瑳椠灭敬敭瑮瑡潩⁮景䌠慨瑰牥㘠‬敲畣獲癩⁥畱捩⁫潳瑲⸠⼪笍ऍ敲畣獲癩彥畱捩彫潳瑲〨‬潣湵⁴‭⤱഻�
```

### Slide 32

```
潶摩匠牯慴汢彥楬瑳㨠›敲畣獲癩彥畱捩彫潳瑲椨瑮氠睯‬湩⁴楨桧ഩ⨯倠敲›潬⁷湡⁤楨桧愠敲瘠污摩瀠獯瑩潩獮椠⁮桴⁥潓瑲扡敬氠獩⁴മ潐瑳›桔⁥湥牴敩⁳景琠敨匠牯慴汢⁥楬瑳栠癡⁥敢湥爠慥牲湡敧⁤潳琠慨⁴桴楥⁲敫獹愠敲猠牯整⁤湩潴渠湯敤牣慥楳杮漠摲牥മ獕獥›潃瑮杩潵獵䰠獩⁴浩汰浥湥慴楴湯漠⁦桃灡整⁲ⰶ爠捥牵楳敶焠極正猠牯⁴‬湡⁤慰瑲瑩潩⁮‮⼪笍ऍ湩⁴楰潶彴潰楳楴湯഻椉⁦氨睯㰠栠杩⥨笠⼠ 瑏敨睲獩ⱥ渠⁯潳瑲湩⁧獩渠敥敤⹤ऍ瀉癩瑯灟獯瑩潩⁮‽慰瑲瑩潩⡮潬ⱷ栠杩⥨഻उ敲畣獲癩彥畱捩彫潳瑲氨睯‬楰潶彴潰楳楴湯ⴠㄠ㬩ऍ爉捥牵楳敶煟極正獟牯⡴楰潶彴潰楳楴湯⬠ㄠ‬楨桧㬩ऍ⁽納
```

### Slide 33

```
湩⁴潓瑲扡敬江獩⁴㨺瀠牡楴楴湯椨瑮氠睯‬湩⁴楨桧ഩ⨯倠敲›潬⁷湡⁤楨桧愠敲瘠污摩瀠獯瑩潩獮漠⁦桴⁥潓瑲扡敬氠獩⁴‬楷桴氠睯㰠‽楨桧⸠倍獯㩴吠敨挠湥整⁲漨⁲敬瑦挠湥整⥲攠瑮祲椠⁮桴⁥慲杮⁥敢睴敥⁮湩楤散⁳潬⁷湡⁤楨桧漠⁦桴⁥潓瑲扡敬氠獩⁴慨⁳敢湥挠潨敳⁮獡愠瀠癩瑯‮汁⁬湥牴敩⁳景琠敨匠牯慴汢⁥楬瑳戠瑥敷湥椠摮捩獥氠睯愠摮栠杩⁨‬湩汣獵癩ⱥ栠癡⁥敢湥爠慥牲湡敧⁤潳琠慨⁴桴獯⁥楷桴欠祥⁳敬獳琠慨⁮桴⁥楰潶⁴潣敭戠晥牯⁥桴⁥楰潶⁴湡⁤桴⁥敲慭湩湩⁧湥牴敩⁳潣敭愠瑦牥琠敨瀠癩瑯‮桔⁥楦慮⁬潰楳楴湯漠⁦桴⁥楰潶⁴獩爠瑥牵敮⹤唍敳㩳猠慷⡰湩⁴Ⱪ椠瑮樠 椨瑮牥档湡敧⁳湥牴敩⁳湩瀠獯瑩潩獮椠愠摮樠漠⁦⁡潓瑲扡敬氠獩⁴Ⱙ琠敨挠湯楴畧畯⁳楌瑳椠灭敬敭瑮瑡潩⁮景䌠慨瑰牥㘠‬湡⁤敭桴摯⁳潦⁲桴⁥汣獡⁳敒潣摲⸠⨠�
```

### Slide 34

```
楰潶�

慬瑳獟慭汬
```

### Slide 35

```
佈䕍佗䭒
```

### Slide 36

```
效灡獟牯�
```

### Slide 37

```
效灡獟牯⁴硅浡汰�
```

### Slide 38

```
效灡獟牯⁴佂䭏倠㘳‷䥆啇䕒㠠ㄮ�

潶摩匠牯慴汢彥楬瑳㨠›敨灡獟牯⡴⤠⼍‪潐瑳›桔⁥湥牴敩⁳景琠敨匠牯慴汢⁥楬瑳栠癡⁥敢湥爠慥牲湡敧⁤潳琠慨⁴桴楥⁲敫獹愍敲猠牯整⁤湩潴渠湯敤牣慥楳杮漠摲牥മ獕獥›桔⁥潣瑮杩潵獵䰠獩⁴浩汰浥湥慴楴湯漠⁦桃灡整⁲ⰶ畢汩彤敨灡Ⱐ愠摮椠獮牥彴敨灡⸠⨠യൻ刉捥牯⁤畣牲湥㭴⼠ 整灭牯牡⁹瑳牯条⁥潦⁲潭楶杮攠瑮楲獥ऍ湩⁴慬瑳畟獮牯整㭤⼠ 湅牴敩⁳敢潹摮氠獡⁴湵潳瑲摥栠癡⁥敢湥猠牯整⹤ऍ畢汩彤敨灡 㬩⼠ 楆獲⁴桰獡㩥吠牵⁮桴⁥楬瑳椠瑮⁯⁡敨灡മ昉牯⠠慬瑳畟獮牯整⁤‽潣湵⁴‭㬱氠獡彴湵潳瑲摥㸠〠※慬瑳畟獮牯整ⵤ⤭笠ऍ按牵敲瑮㴠攠瑮祲汛獡彴湵潳瑲摥㭝⼠ 硅牴捡⁴慬瑳攠瑮祲映潲⁭楬瑳മउ湥牴孹慬瑳畟獮牯整嵤㴠攠瑮祲せ㭝⼠ 潍敶琠灯漠⁦敨灡琠⁯桴⁥湥൤उ湩敳瑲桟慥⡰畣牲湥ⱴ〠‬慬瑳畟獮牯整⁤‭⤱※⼯删獥潴敲琠敨栠慥൰紉ഠ�
```

### Slide 39

```
潶摩匠牯慴汢彥楬瑳㨠›湩敳瑲桟慥⡰潣獮⁴敒潣摲☠畣牲湥ⱴ椠瑮氠睯‬湩⁴楨桧ഩൻ椉瑮氠牡敧※⼯瀠獯瑩潩⁮景挠楨摬漠⁦湥牴孹潬嵷眠瑩⁨桴⁥慬杲牥欠祥ऍ慬杲⁥‽′‪潬⁷‫㬱⼠ 慬杲⁥獩渠睯琠敨氠晥⁴档汩⁤景氠睯മ眉楨敬⠠慬杲⁥㴼栠杩⥨笠ऍ椉⁦氨牡敧㰠栠杩⁨☦攠瑮祲汛牡敧⁝‼湥牴孹慬杲⁥‫崱ഩउ氉牡敧⬫※⼯氠牡敧椠⁳潮⁷桴⁥档汩⁤景氠睯眠瑩⁨桴⁥慬杲獥⁴敫⹹ऍ椉⁦挨牵敲瑮㸠‽湥牴孹慬杲嵥ഩउ戉敲歡※⼯挠牵敲瑮戠汥湯獧椠⁮潰楳楴湯氠睯മउ汥敳笠⼠ 牐浯瑯⁥湥牴孹慬杲嵥愠摮洠癯⁥潤湷琠敨琠敲⹥ऍउ湥牴孹潬嵷㴠攠瑮祲汛牡敧㭝ऍउ潬⁷‽慬杲㭥ऍउ慬杲⁥‽′‪潬⁷‫㬱ऍ紉ഠ紉ഠ攉瑮祲汛睯⁝‽畣牲湥㭴納
```

### Slide 40

```
效灡獟牯⁴佂䭏倠㘳�
```
