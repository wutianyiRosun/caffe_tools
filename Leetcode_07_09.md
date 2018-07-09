### 69. Sqrt(x)
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:

Input: 4
Output: 2

Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since 
             the decimal part is truncated, 2 is returned.
             
```
//二分法求解
class Solution {
public:
    int mySqrt(int x) {
        int ans;
        if(x==0) return 0;
        int start=1, end=x;
        while(start<=end){
            int mid=(start+end)/2;
            if(mid<=x/mid){
                start=mid+1;
                ans=mid;
            }
            else{
                end=mid-1;
            }
        }
        return ans;
        
    }
};

```

