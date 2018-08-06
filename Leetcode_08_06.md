### 313. Super Ugly Number
Write a program to find the nth super ugly number.

Super ugly numbers are positive numbers whose all prime factors are in the given prime list primes of size k.

Example:

Input: n = 12, primes = [2,7,13,19]
Output: 32 
Explanation: [1,2,4,7,8,13,14,16,19,26,28,32] is the sequence of the first 12 
             super ugly numbers given primes = [2,7,13,19] of size 4.
 
 ```
 //Solution1: 就是枚举1到N中所有的数字，然后判断每个数字是否为UglyNumber
//Solution2: 用空间换时间，假设数组res[i]中已经右排好序的几个UglyNumber，当前最大值为M,那接下来这个UglyNumber
//肯定是前面某一个丑数乘以primes里面的每个元素，取最小的,因此我们可以把primes[i]与结果数组res的所有元素相乘得到第一个大于M的值， 记为M_i, 
//这样我们取所有M_i中的最小的数作为M的下一个丑数。 但这个过程中会有冗余，每次都重复计算了很多小于M的丑数， 因此我们要为每个Primes[i]标记它下一次重哪个丑数开始乘，使得Primes[i]*(* T[i]) >M, 
class Solution {
public:
    int nthSuperUglyNumber(int n, vector<int>& primes) {
        //int * res = new int[n];
        int res[n];
        res[0]=1;
        vector<int*> T(primes.size(), res);
        int nextUglyIndex=1;
        while(nextUglyIndex < n){
            int min_value = min_primes(primes, T);
            res[nextUglyIndex]=min_value;
            for(int i=0; i<T.size(); i++){
                while((*T[i])*primes[i] <= min_value)
                    ++T[i];
            }
            nextUglyIndex++;
        }
        return res[n-1];
    }
    
    int min_primes(vector<int> & primes, vector<int* > & T){
        int res=INT_MAX;
        for(int i=0; i<primes.size(); i++){
            res= min(res, primes[i] * (*T[i]));
        }
        return res;
    }
};
```
