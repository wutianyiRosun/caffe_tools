今天的三道题53,70,746都是关于动态规划的，53求序列子序列最大和，在构造原问题与子问题的联系不是非常容易想到。

### 53. Maximum Subarray
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.
```
//Time complexity: O(N), Space complexity:O(N)
//对于动态规划，我们要做的是把原问题与子问题的解的形式给联系起来
//很直观的一个设想，子序列最大和为A[i,..,j],但原问题的形式是A[1,...,n],无法联系起来
//因此设想假如我们知道A[1,...,n-1]的子序列最大和，记为dp[n-1]，那原问题的解有如下形式
//dp[n]=A[n]+(dp[n-1]>0?dp[n-1]:0)
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
       int len=nums.size();
       int dp[len];//dp[i]表示序列到第i个元素为止的最大和
       dp[0]=nums[0];
       int max=dp[0];
       for(int i=1;i<nums.size();i++){
           dp[i]=nums[i]+(dp[i-1]>0?dp[i-1]:0);
           if(dp[i]>max)
               max=dp[i];
       }
       return max;
    }
};
```

### 70. Climbing Stairs
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output:  2
Explanation:  There are two ways to climb to the top.

1. 1 step + 1 step
2. 2 steps

```
//Time complexity: O(N); Space complexity: O(1)
//假设当前还差一步就到第n个阶梯了，两种情况，第一种情况是只需跨一个台阶就到，第二中情况需要跨跨两个台阶
//OPT[n]=OPT[n-1]+OPT[n-2]
class Solution {
public:
    int climbStairs(int n) {
        if(n==1)
            return 1;
        if(n==2)
            return 2;
        int pre=1,sec=2;
        int res;
        for(int i=3;i<=n;i++){
            res=pre+sec;
            pre=sec;
            sec=res;
        }
        return res;   
    }
};
```

### 746. Min Cost Climbing Stairs

On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).

Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the floor, and you can either start from the step with index 0, or the step with index 1.

Example 1:
Input: cost = [10, 15, 20]
Output: 15
Explanation: Cheapest is start on cost[1], pay that cost and go to the top.
```
class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        int n=(int)cost.size();
        vector<int> dp(n);
        dp[0]=cost[0];
        dp[1]=cost[1];
        for (int i=2; i<n; ++i)
            dp[i]=cost[i]+min(dp[i-2],dp[i-1]);
        return min(dp[n-2],dp[n-1]);
    }
};
```
