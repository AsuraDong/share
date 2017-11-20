[toc]
> 对于简单的运算符，可以参考之前的博文。之后会有一篇关于从等号运算符重载的角度研究深浅拷贝的博文。<br>这里是讲：**逗号，取成员运算符，输入输出运算符，下标运算符，括号，new和delete**的重载。

## 逗号运算符重载
> 逗号运算符重载需要一个参数，并且返回自身类。逗号运算符在复制操作中比较常见，下面就是以赋值操作为例的逗号运算符重载。

```c++
#include<string>
#include<iostream>
using namespace std;
class Tem{
	private:
		int x;
	public:
		Tem(int);
		Tem operator ,(Tem);
		void display();
}; 

Tem::Tem(int xx=0){
	x = xx;
}

Tem Tem::operator , (Tem t){
	cout<<t.x<<endl;
	return Tem(t.x);
}
void Tem::display(){
	cout<<"Class(Tem) includes of: "<<x<<endl;
}

int main(){
	
	Tem tem1(10);
	Tem tem2(20);
	Tem other = (tem1,tem2); //会选择第二个 int a= 1,2;a等于2而不是1 
	other.display();
	
	return 0;
}
```

***

## 取成员运算符重载
> 返回类类型的指针变量，符合平时的用法，这样就可以不用在声明变量时候使用指针，但是之后可以按照指针的方式调用，简单方便。

```c++
#include<iostream>
using namespace std;

class Tem{
	public:
		int n;
		float m;
		Tem* operator ->(){
			return this;
		}
}; 
int main(){
	Tem tem;
	tem->m = 10; //调用->运算符，返回Tem*类型并访问m 
	cout<<"tem.m is "<<tem.m<<endl;
	cout<<"tem->m is "<<tem->m<<endl;
	return 0;
}
```

***

## 输入输出运算符重载
> \>\>,<<运算符重载分别在cin、cout之后调用。我们需要用友元运算符对他们进行重载，注意返回类型分别是istream 和 ostream。

```c++
#include<iostream>
using namespace std;

class Date{
	private:
		int year,month,day;
	public:
		Date (int y,int m,int d){
			year = y;
			month = m;
			day  = d;
		}
		friend ostream& operator <<(ostream &stream,const Date &date){
			stream<<date.year<<" "<<date.month<<" "<<date.day<<endl;
			return stream;
		}
		friend istream& operator >>(istream &stream,Date &date){
			stream>>date.year>>date.month>>date.day;
			return stream;
		}
}; 
int main(){
	Date _date(2017,6,13);
	cout<<_date;
	cin>>_date;
	cout<<_date;
	return 0;
}
```

***

## 下标运算符重载
> 下标运算符只能被重载为类的非静态成员函数，不能重载为友元函数和普通函数。<br>
下标运算符只能有一个参数，多和数组有关，返回引用类型可以查看和修改数组元素。

```c++
#include<iostream>
#include<string>
using namespace std;

const int LEN = 3;

class Tem{
	private:
		int a[LEN];
	public:
		Tem(){
			for (int i=0;i<LEN;++i)
				a[i] = i;
		}
		int &operator [](int i){
			return a[i];
		} 
};

int main(){
	Tem tem;
	cout<<tem[1]<<endl;
	tem[1] = -1;//修改
	cout<<tem[1]<<endl;//重新查看 
	return 0;
}
```

***

## 括号运算符重载
>  括号运算符只能被重载为类的非静态成员函数。并且**参数个数和返回类型没有限制**。
> **所以我们可以实现很多脚本语言中或者string库里面的切片操作。**

```c++
#include<iostream>
#include<string>
using namespace std;

const int LEN = 10;

class Tem{
	private:
		int a[LEN];
	public:
		Tem(){
			for (int i=0;i<LEN;++i)
				a[i] = i;
		}
		int &operator [](int i){
			return a[i];
		} 
		int * operator ()(int start ,int end){ //用括号运算符实现切片操作 
			int *t = new int [end-start];
			for(int i=start;i<end;++i)
				t[i-start] = a[i];
			return t;
		}
};

int main(){
	Tem tem;
	
	int *arr = tem(0,5);
	for(int i=0;i<5;++i){
		cout<<arr[i]<<" ";
	}
	cout<<endl;

	
	return 0;
}
```

## new和delete运算符重载
> 注意new和delete重载的时候**参数的形式和返回类型**即可。

```c++
#include<iostream>
#include<cstddef>
using namespace std;

const int LEN = 10;
class Tem{
	private:
		int a[LEN];
	public:
		Tem(){
			for (int i=0;i<LEN;++i)
				a[i] = i;
		}
		void *operator new(size_t size); //开辟大小为size的空间 
		void *operator new(size_t size,char p); //开辟大小为size的空间，并且每个都赋值为p 
		void operator delete(void *p);
};
void * Tem::operator new(size_t size){//参数是无符号类型，在cstddef里，是c++里的unsigned
	cout<<"Create a place includes of "<<size<<" bytes\n";
	char  *s = new char[size];
	*s = 'a';
	return s;
}

void * Tem::operator new(size_t size,char p){ //返回类型是可以自动转化的指针类型
	cout<<"Create a place includes of "<<size<<" bytes\n";
	char  *s = new char[size];
	for(int i=0;i<size;i++)
		s[i] = p;
	return s;
}

void Tem::operator delete(void *p){
	cout<<"Delete \n";
	delete [] p; //最后释放空间 
}
int main(){
	Tem *tem = new Tem;
	delete tem;
	
	Tem *_tem = new('E') Tem;
	delete _tem;
	
	return 0;
}
```

