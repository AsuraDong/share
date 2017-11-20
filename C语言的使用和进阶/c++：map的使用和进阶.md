| 功能 | 实现 |
| - | - |
| 两种插入方法 | `make_pair()`/`pair<,>()`|
| 大小 | `map.size()`|
| 遍历 | `map<,>::iterator`|
|两种方法查找键值| `map<,>::const_iterator map.find()`/`map.count(key)`|
| 按照value查找|请自定义函数或者类|
| 交换 | `algorithm.swaq(,)`|
| 删除元素 | `map.erase()`,map,set都是关联容器,所以在使用的时候需要注意（具体读代码）|


```c++
#include<iostream>
#include<string>
#include<map>
#include<cstdlib>
#include<algorithm>
using namespace std;

int main(){
	map<int,string> dict;
	
	// 两种插入方法 
	dict.insert(make_pair(1,"AsuraDong"));
	dict.insert(pair<int,string>(0,"Vic"));
	dict[2] = "DongYuanxin";
	
	// 大小 
	cout<<"size is:"<<dict.size()<<endl;
	
	// 遍历
	map<int,string>::iterator it = dict.begin();
	while(it!=dict.end()) {
		cout<<"Key is: "<<it->first<<". Value is: "<<it->second<<"."<<endl;
		it++;
	} 
	
	// 查找键值
	// 注意，这里的iterator的名字不能和上面的重复 
	map<int,string>::const_iterator it2 = dict.find(2); 
	if(it2!=dict.end()) 
		cout<<"Find "<<it2->first<<endl;
	else 
		cout<<"Not found\n";
	// 通过计算key的值查找键值 
	cout<<"The times of the key is:"<<dict.count(100)<<endl; 
	
	// 查找value值
	// 请自己定义类或方法 
	
	// swap交换两个键值对 
	cout<<dict[1]<<" "<<dict[2]<<endl;
	swap(dict[1],dict[2]);
	cout<<dict[1]<<" "<<dict[2]<<endl;
	
	// erase删除(map,set都是关联容器) 
	// 如果某一个元素已经被删除，那么其对应的迭代器就失效了，不应该再被使用；
	// 否则会导致程序无定义的行为。
	map<int,string>::iterator it3 = dict.find(2);
	dict.erase(it3);
	cout<<"size is:(after erasing one elem)"<<dict.size()<<endl;
	map<int,string>::iterator _it;
	for(it=dict.begin();it!=dict.end();){
		// dict.erase(it++); // 不能跨平台，不推荐 
		// it = dict.erase(it); // 错误写法 
		_it = it;
		it++;
		dict.erase(_it);
		cout<<"Now size is:"<<dict.size()<<endl;
	}
	return 0;
} 
```