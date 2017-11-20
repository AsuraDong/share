## 1. 队列
> 这里只记录STL中的单向队列（`deque`）
> 由于实现原理，**`stack`和`queue`都无法遍历**，可以考虑使用`vector`或`list`
### 1.1 方法和属性
| 方法属性 | 代码 |
| - |-|
|插入元素 |  `deque.push()` |
|弹出元素 |  `deque.pop()` |
|取出队首元素 |  `deque.front()` |
|取出队末元素 |  `deque.back()` |



### 1.2 示例代码
```c++
#include<iostream>
#include<queue>
#include<algorithm>
using namespace std;

template<typename T>
void show(queue<T>); // queue链表实现，无法遍历 

int main(){
	queue<int> que;
	// 插入push
	for(int i=0;i<10;)
		que.push(++i);
	
	// 弹出pop
	que.pop();
	
	// 队首元素front
	cout<<que.front()<<endl;
	
	// 队末元素back
	cout<<que.back()<<endl;
	
	if(!que.empty())
		cout<<que.size()<<endl;
	
	return 0;
}
```


## 2. 栈
> 方法和属性**基本与`queue`相同**。常用的不同的一个地方是：
> 访问栈顶元素的时候使用`top()`，而不是队列中的`front()`关键字。
> 由于实现原理，**`stack`和`queue`都无法遍历**，可以考虑使用`vector`或`list`

```c++
#include<iostream>
#include<stack>
using namespace std;
// 类似queue，无法遍历。如果要遍历，请用list
 
int main(){
	stack<int> s;
	for(int i=0;i<10;i++)
		s.push(i+1);
	cout<<"Size is "<<s.size()<<endl;
	
	while(!s.empty()){
		cout<<s.top()<<" ";
		s.pop();
	}
	
	return 0;
}
```