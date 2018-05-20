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
