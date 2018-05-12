### 1.c++中memset()
头文件： <string.h>  或 <memory.h>

函数原型： void *memset(void *s , int ch , size_t  n )

memset(结构体/数组名 , 用于替换的ASCII码对应字符 , 前n个字符 );

memset(结构体/数组名 , "用于替换的字符“ , 前n个字符 );

函数作用：在一段内存块中填充某一个给定的值，常用于较大的对结构体和数组的清零操作
