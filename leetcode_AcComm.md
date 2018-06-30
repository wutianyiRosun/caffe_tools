### 1.c++中memset()
头文件： <string.h>  或 <memory.h>

函数原型： void *memset(void *s , int ch , size_t  n )

memset(结构体/数组名 , 用于替换的ASCII码对应字符 , 前n个字符 );

memset(结构体/数组名 , "用于替换的字符“ , 前n个字符 );

函数作用：在一段内存块中填充某一个给定的值，常用于较大的对结构体和数组的清零操作

### 2.c++中atoi函数
1、atoi函数把字符串转换成整型数。其含义是ASCII to integer 的缩写.

### 3.C++中的c_str()函数用法
1 const char *c_str()

c_str()函数返回一个指向正规C字符串的指针常量, 内容与本string串相同。
这是为了与c语言兼容，在c语言中没有string类型，故必须通过string类对象的成员函数c_str()把string 对象转换成c中的字符串样式。


### 4. lower_bound()和upper_bound()函数

STL中关于二分查找的函数有三个lower_bound 、upper_bound 、binary_search 。这三个函数都运用于有序区间（当然这也是运用二分查找的前提），下面记录一下这两个函数。

ForwardIter lower_bound(ForwardIter first, ForwardIter last,const _Tp& val)算法返回一个非递减序列[first, last)中的第一个大于等于值val的位。
特殊情况：
1.如果m在区间中没有出现过，那么返回第一个比m大的数的下标。
2.如果m比所有区间内的数都大，那么返回r。这个时候会越界，小心。
3.如果区间内有多个相同的m，返回第一个m的下标。
时间复杂度：
一次查询O(log n)，n为数组长度。


ForwardIter upper_bound(ForwardIter first, ForwardIter last, const _Tp& val)算法返回一个非递减序列[first, last)中的第一个大于值val的位置。

### 5. 静态库(.a)和动态库(.so)
1、静态函数库

这类库的名字一般是libxxx.a；利用静态函数库编译成的文件比较大--空间，因为整个函数库的所有数据都会被整合进目标代码中，他的优点就显而易见了，即编译后的执行程序不需要外部的函数库支持，因为所有使用的函数都已经被编译进去了。当然这也会成为他的缺点，因为如果静态函数库改变了，那么你的程序必须重新编译。
```
//pr1.c、pr2.c 和 main.c
$ gcc -O -c pr1.c pr2.c //编译pr1.c、pr2.c 文件, 生成pr1.o和pr2.o文件
$ ar -rsv libpr.a pr1.o pr2.o  //链接静态库,为了在编译程序中正确找到库文件，静态库必须按照 lib[name].a 的规则命名，如下例中[name]=pr
$ gcc -o main main.c -L./ -lpr     // 生成main, -L 加载库文件路径，-l 指明库文件名字
$ ./main    //执行目标程序
```
2、动态函数库

这类库的名字一般是libxxx.so；相对于静态函数库，动态函数库在编译的时候并没有被编译进目标代码中，你的程序执行到相关函数时才调用该函数库里的相应函数，因此动态函数库所产生的可执行文件比较小。由于函数库没有被整合进你的程序，而是程序运行时动态的申请并调用--时间，所以程序的运行环境中必须提供相应的库。动态函数库的改变并不影响你的程序，所以动态函数库的升级/更新比较方便。

#### linux动态库的命名规则

动态链接库的名字形式为 libxxx.so，前缀是lib，后缀名为“.so”。

针对于实际库文件，每个共享库都有个特殊的名字“soname”。在程序启动后，程序通过这个名字来告诉动态加载器该载入哪个共享库。

在文件系统中，soname仅是一个链接到实际动态库的链接。对于动态库而言，每个库实际上都有另一个名字给编译器来用。它是一个指向实际库镜像文件的链接文件（lib+soname+.so)
```
//编写四则运算动态库代码, DynamicMath.h DynamicMath.cpp
$ g++ -fPIC -c DynamicMath.cpp  //生成目标文件，此时要加编译器选项-fpic, -fPIC 创建与地址无关的编译程序（pic，position independent code），是为了能够在多个应用程序间共享
$ g++ -shared -o libdynmath.so DynamicMath.o //然后，生成动态库，此时要加链接器选项-shared, -shared指定生成动态链接库
```
### 6. c++中map<,> 的常用操作

声明 map<int,int> data

插入 data.insert(pair<int,int>(key, value)) or data[key]=value

查找 auto it=data.find(key)

遍历 auto it= dataa.begin()  while(it!=data.end()){}


### 7.　进程间通信目的
1）数据传输：一个进程需要将它的数据发送给另一个进程，发送的数据量在一个字节到几兆字节之间。
2）共享数据：多个进程想要操作共享数据，一个进程对共享数据的修改，别的进程应该立刻看到。
3）通知事件：一个进程需要向另一个或一组进程发送消息，通知它（它们）发生了某种事件（如进程终止时要通知父进程）。
4）资源共享：多个进程之间共享同样的资源。为了作到这一点，需要内核提供锁和同步机制。
5）进程控制：有些进程希望完全控制另一个进程的执行（如Debug进程），此时控制进程希望能够拦截另一个进程的所有陷入和异常，并能够及时知道它的状态改变。
进程通过与内核及其它进程之间的互相通信来协调它们的行为。Linux支持多种进程间通信（IPC）机制，信号和管道是其中的两种。除此之外，Linux还支持System V 的IPC机制（用首次出现的Unix版本命名）。
