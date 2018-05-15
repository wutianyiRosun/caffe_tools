### 829. Consecutive Numbers Sum

Given a positive integer N, how many ways can we write it as a sum of consecutive positive integers?

Example 1:

Input: 5
Output: 2
Explanation: 5 = 5 = 2 + 3

```
#Solution： 对于连续n个数之和为N
#case 1: 1个数， 那就只有N本身
#case 2: 2个数， 1+k, 2+k, sum= 1+k+2+k =N, k为整数，即 (N-3)%2==0
#case 3: 3个数， 1+k, 2+k, 3+k, sum= 1+k+2+k+3+k, k为整数， 即(N-6)%3==0
#case i, i个数， 1+k, 2+k, ..., i+k , sum= 1+k+2+k+...+i+k, 即(N-(1+k+i+k)*i/2)==0 --> (N-(1+i)*i/2)%i==0
#时间复杂度: O(sqrt(N))
class Solution {
public:
    int consecutiveNumbersSum(int N) {
        int count=0;
        for(int i=1; (1+i)*i/2<=N; i++){
            if( (N-(1+i)*i/2)%i==0 )
                count++;
        }
        return count;   
    }
};
```

### 279. Perfect Squares
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.

```
//Solution: 动态规划求解，我们用nums[i]比表示和为i的the least number of perfect square numbers。则原问题就等价于求nums[n];
//对于任意一个数i,我们可以把它拆成i-j*j, j*j这两个数，此处j*j<=i;则nums[i]=nums[i-j*j]+1
//初始状态nums[0]=0

class Solution {
public:
    int numSquares(int n) {
        if(n<=0)
            return 0;
        vector<int> nums(n+1, INT_MAX);
        nums[0]=0;
        for(int i=1;i<=n;i++){
            for(int j=1;j*j<=i;j++){
                nums[i]= min(nums[i], nums[i-j*j]+1);
            }
        }
        return nums[n];
        
    }
};
```
