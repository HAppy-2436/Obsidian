# AVL 树
- 来源：`C:\Users\Li\OneDrive\Backup\1\大一下\2024数据结构与算法wlp\历年\王丽i萍 数据结构与算法\王丽i萍 数据结构与算法\chapter10-04\数据结构与程序设计(27)AVL Tree.ppt`
- 提取文本段：579
- 字符数：20653

## 核心概念
- 二叉树 (Binary Tree)
- 二叉搜索树 / BST
- AVL 树
- 平衡二叉树
- 图 (Graph)
- 递归 (Recursion)
- 平衡因子 (Balance Factor)
- 旋转 (Rotation)
- 插入 (Insertion)
- 删除 (Deletion)
- 查找 (Search)
- 中序遍历 (Inorder)
- 前序遍历 (Preorder)
- 后序遍历 (Postorder)

## 关键定义
- AVL Definition:
- Height Balance: AVL Trees 定义
- Height Balance: AVL Trees 定义

## 典型例题 / 问题
- 问题：怎么样判断节点的平衡因子是否被破坏？
- 问题：怎么样判断节点n的平衡因子是否被破坏？
- Example：Remove P487
- Example：Remove P487
- Example：Remove P487
- Example：Remove P487

## 代码片段
```cpp
enum Balance_factor { left_higher, equal_height, right_higher };
enum Balance_factor { left_higher, equal_height, right_higher };
template <class Entry>
struct Binary_node {
Entry data;
Binary_node<Entry> *left;
Binary_node<Entry> *right;
Binary_node( );
Binary_node(const Entry &x);
virtual void set_balance(Balance_factor b);
virtual Balance_factor get_balance( ) const;
};
#include "Binary_node.cpp"
template <class Record>
struct AVL_node: public Binary_node<Record> {
Balance_factor balance;
AVL_node( );
AVL_node(const Record &x);
void set_balance(Balance_factor b);
Balance_factor get_balance( ) const;
```

## 提取的原始内容

```text
单击此处编辑母版标题样式

单击此处编辑母版文本样式
第二级
第三级
第四级
第五级

*

数据结构与程序设计

*

单击此处编辑母版标题样式

单击此处编辑母版文本样式
第二级
第三级
第四级
第五级

*

数据结构与程序设计

*

单击此处编辑母版文本样式
第二级
第三级
第四级
第五级

*

*

*

数据结构与程序设计

*

数据结构与程序设计(27)

王丽苹  
lipingwang@sei.ecnu.edu.cn

*

数据结构与程序设计

*

10.4 Height Balance: AVL Trees

10.3 节创建的二叉查找树左右子树高度不能保证总是近似平衡。例如8个节点时，8为根，整棵右子树为空。
AVL Definition:
An AVL tree is a binary search tree in which the heights of the left and right subtrees of the root differ by at most 1 and in which the left and right subtrees are again AVL trees.

*

数据结构与程序设计

*

Height Balance: AVL Trees

With each node of an AVL tree is associated a balance factor that is left higher, equal, or right higher according, respectively, as the left subtree has height greater than, equal to, or less than that of the right subtree.

*

数据结构与程序设计

*

Height Balance: AVL Trees

In drawing diagrams, we shall show a left-higher node by `/,' a node whose balance factor is equal by `−,' and a right-higher node by `\.'

*

数据结构与程序设计

*

Height Balance: AVL Trees

*

数据结构与程序设计

*

Height Balance: AVL Trees

*

数据结构与程序设计

*

Height Balance: AVL Trees

We employ an enumerated data type to record balance factors:                     			  
enum Balance_factor { left_higher, equal_height, right_higher };
AVL nodes are structures derived from binary search tree nodes with balance factors included.

Left*    balance_factor   data     right*

Left*        data               right*

AVL Node 是Tree Node的子类

Binary Search Tree Node

*

数据结构与程序设计

*

Binary Tree Node

enum Balance_factor { left_higher, equal_height, right_higher };
template <class Entry>
struct Binary_node {
// data members:
	Entry data;
	Binary_node<Entry> *left;
	Binary_node<Entry> *right;
// constructors:
	Binary_node( );
	Binary_node(const Entry &x);
// virtual methods:
virtual void set_balance(Balance_factor b);
virtual Balance_factor get_balance( ) const;
};

*

数据结构与程序设计

*

AVL Trees  Node

#include "Binary_node.cpp"
template <class Record>
struct AVL_node: public Binary_node<Record> {
// additional data member:
	Balance_factor balance;
// constructors:
	AVL_node( );
	AVL_node(const Record &x);
// overridden virtual functions:
	void set_balance(Balance_factor b);
	Balance_factor get_balance( ) const;
};

*

数据结构与程序设计

*

AVL Node的继承分析

Left*    balance_factor   data     right*

Left*        data               right*

红色：Binary Node中的元素。
黑色：子类AVL node中增加的元素。

Tree Node

AVL Node

Left*    balance_factor   data     right*

Binary_node* left;
left = new AVL_Node;  //父类指针指向子类的对象
Left->setBanlance(equal_height); //此处发生动态绑定，调用的是子类AVL_Node中setBanlance方法的实现。

*

数据结构与程序设计

*

AVL Trees  Node实现

AVL_node<Record> :: AVL_node(){
	left = NULL;
	right = NULL;
	balance = equal_height;
}

template <class Record>
AVL_node<Record> :: AVL_node(const Record &x){
	data = x;
	left = NULL;
	right = NULL;
	balance = equal_height;
}

*

数据结构与程序设计

*

AVL Trees  Node实现

template <class Record>
void AVL_node<Record> :: set_balance(Balance_factor b)
{
	balance = b;
}

template <class Record>
Balance_factor AVL_node<Record> :: get_balance( ) const
{
	return balance;
}

*

数据结构与程序设计

*

Binary Tree Node

enum Balance_factor { left_higher, equal_height, right_higher };
template <class Entry>
struct Binary_node {
// data members:
	Entry data;
	Binary_node<Entry> *left;
	Binary_node<Entry> *right;
// constructors:
	Binary_node( );
	Binary_node(const Entry &x);
// virtual methods:
virtual void set_balance(Balance_factor b);
virtual Balance_factor get_balance( ) const;
};

*

数据结构与程序设计

*

Binary Tree Node 实现

template <class Entry>
Binary_node<Entry> :: Binary_node(){
	left = NULL;
	right = NULL;
}

template <class Entry>
Binary_node<Entry> :: Binary_node(const Entry &x){
	data = x;
	left = NULL;
	right = NULL;
}

*

数据结构与程序设计

*

Binary Tree Node 实现

template <class Entry>
void Binary_node<Entry> :: set_balance(Balance_factor b)
{
}

template <class Entry>
Balance_factor Binary_node<Entry> :: get_balance( ) const
{
	return equal_height;
}

*

数据结构与程序设计

*

left->get_balance( )

We often invoke these methods ( set_balance, get_balance) through pointers to nodes, such as left->get_balance( ). 
Left为Binary_node类型的指针。
Left指向的是Binary_node的对象时，调用的是父类中get_balance()方法的实现。
Left指向的是AVL_node的对象时，调用的是AVL_node中get_balance()方法的实现。
get_balance( )为虚函数，支持动态绑定。

*

数据结构与程序设计

*

Height Balance: AVL Trees 定义

#include "Search_tree.cpp"
template <class Record>
class AVL_tree: public Search_tree<Record> {
public:
	Error_code insert(const Record &new_data);
	Error_code remove(Record &old_data);

*

数据结构与程序设计

*

Height Balance: AVL Trees 定义

private: // Add auxiliary function prototypes here.
	Error_code avl_insert(Binary_node<Record> * &sub_root, const Record &new_data, bool &taller);
	void rotate_left(Binary_node<Record> * &sub_root);
	void rotate_right(Binary_node<Record> * &sub_root);
	void right_balance(Binary_node<Record> * &sub_root);
	void left_balance(Binary_node<Record> * &sub_root);
	//add for remove
	Error_code avl_remove(Binary_node<Record> * &sub_root, Record &new_data, bool &shorter);
	bool right_balance2(Binary_node<Record> * &sub_root);
	bool left_balance2(Binary_node<Record> * &sub_root);
};

*

数据结构与程序设计

*

10.4.2 Insertions into an AVL tree

*

数据结构与程序设计

*

10.4.2 AVL树插入的方法

向AVL树中插入新节点的方法与二分查找树插入新节点的方法基本相同：
 首先按照二分查找树构建的方法，向AVL树中插入新节点。（10.2.3  P452）
在新节点插入之后，从树叶向根部依次分析树的平衡因子是否被破坏了，如果被破坏则需要立即按照一定的方法重新调整树的结构。

*

数据结构与程序设计

*

Insertions into an AVL tree

如图所示，在插入新节点u之后，K的平衡因子被破坏，此时需要进行调整。左旋，具体的旋转方法在后面介绍。
问题：怎么样判断节点的平衡因子是否被破坏？

*

数据结构与程序设计

*

Insertions into an AVL tree

问题：怎么样判断节点n的平衡因子是否被破坏？
方法：先判断在节点n的左子树还是右子树有插入操作且该子树的高度是否改变（即高度增加1）。
如果左子树有插入操作，且高度改变
如果节点的平衡因子为 - 变为 / 。
如果节点的平衡因子为 /,变为 //，且需要调整。
如果节点的平衡因子为\, 变为- 。
如果右子树有插入操作，且高度有改变
如果节点的平衡因子为 - 变为 \。
如果节点的平衡因子为 \,变为 \\，且需要调整。
如果节点的平衡因子为/, 变为- 。

*

数据结构与程序设计

*

Insertions into an AVL tree

插入节点P时，m的平衡因子被破坏，现在需要调整结构。

*

数据结构与程序设计

*

AVL Trees 插入操作

template <class Record>
Error_code AVL_tree<Record> :: insert(const Record &new_data)
/* Post: If the key of new data is already in the AVL tree , a code of duplicate_error is returned. Otherwise, a code of success is returned and the Record new data is inserted into the tree in such a way that the properties of an AVL tree are preserved.
Uses: avl_insert . */
{
	bool taller; // Has the tree grown in height?	
	return avl_insert(root, new_data, taller);
        //向root中插入一个新节点new_data.
        //taller表示插入是否使得以root为根的树高度增加。
}

*

数据结构与程序设计

*

template <class Record>
Error_code AVL_tree<Record> :: avl_insert(Binary_node<Record> * &sub_root,  const Record &new_data, bool &taller)
{
	Error_code result = success;
	if (sub_root == NULL) {
		sub_root = new AVL_node<Record>(new_data);
		taller = true;
	} 
	else if (new_data == sub_root->data) {
		result = duplicate_error;
		taller = false;
	}

*

数据结构与程序设计

*

else if (new_data < sub_root->data) { // Insert in left subtree.
		result = avl_insert(sub_root->left, new_data, taller); 
		if (taller == true)
		switch (sub_root->get_balance( )) { // Change balance factors.
		case left_higher:
			left_balance(sub_root);
			taller = false; // Rebalancing always shortens the tree.
			break;
		case equal_height:
			sub_root->set_balance(left_higher);
			break;
		case right_higher:
			sub_root->set_balance(equal_height);
			taller = false;
			break;
		}  
	}

*

数据结构与程序设计

*

在Subroot的左子树插入节点后的情况分析：

h+1

h

case left_higher
left_balance(sub_root)

h

h

case equal_height
taller = true

h

case right_higher

h+1

sub_root

*

数据结构与程序设计

*

else { // Insert in right subtree.
		result = avl_insert(sub_root->right, new_data, taller);
		if (taller == true)
		switch (sub_root->get_balance( )) {
		case left_higher:
			sub_root->set_balance(equal_height);
			taller = false;
			break;
		case equal_height:
			sub_root->set_balance(right_higher);
			break;
		case right_higher:
			right_balance(sub_root);
			taller = false; // Rebalancing always shortens the tree.
			break;
		}	 
	} 
	return result;
}

*

数据结构与程序设计

*

h+1

h

case left_higher

h

h

case equal_height
taller = true

h

case right_higher
right_balance(sub_root);

h+1

sub_root

在Subroot的右子树插入节点后的情况分析：

*

数据结构与程序设计

*

P480 2 Rotations 旋转操作

如果节点的平衡因子被破坏，用什么方法调整平衡。
方法：需要根据破坏平衡的原因来调整。
破坏平衡的原因有四种：
RR型，RL型，LL型，LR型。
其中RR与LL雷同，RL与LR雷同。
下面重点介绍RR型的调整和RL型的调整。

*

数据结构与程序设计

*

P480 2 Rotations 旋转操作

*

数据结构与程序设计

*

第一种情况：case right_higher:

*

数据结构与程序设计

*

AVL Trees 左旋操作

template <class Record>
void AVL_tree<Record> :: rotate_left(Binary_node<Record> * &sub_root)
/* Pre: sub_root points to a subtree of the AVL tree . This subtree has a nonempty right subtree.
Post: sub_root is reset to point to its former right child, and the former sub_root node is the left child of the new sub_root node. */
{
	if (sub_root == NULL || sub_root->right == NULL) // impossible cases
		cout << "WARNING: program error detected in rotate left" << endl;
	else {
		Binary_node<Record> *right_tree = sub_root->right;
		sub_root->right = right_tree->left;
		right_tree->left = sub_root;
		sub_root = right_tree;
	} 
}

*

数据结构与程序设计

*

第二种情况：case left_higher:

*

数据结构与程序设计

*

template <class Record>
void AVL_tree<Record> :: rotate_right(Binary_node<Record> * &sub_root)
/* Pre: sub_root points to a subtree of the AVL tree . This subtree has a nonempty
left subtree.
Post: sub_root is reset to point to its former left child, and the former sub_root
node is the right child of the new sub_root node. */
{
	if (sub_root == NULL || sub_root->left == NULL) // impossible cases
		cout << "WARNING: program error detected in rotate right" << endl;
	else {
		Binary_node<Record> *left_tree = sub_root->left;
		sub_root->left = left_tree->right;
		left_tree->right = sub_root;
		sub_root = left_tree;
	} 
}

AVL Trees 右旋操作

*

数据结构与程序设计

*

当右子树过高于左子树2层时的调整

template <class Record>
void AVL_tree<Record> :: right_balance(Binary_node<Record> * &sub_root)
/* Pre: sub root points to a subtree of an AVL tree , doubly unbalanced on the right.
Post: The AVL properties have been restored to the subtree.
Uses: Methods of struct AVL node ; functions rotate_right ,rotate_left . */
{
	Binary_node<Record> * &right_tree = sub_root->right;
	switch (right_tree->get_balance( )) {
	case right_higher: // single rotation left
		sub_root->set_balance(equal_height);
		right_tree->set_balance(equal_height);
		rotate_left(sub_root); 
		break;
	case equal_height: // impossible case because taller == true
		cout << "WARNING: program error in right balance" << endl;

*

数据结构与程序设计

*

case left_higher: // double rotation left
		Binary_node<Record> *sub_tree = right_tree->left;
		switch (sub_tree->get_balance( )) {
		case equal_height:
			sub_root->set_balance(equal_height);
			right_tree->set_balance(equal_height); 
			break;
		case left_higher: //T2 is h, T3 is h-1
			sub_root->set_balance(equal_height);
			right_tree->set_balance(right_higher); 
			break;
		case right_higher: //T2 is h-1, T3 is h
			sub_root->set_balance(left_higher);
			right_tree->set_balance(equal_height); 
			break;
		} 
		sub_tree->set_balance(equal_height);
		rotate_right(right_tree);
		rotate_left(sub_root); 
		break;
	} 
}

*

数据结构与程序设计

*

case left_higher:

*

数据结构与程序设计

*

template <class Record>
void AVL_tree<Record> :: left_balance(Binary_node<Record> * &sub_root)
/* Pre: sub root points to a subtree of an AVL tree , doubly unbalanced on the left.
Post: The AVL properties have been restored to the subtree.
Uses: Methods of struct AVL node ; functions rotate_right ,rotate_left . */
{
	Binary_node<Record> * &left_tree = sub_root->left;
	switch (left_tree->get_balance( )) {
	case left_higher: // single rotation left
		sub_root->set_balance(equal_height);
		left_tree->set_balance(equal_height);
		rotate_right(sub_root); 
		break;
	case equal_height: // impossible case
		cout << "WARNING: program error in right balance" << endl;

当左子树过高于右子树2层时的调整

*

数据结构与程序设计

*

case right_higher: // double rotation left
		Binary_node<Record> *sub_tree = left_tree->right;
		switch (sub_tree->get_balance( )) {
		case equal_height:
			sub_root->set_balance(equal_height);
			left_tree->set_balance(equal_height); 
			break;
		case right_higher:
			sub_root->set_balance(equal_height);
			left_tree->set_balance(left_higher); 
			break;
		case left_higher:
			sub_root->set_balance(right_higher);
			left_tree->set_balance(equal_height); 
			break;
		} 
		sub_tree->set_balance(equal_height);
		rotate_left(left_tree);
		rotate_right(sub_root); 
		break;
	} 
}

*

数据结构与程序设计

*

Insertions into an AVL tree

插入节点P时，m的平衡因子被破坏，现在需要调整结构。

*

数据结构与程序设计

*

AVL Trees--Main

void main(){
	AVL_tree<Record> mytree;
	for(int i=1;i<10;i++){
		mytree.insert(Record(i));
		cout<<"Preorder:"<<endl;
		mytree.preorder(print);
		cout<<endl;
		cout<<"inorder:"<<endl;
		mytree.inorder(print);
		cout<<endl;
		cout<<"Postorder:"<<endl;
		mytree.postorder(print);
		cout<<endl<<endl;
	}

*

数据结构与程序设计

*

AVL Trees--Main

1

1

2

2

3

1

2

3

1

4

Rotate_left

*

数据结构与程序设计

*

AVL Trees--Main

2

4

1

5

3

4

5

2

6

3

1

Rotate_left

Rotate_left

*

数据结构与程序设计

*

AVL Trees--Main

4

6

2

7

3

1

5

4

6

2

7

3

1

5

8

Rotate_left

*

数据结构与程序设计

*

AVL Trees--Main

4

6

2

8

3

1

5

9

7

Rotate_left

*

数据结构与程序设计

*

AVL Trees--Main

AVL_tree<Record> mytree2;
	for(i=9;i>0;i--){
		mytree2.insert(Record(i));
		cout<<"Preorder:"<<endl;
		mytree2.preorder(print);
		cout<<endl;
		cout<<"inorder:"<<endl;
		mytree2.inorder(print);
		cout<<endl;
		cout<<"Postorder:"<<endl;
		mytree2.postorder(print);
		cout<<endl<<endl;
	}
	cin.get();
}

*

数据结构与程序设计

*

AVL Trees--Main

9

9

8

8

9

7

8

9

7

6

Rotate_right

*

数据结构与程序设计

*

AVL Trees--Main

8

9

6

7

5

6

8

5

9

7

4

Rotate_right

Rotate_right

*

数据结构与程序设计

*

AVL Trees--Main

6

8

4

9

5

3

7

6

8

4

9

5

3

7

2

Rotate_right

*

数据结构与程序设计

*

AVL Trees--Main

6

8

4

9

5

2

7

3

1

Rotate_right

*

数据结构与程序设计

*

10.4.3 AVL的删除操作

向AVL树中删除节点的方法与二分查找树删除节点的方法基本相同：
 首先按照二分查找树删除的方法，找到删除的节点。
在节点删除之后，从删除点所在的位置向根部依次分析树的平衡因子是否被破坏了，如果被破坏则需要立即按照一定的方法重新调整树的结构。（调整方法与插入操作相同）

*

数据结构与程序设计

*

平衡因子的分析（1）

*

数据结构与程序设计

*

平衡因子的分析（2）

*

数据结构与程序设计

*

平衡因子的分析（3）

*

数据结构与程序设计

*

Example：Remove P487

删除P以后的结果是？

*

数据结构与程序设计

*

Example：Remove P487

第一步：调整节点o

*

数据结构与程序设计

*

Example：Remove P487

第二步：调整节点m，  LR型的结构，需要先左旋，再右旋

*

数据结构与程序设计

*

Example：Remove P487

*

数据结构与程序设计

*

Remove（..）

template <class Record>
Error_code AVL_tree<Record> :: remove(Record &new_data)
/* Post: If the key of new data is not in the AVL tree , a code of not_present is returned. Otherwise, a code of success is returned and the Record new data is removed from the tree in such a way that the properties of an AVL tree are preserved.
Uses: avl_remove . */
{
	bool shorter=true; // Has the tree shorter in height?	
	return avl_remove(root, new_data, shorter);
}

*

数据结构与程序设计

*

avl_remove(..)

template <class Record>
Error_code AVL_tree<Record> :: avl_remove(Binary_node<Record> * &sub_root, Record &new_data, bool &shorter)
{
	Error_code result = success;
       Record sub_record;
	if (sub_root == NULL) {
		shorter = false;
		return not_present;
	}

*

数据结构与程序设计

*

else if (new_data == sub_root->data) {//删除节点，操作与二分查找树相同
		Binary_node<Record> *to_delete = sub_root;
		// Remember node to delete at end.
		if (sub_root->right == NULL){ //右子树为空
			sub_root = sub_root->left;
			shorter = true;
			delete to_delete; // Remove to_delete from tree.
			return success;
		}
		else if (sub_root->left == NULL){ //左子树为空
			sub_root = sub_root->right;
			shorter = true;
			delete to_delete; // Remove to_delete from tree.
			return success;
		}

*

数据结构与程序设计

*

else { //左右子树都不为空
                           // Neither subtree is empty.
			to_delete = sub_root->left; 
                              // Move left to find predecessor.	
			Binary_node<Record> *parent = sub_root; 
                            // parent of to_delete
			while (to_delete->right != NULL) { 
                                                    // to_delete is not the predecessor.
				parent = to_delete;
				to_delete = to_delete->right;
			}	 
//sub_root->data = to_delete->data; // Move data from to_delete to root. 
			new_data = to_delete->data;
			sub_record = new_data; //记录删除的数据值
		} //else分支，完成删除任务的替换。
                //在删除点x的左右子树都存在时，此时删除的是前驱点w。
	}

*

数据结构与程序设计

*

if (new_data < sub_root->data) { // remove in left subtree.
		result = avl_remove(sub_root->left, new_data, shorter);
		if(sub_record.the_key()!=0)sub_root->data = sub_record; 
                            // Move data from to_delete to root. 
		if (shorter == true)
		switch (sub_root->get_balance( )) { // Change balance factors.
		case left_higher:
			sub_root->set_balance(equal_height);
			break;
		case equal_height:
			sub_root->set_balance(right_higher);
			shorter = false;
			break;
		case right_higher:
			shorter = right_balance2(sub_root);
			break;
		}  
	}

*

数据结构与程序设计

*

if (new_data > sub_root->data) { // remove in right subtree.
		result = avl_remove(sub_root->right, new_data, shorter);
		if(sub_record.the_key()!=0)sub_root->data = sub_record; 
                                 // Move data from to_delete to root. 
		if (shorter == true)
		switch (sub_root->get_balance( )) { // Change balance factors.
		case left_higher:
			shorter = left_balance2(sub_root);
			break;
		case equal_height:
			sub_root->set_balance(left_higher);
			shorter = false;
			break;
		case right_higher:
			sub_root->set_balance(equal_height);
			break;
		}  
	} 
	return result;
}

*

数据结构与程序设计

*

right_balance2

template <class Record>
bool AVL_tree<Record> :: right_balance2(Binary_node<Record> * &sub_root)
/* Pre: sub root points to a subtree of an AVL tree , doubly unbalanced on the right.
Post: The AVL properties have been restored to the subtree.
Uses: Methods of struct AVL node ; functions rotate_right ,rotate_left . */
{
	bool shorter;
	Binary_node<Record> * &right_tree = sub_root->right;
	switch (right_tree->get_balance( )) {
	case right_higher: // single rotation left
		sub_root->set_balance(equal_height);
		right_tree->set_balance(equal_height);
		rotate_left(sub_root); 
		shorter = true;
		break;

*

数据结构与程序设计

*

case equal_height: // single rotation left  R-型，左转后高度不变
		right_tree->set_balance(left_higher);
		rotate_left(sub_root); 
		shorter = false;
		break;

right_balance2

*

数据结构与程序设计

*

case left_higher: // double rotation left
		Binary_node<Record> *sub_tree = right_tree->left;
		switch (sub_tree->get_balance( )) {
		case equal_height:
			sub_root->set_balance(equal_height);
			right_tree->set_balance(equal_height); 
			break;
		case left_higher:
			sub_root->set_balance(equal_height);
			right_tree->set_balance(right_higher); 
			break;

right_balance2

*

数据结构与程序设计

*

case right_higher:
			sub_root->set_balance(left_higher);
			right_tree->set_balance(equal_height); 
			break;
		} 
		sub_tree->set_balance(equal_height);
		rotate_right(right_tree);
		rotate_left(sub_root); 
		shorter = true;
		break;
	} 
	return shorter;
}

right_balance2

*

数据结构与程序设计

*

left_balance2请上机完成

template <class Record>
bool AVL_tree<Record> :: left_balance2(Binary_node<Record> * &sub_root)
/* Pre: sub root points to a subtree of an AVL tree , doubly unbalanced on the left.
Post: The AVL properties have been restored to the subtree.
Uses: Methods of struct AVL node ; functions rotate_right ,rotate_left . */
{

*

数据结构与程序设计

*

Main -- Book P487

void main(){
	AVL_tree<Record> mytree;
	mytree.insert(Record(13));
	mytree.insert(Record(5));
	mytree.insert(Record(16));
	mytree.insert(Record(3));
	mytree.insert(Record(10));
	mytree.insert(Record(14));
	mytree.insert(Record(18));
	mytree.insert(Record(2));
	mytree.insert(Record(4));
	mytree.insert(Record(8));
	mytree.insert(Record(11));
	mytree.insert(Record(15));
	mytree.insert(Record(17));
	mytree.insert(Record(20));
	mytree.insert(Record(1));
	mytree.insert(Record(7));
	mytree.insert(Record(9));
	mytree.insert(Record(12));
	mytree.insert(Record(19));
	mytree.insert(Record(6));

*

数据结构与程序设计

*

Main -- Book P487

cout<<"Preorder:"<<endl;
	mytree.preorder(print);
	cout<<endl;
	cout<<"inorder:"<<endl;
	mytree.inorder(print);
	cout<<endl;
	cout<<"Postorder:"<<endl;
	mytree.postorder(print);
	cout<<endl<<endl;

*

数据结构与程序设计

*

Result

Preorder:
13  5  3  2  1  4  10  8  7  6  9  11  12  16  14  15  18  17  20  19
inorder:
1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20
Postorder:
1  2  4  3  6  7  9  8  12  11  10  5  15  14  17  19  20  18  16  13

*

数据结构与程序设计

*

Main -- Book P487

Record tmp(16);
	mytree.remove(tmp);
	cout<<"Preorder:"<<endl;
	mytree.preorder(print);
	cout<<endl;
	cout<<"inorder:"<<endl;
	mytree.inorder(print);
	cout<<endl;
	cout<<"Postorder:"<<endl;
	mytree.postorder(print);
	cout<<endl<<endl;

	cout<<tmp.the_key();
	cin.get();

}

*

数据结构与程序设计

*

Result

Preorder:
10  5  3  2  1  4  8  7  6  9  13  11  12  18  15  14  17  20  19
inorder:
1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  17  18  19  20
Postorder:
1  2  4  3  6  7  9  8  5  12  11  14  17  15  19  20  18  13  10

15

*

数据结构与程序设计

*

课后作业

请用作业本完成
P489 页 E2 
（b），（f）

*

数据结构与程序设计

*

上机作业

请上机完成AVL树的插入和删除操作。

*

*

*

*

*

*

*

*

*

*

*

*

*

*

*

*

*

*

*

*

*

*

*

递归的方法讲解平衡因子修改的过程。

*

*

*

该段代码，在sub_root的左子树插入一个节点。avl_insert(sub_root->left, new_data, taller); 
if (taller == true) //如果taller为真，代表sub_root的左子树高度增加。

switch (sub_root->get_balance( ))//分析当sub_root的左子树高度增加时，对sub_root节点平衡因子的影响。

*

*

这段代码，在sub_root的右子树插入一个节点。avl_insert(sub_root->left, new_data, taller); 
if (taller == true) //如果taller为真，代表插入操作之后sub_root的右子树高度增加。

switch (sub_root->get_balance( ))//分析当sub_root的右子树高度增加时，对sub_root节点平衡因子的影响。

*

*

*

*

*

*

*

*

*

*

*

*

*

递归的方法讲解平衡因子修改的过程。

*

*

*

*

*

*

*

*

*

*

*

*

*

*

*

*

*

*

*

*

*

*

*

*

*

*

*

*

*

*

*

*

*

*

*

*
```
