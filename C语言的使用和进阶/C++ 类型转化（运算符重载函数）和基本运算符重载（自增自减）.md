[toc]

## 类型转化（运算符重载函数）
> 用转换构造函数可以将一个指定类型的数据转换为类的对象。但是不能反过来将一个类的对象转换为一个其他类型的数据(例如将一个Complex类对象转换成double类型数据)。在C++提供类型转换函数(type conversion function)来解决这个问题。类型转换函数的作用是将一个类的对象转换成另一类型的数据。

类型转换函数的一般形式为：
```c++
operator 类型名( ){
	实现转换的语句
}
```
下面是简单实现。这时候，Base起了两方面的作用：类和数据类型。系统会在需要的时候自动调用对应的类方法。
```c++
#include <iostream>
using namespace std;

class Base{
	private:
		float  x;
		int y;
	public:
		Base (float xx=0,int yy=0){
			x = xx;
			y = yy;
		}
		operator float (){
			return x;
		}
		operator int (){
			return y;
		}
		void display(){
			cout<<"x is :"<<x<<";y is :"<<y<<endl;
		}
};

int main()
{
	Base base(1.0,2);
	base.display();
	int y= base;
	float x= base;
	cout<<"NewX is :"<<x<<"NewY is:"<<y<<endl;
    return 0;
}
```

***

## 基本运算符重载（自增自减）
> 主要总结 自增自减的前置和后置的用法。其他的加减乘除较简单。

简单的代码实现（纯语法）
```c++
#include <iostream>
using namespace std;

class Base{
	private:
		float  x;
		int y;
	public:
		Base (float xx=0,int yy=0){
			x = xx;
			y = yy;
		}
		operator float (){
			return x;
		}
		operator int (){
			return y;
		}
		Base operator ++(){//前置 ++
			x++;
			y++;
			return *this;
		} 
		Base operator --(){
			x--;
			y--;
			return *this;
		}
		Base operator ++(int ){//后置 ++
			Base temp = *this;
			++(*this);
			return temp;
		}
		Base operator --(int ){
			Base temp = *this;
			--(*this);
			return temp;
		}
		void display(){
			cout<<"x is :"<<x<<";y is :"<<y<<endl;
		}
		
};

int main()
{
	Base base(1.0,1);
	Base tem = base++;
	base.display();
	tem.display(); 
	
	Base base2(1.0,1);
	tem = ++base2;
	base.display();
	tem.display(); 
    return 0;
}
```
发现：
1. 后置和前置的区别是有无int参数。
2. 后置需要申请新的空间，大小是类的大小。所以，后置操作会有额外的时间空间开销。
3. 尽量使用前置操作：如：`for (int i=0;i<n;++i)` 

