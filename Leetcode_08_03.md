### 813. Largest Sum of Averages


We partition a row of numbers A into at most K adjacent (non-empty) groups, then our score is the sum of the average of each group. What is the largest score we can achieve?

Note that our partition must use every number in A, and that scores are not necessarily integers.

Example:
Input: 
A = [9,1,2,3,9]
K = 3
Output: 20
Explanation: 
The best choice is to partition A into [9], [1, 2, 3], [9]. The answer is 9 + (1 + 2 + 3) / 3 + 9 = 20.
We could have also partitioned A into [9, 1], [2], [3, 9], for example.
That partition would lead to a score of 5 + 2 + 6 = 13, which is worse.

```
//动态规划求解，我们用dp[i][k]表示子序列A[0,...,i-1]分成k组其平均数之和的最大值
//我们记sum[i]表示序列A[0, i-1]之和
//则我们有如下dp 方程：   dp[i][k]= max_{j}( dp[j][k-1]+ 1.0*(sum[i]-sum[j])/(i-j+1)， where 0<j<i

class Solution {
public:
    double largestSumOfAverages(vector<int>& A, int K) {
        int len=A.size();
        vector<int> sum(len+1,0);
        for(int i=1; i<=len; i++){
            sum[i]=sum[i-1]+A[i-1];
        }
        if(K<=1)
            return 1.0*sum[len] / len;
        if(K>=len){
            return sum[len];
        }
        vector< vector<double> > dp(len+1 ,vector<double>(K+1, 0.0));
        for(int i=1; i<=len; i++)
            dp[i][1]=1.0*sum[i]/i;  //前i个元素分成1组的LSA,  
        for(int k=2; k<=K; k++){
            for(int i=0; i<=len; i++){
                for(int j=i-1; j>0; j--){
                    dp[i][k]= max(dp[i][k], dp[j][k-1]+1.0*(sum[i] - sum[j]) /(i-j));
                    //dp[i][k]表示子序列A[0,...,i-1]分成k组其平均数之和的最大值,枚举1<= j <= i-1, dp[j][k-1]+ average(A[i-1], ..., A[j])
                }
            }
        }
        return dp[len][K];
    }
};


```
