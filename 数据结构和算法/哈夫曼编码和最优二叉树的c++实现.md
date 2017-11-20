[toc]
> 赫夫曼树就是总加权路径最小的最优二叉树。课上学的时候，书上用的是数组和对应的下标来模拟最优二叉树的建立。但是，**`i,j,k`等乱七八糟的数组下标访问是很难控制的。**
所以，还是按照正常人的思路，**从下到上，一步步建立树的结构（而不是借助数组）**

oj题目如下（注意题目中是权值）：
```
输入

第一行输入t，表示有t个测试实例
第二行先输入n，表示第1个实例有n个权值，接着输入n个权值，权值全是小于1万的正整数
依此类推

输出

逐行输出每个权值对应的编码，格式如下：权值-编码
即每行先输出1个权值，再输出一个短划线，再输出对应编码，接着下一行输入下一个权值和编码。
以此类推

样例输入
1
5 15 4 4 3 2

样例输出
15-1
4-010
4-011
3-001
2-000
```

### 1. 建立树结构
- 开启一个`vector`，存入代表权值的节点。
- 每次取前出2个节点，生成新的节点，并将新的节点插入到`vector`中，再次排序。
- 重复执行前两步，知道最后只剩一个元素(`size==1`)

![最优二叉树](./image/哈夫曼编码和最优二叉树的c++实现/最优二叉树)

### 2. 输出编码
> 这里刚开始确实把我难住了，后来仔细一想，利用递归的思想可以很轻松的解决

- 准备好`root`根节点和一个代表路径的栈(`stack<int>path`)
- 每次递归前，需要检索当前节点的权重是否等于给定权重，如果是的话并且这个节点没有被访问过，就返回`true`，否则，返回`false`。
- 访问左节点，先向`path`推入代表左方向的`0`，递归调用，如果成功，就返回`true`；否则，说明下面的节点中没有对应权重，那么要从`path`中弹出代表左方向的`0`。
- 对右节点同样。
- 走到最后的话，肯定是没有得啦，就请`return false`。

**需要注意的是，在叶节点中，加入了一个`flag`标志，代表是否访问过。类似题目中有2个4，所以需要访问过需要标记一下，否则编码是相同的（在第二步实现的）**

### 3. 代码实现

```c++
#include<iostream>
#include<vector>
#include<stack>

using namespace std;

class HuffNode {
	public:
		int weight; // 这里的权重就是次数 
		HuffNode *lc,*rc;
		bool flag; // 叶节点是否访问过（针对权重一样的叶节点） 
		HuffNode(){
			this->flag = false;
		}
}; 

class HuffTree{
	private:
		vector<HuffNode *> all_node;
		void mySort(){ // 自定义排序（根据weight排序） 
			int i,j;
			int size =  all_node.size();
			for(j=0;j<size-1;++j) 
				for(i = 0;i<size-1-j;++i)
					if (all_node[i]->weight>=all_node[i+1]->weight)
						swap(all_node[i],all_node[i+1]);
		}
	public:
		HuffTree(int *arr,int size){ // 将输入输入all_node 
			for(int i=0;i<size;++i) {
				HuffNode* node = new HuffNode();
				node->weight = arr[i];
				node->lc = NULL; node->rc = NULL;
				all_node.push_back(node);
			}
		}
		HuffNode* getRoot(){ // 得到根节点 
			return all_node[0]; 
		} 
		void buildTree(){
			while(all_node.size()>=2) { // 构建最优二叉树 
				mySort();
				HuffNode *new_node = new HuffNode();
				new_node->lc = all_node[0];
				new_node->rc = all_node[1];
				new_node->weight = all_node[0]->weight+all_node[1]->weight;
				all_node.erase(all_node.begin(),all_node.begin()+2);
				all_node.insert(all_node.begin(),new_node);
			}
		}
		bool getPath(HuffNode *&root,stack<int>&path,const int weight) { // 修改对应的权重的编码（路径）path 
			if(!root ) return false; 
			if(root->weight == weight && !root->lc && !root->rc){ 
				if(root->flag==false){
					root->flag = true;
					return true;
				}
				return false;
			} 
			if(root->lc ) {
				path.push(0);
				if(getPath(root->lc,path,weight)) return true;
				path.pop();
			}
			if (root->rc) {
				path.push(1);
				if(getPath(root->rc,path,weight)) return true;
				path.pop();
			}
			
			return false;
		}
};
// 逆序输出栈 
void print(stack<int> path){
	if(path.size()!=0){
		int top = path.top();
		path.pop();
		print(path);
		cout<<top;	
	}
}
int main(){
	int t;
	cin>>t;
	int n;
	while(t--) {
		cin>>n;
		int *arr = new int [n];
		for(int i=0;i<n;++i)
			cin>>arr[i];
		HuffTree my_tree(arr,n); // 初始化 
		my_tree.buildTree(); // 创建树 
		HuffNode *root= my_tree.getRoot(); // 得到跟节点 
		
 		for(int i=0;i<n;++i){
 			stack<int> path;
 			my_tree.getPath(root,path,arr[i]);
 			cout<<arr[i]<<"-";
 			print(path);
 			cout<<endl; 
		 }

	}
	return 0;	
}
```