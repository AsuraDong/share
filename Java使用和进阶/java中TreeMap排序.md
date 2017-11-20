[toc]

## 1. 定义TreeMap的排序方法
> 1. 使用`Comparator`对象作为参数
> 2. 需要注意的是：**排序方法是针对键的，而不是值的。如果想针对值，需要更麻烦的一些方法（重写一些方法）**

```java
TreeMap<Screen,Integer> res = new TreeMap<Screen, Integer>(new Comparator<Screen>() {
            @Override
            public int compare(Screen screen1, Screen t1) { // 定义TreeMap的排序方法
                return screen1.compareTo(t1); // TreeMap的排序方法是：调用screen的比较方法
            }
        });
```

## 2. 定义里面的对象的比较方法
> 继承`Comparable`接口

```java
public class Screen implements Comparable{
    private double size,price;
    
    ...
    
    @Override
    public int compareTo(Object s){ // 定义比较方法
        Screen screen = (Screen)s;
        return this.price>screen.getPrice()?-1:1; // 返回负整数和正整数
    }
}
```

## 3. 所有代码
> 按照Screen的价钱排序

- `Screen.java`
    ```java
    import java.util.*;
    import java.lang.Integer;
    
    public class Screen implements Comparable{
        private double size,price;
        public Screen(){}
        public void setSize(double size){
            this.size = size;
        }
        public void setPrice(double price){
            this.price = price;
        }
        public double getSize(){ return this.size;}
        public double getPrice() { return this.price;}
        public void show(){
            System.out.println("size is: "+this.size+"; price is: "+this.price);
        }
        @Override
        public int compareTo(Object s){ // 定义比较方法
            Screen screen = (Screen)s;
            return this.price>screen.getPrice()?-1:1; // 返回负整数和正整数
        }
    }
    ```
- `TestScreen.java`
    ```java
    import java.util.Comparator;
    import java.util.Scanner;
    import java.util.TreeMap;
    import problem2.Screen;
    
    public class TestScreen {
        final static int MAX_NUM = 8;
        public static void main(String []args){
            TreeMap<Screen,Integer> res = new TreeMap<Screen, Integer>(new Comparator<Screen>() {
                @Override
                public int compare(Screen screen1, Screen t1) { // 定义TreeMap的排序方法
                    return screen1.compareTo(t1); // TreeMap的排序方法是：调用screen的比较方法
                }
            });
            double price, size;
            Scanner scan = new Scanner(System.in);
            for(int i=0;i<MAX_NUM;++i){
                Screen screen = new Screen();
                size = scan.nextDouble();
                price = scan.nextDouble();
                screen.setSize(size);
                screen.setPrice(price);
                res.put(screen,i);
            }
            for(Screen screen:res.keySet()){
                screen.show();
            }
            return ;
        }
    }
    //        测试样例（输入）
    //        1 2
    //        3 4
    //        5 6
    //        7 8
    //        9 10
    //        1 2
    //        3 4
    //        3 4
    ```