
**之前遇到一道题目，需要查找一个数组中出现次数最多的元素和次数，并且输出。第一次用struct模拟字典，十分麻烦而且复杂度是O(n\*n)。其实，运用转化的思想，可以先将其排序，然后再查找即可，时间复杂度之后只有O( n\*log_2(n))。**

题目是这样的：
> 某小镇要票选镇长，得票最高者当选。但由于投票机制不健全，导致每届投票时，候选人在投票系统的识别码类型不一致。请编写函数模板，能针对多种类型的数据，查找出得票最高的元素。其中，每届投票的选票有n张，识别码类型为T
注意：必须使用模板函数

输入：
```
3
I 10
5 3 5 2 9 7 3 7 2 3
C 8
a b a e b e e q
S 5
sandy david eason cindy cindy
```

输出：
```
3 3
e 3
cindy 2
```

#### 代码实现：算法在findMax函数实现
```c++
#include<iostream>
#include<string>
#include<algorithm> 
using namespace std;


template <class T>

void findMax(T* arr,int len){
	int j;	
	for(j=0;j<len;++j)
		cin>>arr[j];
	sort(arr,arr+len);
	int times=0 ,tem_times=1;
	T elem=arr[0] ;
	
	for(j = 1;j<len;++j)
		if(arr[j]==arr[j-1])
			tem_times++;
		else{
			if(tem_times>times){
				times = tem_times;
				elem = arr[j-1];
			}
			tem_times = 1;
		}
	if(tem_times>times){
		elem = arr[len-1];
		times = tem_times;
	}
	cout<<elem<<" "<<times<<endl;
}
	
	
int main(){
	int t,num;
	cin>>t;
	char type;
	while(t--){
		cin>>type;
		cin>>num;
		if(type=='I'){	
			int *arr = new int [num];
			findMax(arr,num);
		}
		else if(type=='S'){
			string *arr = new string [num];
			findMax(arr,num);
		}
		else if(type=='D'){
			double *arr = new double [num];
			findMax(arr,num);
		}
		else{
			char *arr = new char [num];
			findMax(arr,num);
		}
		
	}
	return 0;
}
```
