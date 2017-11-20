### 关于`vector`
> 由于笔者原来一直使用的是python，所以想在c++中找到类似于python中`list`的数据结构。后来发现`vector`用起来和python中的`list`还是很像的。如果没有什么特殊要求或者复杂度问题，笔者建议在做OJ题目的时候，尽量使用`vector`（Acm除外）。

### 方法和属性
| 方法和属性 | 代码 |
| - | -|
| 预留空间| `vector.reserve()` |
| 设定大小 | `vector.resize()` |
| 推入元素 | `vector.push_back()`|
| 弹出元素 | `vector.pop_back()`|
| 清空全部| `vector.clear()` |
| 头部和尾部| `vector.front()/back()` |
| 删除 | `vector.erase()`|
| 大小和容量 |`vector.size()/capacity()`|

### 一个demo
```c++
#include<iostream>
#include<vector> 
#include<algorithm>
using namespace std;
template<typename T>
void show(vector<T>vec);

int main(){
	vector<int> vec;
	cout<<"size is:"<<vec.size()<<" capacity is:"<<vec.capacity()<<endl;
	// 预留10个空间 ，没有初始化 
	vec.reserve(10);
	cout<<"size is:"<<vec.size()<<" capacity is:"<<vec.capacity()<<endl;
	show(vec);
	
	// 设置大小为10，每个位置初始化为0 
	vec.resize(10);
	cout<<"size is:"<<vec.size()<<" capacity is:"<<vec.capacity()<<endl;
	
//	cout<<"Debug\n";
//	show(vec);
//	vec[0] = 100;
//	show(vec);
	
	// 推入一个，所以目前大小为11>10，那么预留空间会自动增加一倍 
	vec.push_back(0);
	cout<<"size is:"<<vec.size()<<" capacity is:"<<vec.capacity()<<endl;
	
	// 清空vector 
	vec.clear();
	show(vec);

	// 数组头的引用
	cout<<"first is: "<<vec.front()<<endl;
	
	// pop和push最后一个 
	for(int i=0;i<10;)
		vec.push_back(++i);
	vec.pop_back();
	show(vec);
	
	// 反转vector 
	reverse(vec.begin(),vec.end());
	show(vec);
	
	vector<int>::iterator it = find(vec.begin(),vec.end(),8);
	if(it!=vec.end())
		cout<<"\nFind :"<<*it<<endl;
	else cout<<"\nNot found\n"; 
	
	// 连续删除元素 
	vec.erase(vec.begin(),vec.end()); 
	show(vec);
	
	return 0;
}

template<typename T>
void show(vector<T>vec) {
	cout<<endl;
	// 判断是否为空 
	if(!vec.empty()) { 
		for(int i=0;i<vec.size();++i) 
			cout<<"at "<<i<<" is "<<vec[i]<<endl;
		cout<<"Now size is "<<vec.size()<<" ";
		cout<<"Now capacity is "<<vec.capacity()<<endl<<endl;
	} else {
		cout<<"Vec is empty now\n\n";
	}
}
```