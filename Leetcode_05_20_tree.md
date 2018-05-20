### 365. Water and Jug Problem

You are given two jugs with capacities x and y litres. There is an infinite amount of water supply available. You need to determine whether it is possible to measure exactly z litres using these two jugs.

If z liters of water is measurable, you must have z liters of water contained within one or both buckets by the end.

Operations allowed:

Fill any of the jugs completely with water.
Empty any of the jugs.
Pour water from one jug into another till the other jug is completely full or the first jug itself is empty.
Example 1: (From the famous "Die Hard" example)

Input: x = 3, y = 5, z = 4
Output: True
```
//可以测量z的条件是， x和y的最大公约数不为0，且该最大公约数是z的一个因数
class Solution {
public:
   
    int gcd(int x, int y)//辗转相除法求最大公约数
    { 
       int max_v=max(x,y);
       int min_v=min(x,y);
       if(min_v==0)
           return 0;
       if(max_v%min_v==0)
           return min_v;
       else
           return gcd(min_v, max_v%min_v);
    }
    bool canMeasureWater(int x, int y, int z) {
        if(!gcd(x,y))return z == 0;
        return (x + y >= z) && (z % gcd(x,y)) == 0;
    }
};
```

### 397. Integer Replacement
Given a positive integer n and you can do operations as follow:

If n is even, replace n with n/2.
If n is odd, you can replace n with either n + 1 or n - 1.
What is the minimum number of replacements needed for n to become 1?

Example 1:

Input:
8

Output:
3

Explanation:
8 -> 4 -> 2 -> 1

```
//我们做一下贪心算法，当n为偶数时，我们以n/2替代
//当n为奇数时，分两种情况
//case1: 当(n+1)/2为偶数时，则以n+1替代n
//case2: 当(n-1)/2为偶数时，则以n-1替代n
//我们可以证明对于任意一个奇数n,  (n+1)/2 + (n-1)/2中必然有一个为奇数，一个为偶数；
//证明，我们用反证法，对于上面假设不成立，即二者之和(n+1)/2 + (n-1)/2 == 2k为偶数(两个偶数相加， 两个基数相加)--->n=2k,推出n为偶数矛盾
//特殊输入 1，2，3, INT_MAX
class Solution {
public:
    int integerReplacement(int n) {
        if(n==1) return 0;
        if(n==2) return 1;
        if(n==3) return 2;
        if (n == INT_MAX) return 32; 
        if(n%2==0){
           return 1+integerReplacement(n/2);  
        }
        else if( (n+1)%4==0){//n为奇数，且(n+1)/2为偶数
            return 1+integerReplacement(n+1); 
        }
        else //n为奇数，且(n-1)/2为偶数
            return 1+integerReplacement(n-1); 
    }
   
};
```
