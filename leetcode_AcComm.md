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
