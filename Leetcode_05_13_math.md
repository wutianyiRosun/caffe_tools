### 754. Reach a Number

 You are standing at position 0 on an infinite number line. There is a goal at position target.

On each move, you can either go left or right. During the n-th move (starting from 1), you take n steps.

Return the minimum number of steps required to reach the destination.

Example 1:

Input: target = 3
Output: 2
Explanation:
On the first move we step from 0 to 1.
On the second step we step from 1 to 3.

```
//Solution: 首先对于target为负数的情况，最小步数应该等同于正数
//我们先一直朝右走，知道所走步数之和不小与target.当sum-target大于0时，则意味着我们在某个步骤需要往左走，假设为第i步，这时和相当于少
//了2×i(本来是sum=sum+i, 我们向左走sum=sum-i),因此当差异为偶数时，则返回步数，如果不为偶数则一直加直到为偶数
class Solution {
public:
    int reachNumber(int target) {
        target= abs(target);
        int sum=0;
        int count=0;
        while(sum<target){
            count++;
            sum+=count;
        }
        while( (sum-target)%2!=0){
            count++;
            sum+=count;
        }
        return count;
    }
};

```
### 29. Divide Two Integers
Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero.

Example 1:

Input: dividend = 10, divisor = 3
Output: 3

```
class Solution {
public:
    int divide(int dividend, int divisor) {
         if (!divisor || (dividend == INT_MIN && divisor == -1))
            return INT_MAX;
        int sign = ((dividend < 0) ^ (divisor < 0)) ? -1 : 1;  //异或 两数同号取1 不同号取-1 
        long long dividend1 = labs(dividend);
        long long divisor1 = labs(divisor);
        
        int sumcount=0;
       
        while( dividend1 >=divisor1){
            long long temp = divisor1, count=1;
            while(dividend1>=(temp<<1)){
                temp = temp<<1;
                count = count<<1;
            }
            dividend1 -= temp;
            sumcount+=count;
        }
       
        return sign==1 ?  sumcount: -1*sumcount;
    }
};
```
