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
### 392. Is Subsequence
 Given a string s and a string t, check if s is subsequence of t.

You may assume that there is only lower case English letters in both s and t. t is potentially a very long (length ~= 500,000) string, and s is a short string (<=100).

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
s = "abc", t = "ahbgdc"

Return true.

Example 2:
s = "axc", t = "ahbgdc"

Return false. 
```
//对于s中的每个字符，我们去t中寻找，如果没找到直接返回false,如果找到，标记当前t中的位置，对于s中下一个字符，从该位置的下一个位置开始查找
class Solution {
public:
    bool isSubsequence(string s, string t) {
        if(s.size()==0)
            return true;
        if(t.size()==0)
            return false;
        int index_t=0;
        for(int i=0; i<s.size(); i++){
            bool flag=false;
            for( int j= index_t; j< t.size(); j++){
                if(t[j] == s[i]){
                    flag=true;
                    index_t= j+1;
                    break;
                }
            }
            if(flag==false)
                return false;
        }
        return true;
    }
};

```
